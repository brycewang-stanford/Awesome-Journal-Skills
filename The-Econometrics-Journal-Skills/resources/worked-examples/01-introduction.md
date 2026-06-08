> **Illustrative teaching example.** The paper, the estimator, the simulation, and every number
> below are **fictional** and exist only to demonstrate The Econometrics Journal house style. No
> real-paper facts are stated and no policy is invented. Corresponding skills:
> [`ectj-contribution-framing`](../../skills/ectj-contribution-framing/SKILL.md),
> [`ectj-writing-style`](../../skills/ectj-writing-style/SKILL.md),
> [`ectj-topic-selection`](../../skills/ectj-topic-selection/SKILL.md),
> [`ectj-identification-strategy`](../../skills/ectj-identification-strategy/SKILL.md), and
> [`ectj-data-analysis`](../../skills/ectj-data-analysis/SKILL.md).

# Worked Example: An EctJ-Style Introduction (before → after)

This demonstrates the **EctJ introduction arc** for a *methodological* paper — the kind The
Econometrics Journal publishes: a **new estimator / test / identification result, with theory plus a
simulation and an empirical illustration**. It is built only from this pack's own skills:

- **`ectj-contribution-framing`**: lead with the econometric problem and why existing methods fail in
  an applied setting; state the leading-case advance (new identification logic, estimator, test,
  approximation, inference method, or computation); say what applied researchers can now do; keep
  claims proportional; make the empirical application reveal practical value, not just illustrate.
- **`ectj-topic-selection`**: a path-breaking or leading-case method/estimator/test/identification
  result that **travels beyond one narrow dataset**, with an empirical application required even for
  theory — Monte Carlo is not a substitute for applied relevance.
- **`ectj-identification-strategy`**: state the population object, identifying restrictions, estimator
  or test statistic, and target parameter *before* derivations; show the leading case is not a toy.
- **`ectj-writing-style`**: compact; assumptions near the theorem; short interpretation over algebra
  restatement; simulations summarised within ~one page; conformance is part of the science.

**Illustrative paper (fictional):** *"A Bias-Corrected Test for a Weak Common Factor in Short
Dynamic Panels."* Fictional advance: a new test statistic plus its limiting distribution, validated
by Monte Carlo and illustrated on a (fictional) firm-level investment panel.

---

## Before (buries the contribution — typical first-draft intro)

> Cross-section dependence in panel data has received considerable attention in the literature. Many
> tests and estimators have been proposed. In this paper we propose a new test statistic. We derive
> its asymptotic distribution under a set of regularity conditions and conduct a Monte Carlo study to
> examine its size and power. We also apply the test to a panel of firms. The remainder of the paper
> is organized as follows. Section 2 reviews the literature, Section 3 sets up the model, Section 4
> derives the asymptotics, Section 5 reports simulations, Section 6 presents the empirical
> application, and Section 7 concludes.

**What's wrong (against the EctJ skills):**

- **No econometric problem stated.** `ectj-contribution-framing` requires leading with *why existing
  methods fail in an applied setting*; "has received considerable attention" is throat-clearing.
- **The leading-case advance is hidden.** "We propose a new test statistic" names no advance — what
  breaks before this paper, and what can an applied researcher now do? (framing skill).
- **Target object not stated up front.** `ectj-identification-strategy` wants the population object,
  identifying restriction, statistic, and target *before* derivations.
- **Monte Carlo is treated as the payoff**, and the empirical application is a throwaway — violating
  `ectj-topic-selection` ("do not treat Monte Carlo as a substitute for applied relevance") and
  `ectj-data-analysis` ("show where the new procedure changes an applied conclusion").
- **Over-signposted roadmap** doing the work the argument should do (`ectj-writing-style`: compact).
- **No applied-value sentence**, so a reader cannot tell this is leading-case rather than exhaustive.

---

## After (EctJ arc — problem → why methods fail → the advance → theory object → evidence → applied value)

