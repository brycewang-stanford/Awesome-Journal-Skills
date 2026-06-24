---
name: joe-tables-figures
description: Use when building the Monte Carlo tables and theory-illustrating figures for a Journal of Econometrics (JoE) manuscript. Covers size/power table conventions, estimator-comparison layout, and figures that make asymptotic and finite-sample behavior legible.
---

# Tables & Figures (joe-tables-figures)

## When to trigger

- Monte Carlo results exist but the tables are dense, unlabeled, or hard to compare across methods
- Size and power are mixed into one block so distortion is invisible
- Figures show output but not the *behavior* the theorems predict (rates, coverage, distributions)
- You are formatting exhibits for a PDF-only initial submission and want them print-legible

## What JoE exhibits must do

At the *Journal of Econometrics* the exhibits are the **empirical backbone of a methods paper**: they have to let a referee verify, at a glance, that the estimator is well-behaved and the test controls size. Initial submission is a **single PDF** (~40 pages, ≥1.5 spacing, 11pt), so tables and figures must be readable inline at that density; structured formatting and source files are handled at revision/acceptance. Build self-contained exhibits whose notes state the DGP, sample sizes, replication count, and nominal level.

## Monte Carlo table conventions

- **Separate size from power.** Report **empirical size at nominal 5%/10%** in its own panel; report **size-adjusted power** separately so a size-distorted test cannot masquerade as powerful.
- **One method per column (or panel), one DGP/$n$ per row block.** The reader should compare your method to the nearest competitor down a column without hunting.
- Report **bias, RMSE, and CI coverage** for estimators; mark the best in each row if it aids reading.
- **Notes are mandatory:** DGP description, error distribution, dependence structure, $n$, replication count, and any tuning values. A referee should reproduce the table's meaning from the note alone.
- Keep decimal places consistent; do not over-report precision that the replication count cannot support.

## Figures that illustrate theory

- **Size/power curves** across the parameter; **coverage vs. $n$** to show asymptotics kicking in; **QQ plots or densities** of the standardized statistic against its limiting distribution.
- **Sensitivity plots** over tuning parameters (bandwidth, lag length, penalty) to show robustness.
- Plot **confidence bands / Monte Carlo error**; avoid chartjunk (no 3D, minimal color, legible at print size).
- Use **vector output (PDF/EPS)** so exhibits stay crisp; ensure they survive grayscale printing.

## Formatting notes

- Number tables and figures, call them out in order, and give each a self-contained caption.
- Math in captions/notes in LaTeX via the **elsarticle** class for consistency with the manuscript.
- At submission everything lives in the single PDF; keep source and high-res files staged for acceptance.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Journal of Econometrics is a methods venue — estimator validity + simulation evidence are the contribution; pair estimates with diagnostics and Monte-Carlo where relevant.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- A 12-column table with no row/column grouping and no notes
- Power reported without empirical size (size-distorted power is meaningless)
- Tuning-parameter sensitivity omitted, hiding fragility
- Figures with default software styling, illegible in grayscale, or missing Monte Carlo error
- Over-precise decimals implying accuracy the replication count cannot deliver

## Output format

```
【Size table】separate panel, nominal 5%/10%? [Y/N]
【Power table】size-adjusted, vs. nearest method? [Y/N]
【Estimator table】bias / RMSE / coverage? [Y/N]
【Notes】DGP / n / reps / tuning stated? [Y/N]
【Theory figures】coverage-vs-n / power curves / limiting-dist check? [list]
【Print quality】vector, grayscale-safe, legible in single PDF? [Y/N]
【Next step】joe-writing-style
```
