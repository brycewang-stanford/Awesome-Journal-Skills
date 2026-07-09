# ICDM Resources

Action-oriented resources for the ICDM skill pack. The `skills/` give strategy; this directory
lets an agent model an ICDM-style data-mining paper, benchmark against award-verified exemplars,
and prepare reproducibility evidence inside the right track's anonymity regime — without importing
any econometrics kit.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite into the ICDM first-page arc for a data-mining methods paper. Illustrative fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real ICDM papers verified through the IEEE ICDM 10-Year Highest-Impact Award roster, and avoid KDD/CIKM/WSDM/SDM misattribution. |
| [`official-source-map.md`](official-source-map.md) | Confirm current-edition ICDM track calls, review model, format, and policy sources before giving submission-ready advice. Includes the access-method note and the 待核实 register. |
| [`external_tools.md`](external_tools.md) | Open official track calls, IEEE Xplore proceedings, the awards site, and dblp. |
| [`code/README.md`](code/README.md) | Use the shared ML-conference reproducibility kit: experiment matrix, artifact checklist, and a dependency-free smoke checker for anonymous reproduction packages. This is not an econometrics kit. |

## Scope note

This is an IEEE data-mining conference pack, not an empirical-economics journal pack. Do not copy
any Stata/DiD/IV/RDD econometrics kit here. Use the shared ML-conference resource for experiment
design, artifact packaging, seed/compute reporting, and — critically at ICDM — for keeping the
reproduction package **triple-blind for the Research Track** (single-blind for the Applied Track).

## Suggested workflow

1. Route with [`../skills/icdm-topic-selection`](../skills/icdm-topic-selection/SKILL.md) (venue
   fit and the Research-vs-Applied-vs-Blue-Sky track fork), then frame with
   [`../skills/icdm-writing-style`](../skills/icdm-writing-style/SKILL.md).
2. Stress-test evidence with [`../skills/icdm-experiments`](../skills/icdm-experiments/SKILL.md),
   [`../skills/icdm-reproducibility`](../skills/icdm-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md), keeping every artifact inside the track's anonymity regime.
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm current official
   rules in [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) before the June deadline.
