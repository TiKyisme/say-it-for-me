# Vietnamese–Korean Factory Draft Set

`VI_KO_FACTORY_DRAFT_30.csv` contains 30 team-authored Vietnamese → Korean **draft** records for Phase 2 planning:

- 12 records are marked `safety_critical=true`.
- The rows identify protected numbers, units, machine IDs, part IDs, and error codes where relevant.
- Every row has `review_status=draft` and `korean_reviewer_status=not_assigned`.
- The Korean text is **not gold data**, must not be used for official BLEU/chrF++/quality evidence, and must be reviewed by a qualified Korean reviewer before any promotion.
- This CSV intentionally uses the sprint-requested `draft` status. It is not yet an evaluator JSONL file: the current evaluator allows only `unreviewed`, `team_reviewed`, `native_speaker_reviewed`, or `approved`, and official evidence requires `approved` plus item-level provenance and rights review.

## Required review workflow

1. Member 1 confirms a Korean reviewer and records their qualification and review date.
2. Reviewer checks source intent, Korean wording, safety context, and each protected token.
3. Dataset owner records source/provenance and rights evidence for each row.
4. Only after all review gates, convert selected records to the strict evaluator JSONL schema and set `review_status=approved`.
5. Retain reviewer records and run the evaluator without the diagnostic override before citing a metric.
