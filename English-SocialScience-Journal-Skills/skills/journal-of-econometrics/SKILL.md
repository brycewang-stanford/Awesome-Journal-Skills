---
name: journal-of-econometrics
description: Use when targeting Journal of Econometrics or deciding whether a theoretical or applied econometrics manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Journal of Econometrics (journal-of-econometrics)

## Journal positioning

The Journal of Econometrics is one of the field-defining outlets for econometric methodology, publishing new estimators, asymptotic and finite-sample theory, and inference procedures alongside serious applied econometrics that advances method. The paper that wins here delivers a method whose properties are proven, whose behavior is demonstrated, and that other researchers will actually use — not a one-off application of an existing toolkit. The readership is econometricians and methodologically sophisticated empirical economists, so the contribution must read as a tool, not a finding.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the publisher's own site or submission system.

## When to trigger

- The author names Journal of Econometrics as the target venue.
- A manuscript proposes a new estimator, test, or inference procedure and the author is unsure whether the theory is developed enough.
- An applied paper rests on a method twist and the author must decide whether to frame it as methods (here) or as a field/applied contribution elsewhere.
- The author needs this venue's desk-reject risks and a credible methods/applied-econometrics alternative list before submitting.

## Scope & topic fit

- New estimators and tests with derived asymptotic theory (consistency, rates, limiting distributions) and, ideally, finite-sample analysis.
- Inference under realistic complications: heteroskedasticity, clustering, weak identification, high dimensionality, non-stationarity, dependence.
- Time-series and panel econometrics, nonparametric/semiparametric methods, microeconometrics, financial econometrics, and machine-learning-for-inference.
- Method that generalizes beyond one dataset; applied work is welcome when it carries a genuine methodological advance, not as a standard application.

## Method & evidence bar

- Theorems with complete, correct proofs are the core deliverable; assumptions must be stated precisely and their roles made transparent.
- Asymptotic results should be accompanied by Monte Carlo evidence showing finite-sample behavior, size/power, and sensitivity to assumption violations.
- A real-data illustration is expected to show the method matters, not to make a substantive empirical claim.
- Position the procedure against existing estimators on rate, robustness, assumptions relaxed, or computational feasibility — a clear improvement on a known frontier.

## Structure & house style

- The introduction states the inferential problem, what existing methods cannot do, the new procedure, and its theoretical properties, before any application.
- Separate the assumptions, the estimator/test definition, the asymptotic theory, the Monte Carlo design, and the empirical illustration into clean, signposted sections.
- A technical/supplementary appendix typically carries long proofs, additional simulations, and regularity conditions; the main text keeps the argument readable.
- Notation must be consistent and standard; exhibits report simulation results (bias, RMSE, size, power) legibly, and code is expected to be available.

## Official-submission checklist

- Search the live site for "Journal of Econometrics submission guidelines / guide for authors" and follow the current Elsevier/society version, not a third-party broker's copy.
- Re-check formatting, abstract/JEL or keyword codes, reference style, the supplementary-material/proof-appendix policy, and the data & code availability requirements.
- Re-check the current replication/code-deposit expectation and any structured-submission requirements on the editorial system.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why an econometrician would adopt this method over the current best alternative.
- [ ] The contribution is stated as a method / theorem / inference advance, not as an empirical result.
- [ ] The introduction positions the paper against the relevant estimation/inference literature and frontier.
- [ ] Proofs are complete and Monte Carlo evidence covers finite-sample size, power, and assumption violations.
- [ ] Code for the estimator and simulations is ready for deposit and reproducible.

## Common desk-reject triggers

- A standard application of an existing estimator with no methodological novelty.
- A proposed method with no asymptotic theory, or with proofs that are sketched, missing, or wrong.
- Monte Carlo "evidence" that omits adverse cases, size distortion, or comparison to incumbents.
- An empirical paper dressed as methods because it used a slightly modified specification.

## Re-routing decision

- Applied econometrics with a modest method twist but a real substantive finding → `journal-of-applied-econometrics` or `journal-of-business-and-economic-statistics`.
- Pure theory of identification with no estimator → `quantitative-economics`; a finished general-interest result → `econometrica`.
- A method built for one field's data → the relevant field venue (`journal-of-international-economics`, `journal-of-labor-economics`, `journal-of-monetary-economics`) framed as applied.
- If the contribution is substantive economics, not inference, route to a general or field economics journal instead.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Journal of Econometrics
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the theory + Monte Carlo evidence clear this venue's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / proof appendix / abstract / code deposit / formatting>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
