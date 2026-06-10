---
name: ectj-data-analysis
description: Use when designing or auditing The Econometrics Journal (EctJ) Monte Carlo simulations, empirical applications, estimator comparisons, robustness checks, computation, seeds, and applied-value evidence.
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

## Minimum evidence map

Before drafting results, create a one-page map with these rows:

- **Theory target**: theorem, proposition, approximation, or diagnostic the simulation is meant to stress.
- **DGP grid**: the smallest parameter grid that probes the boundary cases, not every imaginable design.
- **Competitors**: incumbent estimator/test plus at least one strong practical alternative.
- **Failure diagnostics**: convergence failures, non-positive matrices, weak identification, bandwidth/tuning
  sensitivity, or coverage breakdowns.
- **Application payoff**: the single empirical decision that changes because the method exists.

The main text should report only the rows that teach the reader why the method works and when it fails.
Full grids belong in the supplement or replication package.

## Reproducibility ledger

Track every reported number in a ledger:

| Manuscript item | Script | Seed/config | Output path | Runtime |
|---|---|---|---|---|
| Table/Figure X | ... | ... | ... | ... |

Use the ledger to decide what must be in the main replication path and what can remain optional.

## Output format

```text
[Evidence readiness] strong / adequate / weak
[Monte Carlo role] <theory validation or stress test>
[Empirical application role] <applied-value demonstration>
[Missing baseline or diagnostic] <item>
[Next analysis] <single run or table>
```
