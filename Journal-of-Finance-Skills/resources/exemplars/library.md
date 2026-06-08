# JF Exemplars Library (method × topic)

> **Verified via web search, access date 2026-06-07.** Every paper below was checked against its
> **Wiley Online Library** *Journal of Finance* article page to confirm it actually appeared in
> *The Journal of Finance* (AFA flagship, published by Wiley), with year and volume/issue. JF articles
> carry the DOI prefix `10.1111/j.1540-6261.*` (older) or `10.1111/jofi.*` (newer); both were used as the
> verification signal. Papers that could not be fully verified as JF were **omitted** — it is
> deliberately a short, clean list rather than a long, uncertain one.
>
> **Sibling-confusion guard (the biggest risk here):** JF is **not** the *Journal of Financial Economics*
> (JFE), the *Review of Financial Studies* (RFS), the *Review of Finance*, or the *Journal of Financial
> and Quantitative Analysis* (JFQA). Several famous finance papers sit at those siblings; the
> "Omitted" section below records the ones most often misattributed to JF. When in doubt, omit.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent regression coefficients or specific findings — read the original on Wiley before
> citing any number. For JF-specific policy, scope, and a "do-not-misattribute" list, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **method × question** is closest to yours, then study how that paper makes a *credible*
result carry a *general-interest, flagship-level* lesson — the JF bar (see
[`../../skills/jf-topic-selection/SKILL.md`](../../skills/jf-topic-selection/SKILL.md) and
[`../../skills/jf-writing-style/SKILL.md`](../../skills/jf-writing-style/SKILL.md)). For each, ask the
self-check question before claiming your paper is "JF-shaped." Foundational-canon attribution to the
correct top-3 journal is itself a JF-reviewer expectation (see
[`../../skills/jf-literature-positioning/SKILL.md`](../../skills/jf-literature-positioning/SKILL.md)).

---

## By method

### Cross-sectional asset pricing — the empirical anomaly that reshapes a factor model

- **Fama & French, "The Cross-Section of Expected Stock Returns," JF 1992, 47(2):427–465.**
  Verified: `onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.1992.tb04398.x`.
  - **Why it is an exemplar:** two easily measured variables (size, book-to-market) organize the entire
    cross-section of average returns — a single broad fact that reset how the whole field models expected
    returns. The prototype "one general-interest result every finance economist must reckon with."
  - **Attribution note:** the **1992 cross-section paper is JF**; the closely related Fama–French
    **three-factor (1993) paper is in JFE, not JF** — do not merge them (`jf-literature-positioning`).
  - **Self-check:** does your cross-sectional fact reorganize a debate the whole field already argues
    about, rather than add one more characteristic no one disputes?

### Trading-strategy / market-efficiency test (empirical asset pricing)

- **Jegadeesh & Titman, "Returns to Buying Winners and Selling Losers: Implications for Stock Market
  Efficiency," JF 1993, 48(1):65–91.**
  Verified: `onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-6261.1993.tb04702.x`.
  - **Why it is an exemplar:** documents momentum — a simple, replicable strategy with returns not
    explained by systematic risk — turning a clean empirical regularity into a standing challenge to
    market efficiency. Broad interest from one transparent result.
  - **Self-check:** is your strategy's profitability shown to survive the obvious risk-based and
    microstructure explanations a referee raises first?

### Performance persistence with a factor benchmark (mutual funds / asset pricing)

- **Carhart, "On Persistence in Mutual Fund Performance," JF 1997, 52(1):57–82.**
  Verified: `onlinelibrary.wiley.com/doi/full/10.1111/j.1540-6261.1997.tb03808.x`.
  - **Why it is an exemplar:** a survivorship-bias-free sample plus a four-factor benchmark shows that
    common factors and costs — not skill — explain most fund-return persistence. A method (the fourth,
    momentum factor) and a fact delivered together.
  - **Self-check:** is your benchmark rich enough that the "skill" you measure cannot be a known factor in
    disguise (the multiple-testing / omitted-factor critique)?

### Behavioral corporate finance — a manager trait moves real investment

- **Malmendier & Tate, "CEO Overconfidence and Corporate Investment," JF 2005, 60(6):2661–2700.**
  Verified: `onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-6261.2005.00813.x`.
  - **Why it is an exemplar:** builds a measurable proxy for an unobservable trait (overconfidence, from
    option-exercise behavior) and ties it to investment–cash-flow sensitivity — a new mechanism with a
    transparent identifying measure, of interest well beyond corporate finance.
  - **Self-check:** is your proxy for the latent trait defensible on its own, before any outcome
    regression, against the "it's just a omitted firm characteristic" story?

