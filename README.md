# Say It For Me

Offline Vietnamese ↔ Korean voice translation for manufacturing communication.

This repository starts with an architecture vertical slice, not fake “AI integration.” It proves:

- explicit `vi-ko` / `ko-vi` direction contracts;
- 48 kHz capture and denoise boundary followed by 16 kHz ASR input;
- VAD-oriented bounded segmentation and backpressure assumptions;
- typed stage interfaces and ordered orchestration;
- model manifest, local-path, checksum, runtime, precision, and license metadata;
- stage-level timing and deterministic errors;
- a mock end-to-end path that can be tested before large model downloads.

The mock stages are intentionally obvious placeholders. They must never be used as benchmark evidence.

New team members start with
[`docs/team/TEAM_START_HERE.md`](docs/team/TEAM_START_HERE.md). It maps each role
to one active card, first action, reviewer and handoff time. Then paste the
master prompt, one role prompt and that one active card into the AI copilot
session.

Project source documents:

- [`docs/product/PRD_SayItForMe.md`](docs/product/PRD_SayItForMe.md) — product,
  architecture, evidence gates, risks, and execution plan.
- [`docs/technical_proposal_working_draft.md`](docs/technical_proposal_working_draft.md)
  — Phase 2 proposal working draft.
- [`docs/reference/1V_P2_TechProposal_Template.md`](docs/reference/1V_P2_TechProposal_Template.md)
  — official Phase 2 template used for compliance review.

## Repository map

```text
say-it-for-me/
├── docs/                     # Architecture, ADRs, proposal, evidence register
│   ├── product/              # Canonical PRD
│   ├── reference/            # Organizer-provided source material
│   └── team/                 # Assignment board, cards, prompts, handoffs
├── examples/                 # Explicitly non-evidence diagnostic fixtures
├── models/                   # Manifest plus git-ignored artifacts
├── reports/                  # Versioned report scaffolds; private/raw data ignored
├── scripts/                  # Reproducible benchmark entry points
├── src/say_it_for_me/
│   ├── audio/                # Framing/segmentation
│   ├── stages/               # Mock now; real adapters arrive by evidence gate
│   ├── contracts.py
│   ├── model_store.py
│   └── pipeline.py
└── tests/
```

## Run the architecture slice

PowerShell:

```powershell
$env:PYTHONPATH = "src"
python -m say_it_for_me --direction vi-ko --mock-transcript "Dừng dây chuyền số 2"
python -m unittest discover -s tests -v
python scripts/benchmark_mock.py --runs 30
```

The CLI emits JSON containing transcript, translation, output audio metadata, and stage timings.

## Model integration order

1. ASR spike: Whisper Tiny vs Base on the same Vietnamese/Korean audio.
2. NMT spike: NLLB vs M2M100/bilingual candidate with quality, latency, RSS, and license gates.
3. Audio spike: DeepFilterNet vs lightweight/bypass at each SNR.
4. TTS spike: verified Vietnamese and Korean checkpoints with Korean-speaker review.
5. Real one-direction file pipeline.
6. Microphone and UI integration.
7. Snapdragon profiling and runtime migration.

Do not add a model to the default manifest until its evidence row is complete in `docs/evidence_register.md`.
