---
name: molcell-workflow
description: Use when deciding which molcell-* sub-skill to invoke next, or when sequencing a manuscript from mechanism-fit test through reviewer rebuttal for Molecular Cell (Mol. Cell, Cell Press). Routes to the specialized skills — it does not replace them.
---

# Molecular Cell Workflow Router (molcell-workflow)

## Overview

This is the router. It does not do the work of any specialized skill; it names **which molcell-* skill fits the current stage** of a manuscript aimed at *Molecular Cell* (Cell Press).

Default assumption: unless told otherwise, the target is **Molecular Cell** — the mechanism-focused molecular-biology flagship — not *Cell*, *Cell Reports*, *Molecular Cell*'s sibling *Structure*, or a field-specific title. The Cell Press family shares STAR Methods, the Key Resources Table, Highlights, the eTOC blurb, the Graphical Abstract, and (now) numbered references, but the venues differ sharply on what kind of advance they reward.

## The single most important idea about Molecular Cell

*Cell* asks "does this reframe a broad field?" **Molecular Cell asks a different question: "is the molecular mechanism worked out to the base-pair, residue, or single-molecule level, and proven by orthogonal approaches?"** Depth of mechanism beats breadth of implication here. A correlative or descriptive story — even a broadly interesting one — is rejected before review if the *how* is not nailed down biochemically and structurally/genetically. Route to `molcell-fit` first, always.

## When to trigger

- "What should I do next with this draft?"
- A draft arrives and you must diagnose the current bottleneck.
- The author is bouncing between bench work, writing, and revision and has lost the thread.
- Reviews arrive from Molecular Cell and you need to switch into rebuttal mode.

## The single most important gate

Molecular Cell editors triage **most submissions to rejection without external review**. The bar is **mechanistic depth + orthogonal validation + physiological relevance**, not novelty of the phenotype alone. The first question is never "is the result interesting?" — it is **"is the molecular mechanism established by independent methods, and does it operate in a physiological context?"** Route to `molcell-fit` first.

## Routing table

| Current symptom                                                | Next skill            |
|----------------------------------------------------------------|-----------------------|
| Not sure the mechanism is deep/validated enough for Mol. Cell  | `molcell-fit`         |
| Mechanism is solid but the arc reads as a technique list       | `molcell-framing`     |
| Main text over ~7,000 words; Discussion recaps Results         | `molcell-writing`     |
| Figures over ~7; data hidden; stats/gels/structures off        | `molcell-figures`     |
| No Key Resources Table / Resource Availability incomplete      | `molcell-star-methods`|
| No GEO/PDB/PRIDE deposition plan or accessions                 | `molcell-data`        |
| Summary is long, structured, or names no mechanism             | `molcell-summary`     |
| No Highlights / eTOC blurb / Graphical Abstract                | `molcell-highlights`  |
| References are author–date or otherwise not Cell Press numbered| `molcell-citation`    |
| About to submit; need a preflight + cover letter               | `molcell-submission`  |
| Received reviews / a revision decision                         | `molcell-rebuttal`    |

## Default order

1. `molcell-fit` — clear the mechanistic-depth + orthogonal-validation bar first
2. `molcell-framing` — lock the single-mechanism arc (question → mechanism → physiological consequence)
3. `molcell-writing` — Article structure and the ~7,000-word / ~7-item budget
4. `molcell-figures` — finalize display items; show the data; blot/structure integrity
5. `molcell-star-methods` — Key Resources Table + Resource Availability + QSA
6. `molcell-data` — GEO/PDB/PRIDE deposition and the availability statement
7. `molcell-summary` — the Summary (late polish)
8. `molcell-highlights` — Highlights + eTOC blurb + Graphical Abstract (late polish)
9. `molcell-citation` — Cell Press numbered-reference pass (late polish)
10. `molcell-submission` — cover letter + preflight
11. `molcell-rebuttal` — after review

> `molcell-summary`, `molcell-highlights`, and `molcell-citation` are **late-stage polish**. Do not perfect the Highlights before the mechanism and figures are settled.

## Decision shortcuts

- "We see a strong phenotype but haven't shown the molecular cause" → `molcell-fit` (likely not yet a Mol. Cell story)
- "The paper is really three techniques stapled together" → `molcell-framing`
- "My Methods is a free-text section" → `molcell-star-methods` (Molecular Cell uses STAR Methods)
- "My antibodies/plasmids/strains aren't tabulated" → `molcell-star-methods` (Key Resources Table)
- "My references are (Author, year)" → `molcell-citation` (Cell Press is now numbered superscript)
- "No GEO/PDB/PRIDE accession yet" → `molcell-data`

## How Molecular Cell differs from its siblings

- **Molecular Cell vs Cell**: *Cell* wants a complete story with broad, cross-field significance. Molecular Cell wants the **molecular mechanism proven deeply** in a defined domain (gene expression, chromatin/epigenetics, RNA biology, DNA replication/repair, signaling, proteostasis, protein structure/function). If breadth is thin but the mechanism is deep and rigorous, Molecular Cell is the better home.
- **Molecular Cell vs Cell Reports**: Cell Reports is **more accepting** of solid, complete, but less mechanistically deep work.
- **Molecular Cell vs Nature Structural & Molecular Biology / EMBO J / Genes & Dev**: strong overlap in scope; Molecular Cell skews toward the deepest, most complete mechanistic stories with orthogonal validation.
- **References are numbered** at Molecular Cell (Cell Press moved to a numbered superscript style across its journals) — do not port author–date citations in unconverted.

## Stage tracker (fill and re-run the router)

Keep this manifest with the draft; the top unfinished row names the skill to invoke next. The gate row must clear before any polish row is touched.

```
MOLECULAR CELL MANUSCRIPT — stage tracker
one-line story : [question → the molecular mechanism → physiological consequence]
sibling check  : Mol. Cell vs Cell / Cell Reports / NSMB / EMBO J

stage                          status        next skill
-----------------------------  ------------  --------------------
GATE: deep mechanism +         [in-progress] molcell-fit
      orthogonal validation
single-mechanism arc           [todo]        molcell-framing
article text + length (~7k w)  [todo]        molcell-writing
figure budget (~7 items)       [todo]        molcell-figures
STAR Methods + KRT + QSA       [todo]        molcell-star-methods
data / code deposition         [todo]        molcell-data
Summary                        [todo]        molcell-summary     (late)
Highlights / eTOC / GA         [todo]        molcell-highlights  (late)
numbered references            [todo]        molcell-citation    (late)
cover letter + preflight       [todo]        molcell-submission
reviews / revision             [—]           molcell-rebuttal

rule: if the GATE row is not [done], every row below stays frozen.
```

## Anti-patterns

- **Do not** skip `molcell-fit` and polish prose — the modal outcome for a mechanism-thin draft is pre-review rejection.
- **Do not** build the Graphical Abstract before the single-mechanism arc is locked in `molcell-framing`.
- **Do not** treat Methods as a free-text section — Molecular Cell requires STAR Methods.
- **Do not** leave numbered/author–date reference confusion until upload — Molecular Cell is numbered.

> All conventions here are working defaults — confirm against the current Molecular Cell information-for-authors page.
