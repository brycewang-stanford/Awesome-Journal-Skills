---
name: review-of-economic-dynamics
description: Use when targeting Review of Economic Dynamics (RED) or deciding whether a quantitative-macro / dynamic-economics manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Review of Economic Dynamics (review-of-economic-dynamics)

## Journal positioning

RED is the journal of the Society for Economic Dynamics (the SED), the leading outlet for quantitative dynamic macroeconomics. It rewards papers that take a dynamic equilibrium model seriously — solving it, calibrating or estimating it against data, and using it to answer a substantive macro or dynamic question. The readership is quantitative macroeconomists who care about heterogeneous agents, dynamic general equilibrium, and the mapping between model and data, so a paper must combine a real economic question with disciplined computational or structural execution.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the SED / Elsevier site and the editorial submission system.

## When to trigger

- The author names RED (or the SED outlet) as the target venue.
- A quantitative-macro paper with a structural/computational model needs a home narrower than the top-5 but above generic field outlets.
- An applied-macro paper needs re-framing so the contribution reads as a dynamic-equilibrium insight, not a reduced-form regression.
- The author needs RED's desk-reject risks and a credible quantitative-macro alternative list.

## Scope & topic fit

- Heterogeneous-agent macro (incomplete markets, wealth/earnings inequality, consumption-savings, HANK-style models).
- Dynamic general equilibrium applied to growth, business cycles, labor-market dynamics, fiscal/monetary policy, and life-cycle questions.
- Structural and computational models where solving the model is central to the contribution.
- Quantitative theory: a model disciplined by data, used to measure mechanisms or evaluate counterfactual policy.

## Method & evidence bar

- The model must be solved and disciplined credibly: calibration to documented moments, structural estimation, or both, with the identification of key parameters made transparent.
- Computational method matters — solution algorithm, state space, and accuracy should be defensible, and quantitative results should be robust to reasonable alternatives.
- Counterfactuals and welfare/policy statements must follow from the model's structure, not be asserted.
- Reduced-form evidence is welcome as discipline or motivation, but the contribution is the dynamic-equilibrium mechanism, not the regression.

## Structure & house style

- The introduction states the dynamic question, the model class, the quantitative mechanism, and the headline number early, and says why the equilibrium structure is necessary to answer it.
- Separate the modeling contribution from the calibration/estimation strategy from the quantitative finding.
- RED uses an unstructured abstract and JEL codes; an online appendix carries computational detail, robustness, and derivations.
- Exhibits should report economically interpretable magnitudes (decompositions, counterfactual gaps, welfare numbers), not only fit statistics.

## Official-submission checklist

- Search the live site for "Review of Economic Dynamics submission guidelines / guide for authors" and follow the current SED/Elsevier version.
- Re-check submission fee or SED-membership-related policy, formatting, abstract/JEL requirements, and anonymization expectations on the submission system.
- Re-check the current data and code / replication-material deposit policy and computational-artifact expectations.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why a quantitative macroeconomist should care about this mechanism.
- [ ] The contribution is stated as a dynamic-equilibrium mechanism / measurement, not as statistical significance.
- [ ] The introduction positions the paper against the current heterogeneous-agent / DGE frontier on this question.
- [ ] Solution method, calibration/estimation, and parameter identification are transparent and robust.
- [ ] Replication code and computational appendix are ready for the official deposit.

## Common desk-reject triggers

- A reduced-form macro paper with no structural or dynamic-equilibrium model.
- A model solved but not disciplined by data (no calibration target or estimation).
- A computational paper where the algorithm is a black box and accuracy is unaddressed.
- Counterfactuals or welfare claims that do not follow from the stated model.

## Re-routing decision

- General-interest macro at the top-5 → `american-economic-review` or the relevant AEA outlet; broad macro theory/measurement → `journal-of-monetary-economics`.
- Long-run growth and development dynamics → `journal-of-economic-growth`; monetary/financial-macro → `journal-of-money-credit-and-banking`.
- Broad European general-economics framing → `journal-of-the-european-economic-association` or `european-economic-review`; pure dynamic theory → `journal-of-economic-theory`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Review of Economic Dynamics
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the model + quantitative discipline clear RED's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / fee / JEL / replication code / appendix>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
