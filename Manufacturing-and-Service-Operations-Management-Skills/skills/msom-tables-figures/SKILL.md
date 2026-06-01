---
name: msom-tables-figures
description: Use when building the exhibits for a Manufacturing & Service Operations Management (M&SOM) manuscript — numerical-study tables, policy and sensitivity plots for analytical work, regression and identification tables for empirical work — in INFORMS house style and inside the official template that enforces the 32-page cap.
---

# Tables & Figures (msom-tables-figures)

## When to trigger

- Numerical-study or regression tables are cluttered or not self-explanatory
- Policy structure / comparative statics need a figure a reviewer can read at a glance
- You are fitting exhibits into the official M&SOM template and the page budget is tight
- Notation in exhibits does not match the text

## Page budget reality: exhibits count against the cap

M&SOM enforces a **hard 32-page maximum** for a new submission that **includes everything** — references, tables, graphs/figures, and appendices — measured when typeset on the official **LaTeX/Word style files** (one column, 11-pt font, 1-inch margins). Unlike narrative word-limit journals, this cap is mechanically enforced on the template, so every table and figure trades directly against text. Build in the template from the start; move bulky proofs, extra numerical experiments, and supporting tables to the **online supplement (≤ 16 pages)**.

## Analytical exhibits

- **Policy / structure figures**: plot the optimal policy form (thresholds, base-stock levels, switching curves) so the structural result is visible, not just stated.
- **Sensitivity tables/plots**: show how the optimal decision and its value move with primitives (demand variability, lead time, cost ratios); report the gap to benchmarks/heuristics.
- **Numerical-study tables**: state parameter ranges, instance counts, and what each column means; make magnitudes (% improvement, cost of an assumption) the headline.

## Empirical exhibits

- **Summary statistics** at the operational unit of analysis.
- **Main results tables** with clustered SEs noted, the operational magnitude interpretable, and specifications laid out left-to-right from baseline to robustness.
- **Identification figures**: event-study/parallel-trends plots, first-stage diagnostics, or RDD density plots.

## House style

Use **INFORMS author-year** citations in captions and notes; keep every exhibit **self-contained** (a reader should not need the text to parse it); match notation, units, and labels exactly to the manuscript. Number tables and figures as the portal/template requires.

## Checklist

- [ ] Exhibits drafted inside the official LaTeX/Word template; page budget tracked
- [ ] Bulky proofs/extra experiments moved to the ≤16-page online supplement
- [ ] Analytical: policy-structure and sensitivity exhibits make the insight visible
- [ ] Empirical: results tables show clustered SEs and operational magnitudes
- [ ] Each exhibit self-contained; notation/units match the text
- [ ] INFORMS author-year style in notes/captions

## Anti-patterns

- A wall of numerical results with no benchmark column or headline magnitude.
- Stating a threshold/base-stock result in prose but never plotting it.
- Letting exhibits push the manuscript over 32 typeset pages.
- Significance stars with no operational interpretation.

## Output format

```
【Template / page budget】on official style file; pages used ...
【Analytical exhibits】policy structure / sensitivity ...
【Empirical exhibits】results / identification ...
【Self-containment & style】INFORMS author-year; notation matched ...
【Supplement】moved to ≤16-page online supplement ...
【Next step】msom-writing-style
```
