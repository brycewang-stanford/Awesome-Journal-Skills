---
name: jpam-submission
description: Use when running the final pre-submission preflight for the Journal of Policy Analysis and Management (JPAM) via ScholarOne — article-type selection, double-blind preparation, the APPAM membership-or-fee requirement, abstract/format, ORCID, data-availability statement, and declarations. Final checks; it does not draft content.
---

# Submission Preflight (jpam-submission)

The last check before pressing submit on **ScholarOne / Manuscript Central**. JPAM is **double-blind**,
so the most common avoidable failure is an under-anonymized manuscript — and unlike most journals, JPAM
requires **APPAM membership or a paid submission fee** before a paper is considered. Verify volatile
specifics on the official author page before relying on them (检索于 2026-06；以官网为准).

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata ScholarOne expects
- Confirming anonymization, the fee/membership requirement, and the data-availability statement

## Process facts (verify volatile items on the official page)

- **Owner / publisher:** Association for Public Policy Analysis and Management (APPAM) / **Wiley**.
- **Portal:** **ScholarOne / Manuscript Central** (the journal moved manuscript management to ScholarOne;
  confirm the current link from the Wiley/APPAM author page). 待核实 on the exact URL.
- **Review model:** **double-blind** — anonymize the manuscript; upload a separate title page.
- **Article types:** Feature Research Articles, Methods for Policy Analysis, Policy Retrospectives
  (peer-reviewed); Point/Counterpoint and Policy Insights (invited, **not** peer-reviewed); Book Reviews.
- **Membership-or-fee:** APPAM members submit free with no submission cap; non-members pay a
  **submission fee** (~**$100 professionals / $40 students**, student ID required), with **no fee for
  resubmission** and **waivers** for economically disadvantaged countries / financial hardship via
  info@appam.org. 待核实 on current amounts.
- **Abstract / length:** confirm the current abstract cap and feature-article length guidance on the
  author page (Policy Insights are ≤ 3,000 words). 待核实 on the exact feature-article word limit.
- **Style:** Wiley/APPAM house reference style (confirm current edition); ORCID encouraged/required for
  the corresponding author — confirm on the live page. 待核实.
- **Data availability:** a data-availability statement and an archived data/code package are expected for
  publication (see `jpam-transparency-and-data`).

## Preflight checklist

### Type & length
- [ ] Article type chosen; peer-review status understood (Feature vs. invited types)
- [ ] Abstract within the current cap; states question + policy + design + finding + implication
- [ ] Length within the current guidance for the chosen type

### Anonymity (double-blind)
- [ ] No author names, affiliations, or acknowledgments in the manuscript
- [ ] Self-references neutralized ("as shown in…"), funding/IRB identifiers removed from the main file
- [ ] Identifying **file metadata stripped** (document properties, comments)
- [ ] Separate (non-anonymous) title page prepared as a distinct file

### Fee / membership & metadata
- [ ] APPAM membership current **or** submission fee paid **or** approved waiver in hand
- [ ] Corresponding-author **ORCID** ready (confirm requirement)
- [ ] Figures/tables self-contained and accessible (see `jpam-tables-figures`)

### Compliance & files
- [ ] Ethics / IRB / human-subjects compliance stated as needed
- [ ] Original work; preprint status checked against Wiley policy
- [ ] **Data-availability statement** included; replication package staged (see `jpam-transparency-and-data`)

## Anti-patterns

- Leaving author identifiers in the text, acknowledgments, or file metadata (breaks anonymity)
- Forgetting the **membership-or-fee** step and having the submission held or returned
- Sending a full research paper to the invited, non-reviewed Point/Counterpoint or Policy Insights slots
- Submitting with no data-availability statement when the policy expects one
- Assuming the old Wiley portal URL — confirm the current ScholarOne link

## Output format

```
【Type】Feature / Methods / Retrospective / (invited type) — peer-reviewed? [Y/N]
【Anonymized】text + self-refs + file metadata clean? [Y/N]
【Abstract】within cap; states implication? [Y/N]
【Fee / membership】member / fee paid / waiver? [which]
【ORCID + data-availability statement】[Y/N]
【Repro package】staged (see jpam-transparency-and-data)? [Y/N]
【Next】await decision → jpam-rebuttal on R&R
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — the full pre-submission checklist as a worksheet
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official JPAM / APPAM / Wiley URLs behind every fact
