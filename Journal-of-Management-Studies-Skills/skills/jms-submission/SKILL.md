---
name: jms-submission
description: Use when running the final pre-submission preflight for a Journal of Management Studies (JMS) manuscript via the Wiley ScholarOne portal — anonymisation for double-blind review, Harvard referencing, the inclusive word count, article type, and the anonymous title page. Final checks; it does not draft content.
---

# Submission Preflight (jms-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on ScholarOne
- Unsure which files JMS expects (anonymised manuscript + separate title page)
- Confirming the manuscript meets double-blind anonymisation and house format
- Choosing the right article type (Original, Review, Point–CounterPoint, JMS Says)

## Process facts (source map refreshed 2026-06; re-confirm on the official Wiley/SAMS pages)

- JMS is the **Society for the Advancement of Management Studies (SAMS)** journal, published by **Wiley**; content is hosted on **Wiley Online Library** (the journal home is `onlinelibrary.wiley.com/journal/14676486`). The editorial office is at **Durham University**. `(检索于 2026-06；以官网为准)`
- **Submission portal:** Wiley **ScholarOne / Manuscript Central** at **mc.manuscriptcentral.com/jmstudies**. `(检索于 2026-06；以官网为准)`
- **Review model:** **double-blind**. The manuscript must be **fully anonymised** (no author names, no identifying self-citations in the first person, no acknowledgements that reveal identity); author details go on a **separate title page** uploaded as a distinct file.
- **Length:** typically **10,000–13,000 words inclusive of tables, figures, and references**; manuscripts substantially over (e.g., >15,000) may be returned for reduction before review. `(检索于 2026-06；以官网为准)`
- **Abstract:** **≤200 words**; **4–6 keywords** in alphabetical order. `(检索于 2026-06；以官网为准)`
- **Article types:** Original Articles, Review Articles, Special Issues, **Point–CounterPoints** (Point ~9,000–12,000 words; CounterPoint ~7,000 words, editorially curated), and **JMS Says** essays. Confirm the current set and length rules. `(检索于 2026-06；以官网为准)`
- **No submission fee** is charged at submission for standard articles; open-access APCs apply only if the author chooses OA at acceptance (Wiley hybrid). Do not treat any APC as a submission-time fee. `(verified 2026-06-22; re-verify the exact OA APC figure before submission)`
- **General Editors (team-based; no single EiC):** **Johann Fortwengel, Corinne Post, and Kristina Potočnik** (verified 2026-06-22 via Wiley/SAMS; re-verify before naming an editor in a cover letter).

## Preflight checklist

### Anonymisation (double-blind)
- [ ] Manuscript contains **no author names**, affiliations, or identifying acknowledgements
- [ ] Self-citations phrased in the **third person** ("Smith (2019) found…", not "in our prior work")
- [ ] File metadata/properties scrubbed of author identity
- [ ] **Separate title page** file with names, affiliations, ORCID, corresponding author, acknowledgements, and funding

### Format & house style
- [ ] **Double-spaced** throughout, including notes and references
- [ ] **Harvard author-date** referencing; alphabetical reference list; page numbers for quotations
- [ ] **Endnotes only** (no footnotes), kept minimal
- [ ] Tables numbered with **Roman numerals**, figures with **Arabic numerals**; each exhibit self-sufficient
- [ ] **UK or US English**, consistent throughout
- [ ] **Abstract ≤200 words**; **4–6 alphabetical keywords**
- [ ] Total length within the **inclusive** 10,000–13,000-word budget

### Article type & declarations
- [ ] Correct article type selected on ScholarOne (Original / Review / Point–CounterPoint / JMS Says)
- [ ] **AI use declared** (including copy-editing) per current policy
- [ ] Data/transparency statement included if required for the design
- [ ] Confirmed the paper is not under review elsewhere; no AI listed as an author

## Anti-patterns

- Submitting a manuscript that reveals authorship (first-person self-citations, acknowledgements, metadata)
- Wrong referencing style (numbered/APA instead of Harvard author-date)
- Forgetting that the word count is **inclusive** of tables/figures/references — then exceeding it
- Footnotes instead of endnotes; figures/tables mis-numbered against house style
- Treating a Point–CounterPoint or JMS Says as a normal Original Article
- Confusing an OA APC with a submission fee

## Output format

```text
【Anonymisation】no author identity in manuscript + separate title page? [Y/N]
【Referencing】Harvard author-date, alphabetical, double-spaced, endnotes only? [Y/N]
【Abstract】≤200 words + 4–6 alphabetical keywords? [Y/N]
【Length】within inclusive 10,000–13,000 words? [Y/N]
【Article type】Original / Review / Point–CounterPoint / JMS Says selected correctly? [Y/N]
【Declarations】AI use + data/transparency statement? [Y/N]
【Next step】submit via ScholarOne → jms-review-process for what to expect
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — submission self-check
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — lightweight manuscript scaffold
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official URLs and volatile facts
