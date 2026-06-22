---
name: ier-submission
description: Use when running the final pre-submission preflight for an International Economic Review (IER) manuscript via the Editorial Express portal — the submission fee gate, the ≤50-page limit, format and style, proprietary-data notification, and the AER data policy. Final checks; it does not draft content.
---

# Submission Preflight (ier-submission)

## When to trigger

- "Submitting tomorrow" — last check before uploading to the IER portal
- Unsure which files, fee, and format the IER submission expects
- Confirming the manuscript is within the page limit and conforms to house style
- Deciding whether proprietary data require notifying the Editor now (it does — at submission)

## Process facts (检索于 2026-06；editor + US$150 fee re-verified 2026-06-22；以官网为准)

- IER is owned by the **University of Pennsylvania Department of Economics** and **Osaka University's Institute of Social and Economic Research (ISER)**, published with Wiley; founded **1960** as a forum for modern quantitative economics. It appears **five times a year** (Feb, May, Aug, Oct, Dec). Editor (re-verified 2026-06-22): **Dirk Krueger** (Penn); Co-editor **Masaki Aoyagi** (Osaka, ISER) — re-verify before naming in a cover letter.
- **Portal:** submission is through **Editorial Express** (editorialexpress.com/ier) — *not* ScholarOne/Manuscript Central. Verify the live link before submitting.
- **Submission fee:** **US$150 (or ¥15,000)**, payable at submission. **The manuscript is not reviewed until the fee is received.** No student waiver is stated on the page (待核实).
- **Length:** **not more than 50 pages**, single-sided, **double-spaced**. Manuscripts must conform to the style guidelines (available on request from the editorial office).
- **Copyright:** assignment to the University of Pennsylvania and Osaka University is a publication condition.
- **Data policy:** the **AER data availability policy (effective Jan 1, 2022)** applies; deposit is post-acceptance, but **proprietary or restricted data must be flagged to the Editor at the time of submission**.
- **Peer review model, exact abstract limit, and reference style** are **待核实** — confirm in the style guidelines / official pages before relying on them.
- **Open Access** is optional at acceptance with an article processing charge (Wiley lists it around US$3,570 / £2,330 / €3,010; verify the current amount — 检索于 2026-06；以官网为准). This APC is *separate* from and additional to the US$150 submission fee; do not conflate them.

### The two-cost structure that trips up first-time submitters

IER has an unusual cost profile worth flagging to the user up front: a **submission fee** of US$150 paid at submission (and the paper is genuinely not reviewed until it clears — this is a hard gate, not a formality), and a **separate, optional Open-Access APC** of several thousand dollars only if the author chooses OA at acceptance. Non-OA publication does not incur the APC. Many authors confuse the two; the submission fee is small and mandatory, the APC is large and optional. Budget and plan for the right one.

## Preflight checklist

### Format & length
- [ ] Manuscript **≤50 pages**, **double-spaced**, single-sided
- [ ] Conforms to the IER style guidelines (request from the editorial office if not held); reference style consistent (待核实 for exact format)
- [ ] Figures and tables legible, self-contained notes, **no significance asterisks** (SEs/confidence sets instead)
- [ ] Abstract present (exact word limit 待核实); title page with affiliations and JEL/keywords
- [ ] Online/supplemental appendix carries long proofs and secondary exhibits so the main text fits the ceiling

### Files & fee for Editorial Express
- [ ] Main manuscript PDF; supplementary/online appendix as a separate file
- [ ] **Submission fee (US$150 / ¥15,000) ready** — manuscript is not reviewed until paid
- [ ] Confirmed the live portal link (editorialexpress.com/ier) before uploading

### Declarations & policy
- [ ] **Proprietary/restricted data flagged to the Editor at submission** (AER-policy requirement)
- [ ] Replication deposit plan ready for conditional acceptance (README PDF, repository, data availability statement) — see `ier-replication-package`
- [ ] Confirmed the paper is not under review elsewhere; AI not listed as an author
- [ ] Cover letter makes the general-interest case and draws the sibling boundary (from `ier-referee-strategy`)

### Fitting the contribution into 50 double-spaced pages

The ≤50-page, double-spaced ceiling is tighter than it looks — double spacing roughly halves the words per page relative to a single-spaced working-paper draft. Authors used to long working papers routinely arrive over the limit. The disciplined fix, decided before the final preflight, is a clean main-text / online-appendix split: the main text carries the model, the headline results, the one or two decisive robustness checks, and the key exhibits; the online appendix carries long proofs, secondary derivations, additional robustness, and overflow tables. Plan this split during `ier-writing-style` and `ier-tables-figures`, not at the submission deadline, so the main text reads as a complete, self-contained argument within the ceiling.

### Portal and format confirmation before upload

Because IER uses Editorial Express rather than the ScholarOne/Manuscript Central system most economists default to, confirm the live portal URL and the exact upload format it expects before the deadline. Verify the current style-guideline requirements (request them from the editorial office if you do not hold them), since exact abstract length and reference format are 待核实 and can change. A last-minute discovery that the portal or format differs from expectation is an avoidable delay on a paper that is otherwise ready.

## Anti-patterns

- Uploading and assuming review starts — at IER **nothing happens until the $150 fee clears**
- Submitting over the 50-page limit, or single-spaced
- Significance asterisks or figures/tables that need the body text to be read
- Discovering proprietary-data restrictions at acceptance instead of flagging them at submission
- Looking for a ScholarOne portal — IER uses Editorial Express
- Treating the Open-Access APC (if chosen at acceptance) as if it were the submission fee

### Last-mile sequence on submission day

1. Confirm the live Editorial Express link and the format it expects.
2. Verify the manuscript is ≤50 pages double-spaced; if over, move overflow to the online appendix now, not after.
3. Strip any significance asterisks; confirm exhibit notes are self-contained.
4. Have payment ready for the US$150 / ¥15,000 fee — and remember review does not start until it clears.
5. If any data are proprietary/restricted, ensure the cover note to the Editor flags it at this submission.
6. Attach the cover letter that makes the general-interest case (from `ier-referee-strategy`).

Run this list once more right before pressing submit; the fee gate and the page ceiling are the two items that most often delay an otherwise-ready paper.

## Output format

```text
【Journal】International Economic Review
【Skill】ier-submission
【Length】≤50 pages, double-spaced? [Y/N]
【Style】house-guidelines conformant; no significance asterisks? [Y/N]
【Portal】Editorial Express link confirmed? [Y/N]
【Fee】US$150 / ¥15,000 ready (review starts only after payment)? [Y/N]
【Proprietary data】flagged to Editor at submission if applicable? [Y/N]
【Deposit plan】AER-policy README/repository plan ready for acceptance? [Y/N]
【Cover letter】general-interest case + sibling boundary? [Y/N]
【Next step】submit via Editorial Express → ier-rebuttal after the decision
```
