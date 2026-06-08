# AISTATS Exemplars Library (topic × method)

> **Verified via web search, access date 2026-06-08.** Every paper below was checked against the **PMLR
> proceedings** (`proceedings.mlr.press/...`) to confirm it actually appeared in the **International
> Conference on Artificial Intelligence and Statistics (AISTATS)** — matching the PMLR volume to the
> AISTATS edition, plus author list, year, and page range. Papers that could not be cleanly confirmed as
> **AISTATS** (as opposed to a sibling venue) were **omitted and documented below**. It is deliberately a
> short, verified list (6 verified > 15 guessed).
>
> **Sibling-confusion guard:** AISTATS is **not** NeurIPS, ICML, ICLR, UAI, or JMLR. Several famous ML
> papers live in those venues or in PMLR volumes that belong to *other* conferences. A PMLR volume number
> alone does **not** prove AISTATS — e.g. PMLR **v23 is COLT 2012**, not AISTATS (see omissions). Each row
> below was checked to be an AISTATS edition specifically.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent results, theorem constants, or table numbers — read the original on PMLR before
> citing anything. For AISTATS-specific policy, scope, and the do-not-misattribute list, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **topic × method** is closest to yours, then study how that paper puts a **statistical
contribution on the first page** with **explicit assumptions** and **claims paired to proof or
experiment** — the AISTATS bar (see
[`../../skills/aistats-writing-style/SKILL.md`](../../skills/aistats-writing-style/SKILL.md),
[`../../skills/aistats-topic-selection/SKILL.md`](../../skills/aistats-topic-selection/SKILL.md), and
[`../../skills/aistats-experiments/SKILL.md`](../../skills/aistats-experiments/SKILL.md)). For each, ask
the self-check question before claiming your paper is "AISTATS-shaped."

**AISTATS edition ↔ PMLR volume (verified rows below):** v33 = AISTATS 2014 (17th); v38 = AISTATS 2015
(18th); v51 = AISTATS 2016 (19th); v89 = AISTATS 2019 (22nd).

---

## By method

### Black-box / general-purpose variational inference (approximate Bayesian inference)

- **Ranganath, Gerrish & Blei, "Black Box Variational Inference," AISTATS 2014, PMLR v33:814–822.**
  Verified: `proceedings.mlr.press/v33/ranganath14.html` (Proceedings of the *Seventeenth* International
  Conference on Artificial Intelligence and Statistics).
  - **Why it is an exemplar:** turns variational inference from a per-model derivation into a **reusable
    stochastic-optimization recipe** (Monte-Carlo gradients of the ELBO), so the *statistical* idea — not
    a single model — is the contribution. A model of the AISTATS "method that travels" abstract.
  - **Self-check:** is your contribution a general inferential tool with a clearly stated estimator and
    variance-reduction story, rather than one tuned architecture?

### Scalable structured variational inference (approximate Bayesian inference)

- **Hoffman & Blei, "Structured Stochastic Variational Inference," AISTATS 2015, PMLR v38:361–369.**
  Verified: `proceedings.mlr.press/v38/hoffman15.html` (Proceedings of the *Eighteenth* International
  Conference on Artificial Intelligence and Statistics).
  - **Why it is an exemplar:** relaxes the mean-field independence assumption to recover **dependencies**
    in stochastic VI — the contribution is an explicit weakening of a *statistical assumption*, exactly
    the kind of move AISTATS rewards.
  - **Self-check:** does your method name the assumption it relaxes, and show the inferential payoff of
    relaxing it?

### Gaussian processes + deep architectures (kernel methods / representation)

- **Wilson, Hu, Salakhutdinov & Xing, "Deep Kernel Learning," AISTATS 2016, PMLR v51:370–378.**
  Verified: `proceedings.mlr.press/v51/wilson16.html` (Proceedings of the *Nineteenth* International
  Conference on Artificial Intelligence and Statistics).
  - **Why it is an exemplar:** fuses the **non-parametric flexibility of kernels** with deep feature
    learning while keeping GP-style uncertainty and near-linear scaling — a statistics-forward way to use
    deep nets, the AISTATS sweet spot between ML practice and probabilistic modeling.
  - **Self-check:** does your deep method retain a **statistical object** (a posterior, a calibrated
    uncertainty, a kernel) rather than only a point predictor?

### Bayesian nonparametric regression via MCMC (probabilistic modeling / inference)

