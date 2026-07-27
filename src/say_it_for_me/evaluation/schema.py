from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path
from typing import Any, Mapping

from say_it_for_me.contracts import Direction


REFERENCE_FIELDS = frozenset(
    {
        "id",
        "direction",
        "source",
        "reference",
        "domain",
        "safety_critical",
        "protected_tokens",
        "provenance",
        "license",
        "review_status",
    }
)
PREDICTION_FIELDS = frozenset({"id", "prediction"})

_ID_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$")
_DOMAIN_PATTERN = re.compile(r"^[a-z0-9][a-z0-9._-]{0,63}$")
_DISALLOWED_UNICODE_CATEGORY_PREFIX = "C"


class ReviewStatus(StrEnum):
    UNREVIEWED = "unreviewed"
    TEAM_REVIEWED = "team_reviewed"
    NATIVE_SPEAKER_REVIEWED = "native_speaker_reviewed"
    APPROVED = "approved"


class EvaluationDataError(ValueError):
    """A dataset error with a stable code and optional JSONL location."""

    def __init__(
        self,
        code: str,
        message: str,
        *,
        field: str | None = None,
        path: str | Path | None = None,
        line: int | None = None,
    ) -> None:
        super().__init__(message)
        self.code = code
        self.field = field
        self.path = str(path) if path is not None else None
        self.line = line

    def at(self, path: str | Path, line: int) -> EvaluationDataError:
        return EvaluationDataError(
            self.code,
            str(self),
            field=self.field,
            path=path,
            line=line,
        )

    def to_dict(self) -> dict[str, object]:
        details: dict[str, object] = {
            "code": self.code,
            "message": str(self),
        }
        if self.path is not None:
            details["path"] = self.path
        if self.line is not None:
            details["line"] = self.line
        if self.field is not None:
            details["field"] = self.field
        return details


def _require_exact_fields(
    value: Mapping[str, Any],
    expected: frozenset[str],
    record_name: str,
) -> None:
    actual = set(value)
    missing = sorted(expected - actual)
    extra = sorted(actual - expected)
    if missing or extra:
        parts = []
        if missing:
            parts.append(f"missing fields: {', '.join(missing)}")
        if extra:
            # JSON object keys are untrusted too. ``ascii`` keeps malformed
            # surrogate or format characters from reaching terminal output.
            parts.append(
                "unexpected fields: "
                + ", ".join(ascii(field) for field in extra)
            )
        raise EvaluationDataError(
            f"INVALID_{record_name.upper()}_SCHEMA",
            f"{record_name} must use the exact schema ({'; '.join(parts)})",
        )


def _require_safe_unicode(value: str, *, field: str) -> None:
    """Reject Unicode Other (C*) code points with an ASCII-safe error.

    Gate 2 data is a frozen Vietnamese/Korean manufacturing corpus, so it has
    no legitimate need for controls, format controls, surrogates, private-use
    code points, or code points unassigned by this Python Unicode database.
    """

    for index, character in enumerate(value):
        category = unicodedata.category(character)
        if category.startswith(_DISALLOWED_UNICODE_CATEGORY_PREFIX):
            raise EvaluationDataError(
                "UNSAFE_UNICODE_CATEGORY",
                f"{field} contains disallowed Unicode category {category} "
                f"at character index {index} (U+{ord(character):04X})",
                field=field,
            )


def _require_string(
    value: object,
    *,
    field: str,
    allow_empty: bool = False,
    max_length: int = 10_000,
    trim_required: bool = True,
) -> str:
    if not isinstance(value, str):
        raise EvaluationDataError(
            "INVALID_FIELD_TYPE",
            f"{field} must be a string",
            field=field,
        )
    if len(value) > max_length:
        raise EvaluationDataError(
            "FIELD_TOO_LONG",
            f"{field} exceeds {max_length} characters",
            field=field,
        )
    # Validate before trimming/normalizing so every C* violation receives the
    # same stable, safely printable error instead of leaking the character.
    _require_safe_unicode(value, field=field)
    if not allow_empty and not value.strip():
        raise EvaluationDataError(
            "EMPTY_FIELD",
            f"{field} must not be empty",
            field=field,
        )
    if trim_required and value != value.strip():
        raise EvaluationDataError(
            "UNTRIMMED_FIELD",
            f"{field} must not have leading or trailing whitespace",
            field=field,
        )
    if unicodedata.normalize("NFC", value) != value:
        raise EvaluationDataError(
            "NON_NFC_TEXT",
            f"{field} must use Unicode NFC normalization",
            field=field,
        )
    return value


