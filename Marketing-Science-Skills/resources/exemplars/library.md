# *Marketing Science* Exemplars Library (method × topic)

> **Verified via web search, access date 2026-06-08.** Every paper below was checked to confirm it
> actually appeared in **_Marketing Science_** — the flagship journal of the INFORMS Society for Marketing
> Science (ISMS), published by **INFORMS** — with year and volume/issue, against the journal's own article
> pages (`pubsonline.informs.org/doi/...`) and the INFORMS Marketing Science RePEc record
> (`ideas.repec.org/a/inm/ormksc/...` / `econpapers.repec.org/.../inm/ormksc`), corroborated by Google
> Scholar lookups carrying the journal name. Papers that could not be fully verified **as _Marketing
> Science_** were **omitted** — this is deliberately a short, clean list, not a long, uncertain one.
>
> **Sibling-journal guard.** *Marketing Science* is **not** the *Journal of Marketing Research* (JMR), the
> *Journal of Marketing* (JM), the *Journal of Consumer Research* (JCR), *Quantitative Marketing and
> Economics* (QME), *Management Science*, *Econometrica*, or the *RAND Journal of Economics*. Several
> famous "quant-marketing" papers live in those venues; the
> [Omitted](#omitted-for-lack-of-full-verification-do-not-attribute-to-marketing-science) section records
> the traps checked and rejected.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent coefficients, elasticities, equilibrium expressions, or specific findings — read the
> original on INFORMS PubsOnline before citing any number. For *Marketing Science*-specific scope, caps,
> blinding, and house style, see [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

*Marketing Science* publishes "articles that answer important research questions in marketing using
**mathematical modeling**" — chiefly **analytical (game-theoretic)** models of strategic interaction and
**structural econometric** models of demand and supply, with reduced-form / experimental / ML evidence
welcome when **disciplined by a model**. Pick the row whose **genre × marketing question** is closest to
yours, then study how that paper turns a marketing decision into a **counterfactual or comparative-static
contribution** a model alone can deliver — the *Marketing Science* bar (see
[`../../skills/mksc-topic-selection/SKILL.md`](../../skills/mksc-topic-selection/SKILL.md),
[`../../skills/mksc-theory-development/SKILL.md`](../../skills/mksc-theory-development/SKILL.md), and
[`../../skills/mksc-contribution-framing/SKILL.md`](../../skills/mksc-contribution-framing/SKILL.md)). For
each, ask the self-check question before claiming your paper is "*Marketing Science*-shaped."

> Note: the econometric [`code/`](../code/) kit (DiD / IV / RDD / DML) is the **evidentiary backbone** for
> the field-experiment and quasi-experimental rows; the analytical rows are evaluated by equilibrium
> derivation and comparative statics, and the structural rows by identification of preference/supply
> parameters and counterfactual simulation (`mksc-methods`, `mksc-data-analysis`).

---

## By method (genre)

### Choice modeling / discrete-choice demand on panel data (econometric)

- **Guadagni & Little, "A Logit Model of Brand Choice Calibrated on Scanner Data," _Marketing Science_ 1983, 2(3):203–238.**
  Verified: `pubsonline.informs.org/doi/...` (mksc.2.3.203); RePEc `inm/ormksc/v2y1983i3p203-238`.
  - **Why it is an exemplar:** the founding choice-model paper — a multinomial logit of brand choice
    estimated on UPC scanner panels, introducing loyalty variables that made disaggregate demand
    estimable on field data. The template for the [`mksc-theory-development`](../../skills/mksc-theory-development/SKILL.md)
    structural-demand move: write utility with micro-foundations, then let panel variation identify it.
  - **Self-check:** is your demand model micro-founded and estimated on real choice variation, with the
    identifying variation named rather than assumed?

### Analytical model of product-line / segmentation strategy (game-theoretic)

- **Moorthy, "Market Segmentation, Self-Selection, and Product Line Design," _Marketing Science_ 1984, 3(4):288–307.**
  Verified: `pubsonline.informs.org/doi/10.1287/mksc.3.4.288`; RePEc `inm/ormksc/v3y1984i4p288-307`.
  - **Why it is an exemplar:** replaces direct third-degree price discrimination with **consumer
    self-selection**, deriving how a firm's optimal product line and prices change once segments cannot be
    addressed directly — a clean analytical contribution carried by comparative statics, the
    [`mksc-theory-development`](../../skills/mksc-theory-development/SKILL.md) analytical pattern (primitives →
    optimization → counterintuitive result).
  - **Self-check:** do your assumptions map to a real marketing institution (self-selection,
    cannibalization), and is the contribution a *derived* comparative static, not an asserted one?

### Structural model with demand and supply / equilibrium pricing (structural econometric)

- **Sudhir, "Competitive Pricing Behavior in the Auto Market: A Structural Analysis," _Marketing Science_ 2001, 20(1):42–60.**
  Verified: `pubsonline.informs.org/doi/abs/10.1287/mksc.20.1.42.10196`; RePEc `inm/ormksc/v20y2001i1p42-60`.
  - **Why it is an exemplar:** estimates a demand system **and** a supply-side pricing game jointly, so the
    conduct parameters and counterfactual prices come from an equilibrium model rather than a reduced-form
    regression — the [`mksc-methods`](../../skills/mksc-methods/SKILL.md) structural standard: identify
    preferences and conduct, then simulate a policy.
  - **Self-check:** does your structural model pin down both demand and supply with a stated identification
    argument, and is the headline a *counterfactual* the estimated model can simulate?

### Analytical model of marketing communication (game-theoretic)

- **Villas-Boas, "Communication Strategies and Product Line Design," _Marketing Science_ 2004, 23(3):304–316.**
  Verified: `pubsonline.informs.org/doi/10.1287/mksc.1030.0048`; RePEc `inm/ormksc/v23y2004i3p304-316`.
  - **Why it is an exemplar:** shows that **costly, confusable communication** shrinks the optimal product
    line below the frictionless benchmark — an analytical result that ties advertising/communication to
    assortment design, the [`mksc-literature-positioning`](../../skills/mksc-literature-positioning/SKILL.md)
    move of locating a new mechanism among modeling precedents.
  - **Self-check:** does the model isolate one mechanism (communication cost/confusion) and show its sign
    on a managerial decision, rather than stacking assumptions for a single numerical example?

### Hierarchical Bayes for individual-level targeting (econometric / Bayesian)

- **Rossi, McCulloch & Allenby, "The Value of Purchase History Data in Target Marketing," _Marketing Science_ 1996, 15(4):321–340.**
  Verified: `pubsonline.informs.org/doi/10.1287/mksc.15.4.321`; EconPapers `inm/ormksc/v15y1996i4p321-340`.
  - **Why it is an exemplar:** uses a **hierarchical Bayes** choice model to quantify the marginal
    information value of purchase-history and demographic data for one-to-one targeting — a measurement/
    methodology contribution that prices an information set, exactly the [`mksc-data-analysis`](../../skills/mksc-data-analysis/SKILL.md)
    discipline of reporting what the model is and is not identified to say.
  - **Self-check:** is the payoff a quantified decision value (here, the worth of a data source) produced
    by an individual-level model, not a population average masquerading as personalization?

### Large-scale field experiment disciplined by a competitive model (causal + structural)

- **Dubé, Fang, Fong & Qu (Luo), "Competitive Price Targeting with Smartphone Coupons," _Marketing Science_ 2017, 36(6):944–975.**
  Verified: `pubsonline.informs.org/doi/...` (mksc.2017.1042); RePEc `inm/ormksc/v36y2017i6p944-975`.
  - **Why it is an exemplar:** a duopoly **field experiment** that varies both firms' targeted prices to
    trace best responses and assess equilibrium, so the causal estimates feed a competitive model rather
    than standing alone — the model for an economics-of-marketing claim earning its keep through
    identification *and* equilibrium reasoning. Pairs naturally with this pack's [`code/`](../code/)
    causal-inference chain as evidentiary backbone (`mksc-methods`).
  - **Self-check:** does your experiment isolate the marketing-instrument variation cleanly, and is the
    result interpreted through a strategic model (best responses, competitive mitigation), not as a single
    treatment effect?

---

## By topic (each cell is a verified _Marketing Science_ paper above)

| Topic | Verified _Marketing Science_ exemplar | Year / vol(issue):pp | Genre / method |
| --- | --- | --- | --- |
| Brand choice & demand estimation | Guadagni & Little, "A Logit Model of Brand Choice" | 1983, 2(3):203–238 | Discrete-choice demand (econometric) |
| Product line & segmentation | Moorthy, "Market Segmentation, Self-Selection & Product Line Design" | 1984, 3(4):288–307 | Analytical (game-theoretic) |
| Competitive pricing | Sudhir, "Competitive Pricing Behavior in the Auto Market" | 2001, 20(1):42–60 | Structural demand + supply |
| Advertising / communication | Villas-Boas, "Communication Strategies and Product Line Design" | 2004, 23(3):304–316 | Analytical (game-theoretic) |
| CRM / targeting & data value | Rossi, McCulloch & Allenby, "Value of Purchase History Data" | 1996, 15(4):321–340 | Hierarchical Bayes (econometric) |
| Digital / mobile & price targeting | Dubé, Fang, Fong & Qu, "Competitive Price Targeting with Smartphone Coupons" | 2017, 36(6):944–975 | Field experiment + competitive model |

---

## Omitted for lack of full verification (do not attribute to _Marketing Science_ without re-checking)

To keep the list zero-hallucination, these strong candidates were **excluded** after web-checking — each
is a real, important paper, but **not in _Marketing Science_** (the sibling-journal traps the brief warned
of):

- **Berry, Levinsohn & Pakes, "Automobile Prices in Market Equilibrium" (1995)** — verified to be in
  **_Econometrica_** 63(4):841–890, **not _Marketing Science_**. The canonical "BLP" random-coefficients
  demand method, ubiquitous in MKSC structural work but published in econometrics.
- **Narasimhan, "Competitive Promotional Strategies" (1988)** — verified to be in **_The Journal of
  Business_** 61(4):427–449, **not _Marketing Science_**. A foundational mixed-strategy promotion model,
  often misremembered as MKSC.
- **Dubé, Hitsch & Rossi, "State Dependence and Alternative Explanations for Consumer Inertia" (2010)** —
  verified to be in the **_RAND Journal of Economics_** 41(3):417–445, **not _Marketing Science_**. A
  flagship quant-marketing structural paper, but published in economics.
- **Fader, Hardie & Lee, "RFM and CLV: Using Iso-Value Curves for Customer Base Analysis" (2005)** —
  verified to be in the **_Journal of Marketing Research_** 42(4):415–430, **not _Marketing Science_**. A
  customer-base-analysis classic, but JMR.
- **Fong, Fang & Luo, "Geo-Conquesting: Competitive Locational Targeting of Mobile Promotions" (2015)** —
  verified to be in the **_Journal of Marketing Research_** 52(5):726–735, **not _Marketing Science_**. A
  mobile-targeting field experiment whose MKSC cousin (Dubé et al. 2017) *is* in this library.

Before adding any new paper to this library, confirm it on `pubsonline.informs.org/doi/...` (or the INFORMS
Marketing Science RePEc record `inm/ormksc`) with volume/issue/pages, and update the access-date header.
When a famous quant-marketing paper "feels" like *Marketing Science*, check the masthead — it is often JMR,
JCR, QME, *Management Science*, *Econometrica*, or *RAND*. When in doubt, **omit**.
