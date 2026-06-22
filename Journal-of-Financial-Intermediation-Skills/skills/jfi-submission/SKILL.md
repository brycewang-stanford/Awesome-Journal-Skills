---
name: jfi-submission
description: Use when running the final pre-submission preflight for the Journal of Financial Intermediation (JFI) via Editorial Manager — the US$500 non-refundable new-submission fee, the system-built review PDF, a <=250-word abstract, 1-7 English keywords, optional Highlights and SSRN preprint, Option C data links/statements, and the mandatory generative-AI disclosure. Final checks; it does not draft content.
---

# Submission Preflight (jfi-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit in Editorial Manager
- Confirming what Editorial Manager expects at initial submission
- Checking the fee, abstract/keyword metadata, data links/statements, and required declarations

## Process facts (verified 2026-06-22; re-confirm on the official Guide for Authors)

- JFI is published by **Elsevier** (ISSN 1042-9573); submission is via **Editorial Manager**, which
  converts uploaded files into a **single PDF** for peer review. Editable files (Word/LaTeX) are needed
  only for typesetting **after** acceptance.
- A **US$500 submission fee** applies to all new submissions, paid in Editorial Manager **before** the
  paper is considered; **desk-rejected papers are not refunded**. Transferred manuscripts do not pay
  another submission fee.
- Requires a concise factual **abstract not exceeding 250 words** and **1-7 English keywords**.
- **"Your-paper-your-way":** no strict reference style at submission as long as it is internally
  consistent; the author–date Elsevier style is applied at proof.
- A **Declaration of Generative AI and AI-assisted technologies in the writing process** must appear
  **before the References** if such tools were used; AI cannot be an author.
- Optional but encouraged: **Highlights** (3–5 bullets, max 85 characters each) and free **SSRN** preprint
  posting during submission (not prior publication).

## Preflight checklist

- [ ] Manuscript merges cleanly to **one review PDF**; numbered sections (1, 1.1, 1.1.1)
- [ ] References in any **internally consistent** style with clean author–year fields
- [ ] Concise, stand-alone abstract, **<=250 words**, no avoidable references
- [ ] **US$500 fee** ready in Editorial Manager (non-refundable on desk-reject)
- [ ] **1-7 English keywords** chosen for indexing
- [ ] **Generative-AI declaration** placed before References (or omitted if not used)
- [ ] Decided on optional **SSRN** preprint and optional **Highlights**
- [ ] **Option C data plan** ready: deposit/cite/link research data, or explain why data cannot be shared
- [ ] **Data Statement** prepared; datasets linked in EM where applicable; `[dataset]` tags in references
- [ ] Conflict-of-interest / funding statements ready; not under review elsewhere

## Fee-gated go/no-go before pressing submit

Because the fee is non-refundable on desk-reject, treat submission as a gated decision, not a formality:

- **Gate 1 — fit:** the jfi-topic-selection verdict is "strong," not "borderline"; a borderline
  intermediation fit means you are likely paying for a desk rejection.
- **Gate 2 — frame:** the abstract names the intermediary, friction, mechanism, and consequence
  (jfi-contribution-framing) — the desk screen reads no further.
- **Gate 3 — design:** the first objection a banking referee will raise (usually a demand-side confound)
  is already pre-empted in the introduction, not saved for Section 6.

## Cover-letter calibration for this desk screen

Three short paragraphs: what the paper shows about intermediation (one identified or proved claim, with
the headline magnitude or proposition); why this journal (name the sub-literature — relationship lending,
capital regulation, deposit competition — not "fits the aims and scope"); and any editor-expertise match
if you request a Managing Editor. Do not paste the abstract.

## Last-mile glitches that cost real money here

- The EM-built review PDF scrambles landscape tables — proof the system's PDF, not your local compile.
- Keywords are generic ("banking," "finance") rather than naming the intermediation mechanism and data.
- Highlights written as full sentences exceeding the 85-character limit, truncated badly by the system.
- Fee paid but Data Statement or declarations missing, triggering an administrative return that delays
  triage. Confirm the current declaration list against the journal's live author guidelines before final
  filing.

## Anti-patterns

- Submitting without paying the fee, or expecting a refund after desk-reject
- Submitting an abstract over 250 words or fewer than 1 / more than 7 English keywords
- Omitting the generative-AI declaration when such tools were used
- Anonymizing the manuscript as if it were double-blind — JFI is single-blind

## Output format

```
【Review PDF】one clean file? [Y/N]
【Fee】US$500 ready in Editorial Manager? [Y/N]
【Abstract / Keywords】<=250 words and 1-7 English keywords? [Y/N]
【AI declaration】present-if-used, before References? [Y/N]
【Option C data plan / Data Statement / [dataset] tags】[Y/N]
【Next step】single-blind review → jfi-rebuttal on R&R
```
