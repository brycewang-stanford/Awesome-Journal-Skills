---
name: mathfin-data-analysis
description: Use for the numerical-experiments part of a Mathematical Finance (Wiley) manuscript — adapted for a theory journal, this means illustrative computation that SUPPORTS a proof (convergence, error bounds, qualitative behavior), not empirical data analysis. Keeps numerics rigorous and subordinate to the theory.
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
