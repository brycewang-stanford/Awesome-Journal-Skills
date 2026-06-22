---
name: ecj-submission
description: Use when running the final pre-submission preflight for a The Economic Journal (EJ) manuscript via Editorial Express — single PDF format, author-date references, single-blind review, JEL codes and keywords, full-length vs. short-paper choice, submission-fee awareness, funding disclosure, and the RES/EJ data-and-code policy. Final mechanical gate; it does not improve the economic argument.
---

# Submission Preflight (ecj-submission)

## When to trigger

- "Submitting tomorrow" — the last mechanical check before pressing submit
- Unsure what the Editorial Express portal requires as files and metadata
- Confirming format, references, review model, and data policy are EJ-correct
- Deciding finally between the full-length and short-paper routes

## Process facts (verified 2026-06-20; re-confirm on the official OUP/RES pages)

- EJ (founded **1891**, the **Royal Economic Society's** flagship, published by **Oxford University Press**; editor-in-chief **Francesco Lippi**) is submitted through the **Editorial Express** portal (editorialexpress.com), **not** ScholarOne. The submission must be a **single PDF** including appendices (but not the cover letter or past reports).
- **Review model: single-blind** — referee identities are kept from authors as far as possible, but **authors are not anonymized**, so do *not* strip your identity from the manuscript. This differs from a double-blind journal.
- **Short-paper option:** EJ encourages short papers in the **AER:Insights style — roughly <6,000 words and ~5 exhibits**; full-length articles may be longer. Choose the route deliberately.
- **Metadata:** JEL classification codes and keywords are entered in Editorial Express; provide title, abstract, authors, and affiliations.
- **References: author-date** style. The accepted-author guide gives EJ-style examples and asks for an alphabetized, then chronological, reference list; data and replication packages should be cited.
- **Accepted-author production limits:** short title **40 characters or fewer**, abstract **100 words or fewer**, and keywords **20 characters or fewer each**. Treat these as production-stage limits and keep submission metadata comfortably within them unless the live portal says otherwise.
- **Submission fee:** RES charges for each **new** EJ submission: current listed fees (re-verified 2026-06-22; non-member rate updated **effective 8 May 2026**) are GBP 248 for non-members, GBP 50 for student / Tier A / unemployed members, and GBP 113 for Tier B-C-D members / Fellows, before 20% VAT. Resubmissions are not charged. Re-confirm the live RES fee table before paying.
- **Funding:** all sources of research funding must be acknowledged in the manuscript.
- **Data & code:** EJ runs **pre-acceptance reproducibility checks** (since July 2019) via the **EJ Data Editor**; the package is deposited to **Zenodo** at acceptance under the RES policy (DCAS-endorsed). Request any **data exemption at first submission** (see `ecj-replication-package`).

## Pre-submission checklist

### Format
- [ ] Manuscript is a **single PDF** including appendices (cover letter and past reports separate)
- [ ] Sections ordered logically (intro → model/theory → data → strategy → results → mechanisms/robustness → conclusion)
- [ ] Equations numbered and referenced as "equation (n)"
- [ ] Figures legible in grayscale; tables self-contained with full notes
- [ ] Online appendix material prepared (proofs, full robustness, descriptive tables)
- [ ] Short paper? within ~6,000 words / ~5 exhibits; full-length? exposition complete

### References (house style)
- [ ] **Author-date** citations throughout — not numbered/bracket
- [ ] Reference list complete; alphabetized then chronological for each author
- [ ] Dataset and replication-package citations included where relevant
- [ ] Every in-text citation appears in the list; every list entry is cited

### Review model & identity (EJ is single-blind)
- [ ] Confirm format target: **full-length article** or **short paper (AER:Insights-style)**
- [ ] Author identities are visible to referees, so **no manuscript anonymization** is required
- [ ] Title page with authors, affiliations, acknowledgments, and **funding sources** included
- [ ] Submission fee category known; payment path ready for a new submission

### Data, code & policy
- [ ] RES/EJ data-and-code policy reviewed (DCAS, EJ Data Editor, Zenodo); package staged (see `ecj-replication-package`)
- [ ] Restricted/proprietary data: **exemption requested at first submission**
- [ ] Not under review elsewhere; no duplicate/overlapping submission

### Exhibits & supplementary
- [ ] Main-text exhibits report economic magnitudes, not stars alone
- [ ] Online appendix complete and referenced from the main text
- [ ] Any restricted-data documentation prepared

### Portal metadata (Editorial Express)
- [ ] Title and abstract entered; accepted-author abstract cap is 100 words
- [ ] **JEL classification codes** entered
- [ ] **Keywords** entered; accepted-author guide asks each keyword to be 20 characters or fewer
- [ ] All co-authors and affiliations correct; corresponding author set
- [ ] Suggested referees (and any opposed referees) prepared with brief justification
- [ ] One-page cover letter: question, contribution, fit with EJ's broad-interest mandate

## Anti-patterns

- Wasting effort anonymizing the manuscript — EJ is **single-blind**, so author identity is expected
- Numbered citations left in from a different journal's template instead of **author-date**
- Submitting via ScholarOne by habit — EJ uses **Editorial Express**
- Padding a clean short result to full length instead of using the short-paper route (or vice versa)
- Forgetting to acknowledge funding sources, or omitting JEL codes/keywords in the portal
- Requesting a restricted-data exemption only at acceptance instead of at first submission

## Output format

```
【Target】full-length article / short paper (AER:Insights-style)
【Format】single PDF incl. appendices, exhibits OK? [y/n]
【References】author-date; list alphabetical/chronological; data citations included? [y/n]
【Review model】single-blind — no anonymization needed [confirm]
【Metadata】JEL codes + keywords + <=100-word abstract ready? [y/n]
【Fee】new-submission fee category/payment ready, resubmission fee exempt if applicable? [y/n]
【Funding】acknowledged in manuscript? [y/n]
【Replication】DCAS package staged; exemption (if any) at first submission? [y/n]
【Next】await decision / on R&R → ecj-rebuttal
```

## Bundled resources

- [`templates/checklist.md`](templates/checklist.md) — 8-section pre-submission self-check across format, references, single-blind review, data policy, exhibits, and portal
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — EJ manuscript skeleton (section order, author-date references, variable table)
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — economics data sources and Stata / R / Python packages for identification, structural estimation, and replication