> **When a dynamic panel is short in time and the cross-section is weakly correlated through a single
> factor, the standard LM-type tests for cross-section dependence over-reject sharply, so applied
> researchers cannot tell a genuinely weak factor from none at all.** *(the econometric problem,
> stated in an applied setting — `ectj-contribution-framing`.)*
>
> Existing tests are built for either strong common factors or independence; under a *weak* factor in
> short panels their finite-sample bias is first-order, and bias corrections derived for large-T
> designs do not apply. *(why existing methods fail — the gap, not a literature tour.)*
>
> We propose a **bias-corrected statistic, $\widehat{T}_{wf}$, that is asymptotically standard normal
> under the null of no weak factor** as the cross-section grows with the time dimension fixed, and we
> derive its local power against weak-factor alternatives. The target object is the **factor-strength
> index $\alpha \in [0,1]$**; the null is $\alpha < \tfrac{1}{2}$ (no estimable factor) against the
> leading alternative of a weak factor. *(target object + identifying restriction + statistic + target,
> stated before any derivation — `ectj-identification-strategy`.)*
>
> The correction is a single closed-form term, so the test is **as cheap to compute as the
> uncorrected LM statistic** and needs no resampling. *(what applied researchers can now do —
> applied value, kept proportional.)*
>
> In a Monte Carlo study spanning $N \in \{50,100,200\}$ with $T=5$, the test holds size near the
> nominal 5% (empirical size 5.3–6.1%) where the uncorrected statistic rejects 18–27% of the time
> under the null, while retaining power above 0.80 against a weak factor with $\alpha=0.55$. *(one
> compact simulation paragraph — `ectj-data-analysis`, `ectj-writing-style`'s ~one-page rule.)*
>
> Applied to a (fictional) panel of 180 firms over five years, the uncorrected test flags
> cross-section dependence and would send the analyst to a costly factor-augmented estimator;
> **$\widehat{T}_{wf}$ does not reject, and a pooled estimator the analyst would otherwise abandon
> remains valid** — the procedure changes the modelling decision, not just a p-value. *(the
> application reveals practical value — `ectj-contribution-framing`, `ectj-data-analysis`.)*
>
> Section 2 sets up the model and states the test; Section 3 gives the limiting theory and local
> power; Section 4 reports the simulation and the firm-panel application. *(compact roadmap — no
> over-signposting.)*

---

## Why the "after" meets the EctJ bar

Mapped to the skill checklists:

- **Leads with the econometric problem in an applied setting**, then states *why existing methods
  fail* — the `ectj-contribution-framing` order, not a literature review.
- **Leading-case advance is explicit and proportional**: a new test + limiting distribution + local
  power, framed as "a weak factor in short panels," not marketed as a complete framework
  (`ectj-contribution-framing` scope guardrail; `ectj-topic-selection` leading-case test).
- **Target object stated before derivations** — factor-strength index $\alpha$, null, statistic,
  target — satisfying `ectj-identification-strategy`'s "state the population object … before
  derivations."
- **Simulation is compact and theory-aligned**, summarised in a single paragraph per
  `ectj-writing-style` (~one page) and `ectj-data-analysis` ("keep Monte Carlo evidence focused;
  compare against a credible alternative; report $N$, $T$, design").
- **The empirical application carries applied value** — it *changes the estimator the analyst would
  choose* — meeting `ectj-topic-selection`'s "empirical application required even for theory" and
  `ectj-data-analysis`'s "show where the procedure changes an applied conclusion."
- **Applied-value sentence is present and fillable:** "Applied researchers can now [tell a weak factor
  from none in short panels] at [the cost of the uncorrected LM test]" — both brackets filled, as
  `ectj-contribution-framing` requires.

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified** Econometrics
> Journal papers (tests, panel estimators, weak-instrument inference) whose introductions execute this
> theory-plus-application arc, and [`../official-source-map.md`](../official-source-map.md) for the
> ≤150-word summary, ≤20-page, and "simulations within ~one page" rules this example is written to.
