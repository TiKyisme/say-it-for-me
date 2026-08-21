# Claim–Evidence Map — Say It For Me

Last updated: 21/08/2026. This is the wording gate for the working proposal. A claim may be promoted to `MEASURED` only when it has a reproducible artifact, raw output, environment details, and a scope-consistent interpretation.

| Claim | Proposal Section | Type | Evidence | Status | Allowed Wording |
| :--- | :--- | :--- | :--- | :--- |
| The target product form factor is a phone. | 1, 5 | User-provided fact | Context log, section 2 | CONFIRMED | “The target form factor is a smartphone.” |
| Vietnamese–Korean is the priority language pair. | 1, 2, 4 | User-provided fact | Context log, section 2 | CONFIRMED | “The priority pair is Vietnamese ↔ Korean.” |
| The repository has explicit `vi-ko` and `ko-vi` request contracts. | 1, 4 | Measured result | `contracts.py`, `pipeline.py`, 32-test run | CONFIRMED | “The reference repository implements explicit direction contracts.” |
| The Python slice enforces a 48 kHz input / 16 kHz ASR boundary. | 4 | Measured result | `pipeline.py`, pipeline tests | CONFIRMED | “The reference slice validates this audio contract.” |
| The segmenter uses 20 ms frames, 200 ms pre-roll, 400 ms end silence, and 8 s maximum. | 4 | Measured result | `audio/segmenter.py`, segmenter tests | CONFIRMED | “The segmenter configuration is …”; do not call it a VAD model. |
| The reference pipeline rejects language output that conflicts with selected direction. | 4 | Measured result | `pipeline.py`; explicit-direction pipeline tests | CONFIRMED | “The reference pipeline rejects a direction mismatch.” |
| The segmenter performs production VAD. | 4 | Hypothesis | No detector code or model | NOT SUPPORTED | “A VAD detector is planned; the current segmenter accepts external speech labels.” |
| The repository has a model-manifest/checksum/lazy-load foundation. | 1, 4, 6 | Measured result | `model_store.py`, model-store tests | CONFIRMED | “The reference foundation provides manifest, checksum, path, and lazy-load controls.” |
| The repository has an approved-only evaluation gate. | 1, 4 | Measured result | evaluation contract and tests | CONFIRMED | “The evaluator excludes non-approved records by default.” |
| 32 repository tests passed. | 1, 4 | Measured result | 06/08/2026 command output; 32 tests, 0.357 s | MEASURED | “32 contract/evaluator tests passed on the recorded environment.” |
| 39 repository tests passed with 3 optional inference-smoke skips. | 1, 4, 6 | Measured result | 21/08/2026 `PYTHONPATH=src python -m unittest discover -s tests -v` output | MEASURED | “39 unit tests passed; three real-inference smoke tests were intentionally skipped because they require optional local dependencies/models.” |
| The 32 passing tests prove a working AI translator. | 1, 4 | Hypothesis | Mock-only pipeline audit | NOT SUPPORTED | “The tests do not demonstrate ASR, NMT, TTS, quality, latency, offline operation, or phone deployment.” |
| Real ASR and NMT adapter implementations exist. | 1, 4, 6 | Code implementation | PR #3 merge `d6a2944`; `asr_real.py`, `nmt_real.py`, adapter tests | IMPLEMENTED | “The repository implements real ASR and NMT adapters; no successful real-audio inference has yet been recorded.” |
| A real VI→KO WAV→transcript→Korean-text run succeeded. | 1, 4, 6 | Measured result | `evidence/demo/run.json` records missing input before model load | BLOCKED | “A reproducible CLI exists, but a consented Vietnamese WAV is required before this run can be measured.” |
| Real WAV input is validated by the demo CLI. | 4 | Code implementation | `demo_cli.py`; `test_demo_cli.py`; `evidence/demo/run.json` | IMPLEMENTED | “The demo CLI accepts only mono 16 kHz PCM-16 WAV and fails explicitly when the input is missing or incompatible.” |
| Korean TTS output works. | 1, 4 | Measured result | No TTS adapter or Korean WAV | NOT IMPLEMENTED | “Korean TTS is not implemented in this repository snapshot.” |
| Fully offline runtime has been achieved. | 1, 2, 6 | Target | No network-disabled run | NOT MEASURED | “The architecture targets offline runtime after provisioning; verification is pending.” |
| Post-utterance first audio is below 3 seconds. | 1, 2, 4 | Target | Evidence register E-002 | NOT MEASURED | “The design target is under 3 seconds.” |
| Memory fits the phone. | 4, 5 | Target | No phone or RSS evidence | NOT MEASURED | “Memory will be measured on the selected phone; current controls are design measures.” |
| FactorySafe Translation Guard preserves critical tokens. | 1, 3, 4 | Proposed feature | Existing evaluator metric only; no runtime guard | NOT IMPLEMENTED | “The proposed guard is designed to preserve and validate protected tokens.” |
| FactorySafe blocks unsafe TTS. | 1, 3, 4 | Proposed feature | No runtime guard or test | NOT IMPLEMENTED | “The design proposes a block/warn/repeat policy before playback.” |
| Cloud tools have a specific latency or privacy behavior. | 3 | Hypothesis | No comparison research in repository | NOT VALIDATED | “Competitor behavior varies; Member 1 will validate product-specific claims.” |
| A bilingual colleague is always unavailable or causes a fixed delay. | 3 | Hypothesis | No interview evidence | NOT VALIDATED | “Human support can be valuable but may not scale to every routine interaction; validate with users.” |
| The factory problem causes a numerical accident, downtime, or cost impact. | 2 | Hypothesis | No user research | NOT VALIDATED | “Potential impact; do not quantify without evidence.” |
| Snapdragon 8 Gen 3 and 7+ Gen 3 are viable candidate phone classes. | 5 | Design decision | Qualcomm platform pages cited in proposal | PROPOSED | “They are candidate SoC classes for evaluation, not selected devices.” |
| The selected phone is Snapdragon 8 Gen 3. | 5, 6 | User-provided fact | Exact phone profile absent | BLOCKED | “No phone has been selected.” |
| A specific phone battery, RAM, storage, TOPS, TDP, or thermal result applies to the project. | 5 | Measured result | Exact device absent | BLOCKED | “No project handset result is claimed; selection and measurement are Phase 3 work.” |
| QAIRT is the current name for QNN. | 5, 6 | External-source fact | Qualcomm AI Hub release notes | CONFIRMED | “Qualcomm documents QNN as the Qualcomm AI Runtime SDK (QAIRT).” |
| Android is the deployment OS. | 5, 6 | Proposed feature | Phone form factor confirmed; OS not confirmed | NOT FINAL | “Android is the proposed deployment path.” |
| The pipeline is stable. | 4 | Target | No 30-run real-model test | NOT MEASURED | “Stability requires 30 consecutive real-model requests.” |
| Korean output is intelligible or reviewed. | 3, 4 | Measured result | No Korean reviewer; no real TTS | BLOCKED | “Korean human review is required before quality/intelligibility claims.” |
| A 30-sentence factory dataset is suitable as quality evidence. | 4 | Hypothesis | Draft data only; no reviewer | NOT EVIDENCE | “Draft records may test schema/guard logic only until Korean review and rights approval.” |
| Exact submission cutoff, format, page limit, file size, and external-link policy are known. | 7, 8 | User-provided fact | Organizer rules were not supplied | LIMITATION | “This proposal is prepared for the Phase 2 date; the authorised uploader must follow portal rules shown at upload.” |
| Four team names, roles and contributions are known. | 7 | User-provided fact | TL Nguyễn Đổng Thiên Kỳ; ATE Nguyễn Tiến Đạt; AUD Nguyễn Đăng Gia Đạo; APP Hà Duy Lộc; `TEAM_FACTS.md` | CONFIRMED | “The four verified members and their role ownership are listed in Section 7.” |
