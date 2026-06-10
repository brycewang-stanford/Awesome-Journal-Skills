---
name: mathfin-tables-figures
description: Use when preparing figures, numerical tables, theorem maps, appendix exhibits, and algorithm displays for a Mathematical Finance manuscript, ensuring every exhibit supports a rigorous result rather than acting as stand-alone empirical evidence.
---

# Tables & Figures (mathfin-tables-figures)

## When to trigger

- A numerical section needs figures or tables
- A proof-heavy manuscript needs diagrams, assumption maps, or appendix organization
- Exhibits risk looking like empirical finance rather than theorem support

## Exhibit rules

Every exhibit should answer: which theorem, proposition, algorithm, or modelling
insight does this support?

1. **Tie figures to formal results.** A convergence plot should cite the theorem or
   rate it illustrates.
2. **Report numerical settings.** Grid, time step, paths, tolerance, truncation,
   seed, and software version belong in the caption or appendix.
3. **Keep tables small.** Use them for parameter values, convergence rates,
   boundary comparisons, or sensitivity to assumptions.
4. **Move detail to appendices.** The author guidelines encourage detailed
   mathematical analysis in appendices; use them for long derivations and
   extended numerical diagnostics.
5. **Avoid empirical-style claims.** A calibration illustration does not establish
   an empirical result unless the paper is designed for that, which this venue
   generally is not.

## Good exhibits

- Error decay against the proven rate
- Free-boundary shape implied by an optimal stopping theorem
- Sensitivity of a pricing formula to parameters with financial meaning
- Algorithm pseudocode paired with convergence conditions
- Assumption dependency diagram for a complex theorem

## Theorem-dependency map as an exhibit

For a paper with layered results, a compact dependency table orients referees faster than
prose:

```text
Assumptions:  (A1) filtered space, usual conditions   (A2) NFLVR   (A3) bounded volatility
Lemma 3.1   <- (A1),(A2)       uniform integrability of the deflated wealth process
Lemma 3.2   <- (A1),(A3)       gradient bound for the value function
Theorem 4.1 <- L3.1, L3.2      duality and existence of the optimizer
Theorem 4.2 <- Thm 4.1,(A3)    regularity of the free boundary
```

Place it at the end of the introduction or the head of the proofs section; it doubles as your
own audit that no result silently uses an unlisted assumption.

## Figure axes speak the model's notation

- Label axes with the manuscript's symbols (t, S_t, the boundary b(t), the Hurst index H), not
  plotting-library defaults — a referee matching the plot to Theorem 4.2 should never have to
  translate notation.
- State units only where financially meaningful (years to maturity, volatility in annual
  terms); pure mathematical objects need no units.
- If a curve depends on a parameter the theorem restricts, show only values inside the
  theorem's hypotheses, or mark excursions outside them explicitly as such.

## Algorithm displays

Pseudocode earns its place only when the paper proves something about the algorithm
(convergence, complexity, stability). Pair each algorithm float with the statement number of
that guarantee, keep inputs and outputs in the manuscript's notation, and state the stopping
criterion explicitly — referees check that the displayed loop matches the object analyzed in
the proof, not a simplified cousin of it.

## Caption rewrite micro-example

A draft caption for an American-put exhibit reads "Exercise boundary for different
volatilities." Journal-ready version: "Free boundary b(t) of the American put under
Assumptions (A1)–(A3), computed with the penalized PDE scheme of Section 5 (grid 400×400,
tolerance 1e-8), illustrating the monotonicity proved in Theorem 4.2; sigma in {0.2, 0.3,
0.4}, r = 0.02, K = 100. The figure illustrates the theorem's qualitative content and makes no
calibration claim." Every clause does one caption-contract job: result, financial object,
settings, interpretation limit.

## Caption contract

Each caption should state four things: the formal result illustrated, the financial object, the numerical
settings, and the interpretation limit. For example, a pricing-sensitivity figure should not claim broad
empirical validation; it should say which theorem or model implication the curve helps readers understand.

If the exhibit cannot name a theorem, proposition, or modelling implication, cut it or move it to an
exploratory appendix. Mathematical Finance exhibits are evidence for theory comprehension, not substitutes
for proof.

## Output format

```text
[Exhibit] figure / table / algorithm / appendix
[Formal result supported] theorem/proposition/lemma
[Numerical details needed] ...
[Caption claim] ...
[Next step] mathfin-writing-style
```
