# AUD Handoff — Nguyễn Đăng Gia Đạo

**Role:** Audio, TTS & Device Engineer  
**Initial status:** NOT STARTED  
**Current objective:** establish real WAV/device facts and Korean TTS evidence for M1 and Sections 4–6.

## P0 tasks

1. Capture the exact phone profile: model, About Phone evidence, SoC, RAM, storage, OS, battery, and debug/sideload capability.
2. Implement/test WAV input and output; collect or manage the first ten consented Vietnamese WAV clips with manifest and conditions.
3. Record and run a Korean TTS candidate; retain exact voice/checkpoint/runtime/license/size, Korean WAV, timing, and one failure.

## Inputs

- Audio buffer and segmenter contracts; mock TTS baseline; phone-first proposal requirements.
- Draft WAV collection manifest and 30-row domain draft.

## Missing inputs

- Physical phone profile and consented audio.
- Korean TTS candidate/artifact/license and reviewer availability.
- Actual device power, thermal, and memory measurements.

## Required output and acceptance

- `src/say_it_for_me/audio/` has reproducible WAV I/O with tests.
- `reports/audio/`, `reports/tts/ko/`, and `reports/hardware/` retain raw output and device/source facts.
- A genuine Korean WAV or a documented blocker/fallback exists by 10/08/2026.
- No custom hardware, battery, or phone performance is invented; PC evidence is not labelled as phone evidence.

**Nearest deadline:** phone profile — 07/08/2026; WAV path/clips — 08/08/2026; Korean TTS evidence — 10/08/2026.  
**Evidence location:** `reports/audio/`, `reports/tts/ko/`, `reports/hardware/`, this file.

## Blocker report

```text
BLOCKER
Owner: AUD — Nguyễn Đăng Gia Đạo
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
