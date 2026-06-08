> **Illustrative teaching example.** The paper, market, merger, and every number below are **fictional**
> and exist only to demonstrate *The RAND Journal of Economics* (RJE) house style. No real-paper facts are
> stated, and no real firm or transaction is invoked. Corresponding skills:
> [`rje-writing-style`](../../skills/rje-writing-style/SKILL.md),
> [`rje-contribution-framing`](../../skills/rje-contribution-framing/SKILL.md), and
> [`rje-identification-strategy`](../../skills/rje-identification-strategy/SKILL.md).

# Worked Example: A *RAND Journal of Economics*-Style Introduction (before → after)

This demonstrates the introduction arc RJE rewards (from `rje-writing-style` and `rje-contribution-framing`):
**market and strategic problem → the IO advance → the method that earns it → headline causal/structural
estimate with magnitude and interval → the competition / regulation / welfare lesson → brief roadmap.**
Because RJE applies a **fast editor screen before refereeing** and enforces **hard page caps**, the
contribution must be **legible on page one** and unmistakably **industrial-organization** (not a
general-economics result). Per the house Style Guide, the manuscript is an "article" (not a "paper"), uses
**because/as** for causation, and defines its market primitives early. Jargon (markup, conduct,
counterfactual) is defined on first use.

**Illustrative paper (fictional):** *"Markups and Merger Effects in a Differentiated Retail-Fuel Market."*
Fictional setting: a regional retail-gasoline market with station-level prices and volumes, in which two of
the larger chains propose to merge.

---

## Before (buries the contribution — typical first-draft intro)

> The effects of mergers have been studied extensively in industrial organization. Many papers estimate
> demand and use the estimates to analyze market power. In this paper, we estimate a demand model for retail
> gasoline and simulate a merger. We use a logit demand system and recover marginal costs. We then compute
> counterfactual prices. The results are interesting for competition policy. Section 2 reviews the
> literature, Section 3 describes the data, Section 4 presents the model, Section 5 reports results, and
> Section 6 concludes.

**What's wrong (against `rje-writing-style` / `rje-contribution-framing` / `rje-identification-strategy`):**

- **Leads with a literature gesture and the method**, not the market and the strategic problem — fatal under
  RJE's fast editor screen, where the IO advance must be legible on page one (`rje-contribution-framing`).
- **No headline estimate, magnitude, or uncertainty**, and no competition/welfare number.
- **Demand is asserted as "logit" with no word on price endogeneity** — the central identification threat in
  structural demand (`rje-identification-strategy` Branch A) is invisible.
- **Conduct is never stated** — the merger simulation's maintained competitive assumption (Bertrand?
  Cournot?) is left implicit, which RJE referees will not accept.
- **Vague payoff** ("interesting for competition policy") and an **over-signposted roadmap** burning scarce
  page budget.

---

## After (RJE arc — market + structural estimate + competition lesson, contribution on page one)

> **When two retail-fuel chains in a concentrated regional market merge, how much do prices rise, and is the
> increase driven by lost competition or by merger-specific cost savings?** Estimating a random-coefficients
> demand system for station-level gasoline and recovering marginal costs from the **Bertrand pricing
> first-order conditions**, we find median own-price elasticities of **−4.1** and station-level markups of
> **18%**, and we simulate that the proposed merger raises retail prices by **2.7% (90% CI 1.9–3.6)** absent
> efficiencies — an increase fully offset only if the merger lowers marginal cost by at least **3.1%**.
> *(Market and strategic problem + the structural estimates + the headline counterfactual with magnitude and
> interval + the competition lesson, on page one; "markup" and "conduct" are defined in place.)*
>
> Estimating this requires confronting **price endogeneity** — stations with unobservably better locations
> charge more and sell more — which biases naive demand estimates toward inelasticity and would understate
> the merger's price effect. *(The central identification threat, stated in market terms.)*
>
> We instrument price with **cost shifters (wholesale rack prices and local tax differences) and the
> characteristics of rival stations**, argue their validity from the institutions of fuel retailing, and
> recover demand and then marginal costs under Bertrand–Nash conduct, which we **test rather than assume**
> against a pass-through restriction the data can reject. *(Identifying variation — the instruments — and the
> conduct assumption made explicit and tested, per `rje-identification-strategy` Branches A–B.)*
>
> The recovered markups are largest for stations with the fewest nearby rivals, and the simulated merger
> price effect is concentrated in **local markets where the merging chains are each other's closest
> competitor** — the diversion-ratio signature a unilateral-effects theory of harm predicts. *(Headline
> result restated with the cross-market signature that distinguishes the mechanism.)*
>
> Our contribution is a **credible, model-disciplined estimate of unilateral merger effects** in this market,
> together with the **break-even efficiency** an antitrust authority would need to clear it — a number that
> maps the structural estimates straight onto the merger-review decision. *(Contribution stated on page one,
> mapped to a competition-policy lever, per `rje-contribution-framing`.)* We are explicit about scope: the
> counterfactual holds the product set and conduct fixed and is reported as a range under those maintained
> assumptions, not as a universal law of fuel mergers. *(Scope and counterfactual honesty, per
> `rje-data-analysis`.)*
>
> The article proceeds as follows. Section 2 sets out the demand and supply model and the conduct test;
> Section 3 describes the station-level data and instruments; Section 4 reports elasticities, markups, the
> merger counterfactual, and its sensitivity to conduct and the efficiency assumption. *(Brief roadmap — no
> over-signposting, respecting the page cap.)*

---

## Why the "after" meets the RJE bar

Mapped to the skill checklists:

- **IO contribution legible on page one** — the first paragraph names the market, the strategic problem
  (merger), the method, and the competition lesson, surviving RJE's fast editor screen
  (`rje-contribution-framing`).
- **Structural estimates with uncertainty** — elasticities, markups, and the **merger price effect with a
  90% interval** lead, then are interpreted, per `rje-data-analysis`.
- **Price endogeneity confronted** — instruments are named and argued in market terms, the
  `rje-identification-strategy` Branch A requirement, rather than assuming exogenous prices.
- **Conduct is explicit and tested** — Bertrand–Nash is stated and *tested* against a rejectable
  restriction, not assumed, satisfying Branch B and the IO referee norm.
- **Counterfactual is disciplined and bounded** — the merger simulation states its maintained assumptions
  (fixed product set, conduct) and reports a range plus a break-even efficiency, per `rje-data-analysis`.
- **House style respected** — the manuscript calls itself an "article," uses **because/as** for causation,
  and keeps the intro within page-cap discipline, per `rje-writing-style`.

> Next: adapt the reproducible analysis skeleton in [`../code/`](../code/) when turning this introduction
> arc into a full empirical workflow, and stress-test the design against
> [`../../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md).
