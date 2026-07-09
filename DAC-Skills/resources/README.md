# DAC Resources

Action-oriented resources for the DAC skill pack. The `skills/` give advice; this directory lets an
agent model a DAC-shaped paper, benchmark against verified exemplars, and prepare a reproducible EDA
evaluation for the double-blind, single-shot Research-Manuscript process on Softconf.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for a QoR-forward EDA paper. Illustrative fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, verified DAC papers (Chaff, ABC rewriting, logic-obfuscation security, DREAMPlace) across contribution shapes, and avoid sibling-venue confusion with ICCAD, DATE, ASP-DAC, and S&P. |
| [`official-source-map.md`](official-source-map.md) | Confirm the current-cycle DAC deadlines, the 6+1 budget, double-blind review, ACM-DL archival, and the Research-vs-Engineering track split before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open the official DAC, IEEE CEDA, ACM DL, and Softconf surfaces, plus the EDA benchmark suites and open flows, for when the gateway blocks a direct fetch. |
| [`code/README.md`](code/README.md) | Use the shared replication-package tooling: a claim-to-QoR matrix, an EDA-flow provenance checklist, and a dependency-free smoke checker for anonymized artifacts. |

## Scope Note

This is an **electronic-design-automation** conference pack whose evidence is **QoR on EDA
benchmarks** — area/delay/power (PPA), wirelength, timing slack, coverage, and runtime on ISPD/EPFL/
ISCAS/ITC/TAU/CircuitNet — carried through a **double-blind, single-shot, TPC-driven** review to an
**ACM Digital Library** archival paper. Do **not** import the ML-conference OpenReview/PMLR machinery,
the empirical-SE artifact-badging kit, or the econometrics Stata/DiD toolset; and do not assume a
rebuttal round or an artifact-evaluation badge track, neither of which DAC has historically run.

## Suggested Workflow

1. Route and frame with
   [`../skills/dac-topic-selection`](../skills/dac-topic-selection/SKILL.md) — deciding DAC vs.
   ICCAD/DATE/ASP-DAC/architecture, **and** Research-Manuscript vs. Engineering-Track, is the
   highest-leverage move — then [`../skills/dac-writing-style`](../skills/dac-writing-style/SKILL.md)
   for the six-page shape.
2. Build evidence with [`../skills/dac-experiments`](../skills/dac-experiments/SKILL.md),
   [`../skills/dac-reproducibility`](../skills/dac-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm the live cycle in
   [`official-source-map.md`](official-source-map.md) and [`external_tools.md`](external_tools.md)
   before the Softconf audit in
   [`../skills/dac-submission`](../skills/dac-submission/SKILL.md).
