# *Journal of Econometrics* Exemplars Library (method × topic)

> **Verified via web search, access date 2026-06-08.** Every paper below was checked to confirm it
> actually appeared in the **_Journal of Econometrics_** (JoE) — the Elsevier (North-Holland) methodology
> journal founded in 1973, ISSN 0304-4076 — with year and volume/issue, against the RePEc/IDEAS series
> record (`ideas.repec.org/a/eee/econom/...`), the Elsevier ScienceDirect article page
> (`sciencedirect.com/.../0304-4076`), and corroborating author-hosted PDFs and Google Scholar lookups
> carrying the journal name. Papers that could not be fully verified **as _Journal of Econometrics_** were
> **omitted** — this is deliberately a short, clean list, not a long, uncertain one.
>
> **Sibling-journal guard.** The *Journal of Econometrics* is **not** *Econometrica*, *Econometric
> Theory*, the *Review of Economics and Statistics*, the *Journal of Applied Econometrics*, the *Journal
> of Business & Economic Statistics*, or the *International Economic Review*. Many famous "econometrics
> methodology" papers — GMM (Hansen 1982), cointegration (Engle–Granger 1987), ARCH (Engle 1982), HAC
> (Andrews 1991; Newey–West 1994), the ARDL bounds test (Pesaran–Shin–Smith 2001) — live in those venues,
> **not** JoE. The [Omitted](#omitted-for-lack-of-full-verification-do-not-attribute-to-the-journal-of-econometrics)
> section records the traps checked and rejected.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent theorems, rates, coefficients, or Monte Carlo numbers — read the original on
> ScienceDirect before citing any result. For JoE-specific scope, fees, length norms, and Elsevier house
> style, see [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **method × econometric problem** is closest to yours, then study how that paper turns
an estimation/inference problem into a contribution that clears the *JoE* bar: a **formal core** —
estimand, identification, assumptions, asymptotics, and finite-sample evidence — that generalizes beyond
a convenient special case (see [`../../skills/joe-identification-strategy/SKILL.md`](../../skills/joe-identification-strategy/SKILL.md),
[`../../skills/joe-contribution-framing/SKILL.md`](../../skills/joe-contribution-framing/SKILL.md), and
[`../../skills/joe-writing-style/SKILL.md`](../../skills/joe-writing-style/SKILL.md)). For each, ask the
self-check question before claiming your paper is "*JoE*-shaped."

---

## By method

### Asymptotic theory for nonstationary regressions (time series / unit roots)

- **Phillips, "Understanding Spurious Regressions in Econometrics," _Journal of Econometrics_ 1986, 33(3):311–340.**
  Verified: RePEc `ideas.repec.org/a/eee/econom/v33y1986i3p311-340.html`; ScienceDirect `10.1016/0304-4076(86)90001-1`.
  - **Why it is an exemplar:** derives the **limiting behavior** of regression statistics when independent
    I(1) series are regressed on one another — t-ratios that diverge, an R² that does not vanish — turning
    a folk warning into a precise functional-central-limit result. The
    [`joe-identification-strategy`](../../skills/joe-identification-strategy/SKILL.md) move: state the DGP,
    derive the asymptotics honestly, and show *why* standard inference fails rather than asserting it.
  - **Self-check:** can you write down the limiting distribution of your statistic under the stated DGP,
    and show exactly where conventional inference breaks?

### Conditional-variance modeling (volatility / financial time series)

- **Bollerslev, "Generalized Autoregressive Conditional Heteroskedasticity," _Journal of Econometrics_ 1986, 31(3):307–327.**
  Verified: RePEc `ideas.repec.org/a/eee/econom/v31y1986i3p307-327.html`; author-hosted PDF reading "Journal of Econometrics 31 (1986) 307–327. North-Holland."
  - **Why it is an exemplar:** generalizes ARCH by letting the conditional variance depend on its own
    lags, defining a parsimonious **GARCH** parameterization, then giving stationarity conditions and an
    estimation/inference scheme — a new model class with its properties worked out, the
    [`joe-contribution-framing`](../../skills/joe-contribution-framing/SKILL.md) "name and characterize a
    new estimator/model" contribution.
  - **Self-check:** is your proposed parameterization more parsimonious than the incumbent *and* delivered
    with existence/stationarity conditions and a usable estimator, not just a fitted example?

### GMM for dynamic panels (panel data / error components)

- **Arellano & Bover, "Another Look at the Instrumental Variable Estimation of Error-Components Models," _Journal of Econometrics_ 1995, 68(1):29–51.**
  Verified: RePEc `ideas.repec.org/a/eee/econom/v68y1995i1p29-51.html`; ScienceDirect `10.1016/0304-4076(94)01642-D`.
  - **Why it is an exemplar:** reframes error-components estimation through a **unified GMM/instrument
    framework**, showing how level and forward-orthogonal-deviation moment conditions can be combined to
    restore identification when lagged-difference instruments are weak — the
    [`joe-identification-strategy`](../../skills/joe-identification-strategy/SKILL.md) "find the valid
    moment conditions and prove what they identify" move.
  - **Self-check:** are your moment conditions stated explicitly, their validity argued from the model,
    and the efficiency gain over the incumbent set demonstrated rather than asserted?

### Pooled testing across heterogeneous units (nonstationary panels)

- **Im, Pesaran & Shin, "Testing for Unit Roots in Heterogeneous Panels," _Journal of Econometrics_ 2003, 115(1):53–74.**
  Verified: RePEc `ideas.repec.org/a/eee/econom/v115y2003i1p53-74.html`; ScienceDirect `10.1016/S0304-4076(03)00092-7`.
  - **Why it is an exemplar:** builds a panel unit-root test that **averages unit-specific statistics**
    while allowing the autoregressive root to differ across units, derives the limiting null distribution,
    and tabulates finite-sample critical values via simulation — theory plus the Monte Carlo that makes it
    usable ([`joe-data-analysis`](../../skills/joe-data-analysis/SKILL.md) size/power discipline).
  - **Self-check:** does your test allow the heterogeneity it claims to, and do you supply the null
    distribution *and* finite-sample critical values a practitioner can apply?

### Identification-robust inference for quantile effects (quantile / treatment effects)

- **Chernozhukov & Hansen, "Instrumental Quantile Regression Inference for Structural and Treatment Effect Models," _Journal of Econometrics_ 2006, 132(2):491–525.**
  Verified: RePEc `ideas.repec.org/a/eee/econom/v132y2006i2p491-525.html`; ScienceDirect `10.1016/j.jeconom.2005.02.009`.
  - **Why it is an exemplar:** develops **inference** (not just point estimation) for instrumental-variable
    quantile regression that stays valid when instruments are weak or the parameter is partially
    identified — confidence regions obtained by inverting a test, exactly the
    [`joe-identification-strategy`](../../skills/joe-identification-strategy/SKILL.md) "give
    identification-robust inference where the design is on its boundary" prescription.
  - **Self-check:** does your inference remain valid under weak identification, and do you report a test to
    invert rather than only a Wald interval that assumes strong identification?

### GMM/IV estimation under spatial dependence (spatial econometrics)

- **Kelejian & Prucha, "Specification and Estimation of Spatial Autoregressive Models with Autoregressive and Heteroskedastic Disturbances," _Journal of Econometrics_ 2010, 157(1):53–67.**
  Verified: RePEc `ideas.repec.org/a/eee/econom/v157y2010i1p53-67.html`; ScienceDirect `10.1016/j.jeconom.2009.10.025`.
  - **Why it is an exemplar:** generalizes GMM estimation of a Cliff–Ord spatial model to allow **unknown
    heteroskedasticity** in the innovations, defines IV estimators for the regression parameters, and
    derives their **joint asymptotic distribution** — primitive conditions and a consistent variance
    estimator, the [`joe-identification-strategy`](../../skills/joe-identification-strategy/SKILL.md)
    "relax a convenient assumption and re-derive the asymptotics" move.
  - **Self-check:** when you relax the assumption your incumbent relied on (here, homoskedasticity), do you
    re-derive the limiting distribution and supply a variance estimator that is consistent under the
    weaker conditions?

---

## By topic (each cell is a verified _Journal of Econometrics_ paper above)

| Topic | Verified _JoE_ exemplar | Year / vol(issue) | Method |
| --- | --- | --- | --- |
| Nonstationary time series | Phillips, "Understanding Spurious Regressions" | 1986, 33(3) | Functional-CLT asymptotics for I(1) regressions |
| Volatility / financial econometrics | Bollerslev, "Generalized ARCH" | 1986, 31(3) | Conditional-variance (GARCH) modeling |
| Dynamic panel data | Arellano & Bover, "Another Look at IV Estimation of Error-Components Models" | 1995, 68(1) | GMM with level + orthogonal-deviation moments |
| Nonstationary panels | Im, Pesaran & Shin, "Testing for Unit Roots in Heterogeneous Panels" | 2003, 115(1) | Averaged panel unit-root test + simulated critical values |
| Quantile / treatment effects | Chernozhukov & Hansen, "Instrumental Quantile Regression Inference" | 2006, 132(2) | Identification-robust IV quantile inference |
| Spatial econometrics | Kelejian & Prucha, "Spatial Autoregressive Models with Heteroskedastic Disturbances" | 2010, 157(1) | GMM/IV under unknown heteroskedasticity |

---

## Omitted for lack of full verification (do not attribute to the *Journal of Econometrics*)

To keep the list zero-hallucination, these strong candidates were **excluded** after web-checking — each
is a real, important methodology paper, but **not in the _Journal of Econometrics_** (the sibling-journal
traps the brief warned of):

- **Hansen, "Large Sample Properties of Generalized Method of Moments Estimators" (1982)** — verified in
  **_Econometrica_** 50(4):1029–1054, **not _JoE_**. The canonical GMM paper.
- **Engle & Granger, "Co-integration and Error Correction: Representation, Estimation, and Testing"
  (1987)** — verified in **_Econometrica_** 55(2):251–276, **not _JoE_**.
- **Engle, "Autoregressive Conditional Heteroscedasticity with Estimates of the Variance of United
  Kingdom Inflation" (1982)** — verified in **_Econometrica_** 50(4):987–1007, **not _JoE_**. (The ARCH
  paper Bollerslev 1986, which *is* JoE, generalizes.)
- **Andrews, "Heteroskedasticity and Autocorrelation Consistent Covariance Matrix Estimation" (1991)** —
  verified in **_Econometrica_** 59(3):817–858, **not _JoE_**.
- **Newey & West, "Automatic Lag Selection in Covariance Matrix Estimation" (1994)** — verified in the
  **_Review of Economic Studies_** 61(4):631–653, **not _JoE_**.
- **Pesaran, Shin & Smith, "Bounds Testing Approaches to the Analysis of Level Relationships" (2001)** —
  verified in the **_Journal of Applied Econometrics_** 16(3):289–326, **not _JoE_**. The ARDL bounds test.
- **Chernozhukov & Hansen, "An IV Model of Quantile Treatment Effects" (2005)** — verified in
  **_Econometrica_** 73(1):245–261, **not _JoE_**; their *JoE* companion (2006, above) is the
  inference paper.

Before adding any new paper to this library, confirm it on `ideas.repec.org/a/eee/econom/...` and the
Elsevier ScienceDirect page (ISSN 0304-4076) with volume/issue, and update the access-date header. When
in doubt, **omit**.
