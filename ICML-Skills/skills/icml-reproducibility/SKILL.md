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

## Reproducibility scoring lens

ICML reviewers fold reproducibility into the soundness judgment rather than scoring it on a separate
axis, so the question is whether a skeptical reviewer could regenerate the headline number.

| Signal a reviewer checks | Strong evidence | Weak signal that invites doubt |
| --- | --- | --- |
| Code in review package | Anonymized, runnable, exact commands | "Code on acceptance" promise only |
| Variance | Seeds with intervals | Single run, no spread |
| Compute | Hardware and budget table | Unstated cost, unfair comparison |
| Theory | Assumptions and proof dependencies listed | Theorem with hidden conditions |

## Worked vignette: theory-plus-benchmark paper

For an adaptive-optimizer paper, reproducibility means the convergence proof's assumptions are
written out, the benchmark scripts run from the anonymized supplement with a fixed seed, and the
compute table lets a reviewer judge whether the speedup is real or a tuning artifact. The recurring
failure is a clean theorem paired with benchmark code that silently relies on an unreleased internal
dataset; document the access path or move to a public dataset before the deadline.

## Reviewer-pushback patterns and the ICML fix

| Pushback | ICML-specific fix |
| --- | --- |
| "Cannot reproduce without the code" | Ship the anonymized runnable package now, not a post-acceptance promise |
| "Hyperparameters undocumented" | Add the search protocol and final values to the appendix |
| "Speedup may be a seed artifact" | Report multiple seeds with confidence intervals |
| "Theorem assumptions hidden" | List assumptions, proof dependencies, and edge cases explicitly |

Because accepted ICML papers can publish the original supplementary material on OpenReview, the
reproducibility package is also a public commitment. Confirm before the deadline that every file is
releasable, every license is stated, and no private credential or identity path remains.

## Output format

```text
[Reproducibility status] strong / adequate / weak
[Weakest claim] <claim not yet supported>
[Required fix] <code/data/seed/compute/baseline/proof>
[Supplement/public-record risk] <none or issue>
[Reviewer-facing sentence] <concise reproducibility statement>
```

