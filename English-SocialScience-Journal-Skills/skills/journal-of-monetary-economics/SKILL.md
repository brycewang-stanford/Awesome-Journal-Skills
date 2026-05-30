---
name: journal-of-monetary-economics
description: Use when targeting Journal of Monetary Economics (JME) or deciding whether a macro / monetary manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Journal of Monetary Economics (journal-of-monetary-economics)

## Journal positioning

The Journal of Monetary Economics (JME) is a field leader in macroeconomics and monetary economics, carrying the Carnegie-Rochester-NYU conference heritage of quantitative theory disciplined by data. It publishes work on business cycles, monetary and fiscal policy, inflation, growth, and the macro mechanisms that link them — typically a model that speaks to a macro question and is taken seriously to the data. The readership is macroeconomists, so a paper must matter for how the profession thinks about aggregate fluctuations or policy, not just fit a series well.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the publisher's own site or submission system.

## When to trigger

- The author names JME (or a top macro field outlet) as the target venue.
- A macro paper combines a quantitative model with empirical discipline and the author is choosing among macro field journals.
- An empirical-macro or monetary-policy paper needs re-framing so the mechanism, not the regression, is the contribution.
- The author needs JME's desk-reject risks and a credible macro alternative list before submitting.

## Scope & topic fit

- Business-cycle theory and quantitative macro: DSGE, RBC-descended and New Keynesian models, heterogeneous-agent macro.
- Monetary policy, inflation, the transmission mechanism, central-bank behavior, and the interaction of monetary and fiscal policy.
- Growth, productivity, and the long-run determinants of macro aggregates when framed for a macro audience.
- Empirical macro with credible identification of aggregate shocks or policy effects; macro-finance and macro-labor at the aggregate level.

## Method & evidence bar

- Quantitative theory is expected to be disciplined: calibration or estimation tied to data, with the model's mechanism made transparent and its quantitative claims defensible.
- Empirical macro must take identification of shocks/policy seriously (e.g., narrative, high-frequency, SVAR, local-projection approaches) and confront alternative explanations.
- A model needs a clear mechanism and a reason its quantitative answer differs from existing models — not a marginal extension with one more friction.
- Robustness across reasonable parameterizations, specifications, and sample choices is expected.

## Structure & house style

- The introduction states the macro question, the mechanism, the modeling/empirical strategy, and the quantitative headline, and says why it changes the macro conversation.
- Make the marginal contribution explicit against the closest quantitative-macro papers; separate the theoretical mechanism from the quantitative result.
- JME uses an unstructured abstract and JEL codes; an online appendix carries derivations, additional calibrations, and robustness.
- Exhibits emphasize quantitative magnitudes, impulse responses, and decompositions; the central mechanism should be legible from a key figure or table.

## Official-submission checklist

- Search the live site for "Journal of Monetary Economics guide for authors / submission guidelines" and follow the current Elsevier version, not a third-party broker's copy.
- Re-check formatting, abstract/JEL codes, reference style, the online-appendix policy, and the data & code / replication availability requirements.
- Re-check the current code-and-replication-package expectation and any conference-linked or invited-issue submission routes on the editorial system.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why a macroeconomist should change their view of cycles or policy because of this paper.
- [ ] The contribution is stated as mechanism / quantitative result / identification, not as model fit or significance.
- [ ] The introduction positions the paper against the current quantitative-macro frontier on this question.
- [ ] The model is disciplined to data (calibration/estimation) and empirical identification of shocks/policy is defensible.
- [ ] The replication package (code, data, calibration targets) is ready and reproducible.

## Common desk-reject triggers

- A model with one extra friction and no new quantitative or mechanistic insight.
- Empirical macro with a regression but no credible identification of the aggregate shock or policy change.
- A calibration that hits targets without a transparent or convincing mechanism.
- A micro or applied paper with no aggregate/macro payoff framed as macroeconomics.

## Re-routing decision

- General-interest macro at top-5 ambition → `american-economic-review` or `aej-macroeconomics`; quantitative dynamics → `review-of-economic-dynamics`.
- Long-run growth and development questions → `journal-of-economic-growth`.
- Money, banking, and policy-facing applied macro-finance → `journal-of-money-credit-and-banking`; macro-finance asset pricing → `journal-of-finance`.
- Open-economy / international macro → `journal-of-international-economics`; pure macro theory mechanism → `journal-of-economic-theory`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Journal of Monetary Economics
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the quantitative model / identification clear this venue's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / JEL / online appendix / replication package / formatting>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
