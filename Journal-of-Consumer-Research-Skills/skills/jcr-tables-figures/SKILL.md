---
name: jcr-tables-figures
description: Use when building the exhibits for a Journal of Consumer Research (JCR) manuscript — study-summary tables, mediation/moderation results, interaction and spotlight plots, conceptual/process figures, and CCT data displays — in Chicago house style, mindful of the 60-page embedding rule and the web appendix. Late-stage polish; settle the contribution first (jcr-contribution-framing).
---

# Tables & Figures (jcr-tables-figures)

## When to trigger

- Exhibits are cluttered, inconsistent, or not self-explanatory
- You need a clear way to summarize a multi-study experimental package
- An interaction or mediation result needs a readable plot
- You are deciding what stays in the manuscript vs. the web appendix

## Remember the JCR page-counting convention

JCR caps the manuscript at **60 double-spaced pages**, and crucially **tables and figures are embedded and count toward that cap** (the cap covers title, abstract, main text with tables/figures embedded, appendices, and references). So exhibits are not "free" the way they are at venues that exclude them — design them to **earn their space**. Move overflow stimuli, full instruments, additional study tables, and supplementary plots to the **web appendix** (max 40 MB), which is distinct from a manuscript appendix and does **not** count toward the cap.

## Exhibits for the experimental package

- **Study-summary table:** one row per study with design, manipulation, key DV, N, and the result — lets reviewers see the convergent multi-study logic at a glance.
- **Means/cells:** report condition means with SDs and Ns; show the predicted pattern clearly.
- **Mediation:** present indirect effects with **bootstrap confidence intervals**; a path diagram with coefficients aids comprehension.
- **Moderation:** plot **simple slopes**; for continuous moderators show the **spotlight/floodlight** result (Johnson-Neyman region) rather than a bar chart of a median split.
- **Process figure:** a clean conceptual/process model (IV → mediator → DV, with moderators) orients the interdisciplinary reader.

## Exhibits for interpretive / CCT work

- **Data-structure or thematic display:** show the path from raw data (quotations/observations) to second-order constructs and the conceptual framework.
- **Representative evidence table:** illustrative quotations mapped to constructs, supporting the audit trail.
- Keep displays interpretive and legible to readers who do not work in CCT.

## House style and consistency

- Follow the JCR style guide; for anything it does not cover, JCR defaults to the **Chicago Manual of Style** (including title capitalization). Configure exhibit titles and notes accordingly.
- Each exhibit must be **self-contained**: title, units, N, significance notation, and a note defining abbreviations.
- Keep construct names, hypothesis labels, and study numbers identical between text and exhibits.
- Anonymize exhibits for double-anonymized review (no author-identifying file names, site names, or institution tells).

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JCR is predominantly lab experiments; randomization-based inference and the many-outcome family-wise correction (`romano_wolf`) are the decisive tools.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Each exhibit is self-explanatory (title, N, units, notes)
- [ ] Multi-study package summarized in one table
- [ ] Mediation shown with bootstrap CIs; moderation via simple slopes / spotlight
- [ ] A clean process/conceptual figure is included (experiments)
- [ ] CCT: data-structure / representative-evidence displays included
- [ ] Chicago-style titles/notes; labels consistent with the text
- [ ] Exhibits earn their space under the 60-page embedded cap; overflow in the web appendix
- [ ] Exhibits anonymized for masked review

## Anti-patterns

- Median-split bar charts standing in for a spotlight analysis.
- Tables that repeat the text instead of compressing it.
- Exhibits that silently break anonymization (site/institution names).
- Padding the manuscript with figures that should live in the web appendix.
- Inconsistent labels between text, tables, and figures.

## Output format

```
【Study-summary table】drafted? rows = studies
【Mediation/Moderation exhibits】bootstrap CI / simple slopes / spotlight: yes/no
【Process or CCT framework figure】included?
【Page-budget】embedded exhibits justified; overflow → web appendix
【House style】Chicago titles/notes; labels consistent; anonymized
【Next step】jcr-writing-style
```
