# TEAM PLAYBOOK — Say It For Me / Phase 2

> **Effective:** 27/07/2026  
> **Version:** 0.2; last updated 27/07/2026  
> **Official deadline:** End of 21/08/2026  
> **Internal upload-ready deadline:** 20/08/2026 18:00, Asia/Ho_Chi_Minh  
> **Audience:** All four team members and their AI copilots

## 1. What the team must deliver

By the internal deadline, the team must have:

1. a complete English Technical Proposal matching the organizer template;
2. an evidence-backed architecture for offline Vietnamese ↔ Korean factory communication;
3. reproducible model-selection results or explicitly labelled unverified targets;
4. a credible Qualcomm hardware, memory, power and deployment path;
5. an early PC prototype or vertical slice if technically feasible;
6. a submission package that another member can reproduce and explain.

The proposal is the required deliverable. The prototype is supporting evidence and
must not consume the time needed to submit a coherent proposal.

## 2. Source of truth

Work from the `say-it-for-me/` repository root and resolve every repository path
in these documents from that root. Read in this order before starting work:

1. `docs/team/TEAM_START_HERE.md` — current assignment board.
2. `docs/team/TEAM_PLAYBOOK.md` — ownership and team protocol.
3. `docs/team/PHASE2_CALENDAR.md` and your active task card.
4. Your role prompt in `docs/team/prompts/`.
5. `docs/product/PRD_SayItForMe.md` — product and architecture decisions.
6. `docs/execution_backlog.md` — gates and small tasks.
7. `docs/evidence_register.md` — claims that need proof.
8. `docs/technical_proposal_working_draft.md` — current submission draft.
9. Relevant ADRs and code contracts.

Document authority is field-specific:

- `docs/team/TEAM_FACTS.md` owns named human assignments and availability.
- The active card owns the current task's status, exact paths, acceptance and
  handoff time.
- `docs/team/PHASE2_CALENDAR.md` owns cross-team milestones and dependency dates.
- The role prompts contain stable boundaries and must not extend a card/calendar
  deadline.
- The newest explicit decision in the PRD or an accepted ADR owns product and
  technical choices.

If a card and calendar conflict, stop and ask TL to update both; do not choose a
more convenient date silently.

## 3. Roles and outcomes

| Code | Role | Accountable outcome |
|---|---|---|
| **TL** | Team Lead / System Architect | One coherent architecture, integrated pipeline, defensible proposal and on-time submission |
| **ATE** | ASR & Translation Engineer | Evidence-based ASR/NMT selection and production-quality adapters |
| **AUD** | Audio & TTS Engineer | Correct audio contracts, noise/VAD/TTS evidence and reliable audio I/O |
| **APP** | App & Integration Engineer | Reproducible evaluation data/harness, direction-first UI and demo/submission assets |

“Accountable outcome” here means specialist artifact ownership: the DRI must
know whether their deliverable is done, know the evidence location, and escalate
before a dependency becomes late. In the RACI below, TL remains accountable for
the cross-module gate, proposal claim and submission decision.

## 4. RACI

`A` = accountable, `R` = executes, `C` = consulted/reviews, `I` = informed.

| Workstream | TL | ATE | AUD | APP |
|---|:---:|:---:|:---:|:---:|
| Scope, architecture and ADRs | A/R | C | C | C |
| Dataset schema/provenance | A | C | C | R |
| Evaluation harness | A | C | I | R |
| ASR candidate spike | A | R | C | C |
| NMT candidate spike | A | R | I | C |
| Denoise/VAD/resampling | A | C | R | I |
| Vietnamese/Korean TTS | A | I | R | C |
| Pipeline integration | A/R | R | R | R |
| UI and demo workflow | A | C | C | R |
| Hardware/BOM/power | A/R | C | R | C |
| Business/problem sections | A | C | C | R |
| Technical Proposal final merge | A/R | C | C | C |
| Korean reviewer coordination | A | C | C | R |
| Submission/export/upload | A | I | I | R |

## 5. File ownership

This ownership prevents merge conflicts; it does not prevent review.

| Owner | May edit directly | Contributes through a handoff note |
|---|---|---|
| TL | `src/say_it_for_me/pipeline.py`, `src/say_it_for_me/model_store.py`, `docs/adr/`, workspace PRD, proposal master, evidence register | — |
| ATE | `src/say_it_for_me/stages/` ASR/NMT adapters, `reports/asr/` (create as needed), `reports/nmt/` (create as needed), ASR/NMT tests | Proposal Sections 4.2–4.4 |
| AUD | `src/say_it_for_me/audio/`, denoiser/TTS adapters, `reports/audio/` (create as needed), `reports/tts/` (create as needed) | Proposal Sections 4.1, 4.4 and 5.2 |
| APP | `src/say_it_for_me/evaluation/`, `src/say_it_for_me/app/` (create when its card starts), `datasets/` (create only after provenance approval), evaluation/UI tests, demo assets | Proposal Sections 2, 3 and UX/timeline content |

Only TL merges contributions into
`docs/technical_proposal_working_draft.md`. Each
specialist submits proposal text in `docs/team/handoffs/<ROLE>_proposal_input.md`.

