---
name: aejpol-submission
description: Use when running the final pre-submission preflight for AEJ: Economic Policy via the AEA online submission system — single-blind review front matter, JEL codes, submission and publication fees, format, the Data and Code Availability Statement, and disclosure. Final checks; it does not draft content.
---

# Submission Preflight (aejpol-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on the AEA system
- Unsure which files, declarations, and codes the AEA submission expects
- Confirming title/byline/front matter, JEL codes, and disclosure statements are in order
- Verifying the Data and Code Availability Statement and disclosures are in order

## Process facts (official AEA pages checked 2026-06-20; editor C. Kirabo Jackson + fees re-verified 2026-06-22)

- AEJ: Policy is one of the **American Economic Association's** four *American Economic Journals*; it is **quarterly** and submitted through the **AEA online submission system**. Re-confirm volatile specifics on the official AEA / AEJ: Policy pages.
- **Single-blind review:** author identities are visible to referees; referee identities remain anonymous to authors. The submitted manuscript carries the title, byline, and author affiliations — do not anonymize it.
- **JEL codes** and **keywords** are required; supply them on the submission form / title information.
- **Submission fee:** AEA members — USD 200 (high-income), USD 100 (middle-income), USD 0 (low-income); nonmembers — USD 300 (high-income), USD 200 (middle-income), USD 0 (low-income). Papers rejected without review are refunded 50 percent.
- **Publication fee:** accepted papers first submitted on or after 1 February 2024 are assessed USD 15 per typeset page at proofs.
- **Length:** abstract of **100 or fewer words**; recommended maximum equivalent to 40 pages at 11-point/1.5 spacing or 45 pages at 12-point/1.5 spacing.
- **Data & code:** a **Data and Code Availability Statement** is expected; the full deposit to the AEA Data and Code Repository (openICPSR) and the **AEA Data Editor** reproducibility check happen before publication (see `aejpol-replication-package`).
- **Disclosure:** the AEA Disclosure Policy applies — each author discloses interested-party funding and relevant financial relationships.
- **Style:** AEA house style; report standard errors (no significance asterisks); main text self-contained with an online appendix for long material.
- One paper under review at a time per AEA rules; AI cannot be listed as an author.

## Preflight checklist

### Front matter
- [ ] Title, byline, and author affiliations appear on the first page
- [ ] Acknowledgement footnote includes author emails, funding/grants, acknowledgments, IRB details, and pre-registration where applicable
- [ ] **JEL codes** assigned; keywords listed; abstract is 100 words or fewer

### Format & style
- [ ] AEA-style manuscript; standard errors in parentheses, **no significance asterisks/boldface**
- [ ] Figures/tables self-contained (sample, units, estimator, clustering, N); readable in greyscale
- [ ] Online appendix carries proofs/extra results; the main text is self-contained
- [ ] Length within the AEJ: Policy recommendation or consciously justified
- [ ] References author–year, complete and consistent

### Files & declarations for the AEA system
- [ ] Main manuscript (PDF) with front matter + online appendix uploaded as required
- [ ] **Data and Code Availability Statement** drafted (public vs. restricted; sources cited)
- [ ] **Disclosure statement** per AEA policy for every author (funding / interested parties)
- [ ] **Submission fee** ready for the submitting author's membership and country-income tier
- [ ] Publication-page-fee exposure understood if accepted
- [ ] Confirmed: not under review elsewhere; AI not listed as an author
- [ ] Experimental papers: pre-registration / pre-analysis plan and protocol referenced

## Anti-patterns

- Hiding the title/byline/affiliations despite the single-blind rule
- Significance asterisks/boldface instead of standard errors
- Missing JEL codes or keywords on the form
- No Data and Code Availability Statement at submission
- Forgetting the AEA disclosure statement for a co-author
- Assuming the fee tier without checking AEA membership and country-income status

## Output format

```
【Front matter】title/byline/affiliations + acknowledgement footnote + JEL + <=100-word abstract? [Y/N]
【Style】SEs not asterisks; exhibits self-contained; online appendix set? [Y/N]
【Data/code statement】availability statement drafted? [Y/N]
【Disclosure】AEA disclosure for every author? [Y/N]
【Fee】submission tier + publication-page-fee exposure understood? [Y/N]
【Next step】submit via AEA system → expect single-blind review (plan for an R&R)
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — 8-section pre-submission self-check
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official AEA / AEJ: Policy URLs behind every fact
