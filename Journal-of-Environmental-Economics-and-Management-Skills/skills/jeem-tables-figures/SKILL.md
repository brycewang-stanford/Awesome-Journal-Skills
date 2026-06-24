---
name: jeem-tables-figures
description: Use when the exhibits of a Journal of Environmental Economics and Management (JEEM) manuscript — regression tables, event-study plots, maps, WTP/demand-curve figures — do not yet show the environmental signal cleanly. Designs publication-grade exhibits in JEEM/Elsevier house style; it does not run the analysis (jeem-robustness) or write the prose (jeem-writing-style).
---

# Tables and Figures (jeem-tables-figures)

## When to trigger

- The main result is settled but the table or figure does not make the welfare number jump out
- A spatial or treatment-timing story would land better as a map or event-study plot than a coefficient
- A valuation paper needs to show a WTP distribution, a demand curve, or choice-experiment marginal effects
- Exhibits are dense, mislabeled, or rely on significance stars instead of magnitudes and CIs

## What JEEM exhibits must do

Environmental economics is inherently spatial and dynamic, so JEEM exhibits should **exploit geography and time**, not just stack coefficients. The reader — and the referee — should be able to see the identifying variation and the welfare magnitude from the exhibit alone. Lead with the figure that shows the design (an event study, a map of treatment, an RD plot, a WTP density); relegate the full regression table to support it.

| Result type | The exhibit that sells it | Common failure to avoid |
|-------------|---------------------------|--------------------------|
| Staggered regulation DiD | event-study plot with leads/lags + CIs | a single DiD coefficient with no dynamics |
| Spatial treatment / exposure | a clean map of treatment and the outcome gradient | a table that hides where the variation is |
| RD in a standard/threshold | binned RD plot with fitted polynomials | over-fitted high-order polynomial, no bins shown |
| Hedonic capitalization | coefficient + implied $ WTP per unit, with CI | a raw coefficient with no welfare translation |
| Stated-preference WTP | WTP distribution / CV curve with uncertainty | only utility coefficients, no compensating variation |
| Damage / dose-response | dose-response curve with CI band | a single linear slope hiding nonlinearity |

## Maps are exhibits, not decoration

Because environmental variation is spatial, a map often does identification work that a table cannot: it shows where treatment fell, whether treated and control units are comparable, and whether the outcome gradient lines up with the exposure. Treat maps with the same rigor as regression tables. State the coordinate reference system and the unit of aggregation; choose a perceptually uniform, colorblind-safe scale (not rainbow); show treatment and outcome on comparable geographies and at a scale where the reader can see the variation. A sloppy map that exaggerates a gradient is worse than no map, because referees will distrust the rest of the exhibits.

## House-style and craft rules

1. **Translate to welfare units in the exhibit.** Report the implied dollar damage, $ WTP, or % capitalization in the table or note — not just a regression coefficient the reader must convert.
2. **Show uncertainty as CIs, not just stars.** Confidence intervals and standard errors communicate magnitude; report them prominently. Significance stars are acceptable in Elsevier style but must never substitute for the magnitude and its CI.
3. **Make maps honest.** State the projection, the unit, and the color scale; avoid rainbow scales that exaggerate; show the treatment and the outcome on comparable geographies.
4. **Self-contained notes.** Each table/figure note states the sample, the unit of observation, the clustering/spatial-SE choice, and the estimand — a referee should not need the text to read the exhibit.
5. **Follow the Elsevier/JEEM mechanics** (检索于 2026-06；以官网为准): high-resolution figures, color used meaningfully, consistent decimal places, units in column headers. Re-check the current artwork and table guidance in the guide for authors.

## Showing nonlinearity in dose-response

