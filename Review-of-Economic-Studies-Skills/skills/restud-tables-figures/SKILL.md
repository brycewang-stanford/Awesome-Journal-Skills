---
name: restud-tables-figures
description: Use when the exhibits in a The Review of Economic Studies (REStud) manuscript need to be made publication-grade — regression tables that are oversized or footnote-bloated, or figures that do not carry the result. Finalizes exhibits to REStud house standard; does not run the underlying analysis.
---

# REStud Tables & Figures (restud-tables-figures)

## When to trigger

- A main table has more columns than a reader can hold in mind (≳ 6)
- Tables carry default software output (stars only, no economic-magnitude reading)
- The central result is buried in a table when a figure would carry it
- Figures are raster (PNG) rather than vector, or lack a self-contained notes block
- Notation, units, or sample counts are inconsistent across exhibits

## REStud exhibit principles

REStud values **elegance and economy**, and that extends to exhibits. Two REStud-specific facts: (1) auxiliary exhibits go in the **online appendix**, so the main-text figure budget is tight — promote only the exhibits that carry the contribution; (2) every published exhibit must map to a line in the deposited code, because the **Data Editor regenerates tables and figures from your replication package before publication** (AEA DCAS check; see `restud-replication-package`) — so script your exhibits, never hand-edit them. The standard:

- **Each exhibit carries one result.** If a table is doing two jobs, split it.
- **The reader can read the magnitude, not just the stars.** State units; an effect of "0.034***" is meaningless until the reader knows 0.034 *of what*.
- **Figures are first-class.** A striking new fact is often best shown as a figure (event-study plot, binscatter, RD plot, model-vs-data overlay). For a new-fact paper, the headline figure may matter more than any table.
- **Self-contained notes.** Every table and figure has a notes block stating sample, period, unit of observation, fixed effects, standard-error clustering, and significance convention — readable without the main text.

## Tables

- Use professional rules (booktabs `\toprule` / `\midrule` / `\bottomrule`); no vertical rules, no double horizontal rules.
- Report coefficient, standard error (in parentheses), and N; add the dependent-variable mean so magnitudes are interpretable.
- Group columns by specification with clear panel headers; indicate fixed effects with a Yes/No block at the foot, not buried in notes.
- Significance: report SEs and let the reader judge; if stars are used, define them once and consistently.
- Generate from code (`estout`/`esttab`, `etable`, `modelsummary`) so the table regenerates with the result — no hand-typed numbers.

## Figures

- **Vector format** (PDF / EPS) — never raster for line art.
- Confidence bands on every event-study / RD / dose-response plot.
- Axis labels with units; legend inside the plot area or a one-line caption; no chartjunk, no 3-D, no gradient fills.
- For a new-fact paper, lead with the figure that *is* the fact.
- Color must survive grayscale printing; distinguish series by marker/line style as well as hue.

## Theory exhibits

For theory and theory-with-empirics papers, exhibits earn their place too:

- A figure of the model's key mechanism (best-response curves, a phase diagram, the comparative-static frontier) can carry a proposition better than the algebra.
- A **model-vs-data overlay** is among the most persuasive REStud exhibits: plot the model's prediction against the empirical moments it was not fit to match.
- Numerical illustrations and calibrated simulations belong in a clearly labeled figure with the parameter values in the notes or the online appendix.

## Consistency pass

Before finalizing, run one pass across all exhibits together (not one at a time):

- Variable names, units, and sample sizes match across every table and figure.
- The same coefficient reported in two places shows the same number to the same precision.
- Numbering is continuous and every exhibit is referenced in the text in order.

Inconsistent exhibits are a fragility signal — referees who spot a mismatched N start doubting the rest.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). REStud is top-5 general-interest economics; credible identification with modern estimators is the bar across applied fields.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Each exhibit carries exactly one result
- [ ] Main table ≤ ~6 columns; longer variants moved to the appendix
- [ ] Dependent-variable mean (or comparable scale) reported for magnitude reading
- [ ] FE / clustering / sample shown in a foot block or self-contained notes
- [ ] Figures are vector; event-study/RD plots show confidence bands
- [ ] Exhibits regenerate from code — no hand-typed numbers
- [ ] Notation, units, and N consistent across all exhibits

## Anti-patterns

- A 14-column table with no headline takeaway
- Reporting only stars, so the economic magnitude is unreadable
- Raster figures that pixelate in the typeset PDF
- Notes that say "see text" instead of being self-contained
- Burying the paper's striking fact in a table when a figure would make it obvious
- Inconsistent variable names or sample sizes across tables (a fragility signal to referees)

## Output format

```
【MAIN EXHIBITS】[table/figure — the one result each carries]
【MAGNITUDE READABLE】yes / no — scale reported
【FORMAT】booktabs tables / vector figures — confirmed
【NOTES SELF-CONTAINED】yes / no
【HEADLINE FIGURE】<which exhibit is the paper's "face">
【NEXT SKILL】restud-writing-style
```
