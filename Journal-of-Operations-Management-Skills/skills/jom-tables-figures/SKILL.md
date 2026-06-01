---
name: jom-tables-figures
description: Use when building or cleaning the exhibits for a Journal of Operations Management (JOM) empirical manuscript — correlation/descriptive tables, regression/SEM result tables, interaction plots, process/intervention figures — in APA-consistent, self-explanatory house style.
---

# Tables & Figures for JOM (jom-tables-figures)

## When to trigger

- Tables are cluttered, inconsistent, or not self-explanatory
- You need the standard empirical-OM exhibit set (descriptives, correlations, models)
- An interaction/contingency effect needs a readable plot
- A field/case/intervention study needs a data-structure or process figure
- You are reconciling exhibits to **APA** style for Wiley

## The empirical-OM exhibit set

A typical JOM empirical paper carries:

1. **Sample/measure table** — constructs, items, sources, reliabilities (survey) or variable definitions and data sources (archival).
2. **Descriptives & correlations** — means, SDs, full correlation matrix; reliabilities on the diagonal for survey constructs. Define every operational variable.
3. **Results tables** — nested regression / FE / SEM / count / survival models in columns, with coefficients, standard errors (note the clustering), fit/diagnostics, and N. Report effect sizes, not just significance.
4. **Interaction/contingency plot** — simple slopes with significance regions for any moderation (contingency effects are central to OM).
5. **Mechanism/process figure** — the hypothesized model; for field/case/IBR, a Gioia-style data structure or a process/intervention timeline.

## House-style rules

- **APA conventions** for tables, figures, notes, and references (JOM uses APA; Wiley applies final styling at proof). Keep formatting *consistent* — at first submission any consistent style is accepted, journal style preferred.
- Number tables/figures; give each a stand-alone title and a complete note (estimator, SE type, significance thresholds, N, units).
- Manuscript body is **double-spaced, single-column, 12-point, one-inch margins, numbered pages, no running headers/footers**; place exhibits per the author guidelines.
- Every exhibit must be readable without the text and must report the *operational* units (days, defects per million, inventory turns, on-time %).

## Self-explanation test

A reviewer should grasp each table/figure from its title, note, and labels alone. Spell out abbreviations, state the estimator and clustering in the note, and never show a coefficient without an SE and an N.

## Anti-patterns

- A correlation table with no reliabilities (survey) or undefined operational variables.
- Reporting stars but no effect sizes / operational magnitude.
- An interaction described in text but not plotted.
- Exhibits that restate the text instead of carrying evidence.
- Inconsistent citation/number style across exhibits.

## Output format

```
【Exhibit set】measures / descriptives+corr / models / interaction / mechanism
【Result table】estimator, SE clustering, effect sizes, N present? ...
【Interaction plot】simple slopes + regions? ...
【Process/data-structure figure】(field/case/IBR) ...
【APA consistency】...
【Next step】jom-writing-style
```
