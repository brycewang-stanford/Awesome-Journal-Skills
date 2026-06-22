---
name: etp-submission
description: Use when running the final pre-submission preflight for Entrepreneurship Theory and Practice (ETP) via ScholarOne Manuscripts — page/format limits, the double-anonymization scrub, APA references, article type, and required statements.
Final checks; it does not draft content.
---

# Submission Preflight (etp-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on ScholarOne
- Unsure which files, statements, and format ETP's submission system expects
- Confirming the page limit, font/spacing, and APA style are met
- Deciding between Original Article and Research Brief
- Verifying the manuscript is properly anonymized for double-anonymized review

## Process facts (source map refreshed 2026-06; re-confirm on the SAGE author-instructions page)

- ETP is published by **SAGE on behalf of Baylor University** and is the **official journal of USASBE**.
  Submission is through **ScholarOne Manuscripts** at **mc.manuscriptcentral.com/ETP**.
  Manuscript file format: **Word preferred**.
- **Editor-in-Chief:** **Johan Wiklund (Syracuse University)** is the editor of record (verified 2026-06-22). A 2026 "ETP at 50" editorial signals his departure and an editorial transition; a successor was not yet named publicly as of 2026-06-22, so confirm the current Editor-in-Chief on the SAGE ETP editorial-board page before addressing a cover letter to a named editor.
- **Peer review is double-anonymized** — the manuscript itself (not just the title page) must be scrubbed of author identity: remove author names/affiliations, anonymize self-citations ("Author, 2020"), strip acknowledgments and identifying file metadata, and avoid telltale dataset or institution references.
- **Length:** Original Articles are typically **≤40 pages**, double-spaced, **12-pt Times New Roman**, **1-inch margins** (no lower limit). **Research Briefs ≤20 pages** plus tables and references.
  Confirm whether tables/references count against the limit on the current author-instructions page (待核实).
- **References:** **APA** style throughout.
- **Abstract:** required; confirm the exact word limit on the current author-instructions page (待核实).
- **ORCID, data availability / open-data statements, and any funding/conflict declarations:** SAGE policies apply — confirm which are required at submission on the current page (待核实).
- **Fees:** ETP is a subscription (hybrid) journal; there is **no submission fee**, and an APC applies only if you choose open access (Sage Choice) (verified 2026-06-22) — confirm the current APC figure and waiver terms before relying on them.

## Preflight checklist

### Anonymization (double-anonymized)
- [ ] Author names/affiliations removed from the manuscript body and headers
- [ ] Self-citations anonymized in text and reference list
- [ ] Acknowledgments, funding, and thanks moved out of the anonymized file
- [ ] File metadata/properties scrubbed of author identity
- [ ] No identifying dataset/institution tells that reveal the team

### Format & style
- [ ] Word file; **double-spaced**, **12-pt Times New Roman**, **1-inch margins**
- [ ] Original Article ≤40 pages (or Research Brief ≤20 pages) — article type chosen deliberately
- [ ] **APA** references throughout; in-text citations match the reference list
- [ ] Abstract present and within the current limit (待核实)
- [ ] Tables/figures formatted per SAGE/APA, called out near placement
- [ ] A theoretical/mechanism figure (and Gioia data structure for inductive work) included

### Files & declarations on ScholarOne
- [ ] Anonymized main manuscript + separate title page (with author details)
- [ ] Cover letter naming the contribution to entrepreneurship theory AND practice and why ETP
- [ ] ORCID linked; data availability statement; conflict/funding declarations as required (待核实)
- [ ] Confirmed the paper is not under review elsewhere; AI not listed as an author

## Anti-patterns

- Submitting a file that still names the authors or de-anonymizes via self-citation (breaks double-anonymized review)
- Exceeding the page limit and hoping the editor overlooks it
- Mixing citation styles or letting in-text cites diverge from the reference list (not APA-clean)
- A cover letter that pitches only theory and ignores ETP's practice mandate
- Treating ETP like JBV/AMJ's submission system — the portal, limits, and house style differ

## Output format

```text
【Anonymization】names/self-cites/metadata scrubbed for double-anonymized review? [Y/N]
【Format】Word / double-spaced / 12pt Times / 1in margins? [Y/N]
【Length】Original ≤40pp or Brief ≤20pp; article type chosen? [Y/N]
【Style】APA references + matched in-text cites? [Y/N]
【Abstract】present and within limit (待核实)? [Y/N]
【Exhibits】mechanism figure (+ Gioia if inductive) included? [Y/N]
【Declarations】ORCID / data statement / conflicts as required (待核实)? [Y/N]
【Cover letter】names theory + practice contribution and why ETP? [Y/N]
【Next step】submit via ScholarOne (mc.manuscriptcentral.com/ETP) → etp-review-process
```

## Worked vignette: a self-citation that breaks anonymization (illustrative)

A team submits an otherwise clean manuscript.
In the theory section they write: "Building on our earlier finding (Smith & Jones, 2021) that nascent founders…" and the reference list shows Smith and Jones as the only two authors — who are also the submitting authors.
Under ETP's double-anonymized review this is a de-anonymization: any reviewer can infer the authorship.
The fix is not to delete the citation (which would orphan a needed reference) but to anonymize it in text — "prior work has found that nascent founders… ([Author], 2021)" — and place the full reference in a separate, non-anonymized title-page file along with names, affiliations, acknowledgments, and funding.
Then scrub the Word document's properties (author metadata) and check headers/footers.
The substance is unchanged; the team's identity is no longer leaked into the file the reviewers see.

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — submission self-check
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — lightweight manuscript scaffold
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official SAGE URLs and volatile facts
