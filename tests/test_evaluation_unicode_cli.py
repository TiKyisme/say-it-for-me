from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


def write_ascii_jsonl(
    path: Path,
    records: list[dict[str, object]],
) -> None:
    path.write_text(
        "".join(
            json.dumps(record, ensure_ascii=True) + "\n"
            for record in records
        ),
        encoding="utf-8",
    )


class EvaluationUnicodeCliTests(unittest.TestCase):
    def test_escaped_lone_surrogate_returns_structured_error(self) -> None:
        repository_root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            references = root / "references.jsonl"
            predictions = root / "predictions.jsonl"
            write_ascii_jsonl(
                references,
                [
                    {
                        "id": "unicode-001",
                        "direction": "vi-ko",
                        "source": "Stop line 2.\ud800",
                        "reference": "Stop line 2.",
                        "domain": "manufacturing-safety",
                        "safety_critical": True,
                        "protected_tokens": ["2"],
                        "provenance": "team-authored:unicode-cli-test",
                        "license": "team-owned",
                        "review_status": "approved",
                    }
                ],
            )
            write_ascii_jsonl(
                predictions,
                [{"id": "unicode-001", "prediction": "Stop line 2."}],
            )
            environment = os.environ.copy()
            environment["PYTHONPATH"] = str(repository_root / "src")

            completed = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "say_it_for_me.evaluation",
                    "evaluate",
                    "--references",
                    str(references),
                    "--predictions",
                    str(predictions),
                ],
                cwd=repository_root,
                env=environment,
                capture_output=True,
                text=True,
                encoding="utf-8",
                check=False,
            )

            self.assertEqual(completed.returncode, 2)
            self.assertEqual(completed.stdout, "")
            self.assertNotIn("UnicodeEncodeError", completed.stderr)
            payload = json.loads(completed.stderr)
            self.assertEqual(
                payload,
                {
                    "error": {
                        "code": "UNSAFE_UNICODE_CATEGORY",
                        "message": (
                            "source contains disallowed Unicode category Cs "
                            "at character index 12 (U+D800)"
                        ),
                        "path": str(references),
                        "line": 1,
                        "field": "source",
                    }
                },
            )


if __name__ == "__main__":
    unittest.main()
