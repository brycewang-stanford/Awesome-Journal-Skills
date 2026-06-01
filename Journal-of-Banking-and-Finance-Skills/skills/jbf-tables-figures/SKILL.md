---
name: jbf-tables-figures
description: Use when preparing Journal of Banking & Finance tables and figures: descriptive statistics, regression tables, event-study plots, mechanism/heterogeneity exhibits, appendix robustness, and self-contained notes.
---

# Tables & Figures (jbf-tables-figures)

## When to trigger

- Main empirical results exist but the exhibits are hard to read
- You need JBF-ready descriptive, regression, event-study, or robustness tables
- Figure and table notes do not identify sample, fixed effects, clustering, or units

## Exhibit architecture

1. **Table 1: sample and summary statistics.** Include variable definitions,
   units, winsorization, and observation counts.
2. **Table 2: baseline results.** Build from sparse to saturated specifications
   so readers can see identifying variation.
3. **Table 3: identification checks.** Pre-trends, placebo outcomes, alternative
   fixed effects, alternative clustering, or IV first stage.
4. **Table 4: mechanisms and heterogeneity.** Tie each split to banking/finance
   theory, not to fishing.
5. **Appendix tables: robustness inventory.** Alternative samples, definitions,
   windows, and estimation methods.

## Figures that work for JBF

- Event-study coefficient plots with confidence intervals and a clear omitted period
- Sample-selection flow charts for complex merges
- Binned scatter or marginal-effect plots for nonlinear mechanisms
- Time-series plots for policy shocks, treatment timing, or market conditions

## Table notes

Every regression table note should state:

- Dependent variable and units
- Sample and period
- Fixed effects
- Clustering level
- Controls
- Treatment or event-window definition
- Stars or confidence-interval convention

## Anti-patterns

- Ten nearly identical coefficient columns with no specification logic
- Statistical significance without economic magnitude
- Appendix robustness that is impossible to map back to the main claim
- Figure axes with undefined units

## Output format

```text
[Main exhibit claim] ...
[Table/Figure role] baseline / identification / mechanism / robustness
[Required note fields] sample, FE, clustering, units, controls
[Missing diagnostics] ...
[Next step] jbf-contribution-framing or jbf-writing-style
```
