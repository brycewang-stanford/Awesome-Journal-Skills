# ACM IMC Resources

Action-oriented resources for the IMC skill pack. The `skills/` give advice; this directory lets
an agent model a measurement-first IMC paper, benchmark against verified exemplars, and prepare a
dataset/artifact release for IMC's double-blind, two-deadline, One-Shot-Revision process with its
ethics and availability expectations.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for an empirical Internet-measurement paper. Illustrative fictional study; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, verified IMC papers across measurement contribution shapes, and avoid sibling-venue confusion with SIGCOMM, NSDI, CoNEXT, and PAM. |
| [`official-source-map.md`](official-source-map.md) | Confirm the current-cycle IMC deadlines, page limits, review model, Ethics requirement, and artifact declaration before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open the official IMC, SIGCOMM, HotCRP, and ACM DL surfaces, plus the cross-check sources for when the gateway blocks a direct fetch. |
| [`code/README.md`](code/README.md) | Use the shared replication-package tooling, plus IMC-specific checks: the availability declaration, dataset provenance, vantage-point documentation, and the ethics gate. |

## Scope Note

This is an **empirical network-measurement** conference pack, not an ML-conference, SE, or
economics pack. Do not import the OpenReview/PMLR machinery, the ACM artifact-badge-first framing
of a software conference, or the Stata/DiD/IV/RDD econometrics kit. IMC evidence is measurement
evidence: representative vantage points, honest ground truth, longitudinal awareness of a moving
Internet, ethical active measurement, and a released dataset — carried through a double-blind,
One-Shot-Revision-capable review with a hard ethics gate.

## Suggested Workflow

1. Route and frame with
   [`../skills/imc-topic-selection`](../skills/imc-topic-selection/SKILL.md) and
   [`../skills/imc-writing-style`](../skills/imc-writing-style/SKILL.md) — deciding IMC vs.
   SIGCOMM/NSDI/CoNEXT/PAM before measuring is the highest-leverage move.
2. Build evidence with [`../skills/imc-experiments`](../skills/imc-experiments/SKILL.md),
   [`../skills/imc-reproducibility`](../skills/imc-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md), and settle the Ethics story early with
   [`../skills/imc-submission`](../skills/imc-submission/SKILL.md).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm the live cycle
   in [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) before the HotCRP audit in
   [`../skills/imc-submission`](../skills/imc-submission/SKILL.md).