- **Heinonen, Mannerström, Rousu, Kaski & Lähdesmäki, "Non-Stationary Gaussian Process Regression with
  Hamiltonian Monte Carlo," AISTATS 2016, PMLR v51:732–740.**
  Verified: `proceedings.mlr.press/v51/heinonen16.html` (Proceedings of the *Nineteenth* International
  Conference on Artificial Intelligence and Statistics).
  - **Why it is an exemplar:** infers **full posteriors over input-dependent length-scale, signal, and
    noise** via HMC instead of point estimates — uncertainty quantification *is* the contribution, which
    is the `aistats-topic-selection` signal that statistical reasoning is central, not decorative.
  - **Self-check:** does your method deliver a *posterior* over the nuisance structure others fix by
    point estimate, and is the sampler's assumption set stated?

### Fairness with combinatorial guarantees (algorithmic fairness / theory)

- **Chierichetti, Kumar, Lattanzi & Vassilvitskii, "Matroids, Matchings, and Fairness," AISTATS 2019,
  PMLR v89:2212–2220.**
  Verified: `proceedings.mlr.press/v89/chierichetti19a.html` (Proceedings of the *Twenty-Second*
  International Conference on Artificial Intelligence and Statistics).
  - **Why it is an exemplar:** states fairness as **constraints over matroids/matchings** and proves
    algorithmic guarantees — a theory-forward fairness contribution with provable structure, not a
    benchmark tweak. Pairs with `aistats-writing-style`'s "claim → proof structure" discipline.
  - **Self-check:** can your fairness notion be stated as a constraint with a *provable* feasibility or
    approximation guarantee, rather than an empirical fairness-accuracy curve only?

---

## By topic (each cell is a verified AISTATS paper above)

| Topic | Verified AISTATS exemplar | Edition / PMLR vol : pages | Method |
| --- | --- | --- | --- |
| Approximate Bayesian inference (general) | Ranganath, Gerrish & Blei, "Black Box Variational Inference" | 2014 / v33:814–822 | Stochastic variational inference |
| Scalable structured inference | Hoffman & Blei, "Structured Stochastic Variational Inference" | 2015 / v38:361–369 | Structured stochastic VI |
| Kernels × deep features | Wilson, Hu, Salakhutdinov & Xing, "Deep Kernel Learning" | 2016 / v51:370–378 | GP + deep kernel |
| Nonparametric UQ / sampling | Heinonen et al., "Non-Stationary GP Regression with HMC" | 2016 / v51:732–740 | Bayesian nonparametrics + HMC |
| Algorithmic fairness (theory) | Chierichetti, Kumar, Lattanzi & Vassilvitskii, "Matroids, Matchings, and Fairness" | 2019 / v89:2212–2220 | Combinatorial fairness with guarantees |

> Five verified papers across five topic × method cells. The Black-Box / Structured-VI pair also
> demonstrates **a research line** (general VI → structured VI) within AISTATS, useful when positioning an
> incremental-but-principled contribution.

---

## Omitted for lack of clean AISTATS verification (do not attribute to AISTATS without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking — several are exactly
the sibling-venue confusions the header warns about:

- **Jain, Kothari & Thakurta, "Differentially Private Online Learning" (PMLR v23:24.1–24.34, 2012)** —
  verified to be **COLT 2012** (the *25th Annual Conference on Learning Theory*), **not AISTATS**. A
  direct PMLR-volume trap: v23 is COLT, not an AISTATS edition. Listed here only as a guardrail.
- **Gretton, Borgwardt, Rasch, Schölkopf & Smola, "A Kernel Two-Sample Test"** — the canonical MMD
  paper is in **JMLR (2012)**, **not AISTATS**. Omitted.
- **van der Maaten & Hinton, "Visualizing Data using t-SNE"** — **JMLR (2008)**; no AISTATS placement of
  the t-SNE paper could be confirmed. Omitted.
- **Differential-privacy / fairness candidates in PMLR v97, v108, v162** — v97/v162 are **ICML**
  volumes and v108 is AISTATS 2020, but the specific papers surfaced (e.g. "Differentially Private Fair
  Learning," v97) sit in **ICML**, not AISTATS. Omitted to avoid venue misattribution.

Before adding any new paper, confirm it on `proceedings.mlr.press` by matching the **PMLR volume to the
AISTATS edition** (the volume landing page names "International Conference on Artificial Intelligence and
Statistics"), then record author list, year, and pages, and update the access-date header. When in doubt,
omit. If web search is unavailable, add the row as **待核实 / TO VERIFY** with **no attribution**.
