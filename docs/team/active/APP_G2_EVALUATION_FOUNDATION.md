# APP ACTIVE CARD — G2 Evaluation Foundation

> **Card version:** 0.2; updated 27/07/2026

- **DRI:** APP — **UNASSIGNED; human name required**
- **Reviewer:** ATE
- **Gate decision owner:** TL after ATE records `PASS`
- **Status:** REVIEW
- **Start / handoff deadline:** 28/07/2026 12:00 ICT → 29/07/2026 15:00 ICT
- **ATE review deadline:** 30/07/2026 11:00 ICT
- **TL gate decision deadline:** 30/07/2026 12:00 ICT

## Outcome

One command validates reference/prediction JSONL and emits reproducible CER,
WER, protected-token, standardized BLEU and chrF++ fields without silently
accepting any non-approved reference as proposal evidence.

## Inputs / source of truth

- `docs/product/PRD_SayItForMe.md`, evaluation section.
- `docs/evidence_register.md`, E-004/E-005/E-011.
- `docs/execution_backlog.md`, Gate 2.
- `docs/testing/evaluation_contract.md`.

## In scope

- Strict JSONL schema/load/join; approved-only selection; CER/WER;
  protected-token occurrence recall; standardized metric adapter; CLI/tests;
  clearly labelled diagnostic fixtures.

## Out of scope

- Creating or approving the real 20-pair set, inventing Korean references,
  selecting ASR/NMT candidates, or presenting diagnostic values as evidence.

## Outputs

- `src/say_it_for_me/evaluation/`
- `tests/test_evaluation_cli.py`
- `tests/test_evaluation_dataset.py`
- `tests/test_evaluation_metrics.py`
- `tests/test_evaluation_unicode_cli.py`
- `docs/testing/evaluation_contract.md`
- `examples/evaluation/README.md`
- `examples/evaluation/NON_EVIDENCE_diagnostic_references.jsonl`
- `examples/evaluation/NON_EVIDENCE_diagnostic_predictions.jsonl`
- `docs/team/handoffs/APP_evaluation_foundation.md`
- `pyproject.toml` and `requirements-evaluation.txt`

## Steps

1. [x] Implement strict reference/prediction records and exact ID coverage.
2. [x] Validate direction, domain, provenance, license and review status.
3. [x] Enforce `approved_only`; expose a diagnostic-only override.
4. [x] Implement CER/whitespace-WER and protected-token occurrence recall.
5. [x] Make the public report API enforce selection and attach policy metadata.
6. [x] Reject unsafe Unicode categories with structured CLI errors.
7. [x] Integrate the `sacrebleu` BLEU/chrF++ adapter and signatures.
8. [x] Add CLI/public-API success, failure, selection and Unicode tests.
9. [x] Document the contract and add visibly `NON_EVIDENCE` fixtures.
10. [ ] Named APP sends the handoff; named ATE independently reviews it.

## Acceptance

Run from repository root:

```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests -p "test_evaluation_*.py" -v
python -m say_it_for_me.evaluation evaluate `
  --references examples/evaluation/NON_EVIDENCE_diagnostic_references.jsonl `
  --predictions examples/evaluation/NON_EVIDENCE_diagnostic_predictions.jsonl `
  --include-non-approved
```

Then repeat the evaluator command without `--include-non-approved`.

- **PASS threshold:** 25/25 evaluation tests pass; diagnostic output records
  `all_records_diagnostic`, included IDs and `sacrebleu` availability; default
  mode fails with `NO_APPROVED_REFERENCES`.
- **Required edge test:** missing/unknown/duplicate IDs, non-approved-only
  datasets and unsafe Unicode fail with stable structured errors; a public
  Python API call cannot bypass the evidence policy.
- **Dependency behavior:** missing `sacrebleu` reports `status: unavailable`
  and never substitutes a home-grown score.
- **Review threshold:** ATE records `PASS`; TL records the Gate 2 foundation
  decision.

## Evidence

- Contract: `docs/testing/evaluation_contract.md`
- Tests: 25/25 evaluation tests and 32/32 repository tests passed on 27/07/2026.
- Diagnostic fixture policy: `examples/evaluation/README.md`
- Handoff: `docs/team/handoffs/APP_evaluation_foundation.md`
- No official BLEU/chrF++ or dataset-quality claim exists yet.

## Dependencies

- TL → named APP/ATE assignment → 28/07 12:00.
- APP → implementation handoff → ATE by 29/07 15:00.
- ATE → independent metric/selection review → APP/TL by 30/07 11:00.
- TL → `PASS` or `CHANGES_REQUESTED` gate decision → 30/07 12:00.

## Escalate when

Korean normalization, dataset license/review evidence, standardized dependency,
or a required report field cannot be represented without changing the schema or
proposal evidence policy.

## Handoff

ATE follows `docs/team/active/ATE_G2_CONTRACT_REVIEW.md`, records the review in
`docs/team/handoffs/ATE_evaluation_review.md`, and returns a finite defect list
or `PASS`. APP does not start the approved 20-pair dataset card until TL records
the foundation decision.

## Review record

- **ATE result:** PENDING
- **TL gate decision:** PENDING
- **Reviewed artifact/command:** PENDING
- **Recorded by / at:** PENDING
