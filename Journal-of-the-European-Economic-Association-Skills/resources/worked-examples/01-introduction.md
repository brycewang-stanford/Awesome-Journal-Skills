> **Illustrative teaching example.** The paper, setting, model, and every number below are **fictional**
> and exist only to demonstrate Journal of the European Economic Association (JEEA) house style. No
> real-paper facts and no real policy are stated. Corresponding skills:
> [`jeea-writing-style`](../../skills/jeea-writing-style/SKILL.md),
> [`jeea-topic-selection`](../../skills/jeea-topic-selection/SKILL.md),
> [`jeea-literature-positioning`](../../skills/jeea-literature-positioning/SKILL.md), and
> [`jeea-identification`](../../skills/jeea-identification/SKILL.md).

# Worked Example: A JEEA-Style Introduction (before → after)

This demonstrates the **JEEA introduction arc** from
[`jeea-writing-style`](../../skills/jeea-writing-style/SKILL.md):
**question → why it is hard → approach (clean identification or a disciplined model) → headline result
(with a standard error / confidence set) → mechanism & interpretation → contribution & lesson → brief
roadmap.**

Two JEEA house rules drive the rewrite and distinguish it from a field-journal introduction:

- JEEA is the **EEA's general-interest journal** (published by Oxford University Press). A JEEA paper must make **both** the
  substantive economic question **and** the approach legible early to an economist outside the subfield
  ([`jeea-topic-selection`](../../skills/jeea-topic-selection/SKILL.md)). The lesson must **travel**.
- JEEA follows the modern-economics presentation discipline: **report point estimates with standard errors
  and confidence sets, not significance asterisks** — findings are written into the sentences
  ([`jeea-writing-style`](../../skills/jeea-writing-style/SKILL.md),
  [`jeea-identification`](../../skills/jeea-identification/SKILL.md)).

**Illustrative paper (fictional):** *"Commuting Costs and the Geography of Opportunity: Evidence from a
Regional Rail Expansion."* Fictional setting: a staggered roll-out of regional rail links across invented
metropolitan areas, used to estimate the effect of falling commuting costs on the employment of workers in
low-access neighborhoods, with a simple spatial-sorting model to interpret the magnitude. Every number is
invented.

---

## Before (buries the question under machinery — typical first-draft intro)

> We estimate a two-way fixed-effects regression of employment on a post-opening indicator interacted with
> treatment, controlling for area and year fixed effects and a vector of demographic covariates. Commuting
> has been studied extensively in urban economics. In this paper we exploit the opening of new rail links
> and find a positive and statistically significant effect on employment (significant at the 1% level,
> ***). Section 2 reviews the literature, Section 3 describes the data, Section 4 presents the empirical
> specification, Section 5 the results, and Section 6 concludes.

**What is wrong (against `jeea-writing-style` / `jeea-topic-selection` / `jeea-literature-positioning`):**

