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

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). RED is quantitative macro — mostly structural/calibration, which is outside this causal-inference toolchain; apply the chain to its empirical/reduced-form papers.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
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

## Illustrative calibration record (Aiyagari-style economy)

Both the paper and the archive should carry a calibration record in this shape (values illustrative):

```text
Internally calibrated (chosen to hit model-generated targets):
  beta  = 0.957   target: K/Y = 2.9 (annual)                     model hits: 2.90
  phi   = -1.1    target: share with negative net worth = 13.5%  model hits: 13.2%
Externally set (taken from outside estimates):
  sigma = 2.0     CRRA; standard in the incomplete-markets literature (author-year)
  rho_z = 0.91    AR(1) earnings persistence, PSID estimates (author-year)
Accuracy at this parameterization:
  max log10 |Euler error| = -4.6, 200-pt log-spaced asset grid, a_max = 40x mean income
```

Separating **internally calibrated** from **externally set** parameters matters at RED: referees check
whether each internal target is actually informative about its parameter, and whether external values
are sourced rather than convenient.

## Moment-fit objections and the RED-grade response

| Objection | Fix |
|---|---|
| "Targets are not independent of the moment you claim to explain" | re-calibrate with the headline moment excluded; report it as untargeted |
| "Fit shown only for targeted moments" | add an untargeted panel (wealth Gini, top shares, MPC distribution) |
| "No accuracy diagnostic at the headline solution" | Euler or den Haan errors at exactly that parameterization |
| "Grid and discretization undocumented" | state grid sizes, bounds, Rouwenhorst/Tauchen choice, and a grid-doubling stability check |

## Minimum reproducible run

Before submission, maintain two runs:

- **Smoke run**: reduced grid or shorter simulation that completes quickly and verifies code paths.
- **Publication run**: full grid, full simulation length, final seeds, final moments, and final exhibits.

Both runs should write comparable output names and logs. If the smoke run and publication run disagree in
qualitative direction, the numerical method needs diagnosis before the paper is ready. Record expected
runtime for both because RED's readme requirement makes runtime part of the archive, not an afterthought.

## Output format

```text
[Analysis status] ready / missing moments / weak solver diagnostics / unreproducible
[Calibration/estimation] <targets, parameters, estimator>
[Numerical checks] <solver, accuracy, convergence, sensitivity>
[Archive readiness] run-all / seeds / OS / runtime / missing
[Next analysis] <single computation or table to repair>
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — Dynare, SSJ, Julia/QuantEcon, FRED
- [`red-replication-and-data-policy`](../red-replication-and-data-policy/SKILL.md) — the archive these outputs feed
