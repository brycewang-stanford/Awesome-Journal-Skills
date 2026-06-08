> **Illustrative teaching example.** The paper, setting, and every number below are **fictional** and
> exist only to demonstrate *Marketing Science* house style. No real-paper facts are stated, and no real
> firm or policy is invoked. Corresponding skills:
> [`mksc-writing-style`](../../skills/mksc-writing-style/SKILL.md),
> [`mksc-topic-selection`](../../skills/mksc-topic-selection/SKILL.md),
> [`mksc-theory-development`](../../skills/mksc-theory-development/SKILL.md),
> [`mksc-literature-positioning`](../../skills/mksc-literature-positioning/SKILL.md), and
> [`mksc-contribution-framing`](../../skills/mksc-contribution-framing/SKILL.md).

# Worked Example: A *Marketing Science*-Style Introduction (before → after)

This demonstrates the introduction arc *Marketing Science* rewards (from `mksc-writing-style`,
`mksc-topic-selection`, and `mksc-contribution-framing`): **important marketing question → why a model is
needed → the model and its identification → the headline counterfactual/comparative-static result → the
managerial/substantive contribution → brief roadmap.** The governing rules: *Marketing Science* answers
marketing questions **with mathematical modeling**, so the lead is the **marketing decision and the
counterfactual a model can deliver**, not the estimator; intuition is **front-loaded before notation**
(`mksc-writing-style`); and the contribution is named on **one primary dimension** — substantive insight,
modeling, methodology, data, or practice (`mksc-contribution-framing`).

> **A note on genre.** *Marketing Science* spans **structural econometric** and **analytical
> (game-theoretic)** modeling, with reduced-form / experimental / ML evidence welcome when **disciplined by
> a model**. This example is a **structural demand-and-supply** paper with a field-experiment instrument; an
> analytical paper would swap the estimation for an equilibrium derivation and comparative statics, keeping
> the **same introduction discipline** (`mksc-methods`, `mksc-theory-development`). The econometric
> [`code/`](../code/) kit is the **evidentiary backbone** for the experimental variation, not the headline.

**Illustrative paper (fictional):** *"Personalized Free Shipping and the Cannibalization of Margin:
A Structural Model of Threshold Design."* Fictional setting: an online retailer that can set a
**personalized free-shipping threshold** (spend $X to ship free) per customer, and ran a randomized
threshold experiment to identify demand.

---

## Before (buries the contribution — typical first-draft intro)

> Free shipping is widely used in e-commerce and has attracted much attention. Many factors affect how
> consumers respond to shipping fees. In this paper, we estimate a random-coefficients logit demand model
> with a control function, using instruments from a field experiment, and we solve the retailer's pricing
> problem numerically. We estimate the model and report counterfactuals. Free shipping is important for
> retailers and consumers. Section 2 reviews the literature, Section 3 describes the data, Section 4
> presents the model, Section 5 reports results, and Section 6 concludes.

**What's wrong (against `mksc-writing-style` / `mksc-topic-selection` / `mksc-contribution-framing`):**

- **Leads with the estimator** ("we estimate a random-coefficients logit … with a control function")
  instead of the marketing decision and the counterfactual — the named anti-pattern in `mksc-writing-style`
  (front-load model intuition before notation).
- **No marketing question and no answer on page one.** A reader cannot tell what *decision* is at stake,
  what the model delivers that a regression cannot, or who should care (fails the `mksc-topic-selection`
  importance × modelability test).
- **No counterfactual stated.** *Marketing Science* topics imply a "what if the firm changes X?" payoff a
  model alone can answer; here it is invisible.
- **Contribution dimension unnamed** — is this a substantive pricing insight, a modeling advance, a method,
  or a data contribution? (the `mksc-contribution-framing` test).
- **Throat-clearing** ("widely used," "attracted much attention," "is important") and an
  **over-signposted** roadmap doing the argument's work.

---

## After (*Marketing Science* arc — marketing question + model + counterfactual + managerial contribution)

