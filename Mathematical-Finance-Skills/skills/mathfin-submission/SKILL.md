---
name: mathfin-submission
description: Use when running the final Mathematical Finance submission preflight through Wiley Research Exchange, including LaTeX source, compiled PDF, supplementary files, classifications, data availability statement, and single-blind review considerations.
---

# Submission Preflight (mathfin-submission)

## When to trigger

- The paper is ready to submit through Wiley Research Exchange
- You need to check LaTeX files, classifications, appendices, and policy statements
- You are unsure what a theory-first Wiley submission needs before upload

## Preflight checklist

### Scientific readiness

- [ ] Main theorem(s) stated with complete hypotheses and conclusions
- [ ] Full proofs included or placed in appendices
- [ ] Detailed mathematical analysis moved to appendix where appropriate
- [ ] Numerical experiments, if any, tied to rigorous analysis
- [ ] Contribution to financial modelling explicit in abstract and introduction

### Files

- [ ] Main Document - LaTeX `.tex` file
- [ ] Main Document - compiled PDF
- [ ] LaTeX supplementary/supporting files as needed
- [ ] Figures and tables prepared as separate files if required at revision
- [ ] Bibliography file and custom macros included

### Metadata and declarations

- [ ] Title, abstract, keywords
- [ ] JEL and AMS/MSC classifications where requested
- [ ] Data Availability Statement
- [ ] Funding, conflicts, acknowledgements
- [ ] Open Access choice and APC implications checked if relevant

## LaTeX hygiene

- Keep custom macros minimal and defined in one place.
- Confirm the PDF compiles from a clean checkout.
- Avoid fragile local paths.
- Ensure theorem, lemma, proposition, assumption, and equation labels are stable.

## Output format

```text
[Scientific readiness] pass / gaps
[Files ready] tex / pdf / bib / figures / supplement
[Policy statements] data / conflicts / funding / OA
[Live checks needed] editor / APC / fee / style
[Next step] submit or fix listed gaps
```
