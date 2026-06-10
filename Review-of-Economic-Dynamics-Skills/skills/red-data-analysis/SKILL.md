---
name: red-data-analysis
description: Use when building or auditing the quantitative analysis behind a Review of Economic Dynamics (RED) manuscript — calibration, moment-matching, structural estimation, and numerical-solution discipline for dynamic models, plus reproducible-computation hygiene that the RED code-first culture expects. Lighter on raw empirics for purely theoretical papers; focused on numerical examples and reproducible computation there.
---

# Quantitative Analysis for RED (red-data-analysis)

## When to trigger

- Calibrating or estimating a dynamic model and reporting model-vs-data fit
- Building the numerical experiments that carry a computational paper
- Making the computation reproducible ahead of the RED data/code archive

## What RED-quality analysis looks like

RED is method-defined, so "data analysis" usually means **disciplining a dynamic model**, and for
**purely theoretical** papers it is lighter — focus there on **numerical examples and reproducible
computation** that illustrate the result rather than estimate it.

- **Calibration** — list every parameter, its value, its source/target, and whether it is calibrated,
  estimated, or assumed. Calibration targets should be explicit moments, not vibes.
- **Moment-matching / estimation** — report the targeted moments, the fit (model vs data), and untargeted
  moments the model also matches (a strong credibility signal). Document the estimator and its assumptions.
- **Numerical solution discipline** — state the solution method (perturbation, projection, global, EGM,
  sequence-space), the grid/approximation order, and an **accuracy check** (e.g., Euler-equation errors).
- **Reproducible computation** — fix and record **random seeds**, capture software/OS and package
  versions, and write a master "run-all" script. RED's readme requires execution order, expected runtime,
  and seeds, so build that discipline in from the start.

## Checklist

- [ ] Every parameter has a value and a documented source/target
- [ ] Targeted and untargeted moments reported; model-vs-data fit shown
- [ ] Solution method, approximation order, and an accuracy check are stated
- [ ] Seeds fixed/recorded; environment captured; a run-all script exists

## Anti-patterns

- Reporting only the moments the model was calibrated to hit
- An undocumented numerical solution with no accuracy diagnostic
- Leaving seeds and environment uncaptured, so the archive will not reproduce

## RED analysis table skeleton

Require a compact audit table before results are written:

| Item | RED-ready entry |
|---|---|
| Parameters | value, source/target, calibrated vs estimated vs assumed |
| Data moments | targeted moments plus untargeted validation moments |
| Solver | method, grid/order, convergence rule, accuracy diagnostic |
| Experiments | baseline, counterfactual, transition path, sensitivity |
| Archive | run-all command, seeds, software/OS, expected runtime |

This table can become a manuscript table, appendix table, or replication README section. If it cannot be
filled, the quantitative core is not ready for RED.

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — Dynare, SSJ, Julia/QuantEcon, FRED
- [`red-replication-and-data-policy`](../red-replication-and-data-policy/SKILL.md) — the archive these outputs feed