def _require_id(value: object) -> str:
    identifier = _require_string(value, field="id", max_length=128)
    if not _ID_PATTERN.fullmatch(identifier):
        raise EvaluationDataError(
            "INVALID_ID",
            "id must start with an ASCII alphanumeric and contain only "
            "ASCII alphanumerics, dot, underscore, or hyphen",
            field="id",
        )
    return identifier


@dataclass(frozen=True, slots=True)
class ReferenceExample:
    id: str
    direction: Direction
    source: str
    reference: str
    domain: str
    safety_critical: bool
    protected_tokens: tuple[str, ...]
    provenance: str
    license: str
    review_status: ReviewStatus

    @classmethod
    def from_mapping(cls, value: object) -> ReferenceExample:
        if not isinstance(value, Mapping):
            raise EvaluationDataError(
                "INVALID_REFERENCE_SCHEMA",
                "reference record must be a JSON object",
            )
        _require_exact_fields(value, REFERENCE_FIELDS, "reference")

        identifier = _require_id(value["id"])
        raw_direction = _require_string(
            value["direction"],
            field="direction",
            max_length=5,
        )
        try:
            direction = Direction(raw_direction)
        except (TypeError, ValueError) as exc:
            allowed = ", ".join(direction.value for direction in Direction)
            raise EvaluationDataError(
                "INVALID_DIRECTION",
                f"direction must be one of: {allowed}",
                field="direction",
            ) from exc

        source = _require_string(value["source"], field="source")
        reference = _require_string(value["reference"], field="reference")
        domain = _require_string(value["domain"], field="domain", max_length=64)
        if not _DOMAIN_PATTERN.fullmatch(domain):
            raise EvaluationDataError(
                "INVALID_DOMAIN",
                "domain must be a lowercase ASCII slug containing only "
                "alphanumerics, dot, underscore, or hyphen",
                field="domain",
            )

        safety_critical = value["safety_critical"]
        if type(safety_critical) is not bool:
            raise EvaluationDataError(
                "INVALID_FIELD_TYPE",
                "safety_critical must be a JSON boolean",
                field="safety_critical",
            )

        raw_tokens = value["protected_tokens"]
        if not isinstance(raw_tokens, list):
            raise EvaluationDataError(
                "INVALID_FIELD_TYPE",
                "protected_tokens must be a JSON array of strings",
                field="protected_tokens",
            )
        tokens = tuple(
            _require_string(
                token,
                field=f"protected_tokens[{index}]",
                max_length=256,
            )
            for index, token in enumerate(raw_tokens)
        )
        if len(set(tokens)) != len(tokens):
            raise EvaluationDataError(
                "DUPLICATE_PROTECTED_TOKEN",
                "protected_tokens must not contain duplicates",
                field="protected_tokens",
            )
        for token in tokens:
            if token not in source:
                raise EvaluationDataError(
                    "PROTECTED_TOKEN_NOT_IN_SOURCE",
                    f"protected token {token!r} is not present in source",
                    field="protected_tokens",
                )
            if token not in reference:
                raise EvaluationDataError(
                    "PROTECTED_TOKEN_NOT_IN_REFERENCE",
                    f"protected token {token!r} is not present in reference",
                    field="protected_tokens",
                )

        provenance = _require_string(
            value["provenance"],
            field="provenance",
            max_length=2_048,
        )
        license_name = _require_string(
            value["license"],
            field="license",
            max_length=256,
        )
        raw_review_status = _require_string(
            value["review_status"],
            field="review_status",
            max_length=32,
        )
        try:
            review_status = ReviewStatus(raw_review_status)
        except (TypeError, ValueError) as exc:
            allowed = ", ".join(status.value for status in ReviewStatus)
            raise EvaluationDataError(
                "INVALID_REVIEW_STATUS",
                f"review_status must be one of: {allowed}",
                field="review_status",
            ) from exc

        return cls(
            id=identifier,
            direction=direction,
            source=source,
            reference=reference,
            domain=domain,
            safety_critical=safety_critical,
            protected_tokens=tokens,
            provenance=provenance,
            license=license_name,
            review_status=review_status,
        )


@dataclass(frozen=True, slots=True)
class Prediction:
    id: str
    prediction: str

    @classmethod
    def from_mapping(cls, value: object) -> Prediction:
        if not isinstance(value, Mapping):
            raise EvaluationDataError(
                "INVALID_PREDICTION_SCHEMA",
                "prediction record must be a JSON object",
            )
        _require_exact_fields(value, PREDICTION_FIELDS, "prediction")
        return cls(
            id=_require_id(value["id"]),
            # Empty output is a model failure that must remain measurable.
            prediction=_require_string(
                value["prediction"],
                field="prediction",
                allow_empty=True,
                trim_required=False,
            ),
        )
