---
name: aejpol-submission
description: Use when running the final pre-submission preflight for AEJ: Economic Policy via the AEA submission system — double-blind anonymization, JEL codes, format, the Data and Code Availability Statement, and disclosure. Final checks; it does not draft content.
---

# Submission Preflight (aejpol-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on the AEA system
- Unsure which files, declarations, and codes the AEA submission expects
- Confirming the manuscript is properly anonymized for double-blind review
- Verifying the Data and Code Availability Statement and disclosures are in order

## Process facts (检索于 2026-06；以官网为准)

- AEJ: Policy is one of the **American Economic Association's** four *American Economic Journals*; it is **quarterly** and reviewed **double-blind** through the **AEA submission system**. Re-confirm volatile specifics on the official AEA / AEJ: Policy pages.
- **Double-blind:** the manuscript, exhibits, and any supplementary files must be **anonymized** — no author names, acknowledgments, funding-by-name, identifying self-citations ("in our earlier work"), or identifying file paths.
- **JEL codes** and **keywords** are required; supply them on the submission form / title information.
- **Submission fee:** an AEA submission fee applies (reduced/waived categories exist for members/students/some countries) — amount is **VOLATILE; verify on the AEA site** before submitting.
- **Data & code:** a **Data and Code Availability Statement** is expected; the full deposit to the AEA Data and Code Repository (openICPSR) and the **AEA Data Editor** reproducibility check happen at the conditional-acceptance stage, **before publication** (see `aejpol-replication-package`).
- **Disclosure:** the AEA Disclosure Policy applies — each author discloses interested-party funding and relevant financial relationships.
- **Style:** AEA house style; report standard errors (no significance asterisks); main text self-contained with an online appendix for long material.

## Preflight checklist

### Anonymization (double-blind)
- [ ] No author names / affiliations / emails anywhere in the manuscript or exhibits
- [ ] Acknowledgments and named funding removed from the review version
- [ ] Self-citations phrased neutrally (no "our prior paper")
- [ ] File metadata and identifying paths scrubbed; data named neutrally

### Format & style
- [ ] AEA-style manuscript; standard errors in parentheses, **no significance asterisks/boldface**
- [ ] Figures/tables self-contained (sample, units, estimator, clustering, N); readable in greyscale
- [ ] Online appendix carries proofs/extra results; the main text is self-contained
- [ ] Abstract present; **JEL codes + keywords** supplied
- [ ] References author–year, complete and consistent

### Files & declarations for the AEA system
- [ ] Anonymized main manuscript (PDF) + anonymized appendix/exhibits
- [ ] **Data and Code Availability Statement** drafted (public vs. restricted; sources cited)
- [ ] **Disclosure statement** per AEA policy for every author (funding / interested parties)
- [ ] Submission fee ready (or eligible category confirmed) — **verify current amount**
- [ ] Confirmed: not under review elsewhere; AI not listed as an author
- [ ] Experimental papers: pre-registration / pre-analysis plan and protocol referenced

## Anti-patterns

- Submitting a manuscript that de-anonymizes the authors (defeats double-blind)
- Significance asterisks/boldface instead of standard errors
- Missing JEL codes or keywords on the form
- No Data and Code Availability Statement at submission
- Forgetting the AEA disclosure statement for a co-author
- Assuming the fee amount instead of checking the current AEA figure

## Output format

```
【Anonymized】no authorship leak in text/exhibits/metadata? [Y/N]
【Style】SEs not asterisks; exhibits self-contained; online appendix set? [Y/N]
【JEL + keywords】supplied on the form? [Y/N]
【Data/code statement】availability statement drafted? [Y/N]
【Disclosure】AEA disclosure for every author? [Y/N]
【Fee】current amount verified / eligible category confirmed? [Y/N]
【Next step】submit via AEA system → expect double-blind review (plan for an R&R)
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — 8-section pre-submission self-check
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official AEA / AEJ: Policy URLs behind every fact
