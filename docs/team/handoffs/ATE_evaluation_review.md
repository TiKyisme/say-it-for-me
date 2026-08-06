# ATE REVIEW — Gate 2 Evaluation Contract

> **Reviewer:** ATE — Nguyễn Tiến Đạt  
> **Status:** NOT_STARTED  
> **Due:** 30/07/2026 11:00 ICT  
> **Decision:** PENDING — `PASS` or `CHANGES_REQUESTED`

This file is the independent review record for
`docs/team/handoffs/APP_evaluation_foundation.md`. Do not copy model-quality
numbers into this review; it approves or rejects the evaluation boundary only.

## Environment

| Field | Value |
|---|---|
| Reviewer / run time | PENDING |
| OS / CPU | PENDING |
| Python | PENDING |
| `sacrebleu` version | PENDING |
| Source revision / worktree state | PENDING |

## Reproduction result

| Check | Expected | Actual | PASS? |
|---|---|---|:---:|
| Evaluation unit tests | 25/25 pass | PENDING | [ ] |
| Diagnostic fixture | `all_records_diagnostic` | PENDING | [ ] |
| Same fixture in default mode | `NO_APPROVED_REFERENCES`, exit 2 | PENDING | [ ] |
| Public API with pending-only rows | `NO_APPROVED_REFERENCES` | PENDING | [ ] |
| Unsafe Unicode subprocess case | structured `UNSAFE_UNICODE_CATEGORY`, exit 2 | PENDING | [ ] |
| Real BLEU adapter | version and signature present | PENDING | [ ] |
| Real chrF++ adapter | `word_order=2` signature present | PENDING | [ ] |

## Contract review

- [ ] Exact one-to-one ID coverage is appropriate.
- [ ] Proposal inputs use strict loaders/`from_mapping()`, not direct dataclass
      construction.
- [ ] `approved_only` is the default at both CLI and public Python API.
- [ ] Diagnostic inclusion is explicit and visibly labelled.
- [ ] NFC/whitespace normalization is reproducible.
- [ ] Korean whitespace-WER limitation is sufficient and will be disclosed.
- [ ] Protected-token exact occurrence recall is appropriate.
- [ ] Provenance/license/review fields are sufficient for the first smoke set.
- [ ] No diagnostic fixture can be mistaken for proposal evidence.
- [ ] The run preserves input hashes plus evaluator/Python/source revisions
      out-of-band until report metadata is implemented.

## Finite defect list

Write `NONE` for PASS. Otherwise, give each defect an ID, owner, exact file,
acceptance test and due time.

PENDING

## Decision and handoff

- **ATE decision:** PENDING
- **Reason:** PENDING
- **APP acknowledgement / at:** PENDING
- **TL gate decision / at:** PENDING
