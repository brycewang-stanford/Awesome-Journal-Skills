---
name: dac-experiments
description: Use when designing or auditing the empirical evaluation of an ACM/IEEE Design Automation Conference (DAC) Research Manuscript, covering standard EDA benchmark suites (ISPD, EPFL, ISCAS/ITC, TAU, CircuitNet, OpenROAD flows), fair state-of-the-art baselines, QoR/PPA reporting with runtime, per-benchmark honesty, ablations that isolate the mechanism, and contamination-aware ML-for-EDA evaluation.
---

# DAC Experiments

Use this before the November deadline when the evaluation is not yet locked. At DAC the evaluation
*is* the paper: reviewers are EDA practitioners who decide acceptance mostly on whether the **QoR
comparison is fair, standard, and reproducible**. The organizing principle is **measured design
quality against the strongest baseline on recognized benchmarks** — not novelty in the abstract.

## Evaluation audit

- **Use standard benchmark suites.** Match the suite to the task: **ISPD** placement/routing
  contests, the **EPFL** combinational benchmark suite for logic synthesis, **ISCAS'85/'89** and
  **ITC'99** for test/verification, the **TAU** contests for timing, **CircuitNet/OpenABC-D** and
  similar for ML-for-EDA, and **OpenROAD / OpenROAD-flow-scripts** for full-flow experiments. A
  private-benchmark-only evaluation is a scored weakness.
- **Compare against the true state of the art,** tuned with a documented, equal effort. An untuned
  or outdated baseline is the most common DAC reject cause; the assigned reviewer often *is* the
  author of the stronger tool you skipped.
- **Report the whole suite, not a subset.** Per-benchmark tables with the full circuit set; a
  cherry-picked average invites "what happened on the circuits you dropped?"
- **Report runtime and scalability,** not just quality. EDA reviewers care whether the method scales
  to realistic design sizes (millions of cells), so include the largest benchmarks and the compute
  used.
- **Ablate the mechanism.** Isolate where the gain comes from — remove your key component and show
  the QoR degrade — so the reviewer can attribute the improvement to your idea, not to tuning.
- **Design threats in.** Know before you run which designs, PDKs, or corners limit generality, and
  instrument to bound them.

## Claim-to-evidence design table

| DAC claim | Matching evidence | Reject pattern avoided |
|---|---|---|
| "Reduces wirelength / congestion" | Per-benchmark WL/DRC on ISPD vs a tuned SOTA placer | "Only averages; weak baseline" |
| "Closes timing better" | WNS/TNS across TAU/real designs, equal area/power | "Improved slack by hurting area silently" |
| "Fewer verification escapes / more coverage" | Coverage/bug-find on ISCAS/ITC or real RTL vs prior tool | "Toy circuits only" |
| "Scales to large designs" | Runtime/memory at million-cell scale | "Small benchmarks; scalability asserted" |
| "ML method predicts QoR" | Held-out designs, error metrics vs analytical/prior-ML baseline | "Trained and tested on the same designs" |
| "The new component drives the gain" | Ablation removing it | "Contribution and tuning entangled" |

## PPA and QoR reporting floor

- Report the **full PPA picture**: a wirelength or timing win that silently costs area or power is
  not a win — show the trade-off.
- Give **per-benchmark numbers** and the aggregate; state the geometric-mean convention you use.
- Report **runtime** for both your method and the baseline on the same hardware, and the hardware.
- For stochastic methods (simulated annealing, RL-based flows) report **variance across seeds/runs**,
  not a single lucky run.

## Contamination-aware ML-for-EDA evaluation

When a learner is in the loop, the reviewer's first questions are about leakage and fairness:

```text
[Split integrity]  train and test on DIFFERENT designs/netlists; never leak a test design into
                   training. Report the split explicitly.
[Baseline]         compare against the strong non-ML tool (analytic placer, classical STA) AND the
                   prior-ML method, not just an untrained control
[Generalization]   evaluate on designs/technology nodes unseen in training; ML-for-EDA that only
                   works on its training distribution is a scored weakness
[Determinism]      report seeds and variance; a single run is not evidence for an RL flow
[Cost honesty]     report training cost and inference cost; a method needing per-design retraining
                   must say so
[Data provenance]  name the dataset (CircuitNet, OpenABC-D) and version; cache generated data
```

## Vignette: evaluating a new global router

A paper claims a router that cuts congestion at equal wirelength. The matching plan: run on the full
**ISPD** routing benchmark set (not a subset); compare against the **strongest published router**
tuned to equal effort; report per-benchmark wirelength, DRC/overflow, and **runtime** on stated
hardware; include the largest circuits to show scaling; ablate the congestion-aware component to
show it, not parameter tuning, drives the gain; and state external validity (technology node,
macro density) as a bounded threat — every number traceable to a logged, re-runnable flow.

## Output format

```text
[Evaluation readiness]  strong / adequate / weak
[Benchmarks]            standard suite(s) named + full set reported? yes/no
[Baseline fairness]     strongest SOTA, tuned, equal effort, on same hardware? yes/no
[QoR completeness]      full PPA + runtime + variance reported? yes/no
[Ablation]              mechanism isolated from tuning? yes/no
[ML leakage]            train/test designs disjoint + unseen-node generalization? yes/no/NA
[Decision-critical run] the one experiment that would most strengthen the case
```
