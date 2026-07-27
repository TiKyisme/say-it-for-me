from __future__ import annotations

import json
from collections.abc import Callable, Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import TypeVar

from .schema import (
    EvaluationDataError,
    Prediction,
    ReferenceExample,
    ReviewStatus,
)


Record = TypeVar("Record")


class _DuplicateJsonKey(ValueError):
    pass


def _object_without_duplicate_keys(
    pairs: list[tuple[str, object]],
) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise _DuplicateJsonKey(key)
        result[key] = value
    return result


def _reject_non_finite_number(value: str) -> object:
    raise ValueError(f"non-finite JSON number {value!r} is not allowed")


def _load_jsonl(
    path: str | Path,
    *,
    record_name: str,
    factory: Callable[[object], Record],
) -> tuple[Record, ...]:
    source_path = Path(path)
    records: list[Record] = []
    try:
        with source_path.open("r", encoding="utf-8") as handle:
            for line_number, raw_line in enumerate(handle, start=1):
                if not raw_line.strip():
                    raise EvaluationDataError(
                        "BLANK_JSONL_LINE",
                        f"{record_name} JSONL must not contain blank lines",
                        path=source_path,
                        line=line_number,
                    )
                try:
                    raw_record = json.loads(
                        raw_line,
                        object_pairs_hook=_object_without_duplicate_keys,
                        parse_constant=_reject_non_finite_number,
                    )
                except _DuplicateJsonKey as exc:
                    raise EvaluationDataError(
                        "DUPLICATE_JSON_KEY",
                        f"duplicate JSON key {str(exc)!r}",
                        path=source_path,
                        line=line_number,
                    ) from exc
                except (json.JSONDecodeError, ValueError) as exc:
                    raise EvaluationDataError(
                        "INVALID_JSON",
                        f"invalid JSON: {exc}",
                        path=source_path,
                        line=line_number,
                    ) from exc
                try:
                    records.append(factory(raw_record))
                except EvaluationDataError as exc:
                    raise exc.at(source_path, line_number) from exc
    except EvaluationDataError:
        raise
    except (OSError, UnicodeError) as exc:
        raise EvaluationDataError(
            "JSONL_READ_ERROR",
            f"cannot read {record_name} JSONL: {exc}",
            path=source_path,
        ) from exc

    if not records:
        raise EvaluationDataError(
            "EMPTY_JSONL",
            f"{record_name} JSONL must contain at least one record",
            path=source_path,
        )
    return tuple(records)


def _reject_duplicate_ids(
    records: Iterable[ReferenceExample | Prediction],
    *,
    record_name: str,
) -> None:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for record in records:
        if record.id in seen:
            duplicates.add(record.id)
        seen.add(record.id)
    if duplicates:
        raise EvaluationDataError(
            f"DUPLICATE_{record_name.upper()}_ID",
            f"duplicate {record_name} IDs: {', '.join(sorted(duplicates))}",
            field="id",
        )


def load_references(path: str | Path) -> tuple[ReferenceExample, ...]:
    references = _load_jsonl(
        path,
        record_name="reference",
        factory=ReferenceExample.from_mapping,
    )
    _reject_duplicate_ids(references, record_name="reference")
    return references


def load_predictions(path: str | Path) -> tuple[Prediction, ...]:
    predictions = _load_jsonl(
        path,
        record_name="prediction",
        factory=Prediction.from_mapping,
    )
    _reject_duplicate_ids(predictions, record_name="prediction")
    return predictions


@dataclass(frozen=True, slots=True)
class EvaluationPair:
    reference: ReferenceExample
    prediction: Prediction

    def __post_init__(self) -> None:
        if self.reference.id != self.prediction.id:
            raise ValueError("reference and prediction IDs must match")


def join_predictions(
    references: Iterable[ReferenceExample],
    predictions: Iterable[Prediction],
) -> tuple[EvaluationPair, ...]:
    """Join by ID while requiring exact, one-to-one dataset coverage."""

    reference_records = tuple(references)
    prediction_records = tuple(predictions)
    _reject_duplicate_ids(reference_records, record_name="reference")
    _reject_duplicate_ids(prediction_records, record_name="prediction")

    reference_ids = {record.id for record in reference_records}
    prediction_by_id = {record.id: record for record in prediction_records}
    prediction_ids = set(prediction_by_id)

    missing = sorted(reference_ids - prediction_ids)
    if missing:
        raise EvaluationDataError(
            "MISSING_PREDICTIONS",
            f"missing predictions for IDs: {', '.join(missing)}",
            field="id",
        )

    unknown = sorted(prediction_ids - reference_ids)
    if unknown:
        raise EvaluationDataError(
            "UNKNOWN_PREDICTIONS",
            f"prediction IDs are not in the reference set: {', '.join(unknown)}",
            field="id",
        )

    return tuple(
        EvaluationPair(reference, prediction_by_id[reference.id])
        for reference in reference_records
    )


@dataclass(frozen=True, slots=True)
class EvaluationSelection:
    included: tuple[EvaluationPair, ...]
    excluded: tuple[EvaluationPair, ...]
    policy: str

    def to_dict(self) -> dict[str, object]:
        return {
            "policy": self.policy,
            "included_ids": [pair.reference.id for pair in self.included],
            "excluded": [
                {
                    "id": pair.reference.id,
                    "review_status": pair.reference.review_status.value,
                }
                for pair in self.excluded
            ],
        }


def select_evaluation_pairs(
    pairs: Iterable[EvaluationPair],
    *,
    include_non_approved: bool = False,
) -> EvaluationSelection:
    """Apply the official-reference inclusion policy.

    ``approved`` is the dataset-owner state confirming reference quality,
    provenance, and license compatibility. Other states remain diagnostic only.
    """

    records = tuple(pairs)
    if include_non_approved:
        return EvaluationSelection(records, (), "all_records_diagnostic")

    included = tuple(
        pair
        for pair in records
        if pair.reference.review_status is ReviewStatus.APPROVED
    )
    excluded = tuple(
        pair
        for pair in records
        if pair.reference.review_status is not ReviewStatus.APPROVED
    )
    if not included:
        raise EvaluationDataError(
            "NO_APPROVED_REFERENCES",
            "official evaluation requires at least one record with "
            "review_status='approved'; use --include-non-approved for a "
            "diagnostic-only report",
            field="review_status",
        )
    return EvaluationSelection(included, excluded, "approved_only")
