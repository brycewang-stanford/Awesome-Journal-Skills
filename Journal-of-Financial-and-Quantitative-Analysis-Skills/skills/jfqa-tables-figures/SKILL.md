---
name: jfqa-tables-figures
description: Build the tables and figures for a Journal of Financial and Quantitative Analysis (JFQA) paper — summary statistics, main regressions, robustness, and finance-standard exhibits with self-contained notes that state sample, clustering, winsorizing, and economic magnitudes. Use to make exhibits readable under double-anonymous review and consistent with JFQA formatting.
---

# JFQA Tables & Figures (jfqa-tables-figures)

Use this skill to design exhibits for a **JFQA** manuscript so a reviewer can read each one standalone and so the file complies with the journal's prescriptive formatting.

## Standard finance exhibit set

- **Table 1 — Summary statistics**: variable definitions, N, means, SDs, key percentiles; note winsorizing/trimming.
- **Correlation matrix** where relevant.
- **Main results table**: the core regressions/sorts, with coefficients, SEs, the clustering dimension, fixed effects listed, and N.
- **Robustness tables**: alternative samples, definitions, FE/clustering.
- **Heterogeneity / mechanism tables**.
- **Figures**: event-study coefficient plots, portfolio-sort patterns, RDD discontinuity plots, time-series of the key series.

## Self-contained notes (required discipline)

Each table/figure note must state: sample and period, unit of observation, what is winsorized, the SE/clustering choice, fixed effects, and how to read the magnitude. A reviewer should not need the text to interpret the exhibit.

## Presentation standards

- Report **economic magnitudes**, not only significance stars; finance referees want effect sizes (bps, monthly alpha, elasticities).
- Number tables/figures and call them out in order.
- Keep figures clean (vector output, legible at print resolution, no chartjunk).

## Formatting compliance

JFQA submissions use **8.5 × 11 paper, 1-inch margins, 12-pt Times New Roman, double-spaced** (body and appendices), in a single **text-searchable PDF**. Ensure embedded exhibits stay legible at these settings and that the PDF remains searchable (no image-only tables).

## Anti-patterns

- Tables that require the text to interpret.
- Significance stars with no economic magnitude.
- Undisclosed winsorizing or an unstated clustering choice.
- Image-only exhibits that break the text-searchable-PDF requirement.

## Output format

```
【Exhibit list】Table 1...N, Figure 1...M with one-line purpose each
【Notes】each states sample / clustering / winsor / magnitude
【Formatting】fits 8.5x11 / 1-in / 12-pt TNR, PDF searchable
【Next step】jfqa-writing-style
```
