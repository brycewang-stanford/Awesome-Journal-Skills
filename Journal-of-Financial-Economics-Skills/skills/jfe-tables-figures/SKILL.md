---
name: jfe-tables-figures
description: Use when the exhibits of a Journal of Financial Economics (JFE) manuscript need to meet house standards — readable tables, self-contained notes, and figures that carry the argument. Handles exhibit craft; it does not decide which robustness tests to run (jfe-robustness).
---

# Tables & Figures (jfe-tables-figures)

## When to trigger

- A main table has so many columns no reader can parse it
- Table notes do not let a reader understand the table without the text
- Standard errors / t-stats are reported inconsistently across tables
- Figures are decorative rather than carrying part of the argument
- You are deciding what stays in the main text vs. the Internet Appendix

## JFE exhibit standards

JFE tables are dense but disciplined. Each main exhibit should make one clear point and be self-contained: a reader should grasp it from the title, column headers, and notes alone. Because JFE papers are long and robustness-heavy, ruthless triage between main-text and Internet-Appendix exhibits is part of the craft. The overflow goes to the online appendix that JFE asks you to **append to the end of the main manuscript file** (see jfe-internet-appendix). Manuscripts are submitted **double-spaced, 12-pt+, with >= 1-inch margins**, so dense tables must still read at that scale. Verify current formatting on jfinec.com.

## Table craft

### Structure
- One exhibit, one message. If a table answers two questions, split it.
- Order columns from baseline to richest specification, left to right.
- Group related rows; keep the variable of interest visually prominent (top rows).

### Reporting conventions
- Report coefficients with standard errors (or t-statistics) in parentheses — pick one convention and use it everywhere.
- State the significance-star convention once and apply consistently.
- Always report N, R-squared (or relevant fit), fixed effects included, and the cluster level — in the table, not only the text.
- Report economic magnitudes alongside coefficients where readers need them.

### Notes
- The note states: sample and period, variable definitions (or a pointer to the definition table), the standard-error treatment, and what each star means.
- Notes should make the table replicable in spirit without flipping back to the text.

## Figure craft

- Event-study/coefficient plots should show confidence bands and the zero line.
- Label axes with units; no unexplained acronyms.
- Use figures where a pattern (pre-trends, a discontinuity, a return path) is clearer than a table — not as decoration.
- Keep them legible in grayscale; do not rely on color alone to distinguish series.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JFE is finance top-3 (with JF, RFS) — corporate-causal chain for corporate papers, factor-zoo haircut for asset pricing; attribute canon to the correct top-3 journal.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Each main table makes one clear point
- [ ] SE/t-stat convention and star convention are consistent across all tables
- [ ] Every table reports N, fit, fixed effects, and cluster level
- [ ] Economic magnitudes shown where interpretation requires them
- [ ] Table notes are self-contained (sample, definitions, SEs, stars)
- [ ] Figures carry argument, have CI bands/units, and work in grayscale
- [ ] Exhibits are legible at double-spaced, 12-pt+ submission formatting
- [ ] Main-text vs. Internet-Appendix exhibit split is deliberate; overflow appended to the main file
- [ ] Every table/figure is reproducible from the Mendeley Data code deposit

## Anti-patterns

- A 12-column main table that no referee will read
- Parentheses that mean SEs in one table and t-stats in another
- Omitting the cluster level or fixed-effects rows from the table
- Three-decimal coefficients with no sense of economic size
- Figures that repeat a table without adding clarity
- Color-only series distinctions that vanish in print

## Output format

```
【Main exhibits】list, each with its one message
【Reporting convention】SEs|t-stats ; star scheme
【Per-table footer fields】N / fit / FE / cluster present? yes/no
【Figures】[purpose of each]
【Moved to appendix】[exhibits relocated]
【Next】jfe-internet-appendix
```
