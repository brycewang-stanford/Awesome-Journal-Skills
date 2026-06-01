---
name: ectj-data-analysis
description: Use when designing or auditing EctJ Monte Carlo simulations, empirical applications, estimator comparisons, robustness checks, computation, seeds, and applied-value evidence.
---

# EctJ Data Analysis

Use this when the method has to prove both statistical behavior and empirical usefulness.

## Analysis checks

- Keep Monte Carlo evidence focused. RES guidance asks that simulation results be summarized
  compactly in the main text; use the supplement for details.
- Include an empirical application that demonstrates applied value, even for theory-heavy
  work.
- Align simulations with the assumptions and failure modes from the theory section.
- Compare against credible econometric alternatives, not only simplified baselines.
- Report sample sizes, data-generating processes, tuning, seeds, software versions, runtime,
  and convergence or failure diagnostics.
- Show where the new procedure changes an applied conclusion, uncertainty interval, test
  decision, or policy-relevant estimate.

## Output format

```text
[Evidence readiness] strong / adequate / weak
[Monte Carlo role] <theory validation or stress test>
[Empirical application role] <applied-value demonstration>
[Missing baseline or diagnostic] <item>
[Next analysis] <single run or table>
```
