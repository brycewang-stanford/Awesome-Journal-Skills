---
name: est-data-analysis
description: Use when executing and reporting the analysis for an Environmental Science & Technology (ES&T) manuscript so it survives expert review — analytical QA/QC, honest uncertainty, statistics appropriate to environmental data, and closed mass balances. It guides analysis and reporting norms; it does not fabricate results.
---

# Data Analysis (est-data-analysis)

ES&T reviewers scrutinize the analytical chain: blanks, recoveries, detection limits, replicates, and
whether the numbers add up. This skill covers execution and reporting; design decisions live in
`est-study-design`, and deposit/reproducibility in `est-reporting-and-reproducibility`.

## When to trigger

- Reducing raw instrument/field data into results
- Building the results section and the QA/QC reporting
- A reviewer asked about detection limits, recoveries, replicates, or statistics
- Closing a mass/energy balance or fitting kinetics/dose–response

## Analysis norms ES&T expects

1. **Report QA/QC explicitly.** Method/field blanks, matrix-spike recoveries, CRM results, **LOD/LOQ**,
   calibration range and R², surrogate/internal-standard recoveries, and how non-detects were handled.
2. **Honest uncertainty.** Report replicates with measures of dispersion (SD/SE/CI), not single
   values; propagate uncertainty through derived quantities; state n every time.
3. **Right statistics for environmental data.** Handle left-censored (below-LOD) data correctly
   (e.g., substitution caveats, MLE/ROS, Kaplan–Meier); check distributional assumptions; use
   nonparametric or transformed analyses for skewed/heteroscedastic data; correct for multiple
   comparisons.
4. **Mass / energy balance.** Account for products, sorbed and volatilized fractions, and losses;
   report closure (%) and explain gaps.
5. **Kinetics / dose–response.** Report rate constants/half-lives with CIs and goodness of fit;
   EC/IC/LC values with confidence bounds; state the model fitted.
6. **Effect size & significance.** Give magnitudes and intervals, not p-values alone; relate results
   to environmentally meaningful thresholds.

## Reproducibility while you work (not at the end)

- A **master script/workflow** regenerates every figure, table, and SI exhibit from processed data.
- **Set and report seeds** for any stochastic step (bootstrap, Monte Carlo, simulation).
- Pin software/package versions; record instrument settings and integration parameters.
- Keep figure/table numbers matched to script outputs (see `est-reporting-and-reproducibility`).

## Anti-patterns

- Results with no blanks, recoveries, or detection limits reported
- Single measurements with no replication or dispersion
- Naive zero/half-LOD substitution for heavily censored data with no caveat
- A transformation/treatment study whose mass balance never closes (or is never reported)
- p-values without effect sizes or environmental thresholds
- Over-fitting kinetics/dose–response with too few points

## Output format

```
【Main result】magnitude + uncertainty (n, SD/CI) + units
【QA/QC】blanks / recoveries / CRM / LOD-LOQ / calibration reported? [Y/N]
【Censored data】handled how
【Mass/energy balance】closure % + explanation
【Statistics】appropriate test + assumptions checked? [Y/N]
【Reproducible】master script + seeds + pinned versions? [Y/N]
【Next】est-figures-and-tables
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — analytical QA/QC, statistics, and modeling packages
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — data-availability and reproducibility expectations
