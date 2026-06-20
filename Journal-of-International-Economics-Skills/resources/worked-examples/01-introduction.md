> **Illustrative teaching example.** The paper, setting, and every number below are **fictional** and
> exist only to demonstrate *Journal of International Economics* house style. No real-paper facts are
> stated, and no real policy is invoked. Corresponding skills:
> [`jie-writing-style`](../../skills/jie-writing-style/SKILL.md),
> [`jie-topic-selection`](../../skills/jie-topic-selection/SKILL.md),
> [`jie-contribution-framing`](../../skills/jie-contribution-framing/SKILL.md), and
> [`jie-identification-strategy`](../../skills/jie-identification-strategy/SKILL.md).

# Worked Example: A *JIE*-Style Introduction (before → after)

This demonstrates the introduction arc the *Journal of International Economics* rewards (from
`jie-writing-style` and `jie-topic-selection`): **international economic question → why it matters to *both*
halves of the field (trade and international macro/finance) → data & identification (or the structural
discipline) → headline estimate with magnitude and interval → what it identifies and against which rival →
contribution → brief roadmap.** The governing rule from `jie-writing-style` is **lead with the question and
the number, demote the method**, and frame the contribution so a trade economist and an open-economy
macroeconomist both see why it matters.

**Illustrative paper (fictional):** *"Invoicing Currency and the Trade Collapse: Firm-Level Evidence from a
Fictional Currency Union Exit, 2011–2016."* Fictional setting: a fictional small open economy that left a
currency union; "dominant-currency exporters" are firms that invoiced in the anchor currency before exit.

---

## Before (buries the contribution — typical first-draft intro)

> Exchange rates and trade have been studied extensively in international economics. Many papers examine
> exchange rate pass-through, invoicing currency, and trade volumes. In this paper, we use firm-level
> customs data and a difference-in-differences design to study how a large exchange rate movement affected
> exports, comparing firms that invoiced in different currencies. We estimate several specifications and
> report the results. Understanding the trade effects of exchange rates is important for policymakers.
> Section 2 reviews the literature, Section 3 describes the data, Section 4 presents the methods, Section 5
> reports results, and Section 6 concludes.

**What's wrong (against `jie-writing-style` / `jie-topic-selection` / `jie-contribution-framing`):**

- **Leads with method** ("we use a difference-in-differences design") instead of the international question
  — the named anti-pattern in `jie-writing-style`.
- **No question and no answer on page one.** Neither a trade economist nor an open-economy macroeconomist
  can tell what the magnitude is or why it matters (fails the `jie-topic-selection` both-halves test).
- **No headline estimate with magnitude or uncertainty** — violates the estimate-first norm.
- **Identification is asserted, not motivated.** What makes invoicing currency *as good as random* across
  firms is never argued (the `jie-identification-strategy` gap).
- **Contribution type is unclear** — new estimate? new mechanism for the dominant-currency paradigm? (the
  `jie-contribution-framing` test.)
- **Throat-clearing** and an **over-signposted roadmap**.

---

## After (*JIE* arc — international question + estimate + identification, contribution early)

> **When a large depreciation hits, does an exporter's *invoicing currency* shape how much its trade
> collapses — and by how much?** Using firm-level customs records around a fictional currency-union exit, we
> find that exporters who had invoiced in the anchor currency cut export *volumes* by **18% more than
> local-currency invoicers over the two years after exit (95% CI 12–24%)**, even though their prices in
> destination currency barely moved — a sharp, currency-of-invoicing-specific margin of the trade collapse.
> *(International question + headline estimate with magnitude and interval, in the first breath, legible to
> both halves of the field.)*
>
> Identifying this is hard because invoicing currency is *chosen*: firms that invoice in the anchor currency
> differ in size, destination mix, and import intensity, any of which could drive the post-exit divergence.
> *(Why it is hard — the selection problem stated in international-economics terms, per
> `jie-identification-strategy`.)*
>
> We use the universe of fictional export transactions, 2011–2016, and compare anchor- vs. local-currency
> invoicers *within the same product-destination market and quarter*, absorbing market shocks with
> product × destination × time fixed effects, and we instrument pre-exit invoicing choice with a firm's
> share of anchor-currency *imported inputs* fixed before the exit was anticipated. The exclusion
> restriction is that, conditional on the fixed effects and firm size, pre-period input-currency exposure
> shifts export-invoicing currency but not the export response *except* through it; we test it with a
> pre-trend on 2011–2012 volumes and a placebo on non-tradable-input firms. *(Data and identification in one
> paragraph; the design is *defended*, not named — per `jie-identification-strategy` / `jie-data-analysis`.)*
>
> The excess collapse is **concentrated among firms with low import intensity** — those that lacked a
> "natural hedge" between anchor-currency revenue and anchor-currency costs — and **does not appear before the
> exit was anticipated**. *(Headline result restated with the mechanism signature that separates the
> invoicing channel from a size or destination story.)*
>
> Our contribution is to show that the trade collapse around a large depreciation operates through a
> **dominant-currency-invoicing margin in quantities, not prices, and is muted by firms' natural hedge** —
> not through the destination-price adjustment a producer-currency-pricing account would predict, and not
> through firm size. *(Contribution stated early and against the specific rival, per
> `jie-contribution-framing`; speaks to the trade side via firm export margins and to the macro side via the
> dominant-currency paradigm.)* The design is **portable** to any large exchange-rate episode with
> firm-level invoicing data. *(Portability — the field-wide payoff.)*
>
> The paper proceeds as follows. Section 2 places the result in the dominant-currency-pricing and
> heterogeneous-firms-trade literatures and describes the customs data; Section 3 develops the
> within-market design and the input-currency instrument; Section 4 reports the estimates, the
> natural-hedge heterogeneity, and robustness. *(Brief roadmap — no over-signposting.)*

---

## Why the "after" meets the *JIE* bar

Mapped to the skill checklists:

- **Contribution front-loaded** — by the end of the first paragraph the reader has the international
  question, the headline magnitude with a 95% interval, and what it identifies (`jie-writing-style`: lead
  with the question and the number).
- **Estimate-first prose** — the headline (18% more; 95% CI 12–24%) leads with magnitude **and uncertainty**,
  then is interpreted, rather than "the regression shows…" (`jie-data-analysis`: report intervals, not bare
  point estimates).
- **Speaks to both halves** — framed via firm export margins (trade) *and* the dominant-currency paradigm
  (international macro), satisfying the `jie-topic-selection` both-audiences test.
- **Identification is motivated and defended** — the endogeneity of invoicing choice is stated, the
  within-market design plus input-currency instrument is argued, and it is stress-tested with pre-trends and
  a placebo (the `jie-identification-strategy` standard).
- **The strongest rival is named and adjudicated** — a producer-currency-pricing story predicts the
  adjustment in destination prices and no natural-hedge heterogeneity; the data show quantity adjustment and
  a hedge gradient instead (`jie-identification-strategy` adjudication: "if the rival were true… instead it
  looks like ___").
- **Contribution type is explicit** — a **new causal estimate with a mechanism** (invoicing-currency
  quantity margin, muted by natural hedging), the `jie-contribution-framing` move of turning "a paper about
  X" into "the first firm-level estimate that Y."
- **Method is demoted to a tool** — the DiD/IV machinery appears only where the design is described, never as
  the lead (avoids the `jie-writing-style` "leading with the method" anti-pattern).

> Next: adapt the reproducible analysis skeleton in [`../code/`](../code/) when turning this introduction arc
> into a full empirical workflow, and pressure-test the design against
> [`../../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md).
