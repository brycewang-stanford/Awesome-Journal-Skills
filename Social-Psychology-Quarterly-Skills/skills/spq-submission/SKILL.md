---
name: spq-submission
description: Use when running the final pre-submission preflight for Social Psychology Quarterly (SPQ) via SageTrack / ScholarOne Manuscript Central — article type, blinded manuscript plus separate title page, word/abstract caps, keywords, ASA Style Guide formatting, the $25 processing fee and its waivers, and ethics. Final checks; it does not draft content.
---

# Submission Preflight (spq-submission)

The last check before pressing submit on **SageTrack / ScholarOne Manuscript Central**. SPQ is **masked**,
so the single most common avoidable failure is an under-blinded manuscript — which the editorial office
will **temporarily reject** and return for reformatting. Live-check SageTrack for the current upload
fields and payment prompt before relying on a saved checklist.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata SageTrack expects
- Confirming the chosen article type's caps are met and the manuscript is properly blinded

## Process facts

- **Owner / publisher:** American Sociological Association (ASA) / SAGE.
- **Portal:** **SageTrack / ScholarOne Manuscript Central** (create an account if you have not used it for
  another ASA journal).
- **Review model:** **masked / blinded** — a blinded manuscript file **plus a separate title page** file.
- **Article types:** **Article** (≤ 10,000 words, all parts, excl. supplementary materials) and **Note**
  (≤ 5,000 words). Do not assume a Registered Reports track for SPQ unless it appears in the live
  SageTrack options.
- **Abstract:** **~150 words**, **non-identifying**, on a separate page headed by the title; **author
  names omitted**; a few **keywords** after the abstract.
- **Title page (separate file):** full title, author(s) and affiliation(s), running head, and the
  **approximate word count** (including notes and references).
- **Style:** **ASA Style Guide** (author-date).
- **Fee:** **$25** ASA manuscript processing fee on **first** submission; **not** charged for
  revised/resubmitted manuscripts or for **ASA student members** (via the "ASA Student Member
  Submission" article type). *(Verified 2026-06-22; SAGE author page may 403 to automated checks —
  re-confirm the live fee workflow before upload.)*

## Preflight checklist

### Type & length
- [ ] Article (≤ 10,000) or Note (≤ 5,000) chosen and its word cap met (supplementary materials excluded)
- [ ] Approximate word count (incl. notes and references) on the **title page**
- [ ] Abstract ~150 words, non-identifying, with keywords; author names omitted from the abstract page

### Masking (blinded review)
- [ ] Blinded manuscript: no author names, affiliations, or acknowledgments in the manuscript file
- [ ] Self-citations phrased non-identifyingly (you *may* cite your own work, just not "as we showed…")
- [ ] Identifying **file metadata stripped** (document properties, comments)
- [ ] Separate **title page** file prepared (title, authors, affiliations, running head, word count)

### Format & compliance
- [ ] ASA Style Guide formatting; consistent author-date citations
- [ ] Figures/tables self-contained and accessible (see `spq-tables-figures`)
- [ ] Ethics / IRB / consent / confidentiality per ASA Code of Ethics
- [ ] Data/materials posture decided and stated honestly (encouraged, not required — see `spq-data-and-transparency`)
- [ ] **$25 processing fee** ready (or student/resubmission waiver applies)

## Anti-patterns

- Leaving author identifiers in the text, acknowledgments, or file metadata (temporary rejection)
- Abstract over ~150 words, identifying, or missing keywords
- No word count on the title page
- Sending a long paper to the Note type
- Treating the data policy as a mandate, or budgeting/skipping the $25 fee incorrectly (verify waiver)

## Output format

```
【Type】Article (≤10,000) / Note (≤5,000) — cap met? [Y/N]
【Blinded】manuscript clean + separate title page? [Y/N]
【Abstract】~150 words, non-identifying, keywords? [Y/N]
【Word count on title page】incl. notes + references? [Y/N]
【ASA style】[Y/N]
【$25 fee】paid or waiver (resubmission / ASA student) applies? [Y/N]
【Next】await decision → spq-rebuttal on R&R
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers, blinding, and repro tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official SPQ URLs behind every fact in this pack
