---
name: tar-submission
description: Use when running the final pre-submission preflight for a The Accounting Review (TAR) manuscript — the Editorial Manager portal, double-blind anonymization, AI disclosure statement, ORCID and Conflict-of-Interest forms, data-authenticity files, the submission caps, and AAA/Chicago formatting. Checks readiness to submit; it does not handle the post-decision response (tar-rebuttal).
---

# Pre-Submission Preflight (tar-submission)

## When to trigger

- "We're submitting this week" — the last check before hitting submit on Editorial Manager
- Unsure what TAR requires (anonymized manuscript, AI disclosure, ORCID, COI, code/data)
- Verifying double-blind anonymization is complete in both file and prose
- Confirming you are within the per-author submission cap and the byline cap

> Always re-verify current limits, the fee, and required files on the official TAR Editorial Policy,
> Guide for Authors, and the AAA Manuscript Preparation Guide before submitting — specifics change.
> As of 2026-06-01 the verified key specs are below; the fee and roster are flagged 待核实.

## Verified TAR/AAA specs (confirm current values)

- **Submission portal:** **Editorial Manager** at **editorialmanager.com/accr**.
- **Length:** initial submissions **should not exceed 55 pages**, *including* references, figures,
  tables, and appendices.
- **Format:** 12-pt Times New Roman, double-spaced, 1-inch margins, serially numbered pages.
- **Abstract:** **no more than 150 words**, beginning the article file.
- **AI disclosure statement:** required — tools used, extent, and reasons — placed **immediately
  after the abstract and before the body**; must be updated on resubmission.
- **Style:** **The Chicago Manual of Style (16th ed.)** for citations/references; Webster's
  Collegiate Dictionary for spelling.
- **Review:** **double-blind** — an editor plus a **minimum of two reviewers**; anonymity of authors
  and reviewers is a critical goal (among AAA journals, only the Journal of Financial Reporting is
  single-blind).
- **ORCID:** required for **all** authors.
- **Conflict of Interest form:** completed COI form (each author) at submission.
- **Plagiarism screening:** applied to all manuscripts.
- **Submission caps:** an individual author is limited to **eight (8) first-round submissions** over a
  rolling 24-month period (R&R papers do not count); **no more than 10 authors** on the byline.
- **Fee (verified 2026-06-22):** non-refundable submission fee of **$285 AAA members / $680 non-members**
  per the current Guide for Authors, paid via the AAA portal at submission (this is separate from the
  optional open-access Article Publishing Charge) — re-confirm the current amount before submitting.
- **IRB:** human-subjects documentation required for experimental/survey work.
- **Data authenticity:** code/data package per data type (see below) is part of submission.

## Pre-submission checklist

### Anonymization (double-blind)

- [ ] Manuscript file has **no** author names, affiliations, or acknowledgments
- [ ] Self-citations are third-person ("prior research (Author 2020)"), not "our earlier work"
- [ ] Acknowledgments, funding, and data-provider thanks are removed from the manuscript body
- [ ] File metadata/properties and file names scrubbed of author/institution identity

### Format & front matter (AAA Manuscript Preparation Guide)

- [ ] Abstract ≤ 150 words begins the article file
- [ ] **AI disclosure statement** placed immediately after the abstract, before the body
- [ ] Chicago (16th ed.) citations and reference list; spelling per Webster's
- [ ] 12-pt Times New Roman, double-spaced, 1-inch margins, serially numbered pages
- [ ] Initial submission **≤ 55 pages** including references, tables, figures, appendices

### Data authenticity & code access (by data type)

- [ ] **Public databases:** precise data description **+** processing computer code prepared
- [ ] **Abstracted public data:** abstraction methodology **+** code prepared
- [ ] **Privately collected data:** sufficient detail / corroborating third parties documented
- [ ] Variable-definitions appendix and reproducible sample-selection steps included

### Forms, ethics & caps

- [ ] **ORCID** linked for every author
- [ ] **Conflict of Interest** form completed for each author
- [ ] **IRB/human-subjects** documentation ready (experiments/surveys)
- [ ] Within the **8 first-round submissions / 24-month** per-author cap
- [ ] **≤ 10 authors** on the byline
- [ ] No concurrent submission; prior working-paper/conference versions disclosed

### References & consistency

- [ ] Every in-text citation appears in the reference list and vice versa
- [ ] Hypothesis/prediction labels, variable names, and table/figure numbers consistent throughout

## Editorial Manager operation notes

- Create/keep your Editorial Manager account and ORCID current; upload files into the slots the
  system designates and preview the built PDF before final submission.
- Select the article type and the keywords/area that route the paper to a fitting editor (a single
  Senior Editor oversees the process, with Lead Editors assigning editors and handling desk
  rejections; Ad hoc Editors cover specialized topics/methods).
- Pay the submission fee through the AAA portal at submission.

## Anti-patterns

- Self-identifying language ("in our 2019 study") left intact, defeating double-blind review.
- AI disclosure missing or placed in the wrong location (it must follow the abstract).
- Reference list in APA or a reference-manager default rather than Chicago (16th ed.).
- No processing code prepared, violating the data-authenticity policy.
- Exceeding 55 pages by forgetting references/tables/figures/appendices count toward it.
- Submitting past the 8-in-24-months cap or with more than 10 authors.

## Output format

```
【Anonymization】pass / fix: ...
【Format & front matter】abstract ≤150 / AI disclosure placed / Chicago refs: pass / fix ...
【Data authenticity】public-db / abstracted / private — code & description ready? yes/no
【Forms & caps】ORCID / COI / IRB / 8-in-24 / ≤10 authors: complete? ...
【Fee】paid via AAA portal? (amount 待核实)
【Article type & routing】selected ...
【Next step】await decision → tar-review-process; on R&R → tar-rebuttal
```

## Resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — accounting data sources, archival/analytical software, and the data-authenticity package
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official AAA/TAR URLs behind every verified fact (accessed 2026-06-01)
