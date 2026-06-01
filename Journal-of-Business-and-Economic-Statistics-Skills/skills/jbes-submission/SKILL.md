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

## Output format

```
【Live facts checked】platform / fee / length / abstract / blinding / style verified? [Y/N — 待核实]
【Manuscript】theorems + exhibits + references ready? [Y/N]
【Supplement】code+data + data availability statement + seeds? [Y/N]
【Declarations】COI / funding / not-under-review / restricted-data? [Y/N]
【Cover letter】method + relevance + Co-Editor targeting + referees? [Y/N]
【Next step】await decision → jbes-rebuttal on R&R
```
