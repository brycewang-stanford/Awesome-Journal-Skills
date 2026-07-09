# WACV Resources

Action-oriented resources for the WACV skill pack. The `skills/` give advice; this
directory lets an agent model a WACV-style paper, benchmark against verified exemplars,
choose a track and a round, and prepare reproducibility artifacts without importing the
economics code kit.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for an applications-track WACV paper, framed for the two-round reviewer. Illustrative fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, metadata-verified WACV papers and avoid sibling-venue (CVPR/ICCV/ECCV) misattribution. |
| [`official-source-map.md`](official-source-map.md) | Confirm current-cycle WACV submission, two-round review, formatting, and publication sources — with the access-method disclosure and the explicit 待核实 list — before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open the official venue systems, both OpenReview round groups, CVF open access, and IEEE surfaces, and run the five author-side passes. |
| [`code/README.md`](code/README.md) | Use the shared ML-conference reproducibility kit: experiment matrix, artifact checklist, and a dependency-free smoke checker for anonymous reproduction packages. This is not the econometrics code kit. |

## Scope note

This is an applications-first computer-vision conference pack, not an empirical-economics
journal pack. Do not copy the Stata/DiD/IV/RDD econometrics kit here. Use the shared
ML-conference resource for experiment design, artifact packaging, seed/compute reporting,
and anonymous review-package checks.

## Suggested workflow

1. Route and frame with
   [`../skills/wacv-topic-selection`](../skills/wacv-topic-selection/SKILL.md) (WACV vs
   CVPR/ICCV/ECCV, and Applications vs Algorithms track) and
   [`../skills/wacv-writing-style`](../skills/wacv-writing-style/SKILL.md).
2. Stress-test evidence with [`../skills/wacv-experiments`](../skills/wacv-experiments/SKILL.md),
   [`../skills/wacv-reproducibility`](../skills/wacv-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md).
3. Plan the calendar with [`../skills/wacv-workflow`](../skills/wacv-workflow/SKILL.md) so
   the Round 1 / Round 2 decision is made before the first deadline, then benchmark
   against [`exemplars/library.md`](exemplars/library.md) and confirm current rules in
   [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md).
