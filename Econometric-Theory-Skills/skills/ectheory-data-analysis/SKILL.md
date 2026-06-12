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

## What an ET referee checks in the Monte Carlo first

At a theorem-proof venue the referee treats simulations as a stress test of whether the limit approximation
is *useful*, not as the result. The first checks:

| Referee check | Passes for ET | Triggers a revision |
| --- | --- | --- |
| DGP vs assumptions | Spans the boundary (near-unit-root, weak ID, growing dim) | One interior DGP that flatters |
| Metric vs claim | Size and power for a test; coverage, bias, RMSE for an estimator | Size only, or RMSE without coverage |
| Sample sizes | A grid of n that makes the rate visible | A single n hiding slow convergence |
| Honesty | Breakdown region reported | Uniformly green tables, no failure regime |

A Monte Carlo that never visits the regime where the proof's delicate step lives is desk-reject-adjacent.

## Worked vignette and the simulation fixes

For a refinement that reduces the error in rejection probability of a t-test from order n^(-1/2) to n^(-1)
under local-to-unity asymptotics, report the design:

```text
# Monte Carlo skeleton for the refinement illustration
seed   = 20260610               # fixed and reported
reps   = 50000                  # per cell
n_grid = [50,100,200,400,800]
c_grid = [0,-5,-10,-20]         # local-to-unity drift c, root rho = 1 + c/n
# size under H0 (first-order vs refined); power under local alt theta0 + h/sqrt(n)
# show ERP=|size-0.05| decays faster for the refined test; flag breakdown at large |c|
```

The fixes: "rate without distribution theory" → upstream (route `ectheory-identification-strategy`), since a
Monte Carlo cannot supply a missing limiting law; "no finite-sample evidence" → add the boundary-spanning
design; "simulations avoid the hard regime" → extend the c-grid into the regime where the proof's delicate
step operates. The ET structure is theorem → proof → simulation; confirm Supplement conventions against the
author guidelines.

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
