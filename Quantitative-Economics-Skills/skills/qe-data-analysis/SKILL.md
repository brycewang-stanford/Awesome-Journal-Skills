---
name: qe-data-analysis
description: Use when executing or auditing the quantitative core of a Quantitative Economics (QE) manuscript — estimation (structural/GMM/MSM or causal), moment construction, data cleaning, computation, and inference — so results are credible and reproducible for the ES Data Editor. Runs and checks the analysis; for the identification argument route to qe-identification-strategy.
---

# Data Analysis (qe-data-analysis)

## When to trigger

- Estimation is running but you need a disciplined plan for moments, solvers, and inference
- Data cleaning / sample construction choices are undocumented or ad hoc
- A structural model's computation (value-function iteration, simulation, optimization) needs validation
- You want the analysis built so it passes the pre-acceptance ES Data Editor reproducibility check on the first try

## QE expects analysis that is both credible and reproducible

QE is the Econometric Society's empirically/computationally oriented journal, so the analysis is judged on **quantitative credibility** and **reproducibility together**. The ES Data and Code Availability Policy (DCAS-compatible) means the **ES Data Editor runs reproducibility checks before final acceptance**: raw data, code, and documentation must regenerate every result in the paper and approved appendices. Build the analysis so this is true from the start, not retrofitted. House norms: report **standard errors and confidence/coverage sets** (no significance asterisks), and for long-running or hard-to-access computations ship **simplified/manageable versions and summary output files** (QE explicitly encourages this).

## Analysis discipline by paper type

### Structural / computational
- Solve cleanly: document the algorithm (VFI, policy iteration, projection), grids, tolerances, and convergence criteria.
- Estimate transparently: state the objective (MLE / GMM / MSM / indirect inference), the weighting matrix, starting values, and use **multi-start** to argue a global optimum.
- Validate: Monte Carlo recovery of known parameters; fit to targeted moments; untargeted-moment checks; sensitivity of estimates to moments.
- Counterfactuals: re-solve the model under the policy; report uncertainty around counterfactual quantities.

### Empirical (applied micro / finance)
- Sample construction documented (inclusion rules, merges, missing-data handling) so it is reproducible.
- Match the estimator to the design (modern DID, IV, RDD — see `qe-identification-strategy`).
- Inference: cluster at the assignment level; wild-cluster bootstrap with few clusters; randomization inference where apt.

### Experimental / simulation
- Pre-registered analysis followed; deviations reported. Seeds set and reported for any randomness.
- Document the DGP / experimental data pipeline end to end.

## Reproducibility scaffolding (build as you go)
- One **master script** (`run_all`) regenerating every table and figure from raw inputs.
- Pin versions: `renv.lock`, `requirements.txt`/`conda`, `Project.toml`/`Manifest.toml`, recorded Stata `ssc`/`net` versions.
- Deterministic seeds; logged run times; a README noting any partial-check scope for the Data Editor.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Quantitative Economics spans structural and applied micro; the chain serves its reduced-form lane, structural estimation uses its own toolkit.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Sample / moment construction fully documented and scripted
- [ ] Structural: solver + tolerances + multi-start + Monte Carlo recovery reported
- [ ] Estimator matched to design; inference reported as SEs / coverage sets (no asterisks)
- [ ] Seeds set and reported; results bit-reproducible from raw data via one master script
- [ ] Heavy/long computations have manageable versions + summary outputs (QE encourages this)
- [ ] Environment pinned; README drafted for the ES Data Editor

## Anti-patterns

- A single global optimum claimed from one start point with no multi-start check
- Undocumented data cleaning that cannot be reproduced
- Significance asterisks instead of standard errors / coverage sets
- Leaving the replication package to assemble at acceptance (the check is before acceptance)
- Non-deterministic results with no seed control

## What QE referees probe in the quantitative core

| Probe | What clears it at QE |
|-------|----------------------|
| Optimum global? | multi-start grid + objective across starts |
| Recovers truth? | Monte Carlo with known parameters; bias, coverage |
| Computation accurate? | tolerances, grid-refinement check, residual errors |
| Estimates robust? | re-estimate under alternative moments |
| Data Editor can reproduce? | one `run_all`, pinned environment, logged seeds |

The defining QE failure mode is **numerical accuracy left unvalidated** — a counterfactual reported to three digits the grid cannot support. Treat numerical error like sampling error: bound it and report it.

## Worked vignette: an SMM estimate (illustrative)

A paper estimates an adjustment-cost parameter by simulated method of moments, targeting investment-rate variance and serial correlation. Suppose the headline counterfactual — removing a subsidy lowers aggregate investment 8% — shifts to 5% when the grid doubles from 100 to 200 capital nodes. That 3-point swing is a numerical artifact a referee will catch. Fix: refine the grid until the counterfactual is stable, show a global minimum across 50 starts, and attach a sensitivity matrix. (Illustrative.)

## Referee pushback and the analysis fix

- *"The structural estimates are not credibly identified."* → Add a sensitivity matrix mapping parameters to moments; show targeted-moment fit and untargeted validation.
- *"Numerical accuracy is not validated."* → Report tolerances, a grid-refinement check, and stability to the digits shown.
- *"Results are not robust to specification."* → Re-estimate under alternative moments and sub-samples; tabulate the headline movement.

## Output format

```
【Paper type】structural / empirical / experimental / simulation
【Estimation】objective + solver/tolerances + multi-start? [Y/N]
【Validation】Monte Carlo recovery / moment fit / design diagnostics
【Inference】SEs / coverage sets (no asterisks); clustering if any
【Reproducibility】master script + pinned env + seeds? [Y/N]
【Next step】qe-tables-figures
```
