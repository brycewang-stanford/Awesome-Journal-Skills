---
name: aeja-submission
description: Use when running the final pre-submission preflight for an American Economic Journal: Applied Economics (AEJ: Applied) manuscript via the AEA ScholarOne system — author-anonymized manuscript and title page, JEL codes, submission and publication fees, format, disclosures, and AEA data-policy readiness. Final checks; it does not draft content.
---

# Submission Preflight (aeja-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on the AEA system
- Unsure which files, fees, and declarations the AEA submission expects
- Confirming title/byline/front matter, JEL codes, and disclosure statements are in order
- Confirming the paper is data-policy-ready should it advance

## Process facts (official AEA pages checked 2026-06-20; re-verified 2026-11-23)

- AEJ: Applied is one of the four **American Economic Journals**, published by the **American Economic Association (AEA)**, quarterly; submission is through the **AEA online submission system**.
- **Author-anonymized submission (changed fall 2026):** the AEA has launched a three-year randomized controlled trial of author-anonymized ("double-blind") reviewing across the AER, AER: Insights and the four AEJs, and the submission guidelines now require **anonymized manuscripts** for every submission: title and abstract at the top of the first page; author names, affiliations, contact information and the acknowledgement footnote moved to a separate PDF labelled **"title page"**; self-citations by name without "my/our"; no identifying study sites, IRB approvals, personal-website links, or RCT-registration reference-list entries; supplementary appendices and response letters anonymized. (The editorial-policy page still describes single-blind review; papers in the control arm are reviewed that way.)
- **AEA templates** may be used, in "review mode"; Chicago Manual author-date preferred for bibliographic software; PDF under 10 MB when reasonably possible.
- **Submission fee:** AEA members: high-income USD 200, middle-income USD 100, low-income USD 0. Nonmembers: high-income USD 300, middle-income USD 200, low-income USD 0. Papers rejected without review receive a 50 percent refund.
- **Publication fee:** accepted papers first submitted on or after 1 February 2024 are assessed USD 15 per typeset page at proofs.
- **Length/front matter:** abstract of **100 or fewer words**; JEL codes customary (not stated as a rule on the current AEJ pages); title and abstract on the first page of the anonymized manuscript; recommended maximum equivalent to 40 pages at 11-point/1.5 spacing/1-inch margins or 45 pages at 12-point/1.5 spacing/1-inch margins.
- **Editor (re-verified 2026-11-23):** Raymond Fisman (Boston University), lead-editor term beginning January 2026; coeditors Marika Cabral, Richard Hornbeck, Peter Hull, Xavier Jaravel, and Namrata Kala (Leah Boustan and Nicholas Ryan completed their terms in 2026); **Data Editor:** Lars Vilhuber (Cornell). Re-verify the masthead on the AEA editors page before submission.
- **Data & code:** the AEA **Data and Code Availability Policy** applies; papers offered R&R are asked to submit their data replication package at resubmission, and accepted papers must clear the Data Editor's compliance/reproducibility check before publication (`aeja-replication-package`).
- One paper under review at a time per AEA rules; AI cannot be listed as an author.

## Preflight checklist

### Front matter
- [ ] Manuscript PDF anonymized: title + abstract on page 1, no names/affiliations/acknowledgement footnote; self-citations by name, no "our previous work"; no identifying sites, IRB approvals, or personal links
- [ ] Separate **"title page" PDF** with names, affiliations, contact information and the acknowledgement footnote, which includes author emails, author-order statement, funding/grants, acknowledgments, IRB details, and RCT registration where applicable
- [ ] **JEL codes** assigned; keywords listed; abstract is 100 words or fewer

### Format & exhibits
- [ ] Length within the AEJ: Applied recommendation or consciously justified
- [ ] Tables and figures legible; **standard errors reported** in parentheses, no significance asterisks (style guide); exhibit notes self-contained
- [ ] Supplemental appendix prepared for nonessential material and kept separate from the main paper
- [ ] References complete and consistent (AEA author-date house style)

### Files, fee & policy readiness
- [ ] Main PDF + supplemental appendix uploaded as required by ScholarOne
- [ ] **Submission fee** ready for the submitting author's AEA membership and country-income tier
- [ ] Publication-page-fee exposure understood if accepted
- [ ] Replication package buildable into an openICPSR deposit; Data Availability Statement drafted
- [ ] Experimental/own-data: instructions/instruments ready; pre-registration cited

### Declarations
- [ ] Separate disclosure statement PDF for each author (including "nothing to disclose" where applicable) — submissions without them are incomplete and not reviewed
- [ ] AI use in preparing the manuscript (including drafting or editing text) briefly described in the submission form
- [ ] Field experiment: AEA RCT ID entered in the submission form (registration cited on the title page, not in the anonymized reference list)
- [ ] Confirmed not under review elsewhere; AI not listed as an author

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue aej-applied-economics-skills   # from a clone of the AJS repository
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
- Forgetting **JEL codes**, disclosure PDFs, or the required front-page information
- Treating the data/code package as irrelevant at submission or R&R, then scrambling at the publication gate
- Omitting standard errors from exhibits, or notes that are not self-contained
- Assuming the fee tier without checking AEA membership and country-income status

## Output format

```
【Front matter】anonymized PDF + separate title page (acknowledgement footnote) + JEL + <=100-word abstract? [Y/N]
【Exhibits】SEs reported, no asterisks, notes self-contained, online appendix separate? [Y/N]
【Fee】submission tier and publication-page-fee exposure understood? [Y/N]
【Data-policy readiness】openICPSR-buildable + DAS drafted? [Y/N]
【Declarations】disclosure done; not under review elsewhere; no AI author? [Y/N]
【Next step】submit via AEA system → aeja-rebuttal after the decision
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — 8-section pre-submission self-check
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official AEA/AEJ: Applied URLs behind every fact
