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

## Cover letter skeleton (JBF-tuned)

```
Dear Editors,
We submit "[title]" for consideration at the Journal of Banking & Finance.
[1-2 sentences: finance question + setting, anchored in banking /
 intermediation / markets / regulation]
[1 sentence: identification or design in plain terms]
[1 sentence: headline result with magnitude in finance units]
[1 sentence: contribution relative to the closest JBF-relevant strand]
The manuscript is not under review elsewhere; the fee/waiver, declarations,
and data availability statement are complete in Editorial Manager.
```

## Highlights drafting (illustrative)

Elsevier Highlights are short result bullets (the common convention is 3-5 bullets of roughly 85 characters each — confirm against the journal's current author guidelines):

- "LCR adoption shifts large-bank lending toward short maturities" — good: result-forward.
- "We study liquidity regulation using a large panel" — bad: describes activity, not a finding.
- Lead every bullet with the finding; reserve one bullet for the policy-relevant magnitude.

## Submission-day order of operations

1. Final anonymization sweep: body text, acknowledgements, footnotes, file metadata.
2. Fee path confirmed: budget approval for the USD 350 or the waiver code in hand.
3. Declarations drafted offline (AI use, COI, funding, data availability) for pasting into Editorial Manager.
4. Upload in order: separate title page, anonymized manuscript, Highlights, declarations.
5. Record the SSRN opt-in decision and the suggested/excluded reviewer list.

## Last-mile failures specific to JBF

| Failure | Consequence | Fix before submitting |
| --- | --- | --- |
| PDF metadata shows an author name | administrative unblinding bounce | strip document properties on the anonymized file |
| Fee handled without budget approval | submission stalls in Editorial Manager | settle the USD 350 or the waiver code first |
| No data statement for licensed bank data | declarations incomplete | draft via jbf-replication-and-data-policy |
| Cover letter pitches only a "novel dataset" | weak desk-screen signal | re-pitch the intermediation mechanism via jbf-contribution-framing |

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
