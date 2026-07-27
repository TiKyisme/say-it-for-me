from __future__ import annotations

import types
import unittest
from unittest.mock import patch

from say_it_for_me.evaluation import (
    EvaluationDataError,
    EvaluationPair,
    Prediction,
    ReferenceExample,
    build_evaluation_report,
    cer,
    protected_token_preservation,
    sacrebleu_metrics,
    wer,
)


def make_reference(
    *,
    identifier: str = "sample-001",
    direction: str = "vi-ko",
    source: str = "Dừng A-17 A-17.",
    reference: str = "정지 A-17 A-17.",
    protected_tokens: list[str] | None = None,
    review_status: str = "approved",
) -> ReferenceExample:
    return ReferenceExample.from_mapping(
        {
            "id": identifier,
            "direction": direction,
            "source": source,
            "reference": reference,
            "domain": "manufacturing-safety",
            "safety_critical": True,
            "protected_tokens": (
                ["A-17"] if protected_tokens is None else protected_tokens
            ),
            "provenance": "team-authored:metrics-test",
            "license": "team-owned",
            "review_status": review_status,
        }
    )


class EvaluationMetricTests(unittest.TestCase):
    def test_cer_and_whitespace_wer_use_edit_distance(self) -> None:
        self.assertAlmostEqual(cer("a b", "a c"), 1 / 3)
        self.assertAlmostEqual(wer("a b", "a c"), 1 / 2)

    def test_error_rates_normalize_unicode_nfc(self) -> None:
        self.assertEqual(cer("café", "cafe\u0301"), 0.0)

    def test_protected_token_metric_counts_required_occurrences(self) -> None:
        self.assertEqual(
            protected_token_preservation(
                "정지 A-17 A-17.",
                "정지 A-17.",
                ["A-17"],
            ),
            0.5,
        )
        self.assertIsNone(
            protected_token_preservation("문장", "문장", []),
        )

    def test_report_splits_error_rates_by_target_language(self) -> None:
        ko_reference = make_reference()
        vi_reference = make_reference(
            identifier="sample-002",
            direction="ko-vi",
            source="오류 코드 E-42.",
            reference="Mã lỗi E-42.",
            protected_tokens=["E-42"],
        )
        pairs = (
            EvaluationPair(
                ko_reference,
                Prediction("sample-001", "정지 A-17."),
            ),
            EvaluationPair(
                vi_reference,
                Prediction("sample-002", "Mã lỗi E-42."),
            ),
        )

        with patch(
            "say_it_for_me.evaluation.metrics.importlib.import_module",
            side_effect=ModuleNotFoundError(
                "No module named 'sacrebleu'",
                name="sacrebleu",
            ),
        ):
            report = build_evaluation_report(pairs)

        by_language = report["quality"]["by_target_language"]
        self.assertEqual(set(by_language), {"ko", "vi"})
        self.assertEqual(
            report["quality"]["overall"]["protected_token_preservation"][
                "rate"
            ],
            2 / 3,
        )
        self.assertEqual(
            report["translation_metrics_by_target_language"]["ko"]["status"],
            "unavailable",
        )
        self.assertEqual(report["dataset"]["licenses"], {"team-owned": 2})
        self.assertEqual(
            report["selection"],
            {
                "policy": "approved_only",
                "included_ids": ["sample-001", "sample-002"],
                "excluded": [],
            },
        )

    def test_public_report_rejects_non_approved_only_pairs(self) -> None:
        reference = make_reference(review_status="team_reviewed")
        pairs = (
            EvaluationPair(
                reference,
                Prediction(reference.id, reference.reference),
            ),
        )

        with self.assertRaises(EvaluationDataError) as caught:
            build_evaluation_report(pairs)

        self.assertEqual(caught.exception.code, "NO_APPROVED_REFERENCES")
        self.assertEqual(caught.exception.field, "review_status")

    def test_public_report_excludes_pending_pairs_from_metrics(self) -> None:
        approved = make_reference(identifier="approved-001")
        pending = make_reference(
            identifier="pending-001",
            reference="A-17",
            review_status="team_reviewed",
        )
        pairs = (
            EvaluationPair(
                approved,
                Prediction(approved.id, approved.reference),
            ),
            EvaluationPair(
                pending,
                Prediction(pending.id, "completely wrong"),
            ),
        )

        with patch(
            "say_it_for_me.evaluation.metrics.importlib.import_module",
            side_effect=ModuleNotFoundError(
                "No module named 'sacrebleu'",
                name="sacrebleu",
            ),
        ):
            report = build_evaluation_report(pairs)

        self.assertEqual(report["dataset"]["examples"], 1)
        self.assertEqual(report["quality"]["overall"]["cer"]["rate"], 0.0)
        self.assertEqual(report["quality"]["overall"]["wer"]["rate"], 0.0)
        self.assertEqual(
            report["selection"],
            {
                "policy": "approved_only",
                "included_ids": ["approved-001"],
                "excluded": [
                    {
                        "id": "pending-001",
                        "review_status": "team_reviewed",
                    }
                ],
            },
        )

    def test_public_report_diagnostic_override_includes_all_pairs(self) -> None:
        approved = make_reference(identifier="approved-001")
        pending = make_reference(
            identifier="pending-001",
            reference="A-17",
            review_status="team_reviewed",
        )
        pairs = (
            EvaluationPair(
                approved,
                Prediction(approved.id, approved.reference),
            ),
            EvaluationPair(
                pending,
                Prediction(pending.id, "completely wrong"),
            ),
        )

        with patch(
            "say_it_for_me.evaluation.metrics.importlib.import_module",
            side_effect=ModuleNotFoundError(
                "No module named 'sacrebleu'",
                name="sacrebleu",
            ),
        ):
            report = build_evaluation_report(
                pairs,
                include_non_approved=True,
            )

        self.assertEqual(report["dataset"]["examples"], 2)
        self.assertGreater(report["quality"]["overall"]["cer"]["rate"], 0.0)
        self.assertEqual(
            report["selection"],
            {
                "policy": "all_records_diagnostic",
                "included_ids": ["approved-001", "pending-001"],
                "excluded": [],
            },
        )

    def test_sacrebleu_adapter_reports_version_scores_and_signatures(self) -> None:
        class FakeScore:
            def __init__(self, score: float) -> None:
                self.score = score

        class FakeMetric:
            def __init__(self, score: float, *args: object, **kwargs: object) -> None:
                self.score = score

            def corpus_score(
                self,
                predictions: list[str],
                reference_streams: list[list[str]],
            ) -> FakeScore:
                self.assert_shape(predictions, reference_streams)
                return FakeScore(self.score)

            def assert_shape(
                self,
                predictions: list[str],
                reference_streams: list[list[str]],
            ) -> None:
                if len(reference_streams) != 1:
                    raise AssertionError("expected one reference stream")
                if len(predictions) != len(reference_streams[0]):
                    raise AssertionError("stream lengths differ")

            def get_signature(self) -> str:
                return f"fake-signature-{self.score}"

        class FakeBleu(FakeMetric):
            def __init__(self) -> None:
                super().__init__(41.5)

        class FakeChrf(FakeMetric):
            def __init__(self, *, word_order: int) -> None:
                if word_order != 2:
                    raise AssertionError("chrF++ requires word_order=2")
                super().__init__(63.25)

        fake_module = types.SimpleNamespace(
            __version__="test-version",
            metrics=types.SimpleNamespace(BLEU=FakeBleu, CHRF=FakeChrf),
        )
        with patch(
            "say_it_for_me.evaluation.metrics.importlib.import_module",
            return_value=fake_module,
        ):
            result = sacrebleu_metrics(["tham chiếu"], ["dự đoán"])

        self.assertEqual(result["status"], "available")
        self.assertEqual(result["version"], "test-version")
        self.assertEqual(result["sacrebleu"]["score"], 41.5)
        self.assertEqual(result["chrf_pp"]["score"], 63.25)
        self.assertIn("signature", result["sacrebleu"])
        self.assertIn("signature", result["chrf_pp"])


if __name__ == "__main__":
    unittest.main()
