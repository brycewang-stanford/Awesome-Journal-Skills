---
name: recsys-review-process
description: Use when explaining or planning around ACM RecSys peer review — the mutually-anonymous model with at least three PC members and a Senior PC overseer, the rebuttal phase, how the reproducibility-crisis culture shapes reviewer priorities, the offline-versus-online evaluation lens, and how acceptance leads to ACM Digital Library publication.
---

# RecSys Review Process

Use this to reason about review-stage strategy. Reopen the current Call for Contributions, the
committees page, and any reviewer guidelines before making process claims — mechanics are
cycle-specific.

## Process model

- RecSys review is **mutually anonymous** (double-blind). Each submission is read by **at least
  three PC members** and overseen by a **Senior PC member** who synthesizes the recommendation.
- There is an author **rebuttal** phase (2026: June 4-9) for a short clarifying narrative.
- Reviewers weigh recommendation novelty, evaluation validity, reproducibility, clarity, and
  relevance to the recommender community — not raw metric wins alone.
- The most useful reply is a decision-focused clarification that gives the Senior PC a clean
  rationale for acceptance or rejection.
- Accepted papers are published in the **ACM Digital Library**, so camera-ready compliance and
  metadata matter as much as the initial decision.

## Who reviews here, and what they distrust

- The pool is a **single-domain recommender community**: expect at least one reviewer who has
  internalized the field's reproducibility debate and will probe baseline tuning line by line.
- Because RecSys is topically tight, matches are close and an under-tuned comparison or a leaky
  split gets caught rather than skimmed past.
- Borderline offline-evaluation papers usually fall on one of three edges: baselines tuned less
  hard than the proposed method, a random split where a temporal one was needed, or an offline
  metric asserted to imply a deployment win with no bridge.

## Scoring leverage table

| Review dimension | What raises it | What sinks it |
|---|---|---|
| Recommendation novelty | A named user/item modeling or evaluation idea | An architecture swap with no recommendation-specific insight |
| Evaluation validity | Equal-budget baselines, temporal split, full-ranking metrics, variance | Untuned baselines, random split, sampled metrics reported as full |
| Deployment relevance | Off-policy estimate, simulator, or A/B result | "Offline nDCG rose, therefore users benefit" |
| Reproducibility | A runnable anonymous repository regenerating the tables | A promise to release code "upon acceptance" only |
| Clarity | One notation source, honest limitations | Buried assumptions; a random-split protocol left implicit |

## Stage-by-stage realism

- Initial reviews: triage by what the Senior PC would weigh, not by reviewer tone.
- Rebuttal: the window is short; an early, precise narrative on the central evaluation objection
  beats a late line-by-line reply (see `recsys-author-response`).
- Decision: the Senior PC synthesizes; one unresolved evaluation-validity objection outweighs
  several resolved clarity complaints.
- Post-decision: ACM Digital Library publication means the rights form and metadata become the
  final gate.

## Vignette: reading a split decision

Two reviewers like the method; one flags that baselines were tuned only on defaults. At RecSys
that single objection is decisive because it maps onto the community's reproducibility anxiety —
so the rebuttal must resolve *that* thread, with the equal-budget grid, before polishing anything
the other reviewers raised.

## Output format

```text
[Current stage] submitted / reviews / rebuttal / decision / camera-ready
[Decision actors] <PC reviewers / Senior PC>
[Likely leverage] <novelty / evaluation validity / deployment relevance / reproducibility / clarity>
[Forbidden moves] <identity leak / unseen new results / unsupported deployment claims>
[Next response move] <one action>
```
