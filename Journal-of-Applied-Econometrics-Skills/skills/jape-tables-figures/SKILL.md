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

## Self-contained and reproducible

- Each note states sample, units, estimator, inference (HAC/clustered), tuning, and what is varied.
- Figures at **highest resolution** with legends; supporting information in **separate files**.
- Every exhibit must be **regeneratable** by the master script from depositable data/code (see `jape-data-analysis`) — note where in the code each exhibit is produced.

## Output format

```
【Page budget】main text ≤ 35 pp? [Y/N]
【Split】core in text, robustness in appendix? [Y/N]
【Notes】each exhibit self-contained? [Y/N]
【Reproducible】regeneratable + code location noted? [Y/N]
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — 35-page limit and online-appendix sources
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — table/figure export tooling
