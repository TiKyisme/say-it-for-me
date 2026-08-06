# TL ACTIVE CARD — G0 Operations and Repository Rules

> **Card version:** 0.2; updated 27/07/2026

- **DRI:** TL — **Team Lead; personal name not supplied**
- **Reviewer:** APP
- **Gate decision owner:** TL, only after APP records `PASS`
- **Status:** BLOCKED — HUMAN_INPUT_REQUIRED
- **Start / deadline:** 27/07/2026 18:00 ICT → 29/07/2026 12:00 ICT
- **Baseline completed:** `7bc1b8ad5528200a735653f580d25cecf1008536`
  on `main`, 27/07/2026.
- **Remaining checkpoints:** roster/capacity by 28/07 12:00;
  device/reviewer/consent facts by 17:30 ICT.

## Outcome

All external/logistics facts, human ownership, capacity, device access and
repository rules are explicit, so every specialist can select one card and
start without guessing.

## Inputs / source of truth

- Organizer email: official deadline end of 21/08/2026.
- `docs/team/TEAM_START_HERE.md`
- `docs/team/TEAM_PLAYBOOK.md`
- `docs/execution_backlog.md`
- Direct answers from the four members; organizer answers where required.

## In scope

- Named role mapping, availability, baseline PC, device access, Korean reviewer,
  consent/privacy decisions and unresolved organizer questions.
- Repository branch/review/CI decision and active-card acknowledgements.

## Out of scope

- Inventing unavailable hardware, reviewer approval or organizer constraints.
- Model selection, benchmark claims or external form submission.

## Outputs

- `docs/team/TEAM_FACTS.md` — replace every provisional role placeholder or `BLOCKED`
  cell with a confirmed value, explicit `NONE`, or a dated blocker that names
  its decision owner.
- `docs/team/TEAM_START_HERE.md` — replace every roster placeholder with the mapped name.
- `docs/team/active/TL_G0_OPERATIONS.md`
- `docs/team/active/ATE_G2_CONTRACT_REVIEW.md`
- `docs/team/active/AUD_G2_AUDIO_FIXTURES.md`
- `docs/team/active/APP_G2_EVALUATION_FOUNDATION.md`
- `CONTRIBUTING.md` — branch/review/CI rules.

## Steps

1. Review the current worktree and create the initial `main` baseline commit by
   28/07 11:30; retain its full SHA.
2. From that exact commit, create and switch to `tl/g0-operations`. Make every
   subsequent Gate 0 edit on this branch; do not edit directly on `main`.
3. Collect four names and map exactly one person to each role.
4. Record hours/week, unavailable dates and prompt acknowledgement.
5. Record the baseline PC and every available Snapdragon/Android/RB3 device;
   use `NONE` when none is available.
6. Confirm Korean reviewer, two review windows and audio consent with APP.
7. Record organizer questions with sender, sent date and decision deadline;
   confirm branch/review and CI mode.
8. Record the baseline's full SHA in `docs/team/TEAM_FACTS.md`, replace the DRI
   placeholders in all four cards, and update the assignment
   board.
9. Set `docs/team/TEAM_FACTS.md` to
   `REVIEW — GATE 0 APP REVIEW PENDING`, and set the
   `docs/team/TEAM_START_HERE.md` banner to
   `ROSTER ASSIGNED — GATE 0 REVIEW PENDING`.
10. Run the pre-review command, commit the authorized Gate 0 files on
    `tl/g0-operations`, and hand APP the exact branch and commit SHA by
    29/07 10:00.
11. APP reviews every row and records the result below by 29/07 12:00.
12. After APP records `PASS`, atomically change `docs/team/TEAM_FACTS.md` to
   `READY — GATE 0 FACTS REVIEWED`, change the
   `docs/team/TEAM_START_HERE.md` banner to `READY — GATE 0 PASS`, and
   synchronize the TL board-row/card status to `DONE`.

## Acceptance

### Pre-review command — APP runs this before recording `PASS`

Run from repository root:

