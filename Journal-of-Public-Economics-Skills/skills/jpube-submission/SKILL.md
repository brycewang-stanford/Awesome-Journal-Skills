---
name: jpube-submission
description: Use when running the final pre-submission preflight for the Journal of Public Economics (JPubE) via Editorial Manager — the US$165 submission fee (US$82.50 student / waived on transfer), single-anonymized review, 250-word abstract, author-date references, editable source files, SSRN option, and AI disclosure. Final checks; it does not draft content.
---

# Submission Preflight (jpube-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on Editorial Manager
- Unsure which files and fees Editorial Manager expects at submission
- Confirming abstract length, reference style, and source-file format are JPubE-compliant
- Checking declarations (AI, conflicts) and the SSRN preprint choice

## Process facts (verified; re-confirm on the official Guide for Authors)

- **Publisher Elsevier;** submission through Elsevier's **Editorial Manager** online system. Founded 1972 by Tony Atkinson; Co-Editors-in-Chief **John N. Friedman (Brown)** and **Wojciech Kopczuk (Columbia)**.
- **Submission fee: US$165** per unsolicited manuscript. A reduced **US$82.50** fee applies to **full-time students** via a student discount code (obtained by contacting the journal, entered during submission). The fee is **waived** when the manuscript is **transferred into the journal via Elsevier's article transfer service**. Unlike many top economics journals that are free or charge only a handling fee, JPubE charges this fee — budget for it unless you are transferring.
- **Single anonymized review;** suitable submissions go to a minimum of two reviewers (author identity is known to reviewers — see `jpube-review-process`).
- **Abstract: 250 words maximum**, concise and factual (purpose, principal results, major conclusion).
- **References: author-date (name-and-year)** in-text per Elsevier formatting.
- **Source files:** editable Word (**single-column**) or LaTeX (**.tex**; double-column permitted only for LaTeX).
- **Generative-AI use must be declared** at submission; **one appeal per submission** is considered under Elsevier's Appeal Policy.
- **Optional SSRN preprint** at submission, with no effect on the editorial outcome.

## Preflight checklist

### Format & style
- [ ] Editable source files ready (Word single-column **or** LaTeX `.tex`)
- [ ] Abstract ≤ **250 words**, factual (purpose / results / conclusion)
- [ ] References in **author-date** style, alphabetical by surname
- [ ] Tables/figures numbered, called in order, with self-contained notes
- [ ] Figures legible at print resolution (vector preferred)

### Fee & system
- [ ] **US$165** fee budgeted (or **US$82.50** student code obtained, or **waived via article transfer**)
- [ ] Editorial Manager account and manuscript metadata complete
- [ ] Suggested / excluded reviewers prepared (expert, fair, conflict-free)
- [ ] SSRN preprint opt-in decision made

### Declarations
- [ ] **Generative-AI** use declared if applicable
- [ ] Conflict-of-interest / disclosure statement prepared
- [ ] Funding and data-source disclosures prepared
- [ ] Data-availability statement ready (see jpube-replication-and-data-policy)
- [ ] Confirmed the paper is not under review elsewhere

### Content sanity
- [ ] Abstract states the policy finding with a number (see jpube-writing-style)
- [ ] Identification + welfare mapping complete (see jpube-identification-strategy, jpube-data-analysis)
- [ ] No over-claiming beyond what the design supports

## Anti-patterns

- Forgetting the **US$165** fee (or the student code / transfer waiver) and stalling at payment
- A PDF-only submission with no editable Word/LaTeX source
- An abstract over 250 words or with no headline number
- Numbered/footnote references instead of author-date
- Undeclared AI assistance; planning to "appeal twice" (only one appeal is considered)

## Desk-reject screen: what trips the first read

Before referees, a handling editor scans for fit and form. These are the avoidable stumbles that send a public-finance manuscript back without review.

| Trip wire | Why it bites at JPubE | Fix before submit |
|-----------|------------------------|-------------------|
| No welfare/policy payoff | Reads as a labor/IO paper with a tax control | Land the MVPF / sufficient-statistic / DWL claim in the abstract |
| Abstract > 250 words | Violates the stated cap | Cut to a number-bearing 250 |
| Flattened PDF only | No editable source for production | Ship Word single-column or LaTeX `.tex` |
| Fee unbudgeted | Stalls at the Editorial Manager payment step | Confirm US$165 / student code / transfer waiver |

## Worked vignette: a bunching paper at the payment screen (illustrative)

An author finishes a taxable-income-elasticity paper (headline **e = 0.3**, illustrative) and opens Editorial Manager the night before a deadline. The preflight catches three things: the abstract is 268 words and never states the DWL implication (trimmed to 248 with the welfare line added); the manuscript is a compiled PDF (editable `.tex` and figures gathered); and the US$165 fee is a fresh submission, not a transfer (payment arranged, not discovered at the final step). None is about the economics — all three are stall risks the screen removes.

## Calibration anchors

- The fee, abstract cap, single-anonymized model, and author-date style are operational tells of JPubE specifically — treat them as binding form checks.
- Hedge: fee amounts, the student-discount route, and the transfer waiver are volatile — re-confirm on the official Guide for Authors before quoting them.

## Output format

```
【Source files】editable Word single-column / LaTeX .tex? [Y/N]
【Abstract】≤250 words, states finding? [Y/N]
【References】author-date, alphabetical? [Y/N]
【Fee】US$165 / US$82.50 student / transfer-waived — handled? [which]
【Declarations】AI / COI / funding / data-availability ready? [Y/N each]
【SSRN】opt-in decision: [yes/no]
【Next step】submit via Editorial Manager → jpube-rebuttal on a decision
```
