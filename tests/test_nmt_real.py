"""Adapter-boundary tests and opt-in smoke tests for real NMT adapters."""
from __future__ import annotations

import os
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
class NmtTranslatorBoundaryTests(unittest.TestCase):
    def test_rejects_same_language(self) -> None:
        for translator_type in (NllbTranslator, M2M100Translator):
            with self.subTest(translator=translator_type.__name__):
                with self.assertRaisesRegex(ValueError, "must differ"):
                    translator_type(device="cpu").translate(
                        _SAMPLE_TRANSCRIPT, Language.VIETNAMESE
                    )

    @unittest.skipUnless(
        os.getenv("RUN_REAL_INFERENCE_SMOKE") == "1",
        "set RUN_REAL_INFERENCE_SMOKE=1 to permit local NMT model smoke tests",
    )
    def test_m2m100_translate_vi_to_ko(self) -> None:
        translator = M2M100Translator(device="cpu")
        result = translator.translate(_SAMPLE_TRANSCRIPT, Language.KOREAN)
        translator.close()
        self.assertEqual(result.source_language, Language.VIETNAMESE)
        self.assertEqual(result.target_language, Language.KOREAN)
        self.assertEqual(result.utterance_id, "nmt-test-001")
        self.assertIsInstance(result.translated_text, str)
        self.assertGreater(len(result.translated_text), 0)


if __name__ == "__main__":
    unittest.main()
