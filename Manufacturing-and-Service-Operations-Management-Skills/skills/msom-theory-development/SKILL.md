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


## Theory pass for Manufacturing & Service Operations Management

Run this as a concrete capability pass. First lock the process bottleneck, decision policy, queue/inventory/service mechanism, and implementation constraint; then test whether the manuscript addresses operations reviewers who look for service/manufacturing process insight, implementable policies, and operational performance evidence.

- **Primary move:** Separate construct, mechanism, scope condition, and testable implication; refuse a theory section that only summarizes prior work.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against Management Science for broader OR/MS reach, Production and Operations Management for wider OM readership, Operations Research for method-first theory; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Worked micro-example (illustrative)

Vignette: a perishable-inventory model for a hospital blood bank choosing a daily order quantity when units expire after a fixed shelf life. The decision is the order-up-to level; the uncertainty is daily demand plus age-dependent outdating. A dynamic program is the right class because the contribution is the *form* of the optimal rule under perishability. The structural result — an order-up-to level that *declines as on-hand inventory ages* — is the insight; an illustrative numerical study shows a flat base-stock rule that ignores age raises outdating by 11% (numbers illustrative). The mechanism, aging shifting the marginal value of a unit, is what makes this OM rather than relabeled statistics.

## Referee-pushback patterns and the venue fix

- *"The model has no decision variable — it's just an equilibrium description."* → Introduce the operational lever (quantity, price, capacity, admission) the operator actually controls, and characterize how it responds to primitives.
- *"Assumptions are made only for tractability."* → State what each buys structurally and what relaxing it costs in the numerical study.
- *"This is an economics/marketing model in OM clothing."* → If no operational decision changes, return to `msom-topic-selection`; M&SOM gates on an operations lever, not a clever equilibrium.

## Output format

```
【Decision / objective / uncertainty】...
【Model class】newsvendor / MDP / queueing / stochastic-prog / game-theoretic — why
【Structural results】policy form / comparative statics / equilibrium ...
【Assumptions】binding ones flagged ...
【Operations centrality】confirmed ...
【Next step】msom-literature-positioning
```
