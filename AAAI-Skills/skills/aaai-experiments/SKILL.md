---
name: aaai-experiments
description: Use when designing or auditing AAAI experiments for the broad-AI program committee, including baselines, ablations, statistical significance, robustness, human evaluation, AI-for-Social-Impact and alignment/safety evidence, compute and cost reporting, and reproducibility-checklist alignment for Phase-1 survival.
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

## Evidence triage table

Because an AAAI reviewer from an adjacent subfield must trust your numbers quickly, classify each
experimental block by how much weight it can bear and what would strengthen it.

| Block | Carries the claim when | Reviewer doubt | Cheap reinforcement |
| --- | --- | --- | --- |
| Headline benchmark | beats tuned recent baselines | "lucky seed" | seeds, variance bars |
| Ablation | isolates one mechanism | "joint removal" | single-factor toggles |
| Robustness | holds across split/shift | "one setting" | extra split or perturbation |
| Human eval | protocol is documented | "rater bias" | IRB note, inter-rater agreement |

## Common AAAI experiment rejects

- Benchmark bump with no mechanism analysis, which a broad committee reads as engineering, not AI
  insight.
- Baselines weaker than current open-source systems, so the comparison looks unfair.
- A Social-Impact or alignment claim with no stakeholder, harm, or risk-mitigation evidence.
- Results that rely on a closed API with no reproducible substitute for the checklist.

## Worked vignette

A planning paper reports a single-seed win on one domain. Audit: the headline block "needs
robustness" and "needs variance", so the fix before the deadline is five seeds with confidence
intervals plus one extra IPC-style domain. Because new results cannot rescue this in rebuttal, the
team runs both before submission and aligns the checklist's seed answer to the supplement.

## Output format

```text
[Claim] <paper claim>
[Evidence status] sufficient / needs baseline / needs ablation / needs robustness / unclear
[Fairness issue] <compute, tuning, data, prompt, metric, human eval>
[Checklist dependency] <what checklist answer this supports>
[Fast fix] <experiment or analysis feasible before deadline>
```

