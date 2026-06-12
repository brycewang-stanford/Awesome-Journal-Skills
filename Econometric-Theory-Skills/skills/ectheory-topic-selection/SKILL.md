---
name: ectheory-topic-selection
description: Use when deciding whether a result is the right kind of contribution for Econometric Theory (ET) — a general, foundational econometric-theory result (asymptotics, proofs, theorems) rather than an applied estimate, and whether it fits a full Article or a short Miscellanea.
---

# Topic Selection (ectheory-topic-selection)

## When to trigger

- You have a new estimator, limit result, or proof and are choosing a target journal
- Unsure whether the result is "ET-foundational" or really an applied/empirical paper
- Deciding between a full **Article** and a short **Miscellanea**
- Wondering whether the result fits one of ET's themed special-issue directions

## The ET fit bar

ET rewards **rigorous, general contributions to the mathematical and statistical foundations of
econometrics** — asymptotic theory, probability-theoretic methods, time-series and nonstationarity
theory, high-dimensional and non-standard environments. The question to answer first: *does this
result teach econometricians something about a method, a limit, or an inferential problem in
generality*, rather than reporting one applied estimate? An empirical application is welcome only as
illustration; the spine must be theory.

Signals of a good ET topic:

- A **new limit theory** (consistency, asymptotic normality, rate, FCLT) under explicitly stated,
  defensible regularity conditions
- A method whose **inferential properties** (size, power, robustness, partial identification) are
  characterized, not just asserted
- A result that **generalizes** a known special case (weaker assumptions, broader DGP, larger
  dimension, dependent data)
- Fit with current ET directions: econometric theory for ML/AI, causal inference under complex
  interference, robust inference and partial identification, high-dimensional and non-standard
  environments, network/spatial econometrics

## Article vs Miscellanea

- **Article** — multiple major contributions, a new method with extensive proofs, and usually
  simulations or an application. Regular Articles must not exceed **50 pages** (overflow → online
  Supplement).
- **Miscellanea** — a dedicated venue for **one or two key innovations** stated and proved
  concisely; typically **fewer than 20 pages, often ~15**. A clean single theorem that sharpens or
  corrects existing theory is a natural Miscellanea.
- The **ET Interview** is an invited oral-history genre, **not** author-submitted — do not target it.

## Checklist

- [ ] The contribution is a general theory result, not a single applied estimate
- [ ] Regularity conditions are statable and defensible (see ectheory-identification-strategy)
- [ ] The generality over prior work is one sentence you can say out loud
- [ ] Article vs Miscellanea chosen, with a length budget against the 50-page ceiling
- [ ] Fit with ET scope / a themed direction articulated

## Anti-patterns

- An applied paper with a thin "theory" wrapper (belongs at an applied outlet)
- A narrow corollary of a known theorem dressed as a full Article (consider Miscellanea or rework)
- Targeting the invited ET Interview genre as if it were submittable

## Fit-vs-venue routing table

When a result could go to several outlets, route it by what each venue rewards. Econometric Theory owns the
*pure limit theory* — the theorem and its proof are the contribution, with simulation as illustration.

| Result shape | Best home | Why |
| --- | --- | --- |
| New limit theory / proof, generality is the point | Econometric Theory | rigorous asymptotics is ET's identity |
| Method with heavy empirical payoff, lighter theory | applied-method outlet | the estimate carries the paper |
| One sharp theorem correcting/sharpening existing theory | ET Miscellanea | a concise 1–2 innovation venue |
| Theory plus a major economic-substance contribution | a general-interest journal | economics is co-equal there |

A quick desk-reject self-test: if you cannot say in one sentence which assumption you weaken or which
limiting law was previously unproven, the result is likely a corollary, not an ET Article.


## Fit pass for Econometric Theory

Treat this skill as an executable review pass, not a prose hint. First lock the primitive assumptions, theorem statement, proof route, and example showing why the result matters; then judge whether the current manuscript answers the venue's real reader: econometric theorists who read for assumptions, theorem novelty, proof architecture, and relation to known asymptotics.

- **Do the pass:** Score the manuscript on venue fit, novelty, evidence readiness, and audience ownership; reject a prestige-only target when a sibling venue owns the contribution more directly.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against Journal of Econometrics for applied-method reach, Quantitative Economics for theoretical economics, Econometrica for general theory-plus-economics contribution; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Result】one-line statement of the theorem/limit
【ET fit】foundational theory? [Y/N] + why
【Type】Article / Miscellanea + page budget
【Themed fit】direction (if any)
【Next step】ectheory-literature-positioning
```
