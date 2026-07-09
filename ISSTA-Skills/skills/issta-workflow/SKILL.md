---
name: issta-workflow
description: Use when planning an ISSTA project timeline from venue fit through the January research-paper deadline, the March author response, the April first decision, the May Major-Revision sprint, the June final decision, artifact evaluation, and the October symposium, with backward-planning offsets for a testing/analysis tool paper and its artifact.
---

# ISSTA Workflow

Use this as the project-management skill for an ISSTA submission. Replace every date below with the
current official timetable and work backward from the HotCRP deadline — ISSTA's calendar, and even
its number of deadlines, changes between editions.

ISSTA is a conference, not a journal: it has no standing editor-in-chief and no article-processing
charge. The rotating leadership is the per-edition General Chair and Program Chairs, appointed by
ACM SIGSOFT and turning over each year, and the cost model is registration, not APCs — proceedings
appear in the ACM Digital Library. Re-check the current organization page rather than carrying a
name forward.

## Milestones (2026 shape — verify the current cycle)

- **Venue fit:** confirm the contribution is genuinely testing-and-analysis, not a broader SE result.
- **Evidence lock:** freeze the technique's scope, the subjects and benchmark versions, the
  baselines, and the artifact plan.
- **Submission deadline (Jan 29, 2026):** HotCRP record complete, 18-page anonymous `sigconf` PDF
  uploaded, subjects pinned.
- **Author response (Mar 24-26, 2026):** rebuttal anchored in submitted evidence.
- **First decision (Apr 16, 2026):** Accept, Major Revision, or Reject.
- **Major-Revision deadline (May 21, 2026):** revised paper plus a ledger walking every reviewer
  comment.
- **Final decision (Jun 25, 2026):** terminal outcome for revised papers.
- **Artifact evaluation:** package for the ACM badges and the Zenodo deposit (separate track/dates).
- **Camera-ready and symposium (Oakland, Oct 3-9, 2026):** ACM DL package, registration, in-person
  presentation.

## Backward plan from the paper deadline

| Weeks out (heuristic) | Testing/analysis milestone |
|---|---|
| 10+ | Technique implemented; scope and threat model fixed |
| 8 | Subjects and benchmark versions pinned; baselines configured at equal budget |
| 6 | Full evaluation runs complete with repeated runs and seeds logged |
| 4 | Statistics done (non-parametric test + effect size); tables generated from logs |
| 3 | Draft in ACM `sigconf`; threats-to-validity section written, not stubbed |
| 2 | Internal mock review by a testing-literate reader; artifact smoke-tested |
| 1 | Anonymity sweep; HotCRP record; artifact staging anonymized |
| 0 | 18-page PDF on HotCRP; confirm the abstract matches |

These offsets are planning heuristics only — anchor each to the current official timetable, never to
a previous cycle's calendar or deadline count.

## Failure modes by stage

- Treating Major Revision as a soft reject: teams that coast after April lose the June decision they
  could have won by walking the reviewers' ledger.
- Deferring the artifact to after acceptance: the badge and Zenodo work is real engineering, and a
  tool that only ran on the authors' cluster earns nothing.
- Leaving `sigconf` reflow to the final week: two-column code listings and full-width tables overflow
  late.
- Picking private subjects over an established benchmark: an evaluation that cannot be compared to
  prior work invites an external-validity reject that no rebuttal fixes.

## Coordination notes

- Assign one owner for the artifact and Zenodo deposit and another for the anonymity sweep; shared
  ownership is how both slip.
- Archive the exact submitted PDF and artifact, because response and Major-Revision replies must
  quote them precisely.

## Output format

```text
[Current stage] idea / evaluation / writing / submission / response / major-revision / accepted
[Next official deadline] <date and source, or unknown>
[Critical path] <three tasks that determine readiness>
[Risk register] <page/anonymity/evaluation/baseline/artifact/presentation>
[Owner map] <task -> person or role>
```
