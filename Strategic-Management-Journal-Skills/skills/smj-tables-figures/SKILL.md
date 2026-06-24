---
name: smj-tables-figures
description: Use when building or cleaning up the tables and figures of a Strategic Management Journal (SMJ) manuscript. Makes exhibits self-contained and persuasive; it does not run the analysis or write prose.
---

# Tables & Figures (smj-tables-figures)

## When to trigger

- You have many tables and are unsure which earn their place in the main text
- Tables are not self-contained (a reader cannot read them without the prose)
- You report coefficients but have no figure showing the effect or mechanism
- Descriptive statistics, correlations, and regressions are disorganized or inconsistent

## Standard SMJ exhibit set

A typical empirical SMJ paper carries a compact, predictable set of exhibits:

1. **Descriptive statistics + correlation matrix** (one table). Flag high correlations and multicollinearity concerns here.
2. **Main results table.** Hierarchical/nested models: controls-only column, then add focal X, then moderators/mechanism. Each column builds.
3. **Identification / endogeneity table.** First stage + IV, DID estimates, matching balance, or selection model — the evidence that defeats the threat.
4. **Robustness table(s).** Alternative DVs, samples, estimators.
5. **Figure(s):** marginal-effects / interaction plot, event-study plot for DID, or a mechanism/path diagram.

Move secondary tables to an online appendix/supplement rather than crowding the main text. SMJ guides authors toward a tight page budget — full articles around **40 pages** (including tables, figures, and references) and short research articles around **20 pages** (verify the current limit) — so exhibits compete for space: keep the main paper lean and use APA-style table formatting with clear notes.

## Table craft

- **Self-contained:** title states what the table shows; notes define every variable, the estimator, the sample, the unit, what stars mean, and what is in parentheses (SE vs. t). A reader should not need the prose.
- **Report standard errors** (in parentheses) and state the clustering level in the note; do not report bare stars.
- **Interaction interpretation:** never interpret an interaction from the coefficient alone — accompany it with a marginal-effects plot or computed effects at meaningful values of the moderator.
- **Consistency:** identical variable names, decimal places, and ordering across tables. Sample N should reconcile across tables (explain any drop).
- **Three-line / clean style:** no vertical rules, minimal horizontal rules; align decimals.

## Figure craft

- A **marginal-effects plot** communicates a moderation hypothesis far better than a triple-interaction coefficient.
- For DID, an **event-study figure** (pre-trends flat, effect emerging post-treatment) is often the single most persuasive exhibit.
- A **mechanism/path figure** can summarize the theorized model; keep it conceptual, not decorative.
- Greyscale-legible (SMJ is widely printed/read in B&W); label axes and units; no chartjunk.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). SMJ is strategy — firm-level panels where strategic choices are endogenous; foreground IV / DiD identification and the endogeneity-of-strategy objection.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Each main-text table is self-contained (title + complete notes)
- [ ] Standard errors shown; clustering level stated in the note
- [ ] Main results presented as nested/hierarchical columns that build
- [ ] An identification/endogeneity exhibit is present and prominent
- [ ] Interactions are visualized (marginal-effects plot), not read off coefficients
- [ ] Variable names, decimals, ordering consistent across all exhibits; N reconciles
- [ ] Secondary tables moved to the appendix/supplement (main paper within the ~40-page / ~20-page budget)
- [ ] Coefficients interpretable as economic magnitudes, not bare stars
- [ ] Figures are greyscale-legible with labeled axes

## Anti-patterns

- A table that cannot be read without the surrounding text
- Reporting only significance stars with no standard errors or clustering note
- Interpreting an interaction term's sign without a marginal-effects plot
- Eight near-identical robustness tables in the main text
- Inconsistent N or variable naming across tables
- A color-only figure that becomes unreadable in print
- DID with no event-study/pre-trends figure

## Output format

```
【Main-text exhibits】[descriptives, main results, identification, robustness, figure(s)]
【Self-contained?】yes / fix: [...]
【SE + clustering noted】yes / fix
【Interaction visualized】yes / needs marginal-effects plot
【Event-study figure (if DID)】present / missing
【Appendix moves】[tables relocated]
【Within page budget (~40 / ~20)】yes / trim
【Next step】smj-writing-style
```

## Templates & resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — table/figure tooling (estout/esttab, modelsummary, coefplot, marginsplot, ggplot2)
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — SMJ formatting, APA reference style, and page-limit guidance
