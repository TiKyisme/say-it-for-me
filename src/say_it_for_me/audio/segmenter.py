from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from enum import StrEnum
from math import ceil

from ..contracts import AudioBuffer


class SegmentReason(StrEnum):
    END_OF_SPEECH = "end_of_speech"
    MAX_DURATION = "max_duration"
    USER_STOP = "user_stop"


@dataclass(frozen=True, slots=True)
class SegmenterConfig:
    sample_rate_hz: int = 48_000
    frame_ms: int = 20
    pre_roll_ms: int = 200
    end_silence_ms: int = 400
    max_utterance_ms: int = 8_000

    def __post_init__(self) -> None:
        values = (
            self.sample_rate_hz,
            self.frame_ms,
            self.pre_roll_ms,
            self.end_silence_ms,
            self.max_utterance_ms,
        )
        if any(value <= 0 for value in values):
            raise ValueError("segmenter values must be positive")
        if self.max_utterance_ms <= self.end_silence_ms:
            raise ValueError("max utterance must exceed end silence")


@dataclass(frozen=True, slots=True)
class SegmentedUtterance:
    audio: AudioBuffer
    reason: SegmentReason


class VadSegmenter:
    """Collects fixed-size frames and finalizes at VAD or duration boundaries."""

    def __init__(self, config: SegmenterConfig | None = None) -> None:
        self.config = config or SegmenterConfig()
        self._pre_roll: deque[AudioBuffer] = deque(maxlen=self._pre_roll_frames)
        self._active_frames: list[AudioBuffer] = []
        self._trailing_silence_frames = 0

    @property
    def is_active(self) -> bool:
        return bool(self._active_frames)

    @property
    def _pre_roll_frames(self) -> int:
        return ceil(self.config.pre_roll_ms / self.config.frame_ms)

    @property
    def _end_silence_frames(self) -> int:
        return ceil(self.config.end_silence_ms / self.config.frame_ms)

    @property
    def _max_frames(self) -> int:
        return ceil(self.config.max_utterance_ms / self.config.frame_ms)

    def accept(
        self,
        frame: AudioBuffer,
        is_speech: bool,
    ) -> SegmentedUtterance | None:
        self._validate_frame(frame)
        if not self.is_active:
            self._pre_roll.append(frame)
            if not is_speech:
                return None
            self._active_frames = list(self._pre_roll)
            self._pre_roll.clear()
            self._trailing_silence_frames = 0
            return self._finalize_if_max()

        self._active_frames.append(frame)
        self._trailing_silence_frames = (
            0 if is_speech else self._trailing_silence_frames + 1
        )

        max_segment = self._finalize_if_max()
        if max_segment is not None:
            return max_segment
        if self._trailing_silence_frames >= self._end_silence_frames:
            return self._finalize(SegmentReason.END_OF_SPEECH)
        return None

    def stop(self) -> SegmentedUtterance | None:
        if not self.is_active:
            return None
        return self._finalize(SegmentReason.USER_STOP)

    def _finalize_if_max(self) -> SegmentedUtterance | None:
        if len(self._active_frames) >= self._max_frames:
            return self._finalize(SegmentReason.MAX_DURATION)
        return None

    def _finalize(self, reason: SegmentReason) -> SegmentedUtterance:
        samples = tuple(
            sample
            for frame in self._active_frames
            for sample in frame.samples
        )
        result = SegmentedUtterance(
            AudioBuffer(samples, self.config.sample_rate_hz),
            reason,
        )
        self._active_frames.clear()
        self._pre_roll.clear()
        self._trailing_silence_frames = 0
        return result

    def _validate_frame(self, frame: AudioBuffer) -> None:
        if frame.sample_rate_hz != self.config.sample_rate_hz:
            raise ValueError("frame sample rate does not match segmenter config")
        expected_samples = self.config.sample_rate_hz * self.config.frame_ms // 1000
        if len(frame.samples) != expected_samples:
            raise ValueError(
                f"expected {expected_samples} samples per frame, "
                f"received {len(frame.samples)}"
            )

