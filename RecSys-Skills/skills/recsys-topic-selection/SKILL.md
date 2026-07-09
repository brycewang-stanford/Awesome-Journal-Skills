---
name: recsys-topic-selection
description: Use when deciding whether a project is a strong ACM RecSys fit, routing among RecSys, SIGIR, KDD, WSDM, TheWebConf, UAI, CHI, and general ML venues, identifying whether the core contribution is genuinely about recommendation, and choosing the right RecSys track before writing begins.
---

# RecSys Topic Selection

Use this before writing. RecSys is a **single-domain** venue: it is strongest when the central
claim is about **recommendation** — ranking objectives, user/item modeling, offline/online
evaluation, feedback loops, exposure and fairness, or deployed recommender behavior. Being merely
*applicable* to recommendation is not enough; the contribution has to speak to a recommender
audience.

## Fit test

- Prefer RecSys when the main claim is a recommendation result: a ranking objective, a
  user/session model, an evaluation protocol, an off-policy/counterfactual method, a
  fairness/diversity/exposure result, or a deployed-system insight.
- Route to **SIGIR** when the core is ad-hoc retrieval, search ranking, or IR evaluation not tied
  to recommendation.
- Route to **KDD** when the contribution is a general data-mining or large-scale algorithm and
  recommendation is just one application.
- Route to **WSDM / TheWebConf (WWW)** when the emphasis is web-scale search-and-mining or web
  systems broadly.
- Route to **UAI** or an ML venue when the contribution is a general learning/probabilistic
  advance rather than recommender-specific evidence.
- Route to **CHI / CSCW** when user or community outcomes dominate over the recommendation
  algorithm.

## Fit signal table

| Signal in the project | RecSys reading |
|---|---|
| A ranking/user-modeling idea evaluated with tuned baselines and a leakage-aware split | Core fit — the house genre |
| Off-policy or counterfactual evaluation of recommendations | Core fit — a RecSys distinctive |
| A deployed system with production constraints and A/B evidence | Core fit — route to the Industry track |
| A reproduction/refutation of prior recommender results | Core fit — route to the Reproducibility track |
| A general retrieval or mining method, recommendation as one demo | Better at SIGIR / KDD / WSDM |
| A general ML method with a recommender benchmark tacked on | Better at an ML venue |

## Which RecSys track

- Main long paper: a rounded recommendation contribution with offline (and ideally online)
  evidence.
- Main short / Past-Present-Future: one focused finding, or a reflective/forward-looking position.
- Reproducibility: repeating, refuting, or re-scoping prior results; a dataset or framework.
- Industry: a deployed system with production constraints and live evidence.
- Resource / Dataset: a community dataset or software resource with build methodology.

## Vignette: where an exposure-correction method goes

A project delivers an off-policy ranker with an exposure-corrected estimator and a simulator
bridge. RecSys reading: strong fit — a recommendation-specific evaluation advance is exactly what
the venue rewards, Main long paper. Strip the recommendation framing and keep only a generic
off-policy estimator, and it drifts toward an ML venue; turn it into a reproduction of three
published rankers, and the Reproducibility track becomes the right home.

## Sharpening moves before committing

- Name the recommendation primitive: the ranking objective, the user/item model, the evaluation
  protocol, or the deployment claim. If none exists, the RecSys framing does not.
- Confirm the evidence can meet the venue's evaluation bar (tuned baselines, leakage-aware split,
  reported variance) — decoration-only benchmarks are a quiet fit failure here.
- Topic emphasis and the track lineup drift between cycles (2026 dropped LBR, added R&P Notes);
  scan the current CFP before final routing.

## Output format

```text
[Fit] strong RecSys / possible RecSys / better elsewhere
[Best venue] RecSys / SIGIR / KDD / WSDM / TheWebConf / UAI / CHI / ML venue / other
[RecSys track] main-long / main-short / past-present-future / reproducibility / industry / resource
[Contribution sentence] <one sentence>
[Top rejection risk] <novelty / evaluation validity / scope / fit>
[Next action] <experiment, framing, or venue switch>
```
