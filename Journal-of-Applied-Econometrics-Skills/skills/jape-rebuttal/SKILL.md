---
name: jape-rebuttal
description: Use when drafting the response letter for a Journal of Applied Econometrics (JAE) revise-and-resubmit — replying to single-blind anonymous referees and the Editor-in-Chief on applied-econometrics objections (identification on real data, inference, robustness) while keeping the JAE Data Archive package in sync with every revised result.
---

# Rebuttal for JAE (jape-rebuttal)

## When to trigger

- You have a JAE decision letter inviting a revision and are drafting the response
- Referees raise objections about identification, inference, or reproducibility
- You need to keep your archive-bound data/code consistent with the revised paper

## How to respond at JAE

JAE review is **single-blind**: referees are anonymous, you are not, and the **Editor-in-Chief** makes the final call. Address the Editor and each referee separately. Reproduce every comment verbatim, then reply with the **exact manuscript change** and, where the point is decision-critical, **new diagnostic evidence** (a robustness table, an alternative estimator, a placebo test). Do not thank the anonymous reviewers inside the manuscript acknowledgments (review is single-blind).

## Group the comments

- **Identification / estimand** — defend assumptions on real data, add tests rather than assert.
- **Inference** — if challenged on standard errors, show HAC/clustered/weak-IV-robust alternatives.
- **Robustness** — push expanded grids into the unlimited **online appendix** (the main text stays within 35 pages).
- **Reproducibility** — if a referee cannot regenerate a number, fix the code and say so.

## Keep the archive in sync

Because every reported result must be regeneratable from the eventual **JAE Data Archive** deposit (plain ASCII/CSV + readme + programs), update the master script and exported text outputs alongside the revised tables. A response that changes numbers but not the underlying code creates an archive mismatch that surfaces at acceptance.

## Anti-patterns

- Arguing identification verbally instead of adding a test
- Letting revised tables and the replication package drift apart
- Bloating the 35-page main text with new robustness instead of using the appendix
- Treating a reject as a resubmission opportunity without an Editor's invitation

## Output format

```
【Per-referee】each comment quoted + concrete change? [Y/N]
【New evidence】decision-critical tests added (not asserted)? [Y/N]
【Appendix】expanded robustness to online appendix? [Y/N]
【Archive sync】code/data updated to match revised results? [Y/N]
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — single-blind / EiC and Data Archive sources
