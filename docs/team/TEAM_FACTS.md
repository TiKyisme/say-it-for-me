# Phase 2 Rescue Tasks — Say It For Me

**Last updated:** 06/08/2026
**Phase 2 deadline:** 21/08/2026

## Confirmed Team Roles

| Role | Member              | Primary Ownership                                                             |
| :--- | :------------------ | :---------------------------------------------------------------------------- |
| TL   | Team Lead           | Technical decisions, integration, proposal consistency, final approval        |
| ATE  | Nguyễn Tiến Đạt     | ASR, VI–KO translation, model evaluation                                      |
| AUD  | Nguyễn Đăng Gia Đạo | Audio, WAV I/O, Korean TTS, phone and hardware evidence                       |
| APP  | Hà Duy Lộc          | Dataset, evaluator, application/demo, business content and submission package |

## Sprint Objective

The final objective of this sprint is to complete the official Phase 2 Technical Proposal template and prepare an upload-ready PDF before 21/08/2026.

Code, datasets, model experiments and device measurements are supporting evidence for the proposal. They are not independent sprint goals.

The immediate technical milestone is:

```text
Vietnamese WAV
→ real Vietnamese ASR
→ real VI→KO translation
→ FactorySafe validation
→ real Korean TTS
→ Korean WAV
```

If the full path cannot be completed in time, every implemented stage, planned stage and limitation must be reported truthfully.

---

# ATE — Nguyễn Tiến Đạt

## Role

**ASR & Translation Engineer**

## Primary Proposal Ownership

* Section 4.1 — System Pipeline Overview
* Section 4.2 — ASR and NMT module inputs
* Section 4.3 — Model optimisation inputs
* Section 4.4 — Linguistic robustness
* Technical evidence used in Sections 1 and 6

## Tasks

| ID        | Priority | Task                                                                                    | Required Output                                                                                                 | Due        |
| :-------- | :------- | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------- | :--------- |
| ATE-P0-01 | P0       | Select no more than two Vietnamese/Korean-capable ASR candidates.                       | Candidate table with exact model, repository, revision, runtime, precision, language support, size and license. | 07/08/2026 |
| ATE-P0-02 | P0       | Run real ASR inference on Vietnamese WAV files supplied by AUD.                         | Transcript outputs, commands, raw logs, stage latency and failure examples.                                     | 08/08/2026 |
| ATE-P0-03 | P0       | Implement or integrate the real ASR adapter without removing the existing mock adapter. | `asr_real.py` or equivalent, configuration instructions and smoke test.                                         | 08/08/2026 |
| ATE-P0-04 | P0       | Select no more than two VI→KO NMT candidates.                                           | Candidate table with language codes, model revision, runtime, precision, size, license and phone feasibility.   | 08/08/2026 |
| ATE-P0-05 | P0       | Run real VI→KO translation on the shared evaluation sentences.                          | Predictions, latency logs, protected-token failures and model comparison.                                       | 09/08/2026 |
| ATE-P0-06 | P0       | Implement or integrate the real NMT adapter.                                            | `nmt_real.py` or equivalent, reproducible command and smoke test.                                               | 09/08/2026 |
| ATE-P0-07 | P0       | Recommend the baseline ASR and NMT models.                                              | Short decision document including selection reasons, rejected candidates and known risks.                       | 10/08/2026 |
| ATE-P1-01 | P1       | Measure ASR and NMT quality using the approved or diagnostic set.                       | CER/WER, chrF++ or other valid metrics, with dataset status and limitations.                                    | 12/08/2026 |
| ATE-P1-02 | P1       | Measure cold/warm latency and memory when possible.                                     | Raw timing and memory reports, clearly labelled PC or phone.                                                    | 14/08/2026 |
| ATE-P1-03 | P1       | Document error cases.                                                                   | At least one ASR failure and one NMT failure with analysis and fallback recommendation.                         | 14/08/2026 |

## Required Files

```text
src/say_it_for_me/stages/asr_real.py
src/say_it_for_me/stages/nmt_real.py
docs/submission/evidence/asr/
docs/submission/evidence/nmt/
docs/team/handoffs/ATE_HANDOFF.md
```

## Definition of Done

