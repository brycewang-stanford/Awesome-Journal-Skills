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

## Theory-to-simulation contract

EctJ referees read Monte Carlo sections as tests of the theory, and RES guidance caps the
main-text simulation summary near one page, so every theoretical claim needs exactly one matching
finite-sample exhibit:

| Theoretical claim | Required Monte Carlo evidence | Typical display |
|---|---|---|
| Asymptotic normality | Coverage of nominal 95% intervals across n | Coverage row per sample size |
| Size control of a test | Null rejection rates near 5% at the relevant boundary | Size table with nominal level in header |
| Local power gain | Power against the incumbent under drifting alternatives | One power figure |
| Rate or bias reduction | Bias and RMSE relative to the strongest competitor | Compact bias/RMSE panel |
| Tuning robustness | Behavior across bandwidth or penalty choices used in practice | Supplement grid, one-line main-text summary |

A theorem with no matching row invites the classic EctJ objection that the asymptotics carry no
finite-sample evidence; a simulation with no matching theorem is decoration to cut.

## Anchoring the DGP in the application

The other classic objection is a simulation design detached from the empirical illustration. Fix
it by calibration (illustrative numbers): if the application is a firm panel with N=180, T=12, and
residual serial correlation around 0.6, the core DGP should be N=200, T=12 with AR(1) errors at
rho in {0, 0.3, 0.6}, not an i.i.d. cross-section with n=10,000. State in the simulation preamble
which DGP parameters were estimated from the application data and which probe theoretical
boundaries. One calibrated design plus one boundary design beats six arbitrary grids at this
venue, and the pairing lets the empirical section reuse the simulation's vocabulary when it
explains why the new procedure changes the applied conclusion.

## Computation reporting floor

- State replication counts and justify them (illustrative floor: 1,000 draws for size claims,
  more when coverage is pushed to the third digit).
- Report wall-clock runtime for the main simulation and the application on stated hardware;
  the EctJ replication policy makes these numbers checkable after conditional acceptance.
- Log convergence failures per design cell and the handling rule (drop, restart, flag); silent
  drops change rejection rates, and referees at this venue know it.
- Name the software stack and versions in the simulation note, matching the replication README.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). The Econometrics Journal is a methods venue — estimator validity + simulation; pair estimates with diagnostics.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Output format

```text
[Evidence readiness] strong / adequate / weak
[Monte Carlo role] <theory validation or stress test>
[Empirical application role] <applied-value demonstration>
[Missing baseline or diagnostic] <item>
[Next analysis] <single run or table>
```
