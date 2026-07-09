---
name: itcs-camera-ready
description: Use when preparing an accepted ITCS paper for open-access publication in LIPIcs — switching to the lipics-v2021 document class, de-anonymizing, completing LIPIcs metadata (ACM CCS, keywords, funding), folding in reviewer-noted fixes, and passing the Schloss Dagstuhl production checks.
---

# ITCS Camera-Ready

On acceptance, an ITCS paper becomes an **open-access LIPIcs article** (Schloss Dagstuhl),
Creative-Commons-licensed, with **no article-processing charge**. The camera-ready is a distinct
production process from submission: it uses the **`lipics-v2021` document class** (not the free
single-column submission format), requires **LIPIcs-specific metadata**, and is checked by the
Dagstuhl editorial office. This skill runs that pass. Confirm the exact deadline and any
ITCS-specific page limit on the current call — the camera-ready page limit is **待核实** as of
2026-07-09 (see [`../../resources/official-source-map.md`](../../resources/official-source-map.md)).

## Switch to the LIPIcs class

- **Use `lipics-v2021`** (the current LIPIcs LaTeX class from Dagstuhl). Do not submit the
  submission-time single-column format as camera-ready; the class controls layout, the DROPS
  metadata, and the license block.
- **Re-fit content to the LIPIcs style.** The class changes spacing and float handling; check that
  theorem environments, the appendix, and any figures still render cleanly.
- **Respect the LIPIcs page-limit convention** (a main-text limit with the bibliography excluded,
  and typically a small "+1 page" allowance granted on acceptance). The exact ITCS number is
  cycle-specific — **待核实**; read the camera-ready instructions.

## De-anonymize completely

The submission was lightweight double-blind; the camera-ready is fully attributed:

- **Restore author names, affiliations, ORCIDs, and emails** in the LIPIcs author blocks.
- **Restore acknowledgements and funding** lines you removed for anonymity — LIPIcs has a dedicated
  funding field; list grants and agencies there.
- **Convert third-person self-references back to natural form** where appropriate, and make sure
  no "[Author, YEAR]" placeholder from the blinding survives.

## Complete the LIPIcs metadata

LIPIcs/DROPS requires structured metadata beyond the PDF body:

- **ACM 2012 CCS concepts** — pick the Computing Classification System categories that match the
  paper; the class provides the `\ccsdesc` macro.
- **Keywords** — a short, specific list for indexing.
- **Author ORCIDs** for every author (LIPIcs strongly encourages these).
- **Funding** — per-author funding statements in the LIPIcs funding field.
- **Related-version links** — declare the arXiv/ECCC/ePrint full version as a "Related Version"
  (e.g., "Full Version") so the open record is linked from the published article.
- **Category / acknowledgements / license** blocks as the class template specifies.

## Fold in reviewer-noted fixes

Even without a rebuttal or revision round, the reviews often flag concrete corrections. The
camera-ready is where they land:

- Correct any misstated claim, add a missing citation, clarify a definition, or repair a proof gap
  the reviews identified.
- Use the (generous) LIPIcs length to *add* the clarification rather than cut — but keep the
  first-pages merits window clean (see [`itcs-writing-style`](../itcs-writing-style/SKILL.md)).
- Ensure the camera-ready and the public **full version stay in sync** after these edits (see
  [`itcs-reproducibility`](../itcs-reproducibility/SKILL.md)).

## Dagstuhl production checks

- **Compile with the exact `lipics-v2021` class and required packages**; the DROPS pipeline is
  strict about a clean build and correct metadata macros.
- **Fonts embedded, PDF/A-friendly, no external font issues** — the editorial office will bounce a
  non-compliant PDF.
- **Bibliography** complete and consistently formatted; DOIs where available.
- **Author agreement / license** signed for the LIPIcs Creative-Commons publication.
- **Register at least one author** to present at the conference; ITCS is a present-in-person venue.

## Camera-ready checklist

```text
[Class]        lipics-v2021 used; content re-fit; page-limit convention met (exact # 待核实)
[De-anonymize] names, affiliations, ORCIDs, emails, acknowledgements, funding restored
[Metadata]     ACM CCS, keywords, ORCIDs, funding, Related-Version (arXiv/ECCC/ePrint) all set
[Fixes]        reviewer-noted corrections folded in; merits window still clean
[Sync]         camera-ready and public full version agree
[Production]   clean lipics-v2021 build, fonts embedded, license signed, bib complete
[Presentation] a presenting author registered
```

## Reverify each cycle

- The camera-ready deadline and the current LIPIcs class version.
- The exact ITCS page-limit number and any "+1 page" allowance (**待核实**).
- The required metadata fields (CCS version, ORCID policy, funding format) on the DROPS/LIPIcs
  author instructions.

## Output format

```text
[ITCS camera-ready status] ready / needs work
[Class] lipics-v2021 building cleanly? page-limit convention met? yes/no
[De-anonymized] all author/affiliation/funding fields restored? yes/no
[Metadata] CCS + keywords + ORCIDs + funding + Related-Version complete? yes/no
[Fixes+sync] reviewer corrections in; full version consistent? yes/no
[Fix queue] <ordered, with the production deadline>
```
