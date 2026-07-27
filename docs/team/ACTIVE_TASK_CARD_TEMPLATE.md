# ACTIVE TASK CARD TEMPLATE

Every active task has one DRI. Reviewers may be multiple; owners may not.

```text
TASK ID / TITLE:
CARD VERSION / LAST UPDATED:
DRI:
REVIEWER:
GATE DECISION OWNER:
STATUS: NOT_STARTED | IN_PROGRESS | BLOCKED | REVIEW | DONE
START / DEADLINE: DD/MM HH:mm ICT → DD/MM HH:mm ICT
CHECKPOINTS: [dependency-relevant intermediate handoff times]

OUTCOME:
[One observable result, not an activity.]

INPUTS / SOURCE OF TRUTH:
- [path, decision, dataset or upstream artifact]

IN SCOPE:
- [...]

OUT OF SCOPE:
- [...]

OUTPUTS:
- [exact repository path]

STEPS:
1. [3–6 ordered steps]

ACCEPTANCE:
- Command: [...]
- PASS threshold: [...]
- Required failure/edge test: [...]

EVIDENCE:
- Raw artifact path:
- Environment/model/data metadata:

DEPENDENCIES:
- [owner + artifact + due time]

ESCALATE WHEN:
- [fact-based condition and decision owner]

HANDOFF:
- Next owner / expected acknowledgement / due time

REVIEW RECORD:
- PASS | CHANGES_REQUESTED | PENDING
- Reviewed command/evidence:
- Recorded by / at:
```
