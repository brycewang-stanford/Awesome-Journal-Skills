---
name: restat-topic-selection
description: Use when deciding whether an applied-economics project fits The Review of Economics and Statistics (REStat) rather than AER / AEJ:Applied / J. Econometrics / a field journal, and sharpening the question to REStat's empirical-and-measurement bar. Decides venue fit and frames the question; it does not run the analysis.
---

# Topic Selection & Venue Fit (restat-topic-selection)

## When to trigger

- A project is between venues: REStat vs AER / AEJ:Applied vs *J. Econometrics* vs a field journal
- The question is interesting but you cannot say why it belongs at REStat specifically
- The contribution is a method but you are unsure REStat (applied, not methods-development) is the home
- You have a clean dataset / measurement advance and need to frame it as a REStat question

## The REStat fit bar

REStat publishes **applied economics and applied econometrics** with a long **measurement tradition**: it wants a substantive economic question answered with **credible identification** *or* a **careful measurement / data contribution** that moves an applied literature. It is **empirical-first** and broad across fields (labor, public, development, trade, IO, health, environment, urban, macro-empirics), wider than a field journal but more specialized than AER. Two REStat sweet spots that distinguish it from siblings: (1) a **clean causal estimate** of a parameter an applied literature cares about; (2) a **measurement or methods-applied** advance — a new index, a better-measured construct, a corrected bias, an estimator put to serious applied use — where the *application*, not the theorem, is the point.

## Fit decision table

| Your project | Better home | Why |
|--------------|-------------|-----|
| Credible causal estimate of broad applied interest, careful measurement | **REStat** | The target |
| Agenda-setting, general-interest, longer, field-defining | AER | REStat takes more specialized applied work, often shorter |
| Identification-driven applied micro of broad interest | AEJ: Applied (close sibling) | Overlaps heavily; REStat leans more on measurement + applied econometrics |
| A new estimator with proofs; method *is* the contribution | *J. Econometrics* / *Econometrica* | REStat is applied — methods must be *applied*, not developed for their own sake |
| Sub-field-internal contribution (JOLE / JPubE / JDE) | Field journal | REStat wants wider applied readership |
| A short, sharp empirical result | **REStat Short Paper** (≤6000 words, ≤5 exhibits; source map refreshed 2026-06-20) | REStat has a short-format track for compact contributions |

## The one-sentence test

Write the contribution in one sentence of the form: *"We measure/identify [parameter/object] in [setting] using [design/data], and find [estimate], which matters for [applied question]."* If the sentence is really *"we develop a new estimator and prove its properties,"* you are at the wrong journal. If it is *"we provide a better-measured [X] and show it changes [applied conclusion],"* you are squarely in REStat's measurement tradition.

## Checklist

- [ ] The economic question is applied, substantive, and stated in one sentence
- [ ] The contribution is identification *or* measurement — not a free-standing method
- [ ] You can name the closest 3–5 papers and what you add (hand to `restat-literature-positioning`)
- [ ] You have decided Article vs Short Paper (length/exhibit budget)
- [ ] Sibling check passed: not better at AER (general-interest) or *J. Econometrics* (method-first)
- [ ] If the contribution is measurement, the construct's validity and its applied payoff are both clear

## Anti-patterns

- Pitching a new estimator as the headline contribution (that is *J. Econometrics*, not REStat)
- A clean estimate with no applied stakes — "identified but uninteresting"
- A measurement contribution with no applied conclusion that changes
- Assuming REStat = AEJ:Applied exactly; REStat weights measurement and applied econometrics more
- Framing as field-internal when the applied parameter has broad interest (sells REStat short)

## Worked vignette: a measurement paper finding its home (illustrative)

An author has built a new county-level index of local labor-market tightness from job-posting data and shows
it predicts wage growth. Pitched as "a new index," it reads as a data note with no clear home. Re-framed for
REStat, the contribution becomes: *"We measure local labor-market tightness with less error than the
vacancy-to-unemployment proxy, and show that correcting this measurement reverses the estimated slope of the
wage curve."* Now the **measurement advance changes an applied conclusion** — squarely REStat's tradition,
and stronger than either a bare index (a data note) or a new estimator (J. Econometrics). The same project
would be undersold as field-internal at a labor journal and too narrow for AER.

## Output format

```
【Venue verdict】REStat (Article / Short Paper) | redirect to: [AER / AEJ:Applied / J.Econometrics / field]
【One-sentence contribution】measure/identify [object] in [setting] via [design] → [estimate] → matters for [question]
【Contribution type】identification | measurement | applied-econometrics
【Closest prior work】[3–5 papers] (→ restat-literature-positioning)
【Length track】Article | Short Paper (≤6000 words, ≤5 exhibits)
【Next step】restat-literature-positioning
```
