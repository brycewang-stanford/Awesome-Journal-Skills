---
name: qje-tables-figures
description: Use when finalizing the main exhibits of a Quarterly Journal of Economics (QJE) manuscript — making the paper figure-forward, with clean tables and self-contained notes that read well in QJE's single-PDF, author-date format. Designs exhibits; it does not run new analysis.
---

# Tables & Figures (qje-tables-figures)

## When to trigger

- The main result is a dense table with too many columns
- The paper is "table-heavy" when the design would land better as a figure
- Table notes are incomplete (sample, units, clustering, significance unclear)
- An event-study / RDD / binscatter result is hidden in a table instead of plotted

## QJE aesthetic: figure-forward, self-contained exhibits

QJE has moved firmly toward **figure-forward presentation** — the Opportunity Insights / Chetty-style QJE paper makes its central result legible in one well-designed graph (e.g., the binned mobility maps and exposure-effect plots of the QJE 2014/2018 neighborhoods papers). Identification designs are inherently visual: event-study plots, RDD discontinuity plots, and binned scatters communicate credibility better than a coefficient buried in a regression column. Tables remain essential for estimates and robustness, but the *headline* should often be a figure a reader grasps in five seconds. Practical QJE constraints: at initial submission **everything is one PDF with figures embedded** (no separate figure files), exhibits are numbered and called out in order, and in-text references are **author-date (Chicago)**.

## The headline-figure decision

| Design          | Headline figure                                              |
|-----------------|--------------------------------------------------------------|
| DID / event std | Event-study plot: leads ≈ 0, clean post-treatment dynamics   |
| RDD             | Discontinuity plot: binned means + local polynomial fit      |
| IV              | First-stage and reduced-form scatter / binscatter            |
| RCT             | Treatment-vs-control outcome distributions or effect-by-arm  |
| Descriptive     | The new fact, plotted with the data doing the talking        |

## Table craft

- **Width discipline.** Main results table should be readable; if it sprawls past a handful of columns, split it or move variants to the appendix (no page limit means you can — but readability still wins).
- **Self-contained notes.** Every table/figure note states: sample and time span, unit of observation, what each column is, fixed effects included, standard-error clustering level, and how significance is denoted.
- **Standard errors in parentheses**, clustering level named in the note; report N and relevant fit statistics.
- **Coefficients with meaning.** Report units so the magnitude is interpretable (effect in SDs, in dollars, in percentage points), not just a bare number.
- Author-date (Chicago) in-text references; figures and tables numbered and called out in order.

## Figure craft

- Show the data: binned scatters, confidence bands, and raw-ish patterns build credibility.
- Avoid chartjunk: no 3D, no needless color, legible axis labels with units; figures must remain legible embedded in the single submission PDF and at print resolution.
- Confidence intervals shown, not just point estimates; bandwidth/bin choices noted.
- A figure should be interpretable from its caption alone.

## Checklist

- [ ] The central result has a headline figure a reader grasps quickly
- [ ] Main table is readable; sprawling variants moved to the appendix
- [ ] Every exhibit note is self-contained (sample, units, FE, clustering, significance)
- [ ] Magnitudes are interpretable (units stated), not bare coefficients
- [ ] Event-study / RDD / first-stage results are plotted, not only tabulated
- [ ] Confidence intervals / bands shown on figures
- [ ] Figures embedded and legible in the single submission PDF; numbered, author-date citations

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result rather than retyping numbers (the usual source
of body-vs-appendix drift). Full map:
[`shared-resources/empirical-methods/execution-with-mcp.md`](../../../shared-resources/empirical-methods/execution-with-mcp.md).

- **Tables:** `etable` (multi-column) or `did_summary_to_latex` straight from the
  `result_id` — one definition, one set of numbers, body and appendix in sync.
- **Event-study / coefficient figures:** `plot_from_result`, `enhanced_event_study_plot`,
  `event_study_table` — axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering (from the result's diagnostics) and
  states the magnitude in interpretable units. See a full fitted-result → exhibit chain
  in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).

## Anti-patterns

- A 9-column main table when a single event-study figure would carry the result
- Table notes that omit the clustering level or the sample definition
- Reporting coefficients with no units, so magnitude is uninterpretable
- Decorative 3D/colored charts that add no information
- Burying the cleanest evidence (the discontinuity, the leads) in an appendix table

## Output format

```
【Headline exhibit】figure type chosen + why
【Main table】column count + what moved to appendix
【Notes audit】sample / units / FE / clustering / significance present? [Y/N each]
【Magnitude legibility】units stated? [Y/N]
【Figures plotted】[event study / RDD / first stage / ...]
【Next step】qje-writing-style
```
