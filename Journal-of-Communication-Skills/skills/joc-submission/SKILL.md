---
name: joc-submission
description: Use when running the final pre-submission preflight for the Journal of Communication (JoC) via Manuscript Central — format selection, double-anonymous preparation, page/abstract caps, APA-7th formatting, Word (.docx), the Data Availability Statement, and declarations. Final checks; it does not draft content.
---

# Submission Preflight (joc-submission)

The last check before pressing submit on **Manuscript Central**. JoC is **double-anonymous**, so the
single most common avoidable failure is an under-anonymized main document or supplement. Verify
volatile specifics on the official page before relying on them.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata Manuscript Central expects
- Confirming the page/abstract caps are met and the manuscript is properly anonymized

## Process facts (verify volatile items on the official page)

- **Owner / publisher:** International Communication Association (ICA) / Oxford University Press.
- **Portal:** **Manuscript Central** (`mc.manuscriptcentral.com/jcom`).
- **Review model:** **double-anonymous** — anonymize the main document **and** supplemental materials;
  provide a separate title page.
- **Formats:** original research article (main document ≤ 35 pages), **JoC Forum** (3,000–6,000 words),
  special-issue submissions.
- **Abstract:** **≤ 150 words.**
- **Length:** main document **≤ 35 pages**, including the abstract, main text, references, tables,
  figures, and endnotes.
- **Style & file:** **APA 7th edition**; **Microsoft Word (.docx)** (PDF not accepted); 12-pt Times New
  Roman, double-spaced, 1.0-inch margins.
- **Self-citations:** written in the **third person**.
- **Transparency:** **Data Availability Statement required**; note any **preregistration** in the cover
  letter; deposit **Open Science Badge** materials if claiming a badge.
- **Fee:** no submission fee stated; hybrid **open-access APC** handled by OUP after acceptance (待核实).

## Preflight checklist

### Format & length
- [ ] Format chosen and its cap met (article ≤ 35 pages / Forum 3,000–6,000 words)
- [ ] Page count includes abstract, text, references, tables, figures, endnotes
- [ ] Abstract ≤ 150 words, states question + approach + finding

### Anonymity (double-anonymous)
- [ ] No author names, affiliations, or acknowledgments in the **main document**
- [ ] **Supplemental materials also anonymized** (no identifying links/paths)
- [ ] **Self-citations in the third person** ("Smith and Lee (2024) showed…", not "as we showed…")
- [ ] Identifying **file metadata stripped** (document properties, comments)
- [ ] Separate (non-anonymous) title page with contact info + brief bio prepared as a distinct file

### Format & metadata
- [ ] APA 7th edition formatting; consistent author-date citations
- [ ] **Word (.docx)**, 12-pt Times New Roman, double-spaced, 1.0-inch margins
- [ ] Figures/tables self-contained, accessible (see `joc-tables-figures`)

### Compliance & files
- [ ] Ethics / IRB / human-subjects compliance
- [ ] **Data Availability Statement** included; preregistration noted in cover letter if applicable
- [ ] Open Science Badge materials staged if a badge is claimed (see `joc-open-science-and-transparency`)

## Anti-patterns

- Leaving author identifiers in the text, supplements, or file metadata (breaks anonymity)
- First-person self-references ("as we previously found") instead of third-person
- Submitting a PDF when JoC requires Word (.docx)
- Abstract over 150 words; main document over 35 pages
- Omitting the Data Availability Statement

## Output format

```
【Format】Article / JoC Forum / Special issue (cap met? Y/N)
【Anonymized】main doc + supplements + file metadata clean? [Y/N]
【Self-citations third person】[Y/N]
【Abstract】word count (≤150)
【Length】≤ 35 pages incl. refs/tables/figures/endnotes? [Y/N]
【APA 7th + Word .docx】[Y/N]
【Data Availability Statement】included? [Y/N]
【Next】await decision → joc-rebuttal on R&R
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers, anonymization, repro tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official JoC URLs behind every fact in this pack
