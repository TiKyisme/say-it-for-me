# Contributing

## Branch and ownership rules

- `main` is the integration branch. TL alone creates the reviewed initial
  baseline commit on `main`; this is the only pre-Gate-0 direct commit.
- Immediately after that commit, TL creates `tl/g0-operations` from the
  baseline. Roster/fact/card edits and the APP Gate 0 review handoff happen on
  that branch. No later development occurs directly on `main`.
- Branch name: `<role>/<task-id>-<short-name>`, for example
  `app/g2-evaluation-schema`.
- One active task card and one primary outcome per branch.
- Preserve user/unrelated changes; inspect `git status` before editing.
- Do not edit another role’s owned files without a handoff recorded in the task card.
- Shared contracts, ADRs, proposal master and model selection require TL review.

## Review requirements

- Every card has one DRI.
- The named reviewer independently runs or inspects the card's acceptance
  evidence and records `PASS` or `CHANGES_REQUESTED` in that card.
- TL records the cross-team gate decision after required reviews.
- A TL-authored card still requires its named non-TL reviewer to record `PASS`.

| Change | Required reviewer |
|---|---|
| ASR/NMT adapter or evidence | ATE owner + TL |
| Audio/VAD/denoise/TTS | AUD owner + ATE for ASR-impact claims |
| Dataset/evaluation/UI | APP owner + ATE for metric logic |
| Shared contract/pipeline/ADR | TL + affected specialist |
| Proposal master/evidence claim | TL + claim owner |

The author may not self-approve their card. A gate decision does not erase a
reviewer's failed acceptance result; the defect must be fixed or explicitly
handled through an ADR/scope-cut decision.

## Pull request / handoff content

- Active task ID and outcome.
- Changed artifacts.
- Reproduction/test commands and results.
- Target/estimate/measured labels.
- Model/data/runtime/hardware/license metadata where relevant.
- Known failures, excluded runs and privacy impact.
- Next owner and due date.

## Required local checks

PowerShell:

```powershell
$env:PYTHONPATH = "src"
python -m compileall -q src scripts tests
python -m unittest discover -s tests -v
```

Run specialist benchmark/evaluation commands in addition to these checks.

## Repository hygiene

Never commit:

- downloaded model weights;
- raw/private audio without explicit consent and repository approval;
- credentials, tokens or personal contact details;
- generated output containing sensitive text/audio;
- a result table without its raw/config metadata.
