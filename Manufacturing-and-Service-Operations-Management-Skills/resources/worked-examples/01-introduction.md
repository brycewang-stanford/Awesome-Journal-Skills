> **Illustrative teaching example.** The paper, setting, and every number below are **fictional** and
> exist only to demonstrate M&SOM house style. No real-paper facts are stated, and no policy is invented.
> Corresponding skills:
> [`msom-writing-style`](../../skills/msom-writing-style/SKILL.md),
> [`msom-contribution-framing`](../../skills/msom-contribution-framing/SKILL.md), and
> [`msom-topic-selection`](../../skills/msom-topic-selection/SKILL.md).

# Worked Example: An M&SOM-Style Introduction (before → after)

This demonstrates the **M&SOM introduction arc** from `msom-writing-style` and
`msom-contribution-framing`: **operational problem → the decision and its tradeoff → why it is hard →
model/data → the structure of the result → managerial implication (the operational lever) → brief
roadmap** — with the M&SOM rule that the introduction **states the operational problem, the decision,
and the insight in words before any notation**, and that the contribution is gated on an **operations
decision being central**, not a method novelty.

**Illustrative paper (fictional):** *"When to Hold the Door: A Threshold Dispatching Policy for
Same-Day Delivery Vans."* Fictional setting: a same-day grocery operator deciding, in real time,
whether to dispatch a partially loaded delivery van now or hold it briefly to consolidate the next
arriving order. This is an analytical (stochastic-modeling) M&SOM paper; an empirical variant is noted
at the end.

---

## Before (buries the operational insight under the model — typical first-draft intro)

> We study a continuous-time Markov decision process with state \((n, \tau)\) denoting the number of
> loaded parcels and elapsed holding time, and we characterize the optimal stopping policy. Let
> \(\lambda\) be the order arrival rate and \(c(\cdot)\) the convex holding-cost function. We prove that
> the value function is submodular and derive the Bellman equation in Section 3. Dispatching has been
> studied extensively in the transportation and queueing literature. We solve the MDP numerically and
> report results. Section 2 reviews the literature, Section 3 presents the model, Section 4 derives the
> structural results, Section 5 reports the numerical study, and Section 6 concludes.

**What's wrong (against `msom-writing-style` / `msom-contribution-framing` / `msom-topic-selection`):**

- **Theorem-first / notation-first.** Opens with the MDP state space and the Bellman equation before
  the reader knows what operational decision is at stake — a named anti-pattern in `msom-writing-style`
  ("a theorem-first introduction with no plain-language operational insight").
- **The operations decision is implicit.** A Department Editor cannot tell, on page one, *what
  operational lever a manager would pull* — failing the operations-centrality gate in
  `msom-topic-selection`.
- **No managerial implication.** Nothing states the "so what for operations," which
  `msom-contribution-framing` makes a required, sectioned deliverable.
- **Contribution framed as solving a model** ("we characterize the optimal stopping policy"), not as
  changing an operational decision.
- **Throat-clearing** ("has been studied extensively") and an **over-signposted roadmap** doing the
  argument's work.

---

## After (M&SOM arc — operational decision first, then the policy structure, then the lever)

