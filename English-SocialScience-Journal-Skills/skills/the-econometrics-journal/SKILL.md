---
name: the-econometrics-journal
description: Use when targeting The Econometrics Journal (EctJ) or deciding whether an econometrics manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# The Econometrics Journal (the-econometrics-journal)

## Journal positioning

The Econometrics Journal is the Royal Economic Society's econometrics journal, with a European base, publishing econometric theory and methods. It covers new estimators, inference procedures, and theoretical results, as well as substantial methodological contributions, typically technical in nature. What wins here is a genuine econometric advance — a new method with established properties, or a theoretical result that improves how empirical work is done. The readership is econometricians and methodologically oriented empirical economists.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the RES / Oxford University Press site and the submission system.

## When to trigger

- The author names The Econometrics Journal (EctJ) as the target venue.
- An econometric-methods paper has a new estimator / test / inference result and the author is choosing among econometrics venues.
- A technical methods contribution from applied work needs re-framing as a standalone econometric advance.
- The author needs EctJ's desk-reject risks and a credible econometrics alternative list.

## Scope & topic fit

- Econometric theory: new estimators, inference procedures, asymptotic and finite-sample results.
- Methods for time series, panels, cross-section, semiparametric and nonparametric inference, and microeconometrics.
- High-dimensional, machine-learning-adjacent, and causal-inference econometrics with rigorous theory.
- Computationally intensive methods and simulation-based inference with established properties.

## Method & evidence bar

- A genuine methodological contribution: a new procedure with derived properties (consistency, asymptotic distribution, finite-sample behavior) or an important theoretical result.
- Proofs and regularity conditions must be complete and correct; assumptions clearly stated and defensible.
- Monte Carlo evidence should be informative about finite-sample performance, not a token table; an empirical illustration is often expected.
- Positioning against the closest existing methods — what the new method does that incumbents cannot.

## Structure & house style

- The introduction should state the inferential problem, why existing methods fall short, the new procedure, and its properties.
- Frame as a methods contribution; an empirical application illustrates the method rather than carrying the paper.
- Use an abstract and JEL codes; relegate proofs and extended Monte Carlo / derivations to appendices or a supplement.
- Notation and theorem-proof structure must be clean and standard; results should be stated precisely.

## Official-submission checklist

- Search the live site for "The Econometrics Journal submission guidelines / RES instructions for authors" and follow the current OUP version.
- Re-check word/figure limits, abstract and JEL requirements, reference and math/notation style, and anonymization expectations.
- Re-check the current replication / data and code and supplementary-material policy.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the inferential problem and what the new method does that existing methods cannot.
- [ ] The contribution is stated as a method / theorem with established properties, not as an empirical finding.
- [ ] Proofs, regularity conditions, and asymptotics are complete and correct.
- [ ] Monte Carlo evidence is informative about finite-sample behavior; the illustration supports the method.
- [ ] Notation, formatting, and replication materials meet the current guide.

## Common desk-reject triggers

- An applied paper using standard methods with no new econometric contribution.
- A "new method" without derived properties or with incomplete / incorrect proofs.
- Token Monte Carlo evidence or an application that does not demonstrate the method's value.
- A method indistinguishable from existing procedures, or poorly positioned against them.

## Re-routing decision

- Higher-visibility or US-centered applied-econometrics methods → `journal-of-econometrics`; applied-econometrics with empirical emphasis → `journal-of-applied-econometrics` or `journal-of-business-and-economic-statistics`.
- Highly technical, proof-driven theory → `econometric-theory`; econometrics for structural / quantitative work → `quantitative-economics`.
- A flagship econometric advance with broad reach → `econometrica`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] The Econometrics Journal
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the method contribution and its theory clear this venue's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / JEL / notation / data-code / supplement>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
