---
name: gec-submission
description: Use when running the final pre-submission preflight for Global Environmental Change (GEC) via Editorial Manager — format selection, double-blind anonymization, word and abstract caps, Highlights, the Data Availability Statement, declarations, and ORCID. Final checks; it does not draft content.
---

# Submission Preflight (gec-submission)

The last check before pressing submit on **Editorial Manager**. GEC is **double-blind** (verify), so a
common avoidable failure is an under-anonymized manuscript; the others are missing **Highlights** and a
missing **Data Availability Statement**. Verify volatile specifics on the official Guide for Authors —
several Elsevier pages return 403 to automated fetches, so some figures below are 待核实.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata Editorial Manager expects
- Confirming caps are met and the manuscript is properly anonymized

## Process facts (verify volatile items on the official page)

- **Publisher:** **Elsevier** (ISSN 0959-3780 print / 1872-9495 online).
- **Portal:** **Editorial Manager** (`editorialmanager.com/gec`).
- **Review model:** **double-blind** — anonymize the manuscript; provide a separate title page. 待核实.
- **Article length:** Research Articles **up to ~8,000 words** (incl. main text and table/figure
  captions, **excl.** references; longer occasionally if warranted). 待核实 on the exact cap.
- **Abstract:** **≤ ~250 words.** 待核实.
- **Highlights:** **3-5 bullets, ≤ ~85 characters each**, as a separate editable file. 待核实.
- **References:** current Elsevier style (numbered `elsarticle` vs. author-date) — confirm. 待核实.
- **Data:** Elsevier research-data policy; include a **Data Availability Statement**. 待核实 on level.
- **Fee:** subscription route (no author fee) or gold OA with an **APC** (quoted ~USD 6,120). 待核实.

## Preflight checklist

### Format & length
- [ ] Article type chosen and its word cap met (Research Article ~8,000 words, excl. refs)
- [ ] Abstract ≤ ~250 words; states problem + approach + finding + significance
- [ ] Highlights: 3-5 bullets, ≤ ~85 chars each, separate editable file

### Anonymity (double-blind)
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
- [ ] **Data Availability Statement** + clean replication archive (data + code) staged
- [ ] Suggested reviewers (if requested) span the relevant disciplines

## Anti-patterns

- Leaving author identifiers in the text, acknowledgments, or file metadata (breaks double-blind)
- Abstract over the cap; missing or off-spec Highlights
- No Data Availability Statement; a results section the archive cannot reproduce
- Budgeting an APC when the subscription route is free to the author (verify)
- Sending a natural-science-only paper (see `gec-review-process` scope screen)

## Output format

```
【Article type】Research Article / Perspective / Review (caps met? Y/N)
【Anonymized】text + self-refs + file metadata clean? [Y/N]
【Abstract】word count (≤ ~250)
【Highlights】3-5 bullets, ≤85 chars each? [Y/N]
【Data Availability Statement + archive】[Y/N]
【Declarations + ORCID】[Y/N]
【Next】await decision → gec-revision-and-rebuttal on revision
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers, anonymization, and repository tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official GEC URLs behind every fact in this pack
