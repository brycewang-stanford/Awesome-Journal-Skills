---
name: jpe-submission
description: Use when running the final pre-submission preflight for a Journal of Political Economy (JPE) manuscript via Editorial Manager — manuscript format, Chicago author-date references, the $250/$125 submission fee, single-blind review, exhibits, the Micro/Macro companion-journal choice, and supplementary files. Final mechanical gate; it does not improve the economic argument.
---

# Submission Preflight (jpe-submission)

## When to trigger

- "Submitting tomorrow" — the last mechanical check before pressing submit
- Unsure what the Editorial Manager portal requires as separate files
- Confirming format, references, and fee handling are correct

> JPE (founded 1892, edited at the University of Chicago; lead editor **Esteban Rossi-Hansberg**) is published by the University of Chicago Press and processed through the **Editorial Manager (EM)** system (author portal: editorialmanager.com/jpolec). Review is **single-blind** (referees see authors; authors do not see referees), so author-anonymization is *not* required — this differs from a double-blind journal. A **submission fee** applies: **$250 for nonsubscribers, $125 for individual JPE subscribers**, non-refundable even if the paper is desk-rejected; a **waiver** is available to authors who completed **three or more JPE referee reports in the prior 12 months**. Since the 2023 launch of the companion journals **JPE Microeconomics** (lead editor John List) and **JPE Macroeconomics** (lead editor Greg Kaplan), decide up front whether your paper targets the flagship JPE or a field companion. Verify the current fee and guidelines on the official page before submitting; everything below is the durable structure of a JPE submission.

## Pre-submission checklist

### Format
- [ ] Manuscript is a single PDF, double-spaced, with figures/tables either embedded or at the end per current guidelines
- [ ] Sections ordered logically (intro → model/theory → data → strategy → results → mechanisms/robustness → conclusion)
- [ ] Equations numbered and referenced as "equation (n)"
- [ ] Figures legible in grayscale; tables self-contained with full notes
- [ ] Online appendix prepared as a separate file (proofs, full robustness, descriptive tables)

### References (house style)
- [ ] **Chicago author-date** citations throughout (e.g., "Becker 1968") — not numbered/bracket
- [ ] Reference list complete and consistently formatted in University of Chicago Press author-date style
- [ ] Every in-text citation appears in the list; every list entry is cited
- [ ] Canonical theory the paper engages is cited (a frequent referee snag)

### Review model & identity (JPE is single-blind)
- [ ] Confirm target: flagship **JPE**, or companion **JPE Microeconomics** / **JPE Macroeconomics**
- [ ] Author identities are visible to referees, so no manuscript anonymization is required (single-blind)
- [ ] Title page with authors, affiliations, acknowledgments, and funding included

### Fee & policy
- [ ] Submission fee ready: **$250 nonsubscriber / $125 JPE subscriber** (non-refundable even on desk reject)
- [ ] If you completed **3+ JPE referee reports in the last 12 months**, request the fee **waiver** before paying
- [ ] Data and code availability policy (JPE endorses **DCAS**) reviewed; replication package staged (see `jpe-replication-package`)
- [ ] Not under review elsewhere; no duplicate/overlapping submission

### Exhibits & supplementary
- [ ] Main-text exhibits report economic magnitudes, not stars alone
- [ ] Online appendix complete and referenced from the main text
- [ ] Any restricted-data documentation prepared

### Author info & metadata
- [ ] Title, abstract, JEL codes, and keywords entered in the portal
- [ ] All co-authors and affiliations correct; corresponding author set
- [ ] Suggested referees (and any opposed referees) prepared with brief justification

## Editorial Manager operational notes

- Register/log in to the JPE Editorial Manager (EM) portal; have title, abstract, JEL codes, and the PDF ready before starting.
- Upload the manuscript PDF; attach the online appendix and cover letter as the portal requests.
- Complete the **$250/$125** fee step (or apply the 3-reports waiver); the paper is not forwarded to editors until the fee clears, and the fee is non-refundable even if desk-rejected.
- Confirm the submission acknowledgment email and manuscript number arrive.

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue jpe-skills   # from a clone of the AJS repository
```

It reports, with a location for each finding:

- this venue's machine-readable limits, review mode and required statements, when the venue has a
  rules block (`--list-venues`);
- citations ↔ references;
- table and figure numbering, cross-references and standard-error notes;
- abstract numbers traced to the tables;
- placeholders and tracked changes.

With the Research Toolkit pack installed, `rt-submission-readiness` runs the same check as stage 0
of the full pre-submission pipeline (scorecard → referee panel → polish → cover letter). Anything
it lists as *not checked* still needs the manual items below.

## Anti-patterns

- Wasting effort anonymizing the manuscript — JPE is **single-blind**, so author identity is expected
- Numbered citations left in from a different journal's template instead of **Chicago author-date**
- Paying the $250 fee when you qualified for the 3-referee-reports waiver
- Forgetting the submission fee step, so the paper never reaches an editor
- Sending a pure macro (or pure micro) paper to the flagship without considering the JPE Macro / JPE Micro companion
- JEL codes or keywords omitted in the portal; online appendix referenced in text but not uploaded

## Output format

```
【Target】flagship JPE / JPE Micro / JPE Macro
【Format】single PDF, double-spaced, exhibits OK? [y/n]
【References】Chicago author-date verified; list complete? [y/n]
【Review model】single-blind — no anonymization needed [confirm]
【Fee】$250 nonsub / $125 sub, or 3-reports waiver requested? [y/n]
【Replication】DCAS package staged per policy? [y/n]
【Portal metadata】title/abstract/JEL/keywords/referees entered? [y/n]
【Next】await decision / on R&R → jpe-rebuttal
```

## Bundled resources

- [`templates/manuscript_template.md`](templates/manuscript_template.md) — JPE manuscript skeleton (section order, author-date references, variable table)
- [`templates/checklist.md`](templates/checklist.md) — pre-submission self-check across format, references, single-blind review, fee, exhibits, and portal
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — economics data sources and Stata / R / Python packages for identification, structural estimation, and replication
