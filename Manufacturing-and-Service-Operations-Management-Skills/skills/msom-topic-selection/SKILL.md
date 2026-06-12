---
name: msom-topic-selection
description: Use when shaping or stress-testing a research question for Manufacturing & Service Operations Management (M&SOM) — confirming an operations decision is central, choosing the analytical-vs-empirical lane, and matching the question to the right editorial Department before any modeling or data work begins.
---

# Topic Selection & M&SOM Fit (msom-topic-selection)

## When to trigger

- You have a problem idea but are unsure it belongs in M&SOM versus a general OR or strategy venue
- A senior co-author asks "where is the operations decision here?"
- You must pick which of the six editorial Departments your work targets
- You are deciding whether to pursue this as an analytical model or an empirical study

## The operations-centrality gate

M&SOM's defining screen is that an **operations decision or problem is central to the contribution**, not a backdrop. The journal covers the **design, procurement, production, delivery, and recovery of goods and services**. A strong analytics, pricing, marketing, or finance paper that merely *uses* an operational setting is routinely desk-screened. Before anything else, write one sentence: *"The operational decision is ___, the tradeoff is ___, and the operational lever is ___."* If you cannot, the topic is not yet M&SOM-ready.

## Choose the lane (and the journal will route by it)

M&SOM publishes **both** analytical/stochastic modeling (optimization, queueing, stochastic models, game theory, revenue management) **and** empirical OM / data-driven analytics. Pick the lane that the *decision* demands:

- **Analytical** when the contribution is a tractable model yielding structural insight about an operational policy (e.g., base-stock structure, threshold pricing, equilibrium contract).
- **Empirical** when the contribution is a credibly identified operational effect or a data-driven policy validated on real operations.

## Match to a Department (this is fit)

Map the question to one of the six departments — Manufacturing & Supply Chain Operations; Services, Platforms & Revenue Management; Environment, Health & Society; Operational Innovation; Analytics in OM; or the Practice Platform. A field-driven or practice-based study may target the Practice Platform; a thought-leadership perspective is an **OM Forum** piece (an identifying banner), not a standard research article. Your topic should clearly belong to one department, because the manuscript's fate hinges on that match.

## Checklist

- [ ] One-sentence operational decision / tradeoff / lever written
- [ ] Analytical vs. empirical lane chosen for principled reasons
- [ ] Target Department identified (and a sensible second choice)
- [ ] Managerial/operational "so what" stated in plain language
- [ ] Confirmed the OM core is the *primary* contribution, not an application backdrop

## Anti-patterns

- A pricing/finance/ML paper dressed in operations vocabulary with no real operational lever.
- "We apply method X to an operations dataset" with no operations decision improved.
- Targeting M&SOM generically without picking a department.


## Fit pass for Manufacturing & Service Operations Management

Run this as a concrete capability pass. First lock the process bottleneck, decision policy, queue/inventory/service mechanism, and implementation constraint; then test whether the manuscript addresses operations reviewers who look for service/manufacturing process insight, implementable policies, and operational performance evidence.

- **Primary move:** Score fit, novelty, evidence readiness, and audience ownership; reject prestige-only targeting when a sibling venue owns the contribution more directly.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against Management Science for broader OR/MS reach, Production and Operations Management for wider OM readership, Operations Research for method-first theory; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Fit screen before you commit (illustrative)

Vignette: a team has scanner data and wants to study whether a loyalty program raises sales — as stated, a marketing question that would be desk-screened. Reshaped it becomes fit: *does the program change the store's replenishment decision by making demand more forecastable, and what is the optimal safety-stock adjustment?* Now the lever (safety stock) and the tradeoff (holding cost vs. stockout) are central. The same reshaping rescues "does advertising raise demand?" (→ how does demand shaping change the inventory decision?) and "we apply deep learning to logistics data" (→ which staffing decision does it improve?).

## Referee-pushback patterns and the venue fix

- *"Strong paper, but the operations decision is a backdrop."* → Promote the operating lever to the primary contribution or re-route to a general OR/MS venue.
- *"Which department is this for?"* → Commit to one of the six departments at topic stage; an undeclared target reads as unfocused. Choose the lane the decision demands (structure to characterize, or an effect to identify), not the lane you are most comfortable in.

## Output format

```
【Operations decision】lever / tradeoff ...
【Lane】analytical / empirical — why ...
【Department】primary + second choice ...
【So-what】managerial implication ...
【Verdict】M&SOM-fit: yes / reshape / wrong venue
【Next step】msom-theory-development
```
