---
name: wacv-experiments
description: Use when designing or auditing WACV experiments, covering Applications-track systems evidence (latency, power, robustness under real constraints) versus Algorithms-track matched-baseline novelty, comparative assessment under the deployed condition, uncertainty over seeds and sessions, ablations, and evidence that survives the two-round review.
---

# WACV Experiments

Use this to build evidence a WACV reviewer accepts in Round 1 instead of sending to Revise
and Resubmit. The controlling idea: WACV reviews under **two tracks**, and each track has a
different evidence bar. Facts are the WACV 2026/2027 cycles as read on 2026-07-09.

## Evidence by track

| Question the reviewer asks | Applications track | Algorithms track |
|---|---|---|
| Does it work where it must? | Metric **under the deployment constraint** (power/latency/light/data budget) | Metric on the standard benchmark |
| Is the comparison fair? | Baselines re-tuned to the **same constraint**, not their defaults | Baselines under **matched backbone/compute** |
| What does it cost? | Measured latency, wattage, memory on the **named device** | FLOPs/params/throughput reported honestly |
| When does it fail? | Failure cases under the real condition | Ablation isolating the mechanism |
| Is the gain real? | Uncertainty over sessions **and** seeds | Uncertainty over seeds; significance where small |

The single most common WACV revision request is "you compared against baselines at their
defaults, not under your constraint." Pre-empt it: an Applications claim is only supported if
the baselines were given the same power/data/latency budget you operated under.

## The four implicit questions

Design the experiment section to answer, in order: **does it work, why, when does it fail,
and what does it cost.** For an applications paper the "what does it cost" row is
load-bearing — a system that hits accuracy but blows the power budget has not made the
contribution it claims.

## Comparative assessment under the deployed condition

```text
For each baseline B and each headline claim C under constraint K:
  1. Re-tune / re-run B under K (same budget, same data regime) — not B's paper defaults.
  2. Report your method and B on the same axis (e.g., boundary-F1 @ K watts).
  3. Include an unconstrained upper-bound reference so the reader sees the cost of K.
  4. Report each number with a spread (std over seeds and, for field/systems work, sessions).
If any baseline was run only at its default and not under K, the comparison is not yet fair.
```

## Uncertainty and honesty

- Report variance: standard deviations over seeds, and for deployed/field systems over
  repeated sessions or devices, not a single run.
- Do not overclaim when a gap is within the spread; say "within a small margin" and show the
  numbers. WACV reviewers, being applications-minded, distrust hero runs.
- Keep the exact split, device, meter, and hyperparameters in the supplement so a Round 2
  reviewer can confirm nothing changed silently between rounds.

## Ablations that isolate the claim

An ablation should remove exactly the component your contribution rests on and show the
metric move under the same condition. For an Algorithms-track paper this is the core of
novelty; for an Applications-track paper, ablate the part that makes the system meet the
constraint (the low-power front end, the data-efficient step), not a generic layer.

## Reverify each cycle

- The two-track review criteria and any track-specific evidence expectations.
- Whether specific reporting (compute, energy) is requested in the current guidelines.
- Dataset licensing/anonymity rules for any data released with the paper.

## Output format

```text
[Track] Applications / Algorithms
[Works] headline metric under the required condition: <value ± spread>
[Fair] baselines run under the same constraint: yes/no
[Cost] latency/power/FLOPs on named device: <reported?>
[Fails] failure analysis under the real condition: <present?>
[Uncertainty] spread over seeds/sessions: yes/no
[R&R risk] <the comparison a reviewer would call unfair>
```
