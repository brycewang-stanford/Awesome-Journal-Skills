---
name: red-submission
description: Use when running the final pre-submission preflight for the Review of Economic Dynamics (RED) — the USD 175 fee (USD 100 all-student; waived on second-and-later resubmissions) that gates review, submission via the ScienceDirect page through Elsevier Editorial Manager, the ≤250-word abstract, 1-6 keywords, author-year references, single-anonymized (no anonymization) format, AI declaration, and optional SSRN preprint. Final checks; it does not draft content.
---

# Submission Preflight for RED (red-submission)

## When to trigger

- "Submitting tomorrow" — last check before uploading to RED
- Confirming the fee, the submission route, and the required front matter
- Unsure whether to anonymize (you should not — RED is single-anonymized)

## RED submission facts (verified; re-confirm on official pages)

- **Fee gates review.** A **USD 175** submission fee is standard; **USD 100** if all coauthors are
  full-time students at submission; **no fee for papers being resubmitted a second or later time**
  (post-first-round revisions are exempt). **The review process does not begin until the fee is received.**
- **Route.** Submit via the journal's **ScienceDirect** page ("Submit your article"); the workflow runs
  through **Elsevier Editorial Manager**.
- **Do NOT anonymize.** RED uses **single-anonymized** review — author identity is visible to reviewers.
- **Abstract** ≤**250 words**, stand-alone, no internal references.
- **Keywords**: **1 to 6**.
- **References**: **author-year (Harvard)** style.
- **Generative AI**: declare any use at submission.
- **SSRN preprint**: RED offers **free SSRN preprint posting** during submission; the manuscript is made
  public once it passes the initial desk screen — opt in if you want early visibility.
- **Replication readiness**: stage the data/code archive now (see `red-replication-and-data-policy`); a fast
  acceptance should not stall on a missing archive. Flag any proprietary-data exemption to the Coordinating
  Editor at submission.

## Preflight checklist

- [ ] Fee path confirmed (USD 175 / USD 100 all-student / exempt resubmission); ready to pay
- [ ] Submitting via ScienceDirect → Editorial Manager
- [ ] Manuscript **not** anonymized (single-anonymized model)
- [ ] Abstract ≤250 words, stand-alone; 1–6 keywords; author-year references
- [ ] Generative-AI declaration prepared
- [ ] Replication archive staged; proprietary-data exemption flagged if needed
- [ ] SSRN preprint opt-in decided

## Anti-patterns

- Anonymizing the manuscript for a single-anonymized journal
- Assuming review starts before the fee is paid
- Paying a fee on a second-round resubmission that is actually exempt

## Output format

```
【Fee】USD 175 / 100 (all-student) / exempt (2nd+ resubmission)? [which]
【Route】ScienceDirect → Editorial Manager? [Y/N]
【Anonymization】left non-anonymized (single-anonymized)? [Y/N]
【Front matter】abstract ≤250w / 1-6 keywords / author-year refs? [Y/N each]
【Declarations】AI-use declared? [Y/N]
【Replication】archive staged; exemption flagged if needed? [Y/N]
【Next step】await desk screen → red-review-process → red-rebuttal on R&R
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — fee, route, and front-matter sources
- [`red-replication-and-data-policy`](../red-replication-and-data-policy/SKILL.md) — the archive to stage before submitting
