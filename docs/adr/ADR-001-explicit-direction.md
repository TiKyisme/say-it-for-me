# ADR-001 — Explicit language direction

- **Status:** Accepted
- **Date:** 23/07/2026

## Context

The product supports only Vietnamese ↔ Korean. Automatic language detection adds latency and creates an avoidable failure mode: one wrong classification reverses the translation path and target voice.

## Decision

The user selects `VI → KO` or `KO → VI` before recording. The selected direction is part of every request contract and remains visible in the UI. ASR receives the source language explicitly.

## Consequences

- Faster, deterministic routing and simpler evaluation.
- Direction errors become testable contract violations.
- One extra user action is required.
- Auto-detection may be evaluated later as an optional convenience, never as the only control.

