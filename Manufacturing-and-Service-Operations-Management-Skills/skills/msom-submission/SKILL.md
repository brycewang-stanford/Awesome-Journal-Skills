---
name: msom-submission
description: Use when running the final pre-submission preflight for a Manufacturing & Service Operations Management (M&SOM) manuscript — the ScholarOne portal, double-anonymous anonymization, the 32-page typeset cap on the official template, the structured abstract, author-chosen Department routing with two preferred Department Editors, and data/code disclosure. Checks readiness to submit; it does not handle the post-decision response (msom-rebuttal).
---

# Pre-Submission Preflight (msom-submission)

## When to trigger

- "We're submitting this week" — the last check before hitting submit
- Unsure what ScholarOne requires or which Department/Department Editors to pick
- Need to confirm double-anonymous anonymization is complete
- Verifying the manuscript fits the 32-page typeset cap on the official template

> Before submitting, check the official M&SOM submission-guidelines page, editorial-board page, and ScholarOne screens for the live upload fields, payment step, and editor rosters. The baseline below was checked on 2026-06-20.

## Verified M&SOM specs (confirm current values)

- **Length:** **32-page maximum** for a new submission, **including** all references, tables, graphs/figures, and appendices, typeset on the official **M&SOM LaTeX/Word style files** (one column, **11-point** font, **1-inch** margins on all sides). **Online supplement ≤ 16 pages** for new submissions.
- **Abstract:** **structured, ≤ 300 words**, no technical jargon, with three subsections — **Problem definition / Methodology-results / Managerial implications**.
- **Submission portal:** ScholarOne Manuscripts at **mc.manuscriptcentral.com/msom**; submit as a **single PDF**.
- **Department routing:** choose a primary editorial **Department** and name **two preferred Department Editors**. The Manufacturing-and-Supply-Chain rule applies — if that department is chosen, the **first** DE choice must be from it and the **second** from a different department.
- **Review:** **double-anonymous** — author identities are known only to the EIC, Department Editor, Associate Editor, and editorial staff; remove names, institutions, and acknowledgments from the manuscript.
- **Style:** **INFORMS author-year (author-date)** citations; reference list ordered by first author, number of authors, then year (INFORMS style file v1.6).
- **Data & code:** manuscripts must permit replication; be prepared to share raw data on request and to retain it; provide your own code plus access/linking instructions for licensed data (Census, Compustat, CRSP, FactSet, WRDS).
- **Fees:** M&SOM author guidelines list an optional **USD 3,000 INFORMS Open Option** fee after acceptance and do not list a regular submission fee on the checked page; treat payment as a ScholarOne-screen check, not a manuscript-design assumption.

## Pre-submission checklist

### Anonymization (double-anonymous)

- [ ] Manuscript PDF contains **no** author names, affiliations, or acknowledgments
- [ ] Self-citations worded neutrally ("Author (2020) shows"), not "our earlier work"
- [ ] Funding/acknowledgments removed from the manuscript (supplied separately as the portal requires)
- [ ] File metadata/properties scrubbed of author identity; file names carry no identifiers

### Format (verify against the official style files)

- [ ] Typeset on the official **M&SOM LaTeX/Word template**: one column, 11-pt, 1-inch margins
- [ ] Main submission **≤ 32 pages** including references, tables, figures, appendices
- [ ] Online supplement **≤ 16 pages** (full proofs, extra numerical studies, notation table)
- [ ] **Structured abstract** ≤ 300 words with all three required sections, jargon-free
- [ ] INFORMS author-year citations; reference order per style file v1.6

### Routing & files for ScholarOne

- [ ] Primary **Department** selected; **two preferred Department Editors** named (with the M&SC first/second rule respected)
- [ ] Correct **article type** chosen (standard research vs. OM Forum vs. Practice Platform)
- [ ] Single anonymized **PDF** uploaded; supplement uploaded as required
- [ ] Cover letter (concise: operations problem, contribution, fit, not under review elsewhere)

### Declarations & data/code

- [ ] Data-and-code statement: replication detail provided; raw-data sharing/retention acknowledged
- [ ] Licensed-data access/linking instructions prepared
- [ ] No concurrent submission; prior conference/working-paper versions disclosed in the cover letter
- [ ] Operations-centrality reaffirmed — the operations decision is the primary contribution

## Anti-patterns

- Submitting with self-identifying language ("in our 2019 study") intact.
- Choosing a Department the paper does not actually fit, or ignoring the M&SC first/second rule.
- Letting references/appendices push the typeset manuscript past 32 pages.
- A structured abstract missing the Managerial-implications section.
- Reference list in a non-INFORMS style straight from the reference manager.

## Output format

```
【Anonymization】pass / fix ...
【Format vs. style files】32-page cap, 11-pt template, structured abstract: pass / fix ...
【Department routing】primary + two DEs (M&SC rule respected) ...
【Files】single PDF / supplement / cover letter: ready? ...
【Data & code】replication detail; licensed-data access instructions ...
【Next step】await decision → msom-review-process; on R&R → msom-rebuttal
```

## Resources

- [`templates/manuscript_template.md`](templates/manuscript_template.md) — M&SOM manuscript skeleton (structured abstract, model/design, results, numerical/empirical study, managerial insights, references) with verified specs
- [`templates/checklist.md`](templates/checklist.md) — pre-submission self-check (anonymization / format / routing / files / data-code)
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — OM modeling/solver and empirical tools (Gurobi / CPLEX / Stata / Python)
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official INFORMS/M&SOM URLs behind every fact (accessed 2026-06-20)
