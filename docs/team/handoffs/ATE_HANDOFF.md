# ATE Handoff — Nguyễn Tiến Đạt

**Role:** ASR & Translation Engineer  
**Initial status:** NOT STARTED  
**Current objective:** produce the real ASR and VI→KO NMT evidence required for M1 and Section 4.

## P0 tasks

1. Record up to two ASR candidates with exact checkpoint, revision, runtime, precision, size, VI/KO support, and license.
2. Run real Vietnamese ASR on WAV input supplied by AUD; retain transcript, command, timing, environment, and one failure.
3. Select/run a VI→KO NMT candidate; retain language codes, predictions, runtime/license data, timing, and protected-token failures.

## Inputs

- Existing typed contracts, mock pipeline, evaluator, ASR/NMT inventories, and evidence register.
- Vietnamese WAV files when AUD provides consented inputs.

## Missing inputs

- Real WAV clips until AUD supplies them.
- Exact model artifacts, runtime compatibility evidence, and license review.
- Korean-reviewed references for official quality evidence.

## Required output and acceptance

- `reports/asr/` and `reports/nmt/` contain commands, raw outputs, model metadata, environment, result/failure notes.
- A real model—not a mock—processes the declared input.
- Claims state PC versus phone correctly and never promote diagnostic data to official evidence.
- Section 4 technical wording is supplied to TL by 10/08/2026.

**Nearest deadline:** ASR candidate inventory — 07/08/2026; real ASR — 08/08/2026; real VI→KO NMT — 09/08/2026.  
**Evidence location:** `reports/asr/`, `reports/nmt/`, this file.

## Blocker report

```text
BLOCKER
Owner: ATE — Nguyễn Tiến Đạt
Blocked output / due date:
Command or action tried:
Observed result / error:
Evidence path:
Impact:
Decision needed from TL:
Next action:
```

## Session log

```text
DATE/TIME
COMPLETED
COMMANDS/ACTIONS
RESULTS
FILES CHANGED
EVIDENCE
BLOCKERS
DECISIONS NEEDED FROM TL
NEXT THREE ACTIONS
```
