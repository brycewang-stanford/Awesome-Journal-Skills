---
name: quantitative-economics
description: Use when targeting Quantitative Economics (QE) or deciding whether a structural / quantitative manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Quantitative Economics (quantitative-economics)

## Journal positioning

Quantitative Economics is an Econometric Society open-access journal devoted to quantitative economics that combines structural and computational modeling with data. It publishes both methodological contributions and quantitatively rigorous applied work — the common thread is taking models seriously enough to confront them with data through estimation, calibration, or computation. What wins here is a paper where the economic model and the quantitative implementation are both first-rate. The readership is structural and quantitative economists across micro and macro who care about model-based inference.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Econometric Society / journal site and the submission system.

## When to trigger

- The author names QE as the target venue.
- A structural / computational paper has a serious model-meets-data contribution and the author is choosing among quantitative venues.
- A reduced-form or theory paper has a strong quantitative-modeling extension that needs re-framing toward QE's strengths.
- The author needs QE's desk-reject risks and a credible quantitative / econometrics alternative list.

## Scope & topic fit

- Structural estimation and quantitative modeling across micro and macro: dynamic models, heterogeneous agents, IO, labor, public, trade, macro.
- Computational and numerical methods for solving and estimating economic models.
- Econometric methods oriented toward structural / model-based inference and identification.
- Quantitatively rigorous applied work where the model carries the contribution, not only the reduced-form result.

## Method & evidence bar

- The model and its quantitative implementation must both be rigorous: clear economic structure, credible identification of structural parameters, and sound estimation / calibration / computation.
- Identification of the structural model should be transparent — what in the data pins down the parameters.
- Numerical methods and computational choices must be documented and defensible; results should be robust to reasonable alternatives.
- As an Econometric Society journal, the standard for technical correctness and transparency is high; replication code is part of the package.

## Structure & house style

- The introduction should state the economic question, the model, the identification, and what the quantitative exercise delivers (counterfactuals, decompositions, estimates).
- Frame the contribution as a model-based advance — methodological, or an applied result that only a structural approach could deliver.
- Use an abstract and JEL codes; relegate derivations, computational detail, and robustness to a supplement / appendix.
- As an open-access journal, follow the current Econometric Society formatting; supplementary material and replication packages are expected.

## Official-submission checklist

- Search the live site for "Quantitative Economics submission guidelines / Econometric Society instructions for authors" and follow the current version.
- Re-check word/figure limits, abstract and JEL requirements, reference and math style, anonymization expectations, and any open-access / article-processing arrangements.
- Re-check the current replication / data and code archive policy (Econometric Society replication requirements).
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating what the quantitative / structural approach delivers that reduced-form work could not.
- [ ] The contribution is stated as model + identification + quantitative result, not as a significant coefficient.
- [ ] Identification of the structural parameters is transparent and defensible.
- [ ] Computational methods, robustness, and replication materials meet Econometric Society standards.
- [ ] Open-access / formatting and the replication archive requirements are satisfied.

## Common desk-reject triggers

- A reduced-form paper with no genuine structural / quantitative-modeling contribution.
- A structural model with opaque or hand-waved identification of its parameters.
- Undocumented computational choices or results that are not robust.
- A pure-theory paper with no quantitative implementation, or applied work where the model is decorative.

## Re-routing decision

- Pure econometric theory / estimators with proofs → `econometric-theory` or `the-econometrics-journal`; applied-econometrics methods → `journal-of-econometrics`.
- General-interest structural work with broad ambition → `american-economic-review`; macro-structural → `aej-macroeconomics` or `journal-of-monetary-economics`.
- Theory-only contributions → `journal-of-economic-theory`; behavioral/experimental → `journal-of-economic-behavior-and-organization`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Quantitative Economics
[Topic tags] <2–3 closest topics>
[Method/evidence] <do the model and quantitative implementation clear this venue's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / JEL / open-access / replication archive / computation docs>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
