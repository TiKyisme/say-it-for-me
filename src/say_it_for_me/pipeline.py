from __future__ import annotations

from collections.abc import Callable
from time import perf_counter_ns
from typing import TypeVar
from uuid import uuid4

from .contracts import (
    AudioBuffer,
    Direction,
    PipelineResult,
    PipelineTrace,
    StageTiming,
)
from .errors import PipelineError
from .ports import Denoiser, Resampler, SpeechRecognizer, SpeechSynthesizer, Translator

T = TypeVar("T")


class VoiceTranslationPipeline:
    """Ordered, explicit-direction pipeline with per-stage timing.

    Heavy-stage concurrency is intentionally outside this class. The Phase 2
    default is one in-flight inference request to keep peak memory bounded.
    """

    CAPTURE_SAMPLE_RATE_HZ = 48_000
    ASR_SAMPLE_RATE_HZ = 16_000

    def __init__(
        self,
        denoiser: Denoiser,
        resampler: Resampler,
        recognizer: SpeechRecognizer,
        translator: Translator,
        synthesizer: SpeechSynthesizer,
    ) -> None:
        self._denoiser = denoiser
        self._resampler = resampler
        self._recognizer = recognizer
        self._translator = translator
        self._synthesizer = synthesizer

    def process(self, audio: AudioBuffer, direction: Direction) -> PipelineResult:
        if audio.sample_rate_hz != self.CAPTURE_SAMPLE_RATE_HZ:
            raise PipelineError(
                "INVALID_CAPTURE_RATE",
                "capture",
                f"expected {self.CAPTURE_SAMPLE_RATE_HZ} Hz capture audio, "
                f"received {audio.sample_rate_hz} Hz",
            )

        utterance_id = str(uuid4())
        trace_id = str(uuid4())
        timings: list[StageTiming] = []

        denoised = self._timed(
            "denoise",
            lambda: self._denoiser.process(audio),
            timings,
        )
        asr_audio = self._timed(
            "resample",
            lambda: self._resampler.process(denoised, self.ASR_SAMPLE_RATE_HZ),
            timings,
        )
        if asr_audio.sample_rate_hz != self.ASR_SAMPLE_RATE_HZ:
            raise PipelineError(
                "INVALID_ASR_RATE",
                "resample",
                f"resampler returned {asr_audio.sample_rate_hz} Hz",
            )

        transcript = self._timed(
            "asr",
            lambda: self._recognizer.transcribe(
                asr_audio,
                direction.source,
                utterance_id,
            ),
            timings,
        )
        if transcript.language is not direction.source:
            raise PipelineError(
                "DIRECTION_MISMATCH",
                "asr",
                "recognizer output language does not match the explicit direction",
            )

        translation = self._timed(
            "translation",
            lambda: self._translator.translate(transcript, direction.target),
            timings,
        )
        if translation.target_language is not direction.target:
            raise PipelineError(
                "DIRECTION_MISMATCH",
                "translation",
                "translator output language does not match the explicit direction",
            )

        synthesized = self._timed(
            "tts",
            lambda: self._synthesizer.synthesize(translation),
            timings,
        )

        warnings = tuple(transcript.warnings)
        return PipelineResult(
            transcript=transcript,
            translation=translation,
            synthesized_audio=synthesized,
            trace=PipelineTrace(trace_id, tuple(timings), warnings),
            metadata={
                "direction": direction.value,
                "capture_sample_rate_hz": str(self.CAPTURE_SAMPLE_RATE_HZ),
                "asr_sample_rate_hz": str(self.ASR_SAMPLE_RATE_HZ),
                "runtime": "mock-architecture-slice",
            },
        )

    @staticmethod
    def _timed(
        stage: str,
        operation: Callable[[], T],
        timings: list[StageTiming],
    ) -> T:
        started_ns = perf_counter_ns()
        try:
            return operation()
        except PipelineError:
            raise
        except Exception as exc:
            raise PipelineError(
                "STAGE_FAILED",
                stage,
                f"{stage} failed: {exc}",
            ) from exc
        finally:
            duration_ms = (perf_counter_ns() - started_ns) / 1_000_000
            timings.append(StageTiming(stage, started_ns, duration_ms))

