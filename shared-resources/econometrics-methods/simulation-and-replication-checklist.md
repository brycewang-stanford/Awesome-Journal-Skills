# Simulation And Replication Checklist

Use this checklist for econometrics methods papers before submission or
conditional-acceptance replication packaging.

## Simulation Design

- State the data-generating process and the assumption each design stresses.
- Compare against credible alternatives, not only toy baselines.
- Report sample sizes, replications, seeds, tuning parameters, convergence
  failures, and runtime.
- Include negative or boundary cases when the method has known limits.
- Keep the main text compact; put full grids and robustness details in the
  allowed appendix or supporting information.

## Empirical Illustration

- Explain what applied conclusion changes when the new method is used.
- Provide enough data provenance and variable documentation for replication.
- Avoid using the empirical example as decoration; it should reveal applied
  value, not just run the estimator once.

## Replication Package

- Top-level README with execution order, software versions, commands, expected
  outputs, runtime, and hardware assumptions.
- Master script or documented workflow.
- Stable seeds and clear random-number handling.
- Data or access instructions, plus any confidentiality or proprietary-data
  restrictions.
- Output mapping from each table/figure/simulation panel to the script that
  creates it.

## Minimal Output

```text
[Simulation role] theory check / stress test / comparison / boundary case
[Empirical role] applied-value demonstration / diagnostic / none
[Missing item] DGP / baseline / seed / software / data / command / output map
[Replication risk] low / medium / high
```
