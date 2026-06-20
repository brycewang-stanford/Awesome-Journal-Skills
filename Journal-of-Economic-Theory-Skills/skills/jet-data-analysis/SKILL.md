---
name: jet-data-analysis
description: Use when handling numerical, computational, or empirical content in a Journal of Economic Theory (JET) paper — JET is theory-first, so examples, simulations, and computed equilibria must stay subordinate to the theorem and reproducible.
---

# Numerical & Computational Content (jet-data-analysis)

## When to trigger

- Your theory paper includes a worked numerical example, a simulation, a computed equilibrium, or
  (rarely) empirical/experimental evidence
- You want to know how much computational content JET will accept and how to present it
- You need to keep a computation from overshadowing the theorem

## The JET rule: theory-first, computation subordinate

JET publishes **rigorous, original theoretical results**. Empirical, experimental, quantitative, and
computational work is welcome **only when firmly grounded in theory** — i.e., as the **illustration or
test of a theoretical contribution that is itself the paper's point**, never as a stand-alone empirical
or computational paper. This skill is deliberately **light**: most JET papers are pure theory, so the
default is *minimal* numerical content.

## How to present numerical content

- **Make it serve the theorem.** A numerical example should make an assumption bite, exhibit the
  characterized object, or show tightness of a bound — not stand alone as a finding.
- **Keep examples small and transparent.** A 2x2 game, a two-type screening problem, or a three-agent
  matching market usually communicates more than a large simulation.
- **Use computation to probe necessity.** A computed **counterexample** is the cleanest way to show an
  assumption cannot be dropped (feeds jet-identification-strategy and jet-rebuttal).
- **Reproducibility.** Provide a small self-contained script (SymPy/`numpy`/`scipy`, Julia, MATLAB/Octave)
  that regenerates every reported number and figure; pin versions and **set/report seeds** for anything
  stochastic. If the paper uses research data, Elsevier **Option C** requires a repository citation/link
  or a cannot-share explanation; if it only has computation, share enough code for the referee to
  reproduce the numerical claim (see jet-replication-and-data-policy).
- **If genuinely empirical/experimental:** state the theoretical prediction first, then test it; the
  prediction is the contribution.

## Picking the smallest environment that makes the point

| Theoretical claim | Smallest honest illustration | Why it convinces a JET referee |
|---|---|---|
| An assumption cannot be dropped | a 2x2 game or two-type screening problem violating only that assumption | the failure is checkable by hand in minutes |
| A bound is tight | an environment attaining the bound exactly | tightness becomes a verifiable statement, not a plot |
| A characterized mechanism is implementable | computed transfers/allocations for two or three types | the numbers confirm the closed form line by line |
| The equilibrium set has the claimed shape | a three-agent matching market or a two-state ambiguity example | the entire set can be enumerated and inspected |
| A dynamic characterization is operational | one computed path of the recursive contract | the recursion is seen to close |

If the smallest environment that exhibits the phenomenon needs more than a page to describe,
reconsider whether the example belongs in the body or in an appendix.

## Minimal verification script (template)

```python
# verify_example_1.py — regenerates every number in Example 1
# (tightness of the bound in Theorem 2 for the two-type screening problem)
import sympy as sp

v_H, v_L, p = sp.symbols("v_H v_L p", positive=True)
rent = (v_H - v_L) * p                      # information rent at the optimum, matches eq. (7)
bound = sp.Rational(1, 2) * (v_H - v_L)     # the Theorem 2 bound
print(sp.simplify(rent.subs(p, sp.Rational(1, 2)) - bound))  # 0 → bound attained at p = 1/2
# Nothing here is stochastic; if an example is FOUND by random search,
# fix the seed, report it, and ship the search script too.
```

One short script per numbered Example, named after the theorem it serves, beats one monolithic
notebook — referees check examples against statements, not pipelines.

## Where computation sits in an accepted JET paper

- As a numbered **Example** placed immediately after the theorem it illustrates, or as a short
  "Numerical illustration" subsection — almost never as a stand-alone section competing with the
  results. Conventions drift across subfields; check recent JET papers in yours.
- Figures generated from computation follow jet-tables-figures: vector output, notation identical
  to the body, the generating script named in the note.

## Anti-patterns

- A large simulation presented as the result, with theory as decoration (off-fit for JET)
- A numerical figure whose underlying values cannot be reproduced
- Calibration/estimation with no theorem behind it (send elsewhere)
- Stochastic illustration with no seed reported

## Output format

```
【Content type】worked example | simulation | computed equilibrium | empirical test | none
【Role】illustrates / tests / counterexample to <theorem/assumption>
【Subordinate to theory?】[Y/N]  ← must be Y for JET
【Reproducible】script + pinned env + seed? [Y/N]
【Next】jet-tables-figures / jet-replication-and-data-policy
```
