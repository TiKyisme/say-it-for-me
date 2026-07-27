# Gate 2 Evaluation Contract

Status: implementation-aligned contract for the current Gate 2 evaluator.

Code of record:

- `src/say_it_for_me/evaluation/schema.py`
- `src/say_it_for_me/evaluation/dataset.py`
- `src/say_it_for_me/evaluation/metrics.py`
- `src/say_it_for_me/evaluation/cli.py`

This document defines which data may become proposal evidence, the exact
JSONL interfaces, and how each reported metric is calculated. If this document
and the code disagree, stop the evaluation, reconcile them, and rerun it before
using any result.

## 1. Evidence boundary

An **official evaluation** uses only reference records whose `review_status` is
`approved`.

`approved` is an assertion by the dataset owner that all three gates have
passed:

1. **Linguistic quality:** the source/reference pair is correct and suitable
   for the stated direction and domain.
2. **Provenance:** the origin of the example is documented and auditable.
3. **License compatibility:** the team has confirmed that the data may be used
   for this competition prototype and its intended evidence/reporting use.

The evaluator validates the literal status value; it cannot independently
prove that these reviews happened. The person changing a row to `approved` is
responsible for retaining the supporting review and rights evidence.

The other valid states—`unreviewed`, `team_reviewed`, and
`native_speaker_reviewed`—are **diagnostic only**. Results that include any of
these records must not be presented as official benchmark or Technical
Proposal evidence.

Both the CLI and the public Python `build_evaluation_report()` API enforce
`approved`-only selection by default and attach the selection metadata in the
same operation as metric construction. The CLI flag
`--include-non-approved`, or the Python argument
`include_non_approved=True`, intentionally disables that evidence boundary and
labels the report selection policy `all_records_diagnostic`. Raw selected-pair
metric construction is private and is not a supported evidence API.

## 2. File-level JSONL contract

Both inputs are UTF-8 JSON Lines files:

- one JSON object per line;
- at least one record per file;
- no blank lines;
- no duplicate JSON keys within an object;
- no duplicate record IDs within a file;
- no non-finite JSON numbers such as `NaN` or `Infinity`; and
- no missing or additional fields beyond the exact schemas below.

Proposal/evidence code must create records through `load_references()` and
`load_predictions()` (or the corresponding `from_mapping()` factories).
Direct dataclass construction is an internal typed convenience and does not
perform the strict schema/Unicode validation defined here.

References and predictions are joined by `id` with exact, one-to-one coverage.
Every reference ID must have one prediction, and every prediction ID must
exist in the reference file. Output order follows reference-file order.

Important: ID coverage is checked **before** the `approved` selection policy is
applied. If one input reference file mixes approved and non-approved rows, the
prediction file must still contain a prediction for every row. For an official
run, prefer a frozen reference file containing only the approved evaluation
set.

After type and maximum-length validation, every schema string value rejects
every Unicode General Category whose name starts with `C`: `Cc` (control),
`Cf` (format, including bidirectional and
zero-width controls), `Cs` (surrogate), `Co` (private use), and `Cn`
(unassigned). This deliberately fail-closed policy prevents invalid UTF-8
scalar values and invisible/direction-changing text from entering the frozen
Vietnamese/Korean manufacturing evaluation set. That set has no approved need
for Unicode `C*` characters; a future legitimate need requires an explicit,
reviewed change to both this contract and the validator.

A violation returns `UNSAFE_UNICODE_CATEGORY` with a safely printable
diagnostic containing the field, JSONL path and line, Unicode category,
character index, and `U+XXXX` code point. The diagnostic never reproduces the
unsafe character itself.

All string values must also already use Unicode NFC normalization. Unless a
field-specific exception is stated, they must be non-empty after trimming and
must not contain leading or trailing whitespace.

## 3. Reference JSONL schema

Each reference line must contain exactly these ten fields:

| Field | JSON type | Required contract |
|---|---|---|
| `id` | string | 1–128 ASCII characters. The first character is alphanumeric; remaining characters may be ASCII alphanumerics, `.`, `_`, or `-`. Must be unique in the file. |
| `direction` | string | Exactly `vi-ko` or `ko-vi`. Direction is explicit; it is not inferred from text. |
| `source` | string | Non-empty source utterance, trimmed, NFC, maximum 10,000 characters. |
| `reference` | string | Non-empty target-language reference, trimmed, NFC, maximum 10,000 characters. |
| `domain` | string | A 1–64 character lowercase ASCII slug. The first character is alphanumeric; remaining characters may be alphanumerics, `.`, `_`, or `-`. |
| `safety_critical` | boolean | A JSON `true` or `false`. Integers such as `0` and `1` are rejected. |
| `protected_tokens` | array of strings | May be empty. Each item is non-empty, trimmed, NFC, at most 256 characters, and unique within the array. Every item must occur as an exact literal substring in both `source` and `reference`. |
| `provenance` | string | Non-empty provenance/audit description, trimmed, NFC, maximum 2,048 characters. |
| `license` | string | Non-empty license or rights status, trimmed, NFC, maximum 256 characters. |
| `review_status` | string | Exactly `unreviewed`, `team_reviewed`, `native_speaker_reviewed`, or `approved`. Only `approved` is eligible for official evidence. |

Example shape only:

```json
{"id":"factory-001","direction":"vi-ko","source":"Dừng máy A-17.","reference":"기계 A-17을 멈추세요.","domain":"manufacturing-safety","safety_critical":true,"protected_tokens":["A-17"],"provenance":"team-authored:factory-smoke-v1; review-log:<path-or-id>","license":"team-owned; rights-check:<path-or-id>","review_status":"approved"}
```

