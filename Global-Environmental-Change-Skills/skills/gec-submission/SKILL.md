---
name: gec-submission
description: Use when running the final pre-submission preflight for Global Environmental Change (GEC) via Elsevier's online submission system — format selection, double-anonymized files, word and abstract caps, Highlights, the Data Availability Statement, declarations, and ORCID. Final checks; it does not draft content.
---

# Submission Preflight (gec-submission)

The last check before pressing submit through Elsevier's online submission system. GEC is
**double-anonymized**, so a
common avoidable failure is an under-anonymized manuscript; the others are missing **Highlights** and a
missing **Data Availability Statement**. Facts below were refreshed from the official Guide for Authors
on 2026-06-20; re-check live pages before filing.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata Elsevier's submission system expects
- Confirming caps are met and the manuscript is properly anonymized

## Process facts (verified 2026-06-20; re-confirm volatile items on the official page)

- **Publisher:** **Elsevier** (ISSN 0959-3780 print / 1872-9495 online).
- **Portal:** Elsevier's online submission system.
- **Review model:** **double-anonymized** — submit a title page and anonymized manuscript as separate
  files.
- **Article length:** Research Articles **up to 8,000 words** (including main text and table/figure
  captions, excluding references); Perspectives **up to 3,000 words** (excluding references).
- **Abstract:** **<=250 words**.
- **Keywords:** **1-7 English keywords** for indexing.
- **Highlights:** required, **3-5 bullets**, **<=85 characters each including spaces**, as a separate
  editable file.
- **References:** any internally consistent style at submission; the journal style is applied after
  acceptance at proof.
- **Data:** Elsevier **Option C** applies: deposit/cite/link research data, or explain why it cannot be
  shared; prepare a **Data Availability Statement**.
- **Publishing fee:** subscription route has no author publication fee; gold OA APC is **USD 6,120**
  excluding taxes (verified 2026-06-22; re-check the live ScienceDirect figure before submission).

## Preflight checklist

### Format & length
- [ ] Article type chosen and its word cap met (Research Article 8,000 words; Perspective 3,000 words)
- [ ] Abstract <=250 words; states problem + approach + finding + significance
- [ ] 1-7 English keywords chosen
- [ ] Highlights: 3-5 bullets, <=85 chars each, separate editable file

### Anonymity (double-anonymized)
- [ ] No author names, affiliations, or acknowledgments in the manuscript
- [ ] Self-citations neutralized; no obvious self-references
- [ ] Identifying **file metadata stripped** (document properties, comments)
- [ ] Separate (non-anonymous) title page prepared as a distinct file

### Format & metadata
- [ ] Elsevier formatting and reference style applied consistently
- [ ] Corresponding-author **ORCID** ready (Elsevier requirement)
- [ ] Figures/tables self-contained and accessible (see `gec-figures-and-tables`)

### Compliance & files
- [ ] **Declaration of competing interests** and any funding statement included
- [ ] Ethics / IRB / human-subjects compliance and consent where applicable
- [ ] **Option C data plan**: deposit/cite/link research data, or explain why sharing is restricted
- [ ] **Data Availability Statement** + clean replication materials staged where sharing is possible
- [ ] Suggested reviewers (if requested) span the relevant disciplines

## Anti-patterns

- Leaving author identifiers in the text, acknowledgments, or file metadata (breaks double-anonymized review)
- Abstract over the cap; missing or off-spec Highlights
- No Data Availability Statement; a results section the archive cannot reproduce
- Budgeting an APC when the subscription route is free to the author
- Sending a natural-science-only paper (see `gec-review-process` scope screen)

## Output format

```
【Article type】Research Article / Perspective / other (caps met? Y/N)
【Anonymized】text + self-refs + file metadata clean? [Y/N]
【Abstract / keywords】<=250 words + 1-7 English keywords? [Y/N]
【Highlights】3-5 bullets, <=85 chars each? [Y/N]
【Option C data plan + Data Availability Statement】[Y/N]
【Declarations + ORCID】[Y/N]
【Next】await decision → gec-revision-and-rebuttal on revision
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers, anonymization, and repository tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official GEC URLs behind every fact in this pack
