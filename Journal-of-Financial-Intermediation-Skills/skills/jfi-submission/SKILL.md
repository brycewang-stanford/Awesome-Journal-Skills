---
name: jfi-submission
description: Use when running the final pre-submission preflight for the Journal of Financial Intermediation (JFI) via Editorial Manager — the US$500 non-refundable fee, single-PDF-for-review, up to 6 JEL codes and 6 keywords, optional SSRN preprint, and the mandatory generative-AI disclosure. Final checks; it does not draft content.
---

# Submission Preflight (jfi-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit in Editorial Manager
- Confirming what Editorial Manager expects at initial submission
- Checking the fee, JEL/keyword counts, and required declarations

## Process facts (verified 2026-06-01; re-confirm on the official Guide for Authors)

- JFI is published by **Elsevier** (ISSN 1042-9573); submission is via **Editorial Manager**, which
  converts uploaded files into a **single PDF** for peer review. Editable files (Word/LaTeX) are needed
  only for typesetting **after** acceptance.
- A **US$500 submission fee** applies to all new submissions, paid in Editorial Manager **before** the
  paper is considered; **desk-rejected papers are not refunded** (policy since 1 Jan 2018). The exact
  current amount is **待核实** — a 2026 live snippet referenced US$400; verify on the live page.
- Requires **up to 6 JEL classification codes** and a **maximum of 6 keywords**.
- **"Your-paper-your-way":** no strict reference style at submission as long as it is internally
  consistent; the author–date Elsevier style is applied at proof.
- A **Declaration of Generative AI and AI-assisted technologies in the writing process** must appear
  **before the References** if such tools were used; AI cannot be an author.
- Optional but encouraged: **Highlights** (3–5 bullets, max 85 characters each) and free **SSRN** preprint
  posting during submission (not prior publication).

## Preflight checklist

- [ ] Manuscript merges cleanly to **one review PDF**; numbered sections (1, 1.1, 1.1.1)
- [ ] References in any **internally consistent** style with clean author–year fields
- [ ] Concise, stand-alone abstract (no references in it); no numeric word cap stated — **待核实**
- [ ] **US$500 fee** ready in Editorial Manager (non-refundable on desk-reject)
- [ ] **≤ 6 JEL codes** and **≤ 6 keywords** chosen
- [ ] **Generative-AI declaration** placed before References (or omitted if not used)
- [ ] Decided on optional **SSRN** preprint and optional **Highlights**
- [ ] **Data Statement** prepared; datasets linked; `[dataset]` tags in references (see jfi-replication-and-data-policy)
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
- Generic JEL coding (G21 alone) when a precise set (e.g., G21 + G28 + E51) routes the paper to the right
  board expertise.
- Highlights written as full sentences exceeding the 85-character limit, truncated badly by the system.
- Fee paid but Data Statement or declarations missing, triggering an administrative return that delays
  triage. Current fee amount and the declaration list: confirm against the journal's current author
  guidelines.

## Anti-patterns

- Submitting without paying the fee, or expecting a refund after desk-reject
- Listing more than 6 JEL codes / 6 keywords
- Omitting the generative-AI declaration when such tools were used
- Anonymizing the manuscript as if it were double-blind — JFI is single-blind

## Output format

```
【Review PDF】one clean file? [Y/N]
【Fee】US$500 ready in Editorial Manager? [Y/N]  (amount 待核实)
【JEL ≤6 / Keywords ≤6】[Y/N]
【AI declaration】present-if-used, before References? [Y/N]
【Data Statement / [dataset] tags】[Y/N]
【Next step】single-blind review → jfi-rebuttal on R&R
```
