---
name: jeg-tables-figures
description: Use when preparing Journal of Economic Growth exhibits: growth-regression tables, convergence plots, transition paths, calibration moments, historical-data maps, robustness tables, and appendix diagnostics.
---

# Tables & Figures (jeg-tables-figures)

## When to trigger

- Main results exist but exhibits do not communicate growth mechanisms
- Calibration or simulation output needs a readable structure
- Empirical tables lack sample, fixed-effect, clustering, or unit notes

## Exhibit architecture

- **Descriptive growth facts**: long-run trends, cross-country dispersion,
  transition paths, or cohort patterns.
- **Main estimates or model results**: one table/figure per claim, not per
  estimator experiment.
- **Mechanism exhibits**: human capital, fertility, technology, institutions,
  financial development, migration, or political economy channels.
- **Robustness/sensitivity**: alternative samples, periods, specifications,
  calibration targets, and parameter values.

## JEG-specific polish

- Use economically meaningful units: annual percentage points of growth, log GDP
  per worker, schooling years, fertility rates, TFP, steady-state ratios.
- Label whether an exhibit is empirical, calibrated, simulated, or theoretical.
- For transition paths, show initial condition, time scale, and steady state.
- For cross-country panels, disclose country coverage and period.

## Exhibit sequence

Most JEG papers need one of these sequences:

- **Empirical growth**: descriptive growth fact -> identification diagnostic -> main estimate -> mechanism or
  heterogeneity -> robustness.
- **Theory/calibration**: model mechanism diagram or proposition summary -> calibration table -> transition
  path -> sensitivity -> welfare or growth decomposition.
- **Mixed paper**: empirical fact motivating the mechanism -> model result -> calibration/estimation -> data
  validation -> counterfactual.

The sequence should make the growth mechanism visible before the robustness appendix expands.

## Growth exhibit contract

Each exhibit should state whether it shows a fact, identifies a mechanism, validates a model, or tests
sensitivity. Do not let all tables look like robustness tables. A JEG reader should be able to follow the
growth story from exhibits alone:

```text
Fact -> mechanism -> model/estimate -> magnitude -> sensitivity -> implication
```

For calibration exhibits, report the target moment, model moment, parameter value, and source. For
empirical exhibits, report country/region coverage, period, units, fixed effects, clustering, and whether
the estimate is meant to be causal or descriptive.

## Map and spatial-exhibit standards

Persistence and comparative-development submissions live and die by their spatial exhibits:

- Every map states the projection, the unit (grid cell, district, ethnic homeland), the period of the plotted variable, and the source layer.
- Show the treatment variation on a map *before* the regression tables appear; growth referees want to see where identification comes from geographically.
- Table notes for geocoded outcomes state the spatial-SE method and cutoffs (e.g., "Conley SEs, 250 km, in brackets") next to the clustered SEs — in the main table, not buried in an appendix.
- Avoid choropleth color scales that flatten the variation actually identifying the model; bin by the estimation sample's own distribution.

## Worked vignette — rebuilding a persistence main table

Illustrative redesign of a weak Table 2 (outcome: log GDP per capita 2015 by district; regressor: early printing-press adoption):

- Column 1: OLS with country FE — 0.19 (clustered SE 0.04).
- Column 2: adds geography controls (ruggedness, latitude, coast distance) — 0.16 (0.04).
- Column 3: same specification reporting Conley 250 km SEs — 0.16 (0.06); an inference column, not a new estimate.
- Column 4: IV using distance to an early adoption hub — 0.24 (0.09), with first-stage F = 21 in the notes.
- One row added: the outcome mean, so magnitudes read directly as percent effects.

The old version's six estimator-variation columns move to the appendix, and the schooling-channel table is promoted into the main text — mechanism before robustness.

## Exhibit-count anchor (hedged)

Accepted articles at this journal commonly carry 6-10 main exhibits backed by a deep online appendix; treat that as a prior from recent issues rather than a rule, and check figure-format specifics against the journal's current author guidelines.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JEG (growth) uses cross-country and long-run panels with deep endogeneity; foreground identification and robustness to alternatives.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Output format

```text
[Exhibit] table / figure / appendix
[Claim supported] ...
[Units and sample] ...
[Model/data status] empirical / calibrated / simulated
[Missing note fields] ...
[Next step] jeg-writing-style
```
