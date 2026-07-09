# IEEE INFOCOM Resources

Action-oriented resources for the INFOCOM skill pack. The `skills/` give advice; this directory
lets an agent model an INFOCOM-shaped paper, benchmark against verified exemplars, and prepare an
optional replication package for a large-scale, double-blind, no-rebuttal IEEE process.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for an analytical + simulation networking paper. Illustrative fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, verified IEEE INFOCOM papers across contribution shapes, and avoid sibling-venue confusion with SIGCOMM, NSDI, MobiCom, and the journals. |
| [`official-source-map.md`](official-source-map.md) | Confirm the current-cycle INFOCOM deadlines, the IEEEtran page budget, the double-blind/EDAS review model, the early-reject phase, and IEEE Xplore publication before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open the official INFOCOM, EDAS, IEEE PDF eXpress, and IEEE Xplore surfaces, plus cross-check sources for when the gateway blocks a direct fetch. |
| [`code/README.md`](code/README.md) | Use the shared replication-package tooling: a claim-to-evidence matrix and a dependency-free smoke checker, adapted to INFOCOM's optional-release, no-artifact-track reality. |

## Scope Note

This is a **computer-networking** conference pack whose papers publish in **IEEE Xplore**, not an
ML-conference or economics pack. Do not import the OpenReview/PMLR machinery or the Stata/DiD/IV/RDD
econometrics kit. INFOCOM evidence is networking evidence: a stated system model, a proof under
justified assumptions, a seeded simulation with a named simulator, or a testbed/measurement study —
carried through a large-scale, double-blind, EDAS-based review that traditionally offers **no
rebuttal**, so the submitted PDF must defend itself.

## Suggested Workflow

1. Route and frame with
   [`../skills/infocom-topic-selection`](../skills/infocom-topic-selection/SKILL.md) and
   [`../skills/infocom-writing-style`](../skills/infocom-writing-style/SKILL.md) — deciding INFOCOM
   vs. SIGCOMM/NSDI/MobiCom by contribution shape before writing is the highest-leverage move.
2. Build evidence with [`../skills/infocom-experiments`](../skills/infocom-experiments/SKILL.md),
   [`../skills/infocom-reproducibility`](../skills/infocom-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm the live cycle in
   [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) before the EDAS audit in
   [`../skills/infocom-submission`](../skills/infocom-submission/SKILL.md).
