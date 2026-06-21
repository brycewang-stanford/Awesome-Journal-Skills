---
name: jole-submission
description: Use when running the final pre-submission preflight for the Journal of Labor Economics (JOLE) via Editorial Manager — single-blind NON-anonymized format, title page with all co-authors, 100-word abstract, the 20,000-word soft cap, Chicago author-date references, and the non-refundable submission fee. Final checks; it does not draft content.
---

# Submission Preflight (jole-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on Editorial Manager
- Unsure which files Editorial Manager expects at the initial-submission stage
- Confirming single-blind (non-anonymized) format, the 100-word abstract, and Chicago author-date style are JOLE-compliant
- Checking the submission fee and declarations before paying

## Process facts (official source map; live-check the portal before upload)

- JOLE is published by the **University of Chicago Press** for the **Society of Labor Economists (SOLE)**; manuscripts are in **English** and submitted online via the current **Editorial Manager** route linked from the official instructions page.
- **Submission fee (since July 1, 2018): $100 for SOLE members, $175 for non-members.** It is **non-refundable even if the paper is desk-rejected**, and **the decision is not released until the fee is paid**. Budget for it; SOLE membership lowers it.
- The manuscript must **begin with a title page** giving **all co-authors' names, institutions, and email addresses**, followed by a **100-word abstract**.
- Review is **single-blind** (single-anonymized): referees are anonymous but know the author's identity, so **do NOT anonymize the manuscript and do NOT anonymize references**. This is the opposite of double-blind journals.
- JOLE does **not normally publish articles exceeding 20,000 words**, counting a **full-page table or figure as 500 words** toward that total.
- References use **University of Chicago Press author-date (Chicago)** style; in-text citations are ordered **chronologically, then alphabetically within the same year** (a, b disambiguation), with **"et al." for three or more authors**. LaTeX is accepted (`.bib`/`.bst` rules; Biblatex/Biber supported with a required directive line).
- Text and figures are preferred as **separate files** (or a single combined file). Operates under UChicago Press / **COPE** ethics guidelines.
- The direct Editorial Manager shell can display portal-status banners; enter through the live official instructions route and follow the prompts shown in that session.

## Preflight checklist

### Format & style

- [ ] **Title page first** with all co-authors' names, institutions, and emails (single-blind — NOT anonymized)
- [ ] **100-word abstract** immediately after the title page
- [ ] Manuscript **≤ ~20,000 words**, counting each full-page table/figure as **500 words**
- [ ] References in **Chicago author-date**; in-text **chronological then alphabetical within a year**; **"et al." for 3+ authors**
- [ ] Text and figures prepared as separate files (or one combined file) per current guidance
- [ ] Tables and figures numbered, called out in order, with self-contained notes
- [ ] If LaTeX, `.bib`/`.bst` and the Biber directive line are correct

### NOT anonymized (single-blind — required)

- [ ] Author names, affiliations, emails **present** on the title page
- [ ] Self-citations written normally; references **not** blinded
- [ ] (No double-blind scrubbing — that would be wrong for JOLE)

### Files for Editorial Manager

- [ ] Main manuscript (title page + 100-word abstract + body + exhibits)
- [ ] Cover letter (concise: labor question, design, headline result, fit with SOLE's audience)
- [ ] Portal path opened from the current UChicago Press instructions page, not an old bookmark
- [ ] Data/proprietary-data notice prepared if applicable (see Declarations)
- [ ] Replication materials staged for the accepted stage (see jole-replication-and-data-policy)

### Declarations & fee

- [ ] **Submission fee ready** ($100 SOLE / $175 non-member) — decision is withheld until paid
- [ ] Conflict-of-interest / disclosure consistent with AEA Disclosure Policy
- [ ] **Editor notified at submission if data are proprietary** or replication cannot be met
- [ ] Confirmed the paper is not under review elsewhere; human-subjects/confidential-data handling noted

### Final content sanity

- [ ] 100-word abstract states the finding with a number (see jole-writing-style)
- [ ] Identification diagnostics complete (see jole-identification-strategy, jole-data-analysis)
- [ ] No over-claiming beyond what the labor design supports

## Anti-patterns

- **Anonymizing the manuscript** — JOLE is single-blind; the title page must name all authors
- An abstract that runs past **100 words**
- A manuscript well over 20,000 words, or exhibit-heavy without counting each full page as 500 words
- Purely alphabetical in-text citations instead of chronological-then-alphabetical author-date
- Forgetting the **non-refundable fee** — the decision will not be released until it is paid
- Submitting from a stale portal bookmark without checking the current instructions route
- Failing to flag **proprietary data** to the editor at submission

## Output format

```
【Title page】all co-authors named (single-blind, NOT anonymized)? [Y/N]
【Abstract】≤ 100 words, states finding? [Y/N]
【Length】≤ ~20,000 words incl. 500/full-page exhibit? [Y/N]
【Reference style】Chicago author-date, chronological-then-alpha in-text? [Y/N]
【Fee】$100 SOLE / $175 non-member ready to pay? [Y/N]
【Declarations】disclosure + proprietary-data notice prepared? [Y/N]
【Next step】await decision → jole-rebuttal on R&R
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — labor data sources and Stata/R/Python packages
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official JOLE URLs and verification status behind every fact
