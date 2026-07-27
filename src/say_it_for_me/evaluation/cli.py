from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Sequence

from .dataset import (
    join_predictions,
    load_predictions,
    load_references,
)
from .metrics import build_evaluation_report
from .schema import EvaluationDataError


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m say_it_for_me.evaluation",
        description="Validate and evaluate Say It For Me prediction JSONL.",
    )
    commands = parser.add_subparsers(dest="command", required=True)
    evaluate = commands.add_parser(
        "evaluate",
        help="join reference/prediction JSONL by ID and emit metrics",
    )
    evaluate.add_argument(
        "--references",
        required=True,
        help="strict reference JSONL path",
    )
    evaluate.add_argument(
        "--predictions",
        required=True,
        help="strict prediction JSONL path",
    )
    evaluate.add_argument(
        "--include-non-approved",
        action="store_true",
        help=(
            "include non-approved references in a diagnostic report; "
            "never use this flag for official proposal metrics"
        ),
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")

    args = build_parser().parse_args(argv)
    try:
        references = load_references(args.references)
        predictions = load_predictions(args.predictions)
        all_pairs = join_predictions(references, predictions)
        report = build_evaluation_report(
            all_pairs,
            include_non_approved=args.include_non_approved,
        )
    except EvaluationDataError as exc:
        print(
            json.dumps({"error": exc.to_dict()}, ensure_ascii=False),
            file=sys.stderr,
        )
        return 2

    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    return 0
