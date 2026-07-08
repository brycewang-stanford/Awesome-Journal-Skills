---
name: mlsys-experiments
description: Use when designing or auditing the evaluation of an MLSys paper, selecting representative workloads and hardware, tuning baselines symmetrically, reporting throughput, latency tails, memory, cost, and quality together, structuring ablations that attribute gains to mechanisms, and building scaling and sensitivity evidence reviewers trust.
---

# MLSys Experiments

Use this before the evaluation is frozen. An MLSys evaluation exists to answer one
compound question: *does the named mechanism deliver the claimed system-level payoff on
workloads that matter, at acceptable cost, for understood reasons?* Each clause needs its
own evidence, and this venue — which published the MLPerf Training methodology in its own
proceedings — holds measurement to benchmark-committee standards.

## Workload selection: the make-or-break choice

"Unrepresentative workload" is the modal fatal objection at this venue. Defend the
choice explicitly:

- Anchor on recognizable workloads: MLPerf-family tasks, widely used open models, or
  published request traces. Bespoke workloads need a characterization section showing
  their statistics (request rates, sequence lengths, arrival burstiness, model mix).
- Cover the axis your mechanism exploits: a scheduler for bursty load must be tested on
  bursty *and* uniform load; the uniform case bounds your claim, it does not weaken it.
- Include at least one workload where you expect little or no gain, and show it. A
  non-win row is the cheapest credibility purchase available.
- State workload licensing/provenance — traces you cannot release constrain your future
  artifact badges (see `mlsys-artifact-evaluation`).

## Baseline discipline

- Compare against the current strongest systems, version-pinned, in their recommended
  configurations — and tune them with the **same budget** you gave your own system.
  Document both budgets; asymmetric tuning is treated as invalidating.
- Include the "do nothing" configuration where meaningful (e.g., default framework
  behavior); reviewers use it to sanity-check absolute numbers.
- If a relevant baseline cannot run in your setting, demonstrate the incompatibility
  rather than asserting it.

## The reporting quartet

Never report throughput alone. Each headline claim carries four coordinates:

| Coordinate | Report as | Classic gaming pattern it prevents |
|---|---|---|
| Throughput/goodput | Under a stated latency constraint | Batch-size inflation that destroys tails |
| Latency | p50 and p99 (p99.9 for serving), distributions not means | Mean-only tables hiding stragglers |
| Memory | Peak device + host, at the measured configuration | Wins that only fit on 80GB parts, unstated |
| Cost/efficiency | $ or joules per unit work, with price/meter basis | "Faster" systems that are 4x more expensive |

Quality (accuracy/perplexity or task metric) rides along whenever the technique could
plausibly change model output — quantization, sparsity, scheduling with dropping,
approximation of any kind. "No quality change" is a claim requiring a measurement.

## Ablation = attribution

Systems papers stack techniques; reviews ask which component pays.

- One ablation row per named mechanism, cumulative or leave-one-out — pick one scheme
  and say which.
- Ablate the *insight*, not only the code: if the claim is "lookahead scheduling wins,"
  include the no-lookahead scheduler, not just the whole-system-off row.
- Sensitivity sweeps over the parameters a deployer must set (window sizes, thresholds);
  a mechanism needing per-workload hand-tuning must say so.

## Scaling and sensitivity evidence

```yaml
# experiment-matrix.yaml — one row per plotted point, generated, never hand-edited
sweep:
  models:    [llama-class-8b, llama-class-70b, moe-16e]
  hardware:  [1xA100, 8xA100-nvlink]        # state interconnect explicitly
  load:      [uniform-qps, bursty-trace-A]
  precision: [bf16, int4]
  trials: 5
  warmup_steps: 20
  metrics: [goodput@p99<250ms, p50, p99, peak_mem_gb, gpu_hours, quality]
  seeds: [1, 2, 3, 4, 5]
```

- Plot trends, not points: gain versus model size, versus load, versus GPU count. A
  single-configuration win invites the "will this survive scale?" objection you cannot
  answer in the four-day response window.
- Log everything; regenerate every figure from logs by script (measurement mechanics
  and variance rules live in `mlsys-reproducibility`).

## Statistical floor for systems numbers

Systems papers rarely need hypothesis-testing machinery, but they always need variance
honesty; the floor this venue's reviewers apply:

- Five or more trials for any number in a comparison table; report spread (stdev or
  IQR) and say which in the caption.
- Overlapping spreads mean the difference is not a finding — either run more trials or
  report the tie honestly; a "win" inside noise is worse than a reported tie because
  one reviewer rerun destroys it.
- For latency distributions, trials are not enough: within-run percentiles need enough
  requests that p99 is estimated from hundreds of samples, not three.
- Seed variation matters only where model quality enters the claim; systems noise
  (placement, thermal state, co-tenants) dominates latency variance and is controlled
  by measurement design, not seeds — the split is detailed in `mlsys-reproducibility`.

## Evaluation-design review before running

Run this table exercise before burning GPU-hours: for each claim in the abstract, write
the figure that will support it, the workload it needs, and the strongest objection a
systems reviewer could raise — then check the matrix covers that objection. Claims
without a planned figure get cut from the abstract, not padded later.

## Common reject patterns to design against

- Microbenchmark gains that never appear end-to-end; always include the end-to-end run.
- Gains measured only at one scale/hardware and claimed generally.
- Quality silently degraded by the optimization, discovered by a reviewer from your own
  appendix table.
- Cost omitted where the honest accounting would erase the win.

## Output format

```text
[Evaluation readiness] strong / adequate / weak
[Workload defense] <named anchors + characterization + non-win case present?>
[Baseline symmetry] <versions pinned, tuning budgets equal + documented?>
[Quartet coverage] <throughput/latency-tails/memory/cost per headline claim>
[Attribution] <mechanism -> ablation row>
[Decision-critical missing run] <one experiment>
```
