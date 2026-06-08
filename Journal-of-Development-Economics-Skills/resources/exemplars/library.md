# JDE Exemplars Library (method × topic)

> **Verified via web search, access date 2026-06-07.** Every paper below was checked against its
> RePEc/EconPapers record under the `eee/deveco` handle (RePEc's series identifier for *Journal of
> Development Economics*, Elsevier) and/or its ScienceDirect article page (`sciencedirect.com/.../S0304-3878…`,
> the JDE ISSN), to confirm it actually appeared in the **Journal of Development Economics** — not in a
> sibling outlet — with year and volume. Papers that could not be fully verified as JDE were **omitted**: it
> is deliberately a short, clean list rather than a long, uncertain one.
>
> **Sibling-confusion guard.** Many landmark development RCTs and quasi-experiments are published *not* in
> JDE but in AEJ:Applied, QJE, AER, Econometrica, JPE, RESTud, World Development, or the Journal of
> Development Studies. Every entry here was specifically confirmed to be JDE; see the **Omitted** section for
> famous papers that were checked and found to belong to those siblings instead.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not reproduce
> or invent regression coefficients or specific findings — read the original on ScienceDirect / the authors'
> pages before citing any number. For JDE-specific policy, scope, and venue facts, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **method × question** is closest to yours, then study how that paper makes a *local,
credible* result carry a *first-order development* lesson — the JDE bar (see
[`../../skills/jde-topic-selection/SKILL.md`](../../skills/jde-topic-selection/SKILL.md),
[`../../skills/jde-identification-strategy/SKILL.md`](../../skills/jde-identification-strategy/SKILL.md), and
[`../../skills/jde-contribution-framing/SKILL.md`](../../skills/jde-contribution-framing/SKILL.md)). For
each, ask the self-check question before claiming your paper is "JDE-shaped."

---

## By method

### Cluster-randomized field experiment (the development workhorse)

- **Meredith, Robinson, Walker & Wydick, "Keeping the doctor away: Experimental evidence on investment in preventative health products," JDE 2013, 105:196–210.**
  Verified: RePEc `eee/deveco:v:105:y:2013:i:c:p:196-210` and `sciencedirect.com/science/article/abs/pii/S0304387813001181`.
  - **Why it is an exemplar:** experimentally estimates demand curves for preventative health products across
    four LMIC settings (Kenya, Guatemala, India, Uganda) and isolates *why* take-up is low — price
    sensitivity, liquidity, targeting women — exactly the policy-lever framing `jde-contribution-framing`
    asks for. The RCT inference and balance/attrition workflow maps to
    [`../code/stata/03_did_modern.do`](../code/stata/03_did_modern.do).
  - **Self-check:** does your experiment recover a *mechanism* and a *policy lever*, not just an average
    treatment effect?

### Large-scale RCT of a property-rights / land program (program evaluation)

- **Goldstein, Houngbedji, Kondylis, O'Sullivan & Selod, "Formalization without certification? Experimental evidence on property rights and investment," JDE 2018, 132:57–74.**
  Verified: RePEc `eee/deveco:v:132:y:2018:i:c:p:57-74` and `sciencedirect.com/science/article/abs/pii/S030438781730127X`.
  - **Why it is an exemplar:** a first large-scale RCT of a land-demarcation program in rural Benin turns an
    institutional question (does tenure security raise long-term investment?) into a credible causal
    estimate, with gendered heterogeneity that sharpens the development lesson.
  - **Self-check:** is your treatment a real, scalable *policy instrument*, and do you report the
    heterogeneity that tells a policymaker for whom it binds?

### Reduced-form effect of an agricultural productivity shock (quasi-experiment / weather IV-style variation)

