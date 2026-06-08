# RFS Exemplars Library (method × topic)

> **Verified via web search, access date 2026-06-07.** Every paper below was checked against
> Oxford Academic's RFS article pages (`academic.oup.com/rfs/...`) to confirm it actually appeared in
> *The Review of Financial Studies* specifically — **not** in a sibling journal (Journal of Finance,
> Journal of Financial Economics, Review of Finance, or Review of Asset Pricing Studies) — with year and
> volume/issue. Papers that could not be fully verified as RFS were **omitted**; several plausible-looking
> finance landmarks that turned out to be in a *sibling* journal are listed at the bottom as explicit
> guardrails. It is deliberately a short, clean list rather than a long, uncertain one.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent regression coefficients or specific findings — read the original on Oxford
> Academic / the authors' pages before citing any number. For RFS-specific policy, scope, and a
> "do-not-misattribute" list, see [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **method × question** is closest to yours, then study how that paper makes a *novel
and rigorous* result clear the RFS bar — a genuinely new question or mechanism, established with a
credible design (see
[`../../skills/rfs-topic-selection/SKILL.md`](../../skills/rfs-topic-selection/SKILL.md) and
[`../../skills/rfs-writing-style/SKILL.md`](../../skills/rfs-writing-style/SKILL.md)). For each, ask the
self-check question before claiming your paper is "RFS-shaped."

---

## By method

### Theory tightly integrated with empirics (intermediary asset pricing / liquidity)

- **Brunnermeier & Pedersen, "Market Liquidity and Funding Liquidity," RFS 2009, 22(6):2201–2238.**
  Verified: `academic.oup.com/rfs/article-abstract/22/6/2201/1592184`.
  - **Why it is an exemplar:** a single tight model — margins link market and funding liquidity, producing
    self-reinforcing spirals — that yields predictions the paper then matches to stylized facts. The
    `rfs-writing-style` model of a theory→prediction→evidence arc; the canonical RFS intermediation paper.
  - **Self-check:** does your model deliver a *new, tested* prediction, not a model in Section 2 and an
    unrelated regression in Section 4?

### Cross-sectional asset pricing / anomaly digestion (factor model)

- **Hou, Xue & Zhang, "Digesting Anomalies: An Investment Approach," RFS 2015, 28(3):650–705.**
  Verified: `academic.oup.com/rfs/article/28/3/650/1574802` (Editor's Choice).
  - **Why it is an exemplar:** a four-factor q-model is shown to subsume a large set of anomalies — a
    "new method credibly better for an important question" novelty axis from `rfs-topic-selection`, with
    the data-mining critique confronted head-on.
  - **Self-check:** if you claim a new factor/predictor, do you confront multiple testing and
    out-of-sample stability (per `rfs-identification` Branch D), not just report in-sample significance?

### Return predictability / time-series asset pricing

- **Bollerslev, Tauchen & Zhou, "Expected Stock Returns and Variance Risk Premia," RFS 2009, 22(11):4463–4492.**
  Verified: `academic.oup.com/rfs/article-abstract/22/11/4463/1565787`.
  - **Why it is an exemplar:** identifies a specific, theoretically grounded predictor (the variance risk
    premium) and shows the predictability hinges on a clean construction choice (model-free implied
    volatility) — novelty plus rigor, not a data-mined regressor.
  - **Self-check:** is your predictor motivated by a mechanism *before* the data, with the inference
    appropriate to overlapping/autocorrelated returns?

### Liquidity-as-priced-risk, cross-market evidence (empirical asset pricing)

- **Bekaert, Harvey & Lundblad, "Liquidity and Expected Returns: Lessons from Emerging Markets," RFS 2007, 20(6):1783–1831.**
  Verified: `academic.oup.com/rfs/article-abstract/20/6/1783/1575135`.
  - **Why it is an exemplar:** uses a setting (emerging markets) where the margin of interest — liquidity
    — varies enough to be seen, turning a hard-to-identify asset-pricing claim into a credible one. The
    "new data lets you see something previously invisible" axis from `rfs-topic-selection`.
  - **Self-check:** does your setting generate enough variation in the priced quantity to identify it,
    rather than relying on a single thin cross-section?

### Regression discontinuity from an institutional rule (corporate / market microstructure)

- **Chang, Hong & Liskovich, "Regression Discontinuity and the Price Effects of Stock Market Indexing," RFS 2015, 28(1):212–246.**
  Verified: `academic.oup.com/rfs/article-abstract/28/1/212/1680962`.
  - **Why it is an exemplar:** the Russell 1000/2000 cutoff is a sharp, externally-imposed threshold that
    firms near the boundary cannot precisely manipulate — the discontinuity *is* the identification.
    Pairs naturally with [`../code/stata/05_rdd.do`](../code/stata/05_rdd.do).
  - **Self-check:** is your discontinuity a real institutional threshold with a density/manipulation test
    and bandwidth robustness (per `rfs-identification` Branch C), not a self-selected cutoff?

### Econometric methodology for corporate finance / asset pricing (research-design)

- **Gormley & Matsa, "Common Errors: How to (and Not to) Control for Unobserved Heterogeneity," RFS 2014, 27(2):617–661.**
  Verified: `academic.oup.com/rfs/article-abstract/27/2/617/1579975`.
  - **Why it is an exemplar:** a "new method" contribution that improves how an entire field controls for
    unobserved heterogeneity — showing RFS publishes methodology when it changes how credible work is
    done. Directly informs the fixed-effects choices in [`../code/`](../code/).
  - **Self-check:** if your contribution is methodological, does it correct a *widespread* inferential
    error and show the fix changes conclusions, not just propose a variant?

---

## By topic (each cell is a verified RFS paper above)

| Topic | Verified RFS exemplar | Year / vol(issue) | Method |
| --- | --- | --- | --- |
| Intermediary liquidity / funding spirals | Brunnermeier & Pedersen, "Market Liquidity and Funding Liquidity" | 2009, 22(6) | Theory + empirics |
| Cross-sectional anomalies / factor models | Hou, Xue & Zhang, "Digesting Anomalies" | 2015, 28(3) | Factor model (q-factor) |
| Return predictability | Bollerslev, Tauchen & Zhou, "Variance Risk Premia" | 2009, 22(11) | Time-series predictability |
| Liquidity as priced risk | Bekaert, Harvey & Lundblad, "Liquidity and Expected Returns" | 2007, 20(6) | Cross-market asset pricing |
| Indexing / price effects | Chang, Hong & Liskovich, "Price Effects of Indexing" | 2015, 28(1) | RDD |
| Research design / unobserved heterogeneity | Gormley & Matsa, "Common Errors" | 2014, 27(2) | Econometric methodology |

---

## Omitted for sibling-journal risk or lack of full verification (do NOT attribute to RFS without re-checking)

To keep the list zero-hallucination, the following finance landmarks were **excluded** after checking —
each is a plausible RFS candidate that web search placed in a *different* venue. They are listed only as
guardrails against the single biggest risk here: confusing RFS with JF / JFE / JPE / Review of Finance.

- **Pástor & Stambaugh, "Liquidity Risk and Expected Stock Returns" (2003)** — verified to be in the
  *Journal of Political Economy* 111(3):642–685, **not RFS**.
- **Adrian & Shin, "Liquidity and Leverage" (2010)** — verified to be in the *Journal of Financial
  Intermediation* 19(3):418–437, **not RFS**.
- **Frazzini & Pedersen, "Betting Against Beta" (2014)** — verified to be in the *Journal of Financial
  Economics* 111(1):1–25, **not RFS**.
- **Bertrand & Mullainathan, "Enjoying the Quiet Life" (2003)** — verified to be in the *Journal of
  Political Economy* 111(5):1043–1075, **not RFS** (a corporate-governance DID often mis-filed as a
  finance-journal paper).

Before adding any new paper to this library, confirm it on `academic.oup.com/rfs` (article page with
volume/issue) and that it is **RFS, not a sibling journal**; then update the access-date header. When in
doubt, omit.