```powershell
$teamRoleRows = Get-Content docs/team/TEAM_FACTS.md |
  Where-Object { $_ -match '^\| (TL|ATE|AUD|APP) \|' }
$taskDriLines = Get-Content docs/team/active/*.md |
  Where-Object { $_ -match '^- \*\*DRI:\*\*' }
$startRoleRows = Get-Content docs/team/TEAM_START_HERE.md |
  Where-Object { $_ -match '^\| \*\*(TL|ATE|AUD|APP)\*\* \|' }
$factsReview = Select-String `
  -Path docs/team/TEAM_FACTS.md `
  -Pattern '^> \*\*Status:\*\* REVIEW — GATE 0 APP REVIEW PENDING'
$startReview = Select-String `
  -Path docs/team/TEAM_START_HERE.md `
  -Pattern '^> \*\*Current onboarding status:\*\* \*\*ROSTER ASSIGNED — GATE 0 REVIEW PENDING'
$teamNames = $teamRoleRows | ForEach-Object {
  (($_ -split '\|')[2]).Trim().Trim('*')
}
$baselineFactLine = (
  Select-String `
    -Path docs/team/TEAM_FACTS.md `
    -Pattern '^\| Initial baseline commit SHA \|'
).Line
$baselineMatch = [regex]::Match(
  $baselineFactLine,
  '\b[0-9a-fA-F]{40}\b'
)
$baselineIsAncestor = $false
if ($baselineMatch.Success) {
  $baselineRecordedSha = $baselineMatch.Value
  git cat-file -e "${baselineRecordedSha}^{commit}" 2>$null
  if ($LASTEXITCODE -eq 0) {
    git merge-base --is-ancestor $baselineRecordedSha HEAD
    $baselineIsAncestor = $LASTEXITCODE -eq 0
  }
}
$currentBranch = git branch --show-current
if (
  $teamRoleRows.Count -ne 4 -or
  $taskDriLines.Count -ne 4 -or
  $startRoleRows.Count -ne 4 -or
  $factsReview.Count -ne 1 -or
  $startReview.Count -ne 1 -or
  ($teamNames | Sort-Object -Unique).Count -ne 4 -or
  $teamRoleRows -match 'ROLE_PLACEHOLDER|\*\*BLOCKED' -or
  $teamRoleRows -match '\[ \]' -or
  $taskDriLines -match 'ROLE_PLACEHOLDER' -or
  $startRoleRows -match 'ROLE_PLACEHOLDER' -or
  $currentBranch -ne 'tl/g0-operations' -or
  -not $baselineIsAncestor
) { throw "Named role assignment is incomplete." }
git status --short
```

- **Pre-review PASS threshold:** the assignment check does not throw; every role has one
  unique name; every prompt acknowledgement is checked; every non-roster
  unknown is `NONE` or a dated `BLOCKED` item; both banners say review is
  pending; the current branch is `tl/g0-operations`; the recorded baseline SHA
  exists and is an ancestor of current `HEAD`; APP then records `PASS` or
  `CHANGES_REQUESTED`.
- **Required edge check:** if no Snapdragon device or Korean reviewer exists,
  the fallback, decision owner and decision date are explicit.
- **Repository check:** no unrelated/user file is overwritten.

### Post-PASS closure command — TL runs this after APP records `PASS`

```powershell
$factsReady = Select-String `
  -Path docs/team/TEAM_FACTS.md `
  -Pattern '^> \*\*Status:\*\* READY — GATE 0 FACTS REVIEWED'
$startReady = Select-String `
  -Path docs/team/TEAM_START_HERE.md `
  -Pattern '^> \*\*Current onboarding status:\*\* \*\*READY — GATE 0 PASS'
$tlBoardDone = Select-String `
  -Path docs/team/TEAM_START_HERE.md `
  -Pattern '^\| \*\*TL\*\* \|.*DONE'
if (
  $factsReady.Count -ne 1 -or
  $startReady.Count -ne 1 -or
  $tlBoardDone.Count -ne 1
) { throw "Gate 0 closure state is not synchronized." }
```

- **Closure PASS threshold:** both banners are `READY`, the TL board row is
  `DONE`, and the APP review record remains `PASS`.

## Evidence

- Fact and acknowledgement record: `docs/team/TEAM_FACTS.md`
- Assignment board: `docs/team/TEAM_START_HERE.md`
- Reviewer result: this card's `Review record` section.

## Dependencies

- Each member → name/availability/acknowledgement → TL by 28/07 12:00.
- APP → reviewer/privacy/device coordination facts → TL by 28/07 17:30.
- TL → reviewed initial baseline commit on `main` → team by 28/07 11:30.
- TL → `tl/g0-operations` branch plus exact review commit SHA → APP by
  29/07 10:00.
- TL → unresolved organizer questions sent and dated → 29/07 09:00.
- APP → independent card review → 29/07 12:00.

## Escalate when

- Any member has no role or cannot meet their current deadline.
- Baseline PC/device, Korean reviewer or consent remains unknown after its
  checkpoint.
- Organizer constraints remain unanswered and would change the package.

## Handoff

TL first hands APP the exact `tl/g0-operations` review commit. After APP records
`PASS`, TL updates this card,
`docs/team/TEAM_FACTS.md` and the `docs/team/TEAM_START_HERE.md` banner/board
row atomically; records Gate 0 status in `docs/execution_backlog.md`; and
tells each named DRI to acknowledge their single active card by 29/07 13:00.

## Review record

- **APP result:** PENDING
- **Reviewed branch / commit SHA:** PENDING
- **Reviewed command/evidence:** PENDING
- **Recorded by / at:** PENDING
