# QE Exemplars Library (method × topic)

> **Verified via web search, access date 2026-06-08.** Every paper below was checked to confirm it
> actually appeared in ***Quantitative Economics*** (the Econometric Society's open-access journal,
> published with Wiley) and carries a **`10.3982/QE…` DOI stem** — the marker that confirms QE
> specifically. Year, volume(issue), and pages were read off the Wiley / Econometric Society article
> pages. Papers lacking complete QE verification were **omitted** — this is deliberately a short,
> clean list rather than a long, uncertain one.
>
> **Sibling-confusion guard (do not misattribute).** QE is **not** any of these, which share parts of the
> 10.3982 prefix or the subject area:
> *Econometrica* (`10.3982/ECTA…`), *Theoretical Economics* (`10.3982/TE…`), the *Journal of
> Econometrics*, or the *Journal of Applied Econometrics*. Only the **`10.3982/QE…`** stem confirms QE.
> The omissions section below records a paper excluded on exactly this ground.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent structural parameters, estimates, or specific findings — read the original before
> citing any number. For QE-specific policy, scope, and house rules, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **method × question** is closest to yours, then study how that paper makes a
*quantitatively serious* result answer a *substantive, general-interest* economic question — the QE bar
(see [`../../skills/qe-topic-selection/SKILL.md`](../../skills/qe-topic-selection/SKILL.md) and
[`../../skills/qe-writing-style/SKILL.md`](../../skills/qe-writing-style/SKILL.md)). For each, ask the
self-check question before claiming your paper is "QE-shaped." Remember QE's house rule: report **standard
errors / coverage sets, never significance asterisks**
([`qe-identification-strategy`](../../skills/qe-identification-strategy/SKILL.md)).

---

## By method

### Structural / computational macro with microdata (heterogeneous-agent calibration)

- **Carroll, Slacalek, Tokuoka & White, "The Distribution of Wealth and the Marginal Propensity to Consume," QE 2017, 8(3):977–1020.**
  Verified: `onlinelibrary.wiley.com/doi/10.3982/QE694` (DOI `10.3982/QE694`).
  - **Why it is an exemplar:** a realistically calibrated buffer-stock model is disciplined by micro and
    macro evidence, then delivers a first-order *quantity* — the aggregate marginal propensity to consume —
    and links it to the wealth distribution. Method and answer reinforce each other, the QE sweet spot.
    Routes to [`../../skills/qe-data-analysis/SKILL.md`](../../skills/qe-data-analysis/SKILL.md)
    (computation + calibration discipline).
  - **Self-check:** does your model map to micro evidence and deliver one memorable, policy-relevant
    quantity, rather than a calibration with no headline number?

### Time-series / SVAR macro-econometrics (asymmetry & nonlinearity)

- **Kilian & Vigfusson, "Are the Responses of the U.S. Economy Asymmetric in Energy Price Increases and Decreases?," QE 2011, 2(3):419–453.**
  Verified: `onlinelibrary.wiley.com/doi/abs/10.3982/QE99` (DOI `10.3982/QE99`).
  - **Why it is an exemplar:** confronts a substantive macro question (are oil-price effects asymmetric?)
    with the right nonlinear-impulse-response apparatus, showing how much of an apparent regularity is an
    artifact of method — a quantitative method *changing the economic answer*.
  - **Self-check:** does your econometric choice change the substantive conclusion, and have you shown that
    explicitly rather than assuming the linear case?

### Structural micro-econometrics of strategic behavior (games, partial identification)

- **Kline, "An Empirical Model of Non-Equilibrium Behavior in Games," QE 2018, 9(1):141–181.**
  Verified: `onlinelibrary.wiley.com/doi/pdf/10.3982/QE647` (DOI `10.3982/QE647`).
  - **Why it is an exemplar:** builds an empirical model whose behavioral assumptions are weaker than Nash
    equilibrium and confronts it with data — a quantitative-method contribution that stays anchored to a
    substantive question about how people actually play, not a pure estimator.
  - **Self-check:** is your weakening of a standard assumption *identified* from data features you can
    name, with the estimand stated?

### Panel data econometrics with unobserved heterogeneity (distributional effects)

- **Fernández-Val & Lee, "Panel Data Models with Nonadditive Unobserved Heterogeneity: Estimation and Inference," QE 2013, 4(3):453–481.**
  Verified: `onlinelibrary.wiley.com/doi/abs/10.3982/QE75` (DOI `10.3982/QE75`).
  - **Why it is an exemplar:** develops fixed-effects estimation and bias-corrected inference for moments
    of random coefficients in short panels — a methods contribution QE publishes because it is built to be
    *applied* to substantive heterogeneity questions, with the incidental-parameter problem confronted
    head-on. Connects to
    [`../../skills/qe-identification-strategy/SKILL.md`](../../skills/qe-identification-strategy/SKILL.md).
  - **Self-check:** if your contribution is methodological, is it framed for a substantive application and
    is its inference (bias, coverage) honestly characterized?

