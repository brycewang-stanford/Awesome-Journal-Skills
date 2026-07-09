---
name: sigmetrics-experiments
description: Use when designing or auditing ACM SIGMETRICS evaluations, covering theorem-plus-validation rigor, stating and testing modeling assumptions, analysis-vs-simulation agreement, real workloads and traces, fairly tuned baselines, statistics and confidence intervals for stochastic systems, learning guarantees, measurement provenance, and matching evidence to the shape of each performance claim.
---

# SIGMETRICS Experiments

Use this before submission when the evidence is not yet locked. SIGMETRICS reviewers are
performance-evaluation specialists; the evaluation is where a good model or measurement is won or
lost. The organizing principle is **evidence proportional to the claim** — an analytic claim needs a
proof *and* validation, a measurement claim needs a methodology a skeptic accepts, and a learning
claim needs a guarantee, not only a benchmark score.

## Evaluation audit

- **Match evidence to the claim shape.** A claim about a **bound** needs a proof plus a simulation
  that shows the analytic curve is right; a claim about a **real system** needs measured data and a
  documented methodology; a claim about a **learner** needs a regret/convergence guarantee; a claim
  about **tail** behavior needs tail metrics (p99), not means.
- **State and test the modeling assumptions.** Fit the arrival/service distributions to the real
  workload (QQ-plots, goodness-of-fit); a theorem whose M/G/1 assumption is never checked against
  the target system invites the "unrealistic model" reject.
- **Show analysis-vs-simulation agreement.** Overlay the analytic prediction on simulated
  measurements; if they disagree, the model or the proof is wrong, and it is better to find that
  yourself.
- **Use real workloads/traces,** sampled or selected by a stated criterion, and describe their
  provenance. Toy inputs invite the "does this hold on real systems?" reject.
- **Choose fair baselines,** including the strongest prior policy/algorithm and a
  simple-but-reasonable alternative, tuned with a documented, equal budget. An untuned baseline is a
  scored weakness.
- **Report statistics for stochastic systems:** confidence intervals over independent runs, the
  number of runs and the source of variance, warm-up/steady-state handling for simulations, and
  effect sizes for comparisons. A single run with no interval is not evidence.
- **For learning contributions,** report the guarantee (regret/convergence/sample complexity) and
  validate it empirically; leaderboard numbers alone route to an ML venue.

## Claim-to-evidence design table

| Performance claim | Matching evidence | Reject pattern avoided |
|---|---|---|
| "Our policy bounds the tail" | Proof under stated assumptions + simulation matching the analytic p99 with CIs | "A p99 plot with no analytic comparison" |
| "The model captures the system" | Distribution fit to a real trace + goodness-of-fit | "Assumed M/G/1, never checked against the workload" |
| "We beat the prior policy" | Both tuned with equal budget; effect sizes + CIs on real workloads | "Untuned baseline; toy inputs" |
| "The algorithm has low regret" | Regret bound (proof) + empirical regret curve vs. the bound | "Benchmark score with no guarantee" |
| "Scales to realistic load" | Metrics across realistic arrival rates/sizes with variance reported | "Only light load tested" |

## Validation floor for analytic results

```text
[Proof]       full derivation (appendix within the reviewed pages); every case and assumption stated
[Simulation]  seeded, steady-state-aware; overlay the analytic prediction; report CIs and #runs
[Agreement]   quantify the gap between analysis and simulation; explain any discrepancy
[Robustness]  stress an assumption (heavy tails, estimation error) and bound the degradation
```

## Provenance floor for measurement studies

- Record the trace/data source, the collection window, sanitization/anonymization, and access
  terms; archive the *processed* dataset (or document access), not just the collection script.
- State inclusion/exclusion criteria and the resulting sample, with the filtering script in the
  artifact.
- Report how outliers, gaps, and measurement artifacts were handled — silent inclusion skews every
  downstream metric.

## Vignette: evaluating a scheduling policy

Suppose the paper claims a new policy provably reduces p99 latency versus a size-aware optimal. The
matching plan: prove the bound under stated assumptions; fit the service-time distribution to a real
trace and show the fit; simulate both policies with logged seeds and steady-state handling, overlay
the analytic p99 on the simulated p99 with confidence intervals; run a trace-driven evaluation with
both policies tuned equally, reporting effect sizes; and quantify the degradation under fetch-size
estimation error — every number traceable to a logged run in the artifact.

## Statistical reporting floor

- Confidence intervals and the number of independent runs for every stochastic measurement.
- Steady-state / warm-up handling stated for simulations.
- The compute and workload scale actually used, not vague feasibility language.

## Output format

```text
[Evaluation readiness] strong / adequate / weak
[Claim -> evidence map] <claim: proof? / validation? / measurement? / guarantee?>
[Assumption check] <assumption -> fit to real workload? goodness-of-fit shown?>
[Analysis-vs-measurement] <agreement shown with CIs? discrepancy explained? yes/no>
[Baseline fairness] <baseline -> tuned? equal budget? documented?>
[Decision-critical next run] <one experiment, proof case, or validation to add>
```
