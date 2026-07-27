from __future__ import annotations

import unittest

from say_it_for_me.cli import build_mock_pipeline
from say_it_for_me.contracts import AudioBuffer, Direction, Language
from say_it_for_me.errors import PipelineError


class PipelineTests(unittest.TestCase):
    def setUp(self) -> None:
        self.audio = AudioBuffer((0.0,) * 48_000, 48_000)

    def test_vi_to_ko_preserves_explicit_direction_and_stage_order(self) -> None:
        result = build_mock_pipeline("Dừng dây chuyền số 2").process(
            self.audio,
            Direction.VI_TO_KO,
        )

        self.assertEqual(result.transcript.language, Language.VIETNAMESE)
        self.assertEqual(result.translation.target_language, Language.KOREAN)
        self.assertEqual(result.translation.translated_text, "2번 생산 라인을 멈추세요.")
        self.assertEqual(
            [timing.stage for timing in result.trace.timings],
            ["denoise", "resample", "asr", "translation", "tts"],
        )
        self.assertGreater(result.trace.total_ms, 0)

    def test_ko_to_vi_uses_selected_source_language(self) -> None:
        result = build_mock_pipeline("2번 생산 라인을 멈추세요.").process(
            self.audio,
            Direction.KO_TO_VI,
        )

        self.assertEqual(result.transcript.language, Language.KOREAN)
        self.assertEqual(result.translation.target_language, Language.VIETNAMESE)
        self.assertEqual(result.translation.translated_text, "Dừng dây chuyền số 2.")

    def test_rejects_audio_that_skips_the_48khz_capture_contract(self) -> None:
        invalid_audio = AudioBuffer((0.0,) * 16_000, 16_000)

        with self.assertRaises(PipelineError) as context:
            build_mock_pipeline("test").process(
                invalid_audio,
                Direction.VI_TO_KO,
            )

        self.assertEqual(context.exception.code, "INVALID_CAPTURE_RATE")
        self.assertEqual(context.exception.stage, "capture")


if __name__ == "__main__":
    unittest.main()

