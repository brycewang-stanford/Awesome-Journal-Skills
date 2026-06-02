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

## Anti-patterns

- No PRISMA diagram, or counts that don't reconcile with the search log
- A forest plot without weights, pooled estimate, or a prediction interval
- A funnel plot presented as proof of (no) bias on its own
- A study table missing the inputs needed to recompute effect sizes
- Figures that can't be regenerated from the deposited code (numbers drift from text)

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
