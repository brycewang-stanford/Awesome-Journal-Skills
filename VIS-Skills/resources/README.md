# IEEE VIS Resources

Action-oriented resources for the IEEE VIS skill pack. The `skills/` give advice; this directory
lets an agent model a VIS-shaped paper, benchmark against verified exemplars, and prepare an
open-materials package for the two-phase, journal-integrated IEEE TVCG review.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for a visualization paper. Illustrative fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, verified IEEE VIS / TVCG papers across contribution types, and avoid sibling-venue confusion with EuroVis, CHI, and SIGGRAPH. |
| [`official-source-map.md`](official-source-map.md) | Confirm the current-cycle VIS deadlines, 9+2 page budget, two-phase review, area model, TVCG publication, and reproducibility program before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open the official VIS, PCS, VGTC-template, TVCG, and GRSI surfaces, plus the cross-check sources for when the gateway blocks a direct fetch. |
| [`code/README.md`](code/README.md) | Use the shared replication-package tooling: a figure-to-claim matrix, a Replicability-Stamp checklist, and a dependency-free smoke checker for a supplemental archive. |

## Scope Note

This is a **data-visualization** conference pack whose full papers publish in a **journal** (IEEE
TVCG), not an HCI-proceedings, vision, or economics pack. Do not import the `acmart`/CHI machinery,
the CVPR camera-ready model, or the Stata/DiD/IV econometrics kit. VIS evidence is
visualization evidence: task-justified encodings, perceptual and controlled studies with effect
sizes, design-study validation, benchmarks on realistic data, and a runnable supplemental archive
carried through a two-phase, conditional-accept review.

## Suggested Workflow

1. Route and frame with
   [`../skills/vis-topic-selection`](../skills/vis-topic-selection/SKILL.md) and
   [`../skills/vis-writing-style`](../skills/vis-writing-style/SKILL.md) — deciding VIS (and which of
   the six areas) versus EuroVis/CHI/SIGGRAPH before writing is the highest-leverage move.
2. Build evidence with [`../skills/vis-experiments`](../skills/vis-experiments/SKILL.md),
   [`../skills/vis-reproducibility`](../skills/vis-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm the live cycle in
   [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) before the PCS audit in
   [`../skills/vis-submission`](../skills/vis-submission/SKILL.md).
