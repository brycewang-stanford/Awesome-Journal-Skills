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

## Process facts (verified vs. 待核实)

- JBES is published by **Taylor & Francis on behalf of the American Statistical Association (ASA)**; it is offered as **Open Select** (hybrid open access — an optional article publishing charge applies only if you choose OA). Source: tandfonline.com/journals/ubes20.
- The **submission platform** (ScholarOne / Editorial Manager / a T&F portal), any **submission fee**, the **manuscript length/word limit**, the **abstract word limit**, the **peer-review blinding model**, and the **required formatting/citation style** could **not** be confirmed (the official instructions page was Cloudflare-blocked). All are **待核实** — confirm on the live JBES instructions-for-authors page before submitting. Do not assume an APC figure; a third-party ~US$2,500 number was not verified.
- Editors are a **rotating panel of Co-Editors / Joint Editors** (no single Editor-in-Chief); target the cover letter accordingly (see jbes-review-process).

## Preflight checklist

### Files & format
- [ ] Manuscript prepared per the **live** JBES instructions (format/length/abstract limit — 待核实, verify on the page)
- [ ] Theorems precise and self-contained; heavy proofs in an appendix
- [ ] Tables/figures numbered, called out in order, with self-contained notes (see jbes-tables-figures)
- [ ] References in the journal's required style (待核实)
- [ ] If the review is anonymized (待核实), the manuscript and PDF metadata are anonymized

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

- Asserting the platform, fee, length limit, or blinding model without checking the live page (all 待核实)
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
| APC budgeted from an unverified figure | Treat the charge as Open Select/optional and confirm; do not assume a number |

Calibration anchor (hedged): JBES is published by **Taylor & Francis on behalf of the ASA** as Open Select (hybrid OA). The submission platform, fee, length and abstract limits, blinding model, and citation style are **待核实** — the official instructions page was Cloudflare-blocked; confirm each against the journal's current author guidelines before declaring the package ready.

## Submission pass for Journal of Business & Economic Statistics

Run this as a concrete capability pass. First lock the statistical estimand, identification/simulation evidence, empirical illustration, and reproducibility path; then test whether the manuscript addresses econometrics/statistics reviewers who expect methodological credibility plus a business or economic use case.

- **Primary move:** Treat current official instructions as volatile; verify portal, file format, anonymity, length, data, ethics, and disclosure requirements before saying ready.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against Journal of Econometrics for theory-heavy methods, Econometric Theory for proof-first work, Quantitative Economics for economics-theory methods; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Live facts checked】platform / fee / length / abstract / blinding / style verified? [Y/N — 待核实]
【Manuscript】theorems + exhibits + references ready? [Y/N]
【Supplement】code+data + data availability statement + seeds? [Y/N]
【Declarations】COI / funding / not-under-review / restricted-data? [Y/N]
【Cover letter】method + relevance + Co-Editor targeting + referees? [Y/N]
【Next step】await decision → jbes-rebuttal on R&R
```
