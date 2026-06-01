---
name: icml-reproducibility
description: Use when strengthening ICML reproducibility evidence, including code/data availability, random seeds, compute disclosure, appendix evidence, impact-statement support, and reviewer-facing reproducibility claims.
---

# ICML Reproducibility

Use this when the paper's acceptance risk is tied to whether experiments, code, or theory can be
trusted. ICML reviewers are asked to evaluate soundness, and ICML author instructions state that
reproducibility and code availability are considered in decisions.

## Evidence checklist

- Data: source, license, preprocessing, splits, leakage checks, and access restrictions.
- Code: anonymous review package, environment, dependencies, exact commands, and expected runtime.
- Randomness: seeds, variance, confidence intervals, or explanation for deterministic runs.
- Compute: hardware, training budget, evaluation budget, and fairness relative to baselines.
- Baselines: tuning protocol, implementation source, and why missing baselines are not applicable.
- Theory: assumptions, theorem statements, proof dependencies, and edge cases.
- Impact: support claims in the impact statement with real evidence or narrow the statement.

## ICML-specific public-record issue

Accepted papers may publish original supplementary material. Do not put unreleasable data, identity
leaks, or private credentials in the review package. If data cannot be public, document the access
path and ethics constraints in the paper.

## Output format

```text
[Reproducibility status] strong / adequate / weak
[Weakest claim] <claim not yet supported>
[Required fix] <code/data/seed/compute/baseline/proof>
[Supplement/public-record risk] <none or issue>
[Reviewer-facing sentence] <concise reproducibility statement>
```

