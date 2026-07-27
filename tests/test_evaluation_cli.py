from __future__ import annotations

import io
import json
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch

from say_it_for_me.evaluation.cli import main


def write_jsonl(path: Path, records: list[dict[str, object]]) -> None:
    path.write_text(
        "".join(
            json.dumps(record, ensure_ascii=False) + "\n"
            for record in records
        ),
        encoding="utf-8",
    )


def reference_record(**overrides: object) -> dict[str, object]:
    record: dict[str, object] = {
        "id": "cli-001",
        "direction": "ko-vi",
        "source": "오류 코드 E-42.",
        "reference": "Mã lỗi E-42.",
        "domain": "manufacturing-safety",
        "safety_critical": True,
        "protected_tokens": ["E-42"],
        "provenance": "team-authored:cli-test",
        "license": "team-owned",
        "review_status": "approved",
    }
    record.update(overrides)
    return record


class EvaluationCliTests(unittest.TestCase):
    def test_evaluate_command_emits_reproducible_json_report(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            references = root / "references.jsonl"
            predictions = root / "predictions.jsonl"
            write_jsonl(references, [reference_record()])
            write_jsonl(
                predictions,
                [{"id": "cli-001", "prediction": "Mã lỗi E-42."}],
            )
            stdout = io.StringIO()
            stderr = io.StringIO()

            with (
                patch(
                    "say_it_for_me.evaluation.metrics.importlib.import_module",
                    side_effect=ModuleNotFoundError(
                        "No module named 'sacrebleu'",
                        name="sacrebleu",
                    ),
                ),
                redirect_stdout(stdout),
                redirect_stderr(stderr),
            ):
                exit_code = main(
                    [
                        "evaluate",
                        "--references",
                        str(references),
                        "--predictions",
                        str(predictions),
                    ]
                )

            report = json.loads(stdout.getvalue())
            self.assertEqual(exit_code, 0)
            self.assertEqual(stderr.getvalue(), "")
            self.assertEqual(report["quality"]["overall"]["cer"]["rate"], 0.0)
            self.assertEqual(report["quality"]["overall"]["wer"]["rate"], 0.0)
            self.assertEqual(
                report["quality"]["overall"]["protected_token_preservation"][
                    "rate"
                ],
                1.0,
            )
            self.assertEqual(
                report["translation_metrics_by_target_language"]["vi"]["status"],
                "unavailable",
            )
            self.assertEqual(
                report["selection"],
                {
                    "policy": "approved_only",
                    "included_ids": ["cli-001"],
                    "excluded": [],
                },
            )
            self.assertNotIn("generated_at", report)

    def test_evaluate_command_rejects_dataset_without_approved_references(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            references = root / "references.jsonl"
            predictions = root / "predictions.jsonl"
            write_jsonl(
                references,
                [reference_record(review_status="team_reviewed")],
            )
            write_jsonl(
                predictions,
                [{"id": "cli-001", "prediction": "Mã lỗi E-42."}],
            )
            stdout = io.StringIO()
            stderr = io.StringIO()

            with redirect_stdout(stdout), redirect_stderr(stderr):
                exit_code = main(
                    [
                        "evaluate",
                        "--references",
                        str(references),
                        "--predictions",
                        str(predictions),
                    ]
                )

            error = json.loads(stderr.getvalue())
            self.assertEqual(exit_code, 2)
            self.assertEqual(stdout.getvalue(), "")
            self.assertEqual(
                error["error"]["code"],
                "NO_APPROVED_REFERENCES",
            )
            self.assertEqual(error["error"]["field"], "review_status")

    def test_include_non_approved_emits_diagnostic_report(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            references = root / "references.jsonl"
            predictions = root / "predictions.jsonl"
            write_jsonl(
                references,
                [reference_record(review_status="native_speaker_reviewed")],
            )
            write_jsonl(
                predictions,
                [{"id": "cli-001", "prediction": "Mã lỗi E-42."}],
            )
            stdout = io.StringIO()
            stderr = io.StringIO()

            with (
                patch(
                    "say_it_for_me.evaluation.metrics.importlib.import_module",
                    side_effect=ModuleNotFoundError(
                        "No module named 'sacrebleu'",
                        name="sacrebleu",
                    ),
                ),
                redirect_stdout(stdout),
                redirect_stderr(stderr),
            ):
                exit_code = main(
                    [
                        "evaluate",
                        "--references",
                        str(references),
                        "--predictions",
                        str(predictions),
                        "--include-non-approved",
                    ]
                )

            report = json.loads(stdout.getvalue())
            self.assertEqual(exit_code, 0)
            self.assertEqual(stderr.getvalue(), "")
            self.assertEqual(report["dataset"]["examples"], 1)
            self.assertEqual(
                report["dataset"]["review_statuses"],
                {"native_speaker_reviewed": 1},
            )
            self.assertEqual(
                report["selection"],
                {
                    "policy": "all_records_diagnostic",
                    "included_ids": ["cli-001"],
                    "excluded": [],
                },
            )

    def test_evaluate_command_returns_structured_error_for_bad_join(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            references = root / "references.jsonl"
            predictions = root / "predictions.jsonl"
            write_jsonl(references, [reference_record()])
            write_jsonl(
                predictions,
                [{"id": "unknown-001", "prediction": "Mã lỗi E-42."}],
            )
            stdout = io.StringIO()
            stderr = io.StringIO()

            with redirect_stdout(stdout), redirect_stderr(stderr):
                exit_code = main(
                    [
                        "evaluate",
                        "--references",
                        str(references),
                        "--predictions",
                        str(predictions),
                    ]
                )

            error = json.loads(stderr.getvalue())
            self.assertEqual(exit_code, 2)
            self.assertEqual(stdout.getvalue(), "")
            self.assertEqual(error["error"]["code"], "MISSING_PREDICTIONS")


if __name__ == "__main__":
    unittest.main()
