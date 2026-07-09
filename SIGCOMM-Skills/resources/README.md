# SIGCOMM Resources

Action-oriented resources for the SIGCOMM skill pack. The `skills/` give advice; this directory lets an
agent model a SIGCOMM-style networking paper, benchmark against venue-verified exemplars, and prepare
reproducibility artifacts without importing the economics code kit.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for a networking-systems paper built on measured evidence. Illustrative fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, venue-verified SIGCOMM papers and avoid networking-sibling confusion (NSDI, MobiCom, CoNEXT, IMC). |
| [`official-source-map.md`](official-source-map.md) | Confirm current-cycle SIGCOMM submission, review, formatting, artifact, and camera-ready sources before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open official venue systems, HotCRP, TAPS, artifact, and award links, with the author-side verification passes. |
| [`code/README.md`](code/README.md) | Use the shared systems/ML reproducibility kit: experiment matrix, artifact checklist, and a dependency-free smoke checker for anonymous evaluation packages. This is not the econometrics code kit. |

## Scope Note

This is a networking-systems conference pack, not an empirical-economics journal pack. Do not copy the
Stata/DiD/IV/RDD econometrics kit here. Use the shared resource for testbed experiment design, artifact
packaging, trace and topology provenance, and anonymous double-blind package checks.

## Suggested Workflow

1. Route and frame with
   [`../skills/sigcomm-topic-selection`](../skills/sigcomm-topic-selection/SKILL.md) and
   [`../skills/sigcomm-writing-style`](../skills/sigcomm-writing-style/SKILL.md).
2. Stress-test evidence with [`../skills/sigcomm-experiments`](../skills/sigcomm-experiments/SKILL.md),
   [`../skills/sigcomm-reproducibility`](../skills/sigcomm-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm current official rules
   in [`official-source-map.md`](official-source-map.md) and [`external_tools.md`](external_tools.md).
