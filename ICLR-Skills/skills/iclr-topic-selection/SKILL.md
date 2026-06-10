---
name: iclr-topic-selection
description: Use when deciding whether a project is a strong ICLR submission, should be reframed for ICLR, or should be routed to NeurIPS, ICML, AAAI, AISTATS, ACL, CVPR, KDD, or another venue. Use when a project lacks a clear representation-learning insight, when an application result needs a learning contribution to fit ICLR, or when weighing ICLR's deep-learning center of gravity against a better-matched venue.
---

# ICLR Topic Selection

Use this when a project is still movable. ICLR is broad, but the paper should teach the learning
community something about representations, objectives, models, data, optimization, evaluation, or
deployment.

## Strong ICLR signals

- A clear representation-learning, model-behavior, optimization, generative modeling, RL, theory, or
  evaluation contribution.
- Evidence that changes how researchers should build, analyze, or judge learning systems.
- A simple central claim that can be verified by focused theory, experiments, or artifacts.
- Interest beyond one dataset, product, or application vertical.
- Honest limitations and ethics treatment for high-impact model or data claims.

## Weak ICLR signals

- Pure application paper with little learning insight.
- Incremental benchmark bump without mechanism, analysis, or robust evidence.
- Closed system claim that reviewers cannot inspect or reproduce.
- Dataset-only paper without a learning-representation or evaluation advance.
- Theory result disconnected from modern learning practice and not routed to a theory-focused venue.

## Routing logic

- Prefer NeurIPS or ICML for broader ML method/theory work with less ICLR-specific representation
  framing.
- Prefer AISTATS or UAI for statistics, uncertainty, causal, or probabilistic emphasis.
- Prefer ACL, CVPR, KDD, or robotics/HCI venues when the contribution is primarily domain-specific.
- Prefer workshops when the idea is timely but under-evidenced.

## Fit-versus-route decision table

ICLR's center of gravity is deep representation learning: architectures, self-supervision,
generative models, foundation models, RL with deep function approximation, optimization for deep
nets, interpretability, and alignment. Score the project against that center before routing.

| Project shape | ICLR fit | Better route if not ICLR |
| --- | --- | --- |
| New self-supervised objective with analysis | Strong | — |
| Theory explaining a deep-net phenomenon | Strong | AISTATS/UAI if purely statistical |
| LLM/foundation-model behavior study | Strong | ACL if narrowly language-specific |
| Benchmark bump, no mechanism | Weak | Domain venue or workshop |
| Causal/uncertainty emphasis | Plausible | AISTATS or UAI |
| Deployed application, little learning insight | Weak | KDD, CVPR, robotics/HCI venue |

## Worked vignette

A team has a method that improves recommendation click-through in production. As written it is an
application paper. To make it ICLR-shaped, they extract the representation-learning claim: a new
contrastive objective that yields embeddings transferring across catalogs, demonstrated with an
ablation and a probe on a public dataset. The product result becomes one validation point, not the
contribution. If that reframing fails to surface a learning insight, the honest route is KDD.

## Reviewer-pushback patterns

- "No learning insight, just engineering." Reframe around the mechanism or route to a domain venue.
- "Dataset-only paper." Add an evaluation or representation advance, or target a datasets-and-
  benchmarks track instead.
- "Theory disconnected from practice." Tie the result to an observed deep-learning phenomenon.

## Output format

```text
[ICLR fit] strong / plausible / weak / no
[Core learning insight] <one sentence>
[Evidence required] <theory, experiment, benchmark, artifact>
[Best venue route] ICLR / NeurIPS / ICML / AISTATS / UAI / domain venue / workshop
[Reframe] <how to make the paper more ICLR-shaped>
```

