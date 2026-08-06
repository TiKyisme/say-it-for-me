# Phase 2 Rescue Tasks — Confirmed Roster

Last updated: 06/08/2026. Deadline: **21/08/2026**. All dates below are recovery deadlines; a missed task must be reported to TL immediately with evidence and a recommended scope cut.

## ATE — Nguyễn Tiến Đạt — ASR & Translation Engineer

| ID | Priority | Task | Output | Acceptance criteria | Due | Evidence location |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ATE-P0-01 | P0 | Select at most two VI/KO-capable ASR candidates. | Candidate table: exact checkpoint/revision, runtime, precision, artifact size, license, language support. | Every field is sourced or explicitly blocked; no candidate is called selected yet. | 07/08/2026 | `reports/asr/` and `docs/team/handoffs/ATE_HANDOFF.md` |
| ATE-P0-02 | P0 | Run real Vietnamese ASR on WAV input supplied by AUD. | Transcript(s), command, raw log, stage timing, one failure. | Audio is actually decoded; result records PC/phone environment and does not use a mock recognizer. | 08/08/2026 | `reports/asr/` |
| ATE-P0-03 | P0 | Select and run a VI→KO NMT candidate. | Exact language codes, prediction(s), model metadata, license note, timing/failure log. | NMT accepts real Vietnamese text and emits Korean text; limitations are recorded. | 09/08/2026 | `reports/nmt/` |
| ATE-P0-04 | P0 | Supply Section 4 technical input to TL. | Decision note with rejected candidates, fallback, and safe proposal wording. | Every claim maps to raw evidence or a target/proposed label. | 10/08/2026 | `docs/team/handoffs/ATE_HANDOFF.md` |

## AUD — Nguyễn Đăng Gia Đạo — Audio, TTS & Device Engineer

| ID | Priority | Task | Output | Acceptance criteria | Due | Evidence location |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| AUD-P0-01 | P0 | Profile the exact available phone. | Model, About Phone evidence, SoC, RAM, storage, OS, battery details, debug/sideload capability. | Facts come from physical phone/OEM source; unknown fields remain unknown. | 07/08/2026 | `reports/hardware/` and `docs/team/handoffs/AUD_HANDOFF.md` |
| AUD-P0-02 | P0 | Implement reproducible WAV I/O and manage first 10 Vietnamese clips. | Reader/writer, validation test, clip manifest, consent/rights and recording-condition log. | No raw audio is committed by default; test proves WAV data path. | 08/08/2026 | `src/say_it_for_me/audio/`, `reports/audio/` |
| AUD-P0-03 | P0 | Select and run a Korean TTS candidate. | Exact voice/checkpoint/runtime/license/size, Korean WAV, command, first-audio timing, one failure. | Output is actual synthesized speech, not tone/mock; listener review is not claimed until available. | 10/08/2026 | `reports/tts/ko/` |
| AUD-P0-04 | P0 | Deliver hardware/audio input to TL. | Two-option phone/platform comparison plus safe power/device wording. | PC and phone evidence are separated; no unmeasured battery or thermal number. | 10/08/2026 | `docs/team/handoffs/AUD_HANDOFF.md` |

## APP — Hà Duy Lộc — Dataset, Application & Submission Engineer

| ID | Priority | Task | Output | Acceptance criteria | Due | Evidence location |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| APP-P0-01 | P0 | Clean and validate the 30-row VI→KO factory draft. | IDs, directions, source/reference, domain, safety flag, protected tokens, provenance, rights, review state. | Draft Korean remains non-gold until review; evaluator schema differences are documented. | 08/08/2026 | `docs/submission/dataset/` or repo dataset location agreed by TL |
| APP-P0-02 | P0 | Confirm organizer rules and Korean reviewer route. | Source/e-mail record for cutoff, timezone, files, limits, links; reviewer relationship/proficiency/window/status. | Unknown organiser/reviewer facts stay blocked, not inferred. | 09/08/2026 | `docs/team/handoffs/APP_HANDOFF.md` |
| APP-P0-03 | P0 | Maintain proposal controls. | Updated completion matrix, claim map, business/problem sources or hypotheses, and submission checklist. | No unsupported achievement wording; every changed claim has source/status. | Daily; first update 10/08/2026 | `docs/submission/` |
| APP-P0-04 | P0 | Provide Sections 2, 3, 7, and 8 input. | Problem/business validation, reviewer state, team/submission facts, demo state. | Claims are source-backed or explicit hypotheses/limitations. | 14/08/2026 | `docs/team/handoffs/APP_HANDOFF.md` |

## TL — Team Lead — Integration & Approval

| ID | Priority | Task | Output | Acceptance criteria | Due | Evidence location |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| TL-P0-01 | P0 | Confirm remaining team/availability facts and unblock dependencies. | Updated human facts or explicit blockers. | No personal name, skill, device fact, or submission requirement is invented. | 07/08/2026 | `docs/team/TEAM_FACTS.md` |
| TL-P0-02 | P0 | Approve candidate/fallback decisions and preserve VI→KO scope. | Written ASR/NMT/TTS/device decisions and scope cut if needed. | Selection follows evidence/license gate; no unsupported default model. | 10/08/2026 | ADR/evidence register/handoffs |
| TL-P0-03 | P0 | Integrate M1 real VI→KO slice. | Reproducible command, models, stage timings, failure and proposal input. | Evidence distinguishes real/PC/phone/target. | 12/08/2026 | `reports/e2e/` |

## Shared handoff rule

Every role updates its handoff before requesting review: completed work, commands/actions, results, files changed, evidence, blockers, TL decisions needed, and next three actions. AI tools may assist, but ownership stays with the named role and TL.
