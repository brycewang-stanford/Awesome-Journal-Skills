# Cell Resources

Action-oriented resources for the **Cell** (Cell Press flagship) skill pack. The `skills/` give advice;
this directory lets an agent **act** — model a Cell-style Summary + opening and the signature front-matter
artifacts, and benchmark against verified *Cell* exemplars. Pair these with the relevant
`skills/cell-*/SKILL.md`.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a paper **Summary + opening** in Cell house style — the single mechanistic arc, a ≤150-word Summary that names the mechanism and quantifies, plus Highlights / eTOC blurb / Graphical Abstract. Illustrative **fictional** paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified *Cell* papers** organized by method × topic. Design positioning only — no fabricated numbers. Includes a sibling-confusion guard (*Cell* ≠ *Nature*/*Science*/*Molecular Cell*/*Cell Reports*/*Cell Metabolism*). |
| [`external_tools.md`](external_tools.md) | The pack's authoritative **Cell-specific source map**: data/code deposition repositories (GEO, PDB, PRIDE, Mendeley Data), STAR Methods / RRID / reporting standards, the signature-artifact conventions, and key Cell Press author pages. |

> **Note on the source map.** This pack's authoritative Cell-specific policy + source index lives in
> [`external_tools.md`](external_tools.md) (deposition, STAR Methods, author guidelines). There is no
> separate `official-source-map.md` file in this pack; `external_tools.md` is the file the QJE pack's
> `official-source-map.md` corresponds to here. Always confirm limits and policy against the current
> [Cell author guidelines](https://www.cell.com/cell/authors) and
> [STAR Methods guidelines](https://www.cell.com/star-methods).

## This is a life-sciences venue — no econometrics kit is vendored here

*Cell* is a **molecular- and cell-biology bench journal**. The repo's shared **empirical-methods /
causal-inference code kit** (Stata + Python DID/IV/RDD/DML pipelines, used by the economics packs such as
QJE) is **deliberately NOT vendored into this pack** — it is irrelevant to a *Cell* submission. The
discipline-appropriate "tooling" for *Cell* is wet-lab and reporting infrastructure: data/code deposition
with accessions, STAR Methods with a Key Resources Table and RRIDs, and the Highlights / eTOC /
Graphical Abstract artifacts — all indexed in [`external_tools.md`](external_tools.md). If you need the
econometrics kit, use an economics pack (e.g. `Quarterly-Journal-of-Economics-Skills/resources/code/`);
do not look for it here.

## Suggested workflow

1. Confirm the work clears the bar with [`../skills/cell-fit`](../skills/cell-fit/SKILL.md) (complete,
   mechanistic story; correct Cell Press venue).
2. Lock the single arc and a declarative title with
   [`../skills/cell-framing`](../skills/cell-framing/SKILL.md); model the Summary + opening on
   [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md).
3. Draft the front matter with [`../skills/cell-summary`](../skills/cell-summary/SKILL.md) (≤150-word
   Summary) and [`../skills/cell-highlights`](../skills/cell-highlights/SKILL.md) (Highlights / eTOC /
   Graphical Abstract).
4. Benchmark against verified *Cell* papers in [`exemplars/library.md`](exemplars/library.md); confirm
   deposition, STAR Methods, and submission resources in [`external_tools.md`](external_tools.md).
