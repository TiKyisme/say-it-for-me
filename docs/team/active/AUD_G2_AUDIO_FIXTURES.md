# AUD ACTIVE CARD — G2 Audio Fixtures and Noise Protocol

> **Card version:** 0.2; updated 27/07/2026

- **DRI:** AUD — **UNASSIGNED; human name required**
- **Reviewer:** ATE
- **Gate decision owner:** TL after ATE records `PASS`
- **Status:** NOT_STARTED
- **Start / deadline:** 28/07/2026 12:00 ICT → 31/07/2026 12:00 ICT
- **Checkpoints:** protocol/inventory 28/07 17:30; tests 29/07 17:30;
  manifest handoff 30/07 12:00.

## Outcome

A deterministic 48 kHz WAV fixture/noise protocol exists for clean and noisy
ASR comparison without committing private recordings.

## Inputs / source of truth

- `docs/product/PRD_SayItForMe.md`, audio contract.
- `docs/adr/ADR-002-bounded-chunk-pipeline.md`
- `src/say_it_for_me/audio/segmenter.py`
- `tests/test_segmenter.py`
- `docs/team/TEAM_FACTS.md`, consent and approved-source decisions.

## In scope

- Mono 48 kHz WAV validation, deterministic noise mixing at 15/10/5/0 dB SNR,
  synthetic test fixtures, manifest/provenance/consent fields and candidate
  inventory.

## Out of scope

- Committing raw human recordings, ASR model ranking, microphone UI or choosing
  an unlicensed noise/audio source.

## Outputs

Create these new paths if absent:

- `tests/data/audio/manifest.example.json`
- `docs/testing/audio_fixture_protocol.md`
- `src/say_it_for_me/audio/wav_io.py`
- `src/say_it_for_me/audio/noise_mix.py`
- `tests/test_audio_contract.py`
- `tests/test_noise_mix.py`
- `reports/audio/candidate_inventory.md`
- `reports/tts/candidate_inventory.md`

## Steps

1. Define exact WAV, speaker/consent/provenance, source-license and split fields.
2. Add read/write validation for mono 48 kHz fixture boundaries.
3. Define the deterministic mixing equation, seed, scaling and clipping policy.
4. Generate tiny synthetic fixtures for contract tests only.
5. Document how approved real VI/KO recordings stay local and enter a manifest.
6. Record exact denoiser/VAD/VI-TTS/KO-TTS candidate identifiers and licenses.
7. Hand the manifest, protocol and command to ATE; obtain a recorded review.

## Acceptance

Run from repository root:

```powershell
$env:PYTHONPATH = "src"
python -m unittest `
  tests.test_audio_contract `
  tests.test_noise_mix `
  tests.test_segmenter -v
```

- **PASS threshold:** all audio/segment tests pass; the manifest is
  machine-readable; the same inputs/seed/SNR produce byte-identical output.
- **Required failure/edge tests:** reject non-mono and non-48 kHz fixtures;
  reject missing consent/provenance for real audio; prevent clipping or report
  the deterministic scaling used.
- **Privacy threshold:** only tiny synthetic audio may be committed; raw human
  audio paths remain ignored.

## Evidence

- Contract and reproduction procedure: `docs/testing/audio_fixture_protocol.md`
- Machine-readable metadata: `tests/data/audio/manifest.example.json`
- Test evidence: `tests/test_audio_contract.py` and `tests/test_noise_mix.py`
- Candidate metadata: `reports/audio/candidate_inventory.md` and
  `reports/tts/candidate_inventory.md`

## Dependencies

- TL; APP supplies consent/reviewer facts → consent, Korean reviewer and approved-source status in
  `docs/team/TEAM_FACTS.md` → 29/07 12:00.
- AUD → synthetic manifest/protocol handoff → ATE by 30/07 12:00.
- ATE → technical review result → AUD/TL by 31/07 12:00.

Synthetic contract work may proceed while real human audio is blocked.

## Escalate when

No licensed/consented Korean audio exists by 30/07, a noise-source license is
unclear, or the proposed mixing/sample-rate contract would change ADR-002.

## Handoff

ATE records `PASS` or `CHANGES_REQUESTED` below by 31/07 12:00. On `PASS`, TL
records the audio-fixture sub-gate and ATE may start equal ASR input-set runs.

## Review record

- **ATE result:** PENDING
- **Reviewed artifact/command:** PENDING
- **Recorded by / at:** PENDING
