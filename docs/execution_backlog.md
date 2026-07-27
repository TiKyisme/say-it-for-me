# Execution Backlog — Small, Verifiable Steps

The organizer deadline is the end of **21/08/2026**. The internal upload-ready
deadline is **20/08/2026 18:00 (Asia/Ho_Chi_Minh)**; 21/08 is contingency.

**Ownership notation:** the first named role is the single DRI. Text after a
semicolon names contributors or reviewers, not co-owners. A row that says
“each owner” represents one independent task per evidence owner.

## Gate 0 — Submission facts and ownership

- [x] **G0.1 (5 min, TL):** Record the official Phase 2 deadline: end of 21/08/2026.
- [ ] **G0.1b (15 min, TL):** Confirm exact cutoff time, upload format, page/file limits, and whether external links are allowed.
- [ ] **G0.2 (20 min, TL):** Fill team name, member names, expertise, and contact details.
- [ ] **G0.3 (15 min, TL; each member supplies their facts):** Record each member’s available hours until submission.
- [ ] **G0.4 (15 min, TL):** Confirm which Snapdragon/Android/RB3 device is physically available.
- [ ] **G0.5 (30 min, APP):** Recruit a Korean-speaking reviewer and book two review windows.
- [ ] **G0.6 (15 min, TL):** Name the baseline PC: CPU, RAM, OS, Python version.

**PASS:** no `TBC` remains for submission logistics, owners, device access, or Korean review.

## Gate 1 — Repository foundation

- [x] **G1.1:** Create typed direction/audio/text contracts.
- [x] **G1.2:** Enforce 48 kHz capture/denoiser and 16 kHz ASR boundary.
- [x] **G1.3:** Add VAD-oriented segmenter with pre-roll, end silence, and hard max duration.
- [x] **G1.4:** Add ordered mock pipeline with stage timings.
- [x] **G1.5:** Add model manifest, local path confinement, SHA-256 verification, and lazy loader.
- [x] **G1.6:** Add tests for direction, sample rates, segmentation, checksums, and lazy loading.
- [x] **G1.7:** Run mock CLI and tests on Windows with Vietnamese/Korean UTF-8 output.
- [x] **G1.8a (10 min, TL):** Initialize Git repository on branch `main`.
- [ ] **G1.8b (20 min, TL):** Agree branch/review rules with all members.
- [ ] **G1.9 (30 min, TL):** CI workflow is present; verify its first remote run after the repository is pushed.

**PASS:** `python -m unittest discover -s tests -v` passes and a mock request emits a trace.

## Gate 2 — Dataset and evaluation contract

- [x] **G2.1 (45 min, APP):** Define and test the strict reference/prediction JSONL schema, including ID, direction, source, reference, domain, safety flag, protected tokens, provenance, license and review status.
- [x] **G2.1b (30 min, APP):** Enforce `approved`-only official selection, expose included/excluded IDs, and keep non-approved rows behind a diagnostic-only flag.
- [x] **G2.1c (30 min, APP):** Prevent public-API policy bypass and reject unsafe Unicode with stable structured errors.
- [ ] **G2.2 (60 min, APP):** Build a 20-pair smoke set from traceable sources.
- [ ] **G2.3 (90 min, APP; Korean reviewer reviews):** Draft the first 30 manufacturing/safety pairs; do not machine-generate final Korean references without review.
- [x] **G2.4a (45 min, APP; ATE reviews):** Implement the standardized `sacrebleu` BLEU and chrF++ adapter with version/signature output and an explicit unavailable state.
- [ ] **G2.4b (30 min, ATE):** Run the real optional dependency, inspect the signatures, and approve or reject the standardized metric boundary.
- [x] **G2.5a (45 min, APP; ATE reviews):** Implement corpus CER/whitespace-WER overall and separately by target language.
- [ ] **G2.5b (30 min, ATE):** Review the Vietnamese/Korean normalization and whitespace-WER limitations and record the decision.
- [x] **G2.6 (30 min, APP):** Add exact occurrence-based protected-token metrics for numbers, units, equipment IDs, and error codes.
- [ ] **G2.7 (30 min, TL):** Review dataset licenses and exclude incompatible data.

**PASS:** one command evaluates a prediction file and emits reproducible metrics plus dataset provenance.

**Current evidence (27/07/2026):** evaluator implementation, 25 evaluation
tests and all 32 repository tests pass. The example under `examples/evaluation/` is deliberately
`NON_EVIDENCE`; Gate 2 remains open until the 20-pair traceable set, ATE review,
real `sacrebleu` run and license approval exist.

## Gate 3 — ASR spike

