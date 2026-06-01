---
name: jbf-submission
description: Use when running the final pre-submission preflight for the Journal of Banking & Finance (JBF) via Elsevier Editorial Manager — the USD 350 submission fee, double-anonymized manuscript plus separate title page, free-format submission, author-date references, keywords/JEL, Highlights, SSRN posting, and the generative-AI declaration. Final checks; it does not draft content.
---

# Submission Preflight (jbf-submission)

## When to trigger

- Submitting this week — last check before pressing submit in Editorial Manager
- Unsure what Editorial Manager expects at initial submission
- Confirming anonymization, fee, and declarations are JBF-compliant

## Process facts (verified 2026-06-01; re-confirm on the official guide — several Elsevier/ScienceDirect pages were CAPTCHA/403-gated)

- **Elsevier**; submission exclusively through **Editorial Manager** (via the journal homepage on ScienceDirect).
- A **USD 350 fee** applies to unsolicited new manuscripts, paid in Editorial Manager. It is **non-refundable**, and a paper may be **desk-rejected without review** even after payment. **Waiver/discount codes** exist for authors with limited means or from developing countries — request one pre-submission, then enter it in Editorial Manager.
- Review is **double anonymized**: an **anonymized manuscript** (no names, affiliations, or identifying acknowledgements) plus a **separate title page**.
- **Free-format ("your paper your way")**: no strict length limit; any consistent reference style at first submission, with Elsevier author-date (Harvard) applied at proof.
- Provide **1-7 English keywords**; **JEL codes** expected (待核实). **Highlights** encouraged. **Generative-AI use must be declared**. Free **SSRN** posting is offered (public once past initial desk review). Abstract cap not JBF-specified; Elsevier default (often ≤250 words) likely — 待核实.

## Preflight checklist

- [ ] Anonymized manuscript (no identity in body or PDF metadata; self-citations neutral)
- [ ] Separate **title page** (authors, affiliations, corresponding author, acknowledgements, funding)
- [ ] Consistent references; 1-7 keywords; JEL codes; Highlights (3-5 bullets)
- [ ] Fee path settled: pay **USD 350** or enter an approved waiver/discount code
- [ ] Declared any **generative-AI** use; opted into **SSRN** posting if desired
- [ ] Suggested/excluded reviewers; cover letter (question, design, headline result, JBF fit)
- [ ] COI/funding disclosures; not under review elsewhere; data availability statement (see jbf-replication-and-data-policy)

## Anti-patterns

- Budgeting zero for the fee, or expecting a refund after a desk reject
- Leaving author identity in the manuscript or PDF metadata under double-anonymized review
- Forgetting the separate title page, or the AI-use declaration

## Output format

```
【Anonymization】body + metadata clean; title page separate? [Y/N]
【Fee】USD 350 paid OR waiver code entered? [Y/N]
【Keywords/JEL】1-7 keywords + JEL set? [Y/N]
【Declarations】AI use + COI/funding + data statement? [Y/N]
【Next step】await desk screen → jbf-review-process; R&R → jbf-rebuttal
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — data sources and Stata/R/Python packages for empirical banking & finance
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official JBF URLs behind every fact in this pack
