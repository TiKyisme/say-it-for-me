# Evaluation examples

## NON-EVIDENCE warning

The two `NON_EVIDENCE_diagnostic_*` files in this directory form one synthetic
reference/prediction pair for checking JSONL parsing, selection behavior, and
metric plumbing.

They are deliberately unsuitable for benchmark or Technical Proposal evidence:

- the reference has `review_status: "unreviewed"`;
- the provenance explicitly says it is a synthetic diagnostic fixture;
- the license/rights field is explicitly not cleared; and
- the manufacturing-safety prediction intentionally drops the protected token
  `220V`.

Run them only with `--include-non-approved`. A run without that flag should
fail with `NO_APPROVED_REFERENCES`.

Do not change this example to `approved`. Build the actual evaluation set in a
separate, review-controlled location with item-level linguistic, provenance,
and license evidence.
