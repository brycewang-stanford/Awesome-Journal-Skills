---
name: arpsych-tables-figures
description: Use when designing the summary tables and conceptual figures for an Annual Review of Psychology (ARPsych) review — the who-found-what tables and the one framework diagram that carries the spine. Designs exhibits; it does not design the spine itself (arpsych-organizing-framework) or run a meta-analysis (arpsych-transparency-and-reproducibility).
---

# Tables & Figures — Exhibits That Carry the Spine (arpsych-tables-figures)

## When to trigger

- The framework is set and you need exhibits that *show* it, not decorate the text
- A who-found-what summary table would save pages of prose
- The review needs one figure a reader can screenshot and remember
- A meta-analytic result needs a forest plot or effect-summary display

## Exhibits in a review do different work than in a primary paper

A primary paper's figures *report results*; a review's exhibits **organize a literature**. ARPsych readers and teachers reproduce the good ones in slides for years. Two exhibit types carry most of the load:

### 1. The conceptual framework figure (the signature exhibit)
One diagram that **makes the spine visible** — the taxonomy, the process model, the levels-of-analysis stack, the theory contest. It is the review's logo. Tests:
- A reader who sees only this figure grasps the review's argument about the field.
- Every box/arrow maps to a section; nothing in the figure is unexplained in text and vice versa.
- It is self-contained — caption defines all terms; no jargon a non-specialist can't parse.
- It is *generative*: empty regions read as open questions, not blank space.

### 2. The synthesis table (who found what)
A structured table that compresses the evidence matrix into reader-facing form — typically rows = studies/constructs, columns = population, design, key finding, replication status. This is how a review honors **comprehensiveness without narrating every study**: the table holds the coverage, the prose discusses the cell-defining work.

| Exhibit | Carries | Failure mode |
|---------|---------|--------------|
| Framework figure | the organizing idea | a pretty diagram that doesn't match the sections |
| Synthesis table | coverage + comparability | a wall of cells with no column that adjudicates |
| Forest / effect plot | a quantitative synthesis | shown without search protocol or heterogeneity |
| Timeline / paradigm map | the evolution of ideas | decorative chronology with no argument |

### Production constraints (检索于 2026-06；以官网为准)
Annual Reviews copyedits to **house format** at production and re-renders figures; deliver editable source and high-resolution files, and **secure permission for any reproduced/adapted exhibit** (检索于 2026-06；以官网为准). Color is used in the online/OA version; ensure figures remain legible if printed grayscale. Confirm exact figure specs on the author pages.

## Checklist

- [ ] One conceptual framework figure that makes the spine visible
- [ ] A reader seeing only that figure can state the review's argument
- [ ] Every figure element maps to a section (and vice versa)
- [ ] Synthesis table compresses the evidence matrix; has a column that adjudicates (e.g., replication status)
- [ ] Any forest/effect plot is paired with a documented search + heterogeneity note
- [ ] Captions are self-contained; terms defined; legible in grayscale
- [ ] Permissions secured for reproduced/adapted exhibits
- [ ] Editable source + high-res files prepared; figure specs re-checked on author pages

## Anti-patterns

- A decorative framework figure that does not match the actual section structure
- A synthesis table with no adjudicating column (just a list, not a comparison)
- A forest plot with no stated search/inclusion protocol (uninterpretable, fails transparency)
- Figures that need the body text to be understood (not self-contained)
- Reproducing a copyrighted figure without permission
- Cramming the whole literature into one unreadable mega-table

## Output format

```text
【Framework figure】present? makes the spine visible? Y/N
【Synthesis table】compresses matrix; has an adjudicating column? Y/N
【Quant exhibit】forest/effect plot tied to documented search? (N/A if none)
【Self-containment】captions define terms; grayscale-legible? Y/N
【Permissions】reproduced exhibits cleared? Y/N
【Production】editable source + high-res; specs re-checked? Y/N
【Next step】→ arpsych-writing-style (write the prose around these exhibits)
```