The example above demonstrates shape, not approval evidence. Real
`provenance`, `license`, and review records must remain traceable to the
specific evaluation item.

## 4. Prediction JSONL schema

Each prediction line must contain exactly these two fields:

| Field | JSON type | Required contract |
|---|---|---|
| `id` | string | Same syntax as reference `id`; must be unique in the prediction file and match one reference ID. |
| `prediction` | string | NFC string, maximum 10,000 characters. Empty output is allowed so model failure remains measurable. Leading/trailing whitespace is accepted and then normalized for CER/WER. Unicode `C*` characters are rejected by the file-level policy. |

Example:

```json
{"id":"factory-001","prediction":"기계 A-17을 멈추세요."}
```

## 5. Selection behavior

The default policy is `approved_only`:

- included: pairs with `review_status == "approved"`;
- excluded: all other pairs, reported with their ID and review status; and
- failure: `NO_APPROVED_REFERENCES` if no approved pair remains.

The diagnostic override `--include-non-approved` uses every joined pair and
sets the selection policy to `all_records_diagnostic`. It must not be used to
produce proposal claims.

The JSON report includes a `selection` object so a reviewer can verify the
policy, included IDs, and excluded IDs. Do not detach a metric value from this
selection metadata.

## 6. Metric contract

### 6.1 CER and WER normalization

Before CER or WER is computed, both reference and prediction undergo the same
minimal normalization:

1. normalize Unicode to NFC;
2. split on Unicode whitespace; and
3. join the resulting segments with one ASCII space.

Case and punctuation remain significant. No lowercasing, punctuation removal,
stemming, morphological analysis, or language-specific tokenization occurs.

CER uses character-level Levenshtein distance after normalization. The single
normalized spaces are characters and therefore count as CER units.

WER uses **whitespace-delimited tokens** and Levenshtein distance. This is a
deliberately simple, language-neutral baseline, not a linguistically complete
Korean word-error measure. Korean spacing and agglutinative morphology can
make semantically close outputs look disproportionately different or hide
meaningful sub-token differences. Treat Korean WER as a limited diagnostic;
interpret it alongside CER, chrF++, protected-token preservation, and human
review.

Corpus CER/WER are micro-averaged:

```text
rate = sum(edit distances over examples) / sum(reference units over examples)
```

### 6.2 Protected-token preservation

Protected-token preservation is occurrence recall:

```text
preserved occurrences / expected reference occurrences
```

Matching is an exact, case-sensitive literal substring comparison after
Unicode NFC normalization. It does not use word boundaries or fuzzy matching.
For each token, the preserved count is capped at its count in the reference,
so repeating a token cannot earn extra credit.

The overall rate is `null` when the selected dataset contains no expected
protected-token occurrences. `failed_example_ids` lists examples where at
least one required occurrence is missing.

### 6.3 BLEU and chrF++

Official BLEU and chrF++ require the optional `sacrebleu` dependency:

```powershell
python -m pip install -r requirements-evaluation.txt
```

The implementation uses:

- `sacrebleu.metrics.BLEU()` for corpus BLEU; and
- `sacrebleu.metrics.CHRF(word_order=2)` for corpus chrF++.

Scores are calculated separately by target language (`ko` for `vi-ko`, `vi`
for `ko-vi`). The report records the installed `sacrebleu` version and metric
signatures. Preserve those fields with any cited score.

If `sacrebleu` is not installed, the CLI still completes but reports
`status: "unavailable"` for translation metrics. Such a report does not contain
official BLEU/chrF++ results and must not be represented as if it does.

### 6.4 Report slices

The report contains:

- dataset counts for direction, domain, safety-critical examples, provenance,
  license, and review status;
- overall CER, WER, and protected-token preservation;
- the same quality metrics split by target language;
- BLEU and chrF++ split by target language; and
- the selection policy and included/excluded IDs.

## 7. Running the evaluator

From the `say-it-for-me` repository root:

```powershell
$env:PYTHONPATH = "src"
python -m say_it_for_me.evaluation evaluate `
  --references path/to/references.jsonl `
  --predictions path/to/predictions.jsonl
```

A successful run writes the JSON report to standard output. Dataset validation
errors write a structured JSON error to standard error and return exit code
`2`.

To inspect the deliberately non-approved fixture in
`examples/evaluation/`, use:

```powershell
$env:PYTHONPATH = "src"
python -m say_it_for_me.evaluation evaluate `
  --references examples/evaluation/NON_EVIDENCE_diagnostic_references.jsonl `
  --predictions examples/evaluation/NON_EVIDENCE_diagnostic_predictions.jsonl `
  --include-non-approved
```

This command is diagnostic only. Omitting `--include-non-approved` must fail
with `NO_APPROVED_REFERENCES`, which confirms that the evidence gate is active.

## 8. Proposal-evidence checklist

Before a number is copied into the Technical Proposal:

- freeze and identify the exact reference and prediction files;
- confirm every selected row is `approved` and has retained linguistic,
  provenance, and license-review evidence;
- run without `--include-non-approved`;
- confirm `selection.policy` is `approved_only`;
- confirm the expected included IDs and investigate every exclusion;
- confirm `sacrebleu` reports `status: "available"` before citing BLEU or
  chrF++;
- retain the complete JSON report, dependency version, and metric signatures;
- report results by target language as well as overall where applicable; and
- disclose the whitespace-WER limitation, especially for Korean.

Never use files whose names or contents say `NON_EVIDENCE` as benchmark or
proposal evidence.
