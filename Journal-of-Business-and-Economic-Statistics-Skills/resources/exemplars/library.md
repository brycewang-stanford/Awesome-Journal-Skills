# *Journal of Business & Economic Statistics* Exemplars Library (method × topic)

> **Verified via web search, access date 2026-06-08.** Every paper below was checked to confirm it
> actually appeared in the **_Journal of Business & Economic Statistics_** (JBES) — published by
> **Taylor & Francis on behalf of the American Statistical Association (ASA)**, founded 1983, ISSN
> 0735-0015 (print) / 1537-2707 (online) — with year and volume/issue, against the RePEc/IDEAS series
> records (`ideas.repec.org/a/bes/jnlbes/...` for older volumes and `ideas.repec.org/a/taf/jnlbes/...`
> for the Taylor & Francis era), the Taylor & Francis Online article page
> (`tandfonline.com/doi/.../07350015...`), and corroborating author-hosted PDFs. Papers that could not be
> fully verified **as _JBES_** were **omitted** — this is deliberately a short, clean list, not a long,
> uncertain one.
>
> **Sibling-journal guard.** JBES is **not** *Econometrica*, the *Journal of Econometrics*, the *Journal
> of Applied Econometrics*, the *Journal of the American Statistical Association* (JASA — its ASA
> sibling), *Econometric Theory*, the *International Economic Review*, or the *Annals of Statistics*. Many
> famous "business/economic statistics" papers — Hamilton's regime-switching (JoE), Andersen–Bollerslev–
> Diebold–Labys realized volatility (Econometrica; the 2001 distribution paper is JASA), Patton's
> time-varying copula (IER), Athey–Tibshirani–Wager generalized random forests (Annals of Statistics) —
> live in those venues, **not** JBES. The
> [Omitted](#omitted-for-lack-of-full-verification-do-not-attribute-to-jbes) section records the traps
> checked and rejected. (Note especially: the Diebold–Mariano test is JBES, **not** JAE.)
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent critical values, coefficients, or Monte Carlo numbers — read the original on Taylor
> & Francis before citing any result. For JBES-specific scope (methodology with *clear empirical
> relevance*, ML/data-science adaptation welcome), the ASA data-and-code expectation, and the
> invited-discussion tradition, see [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **method × empirical question** is closest to yours, then study how that paper clears
the *JBES* bar: a **method-level contribution paired with clear empirical relevance** — a new
estimator/test/algorithm with its validity (assumptions, asymptotics, size/power), Monte Carlo evidence,
and a substantive application (see [`../../skills/jbes-contribution-framing/SKILL.md`](../../skills/jbes-contribution-framing/SKILL.md),
[`../../skills/jbes-identification-strategy/SKILL.md`](../../skills/jbes-identification-strategy/SKILL.md), and
[`../../skills/jbes-data-analysis/SKILL.md`](../../skills/jbes-data-analysis/SKILL.md)). For each, ask the
self-check question before claiming your paper is "*JBES*-shaped."

---

## By method

### Tests for a unit root with an unknown trend break (time series / nonstationarity)

- **Banerjee, Lumsdaine & Stock, "Recursive and Sequential Tests of the Unit-Root and Trend-Break Hypotheses: Theory and International Evidence," _Journal of Business & Economic Statistics_ 1992, 10(3):271–287.**
  Verified: T&F `10.1080/07350015.1992.10509905`; RePEc `bes/jnlbes`.
  - **Why it is an exemplar:** develops **recursive, rolling, and sequential** test statistics for a unit
    root when the trend-break date is unknown a priori, derives their asymptotic distributions, and
    applies them to international macro data — the
    [`jbes-identification-strategy`](../../skills/jbes-identification-strategy/SKILL.md) "new test: null,
    limiting distribution, and an application the method is built for" shape (novelty × empirical
    relevance).
  - **Self-check:** does your test treat the nuisance feature (here, an unknown break date) honestly in
    the limiting theory, and is it demonstrated on the data it was built to handle?

### A test for equal predictive accuracy (forecast evaluation)

- **Diebold & Mariano, "Comparing Predictive Accuracy," _Journal of Business & Economic Statistics_ 1995, 13(3):253–263.**
  Verified: RePEc `ideas.repec.org/a/bes/jnlbes/v13y1995i3p253-63.html` (EconPapers `bes:jnlbes:v:13:y:1995:i:3:p:253-63`); T&F.
  - **Why it is an exemplar:** proposes a test of equal forecast accuracy under a **general loss function**
    (need not be quadratic or symmetric) with errors that may be non-Gaussian and serially correlated —
    one organizing methodological claim with immediate empirical use, the
    [`jbes-contribution-framing`](../../skills/jbes-contribution-framing/SKILL.md) "method advance + what
    practitioners can now do" template.
  - **Self-check:** is your inferential tool stated for the realistic conditions practitioners face (here,
    arbitrary loss, dependent errors), not just the textbook case?

### Finite-sample comparison of competing estimators (GMM / asset pricing)

- **Hansen, Heaton & Yaron, "Finite-Sample Properties of Some Alternative GMM Estimators," _Journal of Business & Economic Statistics_ 1996, 14(3):262–280.**
  Verified: T&F `10.1080/07350015.1996.10524656`; RePEc `bes/jnlbes`; author-hosted PDF.
  - **Why it is an exemplar:** compares iterated, two-step, and continuous-updating GMM in **finite
    samples** on an asset-pricing application, showing where each is biased or poorly sized — the
    [`jbes-data-analysis`](../../skills/jbes-data-analysis/SKILL.md) Monte-Carlo-plus-application
    discipline (size, bias, breakdown shown, not hidden) that JBES rewards.
  - **Self-check:** does your simulation reveal where the competing estimators *break*, across DGPs and
    sample sizes, rather than only confirm good behavior under a favorable design?

### Computable asymptotic p-values for a class of tests (structural change)

- **Hansen, "Approximate Asymptotic P-Values for Structural-Change Tests," _Journal of Business & Economic Statistics_ 1997, 15(1):60–67.**
  Verified: RePEc `ideas.repec.org/a/bes/jnlbes/v15y1997i1p60-67.html`; T&F `10.1080/07350015.1997.10524687`.
  - **Why it is an exemplar:** turns structural-change tests whose limiting distributions are awkward into
    a **usable tool** by approximating their asymptotic distributions so p-values are easy to compute —
    the [`jbes-contribution-framing`](../../skills/jbes-contribution-framing/SKILL.md) "computational
    improvement that makes an existing method feasible for practitioners" contribution type.
  - **Self-check:** does your computational contribution preserve the target (same test) while making it
    deployable, with accuracy of the approximation demonstrated?

### Shrinkage forecasting with many predictors (data science × macro forecasting)

- **Stock & Watson, "Generalized Shrinkage Methods for Forecasting Using Many Predictors," _Journal of Business & Economic Statistics_ 2012, 30(4):481–493.**
  Verified: RePEc `ideas.repec.org/a/taf/jnlbes/v30y2012i4p481-493.html`; T&F.
  - **Why it is an exemplar:** unifies and compares **shrinkage/regularization** forecasting methods
    (Bayesian model averaging, bagging, ridge-type rules) in a many-predictor macro setting — the JBES
    welcome of **machine-learning/data-science adaptation with clear empirical relevance**
    ([`jbes-topic-selection`](../../skills/jbes-topic-selection/SKILL.md)), evaluated out-of-sample rather
    than by in-sample fit.
  - **Self-check:** if you adapt a data-science method, do you frame the *methodological* delta and show
    its empirical payoff out-of-sample, rather than report an in-sample improvement?

---

## By topic (each cell is a verified _JBES_ paper above)

| Topic | Verified _JBES_ exemplar | Year / vol(issue) | Method |
| --- | --- | --- | --- |
| Nonstationary time series | Banerjee, Lumsdaine & Stock, "Recursive and Sequential Tests…" | 1992, 10(3) | Unit-root tests with unknown trend break |
| Forecast evaluation | Diebold & Mariano, "Comparing Predictive Accuracy" | 1995, 13(3) | Equal-predictive-accuracy test under general loss |
| GMM / asset pricing | Hansen, Heaton & Yaron, "Finite-Sample Properties of GMM Estimators" | 1996, 14(3) | Finite-sample estimator comparison + application |
| Structural change | Hansen, "Approximate Asymptotic P-Values for Structural-Change Tests" | 1997, 15(1) | Computable asymptotic p-values |
| Macro forecasting / data science | Stock & Watson, "Generalized Shrinkage Methods…" | 2012, 30(4) | Shrinkage/regularization forecasting, many predictors |

---

## Omitted for lack of full verification (do not attribute to *JBES*)

To keep the list zero-hallucination, these strong candidates were **excluded** after web-checking — each
is a real, important methods paper, but **not in _JBES_** (the sibling-journal traps the brief warned of):

- **Hamilton, "Analysis of Time Series Subject to Changes in Regime" (1990)** — verified in the
  **_Journal of Econometrics_** 45(1–2):39–70, **not _JBES_**. The Markov regime-switching estimation
  paper.
- **Andersen, Bollerslev, Diebold & Labys, "Modeling and Forecasting Realized Volatility" (2003)** —
  verified in **_Econometrica_** 71(2):579–625, **not _JBES_**; their 2001 "The Distribution of Realized
  Exchange Rate Volatility" is in **_JASA_** 96(453):42–55, **not _JBES_**.
- **Patton, "Modelling Asymmetric Exchange Rate Dependence" (2006)** — verified in the **_International
  Economic Review_** 47(2):527–556, **not _JBES_**. The canonical time-varying-copula paper.
- **Athey, Tibshirani & Wager, "Generalized Random Forests" (2019)** — verified in the **_Annals of
  Statistics_** 47(2):1148–1178, **not _JBES_**.
- **Chernozhukov, Chetverikov, Demirer, Duflo, Hansen, Newey & Robins, "Double/Debiased Machine Learning
  for Treatment and Structural Parameters" (2018)** — verified in the **_Econometrics Journal_**
  21(1):C1–C68, **not _JBES_**.

Before adding any new paper to this library, confirm it on `ideas.repec.org/a/bes/jnlbes/...` or
`.../a/taf/jnlbes/...` and the Taylor & Francis page (ISSN 0735-0015) with volume/issue, and update the
access-date header. When in doubt, **omit**.
