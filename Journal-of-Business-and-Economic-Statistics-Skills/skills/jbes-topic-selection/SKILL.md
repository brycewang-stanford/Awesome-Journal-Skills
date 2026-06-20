---
name: jbes-topic-selection
description: Use when deciding whether a project fits the Journal of Business & Economic Statistics (JBES) — the methods-with-empirics fit test. Checks methodological novelty plus clear empirical relevance before time is sunk; it does not develop the method itself.
---

# Topic / Scope Fit (jbes-topic-selection)

## When to trigger

- You are unsure whether a project is a JBES paper or belongs at an economics or pure-statistics journal
- You have a method but no convincing empirical use, or an application but no methodological novelty
- You want to confirm a machine-learning / data-science angle is in-scope before committing
- A co-author proposes JBES and you need a scope sanity check

## The JBES scope bar: methods + empirics, together

JBES publishes **high-quality methodological contributions** in statistics and econometrics oriented toward applications in **microeconomics, macroeconomics, business, and finance**. The defining filter is a **conjunction**, not a disjunction:

1. **Methodological novelty** — a new method, a genuine improvement to an existing one, a useful adaptation of a method from another field (**machine learning and data science are explicitly welcomed**), or a **computational** improvement that makes a method usable in practice.
2. **Clear empirical relevance** — even theoretical contributions are expected to matter for real applications, and a JBES paper **usually features a substantive empirical application**.

A project with only one leg is off-fit: **pure theory without empirical motivation**, or a **pure application with no methodological contribution**, reads as out of scope.

## Fit test (run before investing)

- **Novelty leg:** State in one sentence what is methodologically new. "We apply existing method X to dataset Y" fails; "we extend X to handle dependence/heavy tails/high dimension, with new asymptotics" passes.
- **Relevance leg:** Name the substantive empirical problem the method solves and the application you will show. "Illustrated on simulated data only" is weak; a real micro/macro/finance application is the norm.
- **Audience leg:** Would both an econometrician and an applied economist/statistician care? JBES bridges modern data science and classical econometrics; a method legible only to one narrow subfield is a harder sell.
- **Venue leg:** Is this better at a pure-statistics theory journal (no application needed) or a general economics journal (no method needed)? If yes, JBES is the wrong target.

## Checklist

- [ ] One-sentence statement of the **methodological** contribution exists
- [ ] A **substantive empirical application** (not just simulation) is planned or in hand
- [ ] The method's relevance to micro / macro / business / finance is concrete
- [ ] If ML/data-science: the adaptation to an econometric problem is the novelty, not the off-the-shelf tool
- [ ] The project is not better suited to a pure-theory or pure-applied venue
- [ ] Both methodologists and applied users would find it useful

## Anti-patterns

- A method paper with a toy illustration and no real application (off-scope at JBES)
- An applied paper that re-uses standard methods with no methodological novelty
- "We use deep learning" with no econometric problem genuinely solved by the adaptation
- Targeting JBES for a pure asymptotic-theory result with no empirical motivation
- Assuming JBES = a generic econometrics outlet; the empirics requirement is real

## Worked vignette: three projects through the fit test

Three hypothetical projects hit the JBES scope bar differently (verdicts **illustrative**). Project A — a new quantile-factor estimator for forecasting industrial production from FRED-MD — passes both legs: methodological novelty (a new estimator with asymptotics) and clear relevance (a real macro forecasting task). Project B — applying an off-the-shelf gradient-boosting model to predict firm defaults with no methodological increment — fails the novelty leg; it belongs at an applied finance journal. Project C — a pure minimax-rate theorem for a nonparametric estimator with no empirical motivation — fails the relevance leg; it belongs at a theoretical statistics journal. Only A satisfies the **conjunction** JBES demands.

## Scope-misfit patterns (venue-specific fixes)

| Why a project misfits JBES | Fix this skill enforces |
|----|----|
| Method with a toy illustration, no real application | Add a substantive micro/macro/business/finance case, or re-route to a statistics journal |
| Standard method on new data, no novelty | Find the methodological increment, or re-route to an applied economics journal |
| "We use deep learning" with no econometric problem solved | Make the adaptation to the econometric problem the novelty, not the off-the-shelf tool |

Calibration anchor (hedged): JBES scope is a **conjunction** — methodological novelty AND clear
empirical relevance, usually with a substantive application — at the statistics–econometrics interface
(time series and forecasting, volatility, causal inference, high-dimensional and Bayesian methods). A
single-leg project is off-fit.

## Output format

```
【Novelty leg】one-sentence method contribution: ... [pass/fail]
【Relevance leg】substantive application named: ... [pass/fail]
【ML/data-science?】adaptation is the novelty? [Y/N/NA]
【Better venue?】pure-theory / general-econ alternative considered? [Y/N]
【Verdict】in-scope for JBES? [Y/N]
【Next step】jbes-literature-positioning
```
