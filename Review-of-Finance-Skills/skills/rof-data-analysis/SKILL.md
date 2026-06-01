---
name: rof-data-analysis
description: Use when auditing Review of Finance empirical or theoretical analysis: sample construction, identification, asset-pricing tests, corporate-finance variables, robustness, code reproducibility, and evidence that can satisfy top-three-finance-journal standards.
---

# Review of Finance Data Analysis

Use this when the finance result is not yet credible enough for RoF. Reopen the current
author guidelines and code-sharing policy before final submission.

## Audit

- Map every finance claim to a table, figure, model result, identification test, or
  robustness check.
- For empirical work, document sample construction, variable definitions, filters, winsorizing
  or trimming, identifiers, timing, and economic magnitudes.
- For theory work, connect assumptions to equilibrium, comparative statics, or pricing
  implications that a broad finance audience can evaluate.
- Use strong benchmarks: standard asset-pricing factors, corporate-finance controls, market
  microstructure alternatives, or banking/household-finance baselines as relevant.
- Prepare code and data documentation early; RoF publication is conditional on receiving
  replication programs when the policy applies.

## Output format

```text
[Analysis readiness] strong / adequate / weak
[Claim -> evidence] <claim: table, figure, model, or robustness>
[Top-three-standard gap] <one issue>
[Replication blocker] <data, code, pseudo-data, or logs>
[Next analysis] <single task>
```
