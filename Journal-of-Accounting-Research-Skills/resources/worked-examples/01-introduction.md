> **Illustrative teaching example.** The paper, setting, and every number below are **fictional** and
> exist only to demonstrate JAR house style. No real-paper facts are stated, and no JAR editorial
> policy is invented here. Corresponding skills:
> [`jar-writing-style`](../../skills/jar-writing-style/SKILL.md),
> [`jar-topic-selection`](../../skills/jar-topic-selection/SKILL.md),
> [`jar-literature-positioning`](../../skills/jar-literature-positioning/SKILL.md), and
> [`jar-contribution-framing`](../../skills/jar-contribution-framing/SKILL.md).

# Worked Example: A JAR-Style Introduction (before → after)

This demonstrates the **JAR introduction arc** from `jar-writing-style`: within the first page or two,
state the **question**, the **setting and source of identifying variation**, the **main finding with its
sign and economic magnitude**, and the **contribution** — written for an accounting economist who wants
the **research design up front**, not after eight pages of literature review.

**Illustrative paper (fictional):** *"Mandatory Segment Disclosure and the Pricing of Private
Information: Evidence from a Staggered Enforcement Rule."* Fictional setting: a securities regulator that
phased in line-of-business segment-disclosure enforcement across industries in different years, generating
staggered variation in the granularity of mandated financial-statement disclosure.

---

## Before (buries the question — typical first-draft intro)

> The relationship between corporate disclosure and information asymmetry has been studied extensively in
> the accounting literature. A large body of work examines voluntary disclosure, analyst following, and
> the information environment. In this paper, we examine the relationship between segment disclosure and
> market liquidity. We assemble a panel of firms and estimate fixed-effects regressions of bid-ask spreads
> on a segment-disclosure measure, controlling for size, leverage, and analyst coverage. Disclosure
> regulation is an important topic for standard-setters. Our results contribute to the literature on
> disclosure and information asymmetry. Section 2 reviews the literature, Section 3 describes the data,
> Section 4 presents the empirical model, Section 5 reports results, and Section 6 concludes.

**What's wrong (against `jar-writing-style` / `jar-topic-selection` / `jar-literature-positioning`):**

- **Lit-review-first intro** that hides the question and the design — the named anti-pattern in
  `jar-writing-style`.
- **No setting or identifying variation on page one.** "We estimate fixed-effects regressions" is a panel
  with no named shock — the "no identification" anti-pattern in `jar-topic-selection`; a referee reads it
  as correlation, not effect.
- **No finding, no sign, no economic magnitude** in the intro.
- **Gap-spotting** ("has been studied extensively," "an important topic") instead of naming the specific
  accounting conversation that is open (`jar-literature-positioning`).
- **Contribution is a laundry-list gesture** ("contribute to the literature"), not the explicit
  one-sentence increment `jar-contribution-framing` requires.
- **Over-signposted roadmap** doing the work the argument should do.

---

## After (JAR arc — question → setting/identification → finding+magnitude → contribution)

