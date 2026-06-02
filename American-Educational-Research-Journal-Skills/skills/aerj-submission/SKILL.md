---
name: aerj-submission
description: Use when running the final pre-submission preflight for the American Educational Research Journal (AERJ) via ScholarOne Manuscript Central — section selection (SIA vs TLHD), masked preparation, length and abstract limits, APA 7th-edition formatting, ORCID, and a separate title page. Final checks; it does not draft content.
---

# Submission Preflight (aerj-submission)

The last check before pressing submit on **ScholarOne Manuscript Central**. AERJ is **masked**, so the
single most common avoidable failure is an under-anonymized manuscript or identifying metadata. Verify
volatile specifics on the official page before relying on them.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata ScholarOne expects
- Confirming the section choice, length/abstract limits, masking, and APA compliance

## Process facts (verify volatile items on the official page)

- **Owner / publisher:** American Educational Research Association (AERA) / SAGE.
- **Portal:** **ScholarOne Manuscript Central** (confirm the current URL on the guidelines page).
- **Section:** choose **SIA** or **TLHD** at submission (separately edited).
- **Review model:** **masked (anonymous)** — names only on the **separate title page file**.
- **Length:** manuscripts **~20–50 pages**, double-spaced, 12-pt, 1" margins, **inclusive** of tables,
  figures, notes, and references (待核实 — confirm current figure and what counts).
- **Abstract:** **100–120 words** (待核实).
- **Style:** **APA 7th edition** (author-date).
- **ORCID:** provide for the corresponding author.
- **Fee:** no submission fee stated; AERA membership not required to submit; gold OA via **SAGE
  Choice** for a fee (待核实).

## Preflight checklist

### Section & length
- [ ] Section chosen (**SIA / TLHD**) and justified if it straddles both
- [ ] Manuscript within the page limit, including tables/figures/notes/references (verify)
- [ ] Abstract **100–120 words**, stating purpose + method + finding + significance

### Masking (anonymous review)
- [ ] No author names/affiliations/acknowledgments in the manuscript file
- [ ] No identifying citations, references, or footnotes ("as we showed in…" neutralized)
- [ ] Identifying **file metadata stripped** (document properties, comments)
- [ ] Separate **title page file** with all author/affiliation/contact details
- [ ] Anonymized preregistration / OSF link if referenced

### Format & metadata
- [ ] **APA 7th edition** formatting; consistent author-date citations and reference list
- [ ] Double-spaced, 12-pt, 1" margins
- [ ] Corresponding-author **ORCID** ready
- [ ] Figures/tables self-contained, accessible, anonymized (see `aerj-tables-figures`)

### Compliance & materials
- [ ] IRB / human-subjects / consent compliance per AERA ethics
- [ ] Reporting meets the AERA standard for the method (see `aerj-transparency-and-data-policy`)
- [ ] Data/code availability or access plan documented

## Anti-patterns

- Leaving author identifiers in the text, acknowledgments, or file metadata (breaks masking)
- Abstract outside 100–120 words; manuscript over the page limit
- Submitting to the wrong section
- Mixing citation styles instead of clean APA 7th
- Budgeting for a submission fee that is not charged (verify)

## Output format

```
【Section】SIA / TLHD (justified? Y/N)
【Masked】text + self-refs + file metadata clean + separate title page? [Y/N]
【Abstract】word count (100–120)
【Length】within limit incl. tables/figures/refs? [Y/N]
【APA 7th + ORCID】[Y/N]
【Reporting + data plan】ready? [Y/N]
【Next】await decision → aerj-rebuttal on R&R
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — APA reference managers, anonymization, repro tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official AERJ submission facts (待核实 on volatile items)
