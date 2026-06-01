---
name: jar-submission
description: Use when running the final pre-submission preflight for a Journal of Accounting Research (JAR) manuscript — the Wiley Research Exchange portal, double-anonymization, the tiered submission fee and one-week payment window, the article-type choice, and the data-and-code package JAR requires. Checks readiness to submit; it does not handle the post-decision response (jar-rebuttal).
---

# Pre-Submission Preflight (jar-submission)

## When to trigger

- "We're submitting this week" — the last check before hitting submit
- Unsure what the Wiley Research Exchange portal requires
- Verifying double-anonymization and that the fee will be paid in time
- Assembling the data-and-code package JAR posts on acceptance

> Always re-verify current fees, article-type rules, the portal URL, and policy wording on the official Chookaszian Center JAR pages and the Wiley author guidelines before submitting — specifics change. As of 2026-06-01 the verified key specs are below.

## Verified JAR specs (confirm current values)

- **Submission portal:** Wiley Research Exchange / Atypon Rex at **wiley.atyponrex.com/journal/JOAR** (as of Oct 2, 2023).
- **Tiered submission fee (effective Jan 1, 2023):** **Tier One $750**, **Tier Two $500**, **Tier Three $50**; **all authors must reside in Tier Two/Three countries** to get the lower rate; previously a flat $500. The fee **must be received within one week of submission** or the paper is withdrawn; generally **non-refundable**, but a desk-rejected **non-conforming** submission may receive a **half refund**. A separate **$250 conference-registration fee** and a **$250 survey-proposal reviewer fee** exist.
- **Article types:** (i) **Regular Manuscripts**, (ii) **Surveys/Methodological Contributions** (standing call; separate proposal-review fee), (iii) **Registered Reports** (two-stage) — pick the right track.
- **Submission cap:** at most **four NEW papers per author over a rolling two-year period** (R&R resubmissions excluded).
- **Review:** **double-anonymized** for regular manuscripts (authors anonymize the manuscript).
- **Style:** custom JAR **author-date** house style; match recent JAR articles (not APA-numeric).
- **Data and code:** JAR **requires and hosts** datasheets/code on acceptance; prepare the package now.
- **AI:** AI/AIGC tools **cannot be authors**.
- **Length / abstract limit:** **待核实** — no official JAR word/page or abstract limit was confirmable on 2026-06-01 (the Wiley `forauthors.html` page returned HTTP 402 to direct fetch). Confirm on the live page before submitting.

## Pre-submission checklist

### Anonymization (double-anonymized)
- [ ] Manuscript file contains **no** author names, affiliations, or acknowledgments
- [ ] Self-citations worded neutrally ("prior work (Author, 2021)"), not "our earlier study"
- [ ] Acknowledgments/funding/author bios on a **separate title page**, not in the manuscript
- [ ] File metadata scrubbed; file names contain no identifiers

### Fee & eligibility
- [ ] Correct **residency tier** determined for **all** authors (lower rate needs all in Tier Two/Three)
- [ ] Means to **pay within one week** of submission arranged (else the paper is withdrawn)
- [ ] Within the **four-new-papers / two-year** cap (R&Rs excluded)

### Files for Wiley Research Exchange
- [ ] Anonymized main manuscript (text, tables, figures as the portal specifies)
- [ ] Separate title page with all identifying information
- [ ] Cover letter (fit, contribution, not under review elsewhere)
- [ ] Correct **article type** selected (Regular / Survey / Registered Report)
- [ ] Online appendix / supplementary files if applicable

### Data-and-code package (JAR policy)
- [ ] Top-to-bottom runnable code regenerating every table/figure from raw extracts
- [ ] README documenting sources, screens, vintages, and access dates
- [ ] Terms-of-use respected (academic-research-only; acknowledge the JAR publication and code authors; authors retain copyright)

### References & consistency
- [ ] Every in-text citation appears in the reference list and vice versa
- [ ] Author-date formatting matches recent JAR articles
- [ ] Hypothesis labels, variable names, and table numbers consistent throughout

## Research Exchange operation notes

Create/keep your account and ORCID current; select the article type that routes the paper to the appropriate Senior/Associate Editor; upload anonymized files and the title page in the designated slots; preview the built PDF before final submission. Remember the **fee clock starts at submission**.

## Anti-patterns

- Self-identifying language ("in our 2020 study") left intact.
- Assuming the lower fee tier when a co-author resides in a Tier One country.
- Missing the **one-week payment** window and getting withdrawn.
- "Code available on request" instead of the required posted package.
- Wrong article type (e.g., submitting a Registered Report as a Regular Manuscript).

## Output format

```
【Anonymization】pass / fix: [...]
【Fee & tier】tier determined (all authors); pay-within-a-week arranged? [...]
【Submission cap】within four-new/two-years? [...]
【Article type】Regular / Survey / Registered Report
【Files ready】manuscript / title page / cover letter / supplements: yes/no
【Data-and-code package】runnable + README + terms respected? [...]
【References】citations↔list reconciled; JAR author-date matched: yes/no
【Next step】await decision → jar-review-process; on R&R → jar-rebuttal
```

## Resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official JAR/Chicago Booth/Wiley URLs behind every verified fact (accessed 2026-06-01)
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — submission, fee, and reproducibility tooling notes
