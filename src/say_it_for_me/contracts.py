from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Iterable


class Language(StrEnum):
    VIETNAMESE = "vi"
    KOREAN = "ko"


class Direction(StrEnum):
    VI_TO_KO = "vi-ko"
    KO_TO_VI = "ko-vi"

    @property
    def source(self) -> Language:
        return (
            Language.VIETNAMESE
            if self is Direction.VI_TO_KO
            else Language.KOREAN
        )

    @property
    def target(self) -> Language:
        return (
            Language.KOREAN
            if self is Direction.VI_TO_KO
            else Language.VIETNAMESE
        )


@dataclass(frozen=True, slots=True)
class AudioBuffer:
    samples: tuple[float, ...]
    sample_rate_hz: int
    channels: int = 1

    def __post_init__(self) -> None:
        if self.sample_rate_hz <= 0:
            raise ValueError("sample_rate_hz must be positive")
        if self.channels != 1:
            raise ValueError("only mono audio is supported in the Phase 2 slice")
        if not self.samples:
            raise ValueError("audio samples must not be empty")

    @classmethod
    def from_iterable(
        cls,
        samples: Iterable[float],
        sample_rate_hz: int,
        channels: int = 1,
    ) -> AudioBuffer:
        return cls(tuple(float(sample) for sample in samples), sample_rate_hz, channels)

    @property
    def duration_ms(self) -> float:
        return len(self.samples) / self.sample_rate_hz * 1000.0


@dataclass(frozen=True, slots=True)
class Transcript:
    utterance_id: str
    text: str
    language: Language
    warnings: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.text.strip():
            raise ValueError("transcript text must not be empty")


@dataclass(frozen=True, slots=True)
class Translation:
    utterance_id: str
    source_text: str
    translated_text: str
    source_language: Language
    target_language: Language
    protected_tokens: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.translated_text.strip():
            raise ValueError("translated_text must not be empty")
        if self.source_language is self.target_language:
            raise ValueError("source and target languages must differ")


@dataclass(frozen=True, slots=True)
class SynthesizedAudio:
    utterance_id: str
    audio: AudioBuffer


@dataclass(frozen=True, slots=True)
class StageTiming:
    stage: str
    started_ns: int
    duration_ms: float


@dataclass(frozen=True, slots=True)
class PipelineTrace:
    trace_id: str
    timings: tuple[StageTiming, ...]
    warnings: tuple[str, ...] = ()

    @property
    def total_ms(self) -> float:
        return sum(timing.duration_ms for timing in self.timings)


@dataclass(frozen=True, slots=True)
class PipelineResult:
    transcript: Transcript
    translation: Translation
    synthesized_audio: SynthesizedAudio
    trace: PipelineTrace
    metadata: dict[str, str] = field(default_factory=dict)

