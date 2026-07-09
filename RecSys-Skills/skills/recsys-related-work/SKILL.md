---
name: recsys-related-work
description: Use when positioning an ACM RecSys submission against recommender-systems literature and its neighbors (SIGIR, KDD, WSDM, TheWebConf, UAI), including the reproducibility-critique line, arXiv and prior versions, concurrent work, ACM Digital Library archival status, and the citation coverage RecSys reviewers expect across recommendation subfields.
---

# RecSys Related Work

Use this to audit novelty and eligibility. Reopen the current Call for Contributions for
dual-submission, anonymity, and prior-publication rules before advising authors.

## Positioning checks

- Separate the **recommendation** contribution from generic ML improvement: a new ranking
  objective, user/item modeling idea, evaluation protocol, off-policy estimator, or empirical
  insight about deployed behavior.
- Cover the recommendation subfields your claim touches: collaborative filtering, sequential/
  session models, off-policy/counterfactual evaluation, fairness/diversity/exposure, and — for any
  empirical claim — the **reproducibility-critique** line.
- Treat ACM Digital Library, journal, and formal conference proceedings as archival unless current
  rules say otherwise.
- Cite arXiv and prior-version work so double-blind review survives; do not point reviewers to
  identity-revealing pages.
- Explain overlap with any concurrent or prior version, and do not submit duplicate archival work.

## Neighbor-venue coverage table

RecSys is a single-domain venue, but its neighbors publish recommendation-relevant work. A
reviewer checks whether you cite the *right* neighbor, not just RecSys itself.

| Neighbor venue | What it contributes to your related work | Reviewer check |
|---|---|---|
| SIGIR | Ranking models, IR evaluation, neural retrieval | Did you distinguish recommendation from ad-hoc retrieval framing? |
| KDD | Large-scale mining, the sampled-metrics critique | Is the scalability or evaluation-methodology neighbor acknowledged? |
| WSDM / TheWebConf | Web-scale recommendation, graph and CF methods | Is the nearest web-recommendation method compared? |
| UAI | Foundational ranking (e.g., BPR) and probabilistic modeling | Are canonical recommendation methods cited to their true venue, not RecSys? |
| Reproducibility line | "Are we really making much progress?" and follow-ups | Does your evaluation answer the tuned-baseline critique head on? |

A bibliography that cites only RecSys papers tells a reviewer you may have missed the method that
already solved this at a neighbor venue — a recognizable reject pattern that benchmark strength
does not repair.

## Positioning vignette

Imagine the paper proposes an exposure-corrected session ranker. Its nearest neighbors: a SIGIR
neural ranker with no exposure correction, a KDD paper on sampled-metric bias, and a prior RecSys
counterfactual-embedding paper. The novelty sentence should name all three contrasts — exposure
handling where the SIGIR line ignored it, full-ranking evaluation answering the KDD critique, and
a session-level objective where the prior RecSys work was static.

## Concurrent-work judgment calls

- Independently concurrent arXiv work: cite neutrally, state the technical difference, avoid
  priority claims reviewers cannot verify.
- Your own prior version: verify its archival status against the current CFP and phrase the
  citation so double-blind review survives.
- When unsure whether a venue is archival, declare the overlap on the submission form rather than
  gambling on a chair's interpretation.

## Output format

```text
[Eligibility] clear / needs declaration / risky
[Closest subfields] <CF / sequential / off-policy / fairness / reproducibility>
[Nearest 3 works] <work -> distinction (with true venue)>
[Archival-overlap risk] <none / issues>
[Novelty sentence] <RecSys-ready recommendation contribution contrast>
```
