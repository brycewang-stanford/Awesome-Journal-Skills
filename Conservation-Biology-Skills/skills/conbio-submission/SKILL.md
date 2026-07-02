---
name: conbio-submission
description: Use when running the final pre-submission preflight for Conservation Biology via Wiley's ScholarOne Manuscript Central — article-type selection, double-blind preparation, word/abstract caps, Style Guide formatting, data-availability statement, and declarations. Final checks; it does not draft content.
---

# Submission Preflight (conbio-submission)

The last check before pressing submit on **Wiley ScholarOne Manuscript Central**
(`mc.manuscriptcentral.com/cobi`). *Conservation Biology* is **double-blind**, so the single most
common avoidable failure is an under-anonymized manuscript. Check upload-week specifics on the official
page before relying on them (per-type caps can change — see `resources/official-source-map.md`).

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata ScholarOne expects
- Confirming the chosen article type's caps are met and the manuscript is properly anonymized

## Process facts

- **Owner / publisher:** Society for Conservation Biology (SCB) / Wiley.
- **Portal:** **Wiley ScholarOne Manuscript Central** (`mc.manuscriptcentral.com/cobi`).
- **Review model:** **double-blind** — anonymize the manuscript and author identities; provide a
  separate title page.
- **Article types & word limits:** Contributed Papers 7,000 in current Wiley listings; use the live
  Instructions for Authors page for the final caps on Research Notes, Reviews, Essays, Conservation
  Practice and Policy, Comments, Diversity, Letters, and any Registered Reports route.
- **Abstract:** **≤ 300 words** (none for Letters, Comments, or Diversity).
- **Word count:** runs from the **first word of the Abstract through the last word of Literature
  Cited**; **excludes** tables, figure legends, and text in tables.
- **Exhibits:** about **one table/figure per four pages** of text.
- **Style:** *Conservation Biology* **Style Guide** (author-date); IMRAD for Contributed Papers,
  Research Notes, and Practice & Policy.
- **Data:** **data-availability statement** for research/synthesis articles; the journal-specific Wiley
  tier encourages data sharing, so archive shareable data/code in a DOI-capable repository and document
  restrictions for sensitive data.

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

## ScholarOne file manifest (stage the upload in this order)

`cobi` on Manuscript Central expects the pieces as separate files, not one merged PDF. Assemble:

1. **Anonymized main document** — blinded manuscript with the abstract, IMRAD body, Literature Cited,
   and the Supporting Information paragraph; no names, affiliations, or acknowledgments.
2. **Separate title page** — the non-anonymous file carrying authors, affiliations, ORCID, and the
   corresponding author. Keep it out of the blinded document entirely.
3. **Figures, tables, and maps** — self-contained, colorblind-safe, legible in grayscale, with sensitive
   localities masked (see `conbio-figures-and-tables`).
4. **Supporting Information** — full model output, balance/sensitivity runs, protocols.
5. **Statements** — data-availability statement, ethics/permits/animal-care/human-subjects declarations,
   and any conflict-of-interest text.

Confirm the exact file prompts, declaration wording, and any per-type caps on the live Wiley Instructions
for Authors page during upload week; treat all of them as live-check items.

## Anonymization scrub sequence (the most common avoidable failure)

Run these in order before the blinded document is final:

- Strip **document metadata**: author name in file properties, tracked-change authorship, comment
  initials, and the PDF producer/author fields.
- Neutralize **self-citation**: change "as we showed in (Author 2021)" to "as shown in (Author 2021)";
  keep the reference in Literature Cited so the argument is intact.
- Blind **fieldwork tells**: an unusual site name, a named permit number, or a lab-specific dataset can
  identify the group as surely as a byline — describe the site generically in the blinded copy.
- Move all **acknowledgments and funding** to the title page; they routinely leak identity.

## Anti-patterns

- Leaving author identifiers in the text, acknowledgments, or file metadata (breaks double-blind)
- Merging the title page into the blinded manuscript instead of uploading it as a separate file
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
