from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from say_it_for_me.cli import build_mock_pipeline  # noqa: E402
from say_it_for_me.contracts import AudioBuffer, Direction  # noqa: E402


def percentile(values: list[float], quantile: float) -> float:
    ordered = sorted(values)
    index = min(len(ordered) - 1, round((len(ordered) - 1) * quantile))
    return ordered[index]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--runs", type=int, default=30)
    args = parser.parse_args()
    if args.runs < 1:
        raise SystemExit("--runs must be positive")

    audio = AudioBuffer((0.0,) * 48_000, 48_000)
    pipeline = build_mock_pipeline("Dừng dây chuyền số 2")
    durations = [
        pipeline.process(audio, Direction.VI_TO_KO).trace.total_ms
        for _ in range(args.runs)
    ]
    print(
        json.dumps(
            {
                "kind": "mock-architecture-overhead-only",
                "runs": args.runs,
                "p50_ms": percentile(durations, 0.50),
                "p95_ms": percentile(durations, 0.95),
                "max_ms": max(durations),
                "mean_ms": statistics.fmean(durations),
                "warning": "Do not use these results as AI performance evidence.",
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

