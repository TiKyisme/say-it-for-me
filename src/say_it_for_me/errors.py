from __future__ import annotations


class SayItForMeError(Exception):
    """Base error with a stable machine-readable code."""

    def __init__(self, code: str, message: str) -> None:
        super().__init__(message)
        self.code = code


class PipelineError(SayItForMeError):
    def __init__(self, code: str, stage: str, message: str) -> None:
        super().__init__(code, message)
        self.stage = stage


class ManifestError(SayItForMeError):
    pass

