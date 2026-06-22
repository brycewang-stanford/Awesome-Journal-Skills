---
name: qje-submission
description: Use when running the final pre-submission preflight for the Quarterly Journal of Economics (QJE) via Editorial Express — single-PDF format, double-blind anonymization, author-date references, the no-fee policy, and supplementary files. Final checks; it does not draft content.
---

# Submission Preflight (qje-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on Editorial Express
- Unsure which files Editorial Express expects at the initial-submission stage
- Confirming the single-PDF format, double-blind anonymization, and author-date style are QJE-compliant
- Checking declarations and supplementary-materials requirements

## Process facts (verified; re-confirm specifics on the official page)

- QJE is published by **Oxford University Press** and **edited at Harvard University's Department of Economics** — the oldest English-language economics journal (founded **1886**) and one of the top-5. Source: academic.oup.com/qje; Wikipedia.
- Submission is through **Editorial Express** at `editorialexpress.com/qje` — the same Express platform used by several econ journals, *not* OUP's ScholarOne. Admin contact: `qje_admin@editorialexpress.com`.
- **There is no submission fee.** This is unusual among top-5 journals (AER, JPE, REStud all charge); do not budget for one. QJE is hybrid open access, so an optional OA charge applies only *after* acceptance if you choose it.
- **Initial submission is a single PDF** containing the full manuscript, tables, figures, and appendices. **No Word files, no LaTeX source, no separate figure files** at this stage — source files are requested only after acceptance.
- QJE uses **double-blind refereeing** — the manuscript must be fully anonymized.
- The editorial team — **five Editors, all at Harvard** (Robert J. Barro, Lawrence F. Katz, Nathan Nunn, Andrei Shleifer, and Stefanie Stantcheva, masthead re-verified 2026-06-22; re-check before submitting) — makes **fast desk decisions (roughly two weeks)**, the quickest among the top-5 flagships, so a clean, complete submission is part of clearing the first screen. (Acceptance runs ~1-4%; desk-reject ~60%+.)

## Preflight checklist

### Format & style

- [ ] One **single PDF** with manuscript, tables, figures, and appendices embedded (no Word, no separate figure files)
- [ ] References in **author-date (Chicago)** style; reference list alphabetical by surname
- [ ] Abstract is short (target **~150 words**)
- [ ] Tables and figures numbered, called out in order, with self-contained notes
- [ ] Long manuscripts are fine (no hard page limit); an extensive **online appendix** is expected
- [ ] PDF compiles cleanly; figures legible at print resolution

### Anonymization (double-blind — required)

- [ ] No author names, affiliations, or acknowledgments in the PDF
- [ ] Self-citations phrased neutrally ("Smith (2020) shows", not "in our earlier work")
- [ ] PDF metadata/properties scrubbed of author identity
- [ ] Acknowledgments and funding info kept out of the body, supplied separately

### Files for Editorial Express

- [ ] Main manuscript as a single PDF (figures/tables/appendix embedded)
- [ ] Cover letter (concise: question, design, headline result, general-interest fit)
- [ ] Suggested / excluded referees prepared (expert, fair, conflict-free)
- [ ] Replication materials staged for the accepted stage (see qje-replication-package)

### Declarations

- [ ] Conflict-of-interest / disclosure statement consistent with the **AEA Disclosure Policy**
- [ ] Funding and data-source disclosures prepared
- [ ] Confirmed the paper is not under review elsewhere

### Final content sanity

- [ ] Abstract states the finding with a number (see qje-writing-style)
- [ ] Identification diagnostics complete (see qje-identification, qje-robustness)
- [ ] No over-claiming beyond what the design supports

## Anti-patterns

- Uploading a Word file or separate figure files at initial submission (QJE wants one PDF)
- Mixed/inconsistent reference styles instead of clean author-date
- Leaving author identity in self-citations or PDF metadata under double-blind review
- Budgeting for a submission fee that does not exist at QJE
- A defensive, multi-page cover letter instead of a tight pitch the editors can read in two weeks
- Submitting a thin appendix to a journal that expects an extensive one

## Output format

```
【Single PDF】one file, all exhibits + appendix embedded? [Y/N]
【Reference style】author-date (Chicago), consistent? [Y/N]
【Anonymization】body + PDF metadata clean (double-blind)? [Y/N]
【Files staged】PDF / cover letter / referees? [Y/N each]
【Declarations】AEA disclosure / funding prepared? [Y/N]
【Content sanity】abstract states finding; identification complete? [Y/N]
【Next step】await ~2-week desk decision → qje-rebuttal on R&R
```

## Supplementary resources

- [`templates/manuscript_template.md`](templates/manuscript_template.md) — QJE-oriented manuscript skeleton (abstract, intro arc, design, exhibits, author-date references)
- [`templates/checklist.md`](templates/checklist.md) — 8-section pre-submission self-check
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — data sources and Stata/R/Python packages for credible-design empirical micro
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official QJE URLs behind every fact in this pack
