from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict

from .contracts import AudioBuffer, Direction
from .pipeline import VoiceTranslationPipeline
from .stages import (
    DictionaryTranslator,
    PassthroughDenoiser,
    ScriptedRecognizer,
    SimpleResampler,
    ToneSynthesizer,
)


def build_mock_pipeline(transcript: str) -> VoiceTranslationPipeline:
    return VoiceTranslationPipeline(
        denoiser=PassthroughDenoiser(),
        resampler=SimpleResampler(),
        recognizer=ScriptedRecognizer(transcript),
        translator=DictionaryTranslator(),
        synthesizer=ToneSynthesizer(),
    )


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(
        description="Run the contract-only Say It For Me vertical slice.",
    )
    parser.add_argument(
        "--direction",
        choices=[direction.value for direction in Direction],
        required=True,
    )
    parser.add_argument("--mock-transcript", required=True)
    args = parser.parse_args()

    direction = Direction(args.direction)
    audio = AudioBuffer((0.0,) * 12_000, 48_000)
    result = build_mock_pipeline(args.mock_transcript).process(audio, direction)

    output = {
        "transcript": result.transcript.text,
        "translation": result.translation.translated_text,
        "source_language": result.translation.source_language.value,
        "target_language": result.translation.target_language.value,
        "output_audio": {
            "sample_rate_hz": result.synthesized_audio.audio.sample_rate_hz,
            "duration_ms": result.synthesized_audio.audio.duration_ms,
        },
        "trace": {
            "trace_id": result.trace.trace_id,
            "total_ms": result.trace.total_ms,
            "stages": [asdict(timing) for timing in result.trace.timings],
        },
        "metadata": result.metadata,
        "warning": "MOCK STAGES: not benchmark evidence",
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
