> **Illustrative teaching example.** The paper, estimator, theorems, and every number below are
> **fictional** and exist only to demonstrate *Journal of Business & Economic Statistics* house style. No
> real-paper facts are stated, and no real method is being claimed. Corresponding skills:
> [`jbes-writing-style`](../../skills/jbes-writing-style/SKILL.md),
> [`jbes-contribution-framing`](../../skills/jbes-contribution-framing/SKILL.md), and
> [`jbes-identification-strategy`](../../skills/jbes-identification-strategy/SKILL.md).

# Worked Example: A *Journal of Business & Economic Statistics*-Style Introduction (before → after)

This demonstrates the introduction arc JBES rewards (from `jbes-writing-style` and
`jbes-contribution-framing`): **the methodological problem and why it matters empirically → the
contribution as one claim that pairs novelty with empirical relevance → the target and its identification
→ assumptions and asymptotics → finite-sample (size/power/coverage) evidence → the substantive
application → short roadmap.** The governing rule from `jbes-contribution-framing` is that a JBES
contribution is a **method-level claim with an empirical consequence** — *we develop method M so
practitioners can now do D in setting S, which prior methods could not* — stated plainly in the abstract
and on page one. JBES sits between modern data science and classical econometrics, so the framing must
make both the **methodological delta** and the **empirical relevance** explicit, and the assumptions must
be weak enough that the paper's own application satisfies them.

**Illustrative paper (fictional):** *"A Robust Test for Equal Forecast Accuracy Under Heavy Tails and
Many Models."* Fictional setup: comparing the out-of-sample accuracy of a large set of forecasting models
when forecast-error losses are heavy-tailed, so standard equal-accuracy tests are oversized and
multiple-model comparison inflates false discoveries.

---

## Before (buries the contribution — typical first-draft intro)

> Forecast evaluation is an important topic in economics and statistics. Many tests have been proposed to
> compare forecasts. In this paper we propose a new test for comparing forecast accuracy and study its
> properties. We derive its asymptotic distribution under standard regularity conditions and conduct
> Monte Carlo simulations. We also apply the test to an empirical example. The results show that our test
> works well. Section 2 reviews the literature, Section 3 presents the test, Section 4 derives the
> theory, Section 5 reports simulations, Section 6 presents the application, and Section 7 concludes.

**What's wrong (against `jbes-writing-style` / `jbes-contribution-framing` / `jbes-identification-strategy`):**

- **No single contribution pairing novelty with relevance.** "A new test … works well" names neither the
  methodological delta (what is new versus existing equal-accuracy tests) nor the empirical consequence
  (what practitioners can now do) — the `jbes-contribution-framing` failure for a methods-with-empirics
  journal.
- **"Standard regularity conditions" with no list.** The assumptions are the contribution's load; hiding
  them hides whether the conditions are weak enough for the heavy-tailed data the paper claims to handle
  (`jbes-identification-strategy`: conditions explicit and plausible in the application).
- **No null distribution, size, or power claim** on page one — a referee cannot tell what is proved or
  whether the test controls size, the JBES credibility ladder.
- **Monte Carlo and application asserted, not characterized** ("works well") — no mention of the
  size/power metric or the multiple-model dimension that motivates the paper (`jbes-data-analysis`).
- **Throat-clearing** ("important topic") and an **over-signposted roadmap** doing the argument's work.

---

## After (*JBES* arc — method + empirical relevance + validity + finite-sample evidence, early)

