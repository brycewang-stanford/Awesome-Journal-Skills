> **Illustrative teaching example.** The paper, dataset, and every number below are **fictional** and
> exist only to demonstrate *Journal of Applied Econometrics* house style. No real-paper facts are stated,
> and no real policy is invoked. Corresponding skills:
> [`jape-writing-style`](../../skills/jape-writing-style/SKILL.md),
> [`jape-contribution-framing`](../../skills/jape-contribution-framing/SKILL.md), and
> [`jape-identification-strategy`](../../skills/jape-identification-strategy/SKILL.md).

# Worked Example: A *Journal of Applied Econometrics*-Style Introduction (before → after)

This demonstrates the introduction arc the *Journal of Applied Econometrics* rewards (from
`jape-writing-style` and `jape-contribution-framing`): **applied question → why it is hard to identify on
real data → the estimand and the credible empirical strategy → the headline result with its uncertainty →
the diagnostics that test the identifying assumptions → why the finding is reproducible → short roadmap.**
The governing rule from `jape-contribution-framing` is that the contribution is an **application on real
data whose results are replicable** — not a pure-theory advance — and from `jape-writing-style` that it
must compress into a **≤100-word summary with no citations**. JAE rewards calibrated claims: a modest,
reproducible, honestly-bounded finding beats an over-claimed fragile one, and every diagnostic must be
**regeneratable from the code and data deposited in the JAE Data Archive**.

**Illustrative paper (fictional):** *"Pass-Through of a Fuel-Tax Change to Retail Prices: An ARDL
Bounds Approach with Station-Level Data."* Fictional setting: a single country's weekly station-level
retail fuel prices around a one-time excise-tax change, with wholesale cost and exchange-rate controls.

---

## Before (buries the contribution — typical first-draft intro)

> Tax pass-through has been studied extensively in public economics and industrial organization. Many
> papers estimate how taxes affect prices. In this paper we use an autoregressive distributed lag model
> to study the pass-through of a fuel-tax change to retail prices using a large dataset. We estimate
> several specifications and report the results. We also conduct robustness checks. Understanding tax
> pass-through is important for policymakers. Section 2 reviews the literature, Section 3 describes the
> data, Section 4 presents the methods, Section 5 reports results, and Section 6 concludes.

**What's wrong (against `jape-writing-style` / `jape-contribution-framing` / `jape-identification-strategy`):**

- **No estimand and no result on page one.** "Study the pass-through … report the results" never states
  *what* is estimated (short-run vs. long-run pass-through) or *what was found* — the
  `jape-contribution-framing` failure (a contribution is a finding, not an activity).
- **Leads with the method** ("we use an autoregressive distributed lag model") instead of the applied
  question and the design that identifies it — the `jape-writing-style` anti-pattern.
- **No identifying assumption and no test.** Pass-through is causal language; the draft never says what
  makes the tax change as-good-as-exogenous to retail margins, nor which diagnostic tests it
  (`jape-identification-strategy`: every assumption must map to a test you can deposit).
- **No uncertainty and no replicability hook.** "Report the results" with no interval and no mention of
  the JAE Data Archive — the venue's signature norm — left unaddressed.
- **Over-claim risk and throat-clearing** ("studied extensively," "important for policymakers") with an
  **over-signposted roadmap** doing the argument's work.

---

## After (*JAE* arc — applied question + estimand + credible design + reproducible result, early)

> **Does a fuel-excise increase pass through fully to the pump, and how fast?** Using weekly
> station-level retail prices around a one-time excise change, we estimate that **long-run pass-through is
> 0.83 (95% CI 0.74–0.92) — incomplete — and that 60% of it is realized within three weeks**, with the
> remainder accruing over the following two months. *(Applied question + the estimand — long-run and
> short-run pass-through — and the headline result with its interval, in the first breath.)*
>
> Identifying pass-through on real data is hard because the tax change coincides with movements in
> wholesale cost and the exchange rate, and retail margins are persistent, so a naïve before/after
> comparison conflates the tax with cost shocks and with the integration order of the price series, which
> is not known a priori. *(Why identification is hard, stated in applied terms — the
> `jape-identification-strategy` real-data framing.)*
>
> Our estimand is the long-run (level) pass-through coefficient and its short-run dynamics. We identify it
> with an **ARDL bounds specification** that remains valid whether the price, cost, and exchange-rate
> series are I(0), I(1), or mutually cointegrated, conditioning on wholesale cost and the exchange rate and
> absorbing station fixed effects; the identifying assumption is that, conditional on these controls, the
> timing of the excise change is unrelated to station-specific margin shocks. *(Estimand + credible design
> + the identifying assumption named, per `jape-identification-strategy`.)*
>
> We **test** that assumption rather than assert it: a bounds F-test confirms a level relationship; a
> placebo "tax change" at randomly assigned pre-period dates yields a pass-through indistinguishable from
> zero; the estimate is stable across lag lengths chosen by AIC and BIC and across alternative HAC and
> wild-cluster-bootstrap standard errors. *(Each identifying assumption mapped to a diagnostic — the
> `jape-identification-strategy` "every assumption has a test" requirement, and `jape-data-analysis`
> inference discipline.)*
>
> Our contribution is an **applied finding** — incomplete, gradual pass-through of this excise change to
> retail fuel prices, estimated under a design robust to unknown integration order — and it is
> **replicable**: the station-level data, the cleaning programs, and the estimation and placebo code are
> deposited in the JAE Data Archive, so every number above can be regenerated. *(Contribution framed as a
> calibrated, reproducible applied result — `jape-contribution-framing` + `jape-replication-and-data-policy`.)*
>
> Section 2 describes the data and institutional setting; Section 3 presents the ARDL design and the
> identification diagnostics; Section 4 reports pass-through and its robustness; Section 5 concludes.
> *(Brief roadmap — no over-signposting.)*

---

## Why the "after" meets the *Journal of Applied Econometrics* bar

Mapped to the skill checklists:

- **Estimand and finding front-loaded** — long-run pass-through 0.83 (95% CI 0.74–0.92) and its speed lead
  the introduction, with the applied question first, satisfying `jape-writing-style` (lead with the
  question and result, not the method) and `jape-contribution-framing` (the contribution is a finding).
- **Claim calibrated to the design** — "incomplete pass-through" is stated as a causal effect only because
  an identifying assumption is named *and tested*; the interval and the placebo bound the claim, the
  `jape-contribution-framing` "do not over-claim" rule.
- **Identification is on real data, with each assumption tested** — the no-confounding-with-cost-shocks
  assumption is checked by a placebo, the level relationship by a bounds F-test, robustness by lag and SE
  variation — the `jape-identification-strategy` "every assumption maps to a depositable test" standard.
- **Inference is matched to the design** — HAC and wild-cluster-bootstrap standard errors and an
  integration-order-robust specification, the `jape-data-analysis` discipline, rather than default OLS
  errors on persistent series.
- **Replicability carries weight** — the data, cleaning, estimation, and placebo code are deposited in the
  JAE Data Archive so every number regenerates, exactly the venue's signature norm
  (`jape-replication-and-data-policy`).
- **Method is demoted to a tool** — the ARDL specification appears where the design is described, never as
  the lead, and the prose would compress into a ≤100-word, citation-free summary (`jape-writing-style`).

> Next: adapt the reproducible analysis skeleton in [`../code/`](../code/) when turning this introduction
> arc into a full, archive-ready empirical workflow.
