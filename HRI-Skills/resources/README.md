# HRI Resources

Action-oriented resources for the HRI skill pack. The `skills/` give advice; this directory lets
an agent model an HRI-shaped paper, benchmark against verified exemplars, and prepare the study
materials and video that a double-blind, two-phase HRI review expects.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for a human-subjects human-robot-interaction study. Illustrative fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, verified HRI *conference* papers across contribution shapes, and avoid confusing the venue with CHI, ICRA/IROS, or the THRI/JHRI journals. |
| [`official-source-map.md`](official-source-map.md) | Confirm the current-cycle HRI deadlines, five-track model, 8-page budget, two-phase review, and human-subjects policy before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open the official HRI, PCS, ACM DL, and IEEE Xplore surfaces, plus the cross-check sources for when the gateway blocks a direct fetch. |
| [`code/README.md`](code/README.md) | Use the shared study-materials/replication tooling: a claim-to-measure matrix, an openness checklist, and a smoke checker adapted to embodied human-subjects artifacts. |

## Scope Note

This is an **interdisciplinary human-robot-interaction** conference pack whose core evidence is a
**human-subjects study of an embodied robot**, published across the ACM DL and IEEE Xplore. It is
not an ML-conference pack (no OpenReview/PMLR leaderboard machinery) and not a pure-robotics
systems pack (no benchmark-only framing). HRI evidence is: a defensible study design (between/
within-subjects, honest Wizard-of-Oz), statistics *with effect sizes*, qualitative rigor where the
question is qualitative, validated scales, and a **video** that lets a reviewer see the interaction
— all carried through a double-blind review with a real rebuttal.

## Suggested Workflow

1. Route and frame with
   [`../skills/hri-topic-selection`](../skills/hri-topic-selection/SKILL.md) (HRI vs. CHI/ICRA/
   RO-MAN, and which of the five tracks) and
   [`../skills/hri-writing-style`](../skills/hri-writing-style/SKILL.md) — choosing the venue and
   track before designing the study is the highest-leverage move.
2. Build the study with [`../skills/hri-experiments`](../skills/hri-experiments/SKILL.md),
   [`../skills/hri-reproducibility`](../skills/hri-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md); plan the video with
   [`../skills/hri-supplementary`](../skills/hri-supplementary/SKILL.md).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm the live cycle in
   [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) before the PCS audit in
   [`../skills/hri-submission`](../skills/hri-submission/SKILL.md).