* At least one ASR model processes real Vietnamese audio.
* At least one NMT model produces Korean text from Vietnamese text.
* Exact model versions and licenses are recorded.
* Commands can be reproduced by TL.
* Results are not described as phone results unless run on the named phone.
* Machine-generated Korean output is not treated as an approved reference.
* At least one failure case is documented.

## Blocker Reporting

ATE must immediately report:

* Unsupported Vietnamese or Korean language.
* Model too large for the expected phone.
* Runtime incompatibility.
* Unclear or unsuitable license.
* Missing audio input.
* Missing Korean references required for evaluation.

---

# AUD — Nguyễn Đăng Gia Đạo

## Role

**Audio & TTS Engineer**

## Primary Proposal Ownership

* Section 4.1 — Audio input and output stages
* Section 4.2 — VAD, audio processing and TTS inputs
* Section 4.4 — Acoustic robustness
* Section 5.1 — Platform comparison inputs
* Section 5.2 — Hardware and power inputs
* Section 6.1 — Audio and device stack

## Tasks

| ID        | Priority | Task                                                                        | Required Output                                                                                                          | Due              |
| :-------- | :------- | :-------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------- | :--------------- |
| AUD-P0-01 | P0       | Profile the exact available phone.                                          | Phone model, About Phone screenshot, SoC, RAM, storage, OS version, battery specification and debug/sideload capability. | 07/08/2026       |
| AUD-P0-02 | P0       | Compare at least two realistic phone or SoC options using official sources. | Platform comparison with AI capability, RAM, toolchain compatibility, form-factor suitability and recommendation.        | 09/08/2026       |
| AUD-P0-03 | P0       | Implement WAV input and output.                                             | WAV reader/writer, mono/sample-rate validation and tests.                                                                | 08/08/2026       |
| AUD-P0-04 | P0       | Coordinate collection of the first real Vietnamese audio set.               | At least 10 WAV clips, manifest, recording conditions, consent and rights status.                                        | 08/08/2026       |
| AUD-P0-05 | P0       | Select a Korean TTS candidate.                                              | Exact voice/checkpoint, runtime, license, artifact size and device feasibility.                                          | 09/08/2026       |
| AUD-P0-06 | P0       | Generate real Korean speech from Korean text.                               | Korean WAV output, command, raw logs, latency and one failure example.                                                   | 10/08/2026       |
| AUD-P0-07 | P0       | Implement or integrate the Korean TTS adapter.                              | `tts_real.py` or equivalent and smoke test.                                                                              | 10/08/2026       |
| AUD-P1-01 | P1       | Collect noisy-condition audio.                                              | Additional clips or variants with noise description and provenance.                                                      | 12/08/2026       |
| AUD-P1-02 | P1       | Test real audio playback and microphone capture if baseline is ready.       | Audio capture/playback result and device notes.                                                                          | 14/08/2026       |
| AUD-P1-03 | P1       | Run phone measurements after models are available.                          | Raw model-load, latency, memory, thermal and failure logs.                                                               | 14/08/2026       |
| AUD-P2-01 | P2       | Evaluate VAD or denoise only after the baseline works.                      | Before/after comparison proving whether the extra stage is worth its latency.                                            | Only after P0/P1 |

## Required Files

```text
src/say_it_for_me/audio/wav_io.py
src/say_it_for_me/stages/tts_real.py
docs/submission/audio/audio_manifest.jsonl
docs/submission/evidence/audio/
docs/submission/evidence/tts/
docs/submission/evidence/device/
docs/team/handoffs/AUD_HANDOFF.md
```

## Definition of Done

* The exact phone profile is available.
* At least 10 real Vietnamese WAV files are available.
* WAV input/output works reproducibly.
* At least one Korean TTS model generates audible Korean WAV.
* Exact voice, runtime and license are recorded.
* All device claims come from the real device or official OEM documentation.
* PC performance is never relabelled as phone performance.

## Blocker Reporting

AUD must immediately report:

* No suitable phone is available.
* Phone debugging or sideloading is blocked.
* Korean TTS license is unclear.
* Korean TTS cannot run locally.
* Audio consent or rights are missing.
* WAV format is incompatible with the ASR adapter.
* Device overheats, crashes or runs out of memory.

---

# APP — Hà Duy Lộc

## Role

**Application, Dataset & Submission Engineer**

## Primary Proposal Ownership

