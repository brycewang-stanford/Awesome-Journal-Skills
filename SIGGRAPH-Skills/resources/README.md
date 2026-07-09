# SIGGRAPH Resources

Action-oriented resources for the SIGGRAPH skill pack. The `skills/` give advice; this directory
lets an agent model a SIGGRAPH-shaped paper, benchmark against verified exemplars, and prepare a
runnable, video-backed supplemental package for the ACM TOG journal-integrated, dual-track review.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after teaser + abstract + introduction rewrite for a computer-graphics paper. Illustrative fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, verified SIGGRAPH papers across contribution shapes, and avoid sibling-venue confusion with Eurographics/EGSR, SGP, SCA, UIST, and CVPR/ICCV. |
| [`official-source-map.md`](official-source-map.md) | Confirm the current-cycle SIGGRAPH / SIGGRAPH Asia deadline, page budget, review model, dual-track outcome, ACM TOG publication, and replicability culture before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open the official SIGGRAPH, SIGGRAPH Asia, TOG, Linklings, and replicability-stamp surfaces, plus the cross-check sources for when the gateway blocks a direct fetch. |
| [`code/README.md`](code/README.md) | Use the shared reproducibility tooling: a layout smoke checker, plus the SIGGRAPH-specific checks (results video, deterministic regeneration, asset shipping, timings) the generic kit cannot make. |

## Scope Note

This is a computer-graphics conference pack whose papers publish in a **journal** (ACM Transactions
on Graphics), not an ML-conference or economics pack. Do not import the OpenReview/PMLR machinery or
the Stata/DiD/IV econometrics kit. SIGGRAPH evidence is **shown graphics evidence**: a teaser and a
results video, head-to-head comparisons against the strongest prior method, quality metrics and
timings on stated hardware, carried through a single-round review with a short rebuttal, a Technical
Papers Committee meeting, and a conditional-accept second stage.

## Suggested Workflow

1. Route and frame with
   [`../skills/siggraph-topic-selection`](../skills/siggraph-topic-selection/SKILL.md) and
   [`../skills/siggraph-writing-style`](../skills/siggraph-writing-style/SKILL.md) — deciding
   SIGGRAPH vs SIGGRAPH Asia vs a sibling venue, and the dual-track vs Journal-only choice, before
   writing is the highest-leverage move.
2. Build evidence with [`../skills/siggraph-experiments`](../skills/siggraph-experiments/SKILL.md),
   [`../skills/siggraph-supplementary`](../skills/siggraph-supplementary/SKILL.md), and
   [`../skills/siggraph-reproducibility`](../skills/siggraph-reproducibility/SKILL.md).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm the live cycle in
   [`official-source-map.md`](official-source-map.md) and [`external_tools.md`](external_tools.md)
   before the Linklings audit in
   [`../skills/siggraph-submission`](../skills/siggraph-submission/SKILL.md).
