---
name: jru-submission
description: Use when running the final pre-submission preflight for the Journal of Risk and Uncertainty (JRU) via Springer's portal — file set, anonymization, Data Availability Statement, ethics and AI disclosures, and house-style checks. Final checks; it does not draft content.
---

# Submission Preflight (jru-submission)

## When to trigger

- "Submitting this week" — last pass before uploading to Springer's submission system
- Unsure which files Springer's Editorial Manager expects, or how to anonymize for review
- Confirming the Data Availability Statement, ethics, funding, and AI-use disclosures are in place
- Verifying the abstract, length, and reference style conform before the editor sees the paper

## Process facts (检索于 2026-06；以官网为准)

- JRU is published by **Springer** (Springer Science+Business Media); content sits on **Springer Nature Link** (ISSN 0895-5646 print / 1573-0476 electronic). Editor-in-Chief and founder: **W. Kip Viscusi** (Vanderbilt), who has led the journal since 1988 (re-verified 2026-06-22 against the Springer editorial-board page; re-confirm before relying).
- Submission is through Springer's online system (**Editorial Manager**, the Springer standard — 待核实 against the live guidelines); the Editor-in-Chief reserves the right to reject submissions that do not meet the author guidelines.
- Review model: **single-blind** is the Springer econ default — **待核实**; confirm whether JRU anonymizes. If single-blind, author identities are visible to referees and need not be stripped, but verify before relying on it.
- **Data Availability Statement** is required on original research articles; Springer strongly encourages depositing underlying data in a recognized repository.
- **Exact abstract word limit, manuscript length cap, and any open-access / APC fees are 待核实** — read them off the official submission guidelines at submission time.
- ORCID is recommended for submitting authors.

## Preflight checklist

### Manuscript & style
- [ ] Abstract within the journal's word limit (待核实 — verify cap); keywords and JEL codes included
- [ ] Title page with full affiliations; corresponding author and ORCID set
- [ ] References in the journal's style (Springer basic / numbered — 待核实); every in-text cite resolves
- [ ] Figures plot the key functions (w(p), value function) with the EU benchmark; tables report SE/CI, not bare asterisks
- [ ] Experiment instructions / decision screens included as supplementary material; estimand stated in the main text

### Files & disclosures for the Springer portal
- [ ] Main manuscript + supplementary appendix; experiment materials and code as supplementary files or repository link
- [ ] **Data Availability Statement** present and consistent with what is deposited
- [ ] **Ethics / IRB approval** stated for human-subjects experiments; consent noted
- [ ] **Competing-interests and funding** declarations complete
- [ ] **AI/LLM use** disclosed per Springer policy; AI not listed as an author
- [ ] Anonymization handled per the confirmed review model (待核实)

### Sibling-fit last look
- [ ] The paper's object is a risk/uncertainty primitive — not a method demo (Experimental Economics) or a broad-behavioral result (JEBO); the cover letter says why JRU

### Final consistency sweep
- [ ] Every number in the abstract matches the corresponding table to the last digit
- [ ] Notation in the text matches the notation in the figures and table notes
- [ ] All in-text citations appear in the reference list and vice versa
- [ ] Supplementary files referenced in the text are actually uploaded
- [ ] Author list, affiliations, and ORCIDs are final (changes after submission are friction)
- [ ] The paper does not assert a fact about the journal (limit, fee, policy) that is not verified — anything uncertain is left out, not guessed

## Cover letter for a specialist desk

The Editor-in-Chief screens for fit, so the cover letter does real work at JRU:

- **One sentence on the primitive.** Name the risk/uncertainty object the paper moves (a representation, an elicited parameter, a VSL, an insurance elasticity).
- **One sentence on why JRU, not a sibling.** Pre-empt the desk question: this is a risk/uncertainty contribution, not a method demo (Experimental Economics) or a broad behavioral result (JEBO).
- **Suggested and excluded reviewers** if the system allows — useful in a small specialized pool where conflicts and rival camps are real.
- **Prior-submission note** if the paper was previously reviewed elsewhere and substantially revised.

## What to expect after submission

- Single-blind specialist review (待核实) typically yields a few **deep** technical objections rather than many shallow ones; budget revision time for new analyses, not just edits.
- The binding decision usually turns on the decision-theoretic or measurement core, so an R&R will most often ask you to shore up the representation or the identification (`jru-theory-model` / `jru-identification`).

## Anti-patterns

- Uploading without a Data Availability Statement (required even when data are restricted)
- Reporting significance with asterisks instead of standard errors / confidence intervals
- Omitting experiment instructions — for an elicitation paper the procedure is part of the method
- Assuming a word/abstract limit or a fee instead of reading the live guidelines (mark 待核实)
- A cover letter that does not say why the paper is JRU and not a sibling venue

## Output format

```text
【Manuscript】abstract within cap (待核实) + keywords + JEL? [Y/N]
【Exhibits】functions plotted vs. EU benchmark; SE/CI not stars? [Y/N]
【Data Availability Statement】present + consistent with deposit? [Y/N]
【Ethics/IRB + funding + AI disclosure】complete? [Y/N]
【Experiment materials】instructions/screens/code supplied? [Y/N]
【Fit】cover letter argues JRU over Experimental Economics / JEBO? [Y/N]
【Next step】submit via Springer portal → jru-rebuttal for what to expect
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — submission self-check
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — lightweight manuscript scaffold
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official Springer URLs and volatile facts
