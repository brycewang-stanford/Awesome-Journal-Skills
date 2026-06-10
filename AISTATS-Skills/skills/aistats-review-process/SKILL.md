---
name: aistats-review-process
description: Use when explaining or planning around AISTATS peer review, OpenReview review release, author-reviewer discussion, reviewer volunteer expectations, reviewer confidentiality, decision criteria, meta-review dynamics, the statistician-heavy reviewer pool, and PMLR proceedings outcomes.
---

# AISTATS Review Process

Use this to reason about review-stage strategy. Reopen the current CFP, OpenReview group,
author instructions, reviewer instructions if posted, and code of conduct before making
process claims.

## Process model

- AISTATS uses OpenReview for submission and review workflow in recent cycles.
- Reviewers evaluate technical correctness, statistical and machine-learning contribution,
  empirical support, clarity, reproducibility, and relevance to artificial intelligence and
  statistics.
- Author discussion is limited. AISTATS 2026 used a discussion period after initial reviews,
  with text-only author-reviewer discussion and no links.
- Reviewer and author obligations include confidentiality, appropriate conflicts,
  professional conduct, and respect for anonymity.
- The most useful response is a decision-focused clarification that gives the area chair or
  meta-reviewer a clean rationale for acceptance or rejection.
- Accepted papers are published in PMLR, so final metadata and camera-ready compliance matter
  as much as the initial acceptance.

## Who reviews here

- The pool mixes ML researchers with statisticians and statistical learning theorists;
  expect at least one reviewer to read proofs and assumption sets line by line.
- Because AISTATS is smaller and more specialized than NeurIPS or ICML, topical matches are
  closer, so vague proof sketches get caught rather than skimmed past.
- Borderline theory-plus-experiments papers usually fall on one of three edges: an assumption
  the experiments do not satisfy, a missing classical-statistics baseline, or a rate claim
  never checked empirically.

## Scoring leverage table

| Review dimension | What raises it | What sinks it |
|---|---|---|
| Correctness | Complete assumption statements with a main-text proof sketch | Hidden conditions; constants swept into O-notation when they matter |
| Significance | A guarantee the ML literature lacked, or a practical method statistics lacked | Incremental rate gain with no conceptual or practical payoff |
| Empirical support | Experiments engineered to probe the theory | Benchmarks disconnected from the theorem regimes |
| Clarity | Numbered assumptions and a single notation source | Notation collisions between sections |

## Stage-by-stage realism

- Initial reviews: triage by what the meta-reviewer would weigh, not by reviewer tone.
- Discussion: windows are short; an early, precise reply is worth more than a late
  comprehensive one.
- Decision: the meta-review synthesizes; one unanswered correctness objection outweighs
  several resolved clarity complaints.
- Reviewer-volunteer expectations for submitting authors have appeared in recent cycles;
  confirm the current CFP rather than assuming either way.

## Output format

```text
[Current stage] submitted / reviews / discussion / decision / camera-ready
[Decision actors] <reviewers/meta-reviewer/chairs>
[Likely leverage] <correctness/statistics/experiments/clarity/reproducibility>
[Forbidden moves] <identity leak / external links if forbidden / new unsupported results>
[Next response move] <one action>
```
