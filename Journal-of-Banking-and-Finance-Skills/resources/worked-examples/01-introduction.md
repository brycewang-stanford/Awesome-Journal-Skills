> **Illustrative teaching example.** The paper, bank, policy, and every number below are **fictional** and
> exist only to demonstrate *Journal of Banking & Finance* house style. No real-paper facts are stated, and
> no real bank or regulation is invoked. Corresponding skills:
> [`jbf-writing-style`](../../skills/jbf-writing-style/SKILL.md),
> [`jbf-topic-selection`](../../skills/jbf-topic-selection/SKILL.md),
> [`jbf-identification-strategy`](../../skills/jbf-identification-strategy/SKILL.md), and
> [`jbf-contribution-framing`](../../skills/jbf-contribution-framing/SKILL.md).

# Worked Example: A *Journal of Banking & Finance*-Style Introduction (before → after)

This demonstrates the introduction arc JBF rewards (from `jbf-writing-style` and `jbf-contribution-framing`):
**finance question → why it matters for banking/intermediation → data & identifying variation → headline
estimate with magnitude and interval → identification → economic mechanism → brief roadmap.** The governing
rule from `jbf-writing-style` is **lead with the finance question, not the method**, and **translate every
coefficient into economics** (basis points, loan spreads, capital ratios, default probabilities). Every
acronym is defined on first use so a referee from another finance subfield can follow.

**Illustrative paper (fictional):** *"Does a Higher Countercyclical Capital Buffer Tighten Small-Business
Credit? Evidence from a Staggered Regional Activation."* Fictional setting: a single banking system in which
a countercyclical capital buffer (CCyB — an add-on to required equity capital) is switched on region by
region over several years, with bank-region-quarter credit-register data.

---

## Before (buries the contribution — typical first-draft intro)

> The relationship between bank capital regulation and lending has been studied extensively in the banking
> literature. Many papers have examined how capital requirements affect credit supply, with mixed results.
> In this paper, we use a difference-in-differences design with bank and time fixed effects on a large
> credit-register dataset to study the effect of the countercyclical capital buffer on lending. We estimate
> several specifications and conduct a number of robustness checks. Our results contribute to the literature
> on bank capital and have implications for regulators and policymakers. Section 2 reviews the literature,
> Section 3 describes the data, Section 4 presents the methodology, Section 5 reports the results, and
> Section 6 concludes.

**What's wrong (against `jbf-writing-style` / `jbf-topic-selection` / `jbf-identification-strategy`):**

- **Leads with the method** ("we use a difference-in-differences design with bank and time fixed effects")
  instead of the finance question — the named anti-pattern in `jbf-writing-style`.
- **No headline estimate, no magnitude, no interval.** A referee cannot tell whether the buffer moved
  lending by 2 basis points or 200, or with what precision (fails the quantity-first / economic-magnitude
  test).
- **Identifying variation is invisible.** "Difference-in-differences" is asserted, but the reader never
  learns *what* the staggered activation compares or why it is plausibly exogenous to a bank's own loan
  demand (fails the `jbf-identification-strategy` "make the identifying variation visible" bar).
- **No economic mechanism.** It is unclear whether tighter credit runs through binding capital constraints,
  risk-weight reshuffling, or substitution to other lenders.
- **Throat-clearing** ("studied extensively," "mixed results," "implications for policymakers") and an
  **over-signposted roadmap** doing the work the argument should do.

---

## After (JBF arc — finance question + estimate + identification + mechanism, contribution early)

