---
name: smr-simulation-studies
description: Use when designing the Monte Carlo simulation study for a Sociological Methods & Research (SMR) paper — data-generating processes, competing methods, performance metrics, and the regimes where the method wins or breaks. Designs the simulation; does not derive properties or run the real-data illustration.
---

# SMR Simulation Studies

Use this to build the Monte Carlo that an SMR reviewer will trust. At a methods journal the
simulation is not a formality — it is the primary evidence that the analytical properties hold in
finite samples and that the method beats real competitors. A weak or self-serving simulation sinks
otherwise sound papers.

## Design the DGP space deliberately

Reviewers attack the data-generating process first. Specify it as a designed experiment, not a
convenient example:

- **Factors and levels**: sample size (and, for panels/networks, the relevant dimensions), the
  parameter that controls the difficulty (effect size, dependence, missingness rate, sparsity), and
  any nuisance complications. State why each level is realistic for sociological data.
- **Coverage of the assumption boundary**: include cells where your own assumptions *fail*, so the
  paper shows the method's limits, not just its triumphs. SMR rewards honesty about breakdown.
- **Calibration to the application**: at least one DGP should be calibrated to the real dataset in
  `smr-empirical-illustration`, so the simulation speaks to a setting readers care about.
- **Replications and seeds**: enough Monte Carlo replications for stable estimates of the metrics, with
  seeds fixed and reported for reproducibility.

## The competitor set (non-negotiable)

A simulation that compares the new method only to a naive baseline is the classic reject. Include:

- The **current default** practitioners actually use.
- The **strongest existing alternative** for the same problem (often from a neighboring discipline —
  see `smr-literature-positioning`).
- Where relevant, an **oracle / infeasible** benchmark to show the gap your method closes.

If your method loses to a competitor in some cell, report it and explain when each method is
preferable — conditional recommendations are more credible than universal victory.

## Metrics that match the claim

| Claim type | Report | Common SMR pitfall |
|---|---|---|
| Point estimation | bias, RMSE, relative efficiency | reporting bias but hiding variance |
| Inference / testing | empirical size, power, CI coverage and width | "performs well" with no coverage number |
| Selection / classification | accuracy + the costs of each error | accuracy only, ignoring imbalance |
| Computation | runtime, scaling, convergence rate | feasibility claim with no timing |

Coverage and size near the nominal level are the metrics SMR reviewers scrutinize most for inference
methods — report the actual numbers, not adjectives.

## Presenting the study compactly

- Summarize the full grid in a table or a small-multiples figure; do not narrate every cell.
- Lead with the cell that makes the contribution's point (where the incumbent breaks and the method
  holds), then show the boundary where the method itself degrades.
- Hand the exhibit design to `smr-tables-figures` so the grid is self-contained and readable in print.

## Checklist

- [ ] The DGP is specified as a factorial design with realistic levels, each justified.
- [ ] Cells where the method's own assumptions fail are included.
- [ ] At least one DGP is calibrated to the empirical illustration's data.
- [ ] The competitor set includes the current default and the strongest alternative.
- [ ] Metrics match each claim (coverage/size for inference, bias+variance for estimation).
- [ ] Replication count and seeds are reported.
- [ ] Cells where the method loses are reported with a conditional recommendation.

## Anti-patterns

- **Strawman comparison**: only a naive baseline, never the real competitor.
- **Sunny-cell selection**: showing only regimes that favor the method.
- **Adjective metrics**: "good size control" with no rejection rates.
- **Cherry-picked n**: one favorable sample size with no scaling pattern.
- **Uncalibrated fantasy DGP**: a design unrelated to any sociological data.
- **Hidden seeds / replication count**: results that cannot be reproduced.

## Output format

```text
[Simulation status] convincing / needs repair / not ready
[DGP factors] <factor : levels, with realism note>
[Competitor set] <default + strongest alternative (+ oracle)>
[Metrics] <bias/RMSE/coverage/size/power/runtime as claimed>
[Boundary cell] <where the method degrades and why that is honest>
[Next SMR skill] smr-empirical-illustration
```
