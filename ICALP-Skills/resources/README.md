# ICALP Resources

Action-oriented resources for the ICALP skill pack. The `skills/` give advice; this directory lets
an agent model an ICALP-shaped theory paper, benchmark against verified exemplars, and prepare the
full-version / proof-rigor package that stands in for an "artifact" at a pure-theory, LIPIcs
open-access venue.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for a theory paper, stating the model, the theorem, and the improvement up front. Illustrative fictional result; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, web-verified ICALP papers across Track A and Track B contribution shapes, and avoid confusing ICALP with STOC/FOCS/SODA. |
| [`official-source-map.md`](official-source-map.md) | Confirm the current-cycle ICALP deadline, page format, track split, review model, LIPIcs publication, and awards before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open the official ICALP, EATCS, HotCRP, and LIPIcs/DROPS surfaces, plus the cross-check sources for when the gateway blocks a direct fetch. |
| [`code/README.md`](code/README.md) | Use the shared submission-readiness tooling adapted to a *proof* paper: an anonymity/format check and a claim-to-proof map, since ICALP has no runnable-artifact track. |

## Scope Note

This is a **theoretical computer science** conference pack whose papers publish open-access in
**LIPIcs** (Dagstuhl), not an ML-conference or empirical-SE pack. Do not import the OpenReview/PMLR
machinery, the ACM/IEEE artifact-badge kit, or an econometrics kit. ICALP evidence is a **theorem and
its proof**: a clean model, a precise statement, and a complete, checkable argument (in the body plus
a labelled appendix / full version), read under lightweight double-blind review with a Track B
rebuttal.

## Suggested Workflow

1. Route and frame with
   [`../skills/icalp-topic-selection`](../skills/icalp-topic-selection/SKILL.md) (Track A vs Track B
   vs STOC/FOCS/SODA or a journal) and
   [`../skills/icalp-writing-style`](../skills/icalp-writing-style/SKILL.md) — the theorem and its
   place in the literature decided before drafting is the highest-leverage move.
2. Build the argument with [`../skills/icalp-experiments`](../skills/icalp-experiments/SKILL.md)
   (proof strategy and, where relevant, supporting computation),
   [`../skills/icalp-reproducibility`](../skills/icalp-reproducibility/SKILL.md) (proof
   verifiability / optional formalization), and [`code/README.md`](code/README.md).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm the live cycle in
   [`official-source-map.md`](official-source-map.md) and [`external_tools.md`](external_tools.md)
   before the HotCRP audit in
   [`../skills/icalp-submission`](../skills/icalp-submission/SKILL.md).
