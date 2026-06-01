---
name: aaai-topic-selection
description: Use when deciding whether a project is a strong AAAI submission, should be reframed for AAAI, or should be routed to IJCAI, NeurIPS, ICML, ICLR, AISTATS, UAI, ACL, CVPR, KDD, CHI, or another venue.
---

# AAAI Topic Selection

Use this while the project is still movable. AAAI is broad across artificial intelligence, so a
strong submission should make an AI contribution that is intelligible beyond a narrow subfield.

## Strong AAAI signals

- Clear AI problem and contribution: method, theory, system, benchmark, dataset, evaluation, social
  impact, alignment, human-AI interaction, planning, reasoning, learning, NLP, vision, robotics, or
  knowledge representation.
- Evidence that supports a general AI claim, not only a local application result.
- Responsible treatment of ethics, safety, privacy, fairness, social impact, or misuse when the
  paper touches those areas.
- Reproducibility path strong enough for checklist scrutiny.
- Narrative clear enough for Phase 1 reviewers from adjacent AI areas.

## Weak AAAI signals

- Pure application deployment with little AI insight.
- Benchmark bump without mechanism, analysis, or robust comparison.
- Closed system with no reviewable evidence.
- Paper better framed as statistics, NLP, vision, HCI, robotics, or systems for a specialist venue.
- Policy-sensitive claims with thin ethics or stakeholder analysis.

## Routing logic

- Prefer IJCAI for broad AI work with an international AI community emphasis.
- Prefer NeurIPS, ICML, or ICLR for stronger ML method/theory or representation-learning framing.
- Prefer AISTATS or UAI for statistics, uncertainty, causal, or probabilistic emphasis.
- Prefer ACL, CVPR, KDD, CHI, ICRA, or systems venues when the contribution is domain-specific.
- Prefer a workshop if evidence is preliminary but the idea is timely.

## Output format

```text
[AAAI fit] strong / plausible / weak / no
[Track route] Main / AI for Social Impact / AI Alignment / other
[Core AI contribution] <one sentence>
[Evidence required] <experiment, theory, artifact, stakeholder analysis>
[Best venue route] AAAI / IJCAI / NeurIPS / ICML / ICLR / AISTATS / UAI / domain venue
```

