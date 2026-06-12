---
name: jde-submission
description: Use when running the final pre-submission preflight for the Journal of Development Economics (JDE) via Editorial Manager — route selection, single-anonymized review, no-fee policy, replication readiness, language consistency, and route-specific length caps. Final checks; it does not draft content.
---

# Submission Preflight (jde-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on Editorial Manager
- Unsure which files and metadata Editorial Manager expects
- Confirming the chosen route's limits (full-length / short-paper / pre-results) are met
- Checking the replication package, declarations, and language consistency

## Process facts (verify volatile items on the official page)

- JDE is published by **Elsevier** and submitted through **Editorial Manager**. It is the **leading field journal in development economics**, edited by Lead Editor **Andrew Foster** (with Dean Karlan among the editors).
- Review is **single-anonymized** (referees know the author; the author does not know referees) — 待核实 on the live page, but high-confidence. **Do not anonymize** the manuscript as if it were double-blind unless the current guidance says so.
- **There is no submission fee.** Open access is optional and charged only after acceptance (APC figure 待核实 — confirm on the official open-access page).
- **Submission cap:** no more than **three papers per author within any 12-month period**.
- **Replication readiness:** data, programs, and computational details can be requested **at the review stage**, so the package must be ready at submission (see jde-replication-and-data-policy).
- **Language:** the manuscript must be in **either American or British English, not a combination**. References may be in **any consistent style** at submission (JDE applies its style at the proof stage), with author-date citations.

## Route-specific limits

- **Full-length:** no fixed length limit; extensive online appendix expected.
- **Short-paper (limited-revision):** ≤ **6,000 words**, ≤ **5 exhibits**, online appendix ≤ **20 pages**, self-contained.
- **Pre-results review (Stage 1):** proposal ≤ **60 pages**, abstract ≤ **150 words**, cover page with JEL codes, hypotheses, statistical analysis plan, **power analysis**, and ethics/funding/conflict disclosures.

## Preflight checklist

### Route & format
- [ ] Route chosen (full-length / short-paper / pre-results) and its caps met
- [ ] References in a **consistent** author-date style (house style applied at proof stage)
- [ ] Tables/figures numbered, called out in order, with self-contained notes
- [ ] Online appendix attached (extensive for full-length; ≤ 20 pp for short-paper)

### Language & declarations
- [ ] **One** consistent English variant (US or UK), not mixed
- [ ] Conflict-of-interest, funding, and ethics/IRB disclosures prepared
- [ ] Confirmed the paper is not under review elsewhere
- [ ] Within the **three-per-12-months** submission cap

### Replication & files
- [ ] Replication package submission-ready (master script + README + pinned versions + seeds)
- [ ] Restricted-data access path documented if data cannot be shared
- [ ] Cover letter (concise: development question, design, headline result, route)
- [ ] Mendeley Data deposit staged for the accepted stage

### Content sanity
- [ ] Abstract states the finding with a magnitude in welfare units (see jde-writing-style)
- [ ] Identification diagnostics complete (see jde-identification-strategy, jde-data-analysis)
- [ ] No over-claiming beyond what the design supports

## Desk-screen failure modes (what gets a JDE paper bounced before review)

| Failure at the desk                                       | Preflight catch                                                |
|-----------------------------------------------------------|----------------------------------------------------------------|
| No first-order development stake — generic micro on LMIC data | Confirm the development mechanism is the point (see jde-topic-selection) |
| Short-paper track over 6,000 words or 5 exhibits          | Hard-count words and exhibits before route selection           |
| Mixed US/UK English across the manuscript                  | One-pass spelling sweep for a single consistent variant        |
| Causal claim on OLS + controls, undefended                 | Identification diagnostics complete before submitting          |
| Replication package not staged (can be requested in review)| Master script + README + seeds ready at submission, not later  |
| Fourth submission inside a 12-month window                 | Track the three-per-12-months cap across co-authored papers    |

## Worked preflight vignette (illustrative)

Hypothetical: a cluster-randomized health-information experiment, sharp single result, draft at 5,400 words with 4 exhibits.

- **Route:** fits the **short-paper** track — under both the 6,000-word and 5-exhibit caps, self-contained, online appendix at ~14 pages (under the 20-page cap, *illustrative*).
- **Preflight hits:** the manuscript was anonymized as if double-blind — un-anonymize, since review is single-anonymized; the cover letter named a "submission fee budget" — delete it, there is no fee.
- **Go/no-go:** replication package regenerates all 4 exhibits from `run_all`; COI/IRB disclosures attached; within the 3-per-12-months cap → cleared to submit.

## Anti-patterns

- Anonymizing as double-blind when JDE review is single-anonymized
- Sending a long paper to the short-paper track (it caps words and exhibits)
- Submitting without a review-ready replication package (it can be requested during review)
- Mixing US and UK English; budgeting for a submission fee that does not exist
- Exceeding the three-submissions-per-12-months cap

## Output format

```
【Route】full-length / short-paper / pre-results (caps met? Y/N)
【Review model】single-anonymized — manuscript handled accordingly? [Y/N]
【Language】consistent US or UK English? [Y/N]
【Replication package】review-ready? [Y/N]
【Declarations】COI / funding / ethics prepared? [Y/N]
【Submission cap】within 3-per-12-months? [Y/N]
【Next step】await decision → jde-rebuttal on R&R
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — data sources and Stata/R/Python packages for development empirical work
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official JDE URLs behind every fact in this pack
