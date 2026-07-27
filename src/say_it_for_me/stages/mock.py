from __future__ import annotations

from math import pi, sin

from ..contracts import (
    AudioBuffer,
    Language,
    SynthesizedAudio,
    Transcript,
    Translation,
)


class PassthroughDenoiser:
    def process(self, audio: AudioBuffer) -> AudioBuffer:
        if audio.sample_rate_hz != 48_000:
            raise ValueError("mock denoiser enforces the 48 kHz denoiser contract")
        return audio


class SimpleResampler:
    """Dependency-free nearest-neighbor resampler for contract tests only."""

    def process(self, audio: AudioBuffer, target_sample_rate_hz: int) -> AudioBuffer:
        if target_sample_rate_hz <= 0:
            raise ValueError("target sample rate must be positive")
        ratio = target_sample_rate_hz / audio.sample_rate_hz
        output_length = max(1, round(len(audio.samples) * ratio))
        samples = tuple(
            audio.samples[min(len(audio.samples) - 1, int(index / ratio))]
            for index in range(output_length)
        )
        return AudioBuffer(samples, target_sample_rate_hz)


class ScriptedRecognizer:
    def __init__(self, text: str) -> None:
        self._text = text

    def transcribe(
        self,
        audio: AudioBuffer,
        language: Language,
        utterance_id: str,
    ) -> Transcript:
        if audio.sample_rate_hz != 16_000:
            raise ValueError("ASR input must be 16 kHz")
        return Transcript(utterance_id, self._text, language)


class DictionaryTranslator:
    _SMOKE_TRANSLATIONS = {
        ("vi", "ko", "Dừng dây chuyền số 2"): "2번 생산 라인을 멈추세요.",
        ("ko", "vi", "2번 생산 라인을 멈추세요."): "Dừng dây chuyền số 2.",
    }

    def translate(
        self,
        transcript: Transcript,
        target_language: Language,
    ) -> Translation:
        key = (transcript.language.value, target_language.value, transcript.text)
        translated = self._SMOKE_TRANSLATIONS.get(
            key,
            f"[MOCK {target_language.value}] {transcript.text}",
        )
        return Translation(
            utterance_id=transcript.utterance_id,
            source_text=transcript.text,
            translated_text=translated,
            source_language=transcript.language,
            target_language=target_language,
        )


class ToneSynthesizer:
    """Creates a short tone so the audio contract can be tested without TTS."""

    SAMPLE_RATE_HZ = 22_050

    def synthesize(self, translation: Translation) -> SynthesizedAudio:
        duration_s = min(1.0, max(0.1, len(translation.translated_text) * 0.01))
        sample_count = round(self.SAMPLE_RATE_HZ * duration_s)
        samples = tuple(
            0.08 * sin(2 * pi * 440 * index / self.SAMPLE_RATE_HZ)
            for index in range(sample_count)
        )
        return SynthesizedAudio(
            translation.utterance_id,
            AudioBuffer(samples, self.SAMPLE_RATE_HZ),
        )

