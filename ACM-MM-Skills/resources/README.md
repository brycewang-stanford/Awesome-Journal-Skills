# ACM MM Resources

Action-oriented resources for the ACM MM skill pack. The `skills/` carry the advice; this
directory lets an agent model an ACM MM-style multimedia paper, benchmark against verified
exemplars from the ACM Digital Library, and prepare artifact/badging material without
importing an unrelated methods kit.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for a cross-modal ACM MM paper. Illustrative fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, metadata-verified ACM MM papers and avoid sibling-venue confusion (ICMR, MMSys, CVPR, TOMM). |
| [`official-source-map.md`](official-source-map.md) | Confirm current-cycle ACM MM submission, review, formatting, track, and badging sources before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open the official site, OpenReview groups, ACM DL, dblp, and SIGMM pages, and run the author-side verification passes. |
| [`code/README.md`](code/README.md) | Use the shared ML-conference reproducibility kit — experiment matrix, artifact checklist, and a dependency-free smoke checker — for ACM MM's anonymous review packages and Reproducibility-track artifacts. |

## Scope note

This is a multimedia conference pack, not a single-modality vision pack and not an
empirical-economics journal pack. Do not import a CVPR/ICCV computer-vision kit or a
Stata/DiD/IV/RDD econometrics kit here. ACM MM evidence spans several media at once, so the
shared ML-conference resource is used for experiment design, media-artifact packaging,
seed/compute reporting, and anonymous-review media checks — with the ACM MM-specific
overlays (thematic area, sigconf budget, badging) coming from the skills.

## Suggested workflow

1. Route and frame with
   [`../skills/acmmm-topic-selection`](../skills/acmmm-topic-selection/SKILL.md) and
   [`../skills/acmmm-writing-style`](../skills/acmmm-writing-style/SKILL.md) — decide it is
   truly multimedia and pick the thematic area before drafting.
2. Stress-test evidence with
   [`../skills/acmmm-experiments`](../skills/acmmm-experiments/SKILL.md),
   [`../skills/acmmm-reproducibility`](../skills/acmmm-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm current
   official rules in [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) before any deadline-sensitive claim.
