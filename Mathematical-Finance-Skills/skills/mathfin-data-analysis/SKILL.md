---
name: mathfin-data-analysis
description: Use when designing or auditing the numerical-experiments part of a Mathematical Finance (Wiley) manuscript — at this theory-first venue that means illustrative computation that SUPPORTS a proof (convergence, error bounds, qualitative behavior), never empirical data analysis. Keeps numerics rigorous, reproducible, and subordinate to the theorems.
---

# Numerical Experiments (mathfin-data-analysis)

## Note on framing

This is a **theory-first** journal. *Mathematical Finance* explicitly states that **numerical
experiments are welcome only when accompanied by a rigorous analysis** supporting the
theoretical developments, and that **routine application of computational methods to financial
data will not be considered**. So "data analysis" here is *not* empirical estimation — it is
numerical work that illustrates or stress-tests a theorem. This skill is deliberately lighter
than its empirical-journal counterpart.

## When to trigger

- You want to add simulations or a numerical scheme to a proof-based paper
- A referee may ask whether your theorem "does anything" beyond existence
- You need to show convergence, accuracy, or qualitative behavior predicted by the theory

## How to keep numerics journal-appropriate

1. **Tie every experiment to a result.** Each figure/table should illustrate a specific
   theorem, proposition, or rate (e.g., "Monte Carlo error decays at the proven $O(n^{-1/2})$
   rate", "the free boundary matches the smooth-fit characterization").
2. **State the method precisely.** Discretization scheme (Euler–Maruyama, Milstein, PDE
   finite-difference/finite-element), step sizes, number of paths, variance reduction,
   truncation of the domain — enough that the experiment is reproducible.
3. **Report error, not just output.** Where the theory gives a rate or bound, show the
   empirical rate against it; show convergence as the grid refines.
4. **Choose parameters with financial meaning** (volatilities, maturities, strikes) so the
   illustration speaks to the modelling problem.
5. **Keep numerics subordinate.** They support the theory; they are never the contribution.
   Do not let a numerical section grow into a stand-alone empirical study.

## Reproducibility (light but real)

- Pin software/library versions; set and **report random seeds** for any Monte Carlo.
- Make illustrative code reproducible; consider archiving it (Zenodo/GitHub) and citing it.
- Include a **Data Availability Statement** even if no external data are used (see
  mathfin-replication-and-data-policy).

## Matching scheme to result type

| Result being illustrated | Natural scheme | What the exhibit must report |
| --- | --- | --- |
| Strong/weak SDE convergence rate | Euler–Maruyama or Milstein with halving steps | log–log error slope against the proven order |
| BSDE well-posedness or rate | Backward Euler / least-squares Monte Carlo / deep BSDE solver | terminal error and driver residual across grids |
| Optimal stopping / free boundary | Binomial tree or PDE variational-inequality solver | boundary location against the smooth-fit characterization |
| Rough-volatility approximation | Hybrid scheme for fractional kernels; Markovian lift | implied-vol skew slope against the proven power law |
| Duality gap = 0 | Primal candidate and dual bound computed independently | gap shrinking as the discretization refines |
| Mean-field limit | N-player simulation vs. McKean–Vlasov solver | distance to the limit decaying in N at the stated rate |

## Worked micro-example: convergence exhibit for a rough-volatility paper

Suppose Theorem 3.2 proves that a Markovian multi-factor approximation of a rough volatility
model converges at a rate governed by the Hurst parameter H. The journal-appropriate exhibit:
simulate both models with the same Brownian increments, plot the implied-volatility error
against the number of factors on log axes, draw the theoretical slope as a reference line, and
caption with the scheme, step size, path count, seed, and the theorem number. What would NOT
fit: calibrating the approximation to index-option data and reporting fit quality — that turns
an illustration into the empirical study the journal screens out.

## Pre-submission numerics audit

- Every exhibit names the theorem, proposition, or rate it illustrates — no orphan plots.
- The observed rate is computed (regression slope), not eyeballed, and stated next to the
  proven one.
- Degenerate sanity cases (zero volatility, Black–Scholes limit, H → 1/2) reproduce known
  closed forms before the general runs are trusted.
- The numerical section would survive deletion: the theorems stand alone without it.

## Anti-patterns

- A numerical study with no theorem behind it (out of scope for this journal).
- Plots with no error/convergence analysis where the theory promises a rate.
- Unstated scheme, step size, or path count — irreproducible.
- Calibrating to real market data and presenting it as the paper's result.

## Output format

```
【Experiment】what it illustrates (which theorem/rate)
【Method】scheme + step/paths + variance reduction
【Error reported】empirical vs. theoretical rate/bound
【Parameters】financial values used
【Reproducibility】seeds + versions + code location
【Next step】mathfin-tables-figures
```
