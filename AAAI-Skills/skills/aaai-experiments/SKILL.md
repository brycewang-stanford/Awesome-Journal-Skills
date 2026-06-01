---
name: aaai-experiments
description: Use when designing or auditing AAAI experiments, including baselines, ablations, statistics, robustness, human evaluation, social-impact evidence, alignment/safety evaluation, and compute reporting.
---

# AAAI Experiments

Use this before submission to ensure empirical evidence supports the AI contribution. AAAI
reviewers may come from adjacent AI subfields, so experiments must be interpretable beyond one
benchmark community.

## Experiment audit

- Map every experimental block to a claim in the introduction.
- Compare against strong, recent, and fairly tuned baselines.
- Include ablations that isolate mechanisms rather than removing multiple components at once.
- Report uncertainty, variance, and statistical tests when small differences matter.
- Test robustness to data split, prompt, seed, environment, user population, or distribution shift
  when relevant.
- For human evaluation, document task, instructions, annotator pool, quality control, aggregation,
  and ethics/IRB status.
- Report compute, hardware, data access, model size, and training/inference cost.

## AAAI-specific review pressure

- Phase 1 reviewers need a fast reason to trust the evidence.
- The reproducibility checklist must match the experiment descriptions.
- AI for Social Impact and AI Alignment claims require stronger treatment of stakeholders, harms,
  risk mitigation, and scope.
- New results usually cannot rescue the paper in rebuttal, so submit complete evidence upfront.

## Output format

```text
[Claim] <paper claim>
[Evidence status] sufficient / needs baseline / needs ablation / needs robustness / unclear
[Fairness issue] <compute, tuning, data, prompt, metric, human eval>
[Checklist dependency] <what checklist answer this supports>
[Fast fix] <experiment or analysis feasible before deadline>
```

