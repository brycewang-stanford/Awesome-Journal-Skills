---
name: issta-experiments
description: Use when designing or auditing ISSTA experiments, covering real subject programs and benchmarks like Defects4J, fair tool-baseline configuration, bug-finding and coverage metrics, non-parametric comparison with effect sizes, equal-budget protocols, repeated runs, and matching evidence to the claim being made.
---

# ISSTA Experiments

Use this before submission when the evaluation is not yet locked. ISSTA experiments earn or lose the
paper on the evaluation criterion, and the reviewer pool knows the standard subjects, baselines, and
statistics — so design the study to answer the exact claim, on subjects a reviewer recognizes.

## Experiment audit

- Match each claim to its evidence: a bug-finding claim needs a benchmark with ground truth, a
  coverage claim needs a measurement protocol, a scalability claim needs a size sweep.
- Use real subjects and established benchmarks where they exist — Defects4J for Java faults,
  real-world CVEs for security bugs, standard fuzzing corpora — so results are comparable to prior
  work, not to a private subject set.
- Configure baselines fairly and at an **equal budget**: same time, same seeds, same subjects. A
  baseline throttled to lose is the fastest way to lose a reviewer's trust.
- Compare with proper statistics: non-parametric tests (e.g. Mann-Whitney U) and an effect size
  (e.g. Vargha-Delaney Â₁₂) rather than a single run, because testing and analysis results are
  stochastic and rarely normal.
- Report the stochastic protocol: seeds, timeout budgets, iteration counts, number of repeated runs,
  and hardware. State whether a table is a mean over runs and give the spread.
- Audit for the usual confounds: subject selection bias, overfitting to the benchmark, counting
  duplicate crashes as distinct bugs, and mismatches between what the metric measures and what the
  claim asserts.

## What experiments are for at this venue

- ISSTA experiments exist to show a technique *works on software that matters*, evaluated fairly.
  One well-designed study on an established benchmark outweighs five extra ad-hoc subjects.
- The strongest evaluations separate *finding* from *being right*: a repair that passes tests is not
  a correct repair; a crash is not automatically a distinct bug. Report the gap between the easy
  metric and the property you care about.
- Reviewers check that the subjects and budget make the comparison meaningful — a fuzzer compared for
  one hour says little about a claim over 24-hour campaigns.

## Claim-to-evidence design table

| Claim | Matching evaluation | Reject pattern avoided |
|---|---|---|
| "Finds more true bugs" | Established benchmark with ground-truth labels; dedup by root cause | "Bugs counted by distinct crashes, not distinct faults" |
| "Higher coverage than baseline X" | Equal budget, same subjects, same instrumentation | "Baseline run in a weaker configuration" |
| "Scales to large programs" | Size sweep with wall-clock and memory reported | "Scalability asserted, never measured" |
| "Improvement is real, not noise" | Repeated runs + non-parametric test + effect size | "Single run presented as representative" |

## Vignette: evaluating a test-generation tool

A paper claims a new generator achieves higher fault-detection than an existing one. The plan:
run both on Defects4J at an equal per-subject time budget, repeat each configuration enough times to
estimate variance, count *detected faults* (not generated tests), compare with a non-parametric test
and report Â₁₂, and disclose the subjects where the tool underperforms rather than dropping them.

```text
subjects      Defects4J (pinned revision), N faults
budget        equal wall-clock per subject, both tools
runs          R repeats per subject; report mean and spread
metric        faults detected (ground truth), not tests generated
statistic     Mann-Whitney U + Vargha-Delaney A12
honesty       report subjects where the tool loses
```

## Statistical reporting floor

- Repeated runs and seeds for every stochastic result; captions must say what the numbers summarize.
- Report the compute actually consumed, not vague feasibility language.

## Output format

```text
[Evaluation readiness] strong / adequate / weak
[Claim -> evidence map] <claim: benchmark/metric/statistic>
[Baseline fairness] equal-budget / configured-to-lose / unclear
[Statistical gaps] <runs / test / effect size / variance>
[Subject/benchmark gaps] <established benchmark used? subjects pinned?>
[Decision-critical next run] <one experiment>
```
