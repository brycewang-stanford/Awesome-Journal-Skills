# Exemplar Library — *Econometric Theory*

> **Verified via web search, access date 2026-06-13.** Every paper below was checked against its
> **Cambridge Core article page** (`cambridge.org/core/journals/econometric-theory/...`) and/or its
> registered **DOI (`10.1017/S0266466…`, the Econometric Theory stem)** to confirm it actually appeared
> in *Econometric Theory* (Cambridge University Press), with year, volume(issue), and pages. Candidates
> that could not be confirmed *as Econometric Theory* were **omitted** and documented below — this is a
> short, clean list, not a long, uncertain one. **6 verified > 15 guessed.**
>
> **Sibling-confusion guard.** *Econometric Theory* (Cambridge UP) is NOT: *Journal of Econometrics*
> (Elsevier), *Econometrica* (Econometric Society / Wiley), *Journal of Business & Economic Statistics*
> (ASA), or *The Econometrics Journal* (RES / Oxford). Asymptotic-theory, unit-root/cointegration, and
> robust-inference papers are split across these venues — several landmark results that *look* like ET
> live in siblings (see the omissions section). Verify the Cambridge Core page / `10.1017/S0266466…` DOI
> before listing anything.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent theorems, rates, constants, or proofs — read the original on Cambridge Core before
> citing any result. For venue scope, manuscript specs, and house style, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

*Econometric Theory* is a **methods-theory** venue: the contribution is a **theorem** — a new estimator,
test, or limit result stated with explicit assumptions and a rigorously derived asymptotic distribution;
Monte Carlo evidence *supports* the theory, it is not the contribution (see
[`../../skills/ectheory-data-analysis/SKILL.md`](../../skills/ectheory-data-analysis/SKILL.md)). Pick the
row whose **kind of contribution × problem** is closest to yours, then study how that paper (a) states
its main result and scope **up front** ([`../../skills/ectheory-contribution-framing/SKILL.md`](../../skills/ectheory-contribution-framing/SKILL.md)),
(b) positions itself by **which assumption it weakens or which limit result it generalizes**
([`../../skills/ectheory-literature-positioning/SKILL.md`](../../skills/ectheory-literature-positioning/SKILL.md)),
and (c) decides it is the *right kind* of result for ET rather than an applied estimate
([`../../skills/ectheory-topic-selection/SKILL.md`](../../skills/ectheory-topic-selection/SKILL.md)). For
each, ask the self-check before claiming your paper is "Econometric Theory–shaped."

Note the spread of *kinds* of contribution this short list spans — a foundational **regression-asymptotics
framework**, its **multivariate/cointegrated generalization**, an **estimator with an optimality theory**,
a reusable **probabilistic limit-theory tool**, and a **robust-inference distribution theory** — which is
exactly ET's range: it rewards the result that other people's proofs will later cite as a lemma.

---

## By kind of contribution

### Foundational regression asymptotics with I(1) regressors (the framework everyone builds on)

- **Park, Joon Y. & Phillips, Peter C.B., "Statistical Inference in Regressions with Integrated
  Processes: Part 1," *Econometric Theory* 1988, 4(3): 468–497.** DOI `10.1017/S0266466600013402`.
  Verified: `cambridge.org/core/journals/econometric-theory/article/abs/statistical-inference-in-regressions-with-integrated-processes-part-1/6D8123B8A28E61371D40832D48CCF6BC`.
  - **Why it is an exemplar:** builds the asymptotic machinery for regressions whose regressors are
    integrated processes — functionals of Brownian motion, not normals — and shows *why* the usual
    Gaussian inference fails and what replaces it. A general theorem that downstream cointegration and
    unit-root work treats as a foundation, not an application.
  - **Self-check:** is your result a **general limit theory** a later author would cite as a lemma, or a
    parameter estimate for one model? (`ectheory-topic-selection`)

### Generalizing the framework to multivariate / cointegrated systems

- **Park, Joon Y. & Phillips, Peter C.B., "Statistical Inference in Regressions with Integrated
  Processes: Part 2," *Econometric Theory* 1989, 5(1): 95–131.** DOI `10.1017/S0266466600012287`.
  Verified: `cambridge.org/core/journals/econometric-theory/article/abs/statistical-inference-in-regressions-with-integrated-processes-part-2/CF72E9310080303446B71EFA71D51668`.
  - **Why it is an exemplar:** extends Part 1 to multivariate linear models with integrated processes of
    *different orders*, nonzero means, drifts, time trends, and cointegrated regressors — the explicit
    "weaken the assumptions / widen the scope" move ET rewards. A two-part program that maps the whole
    territory rather than one corner of it.
  - **Self-check:** does your paper state **exactly which assumption of the prior result you relax** and
    prove the limit theory still holds? (`ectheory-literature-positioning`)

### An estimator with an explicit optimality theory

