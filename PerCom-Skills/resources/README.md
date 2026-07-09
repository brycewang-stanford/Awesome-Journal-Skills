# IEEE PerCom Resources

Action-oriented resources for the PerCom skill pack. The `skills/` give advice; this directory
lets an agent model a PerCom-shaped paper, benchmark against verified exemplars, and prepare a
reproducible human-subjects sensing package for the double-blind, rebuttal-based IEEE process.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for a pervasive-computing activity-recognition paper. Illustrative fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, verified IEEE PerCom papers across contribution shapes, and avoid confusion with ACM UbiComp/IMWUT, MobiCom, SenSys, and IPSN. |
| [`official-source-map.md`](official-source-map.md) | Confirm the current-cycle PerCom deadline, IEEEtran page budget, double-blind rebuttal model, IEEE Xplore publication, and awards before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open the official PerCom, HotCRP, IEEE Xplore, and dblp surfaces, plus the cross-check sources for when the gateway blocks a direct fetch. |
| [`code/README.md`](code/README.md) | Use the shared reproducibility tooling: an evidence-to-claim matrix, a sensing-dataset release checklist, and a dependency-free smoke checker for anonymized artifacts. |

## Scope Note

This is a **pervasive / ubiquitous computing** conference pack whose papers publish in **IEEE
Xplore**, not an ML-conference or economics pack. Do not import the OpenReview/PMLR machinery or
the Stata/DiD/IV/RDD econometrics kit. PerCom evidence is human-centric ubicomp evidence: real
human subjects and sensors, cross-subject / leave-one-subject-out evaluation, F1 rather than raw
accuracy on imbalanced activity classes, honest deployment realism, and a releasable sensing
dataset — carried through a double-blind review with a single bounded rebuttal.

## Suggested Workflow

1. Route and frame with
   [`../skills/percom-topic-selection`](../skills/percom-topic-selection/SKILL.md) and
   [`../skills/percom-writing-style`](../skills/percom-writing-style/SKILL.md) — deciding PerCom
   vs. UbiComp/IMWUT, MobiCom, SenSys, or IPSN before writing is the highest-leverage move.
2. Build evidence with [`../skills/percom-experiments`](../skills/percom-experiments/SKILL.md),
   [`../skills/percom-reproducibility`](../skills/percom-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm the live cycle
   in [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) before the HotCRP audit in
   [`../skills/percom-submission`](../skills/percom-submission/SKILL.md).
