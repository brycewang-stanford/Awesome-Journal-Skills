---
name: journal-of-applied-econometrics
description: Use when targeting Journal of Applied Econometrics (JAE) or deciding whether an applied-econometric manuscript that brings methods to a substantive economic question fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Journal of Applied Econometrics (journal-of-applied-econometrics)

## Journal positioning

JAE is a leading outlet for applied econometrics — econometric methods brought to bear on substantive economic questions, with a strong tradition of data-rich, replicable empirical work. It maintains a data archive, and replicability is part of its identity. It rewards papers that either apply existing methods in a careful, illuminating way or develop a method that is demonstrably useful in a real application; it is methods-in-application, not pure econometric theory. The readership is applied econometricians, so both the method and the empirical payoff must be convincing.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the journal/Wiley site and the editorial submission system.

## When to trigger

- The author names JAE as the target venue, or wants a home for a methods-in-application empirical paper.
- A paper develops or applies an econometric method and the empirical application is central.
- A data-rich empirical paper needs re-framing so the econometric method and its application are foregrounded.
- The author needs JAE's desk-reject risks and a credible applied-econometrics alternative list.

## Scope & topic fit

- Applied econometric analyses of substantive economic questions across fields, with the method made explicit.
- Time series, panel, micro-econometric, and Bayesian methods applied to real data.
- Forecasting and model evaluation grounded in an economic application.
- Methodological contributions demonstrated in, and motivated by, a genuine empirical problem.

## Method & evidence bar

- The econometric method must be appropriate, correctly applied, and clearly tied to the economic question; identification and inference are scrutinized.
- Data quality, sample construction, and robustness matter; results should be shown to be stable across specifications.
- Replicability is central: the analysis should be reproducible from deposited data and code in the journal's archive.
- A pure theory result with no application, or an application with sloppy econometrics, does not fit.

## Structure & house style

- The introduction states the economic question, the econometric approach, why that method is needed, and the headline finding early.
- Make clear whether the contribution is the method, the application, or both, and position against the relevant applied-econometrics literature.
- Uses an unstructured abstract and JEL codes; an appendix and the data archive carry derivations, robustness, and replication materials.
- Exhibits report estimates with proper inference and interpretable magnitudes; specification and robustness tables are expected.

## Official-submission checklist

- Search the live site for "Journal of Applied Econometrics submission guidelines / author guidelines" and follow the current Wiley version, and note the JAE Data Archive requirements.
- Re-check formatting, abstract/JEL requirements, anonymization, and figure/table standards on the submission system.
- Re-check the current data and code deposit policy and the JAE Data Archive submission workflow (a permanent, replication-focused feature of this journal).
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the substantive economic question and why this econometric method answers it.
- [ ] The contribution is stated as method-in-application / identification / measurement, not as statistical significance.
- [ ] The introduction positions the paper against the relevant applied-econometrics literature.
- [ ] Method, identification, and inference are correct; results are robust across specifications.
- [ ] Data and code are ready for the JAE Data Archive and replication.

## Common desk-reject triggers

- Pure econometric theory with no genuine empirical application.
- An application with inappropriate or incorrectly applied econometrics.
- A method that adds nothing beyond standard tools for the question at hand.
- Results not reproducible / data and code not depositable to the archive.

## Re-routing decision

- Pure econometric theory and methods → `journal-of-econometrics`; methods at the statistics/econometrics interface → `journal-of-business-and-economic-statistics`.
- General-interest applied result → `american-economic-review`; applied micro with policy identification → `journal-of-human-resources`.
- Technically heavy theory/econometrics → `international-economic-review`; broad general field → `european-economic-review`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Journal of Applied Econometrics
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the method-in-application clear JAE's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / JEL / JAE Data Archive / replication / exhibits>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
