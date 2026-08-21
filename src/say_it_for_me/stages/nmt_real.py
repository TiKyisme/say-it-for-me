from __future__ import annotations

import logging
import time
from typing import Literal

import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

from ..contracts import Language, Transcript, Translation

logger = logging.getLogger(__name__)

_NLLB_LANG_CODES = {
    Language.VIETNAMESE: "vie_Latn",
    Language.KOREAN: "kor_Hang",
}

_M2M100_LANG_CODES = {
    Language.VIETNAMESE: "vi",
    Language.KOREAN: "ko",
}


def _validate_request(transcript: Transcript, target_language: Language) -> None:
    if transcript.language is target_language:
        raise ValueError("translation source and target languages must differ")
    if not transcript.text.strip():
        raise ValueError("translation input text must not be empty")


def _require_translation_output(text: str, model_name: str) -> str:
    if not text.strip():
        raise ValueError(f"{model_name} returned an empty translation")
    return text


class NllbTranslator:
    """Real NMT adapter using facebook/nllb-200-distilled-600M."""

    CHECKPOINT = "facebook/nllb-200-distilled-600M"

    def __init__(
        self,
        device: Literal["cpu", "cuda"] = "cpu",
        max_length: int = 256,
    ) -> None:
        self._device = device
        self._max_length = max_length
        self._model = None
        self._tokenizer = None

    def warmup(self) -> None:
        if self._model is not None:
            return
        logger.info("Loading NLLB-200 distilled 600M on %s", self._device)
        self._tokenizer = AutoTokenizer.from_pretrained(self.CHECKPOINT)
        self._model = AutoModelForSeq2SeqLM.from_pretrained(self.CHECKPOINT)
        if self._device == "cuda":
            self._model = self._model.half().cuda()
        self._model.eval()

    def close(self) -> None:
        self._model = None
        self._tokenizer = None

    def translate(
        self,
        transcript: Transcript,
        target_language: Language,
    ) -> Translation:
        _validate_request(transcript, target_language)
        self.warmup()
        assert self._model is not None and self._tokenizer is not None

        src_code = _NLLB_LANG_CODES[transcript.language]
        tgt_code = _NLLB_LANG_CODES[target_language]

        self._tokenizer.src_lang = src_code
        inputs = self._tokenizer(
            transcript.text, return_tensors="pt", truncation=True, max_length=self._max_length
        )
        if self._device == "cuda":
            inputs = {k: v.cuda() for k, v in inputs.items()}

        forced_bos = self._tokenizer.convert_tokens_to_ids(tgt_code)

        start = time.perf_counter_ns()
        with torch.no_grad():
            generated = self._model.generate(
                **inputs,
                forced_bos_token_id=forced_bos,
                max_new_tokens=self._max_length,
            )
        translated_text = _require_translation_output(
            self._tokenizer.decode(generated[0], skip_special_tokens=True), "NLLB"
        )
        elapsed_ms = (time.perf_counter_ns() - start) / 1_000_000

        logger.info(
            "NMT done (NLLB): %s→%s elapsed=%.1fms",
            src_code, tgt_code, elapsed_ms,
        )
        return Translation(
            utterance_id=transcript.utterance_id,
            source_text=transcript.text,
            translated_text=translated_text,
            source_language=transcript.language,
            target_language=target_language,
        )


class M2M100Translator:
    """Real NMT adapter using facebook/m2m100_418M (MIT license)."""

    CHECKPOINT = "facebook/m2m100_418M"

    def __init__(
        self,
        device: Literal["cpu", "cuda"] = "cpu",
        max_length: int = 256,
    ) -> None:
        self._device = device
        self._max_length = max_length
        self._model = None
        self._tokenizer = None

    def warmup(self) -> None:
        if self._model is not None:
            return
        logger.info("Loading M2M100-418M on %s", self._device)
        from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

        self._tokenizer = M2M100Tokenizer.from_pretrained(self.CHECKPOINT)
        self._model = M2M100ForConditionalGeneration.from_pretrained(self.CHECKPOINT)
        if self._device == "cuda":
            self._model = self._model.half().cuda()
        self._model.eval()

    def close(self) -> None:
        self._model = None
        self._tokenizer = None

    def translate(
        self,
        transcript: Transcript,
        target_language: Language,
    ) -> Translation:
        _validate_request(transcript, target_language)
        self.warmup()
        assert self._model is not None and self._tokenizer is not None

        src_code = _M2M100_LANG_CODES[transcript.language]
        tgt_code = _M2M100_LANG_CODES[target_language]

        self._tokenizer.src_lang = src_code
        inputs = self._tokenizer(
            transcript.text, return_tensors="pt", truncation=True, max_length=self._max_length
        )
        if self._device == "cuda":
            inputs = {k: v.cuda() for k, v in inputs.items()}

        forced_bos = self._tokenizer.get_lang_id(tgt_code)

        start = time.perf_counter_ns()
        with torch.no_grad():
            generated = self._model.generate(
                **inputs,
                forced_bos_token_id=forced_bos,
                max_new_tokens=self._max_length,
            )
        translated_text = _require_translation_output(
            self._tokenizer.decode(generated[0], skip_special_tokens=True), "M2M100"
        )
        elapsed_ms = (time.perf_counter_ns() - start) / 1_000_000

        logger.info(
            "NMT done (M2M100): %s→%s elapsed=%.1fms",
            src_code, tgt_code, elapsed_ms,
        )
        return Translation(
            utterance_id=transcript.utterance_id,
            source_text=transcript.text,
            translated_text=translated_text,
            source_language=transcript.language,
            target_language=target_language,
        )
