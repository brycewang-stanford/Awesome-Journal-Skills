---
name: jbes-submission
description: Use when running the final pre-submission preflight for the Journal of Business & Economic Statistics (JBES) — files, the data-and-code supplement, declarations, and the cover letter for a multi-Co-Editor methods journal. Final checks; it does not draft content.
---

# Submission Preflight (jbes-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit
- Unsure which files JBES expects at initial submission
- Confirming the data/code supplement and declarations are ready
- Drafting the cover letter for a multi-Co-Editor journal

## Process facts (verified 2026-06-20, with live-T&F preflight required)

- JBES is published by **Taylor & Francis on behalf of the American Statistical Association (ASA)**; it
  is offered as **Open Select** / hybrid open access.
- Current Joint Editors are **Yingying Fan**, **Michael Kolesár**, and **Dacheng Xiu** per the official
  T&F search snippet; target the cover letter accordingly (see jbes-review-process).
- The live T&F author-instruction page must be opened before declaring a submission ready. This pack
  does not hard-code platform, fees, manuscript length, abstract limit, review anonymity model, or
  required citation style from indirect evidence.

## Preflight checklist

### Files & format
- [ ] Manuscript prepared per the **live** JBES instructions (format, length, abstract, and file rules)
- [ ] Theorems precise and self-contained; heavy proofs in an appendix
- [ ] Tables/figures numbered, called out in order, with self-contained notes (see jbes-tables-figures)
- [ ] References in the journal's required style after live T&F check
- [ ] If the live page requires anonymization, the manuscript and PDF metadata are anonymized

### Supplement (ASA expectation)
- [ ] Data-and-code supplement assembled (see jbes-replication-and-data-policy)
- [ ] Data availability statement included
- [ ] Master script regenerates every Monte Carlo and empirical exhibit; seeds set

### Declarations
- [ ] Conflict-of-interest / funding disclosures prepared per ASA/T&F ethics policy
- [ ] Confirmed the paper is not under review elsewhere
- [ ] Proprietary/restricted data flagged with access steps and any waiver request

### Cover letter
- [ ] Concise: the method, its novelty, the empirical relevance/application, and fit for JBES
- [ ] Targeted to a plausible handling Co-Editor's expertise
- [ ] Suggested/excluded referees prepared (expert, fair, conflict-free)

## Anti-patterns

- Asserting the platform, fee, length limit, or review-anonymity model without checking the live page
- Submitting strong theory with no empirical application (off-scope at a methods-with-empirics journal)
- Omitting the data/code supplement that ASA policy expects
- A generic cover letter that ignores the multi-Co-Editor model
- Budgeting an APC figure that was never officially confirmed


## Desk-reject and pre-submission patterns (venue-specific fixes)

| What gets a JBES submission bounced early | Fix this skill enforces |
|----|----|
| Strong theory, no empirical application | Add the substantive macro/finance/micro case; the empirics requirement is real, not optional |
| An off-the-shelf method on new data, no methodological increment | Reframe around the novel adaptation, or re-route to an applied economics journal |
| Data/code supplement missing | Assemble it per ASA expectation before pressing submit (see jbes-replication-and-data-policy) |
| Generic cover letter to a single "Editor" | Target a plausible handling Co-Editor; there is no single Editor-in-Chief |
| APC budgeted from a non-official figure | Treat the charge as Open Select/optional and confirm; do not assume a number |

Calibration anchor (hedged): JBES is published by **Taylor & Francis on behalf of the ASA** as Open
Select (hybrid OA). Treat platform, fees, length and abstract limits, review-anonymity model, and
citation style as live-page preflight items; do not infer them from other T&F journals.

## Submission pass for Journal of Business & Economic Statistics

Run this as a concrete capability pass. First lock the statistical estimand, identification/simulation evidence, empirical illustration, and reproducibility path; then test whether the manuscript addresses econometrics/statistics reviewers who expect methodological credibility plus a business or economic use case.

- **Primary move:** Treat current official instructions as volatile; verify portal, file format, anonymity, length, data, ethics, and disclosure requirements before saying ready.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against Journal of Econometrics for theory-heavy methods, Econometric Theory for proof-first work, Quantitative Economics for economics-theory methods; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, open the live T&F instructions and name the one
  submission-only fact that could change the recommendation.

## Output format

```
【Live T&F facts checked】platform / fee / length / abstract / review model / style? [Y/N]
【Manuscript】theorems + exhibits + references ready? [Y/N]
【Supplement】code+data + data availability statement + seeds? [Y/N]
【Declarations】COI / funding / not-under-review / restricted-data? [Y/N]
【Cover letter】method + relevance + Co-Editor targeting + referees? [Y/N]
【Next step】await decision → jbes-rebuttal on R&R
```
