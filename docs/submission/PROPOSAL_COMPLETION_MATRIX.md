# Proposal Completion Matrix — Say It For Me

Last updated: 21/08/2026. This matrix tracks the working submission at `docs/submission/1V_P2_TechProposal_SayItForMe.md`. Statuses distinguish drafted, confirmed, proposed, measured, implemented, and blocked material; a drafted section is not automatically submission-ready.

| Template Section | Rubric Weight | Required Content | Current Status | Evidence Available | Missing Input | Owner | Due Date |
| :--- | ---: | :--- | :--- | :--- | :--- | :--- | :--- |
| Cover metadata | — | Team/project name, date, version, confidentiality | BLOCKED — project name known; specialist roster known; TL personal name and final date absent | Context log confirms project and deadline | TL personal name; actual submission date | APP | 18/08/2026 |
| 1 Executive Summary | — | 200–300 word problem, solution, users, differentiator summary | DRAFTED — evidence-labelled | Context log; repo audit | Final team name; reader review | TL | 18/08/2026 |
| 1.1 Problem Overview | 15% | Gap, affected users, setting, current limitations | DRAFTED — initial hypothesis | Context log selected use case | Factory interviews or credible sources | APP | 14/08/2026 |
| 1.2 Proposed Solution | 15% | Name, technology, deployment, distinction | DRAFTED — proposed | Context log phone / VI–KO decisions | Team confirmation of innovation wording | AI/Technical Lead | 12/08/2026 |
| 1.3 Key Value Proposition | 15% | Specific differentiators | DRAFTED — safe wording | Explicit-direction contracts; evaluator; model-store code | FactorySafe implementation/evidence; offline test | AI/Technical Lead | 14/08/2026 |
| 2.1 Problem Statement | 15% | User, environment, criticality, current failures | DRAFTED — hypothesis | Context log | Interview/source validation | APP | 14/08/2026 |
| 2.2 Impact Analysis | 15% | Safety, productivity, connectivity impacts | DRAFTED — qualitative hypothesis | Context log use cases | Validated site impact; no fabricated numbers | APP | 14/08/2026 |
| 2.3 Target Users & Use Cases | 15% | Segments, language needs, context, priority | DRAFTED — proposed | Context log | User confirmation and priority validation | APP | 14/08/2026 |
| 2.4 Key Design Constraints | 15% | Offline, latency, environment, languages, constraints | DRAFTED — mixed status | Confirmed phone / language / direction decisions; ADRs | Exact phone profile; network test | TL + AUD | 12/08/2026 |
| 3.1 Industry Problem & Solution Fit | 15% | Current alternatives and specific gaps | DRAFTED — validation needed | Context log | Cited competitor evidence; interviews | APP | 14/08/2026 |
| 3.2 Innovation & Competitive Strengths | 15% | Comparison and innovation thesis | DRAFTED — FactorySafe proposed | Evaluation protected-token metric; context proposal | FactorySafe tests; Korean/domain review | APP + TL | 14/08/2026 |
| 4.1 System Pipeline Overview | 35% | End-to-end stages plus pipeline diagram | DRAFTED — real ASR/NMT adapters and strict demo CLI implemented; no successful real-audio run | PR #3 merge; `demo_cli.py`; `evidence/demo/run.json`; SVG diagram | Consented Vietnamese WAV; successful ASR→NMT artifact; TTS/offline/phone evidence | TL | 21/08/2026 |
| 4.2 Module-by-Module Design | 35% | Models, size, runtime, precision, latency target, technique | DRAFTED — candidate inventories and adapters implemented; baseline is provisional | ATE comparison reports; `asr_real.py`; `nmt_real.py` | Model artifacts; measured output, latency/memory, reviewed quality; license confirmation for NLLB | ATE + AUD; TL approves | 21/08/2026 |
| 4.3 Optimisation & Memory | 35% | Quantisation, memory plan, RAM ceiling | DRAFTED — architecture and targets | `model_store.py`; ADR-002 | Phone RAM; runtime compatibility; RSS/thermal data | ATE + AUD; TL approves | 14/08/2026 |
| 4.4 Robustness & Edge Cases | 35% | Acoustic, linguistic, edge-case handling | DRAFTED — mixed; input-format and same-language failures implemented | Segmenter; explicit-direction tests; adapter boundary tests; `evidence/demo/run.json` | Noisy audio, real ASR/NMT results, Korean review, protected-token runtime guard | ATE + AUD + APP | 21/08/2026 |
| 5.1 Platform Selection & Justification | 25% | Two options, AI capability, power/RAM/storage/toolchain/form factor, recommendation | DRAFTED — selection blocked | Official Qualcomm platform pages; context phone decision | Exact phone and OEM specifications; physical device profile | AUD; TL approves | 12/08/2026 |
| 5.2 Hardware Components & Power Budget | 25% | Smartphone BOM and power reasoning | DRAFTED — no fabricated figures | Context says phone is primary form factor | Battery, power, thermals, audio path, model sizes | AUD | 14/08/2026 |
| 6.1 Software Stack | — | OS, runtime, audio, model serving, app layer | DRAFTED — PC-only real ASR/NMT runtime now implemented; phone stack remains proposed | PR #3; `requirements-inference.txt`; demo CLI | Exact OS/device, mobile-compatible runtime, network-disabled run | TL + AUD | 21/08/2026 |
| 6.2 Architecture Diagram | — | Software/hardware integration diagram | COMPLETE FOR WORKING DRAFT — state-labelled SVG | `phone_deployment_architecture.svg` | Final phone details for revision | TL | 18/08/2026 |
| 6.3 Offline-First Principles | — | Local storage, no runtime cloud, safe fallback | DRAFTED — design only | Manifest/checksum foundation; context rules | Network-disabled real-model run and privacy decision | TL | 14/08/2026 |
| 7.1 Team Members | 10% | Four names, roles, expertise, contributions | DRAFTED — three specialist names/roles confirmed; TL personal name/details blocked | Current roster source | TL personal name, availability, detailed expertise | TL | 12/08/2026 |
| 7.2 Project Timeline | 10% | Milestones, activities, target dates, early demo status | DRAFTED — recovery dates | Context log deadline and scope-cut plan | Availability, exact portal cutoff, demo status | APP | 12/08/2026 |
| 8 Submission Checklist | — | All submission requirements and export status | DRAFTED — gated checklist | Template and working proposal audit | Format/page/size/link policy; actual export/upload | APP; TL approves | 18/08/2026 |

## Completion snapshot

| Area | Working-draft completion | Submission-ready state |
| :--- | :--- | :--- |
| 1 Executive Summary | 100% drafted | Needs final metadata and reader review |
| 2 Problem & Target Users | 100% drafted | Blocked on validation evidence |
| 3 Business & Innovation | 100% drafted | Blocked on competitor/user validation and FactorySafe proof |
| 4 AI Design | 100% drafted | Adapter code and candidate metadata implemented; blocked on successful real-audio/model, quality, latency, TTS, offline, and phone evidence |
| 5 Hardware | 100% drafted | Blocked on exact handset and measurement |
| 6 Architecture | 100% drafted | Needs selected phone / runtime revision |
| 7 Team & Timeline | 50% drafted | Blocked on four verified team profiles and availability |
| 8 Submission | 50% drafted | Blocked on organizer rules, PDF export, and upload |

Overall working-draft completion: **approximately 85%**. Overall submission-ready completion: **approximately 35%**, because verified team, phone, model, validation, and organizer inputs remain outstanding.

Reader test on 06/08/2026: passed after scope, status-vocabulary, FactorySafe-ordering, and latency-budget clarifications. The remaining blockers are only the explicitly labelled human inputs and final submission actions above.
