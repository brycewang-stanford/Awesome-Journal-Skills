---
name: mathfin-literature-positioning
description: Use when positioning a Mathematical Finance (Wiley) manuscript against the financial-mathematics frontier — stake the methodological contribution against prior stochastic-analysis, pricing, and control results, citing the precise theorem you sharpen, generalize, or supersede.
---

# Literature Positioning (mathfin-literature-positioning)

## When to trigger

- The introduction reads as a survey rather than a precise contribution claim
- Unsure which prior theorem your result generalizes, sharpens, or contradicts
- A referee might say "this is already known under weaker/stronger assumptions"

## The Mathematical Finance positioning bar

Because the journal prizes **methodological novelty and contribution to financial modelling**,
positioning must be **theorem-level**, not topic-level. The reader (often a Bachelier Finance
Society member steeped in stochastic analysis) wants to know exactly which assumptions you
relax, which generality you add, or which open problem you close — and why earlier machinery
was unable to. A vague "the literature has studied X" invites a desk concern about novelty.

## How to position

1. **Name the closest prior result** and its assumptions precisely (model class, regularity,
   filtration, market completeness). State what it *cannot* deliver.
2. **Locate your delta on one axis**: weaker assumptions, broader model class, sharper rate,
   constructive vs. existence-only, time-consistent vs. not, or a genuinely new object.
3. **Cite landmark machinery, not laundry lists** — the foundational tools you build on
   (e.g., semimartingale theory, FTAP/NFLVR, BSDE theory, convex duality, stochastic control)
   should be cited where they do work, not as decoration.
4. **Pre-empt the "special case" objection**: show your result is not a corollary of an
   existing theorem under a change of variables.
5. **Flag what you do NOT claim** — keeping scope honest is part of the rigor culture.

## Frontier strands and what positioning owes each

- **Robust finance / model uncertainty:** say whether your setting is dominated or
  non-dominated, pathwise or quasi-sure — claims blur across these regimes and referees check.
- **Rough volatility:** state the Hurst regime and whether the result concerns the model's
  probabilistic structure, its approximation theory, or its pricing asymptotics.
- **Mean-field games / large populations:** distinguish existence for the limiting MFG from
  convergence of the N-player equilibrium — different theorems with different ancestors.
- **Transaction costs / frictions:** identify whether the comparison literature is shadow-price,
  duality, or viscosity/PDE based; your delta reads differently against each.
- **Term structure / HJM:** position against the consistency and finite-dimensional-realization
  results, naming the state space your forward-curve dynamics live on.
- **Risk measures / time consistency:** specify static vs. dynamic, convex vs. coherent, and
  which representation theorem you extend.

## Delta sentence scaffold

```text
The closest result is [Author, Year, Thm n], which proves [conclusion] under [hypotheses].
Our Theorem [m] removes [hypothesis] / extends the model class from [class A] to [class B] /
upgrades existence to a constructive characterization. The key obstacle is [technical issue];
[Author]'s argument relies on [tool], which fails here because [reason]. We instead [new idea].
```

One scaffold per main theorem suffices; referees at this venue prefer a single precise
comparison to a paragraph of adjacent citations.

## Sibling-venue triangulation

Positioning also signals fit. If every paper you compare against lives in a probability journal
with no financial object in its theorem statements, the manuscript reads as misdirected pure
mathematics; if the comparisons are all empirically oriented, the rigor-bar question arises.
Healthy *Mathematical Finance* positioning braids the journal's own literature with *Finance
and Stochastics* and stochastic-analysis sources, keeping the financial-modelling payoff
visible in the same paragraph as the mathematical delta.

## Anti-patterns

- A standalone literature-review section detached from the contribution claim.
- Citing a result without its hypotheses, so the reader cannot judge your delta.
- Over-claiming generality the proof does not actually deliver.
- Ignoring a known counterexample or a sharper existing bound.
- Treating "no one has done exactly this" as novelty when the technique is routine.

## Output format

```
【Closest prior result】author/year + its assumptions + its limit
【Your delta】weaker-assumptions / broader-class / sharper / constructive / new-object
【Machinery you build on】[foundational tools, cited where they work]
【Special-case defense】why your result is not a corollary of prior work
【Scope honesty】what you explicitly do NOT claim
【Next step】mathfin-identification-strategy
```
