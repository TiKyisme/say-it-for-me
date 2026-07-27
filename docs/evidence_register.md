# Evidence Register

No target becomes a proposal claim until its evidence cell links to a reproducible artifact.

| ID | Claim / decision | Current status | Required evidence | Owner | Artifact |
|---|---|---|---|---|---|
| E-001 | Runtime makes zero network calls after provisioning | Architecture-enforced, not tested | Offline run with network disabled; dependency audit | TL | `reports/offline/` |
| E-002 | Post-utterance first audio p50 `< 3 s` | Unverified target | 5 warm-ups + 30 measured runs; stage p50/p95; named hardware | TL; specialists supply stage evidence | `reports/e2e/` |
| E-003 | Peak RSS fits the selected device | Unverified | RSS before/after every model load and at peak inference | TL; ATE supplies model RSS | `reports/memory/` |
| E-004 | Whisper Tiny or Base supports vi/ko adequately | Unverified | Clean/noisy CER/WER by language, latency, RSS | ATE | `reports/asr/` |
| E-005 | Selected NMT candidate is best for VI↔KO | Unverified | chrF++, sacreBLEU, terminology accuracy, latency, RSS, size | ATE | `reports/nmt/` |
| E-006 | NMT license permits the intended competition use | Open gate | License text plus organizer/legal confirmation if needed | TL | `reports/licenses/` |
| E-007 | Denoising improves noisy ASR | Unverified | Same clips at 15/10/5/0 dB with denoiser on/off | AUD; ATE supplies ASR scoring | `reports/audio/` |
| E-008 | Vietnamese TTS is intelligible and fast | Unverified | Exact model card, RTF, first-audio latency, reviewer score | AUD | `reports/tts/vi/` |
| E-009 | Korean TTS is intelligible and fast | Blocked on exact candidate/reviewer | Exact model card, RTF, first-audio latency, Korean review | AUD | `reports/tts/ko/` |
| E-010 | QCS6490 is the selected target platform | Provisional | Device access, full pipeline profile, thermal and power data | TL | `reports/hardware/` |
| E-011 | Manufacturing glossary preserves critical terms | Unverified | Validated term set and exact-match/semantic accuracy report | APP; ATE reviews metric logic | `reports/evaluation/` |
| E-012 | Pipeline remains stable | Mock only | 30 consecutive real-model requests with zero crashes | TL; specialists review owned failures | `reports/stability/` |

## Evidence bundle rules

Every report directory must contain:

- `README.md`: purpose, hardware, OS, model revisions, commands;
- machine-readable raw results (`.json` or `.csv`);
- a short interpreted summary;
- errors and excluded runs;
- dependency lock or package versions;
- dataset provenance and license references;
- a clear statement when results are PC-only rather than Snapdragon results.

Mock pipeline timings are architecture overhead only and must not populate E-002.
