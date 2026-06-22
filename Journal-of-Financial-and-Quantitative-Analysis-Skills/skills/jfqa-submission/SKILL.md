---
name: jfqa-submission
description: Use when running the final pre-submission preflight for the Journal of Financial and Quantitative Analysis (JFQA) via Editorial Manager — text-searchable single PDF, 8.5x11 / 1-inch / 12-pt Times New Roman double-spaced formatting, double-anonymous anonymization, the 100-word abstract cap, the $350 fee, prior-rejection disclosure to avoid the one-year ban, and code-sharing exception timing. Final checks; it does not draft content.
---

# JFQA Submission Preflight (jfqa-submission)

Run this before pressing submit on **Editorial Manager** (`editorialmanager.com/jfqa/`). JFQA requires an account **separate** from a Cambridge Core account.

## Process facts (verify on the official page)

- Published by **Cambridge University Press** for the **University of Washington Foster School of Business**.
- **$350** fee (re-verified 2026-06-22, unchanged), credit card only; **$275 refunded** if the paper is not sent to a reviewer (a desk reject keeps **$75**). **Double-anonymous** review; the text-searchable PDF goes blind to reviewer(s). No fixed length limit, but over-long papers are likely desk-rejected.
- **Editor structure:** JFQA has **no single Editor-in-Chief** — seven **Managing Editors** (Bessembinder, Duchin, Foucault, Harford, Li, Pennacchi, Siegel as of 2026-06-22) handle papers by assignment. *Upcoming:* Pennacchi steps down 1 Sep 2026, replaced by Mariassunta Giannetti (announced 4 Jun 2026). Re-verify the current slate before submission.

## Preflight checklist

### Manuscript & formatting
- [ ] Single **text-searchable PDF** (no image-only pages, no separate figure files).
- [ ] **8.5 × 11** paper, **1-inch** margins, **12-pt Times New Roman**, **double-spaced** body and appendices.
- [ ] **Abstract**: one paragraph, **≤ 100 words** (see jfqa-contribution-framing).
- [ ] Tables/figures embedded, numbered, with self-contained notes (see jfqa-tables-figures).

### Anonymization (double-anonymous — required)
- [ ] No author names, affiliations, or acknowledgments in the PDF.
- [ ] Self-citations phrased neutrally; PDF metadata scrubbed of author identity.

### Disclosures & resubmission rule
- [ ] If this paper was **previously rejected by JFQA** and substantially modified, the **cover letter explicitly discloses the prior rejection** — failing to do so triggers desk rejection **and a one-year submission ban** for the corresponding author.
- [ ] Confirmed not under review elsewhere.

### Code-sharing timing
- [ ] If you need a **code-sharing exception** (e.g., delayed release for confidential data), it is requested **on this initial submission** — not later (see jfqa-replication-and-data-policy).

## Anti-patterns

- Image-only PDF; abstract over 100 words; wrong font/margins/spacing; author identity left in text or metadata.
- Resubmitting a previously rejected paper without disclosing it (one-year ban); requesting a code-sharing exception only after submission.

## Desk-reject patterns at the JFQA screen

| Pattern | Why it fails here | Preflight fix |
|---|---|---|
| Abstract at 130 words | violates a stated hard cap before content is judged | compress with jfqa-contribution-framing |
| Scanned or image-only exhibits | breaks the text-searchable-PDF requirement | regenerate exhibits as embedded vector/text |
| Manuscript far longer than the contribution | JFQA explicitly discourages over-long papers | move robustness to an Internet Appendix |
| Author name in PDF Properties | de-anonymizes a double-anonymous process | scrub metadata, rebuild from a clean profile |
| Undisclosed prior JFQA rejection | triggers desk rejection plus the one-year ban | disclose in the cover letter with the change summary |
| Descriptive essay without quantitative analysis | misses the journal's quantitative identity | retest fit via jfqa-topic-selection first |
| Exception request sent after submission | the policy requires it at initial submission | fold the request into today's cover letter |

## Submission-day run sheet

1. Rebuild the PDF from the final source on a clean user profile; verify searchability by text-searching a phrase from a table note.
2. Open the PDF properties and confirm Author/Creator fields carry no names; re-export if they do.
3. Re-count the abstract one final time — edits during revision quietly push it past 100 words.
4. Log in to the Editorial Manager JFQA account (it is separate from any Cambridge Core login); enter all co-authors with current affiliations in the metadata, which stays hidden from reviewers.
5. Paste the cover letter: prior-rejection disclosure if applicable, code-sharing exception request if needed, and a one-line fit statement naming the subfield.
6. Pay the $350 by credit card; download and archive the submission confirmation and the exact PDF submitted, since the R&R must diff against it months later.

Specific upload fields and fee mechanics evolve — confirm against the journal's current author guidelines on the day you submit.

## Output format

```
【PDF】single, text-searchable, exhibits embedded? [Y/N]
【Formatting】8.5x11 / 1-in / 12-pt TNR / double-spaced? [Y/N]
【Abstract】≤100 words, one paragraph? [Y/N]
【Anonymized】body + metadata clean? [Y/N]
【Prior-rejection disclosure】included if applicable? [Y/N/NA]
【Code exception】requested now if needed? [Y/N/NA]
【Fee】$350 ready ($275 refundable)? [Y/N]
【Next step】await desk decision → jfqa-rebuttal on R&R
```

## Supplementary resources

- [`templates/manuscript_template.md`](templates/manuscript_template.md) — JFQA manuscript skeleton (≤100-word abstract, intro arc, design, exhibits)
- [`templates/checklist.md`](templates/checklist.md) — pre-submission self-check
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — finance data sources and Stata/R/Python packages
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official JFQA URLs behind every fact