> **When forecast-error losses are heavy-tailed and many models are compared at once, the standard
> equal-accuracy test is oversized and naïve pairwise comparison inflates false discoveries — so
> practitioners cannot reliably declare one forecast better than another.** We propose a **rank-based
> equal-predictive-accuracy test** that controls size under heavy tails by replacing the loss differential
> with its self-normalized rank statistic, and we pair it with a **stepwise multiple-testing procedure**
> that controls the familywise error rate across a large model set. *(The methodological problem + the
> contribution as one claim joining the method advance to what practitioners can now do — heavy-tailed-
> robust, many-model forecast comparison.)*
>
> The **target** is the vector of expected loss differentials between each candidate forecast and a
> benchmark; identification requires only that these expected differentials exist, so the test applies
> where second moments of the loss may not. *(Target + its identification condition, stated weakly enough
> for the heavy-tailed application — the `jbes-identification-strategy` "conditions plausible in the
> application" requirement.)*
>
> Under stationary, mixing forecast errors with possibly infinite loss variance (Assumptions A1–A3, all
> primitive), the self-normalized rank statistic has a **nuisance-parameter-free limiting null
> distribution** that we characterize, and the stepwise procedure achieves asymptotic familywise size
> control; we provide a consistent estimator of the relevant long-run quantities. *(Labeled assumptions +
> limiting null distribution + size-control guarantee + a consistent variance object — the JBES
> credibility ladder, no "standard regularity conditions.")*
>
> In Monte Carlo with Student-t(2) losses and up to 100 competing models, our test holds empirical size
> near the nominal 5% (versus 0.17 for the standard test) and loses little power against local
> alternatives, while the stepwise procedure keeps the familywise error near 5% where pairwise testing
> reaches 0.40. *(Finite-sample evidence on the dimensions that matter — size under heavy tails, power,
> and multiplicity — reported with the comparison, per `jbes-data-analysis`; breakdown of the incumbent
> shown, not hidden.)*
>
> Applied to a panel of macroeconomic forecasts, the test identifies a small set of models that
> significantly beat the benchmark after multiplicity control, where the standard approach spuriously
> flags many. *(The substantive application that exercises the novelty — empirical relevance delivered,
> not decorative.)*
>
> Our contribution is therefore a **method with a concrete empirical payoff**: a forecast-accuracy test
> and multiple-comparison procedure that remain valid when losses are heavy-tailed and the model set is
> large, a regime where existing tests are provably miscalibrated. *(Contribution restated as novelty ×
> relevance, right-sized to what is proved and simulated — `jbes-contribution-framing`.)*
>
> Section 2 sets up the test and assumptions; Section 3 gives the limiting theory and the stepwise
> procedure; Section 4 reports the Monte Carlo; Section 5 presents the application. *(Brief roadmap — no
> over-signposting.)*

---

## Why the "after" meets the *Journal of Business & Economic Statistics* bar

Mapped to the skill checklists:

- **One contribution pairing novelty with empirical relevance** — "heavy-tailed-robust, many-model
  forecast comparison" names both the methodological delta and what practitioners can now do, the
  `jbes-contribution-framing` "method advance + empirical consequence" shape, stated on page one.
- **Assumptions are primitive, labeled, and plausible in the application** — A1–A3 allow infinite loss
  variance, exactly the regime the empirical forecasts exhibit, satisfying the
  `jbes-identification-strategy` rule that conditions be explicit and not so strong the paper's own data
  fail them.
- **The full validity ladder appears early** — target and identification, limiting null distribution,
  size control, and a consistent variance object, the `jbes-identification-strategy` credibility ladder
  for a new test (null, limiting distribution, size + power).
- **Finite-sample evidence is characterized, not asserted** — size under Student-t(2), power against local
  alternatives, and familywise error across 100 models, with the incumbent's breakdown shown, the
  `jbes-data-analysis` size/power/coverage discipline.
- **Empirical relevance is delivered, not decorative** — the macro-forecast application uses the novelty
  (multiplicity-controlled, heavy-tail-robust selection), meeting the JBES "clear empirical relevance"
  scope (`jbes-topic-selection`).
- **The claim is right-sized and the method stays legible** — generality is scoped to what is proved
  (stationary mixing, existing first moments), notation is defined on first use, and the roadmap is one
  sentence, avoiding the `jbes-writing-style` over-claiming and over-signposting anti-patterns.

> Next: adapt the reproducible analysis skeleton in [`../code/`](../code/) when turning this introduction
> arc into a full Monte-Carlo-plus-application workflow.