## 6. Calendar and gates

### 27–31/07 — Foundation

**Team milestone:** role ownership confirmed; repository workflow agreed; evaluation
contract runs; exact candidate checkpoints and device availability are recorded.

- TL: resolve organizer constraints, team metadata, device access, CI and proposal outline.
- ATE: prepare ASR/NMT runner design and exact candidate inventory.
- AUD: prepare audio/noise fixtures, WAV adapter plan and exact TTS candidate inventory.
- APP: own dataset schema, evaluation CLI, provenance rules and UI wireframe.

### 01–07/08 — Model evidence

**Team milestone:** candidate reports exist for ASR, NMT, denoise and both TTS
languages. Reports include quality, latency, memory, size, license and failures.

- ATE: ASR report by 04/08; NMT report by 07/08.
- AUD: denoiser/VAD report by 04/08; VI/KO TTS report by 07/08.
- APP: smoke/general/manufacturing evaluation sets and Korean review coordination.
- TL: license/hardware gates and decision ADRs.

### 08–12/08 — Real PC one-direction vertical slice

**Team milestone:** real adapter integration begins by 10/08; the complete
`VI→KO` file pipeline passes G6 by 12/08, or a documented fallback is activated.

- TL: orchestrator and integration order.
- ATE: real ASR/NMT adapters and failure handling.
- AUD: WAV/microphone, denoise/resample, TTS and playback adapters.
- APP: direction-first UI, trace display and evaluation integration.

### 13–16/08 — Evidence and proposal v0.8

**Team milestone:** `KO→VI` integration candidate and bidirectional rehearsal by
14/08; then 30-run stability evidence, hardware/BOM table, demo scenario and
proposal v0.8 by 16/08.

### 17–18/08 — Content freeze and reader test

No new model or architecture unless TL declares a submission blocker. Each owner
approves their facts, numbers, links and failure statements. A fresh reader must be
able to answer the reader questions in Section 11.

### 19–20/08 — Package and internal submission

Render diagrams, export PDF/DOCX, validate links, run checklist and prepare the
Google Form upload. Upload-ready package is due 20/08 18:00.

### 21/08 — Contingency

Only upload recovery or critical corrections. Save submission confirmation.

## 7. Daily operating rhythm

- **09:00 async update:** yesterday / today / blocker / artifact link.
- **17:30 integration check:** owner reports PASS/FAIL against current gate.
- **Monday 30 min:** dependencies, capacity and risks.
- **Wednesday 30 min:** integration and evidence review.
- **Friday 45 min:** demo current build and approve/reject gate.

No meeting is complete without an owner, action, due date and output location.

Every member works from exactly one active card at a time. Use
`docs/team/ACTIVE_TASK_CARD_TEMPLATE.md`; current assignments live in
`docs/team/active/`.

The DRI writes the artifact and keeps the card current. The named reviewer runs
or inspects the acceptance evidence and records `PASS` or
`CHANGES_REQUESTED` in the card. TL records the cross-team gate decision after
required reviews; TL may not mark a TL-authored card `DONE` without its named
reviewer recording `PASS`.

## 8. Definition of Done for every task

A task is `DONE` only when all applicable items are true:

- output exists at the agreed path;
- exact command to reproduce it is documented;
- success and at least one failure/edge case are tested;
- model/runtime/data versions and licenses are recorded;
- measurements state hardware, warm-up count, run count and p50/p95 where relevant;
- target, estimate and measured result are visibly distinguished;
- dependent owner has acknowledged the handoff;
- no private/raw audio was committed accidentally.

“Code runs on my machine” and “document drafted” are not sufficient.

## 9. Blocker protocol

Raise a blocker as soon as any of these is true:

- dependency is more than four working hours late;
- expected model/download/runtime cannot be reproduced;
- license or intended use is unclear;
- Korean reference or TTS output lacks a qualified reviewer;
- measured p95/RSS misses its gate by more than 25%;
- the task would change a public contract or accepted ADR;
- the owner cannot meet the committed date.

Use this format:

```text
BLOCKER:
Owner:
Blocked deliverable and due date:
Evidence/error:
What I already tried:
Impact if unresolved:
Recommended decision:
Decision needed from:
Decision deadline:
```

Do not hide a blocker by silently changing a model, metric, sample rate or target.

## 10. Handoff format

```text
HANDOFF:
From → To:
Deliverable:
Artifact paths:
Reproduction command:
PASS/FAIL result:
Known limitations:
Decision required:
Next owner/action/date:
```

## 11. Reader-test questions

Before content freeze, a new reader must answer these from the docs alone:

1. What exact factory communication problem is being solved?
2. Why is explicit VI→KO/KO→VI direction used?
3. Where is audio 48 kHz and where is it 16 kHz?
4. How are model artifacts stored, loaded and verified offline?
5. How does chunking reduce latency without unbounded parallel memory?
6. Which models are selected, and which remain candidates?
7. Which claims are measured versus targets?
8. What hardware is proposed and why?
9. What does each team member own this week?
10. What must be complete before 20/08 18:00?

Any wrong or ambiguous answer creates a documentation task owned by TL.
