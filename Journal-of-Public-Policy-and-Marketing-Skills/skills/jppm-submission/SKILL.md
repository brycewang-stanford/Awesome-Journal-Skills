---
name: jppm-submission
description: Use when running the final preflight for a Journal of Public Policy & Marketing (JPP&M) submission — the two-file split, double-anonymization, 50-page cap, Policy Contribution Statement, abstract/keywords, and the SageTrack portal. Final checks only; it does not draft content.
---

# Submission Preflight (jppm-submission)

## When to trigger

- Submitting to JPP&M this week and running the last-mile checks
- Unsure how the 50-page all-inclusive cap counts your appendices
- Assembling the title page, main document, and web appendix into the required files
- Verifying anonymization, statements, and declarations before SageTrack upload

## Process facts (checked 2026-07-16 on ama.org / SAGE; re-check volatile items on the official site)

- JPP&M is an **American Marketing Association journal published by SAGE** (pISSN 0743-9156, eISSN 1547-7207). Joint Editors in Chief **Melissa Bublitz and Stacey Finkelstein** began processing new submissions **April 1, 2026**, succeeding Jeremy Kees and Beth Vallen — re-verify the masthead on the AMA editors page before submitting.
- **Portal**: SageTrack (ScholarOne) at **https://mc.manuscriptcentral.com/ama_jppm**.
- **Length**: maximum **50 pages, double-spaced, 1-inch margins, inclusive of title, abstract, keywords, text, footnotes, references, tables, figures, and print appendices** — enforced **at all stages of review**. Tables and references may be single-spaced per the AMA guidelines; web appendices sit outside the cap (re-check the current guidelines for what counts as a print vs. web appendix).
- **Required pieces**: an unstructured **abstract of 200 words**; **at least 3 keywords**; a **Policy Contribution Statement** (≤300 words) on the first page of the main document, excluded from the page cap.
- **Review model**: **double-anonymized**. Submit at least two files — (1) a title page with authors, affiliations, acknowledgments; (2) an anonymized main document. Refer to data sites generically ("a large public university," "a Fortune 500 retailer").
- **Style**: AMA journals house style for citations, references, headings, and exhibits (shared with JM/JMR) — confirm details on the AMA submission-guidelines page; fees/membership requirements, if any, should be checked on the portal at submission (re-check on the official site).

Templates: [`templates/checklist.md`](templates/checklist.md) and [`templates/manuscript_template.md`](templates/manuscript_template.md).

## Preflight checklist

### Files & length
- [ ] Title page (identifying info, acknowledgments, funding) as a separate file
- [ ] Main document anonymized; opens with the Policy Contribution Statement
- [ ] Page count ≤50 double-spaced pages counting everything printed except the statement
- [ ] Web appendix assembled separately for the overflow battery

### Required statements & metadata
- [ ] Policy Contribution Statement ≤300 words with all three elements (conversation / advance / stakeholders)
- [ ] Abstract ≤200 words; ≥3 specific keywords after it
- [ ] IRB/ethics approval stated for human-subjects work, with extra care documented for vulnerable populations
- [ ] Funding, conflicts of interest, and any AI-use disclosure prepared per current AMA policy
- [ ] Data-availability plan ready (what can be shared; what is restricted and why)

### Anonymization sweep
- [ ] No author names, affiliations, or thanks in the main document
- [ ] Self-citations phrased in third person; no "our prior work"
- [ ] File metadata (Author field, tracked changes, comments) scrubbed in every uploaded file
- [ ] Pre-registration links use anonymized view-only versions
- [ ] Institutions and field partners referred to generically

### Fit signals the desk screen checks
- [ ] The statement and abstract independently convey a policy-first paper
- [ ] Implications name actors with authority to act
- [ ] Evaluation designs show their counterfactual in the abstract/statement, not page 30

## Anti-patterns

- Counting on the web appendix to hide print-appendix material the guidelines count against the cap
- A Policy Contribution Statement that summarizes the abstract instead of answering its three questions
- Anonymizing the text but uploading files whose metadata names the authors
- Discovering at upload that the portal requires declarations you never drafted
- Submitting under the old editorial team's expectations without re-checking current policies

## Output format

```text
【Files】title page / anonymized main doc / web appendix — ready? [Y/N each]
【Length】≤50 pages all-inclusive at current stage? [Y/N + count]
【Statement】Policy Contribution Statement ≤300 words, 3 elements? [Y/N]
【Abstract & keywords】≤200 words + ≥3 keywords? [Y/N]
【Anonymization】text + metadata + links swept? [Y/N]
【Declarations】ethics, COI, funding, data availability? [Y/N]
【Portal】mc.manuscriptcentral.com/ama_jppm confirmed live? [Y / re-check]
【Next step】submit, then jppm-review-process
```
