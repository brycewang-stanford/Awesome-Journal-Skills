---
name: issta-workflow
description: Use when planning an ISSTA project timeline from venue fit through the January abstract and research-paper deadlines, the March author response, the April first decision (including early reject), the May Major-Revision sprint, the June final decision, the July camera-ready, artifact evaluation, and the September symposium, with backward-planning offsets for a testing/analysis tool paper and its artifact.
---

# ISSTA Workflow

Use this as the project-management skill for an ISSTA submission. Replace every date below with the
current official timetable and work backward from the HotCRP deadline — ISSTA's calendar, and even
its number of deadlines, changes between editions.

ISSTA is a conference with a journal-style outlet: it has no standing editor-in-chief. The rotating
leadership is the per-edition General Chair and Program Co-Chairs, appointed by ACM SIGSOFT and
turning over each year (ISSTA 2027: General Chair Jun Sun; Program Co-Chairs Dan Hao and Jacques
Klein, verified 2026-11-24). Accepted papers appear open access in PACMSE (Issue ISSTA 2027) in
the ACM Digital Library; authors not covered by ACM OPEN may owe an APC (2027 amount to be
announced; 2026 was US$250 ACM members / US$350 non-members), on top of registration. Re-check
the current organization page rather than carrying a name forward.

## Milestones (ISSTA 2027 — verify the current cycle)

- **Venue fit:** confirm the contribution is genuinely testing-and-analysis, not a broader SE result.
- **Evidence lock:** freeze the technique's scope, the subjects and benchmark versions, the
  baselines, and the artifact plan.
- **Mandatory abstract (Jan 8, 2027):** HotCRP record with title, abstract, authors, conflicts,
  research area; author list and title frozen from here.
- **Submission deadline (Jan 11, 2027):** 18-page anonymous `acmsmall` PDF with the Data
  Availability section uploaded, subjects pinned.
- **Author response (Mar 22-25, 2027):** rebuttal anchored in submitted evidence.
- **First decision (Apr 20, 2027):** Accept, Major Revision, or Reject — including early rejection
  of papers whose first two reviews are both negative.
- **Major-Revision deadline (May 20, 2027):** revised paper plus a ledger walking every revision
  item (four weeks).
- **Final decision (Jun 17, 2027):** terminal outcome for revised papers.
- **Camera ready (Jul 22, 2027):** PACMSE package, rights and any APC step.
- **Artifact evaluation:** package for the ACM badges and a DOI-issuing deposit (separate
  track/dates; the 2027 AE call was not yet posted on 2026-11-24).
- **Symposium (Singapore, Sep 7-10, 2027):** registration and presentation.

## Backward plan from the paper deadline

| Weeks out (heuristic) | Testing/analysis milestone |
|---|---|
| 10+ | Technique implemented; scope and threat model fixed |
| 8 | Subjects and benchmark versions pinned; baselines configured at equal budget |
| 6 | Full evaluation runs complete with repeated runs and seeds logged |
| 4 | Statistics done (non-parametric test + effect size); tables generated from logs |
| 3 | Draft in ACM `acmsmall`; threats-to-validity and Data Availability sections written, not stubbed |
| 2 | Internal mock review by a testing-literate reader; artifact smoke-tested |
| 1 | Mandatory abstract on HotCRP; anonymity sweep; artifact staging anonymized |
| 0 | 18-page PDF on HotCRP; confirm the abstract matches |

These offsets are planning heuristics only — anchor each to the current official timetable, never to
a previous cycle's calendar or deadline count.

## Failure modes by stage

- Treating Major Revision as a soft reject: teams that coast after April lose the June decision they
  could have won by walking the reviewers' ledger.
- Deferring the artifact to after acceptance: one reviewer checks the review-time artifact, the
  badge and DOI-archive work is real engineering, and a tool that only ran on the authors' cluster
  earns nothing.
- Leaving the 18-page fit to the final week: single-column `acmsmall` pages hold less than they
  look, and wide result tables overflow late.
- Picking private subjects over an established benchmark: an evaluation that cannot be compared to
  prior work invites an external-validity reject that no rebuttal fixes.

## Coordination notes

- Assign one owner for the artifact and DOI-archived deposit and another for the anonymity sweep; shared
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
