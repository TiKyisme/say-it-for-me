"""Reproducible, file-based VI→KO real-inference demonstration entry point.

This command deliberately has no mock fallback. A successful run requires a
consented Vietnamese 16 kHz mono PCM WAV and locally usable model runtimes.
"""
from __future__ import annotations

import argparse
import json
import platform
import sys
import wave
from datetime import UTC, datetime
from pathlib import Path
from struct import unpack
from time import perf_counter_ns
from typing import Any

from .contracts import AudioBuffer, Direction, Language, Transcript


def _duration_ms(started_ns: int) -> float:
    return round((perf_counter_ns() - started_ns) / 1_000_000, 3)


def load_pcm16_mono_wav(path: Path) -> AudioBuffer:
    """Load a strict 16 kHz mono, signed PCM-16 WAV for the ASR adapter."""
    if not path.is_file():
        raise FileNotFoundError(f"input WAV does not exist: {path}")
    with wave.open(str(path), "rb") as reader:
        channels = reader.getnchannels()
        sample_rate_hz = reader.getframerate()
        sample_width = reader.getsampwidth()
        frame_count = reader.getnframes()
        compression = reader.getcomptype()
        if compression != "NONE":
            raise ValueError(f"input WAV must be uncompressed PCM, got {compression}")
        if channels != 1:
            raise ValueError(f"input WAV must be mono, got {channels} channels")
        if sample_rate_hz != 16_000:
            raise ValueError(
                f"input WAV must be 16 kHz for the direct demo path, got {sample_rate_hz} Hz"
            )
        if sample_width != 2:
            raise ValueError(
                f"input WAV must use signed PCM-16, got {sample_width * 8}-bit samples"
            )
        raw_pcm = reader.readframes(frame_count)
    if not raw_pcm:
        raise ValueError("input WAV contains no audio frames")
    samples = tuple(sample / 32768.0 for sample in unpack(f"<{frame_count}h", raw_pcm))
    return AudioBuffer(samples=samples, sample_rate_hz=sample_rate_hz)


def _write_text(path: Path, value: str) -> None:
    path.write_text(value + "\n", encoding="utf-8")


def _write_run(path: Path, value: dict[str, Any]) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def run_demo(args: argparse.Namespace) -> int:
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    started_ns = perf_counter_ns()
    run: dict[str, Any] = {
        "schema_version": 1,
        "started_at_utc": datetime.now(UTC).isoformat(),
        "input": str(Path(args.input)),
        "direction": args.direction,
        "asr_model": f"Whisper {args.asr}",
        "asr_runtime": "faster-whisper / CTranslate2",
        "nmt_model": (
            "facebook/m2m100_418M"
            if args.nmt == "m2m100"
            else "facebook/nllb-200-distilled-600M"
        ),
        "nmt_runtime": "transformers / PyTorch",
        "hardware": platform.machine(),
        "os": platform.platform(),
        "python": sys.version,
        "network_status": "NOT_VERIFIED",
        "tts_status": "NOT_IMPLEMENTED",
        "stage_timings_ms": {},
        "total_ms": None,
        "status": "STARTED",
        "failure": None,
    }
    stage = "input_validation"
    try:
        stage_started = perf_counter_ns()
        audio = load_pcm16_mono_wav(Path(args.input))
        run["stage_timings_ms"][stage] = _duration_ms(stage_started)

        from .stages.asr_real import WhisperRecognizer
        from .stages.nmt_real import M2M100Translator, NllbTranslator

        stage = "asr_model_provisioning_or_load"
        recognizer = WhisperRecognizer(model_size=args.asr, device=args.device)
        stage_started = perf_counter_ns()
        recognizer.warmup()
        run["stage_timings_ms"][stage] = _duration_ms(stage_started)

        stage = "asr_inference"
        stage_started = perf_counter_ns()
        transcript = recognizer.transcribe(audio, Language.VIETNAMESE, "demo-vi-001")
        run["stage_timings_ms"][stage] = _duration_ms(stage_started)
        recognizer.close()

        stage = "nmt_model_provisioning_or_load"
        translator = M2M100Translator(device=args.device) if args.nmt == "m2m100" else NllbTranslator(device=args.device)
        stage_started = perf_counter_ns()
        translator.warmup()
        run["stage_timings_ms"][stage] = _duration_ms(stage_started)

        stage = "nmt_inference"
        stage_started = perf_counter_ns()
        translation = translator.translate(transcript, Language.KOREAN)
        run["stage_timings_ms"][stage] = _duration_ms(stage_started)
        translator.close()

        _write_text(output_dir / "transcript_vi.txt", transcript.text)
        _write_text(output_dir / "translation_ko.txt", translation.translated_text)
        run["status"] = "SUCCESS"
    except Exception as exc:
        run["status"] = "FAILED"
        run["failure"] = {"stage": stage, "type": type(exc).__name__, "message": str(exc)}
    finally:
        run["total_ms"] = _duration_ms(started_ns)
        _write_run(output_dir / "run.json", run)

    if run["status"] != "SUCCESS":
        print(json.dumps(run, ensure_ascii=False), file=sys.stderr)
        return 1
    print(json.dumps(run, ensure_ascii=False))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the real VI→KO ASR/NMT file demo.")
    parser.add_argument("--direction", choices=[Direction.VI_TO_KO.value], required=True)
    parser.add_argument("--input", required=True, help="Consented Vietnamese 16 kHz mono PCM WAV")
    parser.add_argument("--asr", choices=["tiny", "base"], default="tiny")
    parser.add_argument("--nmt", choices=["m2m100", "nllb"], default="m2m100")
    parser.add_argument("--device", choices=["cpu", "cuda"], default="cpu")
    parser.add_argument("--output-dir", required=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    return run_demo(build_parser().parse_args(argv))


if __name__ == "__main__":
    raise SystemExit(main())
