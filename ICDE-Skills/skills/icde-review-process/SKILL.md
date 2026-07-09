---
name: icde-review-process
description: Use when explaining or planning around IEEE ICDE peer review: the two-round-per-edition structure, area-chair-coordinated assignment with at least three reviewers, two-phase reviewing with a possible Revise & Resubmit, single-blind dynamics, how a builder-heavy committee reads a systems paper, and how outcomes feed IEEE Xplore.
---

# ICDE Review Process

Use this to reason about review-stage strategy. Reopen the current call, important-dates page,
and any reviewer instructions before making process claims; ICDE re-declares its review model
each edition.

## Process model

- ICDE takes research papers in **two rounds per edition** (ICDE 2027: ≈June and November).
  Each paper draws **at least three reviewers**, coordinated by an **area chair** who
  synthesizes the reviews into a recommendation.
- The ICDE 2026 model ran **two reviewing phases** inside a round: the first phase returned
  **Revise & Resubmit, Accept, or Reject**; invited revisions were re-reviewed (≈4-week window)
  before a final **Accept/Reject**. Whether the current edition keeps the R&R phase is
  edition-specific (待核实).
- Review is **single-blind**: reviewers see author identity; authors do not see reviewers. This
  changes the calculus — reputational priors exist, so the paper must earn belief on evidence,
  not on names.
- A **Round 1 reject is terminal for the edition**; the paper cannot re-enter Round 2. That
  raises the stakes on getting the evaluation right the first time.
- Accepted papers publish in **IEEE Xplore**; camera-ready compliance and IEEE metadata matter
  as much as the acceptance itself.

## Who reviews here

- The committee is **builder-heavy**: reviewers who have implemented indexes, optimizers, and
  storage engines. They read an evaluation the way an engineer reads a benchmark — skeptical of
  untuned baselines, single-point results, and hidden costs.
- Because scope overlaps SIGMOD and VLDB, at least one reviewer will likely know the nearest
  prior system intimately; a novelty claim that ignores it is caught, not skimmed past.
- Borderline systems papers usually fail on one of three edges: an untuned or unfair baseline, a
  performance claim with no operating point, or a mechanism whose benefit is never isolated by
  an ablation.

## Scoring leverage table

| Review dimension | What raises it | What sinks it |
|---|---|---|
| Novelty | A named mechanism a builder could not have trivially derived | "Yet another index" with no isolable new idea |
| Evaluation | Tuned baselines, scale curves, variance, disclosed cost | Single-point wins on one synthetic workload |
| Soundness | Ablations that isolate the mechanism's contribution | Gains that could come from unrelated engineering |
| Reproducibility | Runnable supplement whose availability is evident | Empty or unrunnable supplemental material |
| Significance | A primitive an ecosystem can adopt | A narrow tweak with no downstream reach |

## Stage-by-stage realism

- **Phase 1 reviews:** read them as the area chair will — is the central evaluation objection
  answerable? A Revise & Resubmit is an opportunity, not a soft reject; treat the requirement
  list as binding.
- **Revision re-review:** the same reviewers check the list; unrequested scope changes hurt.
- **Decision:** one unresolved fairness or cost objection outweighs several resolved clarity
  nits, because a builder-heavy committee anchors on the evaluation.
- **Round choice as strategy:** since Round 1 rejects skip the edition, aiming an immature
  evaluation at the earlier round is a common self-inflicted loss.

## Output format

```text
[Current stage] submitted / phase-1 reviews / revision / decision / camera-ready
[Round] Round 1 or Round 2 (edition)
[Decision actors] <reviewers / area chair / program chairs>
[Likely leverage] <novelty / evaluation / soundness / reproducibility>
[Central objection] <the one thing the area chair will weigh most>
[Next response move] <one action>
```
