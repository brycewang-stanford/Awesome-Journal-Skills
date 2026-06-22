---
name: jle-submission
description: Use when running the final pre-submission preflight for a The Journal of Law and Economics (JLE) manuscript via the Editorial Manager portal — the single-blind title page, the US$100 submission fee, Chicago author-date style, the replication-policy readiness, and disclosures. Final checks; it does not draft content.
---

# Submission Preflight (jle-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on JLE's Editorial Manager site
- Unsure which files, fee, and declarations the JLE submission expects
- Confirming the single-blind front matter (title page with author names) is right — not anonymized
- Confirming the paper is replication-policy-ready should it advance

## Process facts (检索于 2026-06-22；以官网为准 — re-confirm on journals.uchicago.edu/journals/jle)

- JLE is published by the **University of Chicago Press** in association with the University of Chicago Law School; it is the founding journal of law and economics (since 1958). Submission is through the **JLE Editorial Manager** site.
- **Single-blind review:** authors' identities are visible to referees; referees are anonymous. **Do not anonymize the manuscript.** Include a **title page with each author's name and contact information.**
- **Submission fee:** **US$100**, required for all manuscripts **beginning May 1, 2026**; **editorial review does not proceed until the fee is paid**; the fee is **non-refundable** (re-verified 2026-06-22, ≥2 sources; 以官网为准).
- **Editors (re-verified 2026-06-22):** Elliott Ash, Matthew Backus, Dennis W. Carlton, Dhammika Dharmapala, Thomas J. Miles, Sam Peltzman (re-verify the masthead before submission).
- **Citation style:** Chicago author-date (University of Chicago Press house style).
- **Data & replication:** the JLE data policy requires data, programs, and computation details **available for replication before publication**; you need not deposit at submission, but the paper must be buildable into a replication package (`jle-replication-package`).
- **Length / abstract limits, exact format specifics:** **待核实** — confirm current limits on the instructions-for-authors page before submitting.

## Preflight checklist

### Front matter (single-blind)
- [ ] **Title page** with every author's name, affiliation, and contact — manuscript **not** anonymized
- [ ] Abstract and keywords per the instructions page (exact abstract limit **待核实**)
- [ ] JEL codes if requested; acknowledgments and funding included

### Format & style
- [ ] **Chicago author-date** citations and reference list, consistent throughout
- [ ] Tables and figures legible with **standard errors and clustering level** reported; notes self-contained
- [ ] Appendix / online appendix prepared and separated from the main paper
- [ ] Manuscript length within the journal's current limit (**待核实**); pages numbered

### Files, fee & policy readiness
- [ ] Manuscript and exhibits uploaded as the Editorial Manager site requires
- [ ] **US$100 submission fee** ready to pay (non-refundable; review will not start until paid)
- [ ] Replication package buildable; data-availability statement drafted
- [ ] Restricted/sealed legal data: access path documented; synthetic extract planned

### Declarations
- [ ] Disclosure of funding and interested-party relationships
- [ ] Confirmed not under review elsewhere; AI not listed as an author

## What JLE does NOT require (so you don't import a sibling's rules)

Authors coming from AEA or Econometric Society journals often over-prepare in the wrong direction. At JLE:

- **No manuscript anonymization.** Unlike AEJ (double-blind) or QE, JLE is single-blind — leave your name on the title page.
- **No society-membership gate.** Unlike Quantitative Economics (Econometric Society membership) you need not be a member to submit.
- **No openICPSR pre-acceptance pipeline.** Unlike AEA journals, JLE does not run a Data-Editor reproducibility verification through openICPSR; its requirement is documentation and availability for replication before publication — important, but a different process.
- **No CC-BY open-access mandate by default.** JLE is a subscription journal with an optional open-access route; do not assume an APC unless you opt in (检索于 2026-06；以官网为准).

Confirm each against the current instructions page rather than carrying a habit from another journal.

## Anti-patterns

- **Anonymizing the manuscript** — JLE is single-blind; the title page must carry author names
- Submitting before paying the **US$100 fee** (editorial review will not begin)
- Assuming the fee is refundable, or assuming exact length/abstract limits from memory instead of re-confirming (**待核实**)
- Non-Chicago citation style, or exhibits missing standard errors / clustering level
- Treating the replication policy as irrelevant at submission, then scrambling before publication

## Worked vignette (illustrative)

An author about to submit a tort-reform paper runs the preflight and catches three things a JLE desk would flag. First, the manuscript had been anonymized out of habit — wrong for single-blind JLE; the author restores the title page with names and contact. Second, references were in a numbered style; the author converts to **Chicago author-date**. Third, the **US$100 fee** (effective May 1, 2026) was not budgeted; the author confirms payment is ready, since editorial review will not begin until it is paid. The replication package is buildable and the data-availability statement drafted. The exact abstract word limit was not visible on the cached instructions page, so the author marks it **待核实** and re-checks the live page before pressing submit.

## Output format

```
【Front matter】title page named (NOT anonymized) + abstract/keywords? [Y/N]
【Style】Chicago author-date; SEs + clustering in exhibits? [Y/N]
【Length/abstract limits】confirmed on instructions page? [Y/N — else 待核实]
【Fee】US$100 ready to pay (non-refundable)? [Y/N]
【Replication readiness】package buildable + DAS drafted? [Y/N]
【Declarations】disclosure done; not under review elsewhere; no AI author? [Y/N]
【Next step】submit via Editorial Manager → jle-rebuttal after the decision
```

## Last-mile sanity pass

Right before pressing submit, confirm the four items most likely to trigger an avoidable delay: the **title page is present and names every author** (single-blind), the **US$100 fee is queued** (review will not start otherwise), the **references are in Chicago author-date**, and every **exhibit reports SEs with the clustering level**. Then re-open the live instructions page once more to re-verify anything marked 待核实 — limits and fee mechanics are the volatile fields.

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — pre-submission self-check
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — lightweight manuscript scaffold
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official UChicago Press / JLE URLs behind every fact
```