* Section 2 — Problem Definition & Target Users
* Section 3 — Business Solution & Innovation
* Section 7 — Team Profile & Timeline
* Section 8 — Submission Checklist
* Dataset preparation and evaluator operation
* Demo, UI flow and final document package

## Tasks

| ID        | Priority | Task                                                       | Required Output                                                                                                     | Due                                  |
| :-------- | :------- | :--------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------ | :----------------------------------- |
| APP-P0-01 | P0       | Clean and validate the 30-row VI→KO factory dataset draft. | Records with ID, direction, source, reference, domain, safety flag, protected tokens, provenance and review status. | 08/08/2026                           |
| APP-P0-02 | P0       | Confirm a Korean reviewer.                                 | Reviewer relationship/proficiency, consent, review window and status.                                               | 09/08/2026                           |
| APP-P0-03 | P0       | Coordinate Korean review.                                  | Reviewer decision log and reviewed records; unreviewed text must remain `draft`.                                    | First batch 11/08; full target 14/08 |
| APP-P0-04 | P0       | Validate the factory communication problem.                | Interview notes or credible sources, problem statement and qualitative impact table without invented metrics.       | 12/08/2026                           |
| APP-P0-05 | P0       | Research existing alternatives.                            | Sourceable comparison covering cloud apps, human interpreters, static phrasebooks and relevant translation devices. | 12/08/2026                           |
| APP-P0-06 | P0       | Confirm organizer submission requirements.                 | Exact cutoff, timezone, accepted files, page/file-size limit, external-link policy and evidence source.             | 07/08/2026                           |
| APP-P0-07 | P0       | Confirm the four-person roster.                            | Names, roles, expertise, availability and contribution areas.                                                       | 07/08/2026                           |
| APP-P0-08 | P0       | Maintain proposal completion tracking.                     | Updated completion matrix and claim-evidence map.                                                                   | Daily                                |
| APP-P0-09 | P0       | Maintain the working proposal package.                     | Version/date, diagrams, Korean fonts, placeholders, links and checklist.                                            | Daily                                |
| APP-P1-01 | P1       | Define FactorySafe product behavior.                       | Warning copy, protected-token examples, phrasebook candidates and UI states.                                        | 12/08/2026                           |
| APP-P1-02 | P1       | Run the evaluator on available data.                       | Validation result, included/excluded IDs and diagnostic metrics with correct evidence labels.                       | 12/08/2026                           |
| APP-P1-03 | P1       | Prepare application and demo flow.                         | UI flow, demo script, shot list and prototype-link status.                                                          | 16/08/2026                           |
| APP-P0-10 | P0       | Perform final proposal audit and PDF preflight.            | No sample text, unsupported claims, unresolved placeholders or broken diagrams; upload-ready package.               | 20/08/2026                           |

## Required Files

```text
docs/submission/dataset/
docs/submission/PROPOSAL_COMPLETION_MATRIX.md
docs/submission/CLAIM_EVIDENCE_MAP.md
docs/submission/PHASE2_REQUIREMENTS.md
docs/submission/SUBMISSION_CHECKLIST.md
docs/demo/DEMO_SCRIPT.md
docs/demo/DEMO_SHOT_LIST.md
docs/team/handoffs/APP_HANDOFF.md
```

## Definition of Done

* Every dataset record has provenance and review status.
* Unreviewed Korean text remains `draft`.
* Problem and competitor claims have sources or are labelled hypotheses.
* Submission rules come from organizer material.
* Team information is verified.
* Completion matrix and claim map are current.
* Final proposal has no template examples, generic placeholders or unsupported achievement claims.
* PDF export passes the preflight checklist.

## Blocker Reporting

APP must immediately report:

* No Korean reviewer is available.
* Organizer requirements are unclear.
* Team information is incomplete.
* Problem claims lack evidence.
* Competitor claims lack reliable sources.
* A proposal claim is unsupported.
* Korean fonts, diagrams or links fail during export.

---

# TL — Nguyễn Đổng Thiên Kỳ

## Role

The TL owns final technical decisions, integration, scope control and submission approval.

AI tools may assist with coding, research and drafting, but they are not accountable owners.

## Primary Proposal Ownership

* Section 1 — Executive Summary
* Section 4 — Final technical design
* Section 5 — Final platform decision
* Section 6 — System integration
* Final consistency across Sections 1–8

## Tasks

