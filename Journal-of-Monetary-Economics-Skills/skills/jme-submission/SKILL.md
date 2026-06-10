---
name: jme-submission
description: Use when running the final pre-submission preflight for the Journal of Monetary Economics (JME) via Elsevier Editorial Manager — the US$350 (US$200 PhD) up-front fee, single-anonymized review, the 40-page / ≤10 tables-and-figures cap, 100-word abstract, line numbers, author-date references, JEL codes, and the supplementary-materials deposit. Final checks; it does not draft content.
---

# Submission Preflight (jme-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on Editorial Manager
- Unsure which files / fees Editorial Manager expects at submission
- Confirming the 40-page cap, 100-word abstract, and JME style are compliant
- Checking declarations and supplementary-materials requirements

## Process facts (verified; re-confirm on the official page)

- JME is published by **Elsevier**; submission is through **Elsevier Editorial Manager** at `editorialmanager.com/monec/` (not a generic portal).
- **Submission fee**: **US$350** for unsolicited new manuscripts; **US$200 for full-time PhD students.** Payment is **required at submission** — a manuscript is **only considered after payment.** **No fee** for revised/resubmitted manuscripts. If a paper is **desk-returned without full review** (≈ within 3 months), **half the fee is refunded.**
- **Review**: **single anonymized** (single-blind) — do **not** anonymize the manuscript. Typically sent to **at least two reviewers**. The first revision is **"up or out."**
- **Length cap (accepted papers)**: **≤ 40 pages** of text/references/footnotes and **≤ 10 tables and figures combined**; online supplements are exempt — design for this now.
- **Editors**: S. Borağan Aruoba (Maryland) and Eric Swanson (UC Irvine).

## Preflight checklist

### Format & style
- [ ] Abstract **≤ 100 words**, not beginning with "This paper" or "We"
- [ ] References **author-date**, journal titles **spelled out in full**; list after appendices, before tables/figures
- [ ] **Double-spaced, 12-point, 1-inch margins**, with **line numbers**
- [ ] **Footnotes** (superscript Arabic), not endnotes
- [ ] Up to **five keywords** and **at least one JEL code**
- [ ] Tables/figures Arabic-numbered; combined count **≤ 10** in the body; main text on track for **≤ 40 pages**

### Files for Editorial Manager
- [ ] Main manuscript (PDF/source per the current Guide for Authors)
- [ ] Cover letter — concise pitch + **up to five suggested referees** and any exclusions
- [ ] Online **supplementary appendix** (robustness, derivations, exempt from the cap)
- [ ] Replication materials staged for **ScienceDirect / Mendeley Data** (see jme-replication-and-data-policy)

### Declarations & fee
- [ ] **Generative-AI declaration** included per Elsevier policy
- [ ] Conflict-of-interest / funding disclosures prepared
- [ ] Confirmed the paper is not under review elsewhere
- [ ] **Fee ready to pay at submission** (US$350, or US$200 with PhD-student verification)

### Content sanity
- [ ] Contribution stated sharply enough to clear the editor's ~50% R&R bar (see jme-contribution-framing)
- [ ] Shock/mechanism identification complete (see jme-identification-strategy)
- [ ] No over-claiming beyond what the design/model supports

## Anti-patterns

- Anonymizing the manuscript (JME is single-blind, not double-blind)
- An abstract over 100 words or starting with "This paper" / "We"
- Forgetting line numbers, JEL codes, or the AI declaration
- Submitting without budgeting the **up-front fee** (the paper is not considered until paid)
- A body with more than 10 exhibits or well over 40 pages


## Submission readiness pass for Journal of Monetary Economics

Use this as a second-pass capability check. First lock the main macro object, the identifying variation, and the policy-relevant counterfactual; then test whether the manuscript addresses macro and monetary economists who expect the shock, mechanism, and policy margin to be visible early.

- **Primary move:** Verify portal, article type, anonymity, declarations, files, data/code, and current source-map facts; return blockers before formatting advice.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against JIE for open-economy trade/finance emphasis, RED for dynamic macro theory, AEJ Macro for broader field positioning; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Abstract】≤100 words, no "This paper"/"We"? [Y/N]
【References】author-date, full journal titles? [Y/N]
【Format】12pt double-spaced, line numbers, footnotes, JEL? [Y/N]
【Length】≤40 pages, ≤10 tables+figures in body? [Y/N]
【Files】manuscript / cover letter (5 referees) / supplement / replication? [Y/N each]
【Declarations + fee】AI declaration; fee ready to pay? [Y/N]
【Next step】await decision → jme-rebuttal on R&R (remember: up or out)
```
