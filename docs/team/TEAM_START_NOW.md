# Say It For Me — Start Now

Read time: 5–10 minutes. Start from the `say-it-for-me/` repository root.

## A. Sprint goal

The deliverable is a complete Phase 2 Technical Proposal, ready for PDF export and submission by **21/08/2026**. Code, datasets, device checks, and benchmarks exist to produce honest proposal evidence—not to delay the proposal.

Nearest technical milestone: **M1 real VI→KO evidence slice** — a real Vietnamese WAV must produce a Vietnamese transcript, Korean text, and Korean WAV through locally run stages, or the missing stage/fallback must be documented truthfully.

Never turn a target, mock result, diagnostic dataset result, or PC-only result into a measured phone claim.

## B. Team ownership

| Role | Name | Owns |
| :--- | :--- | :--- |
| TL | Team Lead | Technical decisions, integration, scope cuts, claim consistency, final approval. |
| ATE | Nguyễn Tiến Đạt | ASR, VI→KO NMT, model selection/evaluation, technical evidence. |
| AUD | Nguyễn Đăng Gia Đạo | WAV/audio, Korean TTS, phone profile, hardware/device evidence. |
| APP | Hà Duy Lộc | Dataset/evaluator, Korean reviewer, demo, proposal package, submission requirements. |

## C. Start immediately

| Owner | P0 first actions | Nearest due date |
| :--- | :--- | :--- |
| TL | Confirm outstanding TL availability/name details; approve the first model and device decisions; keep scope to VI→KO; unblock cross-role dependencies. | 07/08/2026 |
| ATE | Record up to two ASR candidates; run real Vietnamese ASR once WAV exists; record up to two VI→KO NMT candidates; return exact checkpoint/runtime/license data. | Candidate inventory 07/08/2026 |
| AUD | Capture exact phone profile; implement WAV I/O; collect/manage first ten consented Vietnamese WAVs; identify a Korean TTS candidate. | Phone profile 07/08/2026 |
| APP | Clean the 30-row draft dataset; confirm organizer rules; find Korean reviewer; update completion matrix and claim map. | Rules/roster status 07/08/2026 |

## D. End-of-session reporting

Update your role handoff at the end of every session:

```text
COMPLETED
COMMANDS/ACTIONS
RESULTS
FILES CHANGED
EVIDENCE
BLOCKERS
DECISIONS NEEDED FROM TL
NEXT THREE ACTIONS
```

“Xong rồi” is not a handoff. Include artifact paths, commands, raw output/location, and limitations.

## E. Read these files in order

1. `docs/team/TEAM_FACTS.md` — confirmed names, responsibilities, and known gaps.
2. This file — current sprint operating rules.
3. `docs/team/PHASE2_RESCUE_TASKS_3_MEMBERS.md` — complete ownership, outputs, acceptance, deadlines, and evidence locations.
4. Your role handoff under `docs/team/handoffs/` — the work you start now.
5. `docs/evidence_register.md` and `docs/testing/evaluation_contract.md` — what may count as evidence.
6. `docs/technical_proposal_working_draft.md`, relevant ADRs, and code contracts — existing repository baseline.

## F. M1 Definition of Done

By 10/08/2026, show one reproducible Vietnamese WAV → real ASR → real VI→KO NMT → real Korean TTS → Korean WAV slice, with exact models/revisions/licenses, commands, stage timings, and one documented failure. If Korean TTS is unavailable, stop at Korean text, record the blocker/fallback, and do not claim speech output.

## G. Git rules

- Never force push.
- Do not commit model weights, large datasets/audio, credentials, or secrets.
- Follow the current branch workflow; pull/rebase only when required by the remote workflow.
- Use one task branch/commit per coherent change and run relevant tests before handoff.
