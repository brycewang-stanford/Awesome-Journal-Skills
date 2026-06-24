---
name: cps-tables-figures
description: Use when designing tables and figures for a Comparative Political Studies (CPS) manuscript so each exhibit is self-contained, comparative-legible, and SAGE-ready. Improves the exhibits; it does not run the analysis or set the data policy.
---

# Tables & Figures (cps-tables-figures)

CPS exhibits must carry the comparative argument on their own. A reviewer should grasp the cross-case or
over-time story from the figure and its caption without hunting through the text. Because references,
tables, and figures do **not** count toward the CPS word limit, exhibits are where you spend space —
but only if each one earns its place.

## When to trigger

- Building or revising the main-text tables and figures
- A reviewer found exhibits unreadable, over-stuffed, or not self-contained
- Deciding which exhibits belong in the paper vs. the supplementary/online appendix
- Preparing figures for SAGE production (color, resolution, grayscale legibility)

## Exhibit priorities (in order)

1. **One main figure that *is* the finding.** For most CPS papers this is a coefficient/forest plot, an
   event-study plot around a reform, an RD plot, or a marginal-effects/predicted-probability plot — not
   a wall of regression coefficients.
2. **A clean main results table** with the headline specification and the key robustness columns only;
   push the full grid to the appendix.
3. **A comparative descriptive exhibit** showing the cross-case or over-time variation the design
   exploits (so the reader sees the leverage).
4. **A balance / first-stage / pre-trends exhibit** appropriate to the design.

## Make every exhibit self-contained

- **Title + caption** state what is shown, the unit, the sample, and the comparison — readable alone.
- **Notes** give: estimator, fixed effects, clustering level, N (units and observations), and what the
  error bars are (CI level). For comparative panels, state the countries and the period.
- **Units and scales** labelled in substantive terms (percentage points, predicted probability), not
  raw coefficients a reader must decode.
- **Effect sizes visible.** Show magnitudes and uncertainty, not just significance asterisks.

## Comparative-specific exhibit craft

- When comparing countries/regions, **order and group** them so the pattern is visible (by region,
  regime type, or the key covariate) rather than alphabetically.
- Use **small multiples** to show the same relationship across cases rather than one overplotted panel.
- Maps only when geography is the point; otherwise a sorted dot plot communicates better.

## SAGE production notes (verify current specs)

- Colorblind-safe palettes; figures must remain legible in **grayscale** for print.
- Vector output (PDF/EPS) where possible; supply high-resolution raster otherwise.
- Match exhibit numbering in the manuscript exactly to the deposited replication output.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-supplement drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). CPS is comparative politics — cross-national and sub-national designs; emphasize identification and clustered / multiway inference.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] One main figure conveys the finding without the text
- [ ] Every exhibit's notes give estimator, FE, clustering, N, and CI level
- [ ] Effect sizes and uncertainty are visible, not just stars
- [ ] Cross-case exhibits are ordered/grouped to reveal the comparative pattern
- [ ] Color choices survive grayscale; figures are vector or high-res
- [ ] Heavy tables moved to the appendix; each is referenced in the text
- [ ] Exhibit numbers match the replication output exactly

## Anti-patterns

- A 40-coefficient table where one forest plot would carry the result
- Captions that require the text to interpret; missing N, clustering, or CI level
- Countries ordered alphabetically so the comparative pattern is invisible
- Significance-star tables with no effect magnitudes
- Figures that collapse to mush in grayscale; low-resolution raster images

## Output format

```
【Main figure】what it shows + why it is the finding
【Main table】headline spec + which robustness columns; rest → appendix
【Comparative descriptive】the exhibit showing cross-case/over-time leverage
【Self-contained?】captions/notes give estimator, FE, clustering, N, CI [Y/N]
【Production】grayscale-safe + vector/high-res [Y/N]
【Next】cps-writing-style
```

## Supplementary resources

- [`../../resources/code/`](../../resources/code/) — table/figure generation scripts to adapt
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — coefplot / ggplot / marginaleffects and mapping packages