- [ ] **G3.1 (30 min, ATE):** Record exact Whisper Tiny/Base checkpoints and runtimes.
- [ ] **G3.2 (60 min, ATE):** Prepare equal clean vi/ko audio sets.
- [ ] **G3.3 (60 min, AUD):** Create deterministic 15/10/5/0 dB noise mixes.
- [ ] **G3.4 (90 min, ATE):** Run Tiny clean/noisy benchmark.
- [ ] **G3.5 (90 min, ATE):** Run Base clean/noisy benchmark.
- [ ] **G3.6 (30 min, ATE):** Report CER/WER, p50/p95, peak RSS, artifact size, and failure examples.
- [ ] **G3.7 (30 min, TL; ATE reviews):** Write ADR selecting Tiny, Base, or a new candidate.

**PASS:** the selected ASR wins against explicit thresholds; no selection is based only on model size.

## Gate 4 — Translation spike

- [ ] **G4.1 (30 min, TL):** Complete the license gate for NLLB and fallbacks.
- [ ] **G4.2 (60 min, ATE):** Convert NLLB candidate with exact CTranslate2 version and compute type.
- [ ] **G4.3 (60 min, ATE):** Prepare M2M100/bilingual candidate in the same runtime when possible.
- [ ] **G4.4 (90 min each, ATE):** Run candidates on the same general/manufacturing sets.
- [ ] **G4.5 (45 min, ATE):** Record chrF++, sacreBLEU, terminology accuracy, p50/p95, RSS, and size.
- [ ] **G4.6 (30 min, TL; ATE reviews):** Score the decision matrix and write ADR.

**PASS:** one candidate meets the license gate and has a reproducible quality/resource trade-off.

## Gate 5 — Audio and TTS spike

- [ ] **G5.1 (45 min, AUD):** Validate DeepFilterNet 48 kHz standalone adapter.
- [ ] **G5.2 (45 min, AUD):** Add resampling adapter and verify durations/sample rates.
- [ ] **G5.3 (90 min, AUD; ATE supplies/reviews ASR scoring):** Measure denoiser on/off impact on ASR by SNR.
- [ ] **G5.4 (45 min, AUD):** Select exact Vietnamese TTS checkpoint and record voice-model license.
- [ ] **G5.5 (60 min, AUD):** Select exact Korean TTS checkpoint and record license/runtime compatibility.
- [ ] **G5.6 (90 min, AUD):** Benchmark RTF and first-audio latency for both voices.
- [ ] **G5.7 (30 min, APP; Korean reviewer reviews):** Coordinate and record Korean intelligibility review on 20 sentences.

**PASS:** both languages synthesize offline and the exact model/license is documented.

## Gate 6 — Real one-direction vertical slice

- [ ] **G6.1 (45 min, TL):** Replace mock ASR behind the existing port.
- [ ] **G6.2 (45 min, TL):** Replace mock NMT behind the existing port.
- [ ] **G6.3 (45 min, TL):** Replace mock target TTS behind the existing port.
- [ ] **G6.4 (30 min, AUD):** Add WAV file input/output before microphone work.
- [ ] **G6.5 (60 min, TL; ATE, AUD and APP review):** Run `VI → KO` file pipeline and route contract failures to the owning module.
- [ ] **G6.6 (30 min, TL):** Capture trace, RSS, model-load times, and artifacts.
- [ ] **G6.7 (30 min, TL; specialists review failures):** Run 30 consecutive smoke utterances.

**PASS:** WAV input → Vietnamese transcript → Korean translation → Korean WAV output, with no network and a complete trace.

## Gate 7 — Bidirectional demo and UI

- [ ] **G7.1 (45 min, APP):** Build direction-first UI; no auto-detect toggle.
- [ ] **G7.2 (45 min, AUD):** Add push-to-talk microphone capture.
- [ ] **G7.3 (45 min, TL):** Add direction-specific TTS loading/unloading policy.
- [ ] **G7.4 (60 min, TL; specialists own their adapters):** Integrate `KO → VI`.
- [ ] **G7.5 (30 min, APP):** Add visible transcript, translation, state, warnings, replay.
- [ ] **G7.6 (45 min, APP):** Add metrics panel labelled PC evidence.
- [ ] **G7.7 (60 min, APP; TL approves):** Rehearse a factory scenario and record failure cases.

**PASS:** both directions work from the UI and the user can always see the selected direction.

## Gate 8 — Proposal review

- [ ] **G8.1 (60 min, TL):** Replace proposal `TBC`s with confirmed facts.
- [ ] **G8.2 (45 min per evidence owner):** Each owner fills their own evidence table using report artifacts.
- [ ] **G8.3 (45 min, TL):** Verify every number is labelled measured, estimated, or target.
- [ ] **G8.4 (45 min, TL; each owner signs their section):** Review against the 35/25/15/15/10 rubric.
- [ ] **G8.5 (30 min, TL):** Validate all links, model licenses, and hardware citations.
- [ ] **G8.6 (30 min, Korean reviewer):** Check Korean examples and demo phrases.
- [ ] **G8.7 (30 min, APP; TL approves):** Export PDF/DOCX and run the submission checklist.

**PASS:** the proposal is complete, evidence-backed, and contains no unsupported Snapdragon result.
