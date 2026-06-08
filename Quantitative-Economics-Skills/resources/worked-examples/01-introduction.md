> **Illustrative teaching example.** The paper, setting, model, and every number below are **fictional**
> and exist only to demonstrate Quantitative Economics (QE) house style. No real-paper facts and no real
> policy are stated. Corresponding skills:
> [`qe-writing-style`](../../skills/qe-writing-style/SKILL.md),
> [`qe-topic-selection`](../../skills/qe-topic-selection/SKILL.md),
> [`qe-contribution-framing`](../../skills/qe-contribution-framing/SKILL.md), and
> [`qe-identification-strategy`](../../skills/qe-identification-strategy/SKILL.md).

# Worked Example: A QE-Style Introduction (before → after)

This demonstrates the **QE introduction arc** from
[`qe-writing-style`](../../skills/qe-writing-style/SKILL.md):
**question → why it is hard quantitatively → approach (data + model/estimator) → headline result (with a
standard error / coverage set) → mechanism & interpretation → contribution & lesson → brief roadmap.**

Two QE house rules drive the rewrite and distinguish it from a general-interest empirics journal:

- QE is the **Econometric Society's** empirically/quantitatively oriented, **open-access** journal, sister
  to *Econometrica* (method-first) and *Theoretical Economics* (pure theory). A QE paper must make **both**
  the substantive economic question **and** the quantitative apparatus legible early
  ([`qe-topic-selection`](../../skills/qe-topic-selection/SKILL.md)).
- QE **forbids significance asterisks and boldface for significance** — findings are communicated through
  **point estimates with standard errors and confidence/coverage sets** written into the sentences
  ([`qe-writing-style`](../../skills/qe-writing-style/SKILL.md),
  [`qe-identification-strategy`](../../skills/qe-identification-strategy/SKILL.md)). The abstract is
  ≤150 words.

**Illustrative paper (fictional):** *"Search Frictions and the Pass-Through of Input Costs: A Structural
Estimation of Retail Price Setting."* Fictional setting: a structural model of retail price-setting under
costly consumer search, estimated by simulated method of moments (MSM) on invented scanner-style data,
then used for a fictional cost-shock counterfactual. Every magnitude is invented.

---

## Before (buries the question under machinery — typical first-draft intro)

> We estimate a structural model of price setting. The model is solved by value-function iteration on a
> grid and estimated by simulated method of moments using a two-step optimal weighting matrix; we use
> 200 simulation draws and a multi-start Nelder–Mead routine. Price-setting under imperfect information
> has been studied extensively. In this paper we match a set of moments and recover the structural
> parameters, then we run a counterfactual. The estimated pass-through elasticity is significant at the
> 1% level (***). Section 2 reviews the literature, Section 3 presents the model, Section 4 the
> estimation, Section 5 the results, and Section 6 concludes.

**What is wrong (against `qe-writing-style` / `qe-topic-selection` / `qe-contribution-framing`):**

