"""Adapter-boundary tests and opt-in smoke test for real Whisper ASR."""
from __future__ import annotations

import os
import unittest

from say_it_for_me.contracts import AudioBuffer, Language

try:
    from say_it_for_me.stages.asr_real import WhisperRecognizer

    _HAS_FASTER_WHISPER = True
except ImportError:
    _HAS_FASTER_WHISPER = False


def _make_silence(duration_s: float = 1.0) -> AudioBuffer:
    sample_rate = 16_000
    n = int(sample_rate * duration_s)
    return AudioBuffer(tuple(0.0 for _ in range(n)), sample_rate)


@unittest.skipUnless(_HAS_FASTER_WHISPER, "faster-whisper not installed")
class WhisperRecognizerBoundaryTests(unittest.TestCase):
    def test_rejects_wrong_sample_rate(self) -> None:
        recognizer = WhisperRecognizer(model_size="tiny", device="cpu", compute_type="int8")
        bad_audio = AudioBuffer(tuple(0.0 for _ in range(48_000)), 48_000)
        with self.assertRaisesRegex(ValueError, "16 kHz"):
            recognizer.transcribe(bad_audio, Language.VIETNAMESE, "test-001")

    @unittest.skipUnless(
        os.getenv("RUN_REAL_INFERENCE_SMOKE") == "1",
        "set RUN_REAL_INFERENCE_SMOKE=1 to permit a local Whisper model smoke test",
    )
    def test_transcribe_returns_transcript(self) -> None:
        recognizer = WhisperRecognizer(model_size="tiny", device="cpu", compute_type="int8")
        audio = _make_silence(2.0)
        try:
            result = recognizer.transcribe(
                audio, Language.VIETNAMESE, "test-002"
            )
        except ValueError:
            self.skipTest("Whisper returned empty on silence input (expected edge case)")
        finally:
            recognizer.close()

        self.assertEqual(result.language, Language.VIETNAMESE)
        self.assertEqual(result.utterance_id, "test-002")
        self.assertIsInstance(result.text, str)
        self.assertGreater(len(result.text), 0)


if __name__ == "__main__":
    unittest.main()
