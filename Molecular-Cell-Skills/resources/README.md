# Molecular Cell Resources

Action-oriented resources for the **Molecular Cell** (Mol. Cell, Cell Press) skill pack. The `skills/` give
advice; this directory lets an agent **act** — model a Molecular Cell Summary + mechanistic opening and the
signature front-matter artifacts, benchmark against the kinds of mechanism papers Molecular Cell publishes,
and confirm every hard fact against an official source. Pair these with the relevant
`skills/molcell-*/SKILL.md`.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a **Summary + opening** in Molecular Cell house style — the single-mechanism arc, a ~150-word Summary that names the molecular mechanism and quantifies, plus Highlights / eTOC blurb / Graphical Abstract. Illustrative **fictional** paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Position your work by **method × topic** against the mechanistic stories Molecular Cell publishes. Design positioning only — no fabricated numbers. Includes a sibling-confusion guard (*Molecular Cell* ≠ *Cell* / *Nature* / *Science* / *NSMB* / *EMBO J* / *Cell Reports*). |
| [`external_tools.md`](external_tools.md) | The pack's **molecular-biology source map**: data/structure/code deposition (GEO, PDB/EMDB, PRIDE, Mendeley Data), STAR Methods / RRID / reporting standards, the sequence–structure–imaging–genomics stack, and key Cell Press author pages. |
| [`official-source-map.md`](official-source-map.md) | The **authoritative fact index**: official URLs, the verified journal facts (ISSN, ownership, EiC, article types, limits, numbered references), and the access date — with live-check rules for volatile items. |

## This is a life-sciences venue — no econometrics kit is vendored here

*Molecular Cell* is a **mechanistic molecular-biology bench journal**. The repo's shared empirical-methods /
causal-inference code kit (Stata + Python DID/IV/RDD/DML pipelines, used by the economics packs) is
**deliberately NOT vendored into this pack** — it is irrelevant to a Molecular Cell submission. The
discipline-appropriate "tooling" here is wet-lab and reporting infrastructure: data/structure/code
deposition with accessions, STAR Methods with a Key Resources Table and RRIDs, and the Highlights / eTOC /
Graphical Abstract artifacts — all indexed in [`external_tools.md`](external_tools.md). If you need the
econometrics kit, use an economics pack (e.g. `Quarterly-Journal-of-Economics-Skills/resources/code/`); do
not look for it here.

## Suggested workflow

1. Confirm the work clears the bar with [`../skills/molcell-fit`](../skills/molcell-fit/SKILL.md) (deep
   mechanism, orthogonal validation, physiological relevance; correct Cell Press venue).
2. Lock the single-mechanism arc and a declarative title with
   [`../skills/molcell-framing`](../skills/molcell-framing/SKILL.md); model the Summary + opening on
   [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md).
3. Draft the front matter with [`../skills/molcell-summary`](../skills/molcell-summary/SKILL.md) (~150-word
   Summary) and [`../skills/molcell-highlights`](../skills/molcell-highlights/SKILL.md) (Highlights / eTOC /
   Graphical Abstract).
4. Position against [`exemplars/library.md`](exemplars/library.md); confirm deposition and STAR Methods in
   [`external_tools.md`](external_tools.md) and every hard fact in
   [`official-source-map.md`](official-source-map.md).
