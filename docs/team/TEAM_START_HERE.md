# TEAM START HERE — Say It For Me / Phase 2

> **Version:** 0.2  
> **Last updated:** 27/07/2026  
> **Official deadline:** End of 21/08/2026  
> **Internal upload-ready deadline:** 20/08/2026 18:00 ICT  
> **Current onboarding status:** **BLOCKED ON NAMED ROSTER, HUMAN FACTS AND BASELINE COMMIT**

This is the one-page entry point for every team member. Work from the
`say-it-for-me/` repository root, and resolve every path below from that root.

## 1. Before anyone starts a role

1. TL reviews the current worktree and creates the initial `main` baseline
   commit by **28/07 11:30 ICT**; TL retains its full SHA.
2. From that exact baseline, TL creates and switches to
   `tl/g0-operations`. Every later Gate 0 document edit and APP review handoff
   occurs on that branch, not directly on `main`.
3. TL fills the four names, availability, prompt acknowledgements and the full
   baseline SHA in `docs/team/TEAM_FACTS.md`.
4. Each person confirms exactly one role code: `TL`, `ATE`, `AUD` or `APP`.
5. TL replaces `UNASSIGNED` in all four active cards, the assignment board and
   owned handoff/report headers. Each specialist verifies their own mapping,
   then creates the card branch from the recorded baseline; nobody develops
   directly on `main`.
6. Read, in order:
   `docs/team/TEAM_PLAYBOOK.md` → `docs/team/PHASE2_CALENDAR.md` → the exact
   active-card path in the board below → `docs/team/prompts/00_MASTER_PROJECT_PROMPT.md`
   → the matching role prompt under `docs/team/prompts/`.
7. Use only one active card. Do not start a later gate while the current card
   is unacknowledged or blocked.

Until Steps 1–5 are complete, role work may be read/prepared but no specialist
code/document edit should begin. The specialist card start time is
**28/07 12:00 ICT**.

Onboarding banner states:

- `BLOCKED ON NAMED ROSTER, HUMAN FACTS AND BASELINE COMMIT`: nobody is ready
  to edit yet.
- `ROSTER ASSIGNED — GATE 0 REVIEW PENDING`: named specialists may begin their
  dated card checkpoints; TL's Gate 0 card is still under APP review.
- `READY — GATE 0 PASS`: APP passed the facts/assignment review and TL closed
  Gate 0.

## 2. Current assignment board

| Role | Named DRI | Current card and status | First concrete action | Handoff / review deadline |
|---|---|---|---|---|
| **TL** | **UNASSIGNED — fill TEAM_FACTS** | `docs/team/active/TL_G0_OPERATIONS.md` — `BLOCKED / HUMAN_INPUT_REQUIRED` | Review the worktree; create the `main` baseline by **28/07 11:30**; switch to `tl/g0-operations`; then collect the named facts | TL hands the branch/commit to APP by **29/07 10:00**; APP records `PASS` or `CHANGES_REQUESTED` by **12:00** |
| **APP** | **UNASSIGNED — fill TEAM_FACTS** | `docs/team/active/APP_G2_EVALUATION_FOUNDATION.md` — `REVIEW` | Re-run the documented commands and send `docs/team/handoffs/APP_evaluation_foundation.md` to ATE | APP handoff **29/07 15:00**; ATE review **30/07 11:00**; TL gate **12:00** |
| **ATE** | **UNASSIGNED — fill TEAM_FACTS** | `docs/team/active/ATE_G2_CONTRACT_REVIEW.md` — `NOT_STARTED` | Acknowledge the card and collect exact candidate links; at **29/07 15:00** read APP handoff and run the review | ATE sends review **30/07 11:00**; TL records gate decision **12:00** |
| **AUD** | **UNASSIGNED — fill TEAM_FACTS** | `docs/team/active/AUD_G2_AUDIO_FIXTURES.md` — `NOT_STARTED` | Draft the 48 kHz fixture/noise contract at the exact paths in the card | ATE technical review by **31/07 12:00**; manifest handoff checkpoint **30/07 12:00** |

All times use `Asia/Ho_Chi_Minh` (ICT).

## 3. Which document wins

- **Human assignment and availability:** `docs/team/TEAM_FACTS.md`.
- **Current outcome, paths, status, acceptance and handoff:** the assigned active
  task card.
- **Cross-team milestones and dependency dates:**
  `docs/team/PHASE2_CALENDAR.md`.
- **Stable role boundaries and engineering rules:** the master and role prompts.
- **Product/technical decisions:** the PRD and accepted ADRs.

A role prompt is a reusable summary; it never extends an active-card or calendar
deadline. If an active card and the calendar disagree, stop and ask TL to update
both before continuing.

## 4. Decision rights

- **DRI:** one person who executes, keeps status current and raises blockers.
- **Reviewer:** independently checks the command, threshold, edge case and
  evidence; records `PASS` or `CHANGES_REQUESTED` in the card.
- **TL / gate decision owner:** accepts or rejects the system gate after the
  named reviews. TL cannot mark a TL-authored card `DONE` without the named
  reviewer recording `PASS`.

Specialists own the correctness and timely handoff of their artifacts. TL
retains final accountability for cross-module architecture, proposal claims and
submission.

## 5. Start-of-session prompt packet

Give an AI copilot exactly:

1. `docs/team/prompts/00_MASTER_PROJECT_PROMPT.md`;
2. one matching prompt under `docs/team/prompts/`;
3. the one exact current active-card path from the assignment board.

Then state: `Execute the next unchecked step and update only the files this card
authorizes.`

Do not paste all four role prompts into one session.

## 6. Verification record

The current documentation packet passed a context-free reader test. Evidence:
`docs/team/READER_TEST_2026-07-27.md`.