- **Leads with the solver and the estimator** ("value-function iteration… simulated method of moments…
  optimal weighting matrix") instead of the economic question — the named QE anti-pattern ("leading the
  intro with the estimator"). Method-first framing reads as *Econometrica*, not QE.
- **No economic question and no quantity on page one.** A general-interest Econometric Society reader
  cannot tell what is being measured or why it matters.
- **No headline estimate with units, and no uncertainty.** "Significant at the 1% level (\*\*\*)" is
  **exactly the asterisk reporting QE forbids** — there is no point estimate, no standard error, no
  coverage set.
- **Throat-clearing** ("has been studied extensively") with vague stakes.
- **Contribution is machinery, not an answer** ("we match a set of moments… run a counterfactual"), with
  no lesson that travels beyond the setting.
- **Over-signposted roadmap** doing the work the argument should do.

---

## After (QE arc — question + quantitative approach + result-with-uncertainty, contribution early)

> **When an input cost rises, how much of it reaches consumers as higher prices — and how much is absorbed
> because shoppers can search across sellers?** We estimate a structural model of retail price-setting in
> which consumers search at a cost, and find that a 10% input-cost increase raises retail prices by
> **6.2% (s.e. 0.7)** in the long run, so roughly a **third of the shock is absorbed** by the search
> friction rather than passed to consumers. *(question + headline quantity + its uncertainty + why it
> matters, in the first breath — no asterisks.)*
>
> Measuring this is hard because pass-through and search intensity are **jointly determined**: the same
> demand conditions that let firms raise prices also change how hard consumers look, so a reduced-form
> price-on-cost regression cannot separate the markup channel from the search channel. *(why it is hard —
> here the obstacle is identification of structural parameters, not a clean experiment.)*
>
> We resolve this with a model whose parameters are **tied to specific data features**: the search-cost
> distribution is identified by the dispersion of prices for identical goods across sellers, and the
> pass-through elasticity by the covariance of prices with a plausibly cost-only component of marginal
> cost. We estimate by simulated method of moments, validate parameter recovery on simulated data
> (Monte Carlo), and report **sensitivity of each estimate to the moments that move it**. *(approach —
> data + model + what identifies the parameters — in one paragraph;
> [`qe-identification-strategy`](../../skills/qe-identification-strategy/SKILL.md) Branch A.)*
>
> Long-run pass-through is **6.2% (s.e. 0.7)** for a 10% cost shock, the model fits the targeted price-
> dispersion moments and an **untargeted** moment (the speed of price adjustment) it was not asked to
> match, and the estimated search cost implies the median shopper compares **2.3 (90% coverage set
> [1.9, 2.8])** sellers. A fictional counterfactual that halves search costs lowers pass-through to
> **4.1% (s.e. 0.6)**. *(headline result restated with mechanism and uncertainty; a counterfactual the
> structure delivers that a reduced-form design cannot.)*
>
> Our contribution is a **quantitative answer, not an estimator**: using a search-based structural model
> we measure how much of an input-cost shock consumers actually bear, and show the absorbed share is
> governed by a **search friction we can estimate from price dispersion alone**. This reframes incomplete
> pass-through as **partly a consumer-search phenomenon**, not solely a markup-adjustment one.
> *(contribution framed as question + quantity + lesson, with scope;
> [`qe-contribution-framing`](../../skills/qe-contribution-framing/SKILL.md).)* The estimand is a long-run
> elasticity for this market and cost type; we do **not** claim it transfers to markets without comparable
> price dispersion, and the counterfactual assumes the estimated parameters are policy-invariant. Beyond
> retail, the result implies that **wherever consumers can cheaply compare sellers, measured pass-through
> understates the underlying cost shock** — relevant to inflation accounting and to how cost pressures
> propagate through any search-intensive market. *(calibrated scope + broad lesson.)*
>
> The paper proceeds as follows. Section 2 presents the model; Section 3 describes the data and the
> moments that identify each parameter; Section 4 reports estimates, fit, and sensitivity; Section 5 runs
> the cost-shock counterfactual. *(brief roadmap — no over-signposting.)*

---

## Why the "after" meets the QE bar

Mapped to this pack's skill checklists:

- **First paragraph states the economic question + the quantity + its uncertainty** — the headline
  elasticity (6.2%, s.e. 0.7) appears immediately, with units and a standard error, never an asterisk
  ([`qe-writing-style`](../../skills/qe-writing-style/SKILL.md): "headline estimate appears early in the
  intro, with units and a standard error / coverage set"; "no significance asterisks").
- **Both the substance and the apparatus are legible early** — a non-specialist sees the pass-through
  question; a quantitative reader sees the structural model and MSM. This is the QE sweet spot where
  "method and answer reinforce each other," not a toy application of an estimator
  ([`qe-topic-selection`](../../skills/qe-topic-selection/SKILL.md)).
- **Identification is named before the machinery** — each parameter is tied to a data feature
  (price dispersion → search costs; cost-only marginal-cost variation → pass-through), with Monte Carlo
  recovery and moment-sensitivity reported, matching
  [`qe-identification-strategy`](../../skills/qe-identification-strategy/SKILL.md) Branch A ("name what
  identifies each parameter," "sensitivity / informativeness," "Monte Carlo recovery").
- **Contribution is an answer with scope, not a method** — "we measure how much consumers bear," plus an
  explicit statement of what the estimand does **not** establish, satisfies
  [`qe-contribution-framing`](../../skills/qe-contribution-framing/SKILL.md) (question + quantity + lesson;
  calibrated claims; "why QE, not Econometrica").
- **A counterfactual only the structure delivers** — halving search costs lowers pass-through — is the
  payoff QE rewards in structural work, with uncertainty carried into the counterfactual quantity.
- **Sibling check passes:** this is not a new estimator with a toy application (*Econometrica*) and not
  pure theory (*Theoretical Economics*); it is a quantitative method answering a substantive question
  — QE's identity.

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified** QE papers whose
> introductions execute this arc, [`../../skills/qe-data-analysis/SKILL.md`](../../skills/qe-data-analysis/SKILL.md)
> for building the estimation so it clears the ES Data Editor reproducibility check, and
> [`../code/`](../code/) for a runnable empirical command chain. For the venue-neutral referee objections
> a structural pass-through claim must pre-empt, see
> [`../../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md).
