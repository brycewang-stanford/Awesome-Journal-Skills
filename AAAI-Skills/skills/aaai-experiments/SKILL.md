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

## Claim-to-evidence ledger

Build this table before adding new experiments. It keeps the AAAI evidence package aligned with
the main text and with the reproducibility checklist.

| Manuscript claim | Required evidence | Phase-1 risk if missing | Checklist hook |
| --- | --- | --- | --- |
| New AI capability | benchmark + qualitative failure cases | broad reviewer sees only engineering | datasets, metrics, baselines |
| Better mechanism | single-factor ablations | gain looks like tuning luck | ablation and hyperparameter answers |
| Robust deployment | shift / seed / subgroup stress test | result seems brittle | variance, compute, environment |
| Social-impact or safety claim | stakeholder, harm, and misuse analysis | ethical claim looks asserted | ethics, limitations, data access |

For each row, mark **ready / weak / missing** and name the fastest fix that can be run before the
supplementary-material deadline. Do not leave a claim in the abstract if its evidence row is weak.

## AAAI-specific review pressure

- Phase 1 reviewers need a fast reason to trust the evidence.
- The reproducibility checklist must match the experiment descriptions.
- AI for Social Impact and AI Alignment claims require stronger treatment of stakeholders, harms,
  risk mitigation, and scope.
- New results usually cannot rescue the paper in rebuttal, so submit complete evidence upfront.
- The AI-assisted review pilot is non-decisional, but it may surface checklist mismatches; make
  result provenance, seeds, data splits, and limits machine-readable enough that a human SPC/AC can
  quickly audit them.

## Pre-rebuttal freeze rule

Before submission, decide which experiments would be impossible to add later under AAAI's rebuttal
constraints: missing baselines, missing seeds, missing supplement files, or missing reproducibility
checklist answers. Treat those as **pre-submission blockers**, not rebuttal TODOs. The author
response can explain and clarify submitted evidence; it should not depend on new results, URLs, or
repaired supplementary files.

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
[Pre-rebuttal blockers] <missing evidence that must be run before submission>
[Fast fix] <experiment or analysis feasible before deadline>
```
