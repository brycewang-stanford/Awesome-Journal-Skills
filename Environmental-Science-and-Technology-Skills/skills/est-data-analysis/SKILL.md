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

## QA/QC reporting table reviewers expect to see

ES&T referees often work down a mental analytical checklist. Reporting each item pre-empts the most
common "rigor not established" objection. The minimum set, with what a reviewer reads when it is
absent:

| Element | What to report | If omitted, the reviewer assumes |
|---------|----------------|----------------------------------|
| Method/field blanks | blank levels vs. sample levels; subtraction approach | contamination is uncontrolled |
| Recoveries | matrix-spike % and CRM agreement | quantitation is biased/unknown |
| LOD/LOQ | derivation (e.g., 3σ/10σ or S/N) and per-analyte values | "detections" may be noise |
| Calibration | range, R², whether samples fall in range | extrapolation beyond standards |
| Surrogate/IS recoveries | per-sample recovery correction | run-to-run drift hidden |
| Non-detects | censoring method (ROS/MLE/KM), not bare substitution | summary statistics distorted |

## Worked micro-example (illustrative — PFAS quantitation with censored data)

A river-PFAS dataset (illustrative numbers) shows how the rules combine into a reportable result:

- 24 samples, triplicate injection; LOQ for PFHxA = 0.5 ng/L (illustrative, derived at 10×S/N).
- Matrix-spike recovery 92% (RSD 7%, n=6); field blank < LOQ; surrogate-corrected.
- 9 of 24 below LOQ — **left-censored**. Naive half-LOQ substitution would report a mean of
  3.1 ng/L; regression-on-order-statistics (ROS) gives 2.4 ng/L (illustrative), because substitution
  inflated the low tail. Report the ROS mean with its CI and *state the method*.
- Reported result: "PFHxA = 2.4 ng/L (95% CI 1.7–3.3, n=24, 38% < LOQ; ROS), recovery 92±7%." That
  single line carries magnitude, uncertainty, n, censoring handling, and recovery — the form a
  reviewer can sign off without a query.

## Referee-pushback patterns and the venue-specific fix

- *"Detection limits and QA/QC are not reported."* → Add the blank/recovery/LOD/LOQ table to the SI
  and cite it from Methods; never leave it implicit.
- *"Below-detect data handled by substitution."* → Re-analyze with ROS/MLE/Kaplan–Meier; show the
  result is robust to the censoring choice.
- *"The mass balance does not close."* → Report closure %, name the unaccounted fraction (sorbed,
  volatilized, mineralized), and bound it rather than ignoring the gap.

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
