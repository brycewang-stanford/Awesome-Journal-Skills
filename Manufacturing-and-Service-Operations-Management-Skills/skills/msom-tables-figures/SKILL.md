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

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). M&SOM mixes analytical and empirical OM; the chain below serves the empirical-OM lane, while analytical / queueing / optimization work is outside it.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
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

## What each exhibit must earn (referee read)

At M&SOM an exhibit that does not advance the operations insight wastes page budget against the 32-page typeset cap. A policy-structure figure earns its page only when the threshold/base-stock/switching curve is *visible*, not merely stated in prose; a sensitivity exhibit must show which primitive moves the optimal decision and by how much; a numerical-study table needs a benchmark column that makes the % gap the headline; an empirical results table needs an interpretable operational magnitude with clustered SEs, not just stars; and an identification figure should make the design credible rather than duplicate a number already in a table. The default repair for over-budget exhibits is the **online supplement** — full proofs, extra experiments, and notation tables live there. (Confirm the current page and supplement limits against the journal's author guidelines.)

## Worked micro-example (illustrative)

Vignette: a base-stock model for a spare-parts network deciding stocking levels across echelons. Two exhibits carry the paper. Figure 1 plots the optimal base-stock level against lead-time variability, making visible that the level *rises convexly* — the structural insight a reader grasps at a glance. Table 2 pairs the proposed policy against a fixed safety-stock benchmark, headlining a 17% average holding-cost reduction at equal fill rate (illustrative). Figure plus benchmark-anchored table do more for the contribution than pages of extra parameter sweeps, which belong in the supplement.

## Referee-pushback patterns and the venue fix

- *"You state a threshold/base-stock result but never plot it."* → Add the policy-structure figure; M&SOM reviewers expect to see the structure, not only read it.
- *"The numerical table has no benchmark, so I can't judge the gain."* → Add the benchmark/heuristic column and make the % improvement the headline number.
- *"Exhibits push the paper over the page cap."* → Move supporting tables and proofs to the supplement; do not shrink fonts or margins against the fixed template.

## Output format

```
【Template / page budget】on official style file; pages used ...
【Analytical exhibits】policy structure / sensitivity ...
【Empirical exhibits】results / identification ...
【Self-containment & style】INFORMS author-year; notation matched ...
【Supplement】moved to ≤16-page online supplement ...
【Next step】msom-writing-style
```
