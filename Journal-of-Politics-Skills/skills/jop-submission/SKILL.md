---
name: jop-submission
description: Use when running the final pre-submission preflight for The Journal of Politics (JOP) via Editorial Manager — category selection, double-blind preparation, the page budget (Research Article <= 35 / Short Article <= 10, double-spaced 12-point), the Online Appendix <= 25 pages, abstract and keywords, and JOP Style Guide formatting. Final checks; it does not draft content.
---

# Submission Preflight (jop-submission)

The last check before pressing submit on **Editorial Manager** (`editorialmanager.com/jop`). Two JOP
failure modes dominate: an **over-the-page-budget** manuscript (JOP counts **pages, not words**) and an
**under-anonymized** file (JOP is **double-blind**). Verify volatile specifics on the official page first.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata Editorial Manager expects
- Confirming the category's page limit is met and the manuscript is properly anonymized

## Process facts (refreshed 2026-06-20; live-check volatile items on the official page)

- **Owner / publisher:** Southern Political Science Association (SPSA) / University of Chicago Press.
- **Portal:** **Editorial Manager** (`editorialmanager.com/jop`).
- **Review model:** **double-blind** — upload an anonymous version; provide a separate title page.
- **Categories & length:** **Research Article ≤ 35 pages**, **Short Article ≤ 10 pages**, each
  **double-spaced, 12-pt, one-inch margins**, **including** text, footnotes, references, and tables/figures.
- **Online Appendix:** separate file, **≤ 25 pages**, **excluded** from the 35-page limit.
- **Abstract:** **≤ 150 words** (question + approach + findings; no citations); **4–5 keywords**.
- **Style:** **The JOP Style Guide** (house author-date).
- **Fee:** no submission/upload-stage charge (verified 2026-06-22 — UChicago Press author
  instructions/open-access page state no submission fee; green self-archiving is free). Gold OA is
  optional and granted at the editor's discretion (typically for funder mandates); a UChicago OA
  request fee around **USD 2,500** has been cited — confirm the current figure on the live page.

## Preflight checklist

### Category & length (pages, not words)
- [ ] Category chosen and its **page limit** met (Research ≤ 35 / Short ≤ 10)
- [ ] Manuscript **double-spaced, 12-pt, one-inch margins** — measured at the real page count
- [ ] Footnotes, references, and exhibits counted toward the limit
- [ ] Online Appendix is a separate file and **≤ 25 pages**
- [ ] Abstract ≤ 150 words (no citations); **4–5 keywords** listed

### Anonymity (double-blind)
- [ ] No author names, affiliations, or acknowledgments in the manuscript
- [ ] No first-person self-references ("as we showed in…"); self-citations in third person
- [ ] Identifying **file metadata stripped** (document properties, comments)
- [ ] Separate (non-anonymous) title/abstract page prepared as a distinct file

### Format & compliance
- [ ] JOP Style Guide formatting; consistent author-date citations
- [ ] Figures/tables self-contained and code-generated (see `jop-tables-figures`)
- [ ] Ethics / IRB / human-subjects compliance addressed
- [ ] Replication package staged for the JOP Dataverse, ready for the analyst at conditional acceptance
      (see `jop-replication-and-data-policy`)

## Anti-patterns

- Editing to a word count and submitting an over-the-page-budget manuscript
- Leaving author identifiers in the text, acknowledgments, or file metadata (breaks anonymity)
- Online Appendix over 25 pages, or smuggling main-text content into it to dodge the 35-page cap
- Sending a long paper to the Short Article category
- Budgeting for an upload-stage charge without checking the live Editorial Manager/UChicago screen

## Desk-reject triggers at the upload gate

These are the avoidable failures that bounce a JOP submission before review. The page-budget and
anonymity screens are mechanical, so clearing them is non-negotiable; the editorial fit screen is handled
in `jop-review-process`.

| Trigger | Why it bounces | The fix before you upload |
|---------|----------------|---------------------------|
| Measured at a word count, not pages | JOP counts double-spaced 12-pt pages incl. notes/refs/exhibits | Re-measure the formatted PDF; cut to the appendix |
| Shrunk spacing/exhibits to "save pages" | Violates the format spec | Format to spec, then cut content, not spacing |
| Author name in a footnote or PDF metadata | Breaks double-blind | Strip metadata; scrub acknowledgments and self-refs |
| Long paper into the Short Article category | Mismatched scope and length | Confirm category against the measured page count |

## Worked micro-example (illustrative)

A hypothetical comparative-politics paper measures 11,800 words and clears the AJPS word ceiling, so the
author assumes it is short enough. Formatted to JOP's spec — double-spaced, 12-pt, with the reference list
and four exhibits counted — it lands at 39 pages (illustrative), four over the Research Article cap. The
fix is not deleting analysis: two regression-grid tables and a balance table move to the appendix, the
bibliography is trimmed, and footnotes fold into the text, bringing it to 34 pages (illustrative).

## Editor pushback patterns and the venue fix

- *"Over the page budget."* Never shrink font or spacing; move robustness and derivations to the appendix
  and trim the bibliography to works you engage.
- *"Anonymity is compromised."* The most common leak is PDF document properties, not the text — strip
  metadata and keep the title page a separate file.
- *"Confirm fee / OA terms."* Fee and open-access policies can change; confirm against the journal's
  current submission guidelines and Editorial Manager screen rather than assuming.

## Output format

```
【Category】Research Article (≤35 pp) / Short Article (≤10 pp) — page limit met? [Y/N]
【Format】double-spaced 12-pt; exhibits/notes/refs counted? [Y/N]
【Online Appendix】separate file, ≤25 pp? [Y/N]
【Abstract + keywords】≤150 words, no citations; 4–5 keywords? [Y/N]
【Anonymized】text + self-refs + file metadata clean? [Y/N]
【Repro package】staged for JOP Dataverse? [Y/N]
【Next】await decision → jop-rebuttal on R&R
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers, anonymization, page-budget and repro tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — JOP portal, page limits, abstract cap, double-blind policy
