---
name: msom-theory-development
description: Use when building the analytical model or operational mechanism at the core of a Manufacturing & Service Operations Management (M&SOM) manuscript — formulating the decision, objective, and uncertainty; deriving structural results; or specifying the operational mechanism behind an empirical hypothesis. Adapts theory work to M&SOM's dominant analytical/stochastic-modeling tradition.
---

# Model & Mechanism Development (msom-theory-development)

## When to trigger

- You have a topic but no formal model or sharp operational mechanism yet
- Your "model" is a regression with no operational decision inside it
- A reviewer asks "what is the structural result?" or "what drives the effect operationally?"
- You need to decide objective, decision variables, state, and source of uncertainty

## For analytical papers (the dominant M&SOM tradition)

M&SOM's historically dominant methodology is **analytical/stochastic operations modeling**. A strong model makes the **operational decision explicit** and yields **structural insight**, not just a numerical answer:

- **Decision variables**: what the operator chooses (order quantity, price, capacity, staffing, routing, contract terms).
- **Objective & dynamics**: expected cost/profit/welfare, often over time; specify the stochastic primitives (demand, lead time, arrivals, service times).
- **Model class**: newsvendor/inventory, MDP/dynamic program, queueing/diffusion, stochastic program, robust/DRO, or game-theoretic/mechanism-design — chosen because it fits the decision.
- **Structural results**: prove monotonicity, convexity, threshold/base-stock/index policies, comparative statics, or equilibrium existence/uniqueness — the *form* of the optimal policy is the insight.
- **Tractability discipline**: assumptions earn their keep by producing clean structure; flag where they bind and what a numerical study must then carry.

## For empirical papers

Specify the **operational mechanism** before estimation: state the behavioral/operational channel (e.g., congestion, learning, inventory record inaccuracy, demand shaping) and the comparative-statics prediction it implies, so the empirical test maps to an operations theory, not a correlation hunt.

## Keep the operations decision central

Every mechanism must change an operational decision or outcome. If the model could be relabeled as pure economics or marketing with no operational lever, return to `msom-topic-selection`.

## Checklist

- [ ] Decision variables, objective, and uncertainty primitives stated explicitly
- [ ] Model class justified by the operational decision (not by convenience)
- [ ] Structural result(s) derived or clearly targeted (policy form, comparative statics)
- [ ] Assumptions listed; which bind and why made transparent
- [ ] Empirical work: operational mechanism and its comparative static stated a priori

## Anti-patterns

- A model with no decision variable — just an equilibrium description with no operational lever.
- Assumptions chosen only for tractability with no discussion of what they cost.
- "Numerical results show…" with no structural insight a manager could carry.
- Relabeling an economics/marketing model as OM without an operations decision.

## Output format

```
【Decision / objective / uncertainty】...
【Model class】newsvendor / MDP / queueing / stochastic-prog / game-theoretic — why
【Structural results】policy form / comparative statics / equilibrium ...
【Assumptions】binding ones flagged ...
【Operations centrality】confirmed ...
【Next step】msom-literature-positioning
```
