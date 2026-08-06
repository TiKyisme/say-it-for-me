# ATE ACTIVE CARD — G2 Evaluation Contract Review

> **Card version:** 0.2; updated 27/07/2026

- **DRI:** ATE — **Nguyễn Tiến Đạt**
- **Reviewer / gate decision owner:** TL
- **Status:** NOT_STARTED
- **Start / DRI handoff deadline:** 28/07/2026 12:00 ICT → 30/07/2026 11:00 ICT
- **Checkpoint:** card acknowledgement and exact candidate source links by
  28/07 17:30; APP review input arrives 29/07 15:00.
- **TL gate decision deadline:** 30/07/2026 12:00 ICT

## Outcome

ATE independently confirms that the evaluation contract can compare ASR/NMT
candidates fairly, records a finite PASS/defect decision, and locks the exact
candidate/checkpoint/runtime inventory.

## Inputs / source of truth

- `docs/team/handoffs/APP_evaluation_foundation.md` — due 29/07 15:00.
- `docs/testing/evaluation_contract.md`
- `src/say_it_for_me/evaluation/`
- `tests/test_evaluation_cli.py`
- `tests/test_evaluation_dataset.py`
- `tests/test_evaluation_metrics.py`
- `docs/evidence_register.md`, entries E-004 and E-005.
- `docs/product/PRD_SayItForMe.md`, model decision gates.

## In scope

- Join/selection policy; normalization and aggregation; standardized metric
  boundary; protected-token logic; exact ASR/NMT candidate inventory.

## Out of scope

- Rewriting reference text/provenance, selecting a winning model, or changing a
  shared schema without TL decision.

## Outputs

Create these new files if absent:

- `docs/team/handoffs/ATE_evaluation_review.md`
- `reports/asr/candidate_inventory.md`
- `reports/nmt/candidate_inventory.md`

## Steps

1. Re-run the evaluator test suite and both diagnostic fixture paths.
2. Review exact ID coverage, explicit direction and `approved_only` policy.
3. Review CER/whitespace-WER normalization and document the Korean limitation.
4. Install/use the optional standardized dependency and inspect BLEU/chrF++
   version/signatures.
5. Review protected numbers, units, equipment IDs and error-code occurrence
   recall.
6. Record exact candidate checkpoint, revision, runtime, precision and license.
7. Write `PASS` or a finite defect list; send it to APP and TL.

## Acceptance

Run from repository root:

```powershell
python -m pip install -r requirements-evaluation.txt
$env:PYTHONPATH = "src"
python -m unittest discover -s tests -p "test_evaluation_*.py" -v
python -m say_it_for_me.evaluation evaluate `
  --references examples/evaluation/NON_EVIDENCE_diagnostic_references.jsonl `
  --predictions examples/evaluation/NON_EVIDENCE_diagnostic_predictions.jsonl `
  --include-non-approved
```

Then repeat the evaluator command without `--include-non-approved`.

- **PASS threshold:** 25/25 evaluation tests pass; diagnostic output says
  `all_records_diagnostic`; default mode fails with
  `NO_APPROVED_REFERENCES`; installed `sacrebleu` reports version and both
  signatures; the review file records `PASS`.
- **Required failure/edge test:** no non-approved Korean/reference row can enter
  official results through the CLI or public API; unsafe Unicode returns a
  structured error; Korean whitespace-WER is not presented as a complete
  linguistic quality measure.
- **Candidate threshold:** both inventories state exact checkpoint, revision,
  runtime, precision, license and download/artifact plan; no winner is claimed.

## Evidence

- Review decision: `docs/team/handoffs/ATE_evaluation_review.md`
- Candidate metadata: `reports/asr/candidate_inventory.md` and
  `reports/nmt/candidate_inventory.md`
- Environment metadata: Python and `sacrebleu` versions recorded in the review.

## Dependencies

- APP → evaluation handoff and passing unit tests → 29/07 15:00.
- TL → decision on any schema/license defect → within four working hours of
  escalation and before 30/07 10:00.

## Escalate when

The model/data license, Korean normalization rule, standardized dependency or
selection policy is ambiguous enough to change candidate ranking or proposal
evidence.

## Handoff

ATE sends the review to APP and TL by 30/07 11:00. TL records `PASS` or
`CHANGES_REQUESTED` below by 30/07 12:00. APP closes finite evaluator defects;
ATE begins the ASR/NMT runner card only after this decision.

## Review record

- **TL result:** PENDING
- **Reviewed artifact/command:** PENDING
- **Recorded by / at:** PENDING