> **Does forcing firms to disclose finer line-of-business segments move private information into prices,
> or does it merely relabel what investors already knew?** Using a regulator's staggered enforcement of
> segment-disclosure rules across industries, we show that finer mandated disclosure narrows bid-ask
> spreads by **14 basis points** (10% of the sample mean) and is concentrated in firms that previously
> aggregated profitable segments. *(question + setting + headline finding with sign and economic
> magnitude, on the first page — `jar-writing-style` front-loading.)*
>
> Identifying this is hard because firms choose their disclosure granularity, and the firms that aggregate
> segments differ systematically from those that report them — so a cross-sectional comparison of spreads
> on a disclosure measure conflates the disclosure with whatever made the firm opaque to begin with.
> *(the binding endogeneity threat — selection into disclosure — named before the design, per
> `jar-methods` and `jar-writing-style`.)*
>
> We exploit a rule under which the regulator phased in enforcement of segment-reporting requirements
> **industry by industry between 2015 and 2019**, on a schedule set by regulatory capacity rather than by
> the disclosure conditions of any firm. The staggered timing lets us compare newly-enforced firms with
> not-yet-enforced firms and trace spreads in event time; we find no differential pre-trends in liquidity
> before an industry's enforcement date. *(concrete setting and source of identifying variation — a named
> rule, not "we leverage exogenous variation"; pre-trends planned, not deferred to the rebuttal.)*
>
> Finer segment disclosure narrows spreads by **14 basis points** (off a mean of 138), with the effect
> appearing only after enforcement and growing over the following two years. The effect is concentrated
> among firms that had bundled a high-margin segment into a larger aggregate, and is absent where the
> mandated breakdown adds no information beyond what firms already reported — evidence the channel is
> **newly revealed cross-segment profitability**, not a mechanical disclosure-count effect. *(finding
> restated with the mechanism and a cross-sectional partition, as `jar-tables-figures` and
> `jar-contribution-framing` ask.)*
>
> Our contribution is to identify a **causal** liquidity effect of *mandated* disclosure **granularity**,
> and to separate genuine information revelation from relabeling — an increment over the
> voluntary-disclosure stream, which cannot rule out that disclosing firms differ, and over prior
> segment-disclosure work that lacked a clean enforcement shock. *(explicit one-sentence contribution
> stated relative to the closest conversation, per `jar-contribution-framing` and
> `jar-literature-positioning`.)* For standard-setters weighing recognition-vs.-disclosure and aggregation
> rules, the result implies that **enforcement of granularity, not the existence of a disclosure mandate,
> is where the pricing of private information is determined.** *(implication for a recurring JAR audience —
> regulators — with stated scope: the design speaks to enforced granularity, not to disclosure that firms
> would have made voluntarily.)*
>
> The paper proceeds as follows. Section 2 describes the enforcement rule and sample; Section 3 presents
> the design and main results; Section 4 examines the cross-segment-profitability mechanism. *(brief
> roadmap — no over-signposting.)*

---

## Why the "after" meets the JAR bar

Mapped to the skill checklists:

- **Intro states question, setting/identification, finding+magnitude, and contribution on page 1-2** —
  the JAR front-loading rule; the headline magnitude (14 bps; 10% of the mean) appears immediately, in
  basis points rather than as stars (`jar-writing-style`; `jar-contribution-framing` "economic magnitude
  interpreted, not just statistical significance").
- **Design described concretely** — a named, externally-scheduled enforcement rule with staggered timing,
  not "we exploit variation"; the binding threat (selection into disclosure) is named and the staggered
  design neutralizes it (`jar-methods`; `jar-writing-style` design-clarity check).
- **Predictions read as economics** — the revelation-vs.-relabeling tension is an information argument
  with a signed prediction, not a construct-chain (`jar-writing-style`).
- **Contribution is one explicit sentence stated against the closest conversation** —
  voluntary-disclosure and prior segment work — not a generic gap; framed as advancing accounting
  knowledge, not method (`jar-contribution-framing`; `jar-literature-positioning`).
- **Accounting question, not finance-in-disguise** — the object is a *disclosure-granularity mandate* and
  its effect on the information environment, squarely in the Ball-Brown capital-markets lineage
  (`jar-topic-selection` fit test).
- **Reproducible-by-design** — a staggered enforcement schedule and standard archival sources make a
  posted data-and-code package feasible, which JAR requires (`jar-topic-selection`; `jar-methods`).
- **One-sentence hook is fillable:** "We show that [enforced segment-disclosure granularity narrows
  spreads by 14 bps] using [staggered industry-by-industry enforcement]" — setting and finding both filled.

> Next: see [`../code/stata/03_did_modern.do`](../code/stata/03_did_modern.do) for the
> heterogeneity-robust staggered-DiD command chain that estimates the event-time spread effect described
> above (with [`../code/stata/05_rdd.do`](../code/stata/05_rdd.do) for the threshold-design alternative).
