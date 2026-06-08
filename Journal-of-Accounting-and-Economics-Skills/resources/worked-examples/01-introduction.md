> **Illustrative teaching example.** The paper, setting, regulation, and every number below are
> **fictional** and exist only to demonstrate JAE house style. No real paper, ASU, or rule is described,
> and no policy is invented as fact. Corresponding skills:
> [`jae-writing-style`](../../skills/jae-writing-style/SKILL.md),
> [`jae-theory-development`](../../skills/jae-theory-development/SKILL.md),
> [`jae-contribution-framing`](../../skills/jae-contribution-framing/SKILL.md), and
> [`jae-methods`](../../skills/jae-methods/SKILL.md).

# Worked Example: A JAE-Style Introduction (before → after)

This demonstrates the **JAE introduction arc** from `jae-writing-style`: the intro should, within the
first pages, state the **economic question, the friction, the prediction, the identification, the data,
and the headline result** — a reviewer should know what you find *before* the methods section. The
register is the economics / positive-accounting one: precise, restrained, hypothesis-driven; causal verbs
matched to the design; contribution stated up front and closed in the discussion.

**Illustrative paper (fictional):** *"Mandated Segment Disclosure, Information Asymmetry, and the Cost of
Debt: Evidence from a Staggered Reporting Mandate."* Fictional setting: a (fictional) reporting mandate
that forced firms above a size threshold, in different years, to disaggregate operating-segment
profitability in their filings. (The mandate, threshold, and timing are invented for teaching.)

---

## Before (buries the prediction — typical first-draft intro)

> The relationship between corporate disclosure and capital markets has been studied extensively. Many
> papers examine voluntary and mandatory disclosure and their consequences. In this paper, we use a
> staggered difference-in-differences design to study the effect of segment-disclosure requirements on
> firms. Disclosure is an important topic for standard-setters and regulators, and firms should arguably
> provide more disaggregated information to investors and lenders. We assemble a panel from Compustat and
> DealScan and estimate event-study specifications. Section 2 reviews the literature, Section 3 describes
> the data, Section 4 presents the empirical strategy, Section 5 reports the results, and Section 6
> concludes.

**What's wrong (against `jae-writing-style`, `jae-theory-development`, `jae-contribution-framing`):**

- **Leads with method** ("we use a staggered difference-in-differences design") instead of the economic
  question and prediction — a named anti-pattern.
- **No economic friction and no *a priori* prediction.** A reviewer cannot tell which agency/information
  mechanism is at work or what sign is expected before the data.
- **No headline magnitude with units** in the intro — significance silence.
- **Normative drift** ("firms should arguably provide more information") — JAE is positive, not
  prescriptive.
- **Gap-spotting / throat-clearing** ("studied extensively," "important topic") with no tension resolved.
- **Contribution unstated**; **over-signposted roadmap** doing the argument's work.

---

## After (JAE arc — question + friction + prediction + identification + result, contribution early)

> **Does forcing firms to disaggregate segment profitability lower their cost of borrowing — and if so,
> through which economic channel?** We show that a mandate requiring disaggregated operating-segment
> disclosure reduces the spread on newly issued bank loans by **18 basis points** on average, and that
> the reduction is concentrated in firms where lenders previously faced the most severe information
> asymmetry. *(economic question + headline magnitude with units + the cross-sectional mechanism, in the
> first breath.)*
>
> The economic friction is informational. A diversified borrower's consolidated statements pool profitable
> and loss-making segments, so a lender cannot tell whether reported earnings are durable or are masking a
> deteriorating division; this adverse-selection problem is priced into the loan spread (Jensen-Meckling
> agency and information-economics primitives). Mandated disaggregation reduces the lender's uncertainty
> about the assets backing the loan, which should **lower the spread**, and the effect should be **larger
> where pre-mandate asymmetry was greater**. *(friction → actors and incentives → directional, a priori
> prediction → cross-sectional partition — the `jae-theory-development` arc.)*
>
> Identifying this is hard because firms that disclose more are not random: better-governed, lower-risk
> borrowers disclose voluntarily and also borrow more cheaply, so a cross-sectional comparison conflates
> disclosure with borrower quality. We exploit a mandate that bound firms above a size threshold in
> **different years**, generating staggered, plausibly exogenous variation in *when* a given firm was
> first required to disaggregate. We compare each newly-bound firm to not-yet-bound firms, verify there
> are no differential pre-trends in spreads, and read parallel trends as the identifying assumption.
> *(self-selection threat named first; the shock that solves it; identifying assumption stated in words —
> `jae-methods`.)*
>
> Loan spreads fall by **18 basis points** (relative to a pre-mandate mean of 162) after a firm becomes
> bound, with the decline emerging only post-mandate and absent beforehand. The effect roughly doubles in
> the quartile of borrowers with the highest pre-mandate bid-ask spreads — our proxy for information
> asymmetry — and is near zero for single-segment firms, for whom the mandate adds no information.
> *(headline result restated; the partition that pins the mechanism; a placebo group that rules out a
> mechanical story.)*
>
> Our contribution is to identify **information asymmetry between borrower and lender, not disclosure cost
> per se, as the margin through which segment reporting moves the price of debt**: the mandate changes no
> cash flow and no covenant, yet reprices credit by shrinking what the lender does not know. This advances
> the contracting-and-disclosure stream beyond documenting that disclosure correlates with cheaper capital,
> to showing *why* — consistent with efficient-contracting demand for verifiable information rather than
> with a generic transparency effect. *(contribution stated early, as a positive claim about a mechanism,
> relative to a specific prior view — `jae-contribution-framing`.)* We state the boundary plainly: the
> design identifies the effect for firms near the size threshold and does not speak to voluntary
> disaggregation or to equity-market consequences.
>
> The paper proceeds as follows. Section 2 develops the prediction and positions it in the
> disclosure-and-contracting literature; Section 3 describes the mandate, sample, and design; Section 4
> reports the spread results and the asymmetry partition; Section 5 reports robustness. *(brief roadmap —
> no over-signposting.)*

---

## Why the "after" meets the JAE bar

Mapped to the skill checklists:

- **Intro states question + friction + prediction + design + result early** — the headline magnitude
  (18 bp; relative to a 162 bp mean) and the mechanism appear immediately, with units
  (`jae-writing-style`: "reviewers should know what you find before the methods section").
- **Prediction derived from an economic primitive** — adverse selection / agency between lender and
  borrower yields a *directional, a priori* sign, not a reverse-engineered correlation
  (`jae-theory-development`; avoids HARKing and atheoretical correlation).
- **Cross-sectional partition ties effect size to friction severity** — larger where pre-mandate
  asymmetry is high, ~zero for single-segment firms — JAE's sharpest evidence of mechanism.
- **Identification matched to the prediction and stated in words** — staggered DiD around a regulatory
  mandate, parallel-trends assumption named and pre-trends checked; self-selection into disclosure named
  as the first threat (`jae-methods`).
- **Contribution stated early and positively** — "information asymmetry, not disclosure cost" — relative
  to a specific prior view, and **closed with explicit scope** (boundary conditions), per
  `jae-contribution-framing`; no normative "firms should" drift.
- **Causal verbs matched to the design** — "reduces / lowers the spread" is licensed by the quasi-
  experiment; the paper does not overreach beyond firms near the threshold (`jae-writing-style`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for verified real JAE papers whose intros
> execute this arc, the [reviewer-objection-checklist](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md)
> to stress-test the DiD before drafting, and [`../code/`](../code/) for the staggered-DiD command chain
> ([`stata/03_did_modern.do`](../code/stata/03_did_modern.do)) referenced above.
