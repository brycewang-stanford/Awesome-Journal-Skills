---
name: est-submission
description: Use when running the final pre-submission preflight for Environmental Science & Technology (ES&T) via the ACS Publishing Center / ACS Paragon Plus — article-type and word-limit checks, the mandatory TOC graphic, Supporting Information, data-availability statement, ACS style, ORCID, and ethics/COI declarations. Final checks; it does not draft content.
---

# Submission Preflight (est-submission)

The last check before pressing submit on the **ACS Publishing Center** (peer-review environment:
**ACS Paragon Plus**). The most common avoidable failures at ES&T are a **missing TOC graphic**, an
over-limit word count, or an absent data-availability statement. Verify volatile specifics on the
official page before relying on them.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata the ACS submission system expects
- Confirming the article type's caps are met and the TOC graphic + SI are ready

## Process facts (verify volatile items on the official page)

- **Publisher:** American Chemical Society (ACS).
- **Portal:** **ACS Publishing Center** / **ACS Paragon Plus** (confirm current entry URL — 待核实).
- **Article types & caps (待核实 on exact numbers):** Research Article ~7,000; Feature ~5,000; Review
  (Critical Review) ~10,000; Perspective ~4,000; Policy Analysis ~7,000; Viewpoint ~1,000 (+≤5 refs);
  Letter to the Editor ~500. **Figures/tables may count as word-equivalents** (~300/600 — 待核实).
- **TOC graphic:** **required** for Research Articles, Critical Reviews, Features, Perspectives, and
  Policy Analysis; not for Viewpoints/Spotlights/Letters.
- **Supporting Information:** submitted simultaneously as separate file(s), with an SI paragraph
  describing contents and file type.
- **Data availability:** a **data-availability statement** plus deposition of data/materials/protocols
  in public databases (see `est-reporting-and-reproducibility`).
- **Style:** **ACS** (numbered citations); SI units; ACS chemical conventions.
- **Ethics:** COI disclosure; coauthor consent; **iThenticate** screening; safety hazards in Methods;
  AI-use disclosed in Acknowledgments; ORCID for the corresponding author (待核实 on exact requirement).

## Preflight checklist

### Type & length
- [ ] Article type chosen; word count within its cap (counting figure/table word-equivalents)
- [ ] Abstract present and within type norms
- [ ] **TOC graphic** prepared (required for this type) and meeting ACS size/format specs

### Files & content
- [ ] Main manuscript + **separate Supporting Information** file(s); SI paragraph written
- [ ] **Data-availability statement** with accession/DOI; data/code deposited
- [ ] Figures/tables self-contained, accessible (see `est-figures-and-tables`)

### Style & metadata
- [ ] ACS numbered citation style; SI units; consistent nomenclature
- [ ] Corresponding-author ORCID ready (待核实)
- [ ] Suggested reviewers (≥4, non-conflicted) and cover letter ready (see `est-cover-letter`)

### Compliance
- [ ] COI disclosure; coauthor consent; ethics/IRB or animal (ARRIVE) statements if relevant
- [ ] Safety/hazard reporting in Methods; AI-use disclosure if applicable
- [ ] Plagiarism self-check; preprint status checked against ACS policy

## Avoidable rejection-at-upload table

These are the failures that bounce a manuscript at or just after upload — before science is judged.
Each line is a hard gate; confirm the volatile specifics on the live ACS page (待核实):

| Gate | Pass condition | Where it is fixed |
|------|----------------|-------------------|
| TOC graphic | present + spec-compliant for this article type | `est-figures-and-tables` |
| Word count | within cap incl. figure/table word-equivalents | `est-writing-style` |
| Supporting Information | separate file(s) + SI paragraph | `est-reporting-and-reproducibility` |
| Data-availability statement | present with accession/DOI | `est-reporting-and-reproducibility` |
| Citation style | ACS numbered throughout | `est-writing-style` |
| Declarations | COI, coauthor consent, safety, AI-use | this skill |

## Worked micro-example (illustrative — final preflight on an emissions-inventory paper)

A Research Article on basin methane attribution, the night before upload (illustrative):

- **Type & length:** Research Article; body 6,200 words + two figures counted as word-equivalents
  (~600 illustrative) → ~6,800, under the ~7,000 cap. Pass.
- **TOC graphic:** a basin schematic with super-emitter sites highlighted — a concept, not a clone of
  the flux map. Pass.
- **SI + data:** aircraft flux retrievals, the inversion configuration, and uncertainty budget in the
  SI; processed fluxes and inversion code on Zenodo with a DOI; data-availability statement written.
- **Declarations:** COI none; all coauthors consented; no human/animal subjects; AI-use disclosed in
  Acknowledgments; corresponding-author ORCID linked (待核实 on exact requirement).
- **The one easy miss:** the two figures' word-equivalents were nearly forgotten — counting them is
  what keeps the paper under cap. This is the single most common avoidable over-limit failure.

## Anti-patterns

- Submitting without the required TOC graphic
- Over the word cap because exhibits' word-equivalents were not counted
- No data-availability statement or undeposited data
- SI uploaded with no SI paragraph describing its contents
- Non-ACS citation style; missing COI/coauthor-consent declarations

## Output format

```
【Type】Research Article / Critical Review / Feature / Perspective / Policy Analysis (cap met? Y/N)
【TOC graphic】required + present + spec-compliant? [Y/N]
【SI + data-availability statement】present, with accession/DOI? [Y/N]
【ACS style + ORCID】[Y/N]
【Ethics/COI/safety】declared? [Y/N]
【Cover letter + ≥4 reviewers】ready? [Y/N]
【Next】await decision → est-revision-and-rebuttal
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers, ACS templates, deposition repositories
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official ES&T URLs behind every fact in this pack
