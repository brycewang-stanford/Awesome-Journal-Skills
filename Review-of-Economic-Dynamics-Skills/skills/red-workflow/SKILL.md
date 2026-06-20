---
name: red-workflow
description: Use when mapping the end-to-end lifecycle of a Review of Economic Dynamics (RED) manuscript — from confirming dynamic/quantitative scope, through the current Elsevier Guide's USD 195 fee and ScienceDirect/Editorial Manager submission, the single-anonymized two-reviewer process, the code-first data/code archive plus Option C data statement, to the revise-and-resubmit. Orchestration; it routes to the other red- skills rather than drafting content.
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
9. **Understand review** — Desk screen, single-anonymized, ≥2 reviewers when sent out; plan around fast-review norms without assuming a guaranteed decision date. → `red-review-process`
10. **Submit** — Pay the USD 195 fee (USD 100 all-student), submit via ScienceDirect / Editorial Manager. → `red-submission`
11. **Revise** — Response-to-referees after an R&R; resubmissions are fee-exempt. → `red-rebuttal`

## Anti-patterns

- Treating RED like a generalist top-5 venue and ignoring its method-defined scope
- Forgetting the per-submission fee gates the review (no fee paid → no review)
- Leaving the replication archive or Option C data statement to the accepted stage when the policy expects code-first discipline

## Router diagnostics

Ask these questions before choosing the next skill:

- Is the dynamic mechanism unclear? Use `red-topic-selection` or `red-contribution-framing`.
- Is the model disciplined by too few moments or free parameters? Use `red-data-analysis`.
- Are assumptions, existence, uniqueness, or accuracy weak? Use `red-identification-strategy`.
- Are exhibits static or uninformative about dynamics? Use `red-tables-figures`.
- Is the archive missing a run-all path, seeds, or runtime? Use `red-replication-and-data-policy`.

The right RED route is usually the step that makes the dynamic model more auditable.

## Stage-gate tracker

Keep one block per project and tick gates as they clear:

```text
RED PIPELINE — [paper short title]
  G1 scope:        dynamic mechanism named; model class chosen          [date/✓]
  G2 positioning:  lineage map written; closest model identified        [ ]
  G3 discipline:   calibration table complete; every target sourced     [ ]
  G4 computation:  solver chosen; accuracy check passing                [ ]
  G5 exhibits:     mechanism figure + fit table drafted                 [ ]
  G6 archive:      run-all reproduces exhibits; readme.txt drafted      [ ]
  G7 manuscript:   abstract ≤250w; author-year refs; 1–6 keywords       [ ]
  G8 submission:   fee path decided; ScienceDirect upload checked       [ ]
  G9 review:       desk cleared; reviewer-clock expectations logged     [ ]
  G10 revision:    point-by-point reply; archive re-run and re-sent     [ ]
```

Gates G3–G6 are where RED differs most from a generalist target: they exist because SED-community
referees re-derive calibrations and sometimes re-execute code.

## Sequencing rules specific to RED

- Build the archive (G6) **in parallel with** the analysis, not after acceptance — the data/code policy
  bites before final acceptance, and retrofitting seeds and execution order into months-old solver code
  is the classic schedule killer for simulation-heavy papers.
- Do not draft the introduction before G2 and G3 exist; an intro written without a lineage map and a
  calibration table tends to over-claim and gets rewritten after the moments come in.
- Budget compute as a project resource: a global-solution model whose counterfactual takes days to run
  limits how many referee experiments a two-round revision can absorb.

## Failure-mode router

| Observed failure | Gate | Skill |
|---|---|---|
| Headline number moves when the grid is refined | G4 | `red-identification-strategy` |
| Untargeted moments badly missed | G3 | `red-data-analysis` |
| Reader cannot restate the mechanism after the intro | G1/G2 | `red-contribution-framing` |
| Archive fails a clean-machine rerun | G6 | `red-replication-and-data-policy` |

## Output format

```text
[Current stage] idea / model / calibration / estimation / writing / submission / review / R&R
[Dynamic bottleneck] scope / mechanism / calibration / computation / archive / response
[Next RED skill] <red-* skill>
[Hard blocker] <fee, archive, model credibility, review risk, or none>
[Next action] <single concrete task>
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official RED URLs behind every fact
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — Dynare, Julia/SSJ, FRED and reproducibility tooling
