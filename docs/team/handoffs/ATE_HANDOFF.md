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

### 19/08/2026 16:00 ICT

COMPLETED
- ASR candidate comparison report (Whisper Tiny vs Base) with full metadata/license
- NMT candidate comparison report (NLLB-200 distilled 600M vs M2M100-418M) with full metadata/license
- Real ASR adapter (WhisperRecognizer) using faster-whisper / CTranslate2
- Real NMT adapters (NllbTranslator, M2M100Translator) using transformers
- Smoke tests for both adapters
- requirements-inference.txt with all inference dependencies
- Wired adapters into stages/__init__.py via lazy imports

COMMANDS/ACTIONS
- Created adapter code conforming to SpeechRecognizer and Translator protocols
- Used lazy __getattr__ in __init__.py to avoid importing heavy deps at package load

RESULTS
- Both adapters pass type contract (accept AudioBuffer/Transcript, return Transcript/Translation)
- Tests skip gracefully when deps not installed

FILES CHANGED
- reports/asr/ASR_CANDIDATE_COMPARISON.md (new)
- reports/nmt/NMT_CANDIDATE_COMPARISON.md (new)
- src/say_it_for_me/stages/asr_real.py (new)
- src/say_it_for_me/stages/nmt_real.py (new)
- src/say_it_for_me/stages/__init__.py (modified)
- tests/test_asr_real.py (new)
- tests/test_nmt_real.py (new)
- requirements-inference.txt (new)

EVIDENCE
- reports/asr/ASR_CANDIDATE_COMPARISON.md
- reports/nmt/NMT_CANDIDATE_COMPARISON.md

BLOCKERS
- No real WAV from AUD yet — cannot produce real ASR transcript evidence
- NLLB CC-BY-NC-4.0 license — TL must decide if competition use is permitted

DECISIONS NEEDED FROM TL
- License decision on NLLB-200 CC-BY-NC-4.0 vs M2M100 MIT for baseline NMT
- Approve candidate inventory to move to real evaluation phase

NEXT THREE ACTIONS
1. Run real ASR on Vietnamese WAV once AUD delivers clips
2. Run real NMT on ASR output and record predictions + timing
3. Produce CER/WER and chrF++ metrics on evaluation sentences
