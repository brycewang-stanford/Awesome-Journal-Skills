> **Illustrative teaching example.** The paper, estimator, theorems, and every number below are
> **fictional** and exist only to demonstrate *Journal of Econometrics* house style. No real-paper facts
> are stated, and no real method is being claimed. Corresponding skills:
> [`joe-writing-style`](../../skills/joe-writing-style/SKILL.md),
> [`joe-contribution-framing`](../../skills/joe-contribution-framing/SKILL.md), and
> [`joe-identification-strategy`](../../skills/joe-identification-strategy/SKILL.md).

# Worked Example: A *Journal of Econometrics*-Style Introduction (before → after)

This demonstrates the introduction arc the *Journal of Econometrics* rewards (from `joe-writing-style`
and `joe-contribution-framing`): **econometric problem → why existing methods fail → the contribution
stated as a property → estimand and identification → assumptions and asymptotics → finite-sample
(Monte Carlo) evidence → short roadmap.** The governing rule from `joe-writing-style` is to **state the
methodological contribution as a property, in plain words before any notation**, and to write the
introduction *last*, after the theorems and Monte Carlo are settled. The deliverable at this venue is a
**formal core** — what is assumed, what is proved, how general it is — plus the simulation that shows the
asymptotics bite in finite samples. Notation is defined on first use so a referee can audit the claim.

**Illustrative paper (fictional):** *"Bias-Corrected GMM for Dynamic Panels with Many Weak Moment
Conditions."* Fictional setup: a linear dynamic panel model where the usual lagged-instrument moment set
grows with the time dimension, so standard two-step GMM is biased and its variance estimator is
unreliable.

---

## Before (buries the contribution — typical first-draft intro)

> Dynamic panel models have been studied extensively in econometrics and applied widely in growth,
> labor, and finance. Many estimators have been proposed, including OLS, fixed effects, and GMM. In this
> paper we propose a new estimator for dynamic panels and study its performance. We derive its asymptotic
> properties under standard regularity conditions and conduct Monte Carlo simulations. The results show
> that our estimator performs well. Our method is useful for empirical researchers. Section 2 reviews the
> literature, Section 3 presents the model, Section 4 derives the theory, Section 5 reports simulations,
> and Section 6 concludes.

**What's wrong (against `joe-writing-style` / `joe-contribution-framing` / `joe-identification-strategy`):**

- **No stated contribution as a property.** "We propose a new estimator … performs well" never says
  *which* deficiency of the incumbent is fixed or *what* is now provable — the named anti-pattern in
  `joe-contribution-framing` (a contribution is a property, not an activity).
- **"Under standard regularity conditions" with no list.** This is the exact phrase
  `joe-identification-strategy` flags: the assumptions are the contribution's load, and hiding them
  hides whether the result is general or a convenient special case.
- **No estimand, no identification claim, no rate or limiting distribution** on page one — a referee
  cannot tell what is being estimated or what is proved (`joe-writing-style`: state the property before
  notation, preview the main theorem).
- **Monte Carlo asserted, not characterized** ("performs well") — no mention of the design dimension that
  matters (here, many/weak moments) or the metric (bias, size), violating `joe-data-analysis` discipline.
- **Throat-clearing** ("studied extensively," "useful for empirical researchers") and an
  **over-signposted roadmap** doing the work the argument should do.

---

## After (*JoE* arc — problem + property + identification + asymptotics + finite-sample evidence, early)

