---
name: isr-submission
description: Use when running the final pre-submission preflight for an Information Systems Research (ISR) manuscript — INFORMS ScholarOne portal, double-anonymization, the 32/38-page cap and formatting, the mandatory ~500-word contribution statement, and the required editor/reviewer nominations in the cover letter. Checks readiness to submit; it does not handle the post-decision response (isr-rebuttal).
---

# Pre-Submission Preflight (isr-submission)

## When to trigger

- "We're submitting this week" — the last check before hitting submit
- Unsure what the ISR cover letter must contain (contribution statement, nominations)
- Need to confirm double-anonymization and INFORMS formatting are complete

> Current ISR submission specs below were refreshed from official INFORMS pages on 2026-06-20. Re-verify on the official INFORMS ISR submission guidelines before submitting.

## Verified ISR/INFORMS specs (confirm current values)

- **Length:** manuscripts **not more than 32 pages of text** and **no more than 38 pages including all material** (references, appendixes, tables, figures). Overflow goes to the **electronic companion** (published if accepted).
- **Abstract:** **300 words maximum.**
- **Formatting:** **double-spaced**; standard font **at least 11 points**; **one-inch margins** on all four sides. INFORMS **author-date** reference style.
- **Submission portal:** INFORMS ScholarOne / Manuscript Central.
- **Review:** **double-anonymized**; a Senior Editor manages review (Associate Editor solicits 2-3 reviewers); final decision by the Senior Editor after an EIC **fit** assessment.
- **Fees:** the source-backed ISR fee is the optional post-acceptance INFORMS **Open Option** open access fee of **US$3,000**.

## ISR-specific cover-letter requirements (do not skip)

- [ ] **~500-word contribution statement** (required since **June 1, 2023**): the novel, rigorous, original contribution to IS; what the paper adds beyond existing literature; why it matters. Generic/missing statements are returned for revision and gate the EIC fit assessment.
- [ ] **Editor/reviewer nominations**: nominate **2 Senior Editors**, **2 Associate Editors**, and **5 preferred reviewers including at least 2 ERB members**. Choose non-conflicted experts in the focal IS conversation.
- [ ] Statement that the paper is not under review elsewhere; prior conference/working-paper versions disclosed.

## Anonymization (double-anonymized)

- [ ] Manuscript contains **no** author names, affiliations, or identifying acknowledgments
- [ ] Self-citations worded neutrally ("prior research (Author, 2020)"), not "our earlier work"
- [ ] Acknowledgments/funding on a **separate title page**, not in the manuscript
- [ ] File metadata and file names scrubbed of author/institution identity

## Format & files

- [ ] Separate title page: title, authors, affiliations, contact, acknowledgments, funding
- [ ] Abstract ≤ 300 words; main text ≤ 32 pages; total ≤ 38 pages
- [ ] Double-spaced, ≥11-pt, 1-inch margins; INFORMS author-date references
- [ ] Electronic companion prepared (proofs, full measurement items, extra robustness)
- [ ] Each table/figure self-contained and within the page budget

## Declarations

- [ ] Human-subjects/IRB stated where applicable; conflicts and funding on the title page
- [ ] Submitting-author ORCID linked
- [ ] Funding, conflict-of-interest, ethics, copyright/plagiarism, and prior-submission statements ready
- [ ] Data provenance certification ready; data/code package staged where it supports the claims

## Anti-patterns

- Submitting with a boilerplate or missing **contribution statement**.
- Omitting the **editor/reviewer nominations** the cover letter requires.
- Self-identifying language or acknowledgments left in the anonymized file.
- Main text over 32 pages because proofs/items were not moved to the companion.

## Output format

```
【Contribution statement】~500 words, ISR-specific? [...]
【Nominations】SEs/AEs/ERB listed? [...]
【Anonymization】pass/fix
【Format vs INFORMS guide】pages/abstract/spacing/style: pass/fix
【Electronic companion】prepared? [...]
【Declarations】IRB/ethics/provenance/data: complete?
【Next step】await decision → isr-review-process; on R&R → isr-rebuttal
```

## Resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — IS data sources and analysis/modeling software
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official INFORMS/ISR URLs behind every encoded current fact (refreshed 2026-06-20)
