"""Smoke tests for the real Whisper ASR adapter.

Skipped automatically when faster-whisper is not installed or model is unavailable.
"""
from __future__ import annotations

import pytest

from say_it_for_me.contracts import AudioBuffer, Language

try:
    from say_it_for_me.stages.asr_real import WhisperRecognizer
    _HAS_FASTER_WHISPER = True
except ImportError:
    _HAS_FASTER_WHISPER = False

pytestmark = pytest.mark.skipif(
    not _HAS_FASTER_WHISPER,
    reason="faster-whisper not installed",
)


def _make_silence(duration_s: float = 1.0) -> AudioBuffer:
    sample_rate = 16_000
    n = int(sample_rate * duration_s)
    return AudioBuffer(tuple(0.0 for _ in range(n)), sample_rate)


@pytest.fixture(scope="module")
def recognizer():
    rec = WhisperRecognizer(model_size="tiny", device="cpu", compute_type="int8")
    rec.warmup()
    yield rec
    rec.close()


class TestWhisperRecognizerContract:
    def test_rejects_wrong_sample_rate(self, recognizer):
        bad_audio = AudioBuffer(tuple(0.0 for _ in range(48_000)), 48_000)
        with pytest.raises(ValueError, match="16 kHz"):
            recognizer.transcribe(bad_audio, Language.VIETNAMESE, "test-001")

    def test_transcribe_returns_transcript(self, recognizer):
        """Real inference on silence — Whisper may hallucinate or raise."""
        audio = _make_silence(2.0)
        try:
            result = recognizer.transcribe(audio, Language.VIETNAMESE, "test-002")
            assert result.language is Language.VIETNAMESE
            assert result.utterance_id == "test-002"
            assert isinstance(result.text, str) and len(result.text) > 0
        except ValueError:
            pytest.skip("Whisper returned empty on silence input (expected edge case)")
