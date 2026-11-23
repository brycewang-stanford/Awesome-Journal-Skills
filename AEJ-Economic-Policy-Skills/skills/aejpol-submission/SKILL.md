---
name: aejpol-submission
description: Use when running the final pre-submission preflight for AEJ: Economic Policy via the AEA ScholarOne system — author-anonymized manuscript and title page, JEL codes, submission and publication fees, format, the Data and Code Availability Statement, and disclosure. Final checks; it does not draft content.
---

# Submission Preflight (aejpol-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on the AEA system
- Unsure which files, declarations, and codes the AEA submission expects
- Confirming the anonymized manuscript, separate title page, JEL codes, and disclosure statements are in order
- Verifying the Data and Code Availability Statement and disclosures are in order

## Process facts (official AEA pages re-verified 2026-11-24; editor C. Kirabo Jackson and fees unchanged)

- AEJ: Policy is one of the **American Economic Association's** four *American Economic Journals*; it is **quarterly** and submitted through **ScholarOne Manuscripts** as a PDF (under 10 MB when reasonably possible). Re-confirm volatile specifics on the official AEA / AEJ: Policy pages.
- **Author-anonymized submission (changed fall 2026):** the AEA has launched a three-year randomized controlled trial of author-anonymized ("double-blind") reviewing across the AER, AER: Insights and the four AEJs, and the submission guidelines now require **anonymized manuscripts** for every submission: title and abstract at the top of the first page; author names, affiliations, contact information and the acknowledgement footnote in a separate PDF labelled "title page"; self-citations by name, never "my/our previous work"; no identifying locations, IRB approvals, or personal-website links; no RCT-registration entry in the reference list; supplementary appendix and response letters anonymized. The editorial-policy page still describes single-blind review (the control arm), so plan for either.
- **JEL codes** and **keywords** are customary (the current AEJ: Policy pages no longer state them as a rule); supply them on the submission form / title page.
- **Submission fee:** AEA members — USD 200 (high-income), USD 100 (middle-income), USD 0 (low-income); nonmembers — USD 300 (high-income), USD 200 (middle-income), USD 0 (low-income). Papers rejected without review are refunded 50 percent.
- **Publication fee:** accepted papers first submitted on or after 1 February 2024 are assessed USD 15 per typeset page at proofs.
- **Length:** abstract of **100 or fewer words**; recommended maximum equivalent to 40 pages at 11-point/1.5 spacing or 45 pages at 12-point/1.5 spacing, including figures, tables, references and appendices (average article 33–34 typeset pages).
- **Cover letter:** not required — use it (preferably the form field) only for coeditor conflicts or data-access limitations.
- **Data & code:** draft the **Data and Code Availability Statement** early (data and code are formally required before acceptance; note data-access limitations in the cover-letter field); the full deposit to the AEA Data and Code Repository (openICPSR) and the **AEA Data Editor** reproducibility check happen before publication (see `aejpol-replication-package`).
- **Disclosure:** the AEA Disclosure Policy applies — each author uploads a separate Disclosure Statement PDF (interested-party funding, relevant financial relationships, IRB status); submissions without them are not reviewed.
- **Style:** AEA house style; report standard errors in parentheses (the style guide says not to use significance asterisks); tables at most 9 columns; main text self-contained with an online appendix for long material.
- Not under consideration at another journal; AI cannot be listed as an author, and any AI use in preparing the manuscript must be briefly described during submission.

## Preflight checklist

### Front matter
- [ ] Manuscript PDF **anonymized**: title + abstract on page 1; no names, affiliations, or acknowledgement footnote; self-citations by name; no identifying study sites, IRB approvals, or personal links
- [ ] Separate **"title page" PDF**: authors, affiliations, contact information, and the acknowledgement footnote (funding/grants, acknowledgments, IRB details, RCT registration where applicable)
- [ ] **JEL codes** assigned and keywords listed (customary); abstract is 100 words or fewer

### Format & style
- [ ] AEA-style manuscript; standard errors in parentheses, **no significance asterisks/boldface**
- [ ] Figures/tables self-contained (sample, units, estimator, clustering, N); readable in greyscale
- [ ] Online appendix carries proofs/extra results; the main text is self-contained
- [ ] Length within the AEJ: Policy recommendation or consciously justified
- [ ] References author–year, complete and consistent

### Files & declarations for the AEA system
- [ ] Anonymized manuscript PDF + title-page PDF + anonymized online appendix uploaded to ScholarOne
- [ ] **Data and Code Availability Statement** drafted (public vs. restricted; sources cited)
- [ ] **Disclosure Statement PDF** per AEA policy for every author (funding / interested parties / IRB)
- [ ] **Submission fee** ready for the submitting author's membership and country-income tier
- [ ] Publication-page-fee exposure understood if accepted
- [ ] Confirmed: not under review elsewhere; AI not listed as an author; any AI use described in the submission form
- [ ] Experimental papers: pre-registration / pre-analysis plan and protocol referenced

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue aej-economic-policy-skills   # from a clone of the AJS repository
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

- Leaving author names, affiliations, the acknowledgement footnote, or "our previous work" in the manuscript PDF now that submissions must be anonymized
- Significance asterisks/boldface instead of standard errors
- Missing JEL codes or keywords on the form
- No Data and Code Availability Statement drafted (and no data-access limitations flagged) at submission
- Forgetting the AEA disclosure statement for a co-author
- Assuming the fee tier without checking AEA membership and country-income status

## Output format

```
【Front matter】anonymized PDF + separate title page (acknowledgement footnote) + JEL + <=100-word abstract? [Y/N]
【Style】SEs not asterisks; exhibits self-contained; online appendix set? [Y/N]
【Data/code statement】availability statement drafted? [Y/N]
【Disclosure】AEA disclosure for every author? [Y/N]
【Fee】submission tier + publication-page-fee exposure understood? [Y/N]
【Next step】submit via ScholarOne → expect anonymized or single-blind review under the AEA RCT (plan for an R&R)
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — 8-section pre-submission self-check
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official AEA / AEJ: Policy URLs behind every fact
