from __future__ import annotations

import importlib
import unicodedata
from collections import Counter, defaultdict
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any

from .dataset import EvaluationPair, select_evaluation_pairs


def normalize_for_error_rate(text: str) -> str:
    """Apply the minimal, language-neutral normalization used by CER/WER."""

    return " ".join(unicodedata.normalize("NFC", text).split())


def _levenshtein_distance(
    reference: Sequence[str],
    hypothesis: Sequence[str],
) -> int:
    if len(reference) < len(hypothesis):
        reference, hypothesis = hypothesis, reference

    previous = list(range(len(hypothesis) + 1))
    for row, reference_unit in enumerate(reference, start=1):
        current = [row]
        for column, hypothesis_unit in enumerate(hypothesis, start=1):
            substitution_cost = int(reference_unit != hypothesis_unit)
            current.append(
                min(
                    previous[column] + 1,
                    current[column - 1] + 1,
                    previous[column - 1] + substitution_cost,
                )
            )
        previous = current
    return previous[-1]


def _units(text: str, unit: str) -> tuple[str, ...]:
    normalized = normalize_for_error_rate(text)
    if unit == "character":
        return tuple(normalized)
    if unit == "word":
        return tuple(normalized.split())
    raise ValueError(f"unsupported error-rate unit: {unit}")


def _single_error_rate(reference: str, prediction: str, *, unit: str) -> float:
    reference_units = _units(reference, unit)
    if not reference_units:
        raise ValueError("reference must contain at least one metric unit")
    prediction_units = _units(prediction, unit)
    return _levenshtein_distance(reference_units, prediction_units) / len(
        reference_units
    )


def cer(reference: str, prediction: str) -> float:
    return _single_error_rate(reference, prediction, unit="character")


def wer(reference: str, prediction: str) -> float:
    """Whitespace-token WER; case and punctuation remain significant."""

    return _single_error_rate(reference, prediction, unit="word")


@dataclass(frozen=True, slots=True)
class ErrorRateStats:
    edits: int
    reference_units: int

    @property
    def rate(self) -> float:
        return self.edits / self.reference_units

    def to_dict(self) -> dict[str, int | float]:
        return {
            "rate": self.rate,
            "edits": self.edits,
            "reference_units": self.reference_units,
        }


def _corpus_error_rate(
    pairs: Sequence[EvaluationPair],
    *,
    unit: str,
) -> ErrorRateStats:
    edits = 0
    reference_unit_count = 0
    for pair in pairs:
        reference_units = _units(pair.reference.reference, unit)
        prediction_units = _units(pair.prediction.prediction, unit)
        edits += _levenshtein_distance(reference_units, prediction_units)
        reference_unit_count += len(reference_units)
    if reference_unit_count == 0:
        raise ValueError("references must contain at least one metric unit")
    return ErrorRateStats(edits, reference_unit_count)


@dataclass(frozen=True, slots=True)
class ProtectedTokenStats:
    preserved_occurrences: int
    expected_occurrences: int
    failed_example_ids: tuple[str, ...]

    @property
    def rate(self) -> float | None:
        if self.expected_occurrences == 0:
            return None
        return self.preserved_occurrences / self.expected_occurrences

    def to_dict(self) -> dict[str, object]:
        return {
            "rate": self.rate,
            "preserved_occurrences": self.preserved_occurrences,
            "expected_occurrences": self.expected_occurrences,
            "failed_example_ids": list(self.failed_example_ids),
        }


def protected_token_preservation(
    reference: str,
    prediction: str,
    protected_tokens: Sequence[str],
) -> float | None:
    reference_nfc = unicodedata.normalize("NFC", reference)
    prediction_nfc = unicodedata.normalize("NFC", prediction)
    expected = 0
    preserved = 0
    for token in protected_tokens:
        token_nfc = unicodedata.normalize("NFC", token)
        expected_count = reference_nfc.count(token_nfc)
        expected += expected_count
        preserved += min(expected_count, prediction_nfc.count(token_nfc))
    return None if expected == 0 else preserved / expected


def _protected_token_stats(
    pairs: Sequence[EvaluationPair],
) -> ProtectedTokenStats:
    expected = 0
    preserved = 0
    failed_ids: list[str] = []
    for pair in pairs:
        reference_nfc = unicodedata.normalize("NFC", pair.reference.reference)
        prediction_nfc = unicodedata.normalize("NFC", pair.prediction.prediction)
        example_failed = False
        for token in pair.reference.protected_tokens:
            expected_count = reference_nfc.count(token)
            prediction_count = prediction_nfc.count(token)
            expected += expected_count
            preserved += min(expected_count, prediction_count)
            if prediction_count < expected_count:
                example_failed = True
        if example_failed:
            failed_ids.append(pair.reference.id)
    return ProtectedTokenStats(preserved, expected, tuple(failed_ids))


