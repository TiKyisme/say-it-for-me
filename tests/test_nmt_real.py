"""Smoke tests for the real NMT adapters (NLLB and M2M100).

Skipped automatically when transformers/torch is not installed.
"""
from __future__ import annotations

import unittest

from say_it_for_me.contracts import Language, Transcript

try:
    from say_it_for_me.stages.nmt_real import M2M100Translator, NllbTranslator

    _HAS_TRANSFORMERS = True
except ImportError:
    _HAS_TRANSFORMERS = False

_SAMPLE_TRANSCRIPT = Transcript(
    utterance_id="nmt-test-001",
    text="Dừng dây chuyền số 2",
    language=Language.VIETNAMESE,
)


@unittest.skipUnless(_HAS_TRANSFORMERS, "transformers/torch not installed")
class NllbTranslatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.translator = NllbTranslator(device="cpu")
        cls.translator.warmup()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.translator.close()

    def test_translate_vi_to_ko(self) -> None:
        result = self.translator.translate(_SAMPLE_TRANSCRIPT, Language.KOREAN)
        self.assertEqual(result.source_language, Language.VIETNAMESE)
        self.assertEqual(result.target_language, Language.KOREAN)
        self.assertEqual(result.utterance_id, "nmt-test-001")
        self.assertIsInstance(result.translated_text, str)
        self.assertGreater(len(result.translated_text), 0)

    def test_rejects_same_language(self) -> None:
        with self.assertRaisesRegex(ValueError, "must differ"):
            self.translator.translate(_SAMPLE_TRANSCRIPT, Language.VIETNAMESE)


@unittest.skipUnless(_HAS_TRANSFORMERS, "transformers/torch not installed")
class M2M100TranslatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.translator = M2M100Translator(device="cpu")
        cls.translator.warmup()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.translator.close()

    def test_translate_vi_to_ko(self) -> None:
        result = self.translator.translate(_SAMPLE_TRANSCRIPT, Language.KOREAN)
        self.assertEqual(result.source_language, Language.VIETNAMESE)
        self.assertEqual(result.target_language, Language.KOREAN)
        self.assertEqual(result.utterance_id, "nmt-test-001")
        self.assertIsInstance(result.translated_text, str)
        self.assertGreater(len(result.translated_text), 0)


if __name__ == "__main__":
    unittest.main()
