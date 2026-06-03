---
name: pmla-submission
description: Use when running the final pre-submission preflight for PMLA (Publications of the Modern Language Association) via the ScholarOne site — venue selection, MLA-membership eligibility, anonymous preparation, word range, MLA style, cover sheet, and AI-content disclosure. Final checks; it does not draft content.
---

# Submission Preflight (pmla-submission)

The last check before submitting on **PMLA's ScholarOne site** (`mc.manuscriptcentral.com/pmla`). PMLA
is **anonymous (blind)**, so the most common avoidable failure is a self-identifying manuscript — and
the most common eligibility failure is a non-member author. Verify volatile specifics on the official
page before relying on them.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata ScholarOne expects
- Confirming the word range is met and the manuscript is properly anonymized

## Process facts (verify volatile items on the official page)

- **Owner / publisher:** Modern Language Association (MLA) / Cambridge University Press.
- **Portal:** **PMLA's ScholarOne** (`mc.manuscriptcentral.com/pmla`); submit a **Word file**.
- **Eligibility:** the author and **all coauthors must be MLA members**; the essay must be
  **unpublished** (in any language) and **not under consideration elsewhere**; a revised version of a
  previously submitted PMLA manuscript is **not** considered.
- **Review model:** **anonymous (blind)** — anonymize the manuscript; supply a separate cover sheet.
- **Venues:** regular article (6,000–9,000 words); special features — Theories and Methodologies, The
  Changing Profession (~3,500 words, 待核实), Criticism in Translation, Little-known Documents.
- **Word count:** **6,000–9,000 words** for articles; **includes discursive notes**; **excludes** the
  list of works cited and translations.
- **Style:** **MLA style** per the most recent **MLA Handbook** (in-text + Works Cited).
- **AI disclosure:** fully **cite, at submission, any content created by an AI tool**.
- **Abstract:** not requested for regular articles; a **100-word abstract** applies to special-feature
  proposals (待核实 — confirm on the live page).

## Preflight checklist

### Venue & length
- [ ] Venue chosen; word range met (article 6,000–9,000; special feature ~3,500 — verify)
- [ ] Count includes discursive notes; excludes Works Cited and translations; proposal abstract ≤ 100 words if applicable (待核实)

### Anonymity (blind review)
- [ ] No author name in the manuscript text or notes; acknowledgments removed
- [ ] References to your own prior work are in the **third person**, not first
- [ ] Identifying **file metadata stripped**; separate **cover sheet** (name, address, title) prepared

### Eligibility & format
- [ ] Author and all coauthors are **current MLA members**
- [ ] Essay is unpublished and not under review elsewhere; not a resubmitted prior PMLA manuscript
- [ ] AI-generated content (if any) fully cited at submission
- [ ] MLA style per the current MLA Handbook; in-text ↔ Works Cited consistent (see `pmla-citation-and-style`)
- [ ] Quotations exact; translation policy applied; submitted as a Word file per ScholarOne

## Anti-patterns

- Leaving author name, acknowledgments, or first-person self-references in the manuscript (breaks anonymity)
- Submitting without MLA membership for every author
- Sending a regular-article-length piece to a special feature (or vice versa)
- Resubmitting a previously declined PMLA manuscript as a "revision"
- Using a non-MLA citation style

## Output format

```
【Venue】article / Theories & Methodologies / Changing Profession / Translation / Little-known Documents (range met? Y/N)
【Eligibility】all authors MLA members? unpublished? not under review elsewhere? [Y/N]
【Anonymized】no name/first-person self-ref; metadata clean; cover sheet ready? [Y/N]
【Word count】6,000–9,000 (notes counted; Works Cited/translations not)?
【MLA style + AI disclosure】[Y/N]
【Next】await decision → pmla-revision-and-response if asked to revise
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — ScholarOne portal, MLA-style and anonymization tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official PMLA URLs behind every fact in this pack
