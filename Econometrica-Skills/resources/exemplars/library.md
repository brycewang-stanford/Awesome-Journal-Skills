# Econometrica Exemplars Library (method × topic)

> **Verified via web search, access date 2026-06-07.** Every paper below was checked against the
> Wiley Online Library *Econometrica* article pages (`onlinelibrary.wiley.com/...`) and/or JSTOR's
> *Econometrica* records to confirm it actually appeared in *Econometrica* — with year, volume, issue, and
> page range. Candidates that could not be fully verified as *Econometrica* were **omitted** (see the
> guardrail section): this is deliberately a short, clean list rather than a long, uncertain one.
>
> **Sibling-confusion guard.** *Econometrica* (Econometric Society / Wiley-Blackwell; ISSN 1468-0262) is
> **not** the *Journal of Econometrics* (Elsevier), *Econometric Theory* (Cambridge), *Quantitative
> Economics* (the Econometric Society's open-access sibling, ISSN 1759-7331), or the *Review of Economic
> Studies*. Each paper below was confirmed on a `1468-0262` / `10.3982/ECTA…` / Econometrica-JSTOR page, not
> a sibling journal.
>
> **Use principle (zero hallucination):** this file gives **design / positioning guidance only**. It does
> **not** reproduce or invent theorem statements, estimator formulas, regression coefficients, or specific
> findings — read the original on Wiley / JSTOR before citing any result or number. For Econometrica-specific
> policy, scope, format limits, and a do-not-misattribute list, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **method × question** is closest to yours, then study how that paper makes the
*estimator, theorem, or identification argument itself the contribution* — the Econometrica bar (see
[`../../skills/ecta-topic-selection/SKILL.md`](../../skills/ecta-topic-selection/SKILL.md) and
[`../../skills/ecta-writing-style/SKILL.md`](../../skills/ecta-writing-style/SKILL.md)). For each, ask the
self-check question before claiming your paper is "Econometrica-shaped." None of these is an off-the-shelf
application; each introduced a durable methodological or theoretical object.

---

## By method

### Generalized method of moments — estimation theory (econometric theory)

- **Hansen, "Large Sample Properties of Generalized Method of Moments Estimators," Econometrica 1982, 50(4):1029–1054.**
  Verified: JSTOR `stable/1912775`; Econometrica 50(4), 1982.
  - **Why it is an exemplar:** the *framework* — consistency, asymptotic normality, and the efficient
    weighting matrix for moment-condition estimators — *is* the contribution; the asymptotic theory is the
    product, not an application of it. The archetype of "estimator-plus-asymptotics as the paper."
  - **Self-check:** is your object a new estimator/test whose *limiting distribution and efficiency* you
    derive, rather than a known estimator applied to new data?

### HAC covariance estimation — inference theory (econometric theory)

- **Newey & West, "A Simple, Positive Semi-Definite, Heteroskedasticity and Autocorrelation Consistent Covariance Matrix," Econometrica 1987, 55(3):703–708.**
  Verified: JSTOR `stable/1913610`; Econometrica 55(3), May 1987.
  - **Why it is an exemplar:** a short, sharp methods note — a single positive-semidefinite covariance
    estimator licensing valid inference under serial correlation — shows Econometrica rewards a *clean
    inferential object* with proof, not length. Pairs with the robustness / SE-clustering discipline in
    [`../../../shared-resources/empirical-methods/reporting-standards.md`](../../../shared-resources/empirical-methods/reporting-standards.md).
  - **Self-check:** does your inference procedure come with the asymptotic theory that *justifies* it
    (`ecta-identification` Branch B), not just a claim that it "works"?

### Sample-selection identification + estimator (econometric theory / structural)

- **Heckman, "Sample Selection Bias as a Specification Error," Econometrica 1979, 47(1):153–161.**
  Verified: JSTOR `stable/1912352`; Econometrica 47(1), Jan 1979.
  - **Why it is an exemplar:** reframes selection as a specification (omitted-variable) problem and delivers
    a constructive correction — the *identification argument and the estimator* are the contribution, with
    behavioral payoff. See [`../../skills/ecta-identification/SKILL.md`](../../skills/ecta-identification/SKILL.md)
    Branch D.
  - **Self-check:** do you state the identifying restriction explicitly and show the structural object is a
    one-to-one image of the data distribution under it?

### Dynamic discrete choice — structural estimation (structural / empirical)

- **Rust, "Optimal Replacement of GMC Bus Engines: An Empirical Model of Harold Zurcher," Econometrica 1987, 55(5):999–1033.**
  Verified: Wiley DOI `10.2307/1911259`; Econometrica 55(5), 1987.
  - **Why it is an exemplar:** the *nested fixed-point* method for estimating a dynamic programming model —
    the methodological machinery, not the bus-engine application — is what carries the paper; the empirical
    setting is the vehicle. The model that an Econometrica structural submission should resemble.
  - **Self-check:** is your structural method (the estimator / the identification of the deep parameters)
    itself novel, or is it an off-the-shelf design with the estimand as the whole point (⇒ redirect per
    `ecta-topic-selection`)?

### Representation / decision theory under risk (microeconomic & decision theory)

- **Kahneman & Tversky, "Prospect Theory: An Analysis of Decision under Risk," Econometrica 1979, 47(2):263–291.**
  Verified: JSTOR `stable/1914185`; Econometrica 47(2), Mar 1979.
  - **Why it is an exemplar:** a behaviorally-grounded model of choice (value over gains/losses; decision
    weights) with observable, comparative-static content — Econometrica's decision-theory lane, where the
    formal representation and its behavioral payoff are the product (`ecta-identification` Branch C).
  - **Self-check:** are your axioms isolated, independent, and behaviorally interpretable, and does the
    representation pin the functional form up to its known degrees of freedom?

### LATE — identification of a causal estimand (econometric theory)

- **Imbens & Angrist, "Identification and Estimation of Local Average Treatment Effects," Econometrica 1994, 62(2):467–475.**
  Verified: JSTOR `stable/2951620`; Econometrica 62(2), Mar 1994.
  - **Why it is an exemplar:** defines *what* an IV estimand identifies (the LATE) under a monotonicity
    condition — the *identification result* is the contribution, independent of any one application. Shows
    Econometrica's framing of identification as a population-level object (`ecta-identification` Branch A).
  - **Self-check:** have you defined your parameter as a population functional and stated the numbered
    condition (here, monotonicity) under which it is identified, with the failure analyzed if dropped?

### Regression-discontinuity identification theory (econometric theory)

- **Hahn, Todd & van der Klaauw, "Identification and Estimation of Treatment Effects with a Regression-Discontinuity Design," Econometrica 2001, 69(1):201–209.**
  Verified: Wiley DOI `10.1111/1468-0262.00183`; Econometrica 69(1), Jan 2001.
  - **Why it is an exemplar:** puts RDD on a formal footing — *what* the discontinuity identifies in a
    potential-outcomes framework and the continuity conditions required — so the *identification theorem*,
    not an empirical RDD, is the contribution. The methods backbone behind off-the-shelf RDD; contrast with
    using RDD off the shelf (which `ecta-topic-selection` would redirect).
  - **Self-check:** does your design contribute a new identification/estimation *result*, or apply an
    existing one (the latter belongs in a general-interest applied venue)?

---

## By topic (each cell is a verified Econometrica paper above)

| Topic | Verified Econometrica exemplar | Year / vol(issue):pp | Method |
| --- | --- | --- | --- |
| Moment-condition estimation theory | Hansen, "Large Sample Properties of GMM Estimators" | 1982, 50(4):1029–1054 | GMM asymptotics |
| Robust inference / covariance estimation | Newey & West, "HAC Covariance Matrix" | 1987, 55(3):703–708 | HAC / inference theory |
| Selection & specification | Heckman, "Sample Selection Bias as a Specification Error" | 1979, 47(1):153–161 | Selection identification + estimator |
| Dynamic structural estimation | Rust, "Optimal Replacement of GMC Bus Engines" | 1987, 55(5):999–1033 | Nested fixed point / DDC |
| Decision under risk | Kahneman & Tversky, "Prospect Theory" | 1979, 47(2):263–291 | Representation / decision theory |
| Causal estimands / IV | Imbens & Angrist, "Local Average Treatment Effects" | 1994, 62(2):467–475 | LATE identification |
| Treatment effects at a threshold | Hahn, Todd & van der Klaauw, "Regression-Discontinuity" | 2001, 69(1):201–209 | RDD identification theory |

---

## Omitted / guardrails (do not attribute to Econometrica without re-checking)

To keep the list zero-hallucination, note the following:

- **Page ranges and issue numbers** above were taken from JSTOR / Wiley records during web search; a few
  classic papers are cited with slightly varying page spans across secondary sources. Confirm the exact
  span on the Wiley/JSTOR article page before quoting it in a reference list.
- **Sibling-journal traps explicitly avoided.** Do **not** add to this list, without re-verifying the
  venue, work that commonly appears in: *Journal of Econometrics* (Elsevier), *Econometric Theory*
  (Cambridge), *Quantitative Economics* (`10.3982/QE…` — the Econometric Society's *other*, open-access
  journal, easily confused because it shares the `10.3982` Wiley prefix), or the *Review of Economic
  Studies*. The `10.3982/QE…` DOI stem in particular is **Quantitative Economics, not Econometrica**
  (Econometrica uses `10.3982/ECTA…`).
- **Editor / board names, fees, and acceptance rates are volatile** and are *not* listed here; they live in
  [`../official-source-map.md`](../official-source-map.md) with their own re-verify warnings.

Before adding any new paper to this library, confirm it on `onlinelibrary.wiley.com` (an Econometrica article
page, DOI stem `10.3982/ECTA…` for recent work or `10.1111/1468-0262…` for older) or JSTOR's Econometrica
records, with volume/issue/pages, and update the access-date header. When in doubt, omit.