- **Leads with the estimator** ("two-way fixed-effects regression… post-opening indicator interacted with
  treatment") instead of the economic question — the named JEEA anti-pattern. Method-first framing reads as
  a field paper, not a general-interest one.
- **No economic question and no quantity on page one.** A general-interest co-editor cannot tell what is
  being measured, for whom, or why it matters broadly.
- **No headline estimate with units, and no uncertainty.** "Significant at the 1% level (\*\*\*)" is
  **exactly the asterisk reporting JEEA's house style avoids** — there is no point estimate, no standard
  error, no confidence set.
- **TWFE on staggered roll-out with no heterogeneity-bias discussion** — a `jeea-identification` Branch B
  red flag that a referee will raise immediately.
- **Throat-clearing** ("has been studied extensively") with vague stakes and no travel test.
- **Over-signposted roadmap** doing the work the argument should do.

---

## After (JEEA arc — question + approach + result-with-uncertainty, contribution early)

> **When a city makes it cheaper to get to work, who actually gets the jobs — and do the gains reach the
> neighborhoods that were cut off?** Using a staggered expansion of regional rail, we find that connecting
> a low-access neighborhood raises the employment rate of its residents by **3.1 percentage points (s.e.
> 0.6)** within three years, and that this gain is concentrated among workers who previously faced the
> longest commutes. *(question + headline quantity + its uncertainty + who benefits, in the first breath —
> no asterisks.)*
>
> Measuring this is hard because rail lines are **not built at random**: they tend to reach growing areas,
> so a naive before–after comparison confounds the transport effect with the growth that attracted the
> line. *(why it is hard — the identification obstacle stated plainly.)*
>
> We address this with the **staggered timing of openings across many areas**, estimating with a
> heterogeneity-robust difference-in-differences estimator rather than two-way fixed effects (which is
> biased under staggered adoption), and we show **flat pre-trends** in the event study before each opening.
> A simple spatial-sorting model interprets the magnitude: the employment gain equals the share of jobs
> brought within a reachable commute times the elasticity of labor supply to commute time. *(approach —
> credible design + a disciplined model to read the number;
> [`jeea-identification`](../../skills/jeea-identification/SKILL.md) Branch B and
> [`jeea-theory-model`](../../skills/jeea-theory-model/SKILL.md).)*
>
> The 3.1-point effect (s.e. 0.6) is stable across heterogeneity-robust estimators (Callaway–Sant'Anna and
> Sun–Abraham give **3.0 and 3.2**), survives wild-cluster inference with few treated areas, and is **zero
> for high-access neighborhoods** that the line did not newly connect — a placebo the design predicts. The
> model implies the effect operates through **reachable job access**, and a fictional counterfactual that
> halves headway (wait time) raises the gain to **4.0 points (s.e. 0.7)**. *(headline result restated with
> mechanism, robustness, and a placebo; [`jeea-robustness`](../../skills/jeea-robustness/SKILL.md).)*
>
> Our contribution is a **general-interest answer, not a transport case study**: cheaper commuting raises
> employment **specifically in the places that were excluded**, and the size of the gain is governed by how
> much *reachable job access* a connection creates — a quantity any city can compute. *(contribution framed
> as question + quantity + lesson; [`jeea-literature-positioning`](../../skills/jeea-literature-positioning/SKILL.md).)*
> The estimand is a local employment effect for newly connected low-access areas; we do **not** claim it
> transfers to already well-served cities, and the counterfactual assumes the sorting elasticity is stable.
> Beyond rail, the result implies that **place-based transport policy can be opportunity policy when it
> targets access, not just mobility** — relevant to spatial inequality debates well outside this setting.
> *(calibrated scope + broad lesson that travels.)*
>
> The paper proceeds as follows. Section 2 presents the access model that interprets the estimate; Section 3
> describes the roll-out and data; Section 4 reports the design, event study, and main effect; Section 5
> runs the headway counterfactual. *(brief roadmap — no over-signposting.)*

---

## Why the "after" meets the JEEA bar

Mapped to this pack's skill checklists:

- **First paragraph states the question + the quantity + its uncertainty + who benefits** — the 3.1-point
  effect (s.e. 0.6) appears immediately, with units and a standard error, never an asterisk
  ([`jeea-writing-style`](../../skills/jeea-writing-style/SKILL.md): "headline estimate appears early, with
  units and a standard error / confidence set"; "no significance asterisks").
- **The lesson travels** — a non-specialist sees a spatial-inequality result ("transport policy can be
  opportunity policy"), not a transport case study; this is the general-interest fit JEEA demands
  ([`jeea-topic-selection`](../../skills/jeea-topic-selection/SKILL.md)).
- **Identification is credible and named before the machinery** — staggered timing, a heterogeneity-robust
  estimator instead of biased TWFE, flat pre-trends, and a placebo, matching
  [`jeea-identification`](../../skills/jeea-identification/SKILL.md) Branch B.
- **A disciplined model reads the number** — the access model turns a reduced-form estimate into an
  interpretable mechanism and a counterfactual, the theory-and-empirics combination JEEA rewards
  ([`jeea-theory-model`](../../skills/jeea-theory-model/SKILL.md)).
- **Contribution is an answer with scope, not a method** — "cheaper commuting raises employment in excluded
  places," plus an explicit statement of what the estimand does **not** establish, satisfies
  [`jeea-literature-positioning`](../../skills/jeea-literature-positioning/SKILL.md) (question + quantity +
  lesson; calibrated claims).
- **Sibling check passes:** this is not a subfield-deep urban-transport piece for a field journal, and not
  an over-claimed top-5 swing — it is a general-interest result executed cleanly, JEEA's identity.

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified** JEEA papers
> across fields, [`../../skills/jeea-replication-package/SKILL.md`](../../skills/jeea-replication-package/SKILL.md)
> for building the package so it clears the JEEA Data Editor check, and [`../code/`](../code/) for a runnable
> empirical command chain. For the venue-neutral referee objections a staggered-DiD claim must pre-empt, see
> [`../../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md).
