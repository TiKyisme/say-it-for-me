from __future__ import annotations

import logging
import time
from typing import Literal

import numpy as np
from faster_whisper import WhisperModel

from ..contracts import AudioBuffer, Language, Transcript

logger = logging.getLogger(__name__)

_LANGUAGE_TO_WHISPER = {
    Language.VIETNAMESE: "vi",
    Language.KOREAN: "ko",
}


class WhisperRecognizer:
    """Real ASR adapter using faster-whisper (CTranslate2 backend)."""

    def __init__(
        self,
        model_size: str = "tiny",
        device: Literal["cpu", "cuda"] = "cpu",
        compute_type: str = "int8",
    ) -> None:
        self._model_size = model_size
        self._device = device
        self._compute_type = compute_type
        self._model: WhisperModel | None = None

    def warmup(self) -> None:
        if self._model is not None:
            return
        logger.info(
            "Loading Whisper %s on %s (%s)",
            self._model_size, self._device, self._compute_type,
        )
        self._model = WhisperModel(
            self._model_size,
            device=self._device,
            compute_type=self._compute_type,
        )

    def close(self) -> None:
        self._model = None

    def transcribe(
        self,
        audio: AudioBuffer,
        language: Language,
        utterance_id: str,
    ) -> Transcript:
        if audio.sample_rate_hz != 16_000:
            raise ValueError("ASR input must be 16 kHz mono PCM")

        self.warmup()
        assert self._model is not None

        audio_array = np.array(audio.samples, dtype=np.float32)
        whisper_lang = _LANGUAGE_TO_WHISPER[language]

        start = time.perf_counter_ns()
        segments, info = self._model.transcribe(
            audio_array,
            language=whisper_lang,
            beam_size=5,
            vad_filter=True,
        )
        text = " ".join(seg.text.strip() for seg in segments)
        elapsed_ms = (time.perf_counter_ns() - start) / 1_000_000

        if not text.strip():
            raise ValueError(
                f"Whisper returned empty transcript for utterance {utterance_id} "
                f"(lang={whisper_lang}, duration={audio.duration_ms:.0f}ms)"
            )

        logger.info(
            "ASR done: utterance=%s lang=%s elapsed=%.1fms chars=%d",
            utterance_id, whisper_lang, elapsed_ms, len(text),
        )
        return Transcript(
            utterance_id=utterance_id,
            text=text,
            language=language,
        )