> **When the number of moment conditions in a dynamic panel grows with the time dimension, two-step GMM
> is biased of order \(O(\ell/N)\) in the number of instruments \(\ell\), and its conventional variance
> estimator understates the true sampling variation — so reported confidence intervals undercover.** We
> propose a **bias-corrected GMM estimator** whose first-order bias is removed analytically and whose
> variance estimator remains consistent under **many-weak-moment** asymptotics, where \(\ell\to\infty\)
> with \(N\) and instrument strength is allowed to drift to zero. *(Econometric problem + the property
> the new estimator has, stated before any further notation; "many weak moments" defined in place.)*
>
> Existing fixes either assume a fixed number of strong instruments — which the growing-\(\ell\) design
> violates — or trim instruments in a way that discards information and leaves the limiting distribution
> non-standard. *(Why existing methods fail, stated precisely against the design, per
> `joe-literature-positioning`.)*
>
> The **estimand** is the autoregressive and slope vector \(\theta_0\) of the dynamic panel; we prove
> **identification** of \(\theta_0\) from the level and forward-orthogonal-deviation moment conditions
> under a rank condition (Assumption A2) that we verify for the leading AR(1) case, and we make the
> instrument-strength sequence (Assumption A3) and the moment-growth rate \(\ell/N\to c\in[0,\infty)\)
> (Assumption A4) **primitive and explicit** rather than high-level. *(Estimand + identification +
> labeled, primitive assumptions — the `joe-identification-strategy` formal core, no "standard regularity
> conditions" hand-wave.)*
>
> Under A1–A4 the bias-corrected estimator is \(\sqrt{N}\)-consistent and asymptotically normal, with a
> sandwich variance estimator we prove consistent under the same many-weak-moment sequence; the
> correction removes the leading \(O(\ell/N)\) bias term we characterize in Theorem 2. *(Convergence
> rate + limiting distribution + a consistent variance estimator — stated, then proved in the body.)*
>
> In a Monte Carlo calibrated to the AR(1) panel with \(\ell\) scaling as \(\sqrt{N}\), the
> bias-corrected estimator cuts median bias from 0.21 to 0.02 and brings the empirical size of a nominal
> 5% test from 0.19 to 0.06, while uncorrected two-step GMM remains oversized across all designs.
> *(Finite-sample evidence reported on the dimension that matters — bias and size under growing \(\ell\)
> — as `joe-data-analysis` requires, not "performs well.")*
>
> Our contribution is therefore a property, not an activity: **an estimator that is asymptotically
> unbiased and correctly sized when the moment count grows with the sample**, a regime in which the
> incumbent two-step GMM is provably miscalibrated. The correction is **portable** to any over-identified
> GMM problem with a drifting moment count — not only dynamic panels. *(Contribution as a property,
> relative to a specific incumbent, with the generality class stated — `joe-contribution-framing`.)*
>
> Section 2 states the model and assumptions; Section 3 proves identification and the limiting theory;
> Section 4 reports the Monte Carlo; Section 5 illustrates on a panel application. *(Brief roadmap — no
> over-signposting.)*

---

## Why the "after" meets the *Journal of Econometrics* bar

Mapped to the skill checklists:

- **Contribution stated as a property, before notation** — "asymptotically unbiased and correctly sized
  when the moment count grows with the sample" is a property of the estimator, not a description of
  activity (`joe-contribution-framing`; `joe-writing-style`: state the advance as a property in plain
  words before any notation).
- **Assumptions are primitive and labeled, not "standard regularity conditions"** — A1–A4 are named, the
  rank condition is verified for a leading case, and the moment-growth rate is explicit, satisfying the
  `joe-identification-strategy` requirement that conditions be primitive and verifiable.
- **The full formal core appears on page one** — estimand, identification claim, convergence rate,
  limiting distribution, and a consistent variance estimator, exactly the chain
  `joe-identification-strategy` enumerates (identification → rate → distribution → variance estimator).
- **Finite-sample evidence is characterized, not asserted** — bias and size are reported under the design
  dimension that drives the result (\(\ell\) growing with \(N\)), the `joe-data-analysis` size/power
  discipline, rather than "performs well."
- **The incumbent is named and the gap is precise** — two-step GMM is identified as the thing that is
  biased \(O(\ell/N)\) and oversized, so the reader sees what improves and under which regime
  (`joe-literature-positioning`).
- **Generality is stated** — the portability note ("any over-identified GMM problem with a drifting
  moment count") gives the class the result covers, the `joe-identification-strategy` generality check,
  without over-claiming.
- **Method is the contribution, but the prose stays legible** — notation is defined on first use and the
  roadmap is one sentence, avoiding the `joe-writing-style` anti-patterns (undefined notation; an
  over-signposted roadmap doing the argument's work).

> Next: adapt the reproducible analysis skeleton in [`../code/`](../code/) when turning this
> introduction arc into a full Monte-Carlo-plus-application workflow.