> **A same-day delivery operator must decide, every time a van is partly loaded, whether to dispatch it
> now or hold it briefly so the next order can ride along — trading the waiting cost of orders already
> on board against the routing savings from consolidation.** We show that the cost-minimizing rule is a
> simple **state-dependent holding threshold**: dispatch as soon as the number of loaded parcels reaches
> a cutoff that *falls* as orders age and *rises* with the order-arrival rate. *(operational problem +
> the decision + its tradeoff + the shape of the answer, in plain words, before any notation.)*
>
> Getting this right is hard because the two costs pull in opposite directions and both depend on a
> demand process the dispatcher observes only as it unfolds: hold too long and loaded orders breach
> their promised windows; dispatch too eagerly and vans leave half-empty, raising cost per drop.
> *(why it is hard — the operational tradeoff, not a technical obstacle.)*
>
> We model dispatching as a stochastic control problem in which orders arrive randomly and holding is
> penalized by a convex delay cost, and we characterize the structure of the optimal policy. *(model
> demoted to one sentence; the method is a tool, not the lead.)*
>
> The optimal policy is a **threshold on loaded parcels that is monotone in elapsed holding time and in
> the arrival rate** — so it can be implemented as a lookup table the dispatch system evaluates in
> constant time, with no re-optimization. In a numerical study calibrated to a fictional metro grocery
> operation, the threshold rule recovers most of the consolidation savings of a fully dynamic policy
> while never violating a delivery promise. *(the result stated as policy structure and comparative
> statics a manager can act on — `msom-contribution-framing`'s analytical-contribution form.)*
>
> Our contribution is to convert real-time dispatching from an intractable case-by-case optimization
> into **one operational rule a dispatcher can follow by hand: hold until parcels-on-board reach a
> posted, age-adjusted cutoff.** The managerial implication is concrete — the operator tunes a single
> threshold table rather than a black-box optimizer, and the comparative statics say exactly how to
> retune it when demand speeds up (raise the cutoffs) or promise windows tighten (lower them). *(the
> managerial lever named explicitly — the required Managerial-implications content.)*
>
> The paper proceeds as follows. Section 2 sets up the dispatching model; Section 3 establishes the
> threshold structure and its comparative statics; Section 4 reports the calibrated numerical study.
> *(brief roadmap — no over-signposting.)*

---

## The structured abstract (M&SOM's required sections)

`msom-writing-style` and `msom-contribution-framing` require a **structured abstract, ≤ 300 words,
free of technical jargon**, with three required sections. For the fictional paper:

- **Problem definition.** A same-day delivery operator must repeatedly decide whether to dispatch a
  partly loaded van now or hold it to consolidate the next order, trading delay cost against routing
  savings.
- **Methodology-results.** We model the decision as a stochastic control problem with random order
  arrivals and a convex holding-cost penalty, characterize the optimal policy analytically, and show in a
  calibrated numerical study that the resulting threshold captures most of the savings of a fully
  dynamic policy without breaching delivery promises.
- **Managerial implications.** Operators can run real-time dispatching as a posted, age-adjusted cutoff
  table — tuning one threshold rather than re-optimizing — and the comparative statics prescribe how to
  retune it as demand or service promises change.

> See [`../official-source-map.md`](../official-source-map.md) for the 2026-06-20 author-guideline source
> behind the structured-abstract headings.

---

## Why the "after" meets the M&SOM bar

Mapped to the skill checklists:

- **Operational problem, decision, and insight stated in words before notation** — the
  `msom-writing-style` rule; the state space and Bellman equation never appear in the intro.
- **Operations decision is central and explicit** — "dispatch now or hold" is the gate
  (`msom-topic-selection`: write the one sentence "the operational decision is ___, the tradeoff is ___,
  the lever is ___"); here all three brackets are filled.
- **Contribution is policy structure + actionable comparative statics**, not "we solve an MDP"
  (`msom-contribution-framing` analytical-contribution form), and the **managerial implication names a
  concrete lever** (a tunable threshold table).
- **Method is demoted to a tool**, mentioned once where the model is introduced, never as the lead —
  avoiding the theorem-first anti-pattern.
- **Department routing is clear** — this is a Manufacturing & Supply Chain / Services-and-platforms
  dispatching problem, so the contribution can be framed in that Department's vocabulary
  (`msom-contribution-framing`).

**Empirical variant (same gate).** Had this been an empirical paper — e.g., estimating, from dispatch
logs, how a holding rule changes on-time rates — the arc is identical: lead with the operational
decision, state a **credibly identified operational effect**, and name the **policy it implies**, not
the estimator. The shared identification and reporting discipline lives in the cross-pack hub:
[`../../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md)
and
[`../../../shared-resources/empirical-methods/reporting-standards.md`](../../../shared-resources/empirical-methods/reporting-standards.md).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for real, web-verified M&SOM papers
> whose introductions lead with the operational decision, and [`../code/`](../code/) for the empirical
> command chain referenced in the empirical variant.