| ID       | Priority | Task                                                          | Required Output                                                                    | Due                 |
| :------- | :------- | :------------------------------------------------------------ | :--------------------------------------------------------------------------------- | :------------------ |
| TL-P0-01 | P0       | Confirm role ownership and availability.                      | Updated `TEAM_FACTS.md` containing TL, ATE, AUD and APP details.                   | 07/08/2026          |
| TL-P0-02 | P0       | Review and approve ASR/NMT candidates proposed by ATE.        | Recorded baseline decision and fallback.                                           | 10/08/2026          |
| TL-P0-03 | P0       | Review and approve audio/TTS/device recommendations from AUD. | Recorded baseline decision and fallback.                                           | 10/08/2026          |
| TL-P0-04 | P0       | Integrate the real VI→KO path.                                | Reproducible command, exact models, raw stage timings and documented failure.      | 12/08/2026          |
| TL-P0-05 | P0       | Integrate FactorySafe validation if feasible.                 | Runtime guard, unit tests and safe failure behavior.                               | 14/08/2026          |
| TL-P0-06 | P0       | Maintain claim/evidence consistency.                          | Updated claim map, evidence links and PC/phone separation.                         | Daily through 18/08 |
| TL-P0-07 | P0       | Approve platform selection.                                   | Final smartphone/platform decision or a clearly labelled proposed selection.       | 14/08/2026          |
| TL-P0-08 | P0       | Maintain state-labelled architecture diagrams.                | Updated software pipeline and phone deployment diagrams.                           | 16/08/2026          |
| TL-P0-09 | P0       | Apply scope cuts.                                             | Written decision on bidirectional support, TTS, mobile integration and demo scope. | 14/08/2026          |
| TL-P0-10 | P0       | Approve the final submission.                                 | Final PDF, checklist, upload package and receipt.                                  | 20–21/08/2026       |

## Definition of Done

* The proposal follows the official template.
* Each section has a verified owner.
* Technical design is internally consistent.
* Every claim is classified as measured, target, proposed, hypothesis or limitation.
* PC and phone evidence are clearly separated.
* Scope cuts are decided early enough to protect the submission.
* Final PDF is reviewed before upload.
* Submission confirmation is retained.

---

# Shared Handoff Format

Each member must update their handoff file at the end of every work session.

```text
DATE/TIME

COMPLETED
- ...

COMMANDS OR ACTIONS
- ...

RESULTS
- ...

FILES CHANGED
- ...

EVIDENCE LOCATION
- ...

BLOCKERS
- ...

DECISIONS NEEDED FROM TL
- ...

NEXT THREE ACTIONS
1. ...
2. ...
3. ...
```

A verbal message such as “done” is not sufficient without files, commands, outputs or evidence.

---

# Next Milestone — M1 Real VI→KO Evidence Slice

**Internal deadline:** 10/08/2026

## Definition of Done

* At least five real Vietnamese WAV inputs exist.
* WAV input works.
* A real ASR model produces Vietnamese transcripts.
* A real NMT model produces Korean text.
* A real Korean TTS model produces Korean audio, or a documented blocker and fallback exist.
* Exact model versions, runtimes and licenses are recorded.
* Stage timings are captured.
* At least one failure case is documented.
* The exact phone profile is available.
* Submission requirements are confirmed.
* Proposal Section 4 is updated using the new evidence.

If Korean TTS is blocked, the accepted reduced milestone is:

```text
Vietnamese WAV
→ real Vietnamese transcript
→ real Korean translation text
```

The missing TTS stage must be presented as a limitation, not as an implemented capability.

---

# Final Internal Deadlines

| Date  | Required State                                               |
| :---- | :----------------------------------------------------------- |
| 07/08 | Roster, submission rules and phone profile confirmed         |
| 08/08 | WAV I/O, first audio clips and real ASR available            |
| 09/08 | Real VI→KO translation available                             |
| 10/08 | Korean TTS or documented blocker; baseline model decisions   |
| 12/08 | Real evidence slice, initial evaluation and updated proposal |
| 14/08 | Evidence freeze, platform decision and scope cuts            |
| 16/08 | Diagrams, demo plan and proposal integration complete        |
| 18/08 | Content freeze and contradiction audit                       |
| 20/08 | Upload-ready PDF and package                                 |
| 21/08 | Submission and receipt retention                             |
