> **Illustrative teaching example.** The estimator, theorem, assumptions, and every number below are
> **fictional** and exist only to demonstrate *Econometric Theory* (ET) house style. No real result is
> stated and no policy is invented. Corresponding skills:
> [`ectheory-writing-style`](../../skills/ectheory-writing-style/SKILL.md),
> [`ectheory-contribution-framing`](../../skills/ectheory-contribution-framing/SKILL.md),
> [`ectheory-identification-strategy`](../../skills/ectheory-identification-strategy/SKILL.md), and
> [`ectheory-data-analysis`](../../skills/ectheory-data-analysis/SKILL.md).

# Worked Example: An Econometric Theory Introduction (before → after)

This demonstrates the **ET introduction arc** for a theorem-proof paper, built only from this pack's own
skills. ET is theorem-proof first: it rewards **a clearly stated, general result whose importance is
obvious from the statement** (`ectheory-contribution-framing`), with the **theorem and its scope on the
first page or two**, the **assumptions stated explicitly and minimally** (`ectheory-identification-strategy`),
and **Monte Carlo as supporting evidence that the asymptotics are useful, not the contribution itself**
(`ectheory-data-analysis`).

ET arc: **the inference problem → the theorem in words + its scope (assumptions, environment, limiting
law) → the generality delta vs known special cases → consequences (what becomes provable / computable /
robust) → Monte Carlo as support → brief roadmap.** Unlike an applied-economics intro, there is **no
policy question and no headline causal magnitude**; the lead is a *theorem*.

**Illustrative paper (fictional):** *"A Robust HAR Test for a Structural Break of Unknown Timing under
Near-Unit-Root Dependence."* Fictional contribution: a new test statistic for a parameter break in a
moderately persistent regressor, with a non-standard limiting distribution derived under weak
regularity conditions, plus a consistent estimator of its critical values.

---

## Before (buries the result — typical first-draft intro)

> The literature on structural breaks is large and has been studied extensively. Many tests have been
> proposed for detecting parameter instability in time-series regressions, and the unit-root and
> near-unit-root literature is also vast. In this paper we propose a new test. We first set up the model
> and notation in Section 2, then state assumptions in Section 3, then in Section 4 we derive the
> asymptotic distribution of our statistic using a functional central limit theorem and the continuous
> mapping theorem, and we also use a HAC estimator to deal with autocorrelation. Section 5 reports an
> extensive Monte Carlo study showing our test works well across many designs. Section 6 has an empirical
> application to interest-rate data. Section 7 concludes. All proofs are in the Appendix.

**What's wrong (against this pack's skills):**

- **Hides the main result** behind setup and notation — the `ectheory-contribution-framing` anti-pattern
  "Hiding the main result on page 8 behind setup and notation."
- **States the proof program instead of what is proved** ("we derive… using an FCLT and the CMT") —
  recounts proof steps before stating the theorem.
- **No theorem in words and no scope on page one:** environment (stationary vs near-unit-root), mode of
  convergence, rate, and **limiting law are never named** (`ectheory-identification-strategy` requires
  "mode of convergence, rate, and limiting law stated precisely").
- **Assumptions invisible** — the reader cannot tell which regularity conditions are doing the work, the
  single most common ET referee objection.
- **Monte Carlo oversold** ("works well across many designs") rather than framed as evidence the
  asymptotics bite, with a candid breakdown region (`ectheory-data-analysis`).
- **Over-signposted roadmap** doing the argument's job; an empirical "application" given equal billing
  with the theorem.

---

## After (ET arc — problem → theorem + scope → generality → consequences → support → roadmap)