> **When a regulator raises the countercyclical capital buffer (CCyB) — an add-on to required bank equity —
> does the constrained bank pass the tightening through to small-business borrowers, or absorb it on its
> balance sheet?** Using a credit register in which the CCyB is activated region by region over six years,
> we estimate that a 1-percentage-point increase in a bank's required buffer reduces its small-business loan
> growth by **3.2 percentage points (95% CI 2.1–4.3)** over the following year, concentrated entirely in
> banks whose pre-activation capital surplus was below the system median. *(Finance question + headline
> estimate with magnitude and interval + where the effect lives, in the first breath; "CCyB" defined in
> place for a referee from another subfield.)*
>
> Identifying this effect is hard because a bank's capital position and its lending both respond to local
> economic conditions: a region where the buffer is switched on may also be a region where loan demand is
> already cooling, so a raw before-after lending drop would confound regulation with demand. *(Why it is
> hard — the endogeneity threat, stated in banking terms, per `jbf-identification-strategy`.)*
>
> We exploit the **staggered regional activation** of the buffer, comparing the same bank's lending in
> activated versus not-yet-activated regions in the same quarter, with bank-by-quarter and region-by-quarter
> fixed effects so that any system-wide shock, and any region-wide demand shock, is differenced out. The
> identifying variation is the *within-bank, within-quarter* difference in regulatory exposure created by
> the activation calendar; we report a heterogeneity-robust staggered difference-in-differences estimator
> and an event-study path showing no differential pre-trend, with standard errors clustered by region.
> *(Data and identifying variation in one paragraph; the design defeats the named threat, per
> `jbf-identification-strategy` and `jbf-data-analysis`.)*
>
> The contraction is a **capital-constraint** channel, not a demand artifact: the effect is present only in
> capital-thin banks, scales with how far the buffer pushes a bank below its internal target, and shows up
> as tighter loan *spreads and rejection rates* — not just lower volumes — while the same banks' lending in
> not-yet-activated regions is unchanged. A pure loan-demand story would imply a uniform effect across banks
> and no spread response; we observe the opposite. *(Economic mechanism named and adjudicated against the
> leading rival, per `jbf-contribution-framing`.)*
>
> Our contribution is to convert a much-debated regulatory question — does the CCyB bind on credit supply? —
> into a **clean within-bank credit-supply estimate with a stated magnitude and an isolated mechanism**,
> rather than a system-level correlation. This matters for banking and financial intermediation because it
> quantifies the small-business credit cost of a leading macroprudential tool and identifies *which* banks
> transmit it, informing buffer calibration. *(Contribution stated early, in intermediation terms, relative
> to a specific rival reading.)*
>
> The paper proceeds as follows. Section 2 describes the buffer's activation calendar and the credit
> register; Section 3 presents the staggered design and the heterogeneity-robust estimator; Section 4
> reports the lending, spread, and rejection results, the capital-surplus heterogeneity, and the mechanism
> and robustness checks. *(Brief roadmap — no over-signposting.)*

---

## Why the "after" meets the JBF bar

Mapped to the skill checklists:

- **Finance question leads, method follows** — the opening sentence is the economic question (does the
  buffer pass through to small-business credit?), and the estimator is introduced only where the design is
  described (`jbf-writing-style`: "lead with the finance question before the method").
- **Headline estimate is quantity-first with an interval** — the 3.2-pp reduction leads with its magnitude
  **and a 95% CI**, then is interpreted, and is later expressed in spreads and rejection rates rather than a
  bare coefficient (`jbf-writing-style` + `jbf-data-analysis`: translate coefficients into economics, report
  uncertainty).
- **Identifying variation is visible** — the within-bank, within-quarter contrast created by the staggered
  activation calendar is stated explicitly, with the fixed-effects structure that differences out the named
  confound (`jbf-identification-strategy`: "make the identifying variation visible").
- **The leading rival is named and adjudicated** — a loan-demand story would imply a uniform, spread-neutral
  effect; the capital-thin concentration and spread/rejection response are the opposite, satisfying the
  design-defense move (`jbf-identification-strategy` event-study / heterogeneity checks).
- **Mechanism is economic, not statistical** — the effect is tied to a capital-constraint channel that
  scales with the distance below the bank's target, the contribution type `jbf-contribution-framing` calls a
  mechanism claim, not a reduced-form sign.
- **Reads past the subfield** — CCyB and the buffer mechanics are defined on first use, and the payoff
  (macroprudential calibration, which banks transmit) speaks to any banking or intermediation referee,
  satisfying the `jbf-topic-selection` scope-fit test.

> Next: adapt the reproducible analysis skeleton in [`../code/`](../code/) when turning this introduction
> arc into a full empirical workflow, and stress-test the design against
> [`../../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md).
