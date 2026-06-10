---
name: neurips-reproducibility
description: Use when strengthening NeurIPS reproducibility evidence, aligning Paper Checklist answers with the paper, writing code/data instructions, setting random-seed and compute disclosure, or deciding whether the MLRC/TMLR reproducibility route fits better than the main track or Datasets & Benchmarks track.
---

# NeurIPS Reproducibility

Use this skill when a NeurIPS paper's claim depends on experiments, data, code, or a reproducibility
argument. The immediate target is a trustworthy main-track paper; the alternative route is MLRC/TMLR
when the central contribution is reproduction, replication, or generalizability of prior claims.

## Main-track reproducibility bar

- State exact data splits, preprocessing, hyperparameters, selection criteria, compute resources,
  software versions, and random-seed protocol.
- Report uncertainty where it matters: confidence intervals, standard errors, multiple seeds,
  sensitivity checks, or negative findings.
- Distinguish exploratory experiments from evidence that supports the main claim.
- Make code/data availability match the checklist answer; "no" is allowed with justification, but a
  central open-source benchmark or dataset usually needs accessible artifacts.
- For human, private, medical, proprietary, or safety-sensitive data, document access constraints
  and ethical controls rather than pretending full release is possible.

## MLRC route check

Consider the NeurIPS Reproducibility / MLRC track when the paper is primarily about confirming,
partially reproducing, failing to reproduce, or extending a published ML result. The 2026 MLRC route
requires TMLR review/acceptance before NeurIPS presentation consideration; this is not a shortcut
for ordinary main-track submissions.

## Checklist-to-evidence cross-check

A "yes" on the NeurIPS Paper Checklist with nothing in the paper to back it is exactly what reviewers
hunt for. Run this cross-check so each reproducibility answer is honest and locatable; hedge the exact
item wording to the current year's checklist.

| Checklist answer | Evidence that must exist | Failure pattern reviewers flag |
| --- | --- | --- |
| Code released: yes | anonymous link plus run commands during review | "yes" with no commands or a dead link |
| Data released: yes | accessible split, license, and loading code | central benchmark claimed open but not provided |
| Seeds/protocol reported | seed count and aggregation rule in the text | a single run reported as if deterministic |
| Compute reported | hardware, wall-clock, and total resource budget | omitted cost behind a "trained until converged" |
| Error bars reported | intervals or std over runs on headline metrics | bold-best numbers with no variance |

A justified "no" beats an unsupported "yes". If full release is blocked by privacy, licensing, or
safety, say so and document what reviewers can still verify.

## Reviewer-pushback patterns

| Reviewer concern | NeurIPS-specific fix |
| --- | --- |
| "Results may be a lucky seed" | report multiple seeds with variance, not a single point |
| "Cannot rerun your pipeline" | ship exact env, configs, and a one-command entry point in the ZIP |
| "Compute claims are unfair" | disclose budget and tune baselines under the same budget |
| "Dataset access unclear" | give license, hosting, and access steps, anonymized for review |

## Worked vignette: a scaling-law claim

A paper claims a clean scaling law but reports one training run per model size with no intervals.
Reviewers cannot tell signal from seed noise. The fix before submission: add at least a few seeds at
the smaller sizes, plot variance bands, disclose the GPU-hours budget, and set the code-released and
error-bars checklist answers to a "yes" that the appendix actually supports. If the contribution were
instead reproducing someone else's published scaling law, the MLRC/TMLR route, not the main track,
would be the correct home.

## Output format

```text
[Reproducibility status] Strong / adequate / weak
[Claim at risk] <result that cannot yet be reproduced>
[Needed evidence] <code/data/seed/compute/ablation/error bars/license>
[Checklist changes] <items to revise>
[Route] Main track / MLRC-TMLR / other
```

