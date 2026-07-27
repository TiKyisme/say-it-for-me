from __future__ import annotations

import hashlib
import json
import re
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from time import perf_counter_ns
from typing import Any, Generic, TypeVar

from .errors import ManifestError

T = TypeVar("T")
SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")


@dataclass(frozen=True, slots=True)
class ModelSpec:
    id: str
    stage: str
    version: str
    relative_path: str
    sha256: str | None
    license: str
    runtime: str
    precision: str
    directions: tuple[str, ...]

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> ModelSpec:
        required = {
            "id",
            "stage",
            "version",
            "relative_path",
            "license",
            "runtime",
            "precision",
            "directions",
        }
        missing = sorted(required - value.keys())
        if missing:
            raise ManifestError(
                "INVALID_MANIFEST",
                f"model entry is missing fields: {', '.join(missing)}",
            )
        return cls(
            id=str(value["id"]),
            stage=str(value["stage"]),
            version=str(value["version"]),
            relative_path=str(value["relative_path"]),
            sha256=value.get("sha256"),
            license=str(value["license"]),
            runtime=str(value["runtime"]),
            precision=str(value["precision"]),
            directions=tuple(str(item) for item in value["directions"]),
        )


class ModelManifest:
    def __init__(
        self,
        specs: tuple[ModelSpec, ...],
        artifact_root: Path,
        schema_version: int,
    ) -> None:
        self.specs = specs
        self.artifact_root = artifact_root.resolve()
        self.schema_version = schema_version
        self._by_id = {spec.id: spec for spec in specs}
        if len(self._by_id) != len(specs):
            raise ManifestError("INVALID_MANIFEST", "model IDs must be unique")

    @classmethod
    def load(
        cls,
        manifest_path: Path,
        artifact_root: Path | None = None,
    ) -> ModelManifest:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
        if data.get("schema_version") != 1:
            raise ManifestError(
                "UNSUPPORTED_MANIFEST",
                f"unsupported schema_version: {data.get('schema_version')}",
            )
        raw_models = data.get("models")
        if not isinstance(raw_models, list):
            raise ManifestError("INVALID_MANIFEST", "models must be a list")
        specs = tuple(ModelSpec.from_dict(item) for item in raw_models)
        return cls(
            specs,
            artifact_root or manifest_path.parent,
            schema_version=1,
        )

    def get(self, model_id: str) -> ModelSpec:
        try:
            return self._by_id[model_id]
        except KeyError as exc:
            raise ManifestError(
                "MODEL_NOT_DECLARED",
                f"model is not declared in the manifest: {model_id}",
            ) from exc

    def resolve_path(self, spec: ModelSpec) -> Path:
        candidate = (self.artifact_root / spec.relative_path).resolve()
        try:
            candidate.relative_to(self.artifact_root)
        except ValueError as exc:
            raise ManifestError(
                "INVALID_MODEL_PATH",
                f"model path escapes artifact root: {spec.relative_path}",
            ) from exc
        return candidate

    def verify(self, model_id: str) -> Path:
        spec = self.get(model_id)
        path = self.resolve_path(spec)
        if not path.is_file():
            raise ManifestError(
                "MODEL_FILE_MISSING",
                f"model artifact does not exist: {path}",
            )
        if spec.sha256 is None or not SHA256_PATTERN.fullmatch(spec.sha256):
            raise ManifestError(
                "CHECKSUM_REQUIRED",
                f"valid SHA-256 is required for model: {model_id}",
            )
        actual = _sha256(path)
        if actual != spec.sha256:
            raise ManifestError(
                "CHECKSUM_MISMATCH",
                f"checksum mismatch for model: {model_id}",
            )
        return path

    def readiness_issues(self) -> tuple[str, ...]:
        issues: list[str] = []
        for spec in self.specs:
            try:
                self.verify(spec.id)
            except ManifestError as exc:
                issues.append(f"{spec.id}: {exc.code}: {exc}")
        return tuple(issues)


@dataclass(frozen=True, slots=True)
class LoadedModel(Generic[T]):
    value: T
    load_duration_ms: float


class ModelManager:
    """Lazy model loader that validates local artifacts before first query."""

    def __init__(self, manifest: ModelManifest) -> None:
        self._manifest = manifest
        self._loaders: dict[str, Callable[[Path, ModelSpec], Any]] = {}
        self._loaded: dict[str, LoadedModel[Any]] = {}

    def register(
        self,
        model_id: str,
        loader: Callable[[Path, ModelSpec], T],
    ) -> None:
        self._manifest.get(model_id)
        self._loaders[model_id] = loader

    def get(self, model_id: str) -> LoadedModel[Any]:
        if model_id in self._loaded:
            return self._loaded[model_id]
        if model_id not in self._loaders:
            raise ManifestError(
                "LOADER_NOT_REGISTERED",
                f"no loader registered for model: {model_id}",
            )

        spec = self._manifest.get(model_id)
        path = self._manifest.verify(model_id)
        started_ns = perf_counter_ns()
        value = self._loaders[model_id](path, spec)
        loaded = LoadedModel(
            value=value,
            load_duration_ms=(perf_counter_ns() - started_ns) / 1_000_000,
        )
        self._loaded[model_id] = loaded
        return loaded

    def unload(self, model_id: str) -> None:
        loaded = self._loaded.pop(model_id, None)
        if loaded is None:
            return
        close = getattr(loaded.value, "close", None)
        if callable(close):
            close()

    def close(self) -> None:
        for model_id in tuple(self._loaded):
            self.unload(model_id)


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as artifact:
        for block in iter(lambda: artifact.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()

