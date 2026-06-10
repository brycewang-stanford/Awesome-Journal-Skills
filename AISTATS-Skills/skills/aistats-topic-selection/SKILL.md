---
name: aistats-topic-selection
description: Use when deciding whether a project is a strong AISTATS fit, comparing AISTATS with NeurIPS, ICML, ICLR, UAI, COLT, JMLR, statistics journals, or application venues, identifying the statistical primitive of the contribution, and sharpening the AI-statistics framing before writing begins.
---

# AISTATS Topic Selection

Use this before writing. AISTATS is strongest for work at the intersection of artificial
intelligence, machine learning, and statistics, especially when statistical reasoning is not
merely an evaluation detail.

## Fit test

- Prefer AISTATS when the contribution advances statistical foundations, inference,
  uncertainty, causal or probabilistic modeling, learning theory, optimization, or empirical
  methodology with clear AI/ML relevance.
- Route to ICML, NeurIPS, or ICLR if the main contribution is broad ML systems, representation
  learning, scaling, or deep learning practice with limited statistical novelty.
- Route to UAI if the contribution is primarily uncertainty, probabilistic graphical models,
  causality, decision making under uncertainty, or Bayesian reasoning.
- Route to COLT if the contribution is mainly formal learning theory and the empirical story
  is secondary.
- Route to a statistics journal when the work needs journal-length exposition, extensive
  proofs, or a statistics audience more than an AI conference audience.
- Check early whether the result can be made convincing in an 8-page submission body.

## Fit signal table

| Signal in the project | AISTATS reading |
|---|---|
| Consistency, minimax rate, regret, or coverage result paired with experiments | Core fit — the house genre |
| Bayesian, causal, kernel, or high-dimensional methodology with guarantees | Core fit |
| Deep architecture with strong benchmarks but thin theory | Better served at NeurIPS, ICML, or ICLR |
| Pure theory with no plausible experiment | COLT or a statistics journal |
| Probabilistic reasoning without a learning angle | UAI or a statistics venue |

## Vignette: where a debiased estimator goes

A project delivers a debiased lasso variant with valid confidence intervals in high
dimensions and simulations confirming coverage. AISTATS reading: strong fit — an inference
guarantee plus validating experiments is exactly what this venue rewards. Strip the
inference theory and keep only prediction benchmarks, and the same project belongs at a
general ML venue; grow it into journal-length asymptotic refinements, and Annals of
Statistics or JMLR becomes the better home.

## Sharpening moves before committing

- Name the statistical primitive: estimator, test, bound, posterior, or identification
  result. If no primitive exists, the AISTATS framing does not exist either.
- Verify the proof load fits the format: the appendix may be long, but the 8-page body must
  carry the argument's spine on its own.
- Confirm the experiments can be designed to test the theory rather than merely accompany it;
  decoration-only benchmarks are a quiet fit failure here.
- Topic emphasis drifts between cycles; scan the current CFP subject-area list before final
  routing.

## Output format

```text
[Fit] strong AISTATS / possible AISTATS / better elsewhere
[Best venue] AISTATS / NeurIPS / ICML / ICLR / UAI / COLT / journal / other
[Contribution sentence] <one sentence>
[Top rejection risk] <novelty/statistics/evidence/clarity/scope>
[Next action] <theory, experiment, framing, or venue switch>
```
