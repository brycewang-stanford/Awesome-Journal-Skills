---
name: jde-tables-figures
description: Use when designing the main exhibits for a Journal of Development Economics (JDE) manuscript — figure-forward presentation of treatment effects, heterogeneity, and event studies for development settings, with self-contained notes. Shapes exhibits; it does not run the estimation.
---

# Tables & Figures (jde-tables-figures)

## When to trigger

- The main result is a nine-column table no reader can parse
- A treatment effect or pre-trend would land harder as a figure
- Heterogeneity across subgroups is buried in interaction rows
- Notes under exhibits are too thin to stand alone for a referee

## The JDE exhibit bar

Development economics has moved toward **figure-forward** presentation, and JDE exhibits should make the headline result legible at a glance to a development economist skimming the paper. Principles:

- **Lead with a figure where the design allows it.** Event-study plots (DID), discontinuity plots (RDD), and treatment-effect-by-subgroup plots communicate a field result faster than a coefficient table. RCT main effects often read best as a clean coefficient plot with confidence intervals.
- **One main table, deep appendix.** Keep the main coefficient table tight (headline outcomes, the preferred specification, clustered SEs noted); push alternative specifications, balance, attrition, and robustness to the extensive online appendix.
- **Self-contained notes.** Each exhibit must state the sample, unit of observation, the level at which standard errors are clustered, the estimator, control set, and what the bars/bands represent — a referee should not have to hunt in the text.
- **Welfare-relevant scaling.** Where possible, scale axes and report effects in policy-comparable units (share of the poverty gap, standard deviations, cost per outcome) so magnitude is visible, not just significance.
- **Geography and maps.** When spatial variation drives the design (market access, program rollout, conflict), a map or spatial figure earns its place.

JDE accepts **any consistent formatting style at submission** (the journal's style is applied at the proof stage), so do not burn time on house-style table formatting before acceptance — spend it on clarity, correct clustering, and reproducibility. Every exhibit must be regenerable from the submitted code.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md).

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id` — one variable definition, one set of numbers, body and appendix in sync.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering (from the result's diagnostics) and
  states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Headline result presented as a figure where the design allows
- [ ] Main table limited to preferred specification + headline outcomes
- [ ] Clustering level and estimator stated in each note
- [ ] Confidence intervals / bands shown; no chartjunk (no 3D, minimal color)
- [ ] Effects scaled to welfare/policy-comparable units where possible
- [ ] Vector output (PDF/EPS) at print resolution
- [ ] Every exhibit reproducible from the master script

## Exhibit-design decision grid (by JDE design type)

| Design in the paper            | Lead exhibit a JDE referee expects                       | Notes line that must appear                            |
|--------------------------------|----------------------------------------------------------|--------------------------------------------------------|
| Cluster-randomized field trial | Coefficient/forest plot of ITT by outcome, 95% CIs       | Randomization level, N clusters, control mean          |
| RDD on an eligibility cutoff   | Binned scatter with local-linear fit + density plot      | Bandwidth, kernel, polynomial order, McCrary p-value   |
| Staggered policy rollout (DID) | Event-study plot, leads near zero, modern estimator      | Estimator (CS / SA / dCDH), cohort weighting           |
| IV off an institutional rule   | First-stage scatter + reduced-form plot                  | First-stage F, exclusion logic, complier share         |
| Spatial / market-access design | Map of treatment intensity or program reach              | Spatial unit, color encoding, spatial SE clustering    |

## Worked micro-example (illustrative numbers)

Hypothetical JDE paper: a cluster-randomized after-school tutoring program across 120 villages in a low-income setting, randomized at the village level (60 treatment, 60 control), ~25 children sampled per village.

- **Wrong instinct:** an eight-column table reporting test scores, attendance, a sub-index, and three interactions, all with stars. A development referee cannot find the headline.
- **JDE-shaped fix:** one coefficient plot — ITT on the standardized test-score index = +0.18 SD (95% CI 0.06 to 0.30), control mean printed below the axis (*illustrative*). Attendance and the sub-index sit beside it as secondary points; the three interactions move to an appendix figure flagged "exploratory."
- **Note line:** "ITT; clustering at village level (60/60), N = 2,940; bars are 95% wild-cluster-bootstrap CIs. Figures *illustrative*."

## Referee pushback the right exhibit pre-empts

- *"Is 0.18 SD a lot?"* → print the control mean and a policy-comparable benchmark on the figure; significance never substitutes for size at JDE.
- *"Which subgroup splits were pre-registered?"* → solid markers for pre-specified subgroups, hollow for exploratory, MHT-adjusted intervals shown.

## Anti-patterns

- A dense table when one event-study or coefficient plot would carry the result
- Notes that omit the clustering level or sample definition
- Significance stars with no economically meaningful magnitude
- Polishing to Elsevier house style before acceptance (style is applied at proof stage)
- A heterogeneity panel that hides which splits were pre-specified versus mined

## Output format

```
【Headline exhibit】figure type + what it shows
【Main table】outcomes + spec + clustering noted
【Appendix exhibits】[robustness, balance, attrition, ...]
【Scaling】effects in policy-comparable units? [Y/N]
【Reproducible from code?】[Y/N]
【Next step】jde-writing-style
```
