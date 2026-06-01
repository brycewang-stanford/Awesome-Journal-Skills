---
name: neurips-reproducibility
description: Use when strengthening NeurIPS reproducibility evidence, checklist answers, code/data instructions, random-seed controls, compute disclosure, or deciding whether MLRC/TMLR is a better route.
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

## Output format

```text
[Reproducibility status] Strong / adequate / weak
[Claim at risk] <result that cannot yet be reproduced>
[Needed evidence] <code/data/seed/compute/ablation/error bars/license>
[Checklist changes] <items to revise>
[Route] Main track / MLRC-TMLR / other
```

