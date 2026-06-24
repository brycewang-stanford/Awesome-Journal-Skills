---
name: red-tables-figures
description: Use when designing the exhibits of a Review of Economic Dynamics (RED) manuscript — impulse-response functions, calibration tables, moment-matching (model-vs-data) tables, policy-experiment figures, and accuracy diagnostics — so a quantitative dynamic paper communicates its mechanism and fit clearly to the SED readership.
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

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). RED is quantitative macro — mostly structural/calibration, which is outside this causal-inference toolchain; apply the chain to its empirical/reduced-form papers.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] IRFs / transition paths show the mechanism, not just outcomes
- [ ] Calibration and moment tables let a reader audit discipline and fit
- [ ] Untargeted moments are reported, not hidden
- [ ] Every exhibit is self-contained, numbered, and legible at print resolution

## Anti-patterns

- Steady-state-only comparisons that hide the dynamics
- Moment tables showing only targeted moments
- Figures with no notes on model variant, shock, or units

## Exhibit sequence

For most RED papers, the exhibit order should mirror the argument:

1. **Mechanism figure**: state variables or transition paths that show the dynamic force.
2. **Discipline table**: parameters, calibration targets, estimation targets, and sources.
3. **Fit table**: targeted and untargeted moments, model vs data.
4. **Counterfactual/experiment**: the quantitative result or policy path.
5. **Accuracy/reproducibility note**: solver error, convergence, seed, or runtime when computation matters.

If the first exhibit is a static regression table, ask whether the paper is really using RED's dynamic
lens or drifting toward a field journal.

## Mock moment table (model vs data)

The fit table referees scan first should look like this (all numbers illustrative):

```text
Table X: Targeted and untargeted moments
                                     Data    Model   Source
Targeted
  Wealth-to-income ratio             2.90    2.90    NIPA / Flow of Funds
  Share with negative net worth      0.135   0.132   SCF
Untargeted
  Wealth Gini                        0.78    0.74    SCF
  Top-10% wealth share               0.71    0.66    SCF
  Average quarterly MPC              0.16    0.19    literature estimates (author-year)
Notes: model moments from the stationary distribution; simulation of 100,000
households; seed recorded in the archive readme.
```

The Targeted/Untargeted split must be typographically explicit — a single undifferentiated column invites
the circularity objection from quantitative-macro referees.

## Exhibit-budget anchor

Hedged anchor (verify against recent RED issues rather than treating it as policy): mainline quantitative
papers commonly carry on the order of 4–8 main-text exhibits — typically one mechanism/IRF figure, a
calibration table, a fit table, and one or two counterfactual exhibits — with accuracy diagnostics and
extended sensitivity in an appendix. Treat that as a budget: each additional main-text exhibit must
change what the reader believes about the mechanism or the magnitude.

## Figure-craft pushback

| Exhibit complaint | Fix for a dynamics paper |
|---|---|
| IRFs without units or horizon labels | percent vs pp deviation, quarters vs years, stated on axes and in notes |
| Counterfactual shown only at the new steady state | add the transition path — adjustment dynamics are often the contribution |
| Mechanism overlays illegible in grayscale | vary line style, not only color; print-test the PDF |
| Distributional result collapsed to a mean | plot the policy function or the cross-sectional shift; heterogeneity is usually the point |

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — plotting and solver outputs
- [`red-data-analysis`](../red-data-analysis/SKILL.md) — the analysis behind the exhibits
