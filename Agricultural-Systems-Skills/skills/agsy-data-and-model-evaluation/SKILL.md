---
name: agsy-data-and-model-evaluation
description: Use when evaluating the model and analyzing results for an Agricultural Systems (AgSy) manuscript so it survives expert systems review — independent model evaluation (observed vs. simulated, fit statistics), sensitivity and uncertainty analysis, and trade-off / scenario analysis across the system. Guides evaluation norms; it does not fabricate results or run the model.
---

# Data & Model Evaluation (agsy-data-and-model-evaluation)

A model is only as credible as its **evaluation**. AgSy reviewers are systems-modelling experts: they
want to see the model tested against **independent** data, its **sensitivity and uncertainty**
characterized, and the **trade-offs** the system exhibits — not a single tuned run presented as truth.
Model description and choice live in `agsy-systems-framing-and-modeling`; this skill covers testing and
reporting.

## When to trigger

- Reporting how well the model reproduces observations
- Running sensitivity / uncertainty analysis
- Building scenario comparisons and trade-off analyses
- A reviewer asked for validation, sensitivity, uncertainty, or alternative scenarios

## Evaluation norms AgSy expects

1. **Independent evaluation.** Compare **observed vs. simulated** on data **not used for calibration**.
   Report standard fit statistics — **RMSE, RRMSE, bias/ME, modelling efficiency (NSE), index of
   agreement (d), R²** — and show the 1:1 plot. State what "good enough" means for the decision.
2. **Sensitivity analysis.** Identify the parameters/inputs that drive outputs (local one-at-a-time
   and, where feasible, global methods — **Morris, Sobol**). Report which assumptions matter most.
3. **Uncertainty.** Propagate uncertainty from inputs, parameters, and structure to the outputs that
   carry the conclusions. Present ranges/intervals, not point estimates dressed as certainty.
4. **Trade-off & scenario analysis.** This is where AgSy papers earn their place: compare scenarios or
   management/design options on **multiple objectives** (yield, profit, environment, risk) and show the
   **trade-offs and synergies** — Pareto fronts, trade-off curves, multi-indicator profiles.
5. **Scaling.** When you aggregate from field to farm to region, state how, and check that aggregation
   does not hide compensating errors.

## Stochastic & data-driven components
- For Monte Carlo, ABM, or stochastic weather/price generators: **set and report seeds**, run enough
  replicates, and report the distribution, not one realization.
- For surrogate/emulator or ML components: validate against the full model and report where they fail.

## Reproducibility while you work (not at the end)
- One **master workflow** regenerates every figure/table from inputs + model runs.
- Pin model version, parameter sets, and software versions; record calibration vs. evaluation splits.
- Keep table/figure numbers matched to script/model outputs — the data/code/model are deposited (see
  `agsy-reproducibility-and-data-policy`).

## Anti-patterns

- Calibrating and "validating" on the **same** data; reporting fit only on the training period
- A single tuned run with no sensitivity or uncertainty analysis
- Reporting R² alone (insensitive to bias) — pair it with RMSE/NSE/bias
- Scenario tables with no trade-offs surfaced (just "scenario B is best")
- Aggregating across scales without checking for compensating errors

## Output format

```
【Evaluation data】independent of calibration? [Y/N]
【Fit statistics】RMSE / NSE / bias / d / R² + 1:1 plot
【Sensitivity】which inputs/parameters dominate
【Uncertainty】propagated to the conclusion-bearing outputs? [Y/N]
【Trade-offs】scenarios compared on multiple objectives (Pareto/curve)
【Reproducible】master workflow + pinned model/version + seeds? [Y/N]
【Next】agsy-figures-and-tables
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — calibration, sensitivity, uncertainty, and multi-objective packages
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — research-data/model reproducibility policy
