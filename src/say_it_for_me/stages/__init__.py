from .mock import (
    DictionaryTranslator,
    PassthroughDenoiser,
    ScriptedRecognizer,
    SimpleResampler,
    ToneSynthesizer,
)

__all__ = [
    "DictionaryTranslator",
    "PassthroughDenoiser",
    "ScriptedRecognizer",
    "SimpleResampler",
    "ToneSynthesizer",
    "WhisperRecognizer",
    "NllbTranslator",
    "M2M100Translator",
]


def __getattr__(name: str):
    if name == "WhisperRecognizer":
        from .asr_real import WhisperRecognizer
        return WhisperRecognizer
    if name == "NllbTranslator":
        from .nmt_real import NllbTranslator
        return NllbTranslator
    if name == "M2M100Translator":
        from .nmt_real import M2M100Translator
        return M2M100Translator
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

