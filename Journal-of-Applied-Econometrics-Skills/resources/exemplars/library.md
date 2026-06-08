# *Journal of Applied Econometrics* Exemplars Library (method × topic)

> **Verified via web search, access date 2026-06-08.** Every paper below was checked to confirm it
> actually appeared in the **_Journal of Applied Econometrics_** (JAE) — the Wiley journal founded in 1986
> (ISSN 0883-7252 print / 1099-1255 online) whose signature norm is the **JAE Data Archive** of
> replication data and code — with year and volume/issue, against the RePEc/IDEAS series record
> (`ideas.repec.org/a/jae/japmet/...`), the Wiley Online Library article page
> (`onlinelibrary.wiley.com/doi/.../jae...`), and, where available, the paper's own entry in the **JAE
> Data Archive** (`qed.econ.queensu.ca/jae/...`, now mirrored at `journaldata.zbw.eu`). Papers that could
> not be fully verified **as _Journal of Applied Econometrics_** were **omitted** — this is deliberately a
> short, clean list, not a long, uncertain one.
>
> **Sibling-journal guard.** The *Journal of Applied Econometrics* is **not** *Econometrica*, the
> *Journal of Econometrics*, the *Journal of Business & Economic Statistics*, the *Review of Economics and
> Statistics*, *Econometric Theory*, or the *American Economic Review*. Many famous "applied econometrics"
> papers — Diebold–Mariano predictive accuracy (JBES), Card–Krueger minimum wage (AER), Smets–Wouters
> DSGE (JEEA), Fernández-Villaverde–Rubio-Ramírez DSGE (JoE) — live in those venues, **not** JAE. The
> [Omitted](#omitted-for-lack-of-full-verification-do-not-attribute-to-the-journal-of-applied-econometrics)
> section records the traps checked and rejected.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent coefficients, forecast losses, or specific findings — read the original on Wiley (or
> re-run the deposited code in the JAE Data Archive) before citing any number. For JAE-specific scope, the
> 100-word summary cap, the 35-page limit, the Data Archive policy, and Wiley house style, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **method × applied question** is closest to yours, then study how that paper clears
the *JAE* bar: a credible **empirical strategy applied to real data**, with the estimand and identifying
assumptions stated, diagnostics that test them, and every number **reproducible** from deposited
data/code (see [`../../skills/jape-identification-strategy/SKILL.md`](../../skills/jape-identification-strategy/SKILL.md),
[`../../skills/jape-contribution-framing/SKILL.md`](../../skills/jape-contribution-framing/SKILL.md), and
[`../../skills/jape-replication-and-data-policy/SKILL.md`](../../skills/jape-replication-and-data-policy/SKILL.md)).
For each, ask the self-check question before claiming your paper is "*JAE*-shaped."

---

## By method

### Count-data models compared on a real outcome (microeconometrics / health)

- **Cameron & Trivedi, "Econometric Models Based on Count Data: Comparisons and Applications of Some Estimators and Tests," _Journal of Applied Econometrics_ 1986, 1(1):29–53.**
  Verified: RePEc `ideas.repec.org/a/wly/japmet/v1y1986i1p29-53.html`; Wiley `10.1002/jae.3950010104`.
  - **Why it is an exemplar:** does not propose a new theorem — it **applies and compares** Poisson,
    negative-binomial, and related count estimators and specification tests on a real health-utilization
    outcome, showing which assumptions matter empirically. The
    [`jape-contribution-framing`](../../skills/jape-contribution-framing/SKILL.md) "methodological
    application — the real-data demonstration is the payoff" contribution.
  - **Self-check:** is your contribution a *demonstration on real data* of when competing estimators agree
    or diverge, with the specification tests that adjudicate, rather than an asymptotics-only claim?

### Finite-mixture model for unobserved heterogeneity (microeconometrics / health demand)

- **Deb & Trivedi, "Demand for Medical Care by the Elderly: A Finite Mixture Approach," _Journal of Applied Econometrics_ 1997, 12(3):313–336.**
  Verified: Wiley `10.1002/(SICI)1099-1255(199705)12:3<313::AID-JAE440>3.0.CO;2-G`; JAE Data Archive `qed.econ.queensu.ca/jae/1997-v12.3/deb-trivedi/`.
  - **Why it is an exemplar:** models heterogeneous demand for medical care as a **finite mixture** of
    latent "healthy" and "ill" sub-populations, letting the data reveal the classes rather than imposing a
    single count process — an applied modeling choice justified by fit and interpretability, with code in
    the Data Archive ([`jape-replication-and-data-policy`](../../skills/jape-replication-and-data-policy/SKILL.md)).
  - **Self-check:** does your latent-class structure earn its complexity on the real data (fit,
    interpretability), and can a reader regenerate every estimate from your deposited programs?

### Bounds test for a long-run relationship (time series / cointegration)

- **Pesaran, Shin & Smith, "Bounds Testing Approaches to the Analysis of Level Relationships," _Journal of Applied Econometrics_ 2001, 16(3):289–326.**
  Verified: RePEc `ideas.repec.org/a/jae/japmet/v16y2001i3p289-326.html`; Wiley `10.1002/jae.616`.
  - **Why it is an exemplar:** gives an **ARDL bounds-testing** procedure for a level (long-run)
    relationship that is valid whether the regressors are I(0), I(1), or mutually cointegrated — a
    technique developed because applied series rarely come with known integration orders, then demonstrated
    on real data ([`jape-identification-strategy`](../../skills/jape-identification-strategy/SKILL.md)
    time-series design: handle unknown integration order rather than assume it away).
  - **Self-check:** does your time-series design stay valid under the integration-order ambiguity your real
    data actually have, with robustness to lag length shown?

### Bayesian evaluation of a structural model (macro-econometrics / DSGE)

- **Schorfheide, "Loss Function-Based Evaluation of DSGE Models," _Journal of Applied Econometrics_ 2000, 15(6):645–670.**
  Verified: RePEc `ideas.repec.org/a/jae/japmet/v15y2000i6p645-670.html`; Wiley `10.1002/jae.582`; ZBW Journal Data Archive replication entry.
  - **Why it is an exemplar:** confronts the reality that DSGE models are **misspecified** and proposes a
    Bayesian, loss-function-based procedure to evaluate and compare them against a reference model on real
    data — the [`jape-identification-strategy`](../../skills/jape-identification-strategy/SKILL.md)
    structural-design discipline (define the loss function and the comparison explicitly), not estimator
    branding.
  - **Self-check:** is your structural comparison stated as an explicit loss against a reference model on
    real data, acknowledging misspecification rather than treating the model as literally true?

### Panel unit-root test robust to cross-unit dependence (nonstationary panels)

- **Pesaran, "A Simple Panel Unit Root Test in the Presence of Cross-Section Dependence," _Journal of Applied Econometrics_ 2007, 22(2):265–312.**
  Verified: RePEc `ideas.repec.org/a/jae/japmet/v22y2007i2p265-312.html`; Wiley `10.1002/jae.951`.
  - **Why it is an exemplar:** augments unit-by-unit ADF regressions with **cross-sectional averages** to
    absorb a common factor, delivering a panel unit-root test usable when units are correlated — built for
    the dependence real macro panels exhibit, with finite-sample critical values supplied
    ([`jape-data-analysis`](../../skills/jape-data-analysis/SKILL.md)).
  - **Self-check:** does your panel procedure confront the cross-unit dependence your real data have, and
    do you supply the critical values an applied user needs to deploy it?

### Out-of-sample forecast comparison of many models (volatility forecasting)

- **Hansen & Lunde, "A Forecast Comparison of Volatility Models: Does Anything Beat a GARCH(1,1)?," _Journal of Applied Econometrics_ 2005, 20(7):873–889.**
  Verified: Wiley `10.1002/jae.800`; JSTOR `25146403`; RePEc `jae/japmet`.
  - **Why it is an exemplar:** a disciplined **out-of-sample horse race** across a large set of volatility
    models on real exchange-rate and equity data, with the comparison conducted under an explicit loss and
    a multiple-model test rather than cherry-picked fit — the
    [`jape-contribution-framing`](../../skills/jape-contribution-framing/SKILL.md) "a modest reproducible
    finding, honestly bounded, beats an overclaimed fragile one" stance.
  - **Self-check:** is your forecast comparison run under a stated loss and a test that controls for
    searching across many models, on out-of-sample data, with the code deposited?

---

## By topic (each cell is a verified _Journal of Applied Econometrics_ paper above)

| Topic | Verified _JAE_ exemplar | Year / vol(issue) | Method |
| --- | --- | --- | --- |
| Health / count-data microeconometrics | Cameron & Trivedi, "Econometric Models Based on Count Data" | 1986, 1(1) | Count-model comparison + specification tests |
| Health-care demand / heterogeneity | Deb & Trivedi, "Demand for Medical Care by the Elderly" | 1997, 12(3) | Finite-mixture (latent-class) count model |
| Time-series cointegration | Pesaran, Shin & Smith, "Bounds Testing Approaches" | 2001, 16(3) | ARDL bounds test for level relationships |
| Macro / DSGE evaluation | Schorfheide, "Loss Function-Based Evaluation of DSGE Models" | 2000, 15(6) | Bayesian loss-based model comparison |
| Nonstationary panels | Pesaran, "A Simple Panel Unit Root Test" | 2007, 22(2) | Cross-sectionally augmented panel unit root |
| Volatility forecasting | Hansen & Lunde, "Does Anything Beat a GARCH(1,1)?" | 2005, 20(7) | Out-of-sample multi-model forecast comparison |

---

## Omitted for lack of full verification (do not attribute to the *Journal of Applied Econometrics*)

To keep the list zero-hallucination, these strong candidates were **excluded** after web-checking — each
is a real, important applied paper, but **not in the _Journal of Applied Econometrics_** (the
sibling-journal traps the brief warned of):

- **Diebold & Mariano, "Comparing Predictive Accuracy" (1995)** — verified in the **_Journal of Business
  & Economic Statistics_** 13(3):253–263, **not _JAE_**. The canonical forecast-comparison test.
- **Card & Krueger, "Minimum Wages and Employment: A Case Study of the Fast-Food Industry…" (1994)** —
  verified in the **_American Economic Review_** 84(4):772–793, **not _JAE_**.
- **Smets & Wouters, "An Estimated Dynamic Stochastic General Equilibrium Model of the Euro Area"
  (2003)** — verified in the **_Journal of the European Economic Association_** 1(5):1123–1175, **not
  _JAE_**.
- **Fernández-Villaverde & Rubio-Ramírez, "Comparing Dynamic Equilibrium Models to Data: A Bayesian
  Approach" (2004)** — verified in the **_Journal of Econometrics_** 123(1):153–187, **not _JAE_**.
- **Geweke, "Using Simulation Methods for Bayesian Econometric Models…" (1999)** — verified in
  **_Econometric Reviews_** 18(1):1–126, **not _JAE_**.

Before adding any new paper to this library, confirm it on `ideas.repec.org/a/jae/japmet/...`, the Wiley
Online Library page, and — ideally — its JAE Data Archive entry, with volume/issue, and update the
access-date header. When in doubt, **omit**.
