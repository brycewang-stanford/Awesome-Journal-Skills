# QJE Exemplars Library (method × topic)

> **Verified via web search, access date 2026-06-07.** Every paper below was checked against
> Oxford Academic's QJE article pages (`academic.oup.com/qje/...`) to confirm it actually appeared in
> *The Quarterly Journal of Economics*, with year and volume/issue. Papers that could not be fully
> verified as QJE were **omitted** — it is deliberately a short, clean list rather than a long,
> uncertain one.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent regression coefficients or specific findings — read the original on Oxford
> Academic / the authors' pages before citing any number. For QJE-specific policy, scope, and a
> "do-not-misattribute" list, see [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **method × question** is closest to yours, then study how that paper makes a *local,
credible* result carry a *general-interest* lesson — the QJE bar (see
[`../../skills/qje-topic-selection/SKILL.md`](../../skills/qje-topic-selection/SKILL.md) and
[`../../skills/qje-writing-style/SKILL.md`](../../skills/qje-writing-style/SKILL.md)). For each, ask
the self-check question before claiming your paper is "QJE-shaped."

---

## By method

### Theory that reframes a market (microeconomic theory)

- **Akerlof, "The Market for 'Lemons': Quality Uncertainty and the Market Mechanism," QJE 1970, 84(3):488–500.**
  Verified: `academic.oup.com/qje/article-abstract/84/3/488/1896241`.
  - **Why it is an exemplar:** a single, simple mechanism (asymmetric information) stated so plainly that
    it reorganized how economists think about insurance, credit, and labor markets — the canonical
    "small model, enormous lesson" QJE paper.
  - **Self-check:** can your central idea be stated, and its bite felt, in one paragraph a non-specialist
    grasps immediately?

### Cross-country growth regression (empirical macro)

- **Mankiw, Romer & Weil, "A Contribution to the Empirics of Economic Growth," QJE 1992, 107(2):407–437.**
  Verified: `academic.oup.com/qje/article-abstract/107/2/407/1838296`.
  - **Why it is an exemplar:** takes an existing theory (Solow), augments it minimally (human capital),
    and shows it fits the cross-country data — the result *settles* how much of the standard-of-living
    gap a workhorse model explains.
  - **Self-check:** does your empirics adjudicate a model the whole field already argues about, rather
    than estimate a parameter no one disputes?

### Regression discontinuity / IV from an institutional rule (applied micro)

- **Angrist & Lavy, "Using Maimonides' Rule to Estimate the Effect of Class Size on Scholastic Achievement," QJE 1999, 114(2):533–575.**
  Verified: `academic.oup.com/qje/article-abstract/114/2/533/1844228`.
  - **Why it is an exemplar:** an institutional cutoff (a maximum-class-size rule) generates exogenous
    variation in class size — the discontinuity *is* the identification, and the rule is too quirky for
    schools to game. Pairs naturally with [`../code/stata/05_rdd.do`](../code/stata/05_rdd.do).
  - **Self-check:** is your discontinuity a real, externally-imposed institutional threshold that units
    cannot precisely manipulate?

### Quantitative model + microdata (misallocation / structural)

- **Hsieh & Klenow, "Misallocation and Manufacturing TFP in China and India," QJE 2009, 124(4):1403–1448.**
  Verified: `academic.oup.com/qje/article-abstract/124/4/1403/1917179`.
  - **Why it is an exemplar:** a transparent model turns dispersion in plant-level marginal products into
    a headline aggregate-TFP counterfactual — QJE does publish model-driven quantitative work when the
    lesson is first-order. See [`../../skills/qje-theory-model/SKILL.md`](../../skills/qje-theory-model/SKILL.md).
  - **Self-check:** does your model map cleanly to microdata and deliver one memorable counterfactual
    magnitude, not just a calibration exercise?

### Large-scale linked administrative data, descriptive + causal (big-data applied micro)

- **Chetty, Hendren, Kline & Saez, "Where is the Land of Opportunity? The Geography of Intergenerational Mobility in the United States," QJE 2014, 129(4):1553–1623.**
  Verified: `academic.oup.com/qje/article-abstract/129/4/1553/1853754`.
  - **Why it is an exemplar:** new population-scale data answer an old, broad question (does opportunity
    vary by place?) with a memorable map of mobility — the prototype the QJE writing-style skill points to.
  - **Self-check:** do genuinely novel data let you answer a question a labor, macro, and development
    economist would *all* care about?

### Movers / exposure-design causal identification (applied micro)

- **Chetty & Hendren, "The Impacts of Neighborhoods on Intergenerational Mobility I: Childhood Exposure Effects," QJE 2018, 133(3):1107–1162.**
  Verified: `academic.oup.com/qje/article-abstract/133/3/1107/4850660`.
  - **Why it is an exemplar:** converts the cross-sectional geography of mobility into a *causal* claim by
    studying families who move, with exposure-time variation doing the identifying work — a model of
    turning a descriptive fact into a credible causal design.
  - **Self-check:** does your design isolate quasi-random variation (timing, exposure, a move) that rules
    out the selection story a referee will raise first?

---

## By topic (each cell is a verified QJE paper above)

| Topic | Verified QJE exemplar | Year / vol(issue) | Method |
| --- | --- | --- | --- |
| Information & market design | Akerlof, "Market for 'Lemons'" | 1970, 84(3) | Theory |
| Economic growth / development | Mankiw, Romer & Weil, "Empirics of Economic Growth" | 1992, 107(2) | Cross-country regression |
| Education / class size | Angrist & Lavy, "Maimonides' Rule" | 1999, 114(2) | RDD / IV |
| Productivity & misallocation | Hsieh & Klenow, "Misallocation and Manufacturing TFP" | 2009, 124(4) | Quantitative model + microdata |
| Inequality / intergenerational mobility | Chetty, Hendren, Kline & Saez, "Land of Opportunity" | 2014, 129(4) | Large-scale admin data |
| Neighborhoods / place effects | Chetty & Hendren, "Impacts of Neighborhoods I" | 2018, 133(3) | Movers / exposure design |

---

## Omitted for lack of full verification (do not attribute to QJE without re-checking)

To keep the list zero-hallucination, the following candidates were **excluded** after checking:

- **Dube, Lester & Reich, "Minimum Wage Effects Across State Borders" (2010)** — verified to be in the
  *Review of Economics and Statistics* 92(4):945–964, **not QJE**. Listed here only as a guardrail.
- **Chetty, Friedman & Rockoff teacher value-added / Project STAR earnings work** — the closely related
  "Measuring the Impacts of Teachers II" appeared in the *American Economic Review* (2014); a QJE
  placement of the specific paper could not be cleanly confirmed by web search, so it is omitted.

Before adding any new paper to this library, confirm it on `academic.oup.com/qje` (article page with
volume/issue) and update the access-date header. When in doubt, omit.
