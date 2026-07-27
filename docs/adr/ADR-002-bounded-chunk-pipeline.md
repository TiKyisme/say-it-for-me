# ADR-002 — VAD-aligned, bounded chunk pipeline

- **Status:** Accepted for the PC baseline
- **Date:** 23/07/2026

## Context

Whole-conversation processing delays feedback and can grow memory. Fixed-time chunking can split words and remove context. Unbounded parallel model inference can increase peak RSS and thermal load on an edge device.

## Decision

- Capture 48 kHz mono audio in 20 ms frames.
- Keep a 200 ms pre-roll ring buffer.
- Prefer VAD/silence boundaries.
- Use an initial 400 ms end-silence threshold and 8 s hard maximum.
- Bound the finalized-segment queue to two.
- Allow capture to continue while one finalized segment is processed.
- Keep one heavy inference request in flight by default.
- Preserve input order and expose concurrency only as a profiled experiment.

## Consequences

- Memory and queueing are predictable.
- Chunk boundary quality must be evaluated.
- Latency can improve without promising unsafe parallelism.
- Defaults may change after noisy-environment measurements.

