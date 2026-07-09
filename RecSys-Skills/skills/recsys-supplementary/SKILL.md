---
name: recsys-supplementary
description: Use when organizing ACM RecSys supporting material under the venue's no-separate-supplement convention — how to split a recommender paper between the body, the appendix that counts inside the page budget, and the anonymous in-paper repository, so tuning grids, extra datasets, and ablations land where reviewers use them.
---

# RecSys Supplementary

Use this when deciding where each piece of supporting material goes. RecSys is unusual: it does
**not** invite a separate anonymous supplement file the way OpenReview venues do. Instead the
appendix **counts inside** the content-page budget, and executable or bulky material lives in the
**anonymous repository** linked from the paper. That constraint drives every placement decision.

## The three-bucket decision

| Bucket | What belongs here | Constraint |
|---|---|---|
| Main body (8 / 4 pages) | The recommendation claim, method, headline offline table, the offline-online bridge, key ablation | Must stand alone; a reviewer should grasp the contribution without the appendix |
| Appendix (inside the budget) | Proof of any bound, dataset details, tuning grids, extra ablations, per-dataset breakdowns | Every page here is a page not spent on the body — include only what changes belief |
| Anonymous repository | Code, configs, checkpoints, logged propensities, raw run outputs, seeds | Reviewers may not open it; nothing decision-critical can live only here |

The sharpest RecSys-specific edge: because the appendix eats your page budget, authors are tempted
to push essential evidence (like the equal-budget tuning grid) into the repository — but that is
exactly the evidence a skeptical reviewer wants to *see stated*, so summarize it in the appendix
and keep the full grid in the repository.

## What to keep in the body no matter what

- The method and its assumption (e.g., positivity for an off-policy estimator).
- The headline ranking table with tuned baselines and reported variance.
- The one ablation that isolates the mechanism.
- One sentence stating the split protocol and whether metrics are full-ranking.

## What gets read, and how carefully

| Item | Inspection likelihood | Practical implication |
|---|---|---|
| Headline offline table | High | Belongs in the body, not the appendix |
| Tuning grid summary | Medium-high | Summarize in the appendix; reviewers check for equal budget |
| Extra datasets / ablations | Medium | Reference each from the body or it is invisible |
| Code repository | Variable (reviewer discretion) | README must orient a reader in one minute |
| Raw run logs | Low | Repository only; never rely on them for a claim |

## Vignette: splitting an off-policy ranking paper

A submission proposing an exposure-corrected ranker: the body keeps the estimator, its positivity
assumption, the tuned headline table, and the simulator bridge figure; the appendix holds the
propensity-model details, the equal-budget tuning grid summary, and per-dataset breakdowns; the
repository carries the seeded runner, checkpoints, and logged propensities. Nothing decision-
critical lives only in the repository, because repository inspection is discretionary.

## Cross-reference discipline

```text
Body Table 1  --cites-->  App. B (tuning grid)  --mirrors-->  repo/configs/*.yaml
Body Fig. 1   --cites-->  App. C (simulator setup)  --mirrors-->  repo/sim/run.sh
```

Orphaned appendix material — a table no body sentence points to — wastes budget and is effectively
invisible under reviewer discretion.

## Output format

```text
[Placement status] Ready / Needs fixes / Not ready
[Body-only items] <method / assumption / headline table / key ablation / split statement>
[Appendix items] <proofs / tuning-grid summary / extra datasets — inside the budget>
[Repository items] <code / configs / checkpoints / propensities / logs>
[Main-paper dependency] <what breaks if the appendix or repo is ignored>
```
