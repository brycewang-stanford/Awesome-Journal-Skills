---
name: jegeo-submission
description: Use when running the final pre-submission preflight for a Journal of Economic Geography (JEG) manuscript via OUP / ScholarOne — word and abstract limits, double-anonymous scrub, ORCID, keywords/JEL, and house style. Final checks; it does not draft content.
---

# Submission Preflight (jegeo-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on ScholarOne / Manuscript Central
- Unsure which files, limits, and declarations the OUP submission expects
- Confirming the manuscript is double-anonymous-clean and within JEG's length/abstract limits
- Deciding whether the paper fits the full-article or the shorter Emerging Voices lane

## Process facts (检索于 2026-06；以官网为准)

- JEG is published by **Oxford University Press**; submission is through **ScholarOne / Manuscript Central** at `mc.manuscriptcentral.com/joeg` (the OUP submission system).
- Review is **double-anonymous**: the author's identity must be removed from the manuscript, not just the title page — referees and authors are mutually anonymized.
- **Length:** standard articles are **≤8,000 words excluding references**; over-length papers may be asked to cut or to move non-essential material to an **online-only appendix**, and this can be a condition for review. The **Emerging Voices** format is shorter (≈5,000 words, few exhibits) for tighter contributions.
- **Abstract ≤100 words**, followed by **four keywords** and **JEL codes**.
- **ORCID iD** is required for the submitting author.
- **Data/code policy** is encouragement-based and handled **after acceptance** (you are asked at acceptance whether associated data exist) — there is no pre-acceptance reproducibility archive.
- Exact figure specs, fee/open-access details, and any updated limits are **待核实** — confirm on the OUP author-instructions page before submitting.

## Preflight checklist

### Length & structure
- [ ] Main text **≤8,000 words excluding references**; over-length material moved to an online appendix (待核实 exact limit)
- [ ] Main text is **self-contained** — the appendix supports, it does not carry a key claim
- [ ] Emerging Voices papers within that format's shorter limit (检索于 2026-06；以官网为准)

### Abstract, keywords, classification
- [ ] **Abstract ≤100 words**, contribution-first
- [ ] **Four keywords** + **JEL codes** included
- [ ] Title conveys the spatial economic contribution

### Double-anonymous scrub
- [ ] Author names/affiliations removed from the manuscript body and headers
- [ ] Self-citations neutralized ("Author (2022)" not "In our 2022 paper on [city]")
- [ ] Acknowledgments/funding lines removed to a separate non-blinded file
- [ ] File metadata (PDF/Word author properties) scrubbed
- [ ] Maps/figures carry no identifying institutional watermarks

### House style & exhibits
- [ ] **No significance asterisks**; standard errors / CIs reported; SE type (Conley/clustered) stated
- [ ] Spatial-model tables report direct vs. indirect effects; W and cutoff noted
- [ ] Maps make an argument, classification scheme stated, readable in grayscale
- [ ] Figure/table specs meet OUP requirements (待核实)

### Files & declarations
- [ ] Anonymized main PDF/Word + separate title page with authors, affiliations, ORCID
- [ ] **ORCID** for the submitting author ready
- [ ] Online appendix file prepared if over length
- [ ] Confirmed the paper is not under review elsewhere; AI not listed as an author

## The double-anonymous scrub deserves its own pass

Double-anonymous review is where economic-geography papers leak identity in ways authors miss, because the *place* is often a fingerprint. Beyond the usual name/affiliation removal:

- A single-region case study can de-anonymize the author by the study site plus their known field area — phrase self-citations and acknowledgments to avoid confirming it.
- Maps and figures sometimes carry institutional logos, GIS-license watermarks, or file-path captions exposing a username; export clean.
- PDF/Word document properties retain the author name by default — clear them.
- "Funded by [grant] to [PI]" in a footnote defeats the whole exercise; move it to the separate title page.

Treat this as a dedicated checklist pass, not a side effect of deleting the byline.

## Anti-patterns

- Submitting with author identity still visible (defeats double-anonymous review — common desk-reject)
- Abstract over 100 words or missing keywords/JEL
- Over-length manuscript with no online-appendix plan
- Significance asterisks, or spatial-lag tables with no direct/indirect split
- Confusing JEG's post-acceptance data policy with a pre-acceptance archive and over- or under-preparing
- Treating ScholarOne for JEG like an Elsevier portal (it is OUP/Manuscript Central)

## Output format

```text
【Length】≤8,000 words excl. refs; appendix plan if over? [Y/N]
【Abstract】≤100 words + 4 keywords + JEL? [Y/N]
【Double-anonymous】body/citations/metadata/figures scrubbed? [Y/N]
【House style】no asterisks; SE type + W/cutoff; maps argue? [Y/N]
【ORCID + files】ORCID ready; anonymized MS + separate title page? [Y/N]
【Format】full article / Emerging Voices
【Next step】submit via mc.manuscriptcentral.com/joeg → jegeo-rebuttal on decision
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — submission self-check
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — lightweight manuscript scaffold
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official OUP URLs and volatile facts