Environmental damages and valuations are often nonlinear — pollution-mortality concentration-response curves, threshold effects in temperature, diminishing WTP in scope. A single linear slope hides exactly the structure a regulator needs (where marginal damage steepens, where a standard should bind). When the relationship is plausibly nonlinear, show the dose-response curve with a confidence band rather than reporting one coefficient, and let the exhibit reveal the shape. A flexible specification that turns out linear is reassuring; a linear specification that hides a kink is a missed contribution and an easy referee point.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JEEM is environmental economics — policy/regulation designs and non-market valuation; the causal chain serves its program-evaluation lane.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] The lead exhibit shows the identifying variation (event study / map / RD plot), not just a coefficient
- [ ] The welfare-relevant magnitude (damage, $ WTP, % capitalization) appears in dollar/percent units
- [ ] Confidence intervals / standard errors shown; stars never replace the magnitude
- [ ] Maps state projection, unit, and a non-misleading color scale
- [ ] Every table/figure note is self-contained (sample, unit, SE choice, estimand)
- [ ] Decimal places, units, and variable labels are consistent across exhibits
- [ ] Figure resolution and format meet current Elsevier artwork specs (待核实)

## Worked vignette (illustrative)

A regulation-DiD paper reports a single coefficient: "treatment lowered PM2.5 by 8% (s.e. 2%)." A referee cannot tell whether pre-trends were flat or whether the effect grew over time. The JEEM fix: replace the lone coefficient with an event-study figure showing four pre-period leads (flat, near zero) and the post-period dynamics (the effect builds over three years to 8%), each with a 95% CI band, clustered spatially. The same table now reports the implied avoided-mortality value in dollars using a stated VSL, so the welfare magnitude is legible without leaving the exhibit. A companion map shows treated vs. control counties, making the identifying variation visible at a glance.

## A note on dollar translation

The single most common JEEM exhibit failure is leaving the result as a regression coefficient. A coefficient on log price, a hazard ratio, or a logit utility weight is not a welfare statement. Every headline exhibit should carry the conversion the reader needs: a hedonic coefficient → implied $ WTP per unit of the amenity; a mortality coefficient → avoided deaths and their valuation; a discrete-choice utility weight → compensating variation. Put the conversion and its CI in the table note or a dedicated column so the referee never has to do the arithmetic — and so the welfare claim is auditable on the page.

## Significance stars vs. magnitude

Elsevier house style permits significance stars, and JEEM does not ban them — but at this journal the persuasive object is the *magnitude and its uncertainty*, not the asterisk. Lead with the point estimate and its confidence interval in interpretable (welfare) units; let stars, if used, be a secondary cue. A table where the reader's eye lands on a row of asterisks instead of on a dollar damage or a WTP has buried the contribution. The discipline is the same as in the robustness suite: show that the welfare-relevant number is both economically meaningful and precisely estimated, and let the reader judge significance from the interval.

## Anti-patterns

- A single DiD coefficient where an event-study plot would show (or undermine) parallel trends
- A hedonic table reporting a coefficient with no implied dollar WTP
- Rainbow / misleading color scales on a pollution or treatment map
- Stated-preference results shown only as utility coefficients, never as compensating variation
- Table notes that omit the clustering/spatial-SE choice or the estimand
- Over-fitted RD polynomials with no binned scatter to ground them

## The exhibit sequence that tells the story

Order the exhibits so a referee can follow the argument from the figures alone: (1) a descriptive map or time series that establishes the environmental setting and where/when the variation occurs; (2) the design exhibit — event study, RD plot, first-stage, or balance table — that earns identification; (3) the headline result with its welfare translation; (4) the robustness exhibit showing the welfare number is stable; (5) any heterogeneity or distributional exhibit that carries the policy implication. This sequence mirrors how the paper should read and pre-empts the referee who skims figures first. Avoid front-loading a dense regression table before the reader has seen the variation.

## Output format

```text
【Journal】Journal of Environmental Economics and Management
【Skill】jeem-tables-figures
【Lead exhibit】event study / map / RD plot / WTP density — shows identifying variation? [Y/N]
【Welfare units】damage $ / $ WTP / % capitalization present in exhibit? [Y/N]
【Uncertainty】CIs/SEs shown; stars not substituting for magnitude? [Y/N]
【Spatial honesty】projection/unit/color scale stated? [Y/N]
【Self-contained notes】sample/unit/SE/estimand in every note? [Y/N]
【Source status】verified URL / 待核实 / not asserted
【Next skill】jeem-writing-style
```
