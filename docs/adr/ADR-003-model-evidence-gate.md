# ADR-003 — Models are candidates until they pass evidence and license gates

- **Status:** Accepted
- **Date:** 23/07/2026

## Context

The original PRD selected model names and quoted compressed sizes/latencies without reproducible measurements. Some candidates have non-commercial or research-only caveats, and Korean TTS availability was assumed incorrectly.

## Decision

A model becomes the default only when the repository records:

1. exact checkpoint and revision;
2. runtime and precision;
3. local artifact size and SHA-256;
4. license and intended-use review;
5. quality on the shared evaluation set;
6. cold/warm latency and p50/p95;
7. process RSS before/after load and at peak inference;
8. failure examples and fallback behavior.

NLLB, M2M100, Whisper Tiny/Base, DeepFilterNet, Piper, and Korean TTS checkpoints are candidates under this rule.

## Consequences

- Phase 2 wording distinguishes target, estimate, and measured result.
- Large downloads happen after the evaluation contract is ready.
- Commercialization claims cannot silently rely on research-only artifacts.