def _quality_slice(pairs: Sequence[EvaluationPair]) -> dict[str, object]:
    return {
        "examples": len(pairs),
        "cer": _corpus_error_rate(pairs, unit="character").to_dict(),
        "wer": _corpus_error_rate(pairs, unit="word").to_dict(),
        "protected_token_preservation": _protected_token_stats(pairs).to_dict(),
    }


def sacrebleu_metrics(
    references: Sequence[str],
    predictions: Sequence[str],
) -> dict[str, object]:
    """Use sacrebleu's own implementations, or report that it is absent."""

    if not references or len(references) != len(predictions):
        raise ValueError(
            "references and predictions must have the same non-zero length"
        )
    try:
        sacrebleu = importlib.import_module("sacrebleu")
    except ModuleNotFoundError as exc:
        if exc.name != "sacrebleu":
            raise
        return {
            "status": "unavailable",
            "library": "sacrebleu",
            "reason": "optional dependency is not installed",
        }

    bleu_metric = sacrebleu.metrics.BLEU()
    chrf_pp_metric = sacrebleu.metrics.CHRF(word_order=2)
    reference_streams = [list(references)]
    prediction_list = list(predictions)

    bleu_score = bleu_metric.corpus_score(prediction_list, reference_streams)
    chrf_pp_score = chrf_pp_metric.corpus_score(
        prediction_list,
        reference_streams,
    )
    return {
        "status": "available",
        "library": "sacrebleu",
        "version": str(getattr(sacrebleu, "__version__", "unknown")),
        "sacrebleu": {
            "score": float(bleu_score.score),
            "signature": str(bleu_metric.get_signature()),
        },
        "chrf_pp": {
            "score": float(chrf_pp_score.score),
            "signature": str(chrf_pp_metric.get_signature()),
        },
    }


def _sorted_counts(values: Sequence[str]) -> dict[str, int]:
    return dict(sorted(Counter(values).items()))


def _build_selected_pairs_report(
    pairs: Sequence[EvaluationPair],
) -> dict[str, object]:
    """Build metrics for pairs already selected by an evidence policy."""

    if not pairs:
        raise ValueError("at least one evaluation pair is required")

    by_target_language: dict[str, list[EvaluationPair]] = defaultdict(list)
    for pair in pairs:
        by_target_language[pair.reference.direction.target.value].append(pair)

    language_quality = {
        language: _quality_slice(language_pairs)
        for language, language_pairs in sorted(by_target_language.items())
    }
    translation_metrics = {
        language: sacrebleu_metrics(
            [pair.reference.reference for pair in language_pairs],
            [pair.prediction.prediction for pair in language_pairs],
        )
        for language, language_pairs in sorted(by_target_language.items())
    }

    references = [pair.reference for pair in pairs]
    return {
        "report_schema_version": 1,
        "dataset": {
            "examples": len(pairs),
            "directions": _sorted_counts(
                [reference.direction.value for reference in references]
            ),
            "domains": _sorted_counts(
                [reference.domain for reference in references]
            ),
            "safety_critical_examples": sum(
                reference.safety_critical for reference in references
            ),
            "provenance": _sorted_counts(
                [reference.provenance for reference in references]
            ),
            "licenses": _sorted_counts(
                [reference.license for reference in references]
            ),
            "review_statuses": _sorted_counts(
                [reference.review_status.value for reference in references]
            ),
        },
        "metric_contract": {
            "normalization": (
                "Unicode NFC; trim/collapse whitespace; preserve case and punctuation"
            ),
            "wer_tokenization": "Unicode whitespace",
            "protected_tokens": (
                "case-sensitive exact literal occurrence recall after Unicode NFC"
            ),
        },
        "quality": {
            "overall": _quality_slice(pairs),
            "by_target_language": language_quality,
        },
        "translation_metrics_by_target_language": translation_metrics,
    }


def build_evaluation_report(
    pairs: Sequence[EvaluationPair],
    *,
    include_non_approved: bool = False,
) -> dict[str, object]:
    """Select eligible evidence and build one policy-labelled report.

    Official reports include only ``approved`` references. Callers must opt in
    explicitly to include other review states for diagnostic use.
    """

    selection = select_evaluation_pairs(
        pairs,
        include_non_approved=include_non_approved,
    )
    report = _build_selected_pairs_report(selection.included)
    return {
        **report,
        "selection": selection.to_dict(),
    }
