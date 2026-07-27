from __future__ import annotations

import unittest

from say_it_for_me.audio import (
    SegmentReason,
    SegmenterConfig,
    VadSegmenter,
)
from say_it_for_me.contracts import AudioBuffer


def frame(value: float = 0.0) -> AudioBuffer:
    return AudioBuffer((value,) * 960, 48_000)


class SegmenterTests(unittest.TestCase):
    def test_finalizes_after_configured_end_silence(self) -> None:
        segmenter = VadSegmenter()
        for _ in range(10):
            self.assertIsNone(segmenter.accept(frame(), is_speech=False))
        for _ in range(5):
            self.assertIsNone(segmenter.accept(frame(0.1), is_speech=True))

        result = None
        for _ in range(20):
            result = segmenter.accept(frame(), is_speech=False)

        self.assertIsNotNone(result)
        assert result is not None
        self.assertEqual(result.reason, SegmentReason.END_OF_SPEECH)
        self.assertFalse(segmenter.is_active)
        self.assertGreater(result.audio.duration_ms, 400)

    def test_max_duration_is_a_hard_boundary(self) -> None:
        config = SegmenterConfig(
            pre_roll_ms=20,
            end_silence_ms=40,
            max_utterance_ms=100,
        )
        segmenter = VadSegmenter(config)
        result = None
        for _ in range(5):
            result = segmenter.accept(frame(0.1), is_speech=True)

        self.assertIsNotNone(result)
        assert result is not None
        self.assertEqual(result.reason, SegmentReason.MAX_DURATION)
        self.assertAlmostEqual(result.audio.duration_ms, 100)


if __name__ == "__main__":
    unittest.main()

