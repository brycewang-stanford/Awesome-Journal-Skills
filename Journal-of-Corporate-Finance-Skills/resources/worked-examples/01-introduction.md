> **Illustrative teaching example.** The paper, firms, reform, and every number below are **fictional** and
> exist only to demonstrate *Journal of Corporate Finance* house style. No real-paper facts are stated, and
> no real firm or law is invoked. Corresponding skills:
> [`jcf-writing-style`](../../skills/jcf-writing-style/SKILL.md),
> [`jcf-topic-selection`](../../skills/jcf-topic-selection/SKILL.md),
> [`jcf-identification-strategy`](../../skills/jcf-identification-strategy/SKILL.md), and
> [`jcf-contribution-framing`](../../skills/jcf-contribution-framing/SKILL.md).

# Worked Example: A *Journal of Corporate Finance*-Style Introduction (before → after)

This demonstrates the introduction arc JCF rewards (from `jcf-writing-style` and `jcf-contribution-framing`):
**corporate-finance question → why it matters → data & identifying variation → headline estimate with
magnitude and interval → identification → economic mechanism → brief roadmap.** The governing rule from
`jcf-writing-style` is **lead with the corporate-finance question, not the method**, and **translate every
coefficient into economics** (firm value, leverage, investment, payout, basis points). Every acronym is
defined on first use so a desk editor and a referee from another corporate-finance subfield can follow.

**Illustrative paper (fictional):** *"Does Mandatory Board Independence Curb Value-Destroying Acquisitions?
Evidence from a Listing-Rule Threshold."* Fictional setting: a listing rule that requires a majority of
independent directors only for firms above a market-capitalization cutoff, creating a regression-
discontinuity (RDD) contrast around the threshold, with firm-level acquisition and accounting data.

---

## Before (buries the contribution — typical first-draft intro)

> Corporate governance and acquisitions have been widely studied in the corporate finance literature. Prior
> work has examined whether board independence affects firm outcomes, with mixed evidence. In this paper, we
> use a regression discontinuity design around a market-capitalization threshold to study the effect of
> mandatory board independence on acquisition activity. We run several specifications and robustness checks.
> Our findings contribute to the governance literature and have implications for regulators and boards.
> Section 2 reviews the literature, Section 3 describes the data, Section 4 presents the methodology, Section
> 5 reports results, and Section 6 concludes.

**What's wrong (against `jcf-writing-style` / `jcf-topic-selection` / `jcf-identification-strategy`):**

