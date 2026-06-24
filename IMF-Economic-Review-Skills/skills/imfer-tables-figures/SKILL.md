---
name: imfer-tables-figures
description: Use when an IMF Economic Review (IMFER) manuscript's exhibits must communicate an international-macro result to a dual academic/policy audience — transparent country coverage, readable cross-country panels, no significance asterisks. Builds the exhibits; it does not run the robustness behind them (imfer-robustness) or write the prose (imfer-writing-style).
---

# Tables and Figures (imfer-tables-figures)

## When to trigger

- A cross-country regression table is dense and the reader cannot find the headline coefficient
- Country/sample coverage is buried — a referee cannot tell which economies and years are in
- Impulse responses, event-study leads, or spillover paths need a figure that a policymaker can read at a glance
- Significance asterisks are still on the tables, or SEs/CIs are missing
- A map or panel-by-country exhibit would communicate the international margin better than a table
- A summary-statistics table omits the cross-country dispersion a referee needs to judge the sample

## What IMFER exhibits must do

IMFER exhibits serve two readers at once: a referee checking the econometrics and a policy reader who wants the magnitude and its country scope. So the **country coverage must be transparent** (which economies, which years, balanced or not), the **headline number must be findable**, and the **uncertainty must be visible as standard errors and confidence intervals — not asterisks**. The best IMFER figure is one that could appear in a WEO/GFSR chart pack *and* survive referee scrutiny: clear axis units, sample noted, mechanism legible.

| Exhibit job | The right form | Watch for |
|-------------|----------------|-----------|
| Show the headline cross-country effect | a compact main table, preferred spec first | not a 12-column kitchen sink |
| Show country/sample coverage | a coverage table or a map; note balanced/unbalanced | hidden sample; undated coverage |
| Show dynamics (spillover, IRF) | a line figure with CI bands | bands omitted; ambiguous units |
| Show a DID/event study | event-time plot with leads and lags | no pre-period leads shown |
| Show heterogeneity (AE vs EM) | split panels or a coefficient plot | a wall of subgroup rows |
| Show a policy magnitude | units a policymaker uses (% of GDP, bps) | raw coefficients with no economic scale |

## Exhibit craft

0. **The summary-statistics table earns its keep.** For a cross-country paper this is not boilerplate: report the dispersion across countries (not just the pooled mean), the coverage by income group, and the key conventions (currency, gross/net) so a referee can judge whether the sample supports the claim before reading a single regression.
1. **One headline exhibit.** Decide the single table or figure that *is* the paper; make it self-contained — a reader who sees only it should grasp the result, the sample, and the uncertainty.
2. **Make country coverage explicit.** State the economies and years in the note; if the panel is unbalanced, say so; a coverage table or map pre-empts the "which countries?" referee question.
3. **No asterisks.** Report standard errors (or CIs); for the headline, prefer a confidence interval so the policy reader sees the range, not a star.
4. **Put magnitudes in policy units.** Translate coefficients into % of GDP, basis points, or a number a mission economist would quote.
5. **Show dynamics with bands.** Spillover paths and IRFs need confidence bands and labeled horizons; event studies need visible pre-trend leads.
6. **Self-contained notes.** Estimator, sample, clustering, and units in the note — the exhibit should not require the text to be intelligible.

### Country panels: the recurring exhibit problems
Cross-country exhibits fail in patterned ways. **Heterogeneous scale**: a few large economies dominate any pooled scatter — log, normalize by GDP, or facet by income group. **Unbalanced coverage masked**: a table reporting "N = 1,200" hides that half the cells are one decade; show coverage by country-year. **Currency and vintage drift**: a figure mixing USD and local-currency series, or two data vintages, misleads; state the convention in the note. **Map theatrics**: a choropleth that colors countries but encodes no number the argument uses is decoration — prefer it only when the geographic pattern *is* the finding (contagion, regional clustering). The fix is always the same: make the cross-country comparison the reader needs explicit and quantitative.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). IMFER is international macro/finance; cross-country panels with confounded policy — emphasize identification and clustering.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] One self-contained headline exhibit; preferred specification first
- [ ] Summary-statistics table shows cross-country dispersion and coverage by income group
- [ ] Country and year coverage stated; balanced/unbalanced noted (coverage table or map if helpful)
- [ ] No significance asterisks; SEs or CIs reported, CI preferred for the headline
- [ ] Magnitudes in policy-readable units (% of GDP, bps), not bare coefficients
- [ ] Dynamics (IRF / spillover / event study) shown with CI bands and labeled horizons
- [ ] Event studies show pre-period leads; heterogeneity shown as panels/coefficient plots not row walls
- [ ] Currency / gross-net / deflator convention stated in every relevant note
- [ ] Large economies do not dominate any pooled scatter (log scale / GDP normalization used)
- [ ] Notes carry estimator, sample, clustering, units — exhibit readable on its own

## Anti-patterns

- A 12-column regression table where the headline coefficient is impossible to locate
- Asterisks/boldface for significance instead of SEs/CIs
- Country coverage hidden — the reader cannot tell which economies or years are in
- Coefficients reported with no economic scale a policymaker could use
- IRFs / spillover paths with no confidence bands
- An event-study figure with no pre-period leads (parallel-trends evidence missing)
- A choropleth map that looks impressive but encodes no quantitative comparison the text uses
- A pooled scatter dominated by a few large economies, with no log scale or GDP normalization
- A summary table reporting only pooled means, hiding the cross-country dispersion
- Exhibit notes that omit the estimator, clustering, or units, forcing the reader back to the text

## Worked vignette (illustrative)

A spillover paper's first draft has a 10-column table of US-shock coefficients across outcomes, asterisked, with the sample described only as "47 countries." The IMFER revision keeps the preferred column as Table 1 with the elasticity translated to "−0.8% of GDP per 100bp" and a 95% CI in the cell; a coverage table lists the 47 economies, the 1996–2023 window, and the unbalanced cells; and the dynamics move to a figure of the impulse response with bands over 12 quarters, AE and EM panels side by side. A referee can now verify the econometrics and a mission economist can quote the magnitude — both from the exhibits alone.

## Referee pushback mapped to the exhibit fix

- *"Which countries and years are in this panel?"* → Add a coverage table or map and note balanced/unbalanced in every exhibit footnote.
- *"What does this coefficient mean economically?"* → Report the magnitude in % of GDP or basis points alongside the raw coefficient.
- *"Drop the asterisks."* → Replace stars with standard errors and, for the headline, a confidence interval.

## Output format

```text
【Journal】IMF Economic Review
【Skill】imfer-tables-figures
【Headline exhibit】table/figure that IS the paper: ___
【Country coverage】economies + years + balanced?: ___
【Uncertainty】SEs / CIs (no asterisks)? [Y/N]
【Policy units】magnitude in % of GDP / bps: ___
【Dynamics】IRF/spillover/event-study with bands? [Y/N]
【Next skill】imfer-writing-style
```
