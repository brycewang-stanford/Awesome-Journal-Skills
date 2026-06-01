---
name: iclr-topic-selection
description: Use when deciding whether a project is a strong ICLR submission, should be reframed for ICLR, or should be routed to NeurIPS, ICML, AAAI, AISTATS, ACL, CVPR, KDD, or another venue.
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

## Output format

```text
[ICLR fit] strong / plausible / weak / no
[Core learning insight] <one sentence>
[Evidence required] <theory, experiment, benchmark, artifact>
[Best venue route] ICLR / NeurIPS / ICML / AISTATS / UAI / domain venue / workshop
[Reframe] <how to make the paper more ICLR-shaped>
```