### Natural-experiment causal identification — does the manager matter? (corporate)

- **Bennedsen, Pérez-González & Wolfenzon, "Do CEOs Matter? Evidence from Hospitalization Events,"
  JF 2020, 75(4):1877–1911.**
  Verified: `onlinelibrary.wiley.com/doi/abs/10.1111/jofi.12897`.
  - **Why it is an exemplar:** uses CEO (and family) hospitalization events as plausibly exogenous shocks
    to managerial attention to identify the causal effect of the individual CEO on firm performance — a
    clean named shock answering a question the whole field cares about. Pairs with the DiD/event-study
    chain in [`../code/stata/03_did_modern.do`](../code/stata/03_did_modern.do).
  - **Self-check:** is your shock genuinely exogenous to the outcome (not anticipated, not co-timed with a
    confounding event) — the `jf-identification` natural-experiment bar?

### Regression-discontinuity from a contractual threshold (corporate / creditor control)

- **Chava & Roberts, "How Does Financing Impact Investment? The Role of Debt Covenants," JF 2008,
  63(5):2085–2121.**
  Verified: `onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-6261.2008.01391.x`.
  - **Why it is an exemplar:** a covenant-violation threshold gives a regression-discontinuity design in
    which capital investment drops sharply once control shifts to creditors — the discontinuity *is* the
    identification, isolating a specific channel (transfer of control rights). Pairs with the RDD /
    manipulation-test chain in [`../code/stata/05_rdd.do`](../code/stata/05_rdd.do).
  - **Self-check:** is your threshold a real, externally-defined contractual/institutional cutoff that
    firms cannot precisely manipulate around (continuity / no-bunching defensible)?

---

## By topic (each cell is a verified JF paper above)

| Topic | Verified JF exemplar | Year / vol(issue) | Method |
| --- | --- | --- | --- |
| Cross-section of returns / factors | Fama & French, "Cross-Section of Expected Stock Returns" | 1992, 47(2) | Cross-sectional asset pricing |
| Market efficiency / momentum | Jegadeesh & Titman, "Buying Winners and Selling Losers" | 1993, 48(1) | Trading-strategy test |
| Mutual-fund performance | Carhart, "On Persistence in Mutual Fund Performance" | 1997, 52(1) | Factor-benchmarked persistence |
| Behavioral corporate / investment | Malmendier & Tate, "CEO Overconfidence and Corporate Investment" | 2005, 60(6) | Trait proxy + regression |
| Managerial effects / governance | Bennedsen, Pérez-González & Wolfenzon, "Do CEOs Matter?" | 2020, 75(4) | Natural experiment (event) |
| Creditor control / financing & investment | Chava & Roberts, "How Does Financing Impact Investment?" | 2008, 63(5) | Regression discontinuity |

---

## Omitted for lack of full verification / sibling-journal misattribution (do not attribute to JF)

To keep the list zero-hallucination, these frequently-cited finance papers were **excluded** after
checking — each sits at a *sibling* journal, not JF. They are listed only as guardrails:

- **Fama & French, "Common Risk Factors in the Returns on Stocks and Bonds" (the three-factor model,
  1993)** — verified in the **Journal of Financial Economics (JFE)** 33(1):3–56, **not JF**. The 1992
  cross-section paper *is* JF; the 1993 three-factor paper is JFE. The single most common JF/JFE mix-up.
- **Harvey, Liu & Zhu, "… and the Cross-Section of Expected Returns" (2016)** — verified in the
  **Review of Financial Studies (RFS)** 29(1):5–68 (`academic.oup.com/rfs/...`), **not JF**. (This is the
  multiple-testing critique that `jf-literature-positioning` says to cite — cite it to RFS.)
- **Gormley & Matsa, "Common Errors: How to (and Not to) Control for Unobserved Heterogeneity" (2014)** —
  verified in the **Review of Financial Studies (RFS)** 27(2):617–661, **not JF**.
- **Yermack, "Higher Market Valuation of Companies with a Small Board of Directors" (1996)** — verified in
  the **Journal of Financial Economics (JFE)** 40(2):185–211, **not JF**.
- **Bertrand & Mullainathan, "Enjoying the Quiet Life? Corporate Governance and Managerial Preferences"
  (2003)** — verified in the **Journal of Political Economy (JPE)** 111(5):1043–1075, an economics journal,
  **not JF**.

Before adding any new paper to this library, confirm it on its **Wiley Online Library** JF article page
(DOI `10.1111/j.1540-6261.*` or `10.1111/jofi.*`, with volume/issue) and update the access-date header.
When in doubt, omit.
