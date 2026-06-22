---
name: aeja-submission
description: Use when running the final pre-submission preflight for an American Economic Journal: Applied Economics (AEJ: Applied) manuscript via the AEA ScholarOne system — single-blind review front matter, JEL codes, submission and publication fees, format, disclosures, and AEA data-policy readiness. Final checks; it does not draft content.
---

# Submission Preflight (aeja-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on the AEA system
- Unsure which files, fees, and declarations the AEA submission expects
- Confirming title/byline/front matter, JEL codes, and disclosure statements are in order
- Confirming the paper is data-policy-ready should it advance

## Process facts (official AEA pages checked 2026-06-20; editor + fees re-verified 2026-06-22)

- AEJ: Applied is one of the four **American Economic Journals**, published by the **American Economic Association (AEA)**, quarterly; submission is through the **AEA online submission system**.
- **Single-blind review:** author identities are visible to referees; referee identities remain anonymous to authors. The manuscript should include title, byline, and author affiliations on the first page.
- **Submission fee:** AEA members: high-income USD 200, middle-income USD 100, low-income USD 0. Nonmembers: high-income USD 300, middle-income USD 200, low-income USD 0. Papers rejected without review receive a 50 percent refund.
- **Publication fee:** accepted papers first submitted on or after 1 February 2024 are assessed USD 15 per typeset page at proofs.
- **Length/front matter:** abstract of **100 or fewer words**; JEL codes; title, byline, and author affiliations on the first page; recommended maximum equivalent to 40 pages at 11-point/1.5 spacing/1-inch margins or 45 pages at 12-point/1.5 spacing/1-inch margins.
- **Editor (re-verified 2026-06-22):** Raymond Fisman (Boston University), lead-editor term beginning January 2026; coeditors Leah Boustan, Marika Cabral, Peter Hull, Xavier Jaravel, and Nicholas Ryan; **Data Editor:** Lars Vilhuber (Cornell). Re-verify the masthead on the AEA editors page before submission.
- **Data & code:** the AEA **Data and Code Availability Policy** applies; papers offered R&R are asked to submit their data replication package at resubmission, and accepted papers must clear the Data Editor's compliance/reproducibility check before publication (`aeja-replication-package`).
- One paper under review at a time per AEA rules; AI cannot be listed as an author.

## Preflight checklist

### Front matter
- [ ] Title, byline, and author affiliations appear on the first page
- [ ] Acknowledgement footnote includes author emails, author-order statement, funding/grants, acknowledgments, IRB details, and RCT registration where applicable
- [ ] **JEL codes** assigned; keywords listed; abstract is 100 words or fewer

### Format & exhibits
- [ ] Length within the AEJ: Applied recommendation or consciously justified
- [ ] Tables and figures legible; **standard errors reported** (stars permitted but SEs are required); exhibit notes self-contained
- [ ] Supplemental appendix prepared for nonessential material and kept separate from the main paper
- [ ] References complete and consistent (AEA author-date house style)

### Files, fee & policy readiness
- [ ] Main PDF + supplemental appendix uploaded as required by ScholarOne
- [ ] **Submission fee** ready for the submitting author's AEA membership and country-income tier
- [ ] Publication-page-fee exposure understood if accepted
- [ ] Replication package buildable into an openICPSR deposit; Data Availability Statement drafted
- [ ] Experimental/own-data: instructions/instruments ready; pre-registration cited

### Declarations
- [ ] Separate disclosure statement PDF for each author (including "nothing to disclose" where applicable)
- [ ] Confirmed not under review elsewhere; AI not listed as an author

## Anti-patterns

- Submitting a manuscript that hides the title/byline/affiliations despite the single-blind rule
- Forgetting **JEL codes**, disclosure PDFs, or the required front-page information
- Treating the data/code package as irrelevant at submission or R&R, then scrambling at the publication gate
- Omitting standard errors from exhibits, or notes that are not self-contained
- Assuming the fee tier without checking AEA membership and country-income status

## Output format

```
【Front matter】title/byline/affiliations + acknowledgement footnote + JEL + <=100-word abstract? [Y/N]
【Exhibits】SEs reported, notes self-contained, online appendix separate? [Y/N]
【Fee】submission tier and publication-page-fee exposure understood? [Y/N]
【Data-policy readiness】openICPSR-buildable + DAS drafted? [Y/N]
【Declarations】disclosure done; not under review elsewhere; no AI author? [Y/N]
【Next step】submit via AEA system → aeja-rebuttal after the decision
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — 8-section pre-submission self-check
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official AEA/AEJ: Applied URLs behind every fact
