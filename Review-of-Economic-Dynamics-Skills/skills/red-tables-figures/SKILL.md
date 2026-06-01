---
name: red-tables-figures
description: Use to design the exhibits of a Review of Economic Dynamics (RED) manuscript — impulse-response functions, calibration tables, moment-matching (model-vs-data) tables, policy-experiment figures, and accuracy diagnostics — so a quantitative dynamic paper communicates its mechanism and fit clearly to the SED readership.
---

# Tables & Figures for RED (red-tables-figures)

## When to trigger

- Building the exhibits that carry a quantitative dynamic paper
- Deciding how to show model-vs-data fit and the mechanism behind a result
- Making IRFs and policy experiments legible at print resolution

## Exhibits that fit RED

RED papers live or die on whether the **mechanism** and the **quantitative fit** are visible. Favor:

- **Impulse-response functions (IRFs)** — the workhorse figure for dynamic models; plot model responses
  to the key shocks, overlay alternative parameterizations to isolate the mechanism, and (where relevant)
  overlay empirical responses.
- **Calibration table** — every parameter, value, source/target, and status (calibrated/estimated/assumed),
  so a reader can audit discipline at a glance.
- **Moment-matching table** — targeted and **untargeted** moments side by side, model vs data; untargeted
  fit is a credibility highlight, so give it prominence.
- **Policy / counterfactual experiment figures** — show the magnitude of the dynamic effect and the
  transition path, not just steady-state comparisons.
- **Accuracy diagnostics** — Euler-equation errors or convergence plots where the computation is non-trivial.

Make each exhibit **self-contained**: numbered, called out in order, with notes stating the model variant,
shock, units, and data source. Author-year citations in notes match RED's reference system.

## Checklist

- [ ] IRFs / transition paths show the mechanism, not just outcomes
- [ ] Calibration and moment tables let a reader audit discipline and fit
- [ ] Untargeted moments are reported, not hidden
- [ ] Every exhibit is self-contained, numbered, and legible at print resolution

## Anti-patterns

- Steady-state-only comparisons that hide the dynamics
- Moment tables showing only targeted moments
- Figures with no notes on model variant, shock, or units

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — plotting and solver outputs
- [`red-data-analysis`](../red-data-analysis/SKILL.md) — the analysis behind the exhibits