- **Saikkonen, Pentti, "Asymptotically Efficient Estimation of Cointegration Regressions," *Econometric
  Theory* 1991, 7(1): 1–21.** DOI `10.1017/S0266466600004217`.
  Verified: `cambridge.org/core/journals/econometric-theory/article/abs/asymptotically-efficient-estimation-of-cointegration-regressions/1BA61705C7FE70AA7FBA972F1681B111`.
  - **Why it is an exemplar:** proposes an OLS-with-time-domain-correction estimator for cointegration
    regressions **and proves it is asymptotically efficient** — defining what efficiency *means* in this
    nonstandard setting (a peakedness/concentration criterion) before showing the estimator attains it. A
    method paper whose contribution is the optimality theorem, not the recipe.
  - **Self-check:** if you propose an estimator/test, do you also **characterize the bound it attains**
    (efficiency, optimality, admissibility) rather than only assert it works? (`ectheory-contribution-framing`)

### A reusable probabilistic limit-theory tool

- **Hansen, Bruce E., "Convergence to Stochastic Integrals for Dependent Heterogeneous Processes,"
  *Econometric Theory* 1992, 8(4): 489–500.** DOI `10.1017/S0266466600013189`.
  Verified: Cambridge Core article `F4823C5BCE6A3E78E5EEFC0B09483422` (and RePEc `cup/etheor` v8 i4 p489–500).
  - **Why it is an exemplar:** gives general conditions for the weak convergence of *stochastic integrals*
    under strong-mixing dependence — a tool reused across I(1), I(2), near-integrated, and
    nonstationary-variance asymptotics. The purest ET contribution: a theorem stated so generally that its
    value is being a citable building block in other people's proofs.
  - **Self-check:** could a reader **lift your main lemma into a different model** unchanged? If the result
    only lives inside your own application, it may be a JoE/applied paper, not ET. (`ectheory-topic-selection`)

### Robust-inference distribution theory (long-run variance / HAC)

- **Kiefer, Nicholas M. & Vogelsang, Timothy J., "A New Asymptotic Theory for
  Heteroskedasticity-Autocorrelation Robust Tests," *Econometric Theory* 2005, 21(6): 1130–1164.**
  DOI `10.1017/S0266466605050565`.
  - **Why it is an exemplar:** models the HAC bandwidth as a *fixed fraction* of the sample size ("fixed-b"
    asymptotics) and derives a non-standard limiting distribution for the robust test that **explicitly
    captures the kernel and bandwidth choice** the conventional theory hides. A new asymptotic *framework*
    that changed how robust tests are sized — theory first, simulation in support.
  - **Self-check:** does your asymptotic device **expose a modeling choice the standard theory sweeps into
    a consistency hand-wave**, and do your Monte Carlos show the new approximation tracks finite samples?
    (`ectheory-data-analysis`)

---

## By problem (each cell is a verified *Econometric Theory* paper above)

| Problem | Verified *Econometric Theory* exemplar | Year / vol(issue) | Kind of contribution |
| --- | --- | --- | --- |
| Inference with integrated regressors | Park & Phillips, "…Integrated Processes: Part 1" | 1988, 4(3) | Foundational regression asymptotics |
| Multivariate / cointegrated systems | Park & Phillips, "…Integrated Processes: Part 2" | 1989, 5(1) | Generalization to wider scope |
| Efficient cointegration estimation | Saikkonen, "Asymptotically Efficient Estimation of Cointegration Regressions" | 1991, 7(1) | Estimator + optimality theory |
| Limit theory toolkit (weak convergence) | Hansen, "Convergence to Stochastic Integrals…" | 1992, 8(4) | Reusable probabilistic tool |
| HAC / long-run-variance robust testing | Kiefer & Vogelsang, "A New Asymptotic Theory for HAC Robust Tests" | 2005, 21(6) | Robust-inference distribution theory |

---

## Omitted for sibling-confusion or lack of verification (do not attribute to *Econometric Theory*)

To keep the list zero-hallucination, the following were **checked and excluded** — several are landmark
results routinely mis-cited to ET because they share its subject matter and authors:

- **Phillips, P.C.B., "Time Series Regression with a Unit Root" (1987)** — *Econometrica* 55(2):277–301,
  **not Econometric Theory**. The single most common ET mis-attribution (Phillips founded ET, so his
  unit-root work is assumed to live there). Guardrail entry.
- **Robinson, P.M., "Gaussian Semiparametric Estimation of Long Range Dependence" (1995)** and
  **"Log-Periodogram Regression of Time Series with Long Range Dependence" (1995)** — *Annals of
  Statistics* 23, **not Econometric Theory** (ET publishes much long-memory work, but these foundational
  estimators are in *Annals*). Guardrail entry.
- **Pesaran, M.H., "General Diagnostic Tests for Cross Section Dependence in Panels"** — circulated as
  CESifo/IZA working papers (2004) and published in *Empirical Economics* 60(1):13–50 (2021), **not
  Econometric Theory**. Guardrail entry.
- **Magnus, J.R. & Neudecker, H., *Matrix Differential Calculus with Applications in Statistics and
  Econometrics*** — a **Wiley book** (1988; rev. 1999, 2019); *Econometric Theory* carries only a 1989
  **book review** of it (5(1):161–165), not the work itself. Do not cite "the matrix-calculus paper in ET."

Before adding any new paper to this library, confirm it on
`cambridge.org/core/journals/econometric-theory` (an article page carrying the volume/issue) **or** its
`10.1017/S0266466…` DOI, and update the access-date header. If web verification is unavailable, add the
row as **待核实 / TO VERIFY** with **no attribution** until checked. **When in doubt, omit.**
