# RecSys Resources

Action-oriented resources for the RecSys skill pack. The `skills/` give advice; this directory lets an
agent model a RecSys-style paper, benchmark against verified exemplars, and prepare reproducibility
artifacts without importing the economics code kit.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for a recommender-systems paper. Illustrative fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, verified RecSys papers and avoid sibling-venue confusion (SIGIR / KDD / WSDM / TheWebConf / UAI). |
| [`official-source-map.md`](official-source-map.md) | Confirm current-cycle RecSys submission, review, formatting, and policy sources before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open official venue systems, proceedings, and author-instruction links, plus RecSys-native reproduction frameworks. |
| [`code/README.md`](code/README.md) | Use the shared ML conference reproducibility kit: experiment matrix, artifact checklist, and a dependency-free smoke checker for anonymous reproduction packages. This is not the econometrics code kit. |

## Scope Note

This is a recommender-systems conference pack, not an empirical-economics journal pack. Do not copy the
Stata/DiD/IV/RDD econometrics kit here. Use the shared ML-conference resource for experiment design,
artifact packaging, seed/compute reporting, and anonymous review-package checks — adapted to RecSys's
top-N ranking, offline/online split, and off-policy evaluation concerns.

## Suggested Workflow

1. Route and frame with
   [`../skills/recsys-topic-selection`](../skills/recsys-topic-selection/SKILL.md) and
   [`../skills/recsys-writing-style`](../skills/recsys-writing-style/SKILL.md).
2. Stress-test evidence with [`../skills/recsys-experiments`](../skills/recsys-experiments/SKILL.md),
   [`../skills/recsys-reproducibility`](../skills/recsys-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm current official rules
   in [`official-source-map.md`](official-source-map.md) and [`external_tools.md`](external_tools.md).