### Distributional causal inference / difference-in-differences (quantile treatment effects)

- **Callaway & Li, "Quantile Treatment Effects in Difference in Differences Models with Panel Data," QE 2019, 10(4):1579–1618.**
  Verified: `onlinelibrary.wiley.com/doi/abs/10.3982/QE935` (DOI `10.3982/QE935`).
  - **Why it is an exemplar:** extends DiD beyond a single average effect to the *quantile* treatment
    effect on the treated under an explicit copula-stability assumption — a credibly identified
    distributional magnitude, exactly the
    [`qe-identification-strategy`](../../skills/qe-identification-strategy/SKILL.md) Branch B bar
    (modern DiD, assumptions stated, bootstrap inference). Pairs with
    [`../code/stata/03_did_modern.do`](../code/stata/03_did_modern.do).
  - **Self-check:** does your design identify the full *distribution* of effects (not just the mean), and
    is the extra identifying assumption stated and defended?

### Inference under dependence (bootstrap / spatial & cross-sectional dependence)

- **Conley, Gonçalves, Kim & Perron, "Bootstrap Inference under Cross-Sectional Dependence," QE 2023, 14(2):511–569.**
  Verified: `onlinelibrary.wiley.com/doi/abs/10.3982/QE1626` (DOI `10.3982/QE1626`).
  - **Why it is an exemplar:** a "spatial dependent wild bootstrap" gives valid inference when
    cross-sectional/spatial dependence has an unknown pattern — precisely the inference discipline QE's
    house rules demand (standard errors / coverage sets that are actually valid, not asterisks on
    mis-specified standard errors).
  - **Self-check:** is your inference valid under the dependence your data actually exhibit, or are you
    reporting standard errors that assume away clustering/spatial correlation?

---

## By topic (each cell is a verified QE paper above)

| Topic | Verified QE exemplar | Year / vol(issue) | Method | DOI |
| --- | --- | --- | --- | --- |
| Wealth distribution & consumption | Carroll, Slacalek, Tokuoka & White, "Distribution of Wealth and MPC" | 2017, 8(3) | Structural / calibrated HA model | 10.3982/QE694 |
| Oil prices & the macroeconomy | Kilian & Vigfusson, "Asymmetric Responses to Energy Prices" | 2011, 2(3) | Nonlinear SVAR / impulse responses | 10.3982/QE99 |
| Strategic behavior in games | Kline, "Non-Equilibrium Behavior in Games" | 2018, 9(1) | Structural micro-econometrics / partial ID | 10.3982/QE647 |
| Heterogeneity in panels | Fernández-Val & Lee, "Nonadditive Unobserved Heterogeneity" | 2013, 4(3) | Panel data / bias-corrected inference | 10.3982/QE75 |
| Distributional treatment effects | Callaway & Li, "Quantile Treatment Effects in DiD" | 2019, 10(4) | Distributional DiD / quantile | 10.3982/QE935 |
| Inference under dependence | Conley, Gonçalves, Kim & Perron, "Bootstrap under Cross-Sectional Dependence" | 2023, 14(2) | Bootstrap / spatial inference | 10.3982/QE1626 |

---

## Omitted for lack of full verification, or to avoid sibling-confusion (do not attribute to QE without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking:

- **Arcidiacono & Miller, "Conditional Choice Probability Estimation of Dynamic Discrete Choice Models
  with Unobserved Heterogeneity" (2011)** — a natural structural-econometrics candidate, but web search
  confirms it is in ***Econometrica*** (79(6):1823–1867, DOI `10.3982/ECTA7743`), **not QE**. Listed here
  only as a sibling-confusion guardrail: the `ECTA` stem, not `QE`, is the tell.
- Several frequently-cited QE-area methods papers (e.g., additional quantile/panel and bootstrap pieces
  surfaced in search) were left off because their **exact QE volume/issue/pages** did not meet the same
  verification standard in one pass; add them only after reading the Wiley / Econometric Society article
  page and confirming the `10.3982/QE…` DOI.

Before adding any new paper to this library, confirm it on `onlinelibrary.wiley.com` or
`econometricsociety.org` (article page with volume/issue/pages) **and** that the DOI begins `10.3982/QE`,
then update the access-date header. When in doubt, omit.
