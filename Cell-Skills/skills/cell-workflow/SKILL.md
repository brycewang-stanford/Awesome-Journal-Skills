---
name: cell-workflow
description: Use when deciding which cell-* sub-skill to invoke next, or when sequencing a manuscript from significance test through reviewer rebuttal for Cell (Cell Press). Routes — it does not replace — the specialized skills.
---

# Cell Workflow Router (cell-workflow)

## Overview

This is the router. It does not replace any specialized skill. It tells you **which cell-* skill to use at the current stage** of a manuscript aimed at *Cell* (Cell Press).

Default assumption: unless the user states otherwise, the target is **Cell** (the flagship), not *Molecular Cell*, *Cell Reports*, *Cell Reports Medicine*, *Developmental Cell*, or other Cell Press titles. The family shares STAR Methods, Highlights, eTOC, and Graphical Abstract conventions, but differs sharply on scope and breadth — flag the difference if the user names a sibling.

## The single most important idea about Cell

Cell does not publish a single striking observation. It publishes a **complete, mechanistic, hypothesis-driven story**: a conceptual advance supported by **multiple independent lines of evidence that converge on a mechanism**. Descriptive or single-result papers are desk-rejected. Route to `cell-fit` first, always.

## When to trigger

- "What should I do next with this draft?"
- A draft arrives and you must diagnose the current bottleneck.
- The user is switching between experiments, writing, and revision and has lost the thread.
- Reviews arrive from Cell and you need to switch into rebuttal mode.

## The single most important gate

Cell editors reject **most submissions before review**. The bar is **conceptual advance + mechanistic completeness**, not technical correctness alone. The first question is never "is the science right?" — it is **"is this a complete, mechanistic story a broad life-sciences readership will care about?"** Route to `cell-fit` first.

## Routing table

| Current symptom                                              | Next skill          |
|-------------------------------------------------------------|---------------------|
| Not sure it's a complete, mechanistic, broad-interest story | `cell-fit`          |
| Story is solid but the arc/narrative is fragmented          | `cell-framing`      |
| No Highlights / eTOC blurb / Graphical Abstract             | `cell-highlights`   |
| Abstract (Summary) is long, structured, or under-quantified | `cell-summary`      |
| Main text wanders; length/structure off; Discussion bloated | `cell-writing`      |
| Figures over budget; fonts/colors/stats reporting off       | `cell-figures`      |
| No Key Resources Table / Resource Availability incomplete   | `cell-star-methods` |
| No data/code deposition plan or accessions                  | `cell-data`         |
| References not in Cell author–date style                    | `cell-citation`     |
| About to submit; need a preflight + cover letter            | `cell-submission`   |
| Received reviews / a revision decision                      | `cell-rebuttal`     |

## Default order

1. `cell-fit` — clear the complete-mechanistic-story bar first
2. `cell-framing` — lock the single narrative arc (hypothesis → mechanism → significance)
3. `cell-writing` — Article structure and length discipline
4. `cell-figures` — finalize display items within budget
5. `cell-star-methods` — Key Resources Table + Resource Availability + QSA
6. `cell-data` — data / code deposition and the availability statement
7. `cell-summary` — the ≤150-word Summary (late polish)
8. `cell-highlights` — Highlights + eTOC blurb + Graphical Abstract (late polish)
9. `cell-citation` — author–date reference pass
10. `cell-submission` — cover letter + preflight
11. `cell-rebuttal` — after review

> `cell-summary`, `cell-highlights`, and `cell-citation` are **late-stage polish**. Do not perfect the Highlights before the story and figures are settled.

## Decision shortcuts

- "We have one striking result but no mechanism" → `cell-fit` (likely not yet a Cell story)
- "The paper reads like three separate mini-papers" → `cell-framing`
- "I have no Graphical Abstract / my Highlights are full sentences" → `cell-highlights`
- "My Methods is a free-text section" → `cell-star-methods` (Cell uses STAR Methods)
- "My antibodies/strains/software aren't tabulated" → `cell-star-methods` (Key Resources Table)
- "My refs are numbered by appearance" → `cell-citation` (Cell is author–date)
- "No GEO/PDB accession yet" → `cell-data`

## How Cell differs from its siblings and from Nature/Science

- **Cell** vs **Molecular Cell**: Molecular Cell wants the same rigor focused on a **molecular mechanism** in a narrower domain (gene expression, DNA/RNA, signaling, proteostasis). If the broad cross-field implication is thin but the molecular mechanism is deep, route to Molecular Cell.
- **Cell** vs **Cell Reports**: Cell Reports is **more accepting** — solid, complete, but less broadly transformative work fits there. A common, honest outcome.
- **Cell** vs **Cell Reports Medicine**: translational / clinically oriented complete stories.
- **Cell** vs **Nature/Science**: all three gate on broad significance, but Cell most explicitly demands **mechanistic completeness** ("a complete story") and uses **author–date** references (opposite of Science's numbered-by-appearance), a **Summary** (not a one-sentence summary), **Highlights**, an **eTOC/In Brief blurb**, a **Graphical Abstract**, and **STAR Methods**. Do not port a Nature/Science manuscript over without these conversions.

## Stage tracker (fill and re-run the router)

Keep this manifest with your draft; the top unfinished row names the skill to invoke next. The gate row must clear before any polish row is touched.

```
CELL MANUSCRIPT — stage tracker
one-line story : [hypothesis → mechanism → why a broad readership cares]
sibling check  : Cell vs Molecular Cell / Cell Reports / Cell Reports Medicine

stage                         status        next skill
----------------------------  ------------  -------------------
GATE: complete mechanistic    [in-progress] cell-fit
      story, broad interest
narrative arc                 [todo]        cell-framing
article text + length         [todo]        cell-writing
figure budget                 [todo]        cell-figures
STAR Methods + KRT + QSA      [todo]        cell-star-methods
data / code deposition        [todo]        cell-data
Summary (≤150 words)          [todo]        cell-summary       (late)
Highlights / eTOC / GA        [todo]        cell-highlights    (late)
author–date references        [todo]        cell-citation      (late)
cover letter + preflight      [todo]        cell-submission
reviews / revision            [—]           cell-rebuttal

rule: if the GATE row is not [done], every row below stays frozen.
```

## Anti-patterns

- **Do not** skip `cell-fit` and start polishing prose — the modal outcome is pre-review rejection.
- **Do not** build the Graphical Abstract before the narrative arc is locked in `cell-framing`.
- **Do not** treat Methods as a free-text section — Cell requires STAR Methods.
- **Do not** generate a rebuttal before the main text and new experiments are actually done.

> All conventions here are working defaults — confirm against current Cell Press author guidelines.
