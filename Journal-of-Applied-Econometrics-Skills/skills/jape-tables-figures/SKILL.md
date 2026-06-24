---
name: jape-tables-figures
description: Use when building tables and figures for a Journal of Applied Econometrics (JAE) manuscript under the hard 35-page article limit — keeping core exhibits in the main text while pushing extended results into the unlimited online appendix, and ensuring every exhibit is regeneratable for the JAE Data Archive.
---

# Tables & Figures for JAE (jape-tables-figures)

## When to trigger

- Deciding which exhibits belong in the main text vs. the online appendix
- Fitting the paper within JAE's 35-page article limit
- Making figures/tables submission- and archive-ready

## The page budget drives exhibit choices

JAE imposes a **hard 35-page limit on the main article**, but **online appendices / supporting information do not count toward it and have no length restriction**. Split deliberately:

- **Main text (≤ 35 pp):** only the exhibits carrying the core applied-econometric lesson — typically a compact descriptive table, the main estimates, and one or two figures that make the finding visible. Show the lesson, not every intermediate specification.
- **Online appendix (unlimited):** full robustness grids, alternative specifications, every diagnostic, additional samples, large supplementary tables. A lean main text + rich appendix is the intended pattern, not a weakness.

## Use figures where they beat tables

Reach for a figure when a table obscures the point: finite-sample patterns, forecast performance, impulse responses, or diagnostic behavior over a tuning parameter.

## Exhibit triage

Classify every exhibit before typesetting:

- **Main evidence**: directly answers the applied question or changes the headline conclusion.
- **Method diagnostic**: explains why the estimator, inference procedure, forecast comparison, or
  simulation design is credible.
- **Robustness support**: protects the result but is not needed for first-pass understanding.
- **Archive-only detail**: required for reproduction, but too mechanical for the article or appendix prose.

Main evidence and one diagnostic usually belong in the article. Robustness support belongs in the online
appendix unless it reverses interpretation. Archive-only detail belongs in the README/code outputs, with
clear pointers from the appendix.

## Self-contained and reproducible

- Each note states sample, units, estimator, inference (HAC/clustered), tuning, and what is varied.
- Figures at **highest resolution** with legends; supporting information in **separate files**.
- Every exhibit must be **regeneratable** by the master script from depositable data/code (see `jape-data-analysis`) — note where in the code each exhibit is produced.

## Anatomy of a JAE estimates table

Referees at this venue read the inference rows before the coefficients. A main-results table should carry, per column: the estimate with its standard error; *which* standard error (HAC with stated bandwidth, cluster-robust with the cluster count, wild-bootstrap p-value with replications); N and sample span; first-stage effective F for any IV column; and fixed effects / controls flags. The note then names the deposited program that rebuilds the table. A table whose note cannot answer "clustered on what, how many clusters?" invites the first referee objection at JAE.

## Worked exhibit budget under 35 pages (illustrative)

A staggered-policy panel paper with 23 candidate exhibits. Triage: main text gets a descriptive table, the headline estimates table (with CRVE and wild-bootstrap p-values side by side), one event-study figure, one heterogeneity table, and one diagnostic figure — 5 exhibits, ~9 pages of floats, leaving ~26 for prose within the limit. The online appendix takes the other 18: full robustness grids, alternative estimators, pre-trend variants, simulation tables. Two exhibits turn out to be archive-only (instrument-construction intermediates): they live as CSVs in the deposit, pointed to from the readme, not typeset at all.

## Exhibit pushback and the archive answer

- "Where is the specification with X?" → it exists in appendix Table C4 *and* as a one-flag rerun of the deposited master script — say both in the response.
- "The figure looks cherry-picked over bandwidths" → replace with a sensitivity curve over the full grid; archive the grid CSV.
- "I cannot match Figure 2 to any number in the text" → add the point estimates to the figure note and name the generating program.
- "Too many tables to follow" → consolidate to one table per claim; JAE's lean-text/rich-appendix design is the escape valve, use it.

## Table-note template

```text
Notes: Sample [span, N]. Estimator: [e.g., 2SLS]. Standard errors:
[HAC, Bartlett, lag L / clustered by state, G = 13 / wild cluster
bootstrap, Webb weights, 9,999 reps, seed in README]. First-stage
effective F = [value] (IV columns). *, **, *** : 10/5/1%.
Reproduce: programs/table3.do in the JAE Data Archive package.
```

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
## Output format

```
【Page budget】main text ≤ 35 pp? [Y/N]
【Split】core in text, robustness in appendix? [Y/N]
【Inference rows】SE type, cluster count, F where relevant? [Y/N]
【Notes】each exhibit self-contained? [Y/N]
【Reproducible】regeneratable + code location noted? [Y/N]
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — 35-page limit and online-appendix sources
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — table/figure export tooling
