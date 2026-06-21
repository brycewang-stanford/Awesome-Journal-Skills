---
name: jm-submission
description: Use when running the final pre-submission preflight for a Journal of Marketing (JM) manuscript — the ScholarOne (Sage Track) portal, double-anonymized formatting, the 50-page inclusive limit, exact-statistic reporting, the Data Availability Statement, and the JM Dataverse plan. Checks readiness to submit; it does not handle the post-decision response (jm-rebuttal).
---

# Pre-Submission Preflight (jm-submission)

## When to trigger

- "We're submitting this week" — the last check before hitting submit
- Unsure what ScholarOne (Sage Track) requires (anonymized file, title page, statements)
- Verifying the manuscript matches current JM/AMA formatting requirements
- Confirming double-anonymization and the Data Availability Statement are in place

> Always live-check current limits, required files, and portal prompts on the official JM/SAGE/AMA submission pages before submitting. As of 2026-06-20 the verified key specs are below.

## Verified JM/AMA specs (confirm current values)

- **Submission portal**: ScholarOne / Manuscript Central (Sage Track) at **mc.manuscriptcentral.com/ama_jm**; **online submission only** (no mail/email).
- **Length**: **50-page maximum**, properly formatted and **inclusive of** title, abstract, keywords, text, footnotes, references, tables, figures, and print appendices; **web appendices do not count**.
- **Abstract**: **200 words** maximum, unstructured.
- **Keywords**: **minimum 3** (AMA also allows up to 8 primary keywords).
- **Formatting**: **12-point Times New Roman** (or 12-pt LaTeX font); double-spaced (tables/references may be single-spaced); **1-inch margins**; **no page numbers, line numbers, headers, or footers**. AMA Word/LaTeX templates are provided.
- **Citations**: AMA author-date; full author names for up to three authors, "et al." for four or more.
- **Statistics**: empirical papers must report **actual p-values, standard errors, and effect sizes**.
- **Review**: **double-anonymized** — remove all author/institution identifiers; the handling Editor is the final decision authority.
- **Integrity**: **iThenticate** plagiarism screening; conflict-of-interest disclosure.
- **Transparency**: **Data Availability Statement** required; replication packet deposited to **JM Dataverse** at conditional acceptance; **preregistration encouraged** (anonymized links + attestation). Applies to conditionally accepted revisions of manuscripts submitted on/after 2023-01-01. Some conditionally accepted JM manuscripts may go through a Data Editor verification step.
- **Fees**: SAGE states there are **no fees payable to submit or publish** in the subscription route; optional Sage Choice/Open Access may carry a fee, and OA fees do not cover separate page or color charges.
- **Preprints / ORCID**: preprints are accepted; enter the preprint DOI at submission and avoid posting updated versions during review. Authors and coauthors are encouraged to link ORCID IDs before acceptance.

## Pre-submission checklist

### Anonymization (double-anonymized)

- [ ] Manuscript file contains **no** author names, affiliations, or acknowledgments
- [ ] Self-citations worded neutrally ("prior research (Author, 2020)"), not "our earlier work"
- [ ] Acknowledgments, funding, ORCID/author bios live on a **separate title page**
- [ ] Preregistration links are **anonymized** (no identity leakage)
- [ ] File metadata/properties and file names scrubbed of author/institution identity

### Format (verify against current AMA/JM guidelines)

- [ ] **12-pt Times New Roman**, double-spaced; **1-inch margins**; **no page/line numbers, headers, or footers**
- [ ] Abstract ≤ **200 words**; **≥3 keywords**
- [ ] AMA author-date citations (full names ≤3; et al. ≥4); reference list complete
- [ ] Main document **≤ 50 pages** inclusive (text + refs + tables + figures + footnotes + print appendices); web appendices separate
- [ ] Tables/figures report exact p-values, SEs, and effect sizes

### Files for ScholarOne (Sage Track)

- [ ] Anonymized main document (manuscript + tables + figures, or as the portal specifies)
- [ ] Separate title page with all identifying information + **Data Availability Statement**
- [ ] Cover letter to the editor (fit, substantive + managerial contribution, not under review elsewhere)
- [ ] Web appendix file(s) for supplementary results (excluded from page count)
- [ ] Replication materials prepared for **JM Dataverse** deposit at conditional acceptance

### Declarations & ethics

- [ ] Human-subjects/IRB approval stated where applicable (on title page, not anonymized text)
- [ ] **Data Availability Statement** on the title page
- [ ] Optional OA, page, or color-charge prompts checked if relevant
- [ ] ORCID IDs linked before acceptance where possible
- [ ] No concurrent submission; conference/working-paper versions disclosed in the cover letter
- [ ] Conflicts of interest and funding disclosed on the title page
- [ ] Preregistration attestation prepared (faithful representation), if applicable

### References & consistency

- [ ] Every in-text citation appears in the reference list and vice versa
- [ ] The substantive canon of the conversation is cited (routing-aware for Coeditor/reviewers)
- [ ] Hypothesis labels, construct names, and exhibit numbers consistent throughout

## ScholarOne (Sage Track) operation notes

- Submit through ScholarOne at **mc.manuscriptcentral.com/ama_jm**; keep your account and ORCID current.
- Select the article type and keywords so the manuscript routes to the appropriate Coeditor (Fischer / Haws / Scott / Slotegraaf) and reviewers.
- Upload the anonymized file and the title page in the slots the system designates; preview the built PDF before final submission.

## Anti-patterns

- Self-identifying language ("in our 2019 study") or a preregistration link that reveals identity.
- Stars-only / "p < .05" statistics instead of exact p-values, SEs, and effect sizes.
- Forgetting that tables, figures, references, and print appendices all count toward the 50-page limit.
- Missing Data Availability Statement, or no plan for the JM Dataverse packet.
- Wrong (non-AMA) citation style straight from a reference manager.

## Output format

```
【Anonymization】pass / fix: [...]
【Format vs. AMA guide】50-page inclusive, 12-pt, no page/line numbers, abstract ≤200w, ≥3 keywords: [...]
【Exact statistics】p-values + SEs + effect sizes present? yes/no
【Files ready】anon manuscript / title page + DAS / cover letter / web appendix: yes/no
【Transparency】Data Availability Statement + JM Dataverse plan + prereg attestation: [...]
【Declarations】IRB / disclosures / no concurrent submission: complete?
【Next step】await decision → jm-review-process; on R&R → jm-rebuttal
```

## Resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — marketing-research data and analysis software (NielsenIQ / Circana / Prolific / Qualtrics / Stata reghdfe / R lavaan / PROCESS)
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official AMA/SAGE/JM URLs behind every verified fact (accessed 2026-06-20) and live-check items
