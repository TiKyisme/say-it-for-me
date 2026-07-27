# APP → ATE HANDOFF — Gate 2 Evaluation Foundation

> **Prepared:** 27/07/2026  
> **Status:** READY_FOR_NAMED_REVIEWER  
> **Evidence class:** implementation/contract evidence, not model-quality evidence

## Deliverable

Strict reference/prediction JSONL validation, exact ID join, approved-only
official selection, diagnostic override, CER/whitespace-WER, protected-token
occurrence recall, standardized `sacrebleu` adapter and machine-readable CLI
report.

## Artifact paths

- `src/say_it_for_me/evaluation/`
- `tests/test_evaluation_cli.py`
- `tests/test_evaluation_dataset.py`
- `tests/test_evaluation_metrics.py`
- `tests/test_evaluation_unicode_cli.py`
- `docs/testing/evaluation_contract.md`
- `examples/evaluation/`
- `pyproject.toml`
- `requirements-evaluation.txt`

## Reproduction commands

Run from repository root:

```powershell
$env:PYTHONPATH = "src"
python -m compileall -q src scripts tests
python -m unittest discover -s tests -v
python -m say_it_for_me.evaluation evaluate `
  --references examples/evaluation/NON_EVIDENCE_diagnostic_references.jsonl `
  --predictions examples/evaluation/NON_EVIDENCE_diagnostic_predictions.jsonl `
  --include-non-approved
```

Repeat the evaluator command without `--include-non-approved` to exercise the
official evidence boundary.

## Prepared-state result

- `compileall`: PASS.
- Repository tests: **32/32 PASS** on 27/07/2026.
- Evaluation tests: **25/25 PASS**.
- Diagnostic fixture: PASS with
  `selection.policy = all_records_diagnostic`.
- Default run on the same unapproved fixture: correctly rejected with
  `NO_APPROVED_REFERENCES`.
- Public report API: approved-only by default; mixed pending rows cannot affect
  official metrics; diagnostic inclusion requires an explicit argument.
- Unsafe surrogate/bidi/zero-width strings: rejected with
  `UNSAFE_UNICODE_CATEGORY`; subprocess CLI returns structured JSON and exit 2.
- Protected-token diagnostic: `0.5` by design because `220V` is omitted.
- `sacrebleu`: **UNAVAILABLE in the prepared environment**; no BLEU/chrF++
  value is claimed.

These prepared-state results do not replace the named ATE's independent run.

## Review decisions requested from ATE

1. Is exact one-to-one ID coverage before approval filtering the intended rule?
2. Is NFC plus whitespace normalization acceptable for the first baseline?
3. Is Korean whitespace-WER sufficiently caveated and paired with CER/chrF++?
4. Is exact, case-sensitive occurrence recall appropriate for protected tokens?
5. Does a real `sacrebleu` install emit the expected version and signatures?
6. Is the default `approved_only` / diagnostic override boundary acceptable?

Record `PASS` or a finite defect list in
`docs/team/handoffs/ATE_evaluation_review.md`.

## Known limitations

- No traceable 20-pair approved smoke set exists yet.
- No Korean reviewer or item-level review log is recorded in
  `docs/team/TEAM_FACTS.md`.
- Dataset licenses have not passed TL review.
- The prepared environment lacks the optional `sacrebleu` package.
- Whitespace-WER is a limited diagnostic for Korean.
- Strict evidence records must come from the loaders/`from_mapping()` factories;
  direct dataclass constructors do not perform schema/Unicode validation.
- Reports do not yet embed input-file hashes, evaluator version, Python version
  or source revision; the ATE run must retain these out-of-band.
- The `NON_EVIDENCE` fixture must never be copied into proposal metrics.

## Next owner / due date

- **ATE:** independent contract and real dependency review by 30/07 11:00 ICT.
- **TL:** gate decision by 30/07 12:00 ICT.
- **APP:** after gate PASS, open a separate card for the traceable 20-pair set.
