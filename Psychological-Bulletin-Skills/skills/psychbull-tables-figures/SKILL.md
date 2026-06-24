---
name: psychbull-tables-figures
description: Use when building exhibits for a Psychological Bulletin manuscript — the PRISMA flow diagram, forest plots, funnel/bias plots, moderator bubble plots, and MARS-ready summary tables in APA 7th-edition format. Guides exhibit design; it does not generate the underlying estimates.
---

# Tables & Figures (psychbull-tables-figures)

A meta-analysis communicates through a small set of **standard, expected exhibits**. Psychological
Bulletin reviewers look for a **PRISMA flow diagram**, a **forest plot**, **funnel/bias plots**, and
**MARS-ready** summary tables, all in **APA 7th-edition** format. This skill covers exhibit design;
the numbers come from the analysis skills.

## When to trigger

- Building the figures and tables for the manuscript
- A reviewer asks for the PRISMA diagram, forest plot, or a study-characteristics table
- Making exhibits self-contained, accessible, and reproducible from the deposited scripts

## The expected exhibits

1. **PRISMA flow diagram** — records **identified → deduplicated → screened → full-text assessed →
   included**, with **exclusion counts and reasons** at each stage (matches the search log).
2. **Forest plot** — each study's effect size and CI, its **weight**, and the **pooled estimate** with
   CI and (ideally) a **prediction interval**; order meaningfully (by year, effect, or subgroup).
3. **Funnel plot** (contour-enhanced) and any bias-diagnostic plots (e.g., PET-PEESE regression).
4. **Moderator / meta-regression bubble plot** — effect vs. continuous moderator, point size ∝ weight.
5. **Study-characteristics table** — one row per study: design, n, population, measures, effect size,
   moderator codes — the backbone of a **MARS**-compliant report.
6. **Summary-of-findings table** — pooled effect, CI, k, I²/τ², prediction interval, bias results.

## APA 7th & accessibility

- APA 7th table/figure format: numbered, titled, with notes defining abbreviations.
- **Self-contained**: readable without the text; define every symbol and effect-size metric.
- **Colorblind-safe** palettes; legible in grayscale; **vector** output (PDF/EPS) for print.
- Exhibits must **regenerate from the deposited scripts** and match the reported numbers.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-supplement drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Psychological Bulletin is a meta-analytic review venue.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- No PRISMA diagram, or counts that don't reconcile with the search log
- A forest plot without weights, pooled estimate, or a prediction interval
- A funnel plot presented as proof of (no) bias on its own
- A study table missing the inputs needed to recompute effect sizes
- Figures that can't be regenerated from the deposited code (numbers drift from text)

## Exhibit expectations at the APA review flagship

Psychological Bulletin referees scan the exhibits before the prose: a synthesis missing its standard
visual vocabulary signals an immature manuscript. The decision table they apply:

| Exhibit | Referee expects | Common desk-reject pattern |
|---------|-----------------|----------------------------|
| PRISMA flow | Counts that reconcile to the search log and text | Diagram numbers that don't add up to the reported k |
| Forest plot | Per-study CI, weights, pooled diamond, prediction interval | A bare list of dots with no pooled estimate or PI |
| Funnel/bias | Contour-enhanced, paired with a formal test | Funnel alone, captioned "no bias" — over-reading a picture |
| Study table | One row per study, all effect-size inputs recoverable | Missing ns/SDs, so effect sizes cannot be reverified |
| Summary-of-findings | k, pooled g, CI, I²/τ², PI, bias result in one place | Scattered numbers a reader must reassemble |

## Worked vignette — what the exhibits must show

*Illustrative figures, not real data.* For the k = 42, g = 0.34, I² = 68% self-affirmation synthesis
above, the exhibit set this skill requires looks like:

- **PRISMA diagram**: 2,310 identified → 1,640 after dedup → 1,640 screened → 188 full-text →
  42 included; exclusion reasons tallied so the bottom box equals the analyzed k.
- **Forest plot**: 42 rows ordered by year, each with g and CI and an inverse-variance weight; a pooled
  diamond at 0.34 [0.24, 0.44] and a wider prediction interval roughly [−0.10, 0.78] that visibly
  exceeds the CI — making the 68% heterogeneity legible at a glance.
- **Contour-enhanced funnel** beside an Egger caption (p = 0.03), not standing alone as "proof."
- **Bubble plot** for the delivery-format moderator, point size proportional to weight.
- **Summary-of-findings table**: one line carrying k, g, CI, I², τ², prediction interval, and the
  trim-and-fill / selection-model sensitivity bounds.

## Referee pushback → venue-specific fix

- *"Your forest plot has no prediction interval."* → Add the PI band; with I² = 68% the CI alone
  understates the spread of true effects.
- *"PRISMA counts don't match the text."* → Reconcile the diagram, the search log, and the reported k so
  every box is auditable.
- *"The funnel plot is presented as evidence of no bias."* → Re-caption as one diagnostic among several
  and cross-reference the Egger/selection-model results.

## Output format

```
【PRISMA diagram】present + reconciles with search log? [Y/N]
【Forest plot】weights + pooled + prediction interval? [Y/N]
【Funnel / bias plots】present? [Y/N]
【Study-characteristics table】MARS-complete? [Y/N]
【APA 7th + accessible】numbered, colorblind-safe, vector? [Y/N]
【Reproducible】regenerates from scripts? [Y/N]
【Next】psychbull-writing-style
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — PRISMA flow diagram, `metafor` forest/funnel plots, exhibit tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — MARS/PRISMA reporting and APA 7th formatting
