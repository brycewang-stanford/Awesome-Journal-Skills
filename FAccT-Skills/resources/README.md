# ACM FAccT Resources

Action-oriented resources for the FAccT skill pack. The `skills/` give advice; this directory lets
an agent model a FAccT-shaped paper, benchmark against verified exemplars, and prepare the
accountability documentation and released artifacts for the mutually-anonymous, interdisciplinary,
revise-and-resubmit process.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for an interdisciplinary responsible-AI paper. Illustrative fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, verified FAccT/FAT* papers across contribution shapes, and avoid confusing FAccT with a pure-ML, HCI, or law venue. |
| [`official-source-map.md`](official-source-map.md) | Confirm the current-cycle FAccT deadlines, page budget, mutually-anonymous review, Accept/Revise/Reject cycle, endmatter statements, and archival policy before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open the official FAccT, OpenReview, ACM DL, and CRAFT surfaces, plus the cross-check sources for when the gateway blocks a direct fetch. |
| [`code/README.md`](code/README.md) | Use the shared replication-package tooling and the FAccT-specific documentation checks (datasheets, model cards, disaggregation, consent) the generic kit cannot make. |

## Scope Note

This is an **interdisciplinary responsible-AI conference** pack, not a pure-ML, HCI, or
software-engineering pack. FAccT publishes archival ACM proceedings, but its distinguishing demand
is that **fairness, accountability, or transparency is a first-class contribution**, evaluated to
the rigor of whichever discipline the paper sits in — statistical care and disaggregation for an
audit, coding and reflexivity for a qualitative study, doctrinal precision for a legal paper. Do
**not** import an ML-leaderboard framing or a SIGSOFT artifact-badging checklist: FAccT's artifact
culture is documentation (datasheets, model cards, impact assessments) and honest data/code release,
carried through a mutually-anonymous, revise-and-resubmit review by a mixed reviewer pool.

## Suggested Workflow

1. Route and frame with
   [`../skills/facct-topic-selection`](../skills/facct-topic-selection/SKILL.md) and
   [`../skills/facct-writing-style`](../skills/facct-writing-style/SKILL.md) — deciding FAccT vs. a
   pure-ML/HCI/law venue, and making the contribution legible to a mixed panel, is the
   highest-leverage move.
2. Build evidence with [`../skills/facct-experiments`](../skills/facct-experiments/SKILL.md),
   [`../skills/facct-reproducibility`](../skills/facct-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm the live cycle in
   [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) before the OpenReview audit in
   [`../skills/facct-submission`](../skills/facct-submission/SKILL.md).
