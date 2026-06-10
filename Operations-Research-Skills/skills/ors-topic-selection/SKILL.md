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

## Desk-reject patterns at the area-editor gate

Before a manuscript reaches reviewers, the Area Editor screens for fit. The recurring
desk-stage rejections at *Operations Research* cluster as:

| Desk-reject trigger | Why OR returns it | Pre-empt by... |
|---------------------|-------------------|----------------|
| Application with no method | "no OR/MS methodological contribution" | isolate a model class, guarantee, or structural theorem |
| Solver-on-a-dataset | belongs at an applied/computing venue | add provable structure or convergence/complexity analysis |
| Managerial-OM survey | empirical-OM, not flagship methodology | redirect to *Management Science* / M&SOM / *J. Operations Management* |
| Code/data structures only | engineering artifact | redirect to *INFORMS Journal on Computing* |
| Wrong editorial area | scope mismatch with Area Editors' Statement | re-read the statement; route on methodology, not application |
| Heuristic with no guarantee | not a methodological result on its own | prove an approximation factor, regret, or convergence rate |

Operations Research is the **INFORMS flagship** for rigorous OR methodology —
optimization, stochastic models, queueing, simulation, game theory, revenue
management — where the premium is on **both** a theorem-grade result and a credible
computational/decision study. It is not a home for an empirical-OM survey; that
distinction is the single biggest source of mis-targeted submissions.

## Fit-test vignette (illustrative)

A team has logistics data and shows, via regression, that consolidation lowers cost.
Run the fit test: **method?** none new — it is a known estimator. **Rigor?** no
theorem, no guarantee. **Significance to OR?** the *finding* is operational but the
*contribution* is empirical. Verdict: not OR as-is. The fix that earns OR fit — extract
the underlying stochastic-routing model, prove a structural property of the optimal
consolidation policy, and validate it computationally. Same data, but now the
contribution is a methodological result with a decision payoff. Only then does the
methodology-area routing (Transportation vs. Stochastic Models) even matter.

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
