---
name: red-workflow
description: Use when mapping the end-to-end lifecycle of a Review of Economic Dynamics (RED) manuscript — from confirming dynamic/quantitative scope, through the USD 175 fee and ScienceDirect/Editorial Manager submission, the single-anonymized two-referee review, the code-first data/code archive, to the revise-and-resubmit. Orchestration; it routes to the other red- skills rather than drafting content.
---

# RED Manuscript Workflow (red-workflow)

## When to trigger

- Starting a paper aimed at the **Review of Economic Dynamics** and wanting the full path
- Unsure which RED-specific step comes next or which sibling skill to open
- Sanity-checking that nothing RED-specific (fee, code archive, single-anonymized norms) is missed

## The lifecycle (RED-specific)

1. **Scope check** — Is the question dynamic and quantitative, studied through a dynamic model
   (theoretical, computational, or empirical)? RED's scope is defined by method/lens, not subfield. → `red-topic-selection`
2. **Position** — Place the paper in the dynamic-economics / SED literature. → `red-literature-positioning`
3. **Frame the contribution** — What is the marginal quantitative/dynamic advance? → `red-contribution-framing`
4. **Identification / model logic** — Assumptions and regularity conditions (theory), or causal
   design (empirical). → `red-identification-strategy`
5. **Analysis** — Calibration, moment-matching, estimation, numerical solution discipline. → `red-data-analysis`
6. **Exhibits** — IRFs, moment tables, model-vs-data figures. → `red-tables-figures`
7. **Write** — RED house style, author-year references, ≤250-word stand-alone abstract, 1–6 keywords. → `red-writing-style`
8. **Stage replication** — Build the data/code archive early; RED's policy is code-first. → `red-replication-and-data-policy`
9. **Understand review** — Desk screen, single-anonymized, ≥2 referees, ~two-month post-desk target. → `red-review-process`
10. **Submit** — Pay the USD 175 fee (USD 100 all-student), submit via ScienceDirect / Editorial Manager. → `red-submission`
11. **Revise** — Response-to-referees after an R&R; resubmissions are fee-exempt. → `red-rebuttal`

## Anti-patterns

- Treating RED like a generalist top-5 venue and ignoring its method-defined scope
- Forgetting the per-submission fee gates the review (no fee paid → no review)
- Leaving the replication archive to the accepted stage when the policy expects code-first discipline

## Router diagnostics

Ask these questions before choosing the next skill:

- Is the dynamic mechanism unclear? Use `red-topic-selection` or `red-contribution-framing`.
- Is the model disciplined by too few moments or free parameters? Use `red-data-analysis`.
- Are assumptions, existence, uniqueness, or accuracy weak? Use `red-identification-strategy`.
- Are exhibits static or uninformative about dynamics? Use `red-tables-figures`.
- Is the archive missing a run-all path, seeds, or runtime? Use `red-replication-and-data-policy`.

The right RED route is usually the step that makes the dynamic model more auditable.

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official RED URLs behind every fact
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — Dynare, Julia/SSJ, FRED and reproducibility tooling