- **Emerick, "Agricultural productivity and the sectoral reallocation of labor in rural India," JDE 2018, 135:488–503.**
  Verified: RePEc `eee/deveco:v:135:y:2018:i:c:p:488-503` and `sciencedirect.com/science/article/abs/pii/S0304387818311787` (DOI `10.1016/j.jdeveco.2018.08.013`).
  - **Why it is an exemplar:** uses exogenous variation in agricultural output (from abnormal precipitation)
    to identify structural-transformation effects on the non-agricultural labor share — a first-order
    growth/structural-change question carried by credible reduced-form variation. Pairs with the IV/robustness
    skeleton in [`../code/stata/04_iv.do`](../code/stata/04_iv.do).
  - **Self-check:** does your exogenous shock speak to a *macro-development* question (structural change,
    growth), not only a local micro outcome?

### Historical / long-run development with panel identification (economic history of development)

- **Fenske & Kala, "Climate and the slave trade," JDE 2015, 112:19–32.**
  Verified: RePEc `eee/deveco:v:112:y:2015:i:c:p:19-32` and `sciencedirect.com/science/article/abs/pii/S0304387814001072`.
  - **Why it is an exemplar:** an annual panel of African temperatures and port-level slave exports gives a
    clean within-port identification of how climate shaped the slave trade — long-run roots of African
    underdevelopment, a question that travels well beyond the subfield (`jde-topic-selection` "it travels"
    filter).
  - **Self-check:** does your historical variation identify a development *mechanism* with panel rigor, not
    just a cross-sectional correlation?

---

## By topic (each cell is a verified JDE paper above)

| Topic | Verified JDE exemplar | Year / vol:pages | Method |
| --- | --- | --- | --- |
| Health / human capital demand | Meredith, Robinson, Walker & Wydick, "Keeping the doctor away" | 2013, 105:196–210 | Field experiment (demand curves) |
| Property rights / land / agriculture | Goldstein, Houngbedji, Kondylis, O'Sullivan & Selod, "Formalization without certification?" | 2018, 132:57–74 | Large-scale RCT |
| Structural transformation / agriculture | Emerick, "Agricultural productivity and sectoral reallocation of labor" | 2018, 135:488–503 | Weather-shock quasi-experiment |
| Economic history of development | Fenske & Kala, "Climate and the slave trade" | 2015, 112:19–32 | Historical panel |

---

## Omitted for sibling-journal placement or lack of full JDE verification (do not attribute to JDE without re-checking)

To keep the list zero-hallucination, the following famous development papers were **checked and excluded**
because web search placed them in a *sibling* outlet, not JDE. They are listed only as guardrails:

- **Glewwe, Kremer & Moulin, "Many Children Left Behind? Textbooks and Test Scores in Kenya" (2009)** —
  verified in **AEJ: Applied Economics** 1(1):112–135, *not JDE*.
- **Bandiera, Burgess, Das, Gulesci, Rasul & Sulaiman, "Labor Markets and Poverty in Village Economies" (2017)** —
  verified in **QJE** 132(2):811–870, *not JDE*.
- **Banerjee & Duflo, "Do Firms Want to Borrow More? …" (2014)** — verified in the **Review of Economic
  Studies** 81(2):572–607, *not JDE*.
- **Jensen, "The (Perceived) Returns to Education and the Demand for Schooling" (2010)** — verified in
  **QJE** 125(2):515–548, *not JDE*.
- **Jensen & Miller, "Giffen Behavior and Subsistence Consumption" (2008)** — verified in **AER**
  98(4):1553–1577, *not JDE*.
- **Banerjee, Cole, Duflo & Linden, "Remedying Education …" (2007)** — verified in **QJE** 122(3):1235–1264,
  *not JDE*.
- **Miguel & Kremer, "Worms …" (2004)** — Econometrica 72(1), *not JDE*; **Bleakley, "Disease and
  Development" (2007)** — QJE 122(1):73–117, *not JDE*. Both are classic development papers in siblings.

Before adding any new paper to this library, confirm it on ScienceDirect (JDE article page, ISSN 0304-3878)
or its RePEc `eee/deveco` record with volume/pages, and update the access-date header. When in doubt, omit.
