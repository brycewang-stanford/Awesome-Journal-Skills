---
name: demog-submission
description: Use when running the final pre-submission preflight for Demography (PAA / Duke University Press) via ScholarOne Manuscripts — article-type selection, double-blind preparation, word/abstract/highlights/keywords limits, house-style formatting, the $35 submission fee, and the open-access (Subscribe to Open) model. Final checks; it does not draft content.
---

# Submission Preflight (demog-submission)

The last check before pressing submit on **ScholarOne Manuscripts** (Demography moved off Editorial
Manager in 2024). Demography is **double-blind**, so the most common avoidable failure is a manuscript
with self-identifying references. Verify volatile specifics on the official page before relying on them.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata ScholarOne expects
- Confirming the chosen type's limits are met and the manuscript avoids self-identifying references

## Process facts (verify volatile items on the official page)

- **Owner / publisher:** Population Association of America (PAA) / Duke University Press.
- **Portal:** **ScholarOne Manuscripts** (since May 31, 2024 — confirm the current submission link).
- **Review model:** **double-blind** — avoid self-identifying references; do not name yourself as author.
- **Article types:** Research Article (<= 8,000 words main text), Research Note (<= 4,000), Commentary
  (<= 2,000). Main-text counts exclude abstract, keywords, footnotes, acknowledgments.
- **Front matter:** abstract **<= 200 words**; **up to 5 keywords/phrases**; **3-5 highlights** (each a
  complete sentence **<= 85 characters** incl. spaces).
- **Exhibits:** Articles up to **~8 tables/figures** (recommend **<= 75 references**); Notes **<= 4**
  (recommend **<= 15 references**); loosely **APA** reference style; Merriam-Webster spelling.
- **Access model:** **Subscribe to Open (S2O)** — free to readers; **not** an APC journal.
- **Fees:** **$35 submission fee** at submission (confirmed current 2026-06-22); **$1,000
  editorial-management fee** at acceptance (waivable; **not** an open-access charge). Re-verify
  amounts/waiver eligibility on the live page before submission. 待核实.

## Preflight checklist

### Type & length
- [ ] Article type chosen and its main-text word cap met (Article <= 8,000 / Note <= 4,000 / Commentary <= 2,000)
- [ ] Abstract **<= 200 words**; **3-5 highlights** each <= 85 chars; **<= 5 keywords**
- [ ] Tables/figures within the limit (~8 Article / 4 Note); references within recommendation

### Anonymity (double-blind)
- [ ] No author names, affiliations, or acknowledgments in the manuscript
- [ ] No self-identifying references ("as we showed in…"); self-citations neutralized
- [ ] Identifying **file metadata stripped** (document properties, comments)
- [ ] Separate (non-anonymous) title page prepared if required by ScholarOne

### Format & metadata
- [ ] Loosely **APA** house style; consistent author-date citations; Merriam-Webster spelling
- [ ] Figures/tables self-contained and accessible (see `demog-tables-figures`)

### Compliance & files
- [ ] Ethics / human-subjects compliance and disclosures complete
- [ ] **Data availability statement** drafted; materials staged for a FAIR repository at acceptance
      (see `demog-data-and-reproducibility`)
- [ ] **$35 submission fee** ready (and waiver path noted if eligible)

## Anti-patterns

- Leaving author identifiers in the text, acknowledgments, or file metadata (breaks double-blind)
- Abstract over 200 words; highlights over 85 characters; more than 5 keywords
- Sending a long paper to the Research Note track, or exceeding the table/figure limit
- Reusing an old **Editorial Manager** link instead of ScholarOne
- Describing the $1,000 fee as an open-access APC (it is not)

## Compliance pre-screen: what the desk checks first (by article type)

Demography — the Population Association of America flagship at Duke University Press — runs a
compliance pre-review before suitability. A failure here can bounce the manuscript before any reviewer
sees it. Map your type to its caps (confirm current numbers against the journal's submission guidelines):

| Item | Research Article | Research Note | Commentary |
|------|------------------|---------------|------------|
| Main-text words | <= 8,000 | <= 4,000 | <= 2,000 |
| Tables + figures | ~8 | <= 4 | minimal |
| References (recommended) | <= 75 | <= 15 | <= 15 |
| Abstract / highlights / keywords | <= 200 words / 3-5 (<= 85 chars) / <= 5 | same | same |
| Double-blind | required | required | required |

## Referee/editor pushback at the desk and the submission-side fix

- *"Self-identifying references compromise the double-blind."* -> Neutralize self-citations ("prior work
  [Author] showed" not "as we showed"), strip document-property metadata, and split off a non-anonymous title page.
- *"This Note exceeds the Note caps."* -> Either trim to <= 4,000 words and <= 4 exhibits or move it to the
  Research Article track; do not submit an over-length Note hoping for leniency.
- *"The data availability statement is missing."* -> Stage the statement and FAIR-repository deposit now,
  even though it is finalized at acceptance (see `demog-data-and-reproducibility`).
- *"Was this submitted through the right portal?"* -> Use ScholarOne Manuscripts; an old Editorial
  Manager link routes nowhere since the 2024 migration.

## Output format

```
【Type】Article / Note / Commentary (main-text cap met? Y/N)
【Anonymized】text + self-refs + file metadata clean? [Y/N]
【Abstract / highlights / keywords】<= 200 words / 3-5 (<= 85 chars) / <= 5? [Y/N]
【Exhibits + references】within limits? [Y/N]
【House style】loosely APA + Merriam-Webster? [Y/N]
【Data statement】drafted + repo staged? [Y/N]
【Fees】$35 submission ready (waiver if eligible)? [Y/N]
【Next】await decision -> demog-rebuttal on R&R
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers, anonymization, FAIR repositories
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official Demography URLs behind every fact in this pack