> **Tests for a parameter break of unknown timing lose size control when the regressor is highly
> persistent: the usual sup-Wald limit is derived under stationarity, but breaks down as the largest
> autoregressive root approaches one.** We provide a heteroskedasticity- and autocorrelation-robust (HAR)
> break test whose asymptotic null distribution is valid *uniformly* across the stationary-to-near-unit-root
> range, together with a consistent estimator of its critical values. *(the inference problem, stated for
> a theorist who recognizes it instantly — no policy.)*
>
> Our main result (Theorem 1) is the following. Under a triangular-array near-unit-root design with the
> largest root local-to-unity (Assumption 1), conditionally heteroskedastic and weakly dependent errors
> with finite fourth moments (Assumption 2), and a single break in a subvector of the slope at an unknown
> fraction of the sample (Assumption 3), the studentized sup statistic **converges in distribution to the
> supremum of a normalized squared Ornstein–Uhlenbeck bridge**, a functional of a diffusion indexed by
> the local-to-unity parameter $c$. The convergence is at the standard $\sqrt{T}$ rate for the break-size
> coordinate, and the limit is **non-standard** — not chi-squared — with critical values depending on $c$
> only through a scalar nuisance that we estimate consistently (Theorem 2). *(the theorem in words, then
> its scope: assumptions, environment, rate, and limiting law — on page one.)*
>
> The result is general in two senses. As $c \to -\infty$ (the stationary limit) the limiting law
> **collapses to the classical sup-Wald distribution of the stationary break-test literature**, so
> existing critical values are recovered as a special case; and the finite-fourth-moment condition in
> Assumption 2 is weaker than the Gaussianity or strong-mixing-with-bounded-support conditions usually
> imposed, so the test covers conditionally heteroskedastic designs that earlier theory excludes.
> *(the generality delta — what known case it nests, and what is genuinely new.)*
>
> Two consequences follow. First, a practitioner can run **one** break test without pre-testing for a
> unit root and without choosing between two incompatible critical-value tables, because size is
> controlled uniformly in $c$. Second, because the nuisance parameter is estimated rather than assumed
> known, the procedure is **feasible** and its critical values are computable from the data. *(what
> becomes provable, robust, and computable because of the result.)*
>
> A Monte Carlo study supports the theory rather than carrying it: across a grid of sample sizes and
> values of $c$ spanning the stationary, moderately persistent, and near-unit-root regions, empirical
> size tracks the nominal level where the asymptotics predict it should, and we report **honestly** the
> near-boundary region ($c$ close to zero at small $T$) where the approximation is least accurate.
> *(Monte Carlo as evidence the asymptotics are useful — proportionate, with a candid breakdown region.)*
>
> The paper proceeds as follows. Section 2 states the model and assumptions; Section 3 proves Theorem 1
> and the feasible critical-value result; Section 4 reports the Monte Carlo evidence. *(brief roadmap —
> no over-signposting; proofs anchor the body, not an afterthought.)*

---

## Why the "after" meets the ET bar

Mapped to this pack's skill checklists:

- **Theorem stated in words plus its scope on page one** — object (studentized sup statistic), mode of
  convergence (in distribution), rate ($\sqrt{T}$), and limiting law (supremum of a normalized squared
  Ornstein–Uhlenbeck bridge) all appear immediately (`ectheory-contribution-framing`:
  "Main theorem stated in words plus its scope, in the first page or two";
  `ectheory-identification-strategy`: "Mode of convergence, rate, and limiting law stated precisely").
- **Assumptions explicit, minimal, and numbered** — Assumptions 1–3 are named where they bind, not
  buried, pre-empting the most common ET referee objection (`ectheory-identification-strategy`).
- **Generality delta made explicit** — the stationary case is recovered as $c \to -\infty$, and the
  moment condition is weaker than the usual one; this is the "what special cases collapse to known
  results, and what is genuinely new" frame (`ectheory-contribution-framing`).
- **Consequences stated, not just the formal result** — no pre-testing, one critical-value table,
  feasible estimation — "what becomes provable/robust/computable."
- **Monte Carlo demoted to support** with a candid breakdown region, never oversold
  (`ectheory-data-analysis`: "Show where the asymptotic approximation is poor").
- **Proof program is not recited in the intro** — the arc states *what* is proved (the limit law), not
  *how* (FCLT + CMT), avoiding the anti-pattern "An introduction that recounts the proof steps before
  stating what is proved."
- **No overclaim** beyond what Assumptions 1–3 deliver, and the non-standard limit is named as
  non-standard rather than forced into a familiar chi-squared shape.

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified** *Econometric
> Theory* papers whose introductions execute this theorem-first arc (near-unit-root limit theory,
> HAR/fixed-b inference, kernel and semiparametric rates), and
> [`../external_tools.md`](../external_tools.md) for the theorem-proof typesetting and Monte Carlo toolkit
> referenced above.
