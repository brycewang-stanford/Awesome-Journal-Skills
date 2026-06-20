---
name: red-submission
description: Use when running the final pre-submission preflight for the Review of Economic Dynamics (RED) — the current Elsevier Guide's USD 195 fee (USD 100 all-student; waived on second-and-later resubmissions) that gates review, submission via ScienceDirect/Editorial Manager, the ≤250-word abstract, 1-6 keywords, author-year references, single-anonymized format, AI declaration, Option C data statement, and optional SSRN preprint. Final checks; it does not draft content.
---

# Submission Preflight for RED (red-submission)

## When to trigger

- "Submitting tomorrow" — last check before uploading to RED
- Confirming the fee, the submission route, and the required front matter
- Unsure whether to anonymize (you should not — RED is single-anonymized)

## RED submission facts (verified; re-confirm on official pages)

- **Fee gates review.** The current Elsevier Guide lists a **USD 195** standard submission fee; **USD
  100** if all coauthors are full-time students at submission; **no fee for papers being resubmitted a
  second or later time**. First invited resubmissions pay a new fee. **The review process does not begin
  until the fee is received.**
- **Route.** Submit via the journal's **ScienceDirect** page ("Submit your article"); the workflow runs
  through **Elsevier Editorial Manager**.
- **Do NOT anonymize.** RED uses **single-anonymized** review — author identity is visible to reviewers.
- **Abstract** ≤**250 words**, stand-alone, no internal references.
- **Keywords**: **1 to 6**.
- **References**: **author-year (Harvard)** style.
- **Generative AI**: declare any use at submission.
- **SSRN preprint**: RED offers **free SSRN preprint posting** during submission; the manuscript is made
  public once it passes the initial desk screen — opt in if you want early visibility.
- **Replication and data readiness**: stage the RED data/code archive now and prepare the Elsevier Option C
  data statement/repository metadata (see `red-replication-and-data-policy`). Flag any proprietary-data
  exemption to the Coordinating Editor at submission.

## Preflight checklist

- [ ] Fee path confirmed (USD 195 / USD 100 all-student / exempt second-or-later resubmission); ready to pay
- [ ] Submitting via ScienceDirect → Editorial Manager
- [ ] Manuscript **not** anonymized (single-anonymized model)
- [ ] Abstract ≤250 words, stand-alone; 1–6 keywords; author-year references
- [ ] Generative-AI declaration prepared
- [ ] Replication archive staged; Option C data statement/repository metadata prepared
- [ ] Proprietary-data exemption flagged if needed
- [ ] SSRN preprint opt-in decided

## Anti-patterns

- Anonymizing the manuscript for a single-anonymized journal
- Assuming review starts before the fee is paid
- Paying a fee on a second-round resubmission that is actually exempt

## Last-mile desk-risk scan

Run this scan after the mechanical preflight — it catches the substantive issues the fee cannot fix:

| Scan item | Pass condition |
|---|---|
| Dynamic-model centrality | the abstract names a model class and a mechanism, not just a dataset |
| Quantitative core complete | every exhibit final; no placeholder counterfactuals |
| Calibration auditable | a parameter table with sources/targets appears in the draft |
| Computation disclosed | solution method and an accuracy statement appear in text or appendix |
| Archive runnable today | run-all executes end to end before you pay the fee |

Paying USD 195 for a paper that will stall at the suitability screen is the most expensive formatting
error at this journal: the fee is per submission and the screen happens before referees see anything.

## Fee-path micro-decisions

- Mixed team (one student, one faculty): the USD 100 rate does not apply — **every** coauthor must be a
  full-time student at submission.
- Resubmission rounds: first invited resubmissions pay again; second-and-later resubmissions are exempt —
  confirm which round your revision counts as against Editorial Manager before paying again.
- Fee paid but desk-rejected: the fee is sunk; do not resubmit a cosmetic revision, since the same
  suitability screen applies.
- Source precedence: the SED author page still carries an older 175 US dollar amount, while the active Elsevier
  Guide/payment workflow lists USD 195; use the Guide amount for live preflight.

## Upload-order note

Stage files so Editorial Manager builds a clean review PDF: manuscript with embedded exhibits for the
first round (allowed under "your paper your way"), then appendices, then declarations. Check the
system-built PDF renders all model equations, IRF figures, and fonts before approving the submission —
a garbled Bellman equation at the desk screen is a self-inflicted wound.

## Output format

```
【Fee】USD 195 / 100 (all-student) / exempt (2nd+ resubmission)? [which]
【Route】ScienceDirect → Editorial Manager? [Y/N]
【Anonymization】left non-anonymized (single-anonymized)? [Y/N]
【Front matter】abstract ≤250w / 1-6 keywords / author-year refs? [Y/N each]
【Declarations】AI-use declared? [Y/N]
【Data/replication】archive staged; Option C statement/repository metadata prepared; exemption flagged if needed? [Y/N]
【Next step】await desk screen → red-review-process → red-rebuttal on R&R
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — fee, route, and front-matter sources
- [`red-replication-and-data-policy`](../red-replication-and-data-policy/SKILL.md) — the archive to stage before submitting
