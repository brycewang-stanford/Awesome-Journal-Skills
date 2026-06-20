---
name: jhe-submission
description: Use when running the final pre-submission preflight for a Journal of Health Economics (JHE) manuscript via Elsevier Editorial Manager — single-anonymized review, keywords, declarations, data-availability statement, and the no-length-limit/short-paper allowance. Final checks; it does not draft content.
---

# Submission Preflight (jhe-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit in Editorial Manager
- Unsure which files, declarations, and statements the Elsevier submission expects
- Confirming format, keywords, and the Data Availability Statement are JHE-compliant
- Confirming the manuscript matches JHE's single-anonymized review (do NOT over-anonymize as for AEA double-blind)

## Process facts (检索于 2026-06；以官网为准 — re-confirm on the JHE guide for authors)

- JHE is Elsevier's field flagship for health economics (ISSN 0167-6296); submission is via **Elsevier Editorial Manager** (editorialmanager.com/jhlthec).
- **Review model: single-anonymized** — referees see author identities; suitable papers go to **≥2 reviewers**. There is no double-blind anonymization requirement, so stripping the manuscript of names is unnecessary (and removing acknowledgments/self-citations is not a desk requirement here).
- **Length:** JHE publishes **papers of any length and encourages short papers** — there is no separate short-paper channel. Match length to content; do not pad.
- **Keywords:** provide **1–7 keywords** in English.
- **Data & code:** Elsevier **Research Data** policy — authors are **encouraged** (not mandated) to deposit data and to **state data availability at submission** via a Data Availability Statement. This is softer than the AEA mandatory openICPSR gate; honest documentation is the standard (see `jhe-replication-package`).
- **Declarations:** Declaration of Competing Interest, funding sources, and a Declaration of Generative AI in the writing process per Elsevier policy; **AI cannot be an author**. One paper under review at a time.
- **Volatile / 待核实:** exact abstract word limit, JEL-code requirement, current editorial board, APC for the open-access option, and any structured-abstract or highlights requirement — re-check the live guide for authors before submitting.

## Preflight checklist

### Format & front matter
- [ ] Manuscript in an accepted format (Word/LaTeX per Elsevier); pages numbered; sections clearly headed
- [ ] **1–7 English keywords** supplied; abstract within the journal's limit (待核实)
- [ ] JEL codes included if required (待核实); affiliations and corresponding-author details complete
- [ ] **Not over-anonymized** — single-anonymized review means author info is expected on the title page
- [ ] References in the journal's house citation style (Elsevier author-date; re-check the guide)

### Exhibits & appendix
- [ ] Tables/figures legible; **standard errors reported** with clustering stated (stars optional)
- [ ] Skewed-spending estimator and outcome definitions stated in notes
- [ ] Online/supplementary appendix prepared and separate from the main paper

### Data, declarations & policy readiness
- [ ] **Data Availability Statement** drafted: names data, holder, access mechanism, realistic path/cost/wait
- [ ] Code package ready to share even if data is restricted (`jhe-replication-package`)
- [ ] Declaration of Competing Interest + funding statement complete
- [ ] Declaration of Generative AI in writing prepared per Elsevier policy; no AI listed as author
- [ ] Confirmed not under review elsewhere; ethics/IRB statement included where human-subjects or restricted health data is used
- [ ] Cover letter states the health-economics contribution and the target audience within JHE's scope

## How JHE submission differs from the AEA journals (do not import the wrong reflexes)

If your last submission was to AEJ: Applied, AER, or another AEA outlet, several habits will mislead you here:

- **Anonymization:** AEA review is double-blind and demands a fully blinded file; **JHE is single-anonymized** — keep the title page with author details and do not scrub acknowledgments or self-citations.
- **Data/code:** the AEA mandates an openICPSR package the Data Editor verifies before publication; **JHE only encourages deposit** and asks for a Data Availability Statement — so the burden shifts from a forced build to honest documentation of a (often restricted) access path.
- **Length:** AEA outlets have working length norms; **JHE explicitly takes any length and encourages short papers**, so a tight result need not be inflated.
- **Stars:** AEA permits significance stars; JHE/Elsevier also permits them, but SEs and clustering remain the load-bearing reporting object either way.

## Anti-patterns

- Over-anonymizing for double-blind when JHE is single-anonymized (wasted effort, signals wrong target)
- Padding a clean short paper to look like a full-length article when JHE encourages short papers
- Submitting with "data available on request" instead of a specific Data Availability Statement
- Omitting standard errors / clustering from exhibits, or notes that are not self-contained
- Assuming the abstract limit, JEL requirement, or APC from memory instead of re-checking the live guide
- Forgetting the Declaration of Generative AI or the competing-interest statement
- Submitting while the same manuscript is under review at another journal (one-at-a-time rule)

## Output format

```
【Portal】Editorial Manager (editorialmanager.com/jhlthec) ready? [Y/N]
【Review model】single-anonymized — NOT over-anonymized? [Y/N]
【Front matter】1–7 keywords + abstract (limit 待核实) + JEL if required? [Y/N]
【Exhibits】SEs + clustering shown, notes self-contained? [Y/N]
【Data Availability Statement】specific (data/holder/mechanism/path)? [Y/N]
【Declarations】competing interest + funding + GenAI; no AI author? [Y/N]
【Next step】submit via Editorial Manager → jhe-rebuttal after the decision
```

## After you press submit

Editorial Manager will route the manuscript to a handling editor who decides whether it goes to review; suitable papers go to ≥2 health-economist referees (检索于 2026-06；以官网为准). There is no double-blind step to clear, so a desk decision turns on **fit and credibility**, not anonymization mechanics — which is why the upstream work (`jhe-topic-selection` for fit, `jhe-identification` for design) does the heavy lifting. Keep the response-letter machinery (`jhe-rebuttal`) ready; if the decision is an R&R, you will re-enter the pack at the owning skill for each binding concern before resubmitting here.

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — pre-submission self-check
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — lightweight manuscript scaffold
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official URLs and volatile facts

## Handoff boundary

This is the final preflight; it checks the package is complete and policy-compliant, not whether the science is ready — that is the upstream specialists' job. If the preflight surfaces a substantive gap (a missing identification defense, an overclaimed welfare statement), do not submit: route back to the owning skill first. After submission, the next stop is `jhe-rebuttal` when the decision letter arrives.
