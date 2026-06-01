---
name: ors-topic-selection
description: Use when deciding whether a problem is a fit for Operations Research (OR) and which of its editorial areas it belongs to — testing for a genuine OR/MS methodological contribution and picking the correct area before formulating. Scopes and routes the problem; it does not build the model (ors-theory-development) or position it in the literature (ors-literature-positioning).
---

# Topic Selection & Area Fit (ors-topic-selection)

## When to trigger

- You have a problem but are unsure it belongs in *Operations Research* versus a sibling venue.
- You must choose the editorial **area** the submission will route into.
- A co-author asks "is this methodological enough for OR?"

## The OR fit test

*Operations Research* (INFORMS) publishes **mathematically rigorous OR/MS
methodology** — optimization, stochastic/probabilistic models, simulation, decision
analysis — favoring **provable results** and methodological novelty over purely
empirical work. Ask:

- **Is the core contribution a method, not just an application?** A new model class,
  algorithm with guarantees, structural theorem, bound, or analysis technique.
- **Is there rigor?** Theorems/proofs, complexity or convergence results, or a
  validated stochastic/simulation analysis — not only numbers.
- **Is it significant to the OR community?** The introduction (which must be
  **equation-free**) has to state the problem, the results, and *why the OR community
  should care*.
- **Does an application carry genuine OR innovation?** Real-world OR is welcome via
  the **Real-World OR Innovations** area, but the innovation must be methodological,
  not a routine deployment.

## Pick the editorial area (route at submission)

Submissions route into one of the journal's named areas, each led by Area Editors who
set scope via published **Area Editors' Statements**. Match your contribution:

| If your core is... | Likely area |
|--------------------|-------------|
| Deterministic optimization, polyhedra, duality, algorithms | Optimization |
| Queues, Markov chains, applied probability | Stochastic Models |
| Discrete-event / Monte Carlo, output analysis, sim-opt | Simulation |
| Learning-driven OR, data-driven decisions | Machine Learning and Data Science |
| Pricing, auctions, platforms, revenue management | Markets/Platforms/Revenue Management |
| Portfolio, hedging, risk | Financial Engineering |
| Routing, networks, mobility | Transportation |
| Public-sector, equity, health, climate | Societal Impact / Energy and Environment |
| Deployed methodological innovation | Real-World OR Innovations |

> Area names and Area Editors rotate — confirm the current list and Area Editors'
> Statements before selecting (待核实 specific names).

## Sibling-venue triage

- Operations/supply-chain *management* framing with managerial emphasis → consider *Management Science* or *M&SOM*.
- Computation-only artifact (codes, data structures) → *INFORMS Journal on Computing*.
- Application with thin methodology → strengthen the method or target an applied INFORMS venue.

## Anti-patterns

- "We applied a known solver to our dataset" with no new method.
- Choosing the wrong area, forcing a re-route and delay.
- An empirical finding with no provable or structural OR contribution.

## Output format

```
【OR fit】method / rigor / significance: pass | weak: [...]
【Area】selected ... (rationale)
【Sibling-venue risk】... (or none)
【Next step】ors-theory-development
```
