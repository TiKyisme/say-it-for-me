# PHASE 2 CALENDAR — 27/07 to 21/08/2026

> **Version:** 0.2; last updated 27/07/2026  
> **Internal rule:** weekends 01–02, 08–09 and 15–16/08 are optional buffer until
> member availability is confirmed. Required milestones are placed on weekdays.
> The active card owns each task's exact start, deadline, acceptance and handoff.
> This calendar owns cross-team dependency milestones. A role prompt does not
> extend either date.

> **06/08/2026 recovery override:** named roles are now confirmed. Dates before
> 06/08 are historical; the current task deadlines, ownership, acceptance
> criteria, and evidence locations are in `PHASE2_RESCUE_TASKS_3_MEMBERS.md`.
> The current M1 target is 10/08/2026 and the Phase 2 deadline remains
> 21/08/2026.

| Date | DRI(s) | Required output by end of day |
|---|---|---|
| **27/07 Mon** | TL / APP / ATE / AUD, each on own card | Playbook/prompts/cards; deadline recorded; evaluation foundation started; candidate/audio plans assigned |
| **28/07 Tue** | TL | By 17:30: roster/capacity, baseline PC/device, reviewer and consent checkpoint |
|  | APP | Evaluation implementation/contract draft; Korean-review booking support |
|  | ATE | Acknowledge role/card; collect candidate source links without selecting a winner |
|  | AUD | By 17:30: audio fixture/noise protocol and denoiser/VAD/TTS inventory draft |
| **29/07 Wed** | TL | By 09:00 organizer questions sent; by 12:00 Gate 0 card reviewed |
|  | APP | By 15:00 evaluation foundation and handoff sent to ATE |
|  | ATE | Start independent evaluation review at 15:00 |
|  | AUD | By 17:30 WAV/sample-rate/noise contract tests |
| **30/07 Thu** | ATE | Evaluation-foundation review sent by 11:00 |
|  | TL | Evaluation-foundation decision recorded by 12:00 |
|  | APP | After foundation PASS, open the 20-pair set card; by 17:30 create traceable structure/status fields, not an approved result |
|  | AUD | By 12:00 synthetic clean/noisy manifest and command handed to ATE |
| **31/07 Fri** | TL | **M1 review:** G0 and evaluation foundation pass, or named blockers; dataset/ASR status explicit |
|  | ATE | ASR candidate inventory and runner smoke complete; full Tiny/Base evidence remains due 04/08 |
|  | APP; Korean reviewer reviews | First manufacturing/safety review batch; approval status remains item-level |
|  | AUD; ATE reviews | Audio fixture technical review complete by 12:00 |
| **03/08 Mon** | TL | NLLB/fallback license pre-check and device-access decision |
|  | ATE | Complete ASR runs; prepare NMT artifacts only if the ASR report remains on time |
|  | AUD | DeepFilterNet/resample adapter ready |
|  | APP | Traceable 20-pair set status, direction-first UI shell and business evidence list |
| **04/08 Tue** | ATE | ASR report/ADR recommendation by 12:00; NMT identical-config runs begin |
|  | AUD | Denoiser on/off ASR evidence; exact VI/KO TTS candidates |
|  | APP | 20-pair review/evidence status, protected-token report and UI states |
| **05/08 Wed** | ATE | NMT candidate raw results on identical general/manufacturing records |
|  | AUD | Complete denoiser evidence and prepare VI/KO TTS runs |
|  | APP | Competitor/interview evidence and remaining UI states |
| **06/08 Thu** | ATE | NMT decision matrix and ADR recommendation |
|  | AUD | TTS RTF/first-audio result and Korean review package |
| **07/08 Fri** | TL | **M2 review:** ASR/NMT stack frozen; Audio/TTS passes or named fallback |
| **10/08 Mon** | TL; specialists supply owned adapters | Real adapters have standalone tests; VI→KO integration begins |
| **11/08 Tue** | TL | Complete VI→KO candidate: WAV VI → transcript → KO text → KO WAV |
|  | APP | Transcript/translation/warning/busy UI states |
| **12/08 Wed** | TL | **G6 pass:** one-direction offline slice, trace/RSS/load-time and 30 runs |
| **13/08 Thu** | TL; specialists supply owned adapters | KO→VI integration candidate; direction-specific voice lifecycle |
| **14/08 Fri** | TL; APP packages | **M3/evidence freeze 18:00:** bidirectional rehearsal or scope-cut; owner evidence bundles |
| **17/08 Mon** | TL; each owner supplies signed input | Complete owner proposal input, Korean examples/TTS review, proposal full draft |
| **18/08 Tue** | TL | **Content freeze 18:00:** reader test, contradiction/claim/template fixes |
| **19/08 Wed** | APP; TL approves | RC1 PDF/DOCX; diagrams, tables, links and Korean text rendered correctly |
| **20/08 Thu** | APP; TL approves | **File freeze 12:00; upload-ready 18:00 ICT** |
| **21/08 Fri** | TL | Portal/file contingency only; submit and save confirmation |

## Pre-approved scope cuts

- No Korean TTS passing its gate by 07/08: keep Korean text output and disclose the
  TTS limitation; do not use an unlicensed/unreviewed voice.
- G6 not passing by 12/08: drop microphone and UI polish; preserve a reproducible
  one-direction WAV pipeline.
- No Snapdragon device: report PC evidence and a migration/profiling plan only.
- Prototype work stops adding features after the 14/08 evidence freeze.
- No Korean reviewer: remove human-quality claims and safety-critical Korean examples;
  keep reference-based metrics clearly limited.

TL records any activated scope cut in an ADR and in the proposal limitation section.
