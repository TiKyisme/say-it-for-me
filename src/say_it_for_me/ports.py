from __future__ import annotations

from typing import Protocol

from .contracts import (
    AudioBuffer,
    Language,
    SynthesizedAudio,
    Transcript,
    Translation,
)


class Denoiser(Protocol):
    def process(self, audio: AudioBuffer) -> AudioBuffer: ...


class Resampler(Protocol):
    def process(self, audio: AudioBuffer, target_sample_rate_hz: int) -> AudioBuffer: ...


class SpeechRecognizer(Protocol):
    def transcribe(
        self,
        audio: AudioBuffer,
        language: Language,
        utterance_id: str,
    ) -> Transcript: ...


class Translator(Protocol):
    def translate(
        self,
        transcript: Transcript,
        target_language: Language,
    ) -> Translation: ...


class SpeechSynthesizer(Protocol):
    def synthesize(self, translation: Translation) -> SynthesizedAudio: ...


class ModelLifecycle(Protocol):
    def warmup(self) -> None: ...

    def close(self) -> None: ...

