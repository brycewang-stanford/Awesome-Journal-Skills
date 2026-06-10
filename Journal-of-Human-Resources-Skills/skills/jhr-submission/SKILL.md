---
name: jhr-submission
description: Use when running the final pre-submission preflight for the Journal of Human Resources (JHR) via the msubmit.net portal — the page-count limit, the nonrefundable upfront fee, the per-author disclosure statement, the data-archive footnote, and scope fit. Final checks; it does not draft content.
---

# Submission Preflight (jhr-submission)

## When to trigger

- "Submitting tomorrow" — last check before uploading to msubmit.net
- Unsure which declarations and footnotes JHR expects at initial submission
- Confirming the 40-page limit and single-anonymous formatting are met

## Process facts (verified 2026-06-01; re-confirm on the live page)

- JHR is published by **University of Wisconsin Press** for the Board of Regents, housed at the UW-Madison **Institute for Research on Poverty (IRP)**; founded **1965**; Editor **Anna Aizer (Brown)** now, **Michael Lovenheim (Cornell)** from **2026-07-01**.
- Submit only via **http://jhr.msubmit.net**. Do **NOT** email the editor, coeditors, managing editor, or editorial office directly.
- **Scope is the first gate.** JHR is empirical microeconomics (labor, development, health, education, discrimination, retirement) with a policy bent and **does NOT consider management/personnel ("HR") research.** The fee is **not refunded** for out-of-scope papers.
- **Nonrefundable submission fee: $175** on the live Authors page ($150 in the Sept-2024 policy PDF — verify which is current). **No fee** for invited revisions; economic-hardship exemption may be requested. The fee does **not** guarantee outside review.
- **Length is page-based, not word-based:** max **40 pages** including references, tables, and figures at **12pt, 1.5-line spacing, 1-inch margins**; up to **50 pages** if double-spaced; footnotes may be smaller/single-spaced. Overflow goes to an **Online Appendix** (must not be excessive).
- **Single-anonymous review:** referees are anonymous, **author names are not hidden** — so do not waste effort anonymizing the body.

## Preflight checklist

### Scope & fit
- [ ] This is empirical microeconomics with a policy-relevant question, **not** HR-management/personnel work
- [ ] A clear causal or descriptive contribution to one of JHR's fields

### Format & length
- [ ] <= 40 pages incl. references/tables/figures (12pt, 1.5-spacing); or <= 50 double-spaced
- [ ] Online Appendix holds overflow and is not bloated
- [ ] Tables/figures numbered, called out in order, with self-contained notes

### Required front matter & footnotes
- [ ] **Per-author Disclosure Statement** up front (funding/support >= $10,000 over 3 yr, positions, relatives/partners, right-to-review, IRB status)
- [ ] **Data-archive plan footnote** with a persistent (DOI) link, or a waiver request made now (see jhr-replication-and-data-policy)
- [ ] **Data Availability Statement** drafted for the title page
- [ ] For RCTs: pre-analysis plan existence, registry, and deviations stated
- [ ] Author-order randomization "r" superscript used if applicable

### Files for msubmit.net
- [ ] Main manuscript (within page limit) + Online Appendix
- [ ] Cover letter (question, design, headline result, policy relevance)
- [ ] Optional: prior journal's decision letter + referee reports to speed review

## Worked page budget for the 40-page cap

Illustrative allocation for a design-based JHR manuscript at 12pt, 1.5-spacing
(adjust to the paper, but the proportions are the point):

| Section | Pages | Notes |
|---|---|---|
| Intro incl. reconciliation paragraph | 5 | Question, variation, magnitude, bridge to prior estimates |
| Institutional setting + data | 7 | Treatment definition, sample construction, linkage |
| Empirical strategy | 4 | Estimator, clustering, identifying assumption stated once |
| Results + design diagnostics | 11 | Roughly 5-7 exhibits: main table, event study or first stage, reconciliation |
| Heterogeneity + external validity | 4 | Only policy-mapped cuts |
| Conclusion + references | 6 | References count against the cap |
| Slack | 3 | R&R additions will need it |

A draft at 47 pages is not "close" — cut exhibits to the Online Appendix before
upload, since the cap includes tables, figures, and references.

## Cover-letter skeleton

```text
1. Question + JHR field (labor/education/health/development/discrimination/retirement)
2. Identifying variation in one sentence (rollout / cutoff / lottery / instrument)
3. Headline magnitude in policy units
4. One reconciliation sentence vs. the closest published estimate
5. Notes: archive-plan footnote or waiver; optional prior-journal reports attached
```

## Anti-patterns

- Paying the nonrefundable fee on an out-of-scope HR-management paper
- Emailing the editor instead of using msubmit.net
- Blowing past 40 pages and dumping the excess into a bloated appendix
- Omitting the disclosure statement or the data-archive footnote (can reverse acceptance)
- Over-anonymizing the body for a single-anonymous journal

## Output format

```
【Scope】empirical micro + policy, not HR-mgmt? [Y/N]
【Length】<=40pp (or <=50 double)? overflow in appendix? [Y/N]
【Fee】$175 nonrefundable acknowledged / hardship? [Y/N]
【Disclosure】per-author statement up front? [Y/N]
【Data】archive footnote + DAS (or waiver requested)? [Y/N]
【Files】manuscript / appendix / cover letter staged? [Y/N]
【Next step】await desk decision → jhr-rebuttal on R&R
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — full pre-submission self-check
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official JHR URLs behind every fact
