from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from say_it_for_me.errors import ManifestError
from say_it_for_me.model_store import ModelManager, ModelManifest


class ClosableModel:
    def __init__(self, value: bytes) -> None:
        self.value = value
        self.closed = False

    def close(self) -> None:
        self.closed = True


class ModelStoreTests(unittest.TestCase):
    def test_verifies_checksum_and_lazy_loads_once(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            artifact = root / "model.bin"
            artifact.write_bytes(b"local-offline-model")
            digest = hashlib.sha256(artifact.read_bytes()).hexdigest()
            manifest_path = root / "manifest.json"
            manifest_path.write_text(
                json.dumps(
                    {
                        "schema_version": 1,
                        "models": [
                            {
                                "id": "test-model",
                                "stage": "asr",
                                "version": "1",
                                "relative_path": "model.bin",
                                "sha256": digest,
                                "license": "test-only",
                                "runtime": "test",
                                "precision": "test",
                                "directions": ["vi-ko"],
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )

            manifest = ModelManifest.load(manifest_path)
            manager = ModelManager(manifest)
            load_count = 0

            def loader(path: Path, _spec: object) -> ClosableModel:
                nonlocal load_count
                load_count += 1
                return ClosableModel(path.read_bytes())

            manager.register("test-model", loader)
            first = manager.get("test-model")
            second = manager.get("test-model")

            self.assertIs(first, second)
            self.assertEqual(load_count, 1)
            self.assertEqual(first.value.value, b"local-offline-model")
            manager.close()
            self.assertTrue(first.value.closed)

    def test_rejects_path_that_escapes_artifact_root(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest_path = root / "manifest.json"
            manifest_path.write_text(
                json.dumps(
                    {
                        "schema_version": 1,
                        "models": [
                            {
                                "id": "escape",
                                "stage": "asr",
                                "version": "1",
                                "relative_path": "../outside.bin",
                                "sha256": "0" * 64,
                                "license": "test",
                                "runtime": "test",
                                "precision": "test",
                                "directions": ["vi-ko"],
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )
            manifest = ModelManifest.load(manifest_path)

            with self.assertRaises(ManifestError) as context:
                manifest.resolve_path(manifest.get("escape"))

            self.assertEqual(context.exception.code, "INVALID_MODEL_PATH")


if __name__ == "__main__":
    unittest.main()

