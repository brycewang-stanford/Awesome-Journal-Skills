# IPSN Resources

Action-oriented resources for the IPSN skill pack. The `skills/` give advice; this directory lets
an agent model an IPSN-shaped paper, benchmark against verified exemplars, and prepare a
hardware-aware replication package for the double-blind, CPS-IoT Week process — while staying honest
that IPSN now submits through the merged **SenSys (Embedded AI and Sensing Systems)**.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for a TinyML-on-a-microcontroller sensing paper. Illustrative fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, verified IPSN papers across the IP track, the SPOTS track, and real deployments, and avoid sibling-venue confusion with SenSys, MobiCom, and NSDI. |
| [`official-source-map.md`](official-source-map.md) | Confirm the IPSN-lineage facts (IP/SPOTS tracks, 12-page double-blind ACM format, awards) and the SenSys merger before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open the historical IPSN surfaces and the live successor SenSys / CPS-IoT Week pages, plus cross-check sources for when the gateway blocks a direct fetch. |
| [`code/README.md`](code/README.md) | Use the shared replication-package tooling, plus the IPSN-specific hardware/firmware/deployment checks the generic kit cannot make. |

## Scope Note

This is a **sensor-networks / cyber-physical / embedded-ML** pack. Its papers are physical-system
papers: real testbeds and deployments, ground-truth instrumentation, energy/latency/accuracy
budgets, firmware, and estimation-theoretic reasoning carried through a **double-blind, HotCRP,
ACM-template** review inside CPS-IoT Week. Do **not** import the OpenReview/PMLR ML-conference
machinery or the econometrics (Stata/DiD/IV/RDD) kit used by other packs. And do not treat IPSN as a
still-running standalone venue: route the actual submission to the successor SenSys.

## Suggested Workflow

1. Route and frame with
   [`../skills/ipsn-topic-selection`](../skills/ipsn-topic-selection/SKILL.md) (IP vs SPOTS, and the
   merger routing) and [`../skills/ipsn-writing-style`](../skills/ipsn-writing-style/SKILL.md) —
   picking the track and the venue before writing is the highest-leverage move.
2. Build evidence with [`../skills/ipsn-experiments`](../skills/ipsn-experiments/SKILL.md),
   [`../skills/ipsn-reproducibility`](../skills/ipsn-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm the live successor
   cycle in [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) before the HotCRP audit in
   [`../skills/ipsn-submission`](../skills/ipsn-submission/SKILL.md).
