---
name: amj-tables-figures
description: Use when building or cleaning the tables and figures for an Academy of Management Journal (AMJ) manuscript — correlation tables, regression/SEM/HLM result tables, the theoretical-model figure, and interaction plots in AOM house style. Finalizes exhibits; it does not run the analysis (amj-data-analysis) or frame the contribution (amj-contribution-framing).
---

# Tables & Figures (amj-tables-figures)

## When to trigger

- Result tables are cluttered, hard to read, or not self-explanatory
- The correlation/descriptives table is missing reliabilities or has inconsistent decimals
- Interaction effects are reported only in text, not plotted
- The theoretical model has no figure, or the figure does not match the hypotheses
- Tables/figures are off AOM house style (verify the current AMJ Style Guide for Authors)

## The exhibits an AMJ paper expects

1. **Means, SDs, and correlations** table — typically Table 1; reliabilities on the diagonal in parentheses; note significance.
2. **Main results** table(s) — regression/SEM/HLM, organized by nested models (controls → main effects → interactions), with standardized or unstandardized coefficients consistently labeled.
3. **Theoretical model figure** — boxes and arrows mapping one-to-one to the hypotheses (H1, H2, …).
4. **Interaction/simple-slopes plots** — one figure per significant interaction, with high/low moderator lines and axis labels in construct terms.
5. **Mediation/path figure** where SEM is used — coefficients on paths, fit indices noted.

## House-style discipline (verify against the current AOM Style Guide)

- **Self-contained**: a reader should understand each table/figure from its title and notes alone.
- **Title** above the table; comprehensive **note** below defines abbreviations, N, SE type, and significance markers.
- **Significance**: use consistent markers (e.g., † p<.10, * p<.05, ** p<.01, *** p<.001) and define them in the note; state whether tests are one- or two-tailed.
- **Standard errors / CIs**: report SEs (or CIs) in parentheses; be consistent across tables.
- **Decimals**: consistent precision (commonly two decimals); align on the decimal point.
- **Nested models**: report model fit / ΔR² / Δ-2LL across steps so the incremental contribution of interactions is visible.
- **Exhibits do not count toward the page limit.** AOM's 40-page main-body maximum *excludes* tables and figures (it includes text, references, and appendices), so move dense supporting material into well-built exhibits rather than crowding the prose — but keep each exhibit genuinely necessary, not padding.
- Confirm current limits on number/format of exhibits and figure resolution against the AMJ Style Guide for Authors and the ScholarOne portal.

## Figures

- Theoretical-model figure: clean boxes/arrows; label each path with its hypothesis number; no decorative clutter.
- Interaction plots: plot predicted values of the DV across the predictor at ±1 SD of the moderator; label lines; keep the y-axis in the DV's metric.
- Use grayscale-safe designs; ensure figures are legible in print and meet the resolution the portal requires.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). AMJ is empirical management — panel, multilevel, DiD, IV, and field/lab experiments; the chain below serves that lane, while grounded-theory / qualitative work uses its own standards.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Table 1 = means, SDs, correlations, with reliabilities on the diagonal
- [ ] Result tables use nested models with ΔR²/fit reported across steps
- [ ] SEs/CIs in parentheses; consistent decimals and alignment
- [ ] Significance markers defined in notes; one-/two-tailed stated
- [ ] Every significant interaction has a simple-slopes plot
- [ ] Theoretical-model figure maps one-to-one to the hypotheses
- [ ] Each exhibit is self-contained (title + complete note)
- [ ] Exhibit count/format checked against the AMJ Style Guide (tables/figures are excluded from the 40-page limit)

## Anti-patterns

- **Wall-of-numbers tables** with no nested structure and no fit statistics.
- **Undefined abbreviations** or missing N/SE-type in notes.
- **Interactions reported in text only** — reviewers expect a plot.
- **Model figure that contradicts the hypotheses** (extra/missing arrows).
- **Inconsistent decimals/significance markers** across tables.
- **Color-only figures** that are unreadable in grayscale or below required resolution.

## Output format

```
【Table 1】means/SD/correlations + reliabilities on diagonal? yes/no
【Result tables】nested models + ΔR²/fit reported? yes/no
【Interaction plots】one per significant interaction? yes/no
【Model figure】matches hypotheses one-to-one? yes/no
【Self-contained】all titles/notes complete? yes/no
【House-style check】markers/SE/decimals/resolution vs. AOM guide: pass/fix
【Next step】amj-writing-style
```
