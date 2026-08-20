"""Smoke tests for the real NMT adapters (NLLB and M2M100).

Skipped automatically when transformers/torch is not installed or model is unavailable.
"""
from __future__ import annotations

import pytest

from say_it_for_me.contracts import Language, Transcript

try:
    from say_it_for_me.stages.nmt_real import NllbTranslator, M2M100Translator
    _HAS_TRANSFORMERS = True
except ImportError:
    _HAS_TRANSFORMERS = False

pytestmark = pytest.mark.skipif(
    not _HAS_TRANSFORMERS,
    reason="transformers/torch not installed",
)

_SAMPLE_TRANSCRIPT = Transcript(
    utterance_id="nmt-test-001",
    text="Dừng dây chuyền số 2",
    language=Language.VIETNAMESE,
)


class TestNllbTranslatorContract:
    @pytest.fixture(scope="class")
    def translator(self):
        t = NllbTranslator(device="cpu")
        t.warmup()
        yield t
        t.close()

    def test_translate_vi_to_ko(self, translator):
        result = translator.translate(_SAMPLE_TRANSCRIPT, Language.KOREAN)
        assert result.source_language is Language.VIETNAMESE
        assert result.target_language is Language.KOREAN
        assert result.utterance_id == "nmt-test-001"
        assert isinstance(result.translated_text, str)
        assert len(result.translated_text) > 0

    def test_rejects_same_language(self, translator):
        with pytest.raises(ValueError, match="must differ"):
            translator.translate(_SAMPLE_TRANSCRIPT, Language.VIETNAMESE)


class TestM2M100TranslatorContract:
    @pytest.fixture(scope="class")
    def translator(self):
        t = M2M100Translator(device="cpu")
        t.warmup()
        yield t
        t.close()

    def test_translate_vi_to_ko(self, translator):
        result = translator.translate(_SAMPLE_TRANSCRIPT, Language.KOREAN)
        assert result.source_language is Language.VIETNAMESE
        assert result.target_language is Language.KOREAN
        assert result.utterance_id == "nmt-test-001"
        assert isinstance(result.translated_text, str)
        assert len(result.translated_text) > 0