> **Should an online retailer personalize the free-shipping threshold — and if it does, does charging
> high-value customers a higher bar to "earn" free shipping lift basket size, or merely cannibalize the
> margin the retailer already had?** We build a structural model of basket-building demand in which a
> consumer's order size responds to a personalized shipping threshold, estimate it on a randomized
> threshold experiment, and use it to solve the retailer's **optimal personalized-threshold policy**. The
> headline counterfactual: optimal personalization raises retailer contribution margin by **4.8%** over a
> uniform threshold, but **62% of the naïve "incremental basket" gain is cannibalized** by orders that
> would have cleared a lower bar anyway. *(Marketing question + the model + the counterfactual the model
> delivers, in the first breath — with magnitudes.)*
>
> A model is necessary because the managerially interesting object — the *equilibrium* basket and margin
> under a threshold the retailer has never set — is a counterfactual no reduced-form elasticity recovers:
> raising the threshold both pushes some consumers to add items (the intended margin) and pushes others to
> abandon or to have qualified anyway (the cannibalization), and only a demand model that separates these
> consumers can net them. *(Why a model — the counterfactual/identification argument, in marketing terms;
> `mksc-theory-development`.)*
>
> We specify a random-coefficients model of order composition in which the shipping threshold enters the
> consumer's add-to-basket decision, and we identify the price/threshold sensitivities from a **field
> experiment that randomized the personalized threshold** across customers — exogenous variation in the
> exact marketing instrument we counterfactually re-optimize, with the experiment serving as the
> identifying backbone rather than the contribution itself. *(Model + identification from experimental
> variation in the instrument; the econometrics is the backbone — see [`../code/`](../code/) —
> `mksc-methods`.)*
>
> Re-optimizing the threshold customer-by-customer lifts contribution margin **4.8%** (vs. the uniform
> policy), but decomposing the gain shows only **38% is genuine incremental basket** while **62% is
> reclassification** of orders that would have shipped free anyway; the incremental share is concentrated
> among **price-sensitive, low-prior-spend** customers and is **negative** for the retailer's highest-value
> segment, for whom a higher bar suppresses orders. *(Headline restated as a decomposition with the segment
> signature — the comparative static that is the contribution.)*
>
> Our contribution is **substantive**: we show that personalized free-shipping thresholds are **mostly a
> margin-reclassification lever, not a basket-growth lever**, reversing the prevailing "personalize to grow
> baskets" intuition, and we characterize *when* personalization pays (price-sensitive, low-spend segments)
> and when it destroys value (high-value segments). *(Contribution on one primary dimension — a substantive
> pricing insight delivered by the model — stated relative to a specific rival reading;
> `mksc-contribution-framing`.)* For retailers, the managerial rule is that a personalized threshold should
> be **lowered, not raised, for high-value customers**, and the 62% cannibalization share is a direct
> caution against reading naïve uplift from a threshold A/B test as incremental margin. *(Managerial
> implication — the practice payoff *Marketing Science* asks of an applied paper.)*
>
> The paper proceeds as follows. Section 2 positions the model among the demand-estimation and
> shipping/pricing literatures; Section 3 presents the demand model and the experiment-based
> identification; Section 4 reports the optimal-threshold counterfactual and the cannibalization
> decomposition. *(Brief roadmap — no over-signposting.)*

---

## Why the "after" meets the *Marketing Science* bar

Mapped to the skill checklists:

- **Marketing question and counterfactual front-loaded** — by the end of the first paragraph the reader has
  the decision (personalize the threshold?), the model, and the counterfactual margin/cannibalization
  result, with magnitudes (`mksc-writing-style`: front-load intuition before notation;
  `mksc-topic-selection`: a counterfactual a model can answer).
- **Importance × modelability both shown** — a real retail pricing decision (importance) that *requires* a
  structural model to net basket-growth against cannibalization (modelability), the exact
  `mksc-topic-selection` two-gate test.
- **Identification stated in marketing terms before estimation** — the randomized threshold experiment
  supplies exogenous variation in the *instrument being re-optimized*, the `mksc-theory-development` /
  `mksc-methods` discipline ("which variation pins down each parameter, and why it is exogenous").
- **Contribution named on one primary dimension** — a **substantive** pricing insight (reclassification,
  not basket growth), with the modeling and field-experiment as support, satisfying
  `mksc-contribution-framing`'s "name the primary dimension."
- **The strongest rival is named and adjudicated** — the "personalize to grow baskets" account predicts a
  large incremental share; the decomposition shows 62% reclassification and a *negative* effect for
  high-value customers, the opposite signature (`mksc-literature-positioning` positions against the
  modeling precedent it overturns).
- **Method demoted to backbone** — the random-coefficients estimator and the [`code/`](../code/) chain
  appear only where identification is described; the headline is the marketing counterfactual, never the
  estimator (avoids the `mksc-writing-style` "lead with the method" anti-pattern).
- **Managerial implication delivered** — a concrete decision rule (lower the bar for high-value customers;
  distrust naïve A/B uplift), the practice payoff *Marketing Science* expects of an applied modeling paper.

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **verified real _Marketing Science_
> papers** whose front ends execute this discipline across analytical and structural genres, and
> [`../code/`](../code/) for the causal-inference command chain that serves as the evidentiary backbone
> here. For what counts as a contribution and how to name its primary dimension, see
> [`../../skills/mksc-contribution-framing/SKILL.md`](../../skills/mksc-contribution-framing/SKILL.md); for
> the shared, venue-neutral inference audit, see
> [`../../../shared-resources/empirical-methods/reporting-standards.md`](../../../shared-resources/empirical-methods/reporting-standards.md)
> and
> [`../../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md).
