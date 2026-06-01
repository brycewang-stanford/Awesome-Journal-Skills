---
name: ectheory-data-analysis
description: Use for the Monte Carlo and numerical-illustration component of an Econometric Theory (ET) paper — designing simulations that show finite-sample behavior tracks the asymptotics, plus any illustrative empirical example. Lighter than empirical journals; the spine stays the theory.
---

# Numerical Illustration & Monte Carlo (ectheory-data-analysis)

## When to trigger

- Your theorem is proved and you need simulations showing it bites in finite samples
- Reviewers will ask whether the asymptotic approximation is accurate at realistic n
- You include an illustrative empirical application and want it to serve the theory, not the reverse
- The simulation design feels arbitrary and you need principled choices

## Role of "data analysis" at a theory journal

ET is theorem-proof first; numerical work is **evidence that the asymptotics are useful**, not the
contribution itself. Two distinct, optional components:

1. **Monte Carlo** — the standard companion to a limit result. Its job is to show that finite-sample
   size/power/bias/coverage track the theory, and to map where the approximation breaks down.
2. **Empirical illustration** — an optional applied example showing the method on real data. It
   illustrates; it does not carry the paper. Keep it proportionate.

## Designing a credible Monte Carlo for ET

- **DGP coverage.** Span the assumptions: include cases near the boundary (weak identification,
  near-unit-root, growing dimension, heavy tails, dependence) where the theory is most stretched.
- **What you report.** For an estimator: bias, RMSE, and the gap between empirical and nominal
  coverage. For a test: empirical size under the null and power under local/fixed alternatives.
- **Comparisons.** Benchmark against the natural existing method, so the simulation shows what your
  theory buys.
- **Sample sizes.** A grid of n that reveals the convergence rate visually, not a single n.
- **Honesty.** Show where the asymptotic approximation is poor; a candid breakdown region strengthens
  credibility more than uniformly green tables.

## Reproducible computation

- Fix and **report random seeds**; report the number of Monte Carlo replications and all n.
- Specify the DGP precisely enough to regenerate every table/figure.
- Keep simulation code clean and runnable; long simulation evidence can go to the online
  Supplementary Material (already-reviewed, separate labeled file, not copyedited).

## Checklist

- [ ] Monte Carlo DGPs span the assumptions, including the boundary cases
- [ ] Reported metrics match the claim (coverage/size/power/bias/RMSE as appropriate)
- [ ] A grid of n reveals the rate; convergence visible
- [ ] Benchmarked against the natural existing method
- [ ] Breakdown region of the approximation shown honestly
- [ ] Seeds, replication count, and DGP fully specified
- [ ] Empirical illustration (if any) kept proportionate to its illustrative role

## Anti-patterns

- A single favorable n and DGP chosen to flatter the method
- Simulations that never probe the boundary where the theory is delicate
- An empirical "application" that overshadows the theorem
- Unreported seeds / replication counts (non-reproducible)
- Reporting size but not power for a test (or vice versa)

## Output format

```
【Components】Monte Carlo / empirical illustration / both
【DGP coverage】boundary cases included? [Y/N]
【Metrics】size / power / coverage / bias / RMSE
【n grid】reveals rate? [Y/N]
【Benchmark】existing method compared? [Y/N]
【Reproducibility】seeds + reps + DGP specified? [Y/N]
【Next step】ectheory-tables-figures
```
