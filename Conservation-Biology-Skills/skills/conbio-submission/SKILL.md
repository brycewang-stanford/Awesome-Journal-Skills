---
name: conbio-submission
description: Use when running the final pre-submission preflight for Conservation Biology via Wiley's ScholarOne Manuscript Central — article-type selection, double-blind preparation, word/abstract caps, Style Guide formatting, data-availability statement, and declarations. Final checks; it does not draft content.
---

# Submission Preflight (conbio-submission)

The last check before pressing submit on **Wiley ScholarOne Manuscript Central**
(`mc.manuscriptcentral.com/cobi`). *Conservation Biology* is **double-blind**, so the single most
common avoidable failure is an under-anonymized manuscript. Verify volatile specifics on the official
page before relying on them (per-type caps drift — see `resources/official-source-map.md`).

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata ScholarOne expects
- Confirming the chosen article type's caps are met and the manuscript is properly anonymized

## Process facts (verify volatile items on the official page)

- **Owner / publisher:** Society for Conservation Biology (SCB) / Wiley.
- **Portal:** **Wiley ScholarOne Manuscript Central** (`mc.manuscriptcentral.com/cobi`).
- **Review model:** **double-blind** — anonymize the manuscript and author identities; provide a
  separate title page.
- **Article types & word limits (verify; versions drift):** Contributed Papers ~6,000–7,000 · Research
  Notes ~3,000 · Reviews ~7,500–8,000 · Essays ~6,000 · Conservation Practice and Policy 5,000 ·
  Comments 2,000 · Diversity 2,000 · Letters 1,000.
- **Abstract:** **≤ 300 words** (none for Letters, Comments, or Diversity).
- **Word count:** runs from the **first word of the Abstract through the last word of Literature
  Cited**; **excludes** tables, figure legends, and text in tables.
- **Exhibits:** about **one table/figure per four pages** of text.
- **Style:** *Conservation Biology* **Style Guide** (author-date); IMRAD for Contributed Papers,
  Research Notes, and Practice & Policy.
- **Data:** **data-availability statement** + deposit of data/code in a public repository (e.g., Dryad)
  with a persistent identifier (待核实 on exact mandatory wording).

## Preflight checklist

### Article type & length
- [ ] Article type chosen and its word cap met (count Abstract → Literature Cited)
- [ ] Abstract ≤ 300 words, states problem + approach + finding (omit where the type forbids it)
- [ ] Exhibit count within ~one per four pages; extras moved to Supporting Information

### Anonymity (double-blind)
- [ ] No author names, affiliations, or acknowledgments in the manuscript
- [ ] Self-references neutralized ("as we showed in…" removed)
- [ ] Identifying **file metadata stripped** (document properties, comments)
- [ ] Separate (non-anonymous) title page prepared as a distinct file

### Format & content
- [ ] Style Guide formatting; consistent author-date citations; title-style rules followed
- [ ] IMRAD order where required; no combined Results/Discussion; no separate Conclusion
- [ ] Figures/tables/maps self-contained and accessible; sensitive localities masked
      (see `conbio-figures-and-tables`)
- [ ] **Conservation relevance** stated explicitly (see `conbio-conservation-relevance-and-implications`)

### Compliance & data
- [ ] Ethics / permits / animal-care / human-subjects compliance stated
- [ ] **Data-availability statement** drafted; data/code package staged for a public repository
      (see `conbio-reporting-and-data-policy`)
- [ ] Sensitive-species data masked; restricted-data access path provided

## Anti-patterns

- Leaving author identifiers in the text, acknowledgments, or file metadata (breaks double-blind)
- Abstract over 300 words; word count outside the chosen type's cap
- Sending a long paper to the Research Note or Comment type
- Choosing Registered Reports after results exist
- Submitting with no data-availability statement or with sensitive locations exposed

## Output format

```
【Article type】Contributed Paper / Note / Review / Essay / Practice & Policy / Comment (cap met? Y/N)
【Anonymized】text + self-refs + file metadata clean? [Y/N]
【Abstract】word count (≤300, or N/A)
【Word count】within cap (Abstract→Literature Cited)? [Y/N]
【Style Guide + IMRAD + title rules】[Y/N]
【Data-availability statement + package staged】[Y/N]
【Next】await decision → conbio-revision-and-rebuttal on revision
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers, anonymization, repro tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official Conservation Biology URLs behind every fact in this pack
