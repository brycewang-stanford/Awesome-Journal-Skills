---
name: issta-review-process
description: Use when explaining or planning around ISSTA peer review, covering double-anonymous reviewing, at least three PC reviews, the Accept/Major-Revision/Reject outcome model, the phase-two major-revision resubmission, the named evaluation criteria, how the decision is actually synthesized, and how earlier editions ran multiple rolling deadlines.
---

# ISSTA Review Process

Use this to reason about review-stage strategy. ISSTA review is double-anonymous and its outcome
model is richer than accept/reject, so plan around the Major-Revision path from the start. Reopen
the current call and dates page before making process claims — the number of deadlines and the exact
mechanics change between editions.

## Process model

- Reviewing is double-anonymous: reviewers do not see author identities and authors do not see
  reviewer identities.
- Each paper receives at least three PC reviews; chairs solicit more when expertise is thin or
  reviewers disagree sharply.
- First-round outcomes are **Accept**, **Major Revision**, or **Reject**. A Major-Revision paper
  revises against a fixed later deadline and receives a terminal decision — it is a real second
  chance, not a soft reject, and reviewers expect the revision to address their points concretely.
- Earlier editions (e.g. ISSTA 2023, 2024) ran **two rolling submission deadlines**, where a
  first-deadline paper could be sent a major revision to the second deadline while second-deadline
  papers got only accept/reject. The multi-round model is genuine ISSTA history; its exact shape is
  cycle-specific, so confirm the current one.
- Accepted papers are published in the ACM Digital Library, so final metadata and camera-ready
  compliance matter alongside the initial decision.

## The named evaluation criteria

| Criterion | What raises it | What sinks it |
|---|---|---|
| Originality | A technique or question the field did not have | A re-parameterized variant of existing work |
| Importance of contribution | A result the testing/analysis community will reuse | A narrow gain with no reuse story |
| Soundness | Claims scoped to what is actually shown | Overclaimed scope; unstated assumptions |
| Evaluation | Real subjects, fair baselines, proper statistics | Toy subjects, mis-configured baselines, single runs |
| Presentation | A clear threat model and evaluation contract | Undefined scope; results without protocol |
| Comparison to related work | Delta stated against the nearest techniques | Missing the closest competitor |
| Verifiability / transparency | Pinned subjects and a runnable artifact | Unshared subjects, unregenerable tables |

The last two — comparison and verifiability — are where testing/analysis papers most often lose
avoidable ground, because the nearest baseline and the shared artifact are both checkable.

## Who reviews here

- The PC is specialized in testing and analysis, so a reviewer will know the closest tool, the
  standard benchmark, and the usual statistical protocol. Vague baselines and hand-picked subjects
  get caught rather than skimmed past.
- Borderline papers usually fall on one of three edges: an evaluation that does not use an
  established benchmark, a baseline configured to lose, or a claim broader than the subjects tested.

## Stage-by-stage realism

- Initial reviews: read for the criteria the meta-reviewer will weigh, not for reviewer tone.
- Response / discussion: address the decision-critical objection first; an early precise reply beats
  a late comprehensive one.
- Major Revision: treat every comment as a tracked change and walk the ledger in the resubmission;
  reviewers who see their points addressed in order revise upward.
- Decision: the meta-review synthesizes; one unresolved soundness or evaluation objection outweighs
  several resolved presentation complaints.

## Output format

```text
[Current stage] submitted / reviews / response / major-revision / decision / camera-ready
[Outcome model] accept / major-revision / reject
[Decision actors] <reviewers / meta-reviewer / chairs>
[Likely leverage] <soundness / evaluation / comparison / verifiability>
[Forbidden moves] <identity leak / unpromised new results in the box>
[Next response move] <one action>
```
