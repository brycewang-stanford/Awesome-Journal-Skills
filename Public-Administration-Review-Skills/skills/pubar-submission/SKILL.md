---
name: pubar-submission
description: Use when running the final pre-submission preflight for Public Administration Review (PAR) — article-type selection, double-blind preparation, the ≤ 8,000-word and ≤ 150-word-abstract caps, Evidence for Practice points, APA formatting, and TOP transparency materials. Final checks; it does not draft content.
---

# Submission Preflight (pubar-submission)

The last check before pressing submit. PAR is **double-blind**, so the single most common avoidable
failure is an under-anonymized manuscript, followed by missing **Evidence for Practice** points. Verify
volatile specifics on the official page before relying on them.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata the portal expects
- Confirming the chosen article type's expectations are met and the manuscript is anonymized

## Process facts (verify volatile items on the official page — 检索于 2026-06-22；以官网为准)

- **Owner / publisher:** American Society for Public Administration (ASPA) / **Wiley**.
- **Editors (re-verified 2026-06-22):** Editors-in-Chief **Jos Raadschelders** (Ohio State) and
  **Katherine Willoughby** (University of Georgia); **Editor Hongtao Yi** (Ohio State); term **2024–2026**.
  Because the term runs through 2026, re-confirm the masthead on the editorial-board page before submitting.
- **Portal:** online submission system — the PAR submission page lists **Editorial Manager**
  (`editorialmanager.com/par`); some older guidance and the task seed reference **ScholarOne /
  Manuscript Central**. **Confirm the live portal before submitting.** 待核实.
- **Review model:** **double-blind** — anonymize the manuscript; separate title page.
- **Article types:** Scholarly Take, Conceptualizing Public Administration, Early Career Intel,
  Practically Speaking, Public Administration in Print (book reviews).
- **Word count:** **≤ 8,000 words including abstract, endnotes, and references**; **tables, figures,
  charts, and appendices are excluded.**
- **Abstract:** **≤ 150 words**, on a page preceding the first page of the manuscript.
- **Evidence for Practice:** **3–5** sentence-length takeaway points for practitioners — encouraged at
  submission, **required at revision.**
- **Style:** **APA author–date** (confirm current edition).
- **Transparency:** TOP-guideline materials and a data-availability statement (Dataverse / QDR; see
  `pubar-transparency-and-data`).
- **Fee:** **no submission fee** (re-verified 2026-06-22; no source states one); open access is optional
  and would carry a post-acceptance Wiley APC — confirm the current figure only if you opt in.

## Preflight checklist

### Type & length
- [ ] Article type chosen and its expectations met
- [ ] Word count ≤ 8,000 (incl. abstract, endnotes, references; excl. tables/figures/appendices)
- [ ] Abstract ≤ 150 words, states question + approach + finding
- [ ] **Evidence for Practice**: 3–5 takeaway points present (required by revision)

### Anonymity (double-blind)
- [ ] No author names on the title page / in the manuscript
- [ ] Own prior work referred to in the **third person**; self-citations neutralized
- [ ] Acknowledgments, institution names, identifying URLs removed
- [ ] Identifying **file metadata stripped** (document properties, comments)
- [ ] Separate (non-anonymous) title page prepared as a distinct file

### Format & transparency
- [ ] APA author–date formatting; consistent citations
- [ ] Figures/tables self-contained, accessible (see `pubar-tables-figures`)
- [ ] Data-availability statement + TOP materials staged (Dataverse/QDR)
- [ ] Ethics / IRB / human-subjects compliance documented

## Anti-patterns

- Leaving author identifiers in the text, acknowledgments, or file metadata (breaks double-blind)
- Forgetting that **references and endnotes count** toward the 8,000-word limit
- Submitting without Evidence for Practice (required by revision)
- Budgeting for a submission fee that is not charged (verify)
- Submitting to the wrong portal because the system changed — confirm the live URL

## Output format

```
【Article type】Scholarly Take / Conceptualizing PA / Early Career Intel / Practically Speaking
【Word count】≤8,000 incl. abstract/endnotes/refs? [Y/N]
【Abstract】word count (≤150)
【Evidence for Practice】3-5 points present? [Y/N]
【Anonymized】text + self-refs + file metadata clean? [Y/N]
【APA style】[Y/N]
【TOP materials】data-availability statement + repository staged? [Y/N]
【Portal】confirmed live submission URL? [Y/N]
【Next】await decision → pubar-rebuttal on R&R
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — copy-paste preflight checklist
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers, anonymization, repro tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official PAR URLs behind every fact in this pack
