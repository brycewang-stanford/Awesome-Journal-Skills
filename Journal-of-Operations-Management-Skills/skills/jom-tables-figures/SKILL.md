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

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JOM is empirical operations / supply-chain — survey and archival panel data; foreground endogeneity of operational choices and clustered / multilevel inference.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- A correlation table with no reliabilities (survey) or undefined operational variables.
- Reporting stars but no effect sizes / operational magnitude.
- An interaction described in text but not plotted.
- Exhibits that restate the text instead of carrying evidence.
- Inconsistent citation/number style across exhibits.

## Exhibit-completeness table reviewers check

Each empirical-OM exhibit has elements without which a reviewer cannot verify the claim. The map below is a practical completeness check; APA and Wiley styling specifics should be confirmed against current author guidelines.

| Exhibit | Must contain | Common reviewer complaint |
|---------|--------------|----------------------------|
| Measures/sample table | Constructs, items, sources, reliabilities (survey) or variable definitions and data sources (archival) | Operational variables left undefined |
| Descriptives + correlations | Means, SDs, full correlation matrix, reliabilities on the diagonal | No reliabilities; no operational units |
| Results table | Coefficients, SEs with clustering noted, fit/diagnostics, N, effect sizes | Stars without effect sizes or operational magnitude |
| Interaction plot | Simple slopes with significance regions | Moderation described in text but never plotted |
| Mechanism/process figure | Hypothesized model, or Gioia data structure / intervention timeline | Figure restates text instead of carrying evidence |

## Desk-reject and return triggers on exhibits

- A correlation table with no reliabilities (survey) or with undefined operational variables.
- A coefficient shown without a standard error and an N.
- Significance reported but no operational magnitude (days, defects per million, inventory turns, on-time percentage).
- Inconsistent number/citation style across tables, signaling rushed preparation.

## Worked vignette: turning a result into a self-explanatory table

A behavioral-OM experiment finds a fatigue manipulation raises order errors, more so under high time pressure (illustrative). The results table reports the main effect (b = 0.42, SE = 0.11) and the interaction (b = 0.27, SE = 0.09), with N = 180, robust SEs noted, and a partial eta-squared column so magnitude is visible. The note states the estimator, the SE type, the thresholds, and that the outcome is errors per 100 orders — an operational unit. A reader who never sees the body can still grasp the story from the title, note, and labels. The companion plot shows simple slopes with significance regions, satisfying the contingency-effect expectation native to OM.

## Exhibit objections reviewers raise, with the fix

- *"The table is not self-explanatory."* Add a complete note (estimator, SE clustering, thresholds, N, operational units) and stand-alone title so it reads without the text.
- *"You report significance but not magnitude."* Add effect sizes and translate them into operational consequences.

## Output format

```
【Exhibit set】measures / descriptives+corr / models / interaction / mechanism
【Result table】estimator, SE clustering, effect sizes, N present? ...
【Interaction plot】simple slopes + regions? ...
【Process/data-structure figure】(field/case/IBR) ...
【APA consistency】...
【Next step】jom-writing-style
```
