# *Science* (AAAS) Resources

Action-oriented resources for the *Science* (AAAS) skill pack. The `skills/sci-*` give advice; this
directory lets an agent **act** — model a *Science*-style abstract and opening, and benchmark against
**real, web-verified** *Science* papers. Pair these with the relevant
[`../skills/sci-*/SKILL.md`](../skills/).

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a *Science* **abstract + opening** in AAAS house style — the one-sentence-summary convention, the ≤ ~125-word abstract, advance-first framing, and the tight Report format. Illustrative **fictional** paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified *Science* (AAAS) papers** organized by field × method (6 verified, access date 2026-06-08). Design/framing positioning only — no fabricated numbers. Includes a sibling-confusion guardrail (*Science* is **not** *Nature* / *PNAS* / *Cell* / *Science Advances* / *Science* sub-journals). |
| [`external_tools.md`](external_tools.md) | The pack's **official-source index**: AAAS author/editorial-policy pages, data & code deposition repositories (GenBank, PDB, Dryad, Zenodo, …), reporting/integrity standards (CRediT, ORCID, ARRIVE, EQUATOR), figure and statistics tooling. The authoritative pack source for venue facts. |

> **Note on the source map.** This pack does not ship a separate `official-source-map.md`; its
> authoritative venue-facts-and-links role is served by [`external_tools.md`](external_tools.md), which
> points at the live AAAS author and editorial-policy pages. Always confirm volatile specifics (word
> caps, fees, formats) against the current
> [Science Author Guidelines](https://www.science.org/content/page/science-information-authors).

## No econometric methods kit (multidisciplinary venue)

*Science* is a **multidisciplinary** general-science journal, not an economics venue. Accordingly, this
pack deliberately **does not vendor** the empirical-econometrics code kit (Stata/Python causal-inference
pipeline — DID, IV, RDD, DML, etc.) that economics packs such as the *Quarterly Journal of Economics*
pack carry. Discipline-appropriate, field-agnostic tooling (data/code deposition, reporting standards,
figures, statistics, reproducibility) lives in [`external_tools.md`](external_tools.md) instead; the
`sci-statistics` and `sci-data` skills cover analysis and reproducibility expectations across fields.

## Suggested workflow

1. Gate the work with [`../skills/sci-fit`](../skills/sci-fit/SKILL.md) (broad-significance / general
   interest), then lock the advance with [`../skills/sci-framing`](../skills/sci-framing/SKILL.md).
2. Model the abstract + opening on
   [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md), holding the Report/Research
   Article format with [`../skills/sci-writing`](../skills/sci-writing/SKILL.md) and the two abstract
   artifacts with [`../skills/sci-abstract`](../skills/sci-abstract/SKILL.md).
3. Benchmark your field × method against verified papers in
   [`exemplars/library.md`](exemplars/library.md).
4. Enforce reporting with [`../skills/sci-statistics`](../skills/sci-statistics/SKILL.md), deposit data
   and code per [`external_tools.md`](external_tools.md) and
   [`../skills/sci-data`](../skills/sci-data/SKILL.md), then run the final gate in
   [`../skills/sci-submission`](../skills/sci-submission/SKILL.md).