- **Leads with the method** ("we use a regression discontinuity design around a market-capitalization
  threshold") instead of the corporate-finance question — the named anti-pattern in `jcf-writing-style`.
- **No headline estimate, no magnitude, no interval.** A referee cannot tell whether mandated independence
  moved acquirer announcement returns by 10 basis points or 5 percentage points, or with what precision.
- **Identifying variation is invisible.** "RDD" is asserted, but the reader never learns *what* the cutoff
  compares or why firms just above and just below it are otherwise similar (fails the
  `jcf-identification-strategy` bar of making the identifying variation visible and defending continuity).
- **No economic mechanism.** It is unclear whether mandated independents block bad deals ex ante, improve
  deal selection, or merely change post-deal disclosure.
- **Throat-clearing** ("widely studied," "mixed evidence," "implications for regulators") and an
  **over-signposted roadmap** doing the work the argument should do.

---

## After (JCF arc — corporate-finance question + estimate + identification + mechanism, contribution early)

> **When a listing rule forces a firm to seat a majority of independent directors, do those directors
> actually stop value-destroying acquisitions — or just reshape disclosure around deals that happen anyway?**
> Exploiting a rule that mandates board-majority independence only above a market-capitalization cutoff, we
> estimate that crossing the threshold raises three-day acquirer announcement returns on subsequent deals by
> **1.8 percentage points (95% CI 0.9–2.7)** and cuts the probability of a diversifying acquisition by about
> a third, with no discontinuity in firm characteristics at the cutoff. *(Corporate-finance question +
> headline estimate with magnitude and interval + the design's identifying contrast, in the first breath;
> "diversifying acquisition" defined in place.)*
>
> Identifying this effect is hard because board independence is chosen, not assigned: firms that seat more
> independent directors differ in size, ownership, and prior performance, so a cross-sectional comparison of
> independent versus insider boards confounds governance with the traits that produced it. *(Why it is hard
> — the endogeneity of governance, stated in corporate-finance terms, per `jcf-identification-strategy`.)*
>
> We use the **listing-rule threshold** as a regression discontinuity: firms whose market capitalization
> falls just above the cutoff face the independence mandate, while otherwise-similar firms just below it do
> not, and treatment status changes sharply at a value the firm cannot precisely manipulate. We show
> covariate smoothness through the cutoff, no bunching in the running variable (a manipulation test), and a
> first stage in which board independence jumps discontinuously at the threshold, then estimate local-linear
> effects with bias-corrected robust confidence intervals and a donut-hole check. *(Data and identifying
> variation in one paragraph; continuity and manipulation defended, per `jcf-identification-strategy` and
> `jcf-data-analysis`.)*
>
> The improvement works through **ex-ante deal selection**, not cosmetic disclosure: above the threshold,
> firms announce fewer diversifying and fewer low-synergy deals, the announcement-return gain is
> concentrated in firms with weak pre-mandate monitoring, and post-deal operating performance rises in step
> — while deal frequency for plainly value-accretive acquisitions is unchanged. A disclosure-only story
> would leave the deal mix and operating outcomes untouched; we observe the opposite. *(Economic mechanism
> named and adjudicated against the leading rival, per `jcf-contribution-framing`.)*
>
> Our contribution is to convert a long-debated governance question — does mandated independence improve
> acquisition decisions? — into a **clean threshold-identified estimate with a stated magnitude and an
> isolated channel (deal selection)**, rather than a governance–performance correlation. This matters for
> corporate finance because it quantifies the acquisition-quality return to a widely used governance mandate
> and shows *which* firms benefit, informing both regulators and boards. *(Contribution stated early, in
> corporate-finance terms, relative to a specific rival reading.)*
>
> The paper proceeds as follows. Section 2 describes the listing rule and the acquisition sample; Section 3
> presents the RDD, the manipulation and smoothness tests, and the first stage; Section 4 reports the
> announcement-return and deal-mix results, the monitoring heterogeneity, and the mechanism and robustness
> checks. *(Brief roadmap — no over-signposting.)*

---

## Why the "after" meets the JCF bar

Mapped to the skill checklists:

- **Corporate-finance question leads, method follows** — the opening sentence is the economic question (does
  mandated independence stop bad deals?), and the estimator appears only where the design is described
  (`jcf-writing-style`: lead with the question, not the method).
- **Headline estimate is quantity-first with an interval** — the 1.8-pp announcement-return gain leads with
  its magnitude **and a 95% CI**, then is interpreted, and is paired with the deal-probability effect rather
  than a bare coefficient (`jcf-writing-style` + `jcf-data-analysis`: translate coefficients into economics,
  report uncertainty).
- **Identifying variation is visible and defended** — the threshold contrast, covariate smoothness, the
  manipulation (no-bunching) test, and the first stage are stated explicitly, the core
  `jcf-identification-strategy` RDD checklist.
- **The leading rival is named and adjudicated** — a disclosure-only story would leave deal mix and
  operating performance unchanged; the observed shift in both is the opposite, satisfying the design-defense
  move.
- **Mechanism is economic, not statistical** — the effect is tied to ex-ante deal selection and concentrated
  where pre-mandate monitoring was weak, the contribution type `jcf-contribution-framing` calls a mechanism
  claim, not a reduced-form sign.
- **Fits JCF scope and house style** — the question is squarely corporate governance and M&A, framed for a
  corporate-finance referee, satisfying the `jcf-topic-selection` remit; the contribution is front-loaded
  for the desk screen `jcf-contribution-framing` warns about.

> Next: adapt the reproducible analysis skeleton in [`../code/`](../code/) when turning this introduction
> arc into a full empirical workflow, and stress-test the design against
> [`../../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md).
