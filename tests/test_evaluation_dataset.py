from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from say_it_for_me.evaluation import (
    EvaluationDataError,
    Prediction,
    join_predictions,
    load_predictions,
    load_references,
    select_evaluation_pairs,
)


def reference_record(**overrides: object) -> dict[str, object]:
    record: dict[str, object] = {
        "id": "factory-001",
        "direction": "vi-ko",
        "source": "Dừng dây chuyền số 2.",
        "reference": "2번 생산 라인을 멈추세요.",
        "domain": "manufacturing-safety",
        "safety_critical": True,
        "protected_tokens": ["2"],
        "provenance": "team-authored:factory-smoke-v1",
        "license": "team-owned",
        "review_status": "native_speaker_reviewed",
    }
    record.update(overrides)
    return record


def write_jsonl(path: Path, records: list[dict[str, object]]) -> None:
    path.write_text(
        "".join(
            json.dumps(record, ensure_ascii=False) + "\n"
            for record in records
        ),
        encoding="utf-8",
    )


class EvaluationDatasetTests(unittest.TestCase):
    def test_loads_strict_reference_and_prediction_schema(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            references_path = root / "references.jsonl"
            predictions_path = root / "predictions.jsonl"
            write_jsonl(references_path, [reference_record()])
            write_jsonl(
                predictions_path,
                [{"id": "factory-001", "prediction": "2번 생산 라인을 멈추세요."}],
            )

            references = load_references(references_path)
            predictions = load_predictions(predictions_path)
            pairs = join_predictions(references, predictions)

            self.assertEqual(pairs[0].reference.id, "factory-001")
            self.assertEqual(pairs[0].reference.direction.value, "vi-ko")
            self.assertTrue(pairs[0].reference.safety_critical)
            self.assertEqual(pairs[0].reference.protected_tokens, ("2",))

    def test_rejects_extra_field_and_reports_jsonl_location(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "references.jsonl"
            write_jsonl(path, [reference_record(notes="not in schema")])

            with self.assertRaises(EvaluationDataError) as context:
                load_references(path)

            self.assertEqual(context.exception.code, "INVALID_REFERENCE_SCHEMA")
            self.assertEqual(context.exception.line, 1)
            self.assertEqual(context.exception.path, str(path))

    def test_rejects_integer_in_place_of_json_boolean(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "references.jsonl"
            write_jsonl(path, [reference_record(safety_critical=1)])

            with self.assertRaises(EvaluationDataError) as context:
                load_references(path)

            self.assertEqual(context.exception.code, "INVALID_FIELD_TYPE")
            self.assertEqual(context.exception.field, "safety_critical")

    def test_rejects_escaped_lone_surrogate_with_safe_location_error(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "references.jsonl"
            path.write_text(
                json.dumps(
                    reference_record(source="line 2 \ud800"),
                    ensure_ascii=True,
                )
                + "\n",
                encoding="utf-8",
            )

            with self.assertRaises(EvaluationDataError) as context:
                load_references(path)

            error = context.exception
            self.assertEqual(error.code, "UNSAFE_UNICODE_CATEGORY")
            self.assertEqual(error.field, "source")
            self.assertEqual(error.path, str(path))
            self.assertEqual(error.line, 1)
            self.assertIn("category Cs", str(error))
            self.assertIn("U+D800", str(error))
            # The diagnostic itself must always be safe to emit as UTF-8.
            str(error).encode("utf-8")

    def test_rejects_bidi_and_zero_width_format_controls(self) -> None:
        unsafe_characters = {
            "right-to-left override": "\u202e",
            "zero-width space": "\u200b",
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "predictions.jsonl"
            for label, character in unsafe_characters.items():
                with self.subTest(character=label):
                    write_jsonl(
                        path,
                        [
                            {
                                "id": "factory-001",
                                "prediction": f"safe{character}text",
                            }
                        ],
                    )

                    with self.assertRaises(EvaluationDataError) as context:
                        load_predictions(path)

                    error = context.exception
                    self.assertEqual(error.code, "UNSAFE_UNICODE_CATEGORY")
                    self.assertEqual(error.field, "prediction")
                    self.assertEqual(error.path, str(path))
                    self.assertEqual(error.line, 1)
                    self.assertIn("category Cf", str(error))
                    self.assertIn(f"U+{ord(character):04X}", str(error))

    def test_rejects_protected_token_absent_from_reference(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "references.jsonl"
            write_jsonl(
                path,
                [
                    reference_record(
                        source="Dừng máy A-17.",
                        protected_tokens=["A-17"],
                    )
                ],
            )

            with self.assertRaises(EvaluationDataError) as context:
                load_references(path)

            self.assertEqual(
                context.exception.code,
                "PROTECTED_TOKEN_NOT_IN_REFERENCE",
            )

    def test_rejects_duplicate_json_keys(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "predictions.jsonl"
            path.write_text(
                '{"id":"factory-001","id":"factory-002","prediction":"x"}\n',
                encoding="utf-8",
            )

            with self.assertRaises(EvaluationDataError) as context:
                load_predictions(path)

            self.assertEqual(context.exception.code, "DUPLICATE_JSON_KEY")
            self.assertEqual(context.exception.line, 1)

    def test_join_uses_reference_order_and_requires_exact_id_coverage(self) -> None:
        first = load_reference(reference_record())
        second = load_reference(
            reference_record(
                id="factory-002",
                source="Mã lỗi E-42.",
                reference="오류 코드 E-42.",
                protected_tokens=["E-42"],
            )
        )
        predictions = (
            Prediction("factory-002", "오류 코드 E-42."),
            Prediction("factory-001", "2번 생산 라인을 멈추세요."),
        )

        pairs = join_predictions((first, second), predictions)

        self.assertEqual(
            [pair.reference.id for pair in pairs],
            ["factory-001", "factory-002"],
        )

        with self.assertRaises(EvaluationDataError) as context:
            join_predictions((first, second), predictions[:1])
        self.assertEqual(context.exception.code, "MISSING_PREDICTIONS")

    def test_rejects_duplicate_reference_ids(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "references.jsonl"
            write_jsonl(path, [reference_record(), reference_record()])

            with self.assertRaises(EvaluationDataError) as context:
                load_references(path)

            self.assertEqual(context.exception.code, "DUPLICATE_REFERENCE_ID")

    def test_selection_defaults_to_approved_only_and_reports_exclusions(
        self,
    ) -> None:
        approved = load_reference(
            reference_record(review_status="approved")
        )
        pending = load_reference(
            reference_record(
                id="factory-002",
                review_status="native_speaker_reviewed",
            )
        )
        pairs = join_predictions(
            (approved, pending),
            (
                Prediction(approved.id, approved.reference),
                Prediction(pending.id, pending.reference),
            ),
        )

        selection = select_evaluation_pairs(pairs)

        self.assertEqual(selection.policy, "approved_only")
        self.assertEqual(
            [pair.reference.id for pair in selection.included],
            ["factory-001"],
        )
        self.assertEqual(
            [pair.reference.id for pair in selection.excluded],
            ["factory-002"],
        )
        self.assertEqual(
            selection.to_dict(),
            {
                "policy": "approved_only",
                "included_ids": ["factory-001"],
                "excluded": [
                    {
                        "id": "factory-002",
                        "review_status": "native_speaker_reviewed",
                    }
                ],
            },
        )

    def test_selection_rejects_official_run_without_approved_references(
        self,
    ) -> None:
        reference = load_reference(reference_record())
        pairs = join_predictions(
            (reference,),
            (Prediction(reference.id, reference.reference),),
        )

        with self.assertRaises(EvaluationDataError) as context:
            select_evaluation_pairs(pairs)

        self.assertEqual(context.exception.code, "NO_APPROVED_REFERENCES")
        self.assertEqual(context.exception.field, "review_status")

    def test_selection_can_include_non_approved_for_diagnostics(self) -> None:
        reference = load_reference(reference_record())
        pairs = join_predictions(
            (reference,),
            (Prediction(reference.id, reference.reference),),
        )

        selection = select_evaluation_pairs(
            pairs,
            include_non_approved=True,
        )

        self.assertEqual(selection.policy, "all_records_diagnostic")
        self.assertEqual(selection.included, pairs)
        self.assertEqual(selection.excluded, ())
        self.assertEqual(
            selection.to_dict(),
            {
                "policy": "all_records_diagnostic",
                "included_ids": ["factory-001"],
                "excluded": [],
            },
        )


def load_reference(record: dict[str, object]):
    from say_it_for_me.evaluation import ReferenceExample

    return ReferenceExample.from_mapping(record)


if __name__ == "__main__":
    unittest.main()
