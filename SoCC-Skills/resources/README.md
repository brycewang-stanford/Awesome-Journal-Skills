# ACM SoCC Resources

Action-oriented resources for the SoCC skill pack. The `skills/` give advice; this directory lets
an agent model a SoCC-shaped paper, benchmark against verified exemplars, and prepare a
reproducibility package for the two-round, dual-anonymous ACM Symposium on Cloud Computing.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for a cloud-systems paper that leads with the deployed-scale problem and the measured result. Illustrative fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, verified SoCC papers across contribution shapes (measurement, systems-building, storage QoS, resource management, serverless), and avoid sibling-venue confusion with OSDI, NSDI, EuroSys, and ATC. |
| [`official-source-map.md`](official-source-map.md) | Confirm the current-cycle SoCC round deadlines, page budget, dual-anonymous review, SIGMOD+SIGOPS sponsorship, and artifact policy before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open the official SoCC, HotCRP, ACM DL, and dblp surfaces, plus the cross-check mirrors for when the gateway blocks a direct fetch. |
| [`code/README.md`](code/README.md) | Use the shared reproducibility tooling: an evidence-to-claim matrix, an ACM-badge checklist, and a dependency-free smoke checker for a released cloud-systems artifact. |

## Scope Note

This is a **cloud-computing systems** conference pack whose home is the joint **SIGMOD+SIGOPS**
community — not a software-engineering, ML-conference, or economics pack. SoCC evidence is
systems-and-data evidence: real deployments or realistic testbeds, production or representative
workloads, throughput/latency/tail/cost measurements with honest baselines, and reproducible
measurement pipelines. Do not import the OpenReview/PMLR machinery, the empirical-SE
threats-to-validity template, or the Stata/DiD econometrics kit.

## Suggested Workflow

1. Route and frame with
   [`../skills/socc-topic-selection`](../skills/socc-topic-selection/SKILL.md) and
   [`../skills/socc-writing-style`](../skills/socc-writing-style/SKILL.md) — deciding SoCC vs.
   OSDI/NSDI/EuroSys/ATC (and vs. a data venue like VLDB/SIGMOD) before writing is the
   highest-leverage move.
2. Build evidence with [`../skills/socc-experiments`](../skills/socc-experiments/SKILL.md),
   [`../skills/socc-reproducibility`](../skills/socc-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm the live round
   in [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) before the HotCRP audit in
   [`../skills/socc-submission`](../skills/socc-submission/SKILL.md).
