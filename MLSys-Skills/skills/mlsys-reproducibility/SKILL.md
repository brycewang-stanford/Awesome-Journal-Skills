---
name: mlsys-reproducibility
description: Use when hardening the reproducibility of MLSys performance claims, pinning the full system layer from driver to interconnect, separating ML randomness from systems noise, choosing repetition counts and variance reporting for throughput and latency numbers, and disclosing hardware, workloads, and cost so strangers can re-measure results.
---

# MLSys Reproducibility

Use this while experiments are still running — reproducibility at this venue is a
measurement-design property, not a packaging afterthought. An MLSys claim is typically
"system A beats system B by X% on workload W on hardware H," and every one of those four
variables can silently drift. The venue's culture (badge-based artifact evaluation, the
MLPerf benchmark lineage published in its own proceedings) means reviewers assume
performance numbers will eventually be re-measured by someone else.

## Two kinds of nondeterminism — control them separately

| Source | Examples | Control |
|---|---|---|
| ML randomness | Init seeds, data order, dropout, sampling temperature | Fix and log seeds; report across-seed variation where accuracy matters |
| Systems noise | Clock boosting/thermal state, co-tenant interference, NUMA/PCIe placement, network jitter, filesystem caches | Warmup phases, repeated trials, exclusive nodes, pinned placement, reporting distributions |

Papers routinely fix seeds meticulously while leaving thermal state and placement
uncontrolled — backwards for a performance paper, where systems noise usually dwarfs
seed effects on latency numbers.

## The environment pin — deeper than requirements.txt

A latency claim depends on layers a Python lockfile never sees. Record all of them:

- Hardware: GPU/accelerator model and count, CPU, memory, interconnect (NVLink/PCIe
  generation, NIC), storage class.
- System: driver version, CUDA/ROCm version, container image digest, kernel version.
- Framework: exact framework build, compilation flags, graph/eager mode, precision
  (FP16/BF16/FP8/INT4), and any autotuning caches — a warm autotuner cache can fake a
  speedup that a fresh machine cannot reproduce.
- Serving stack: batch policy, concurrency limits, admission control settings.

## Measurement harness discipline

```python
import time, statistics

def measure(step, warmup=20, trials=200):
    for _ in range(warmup):          # exclude JIT, autotuning, cache-fill effects
        step()
    xs = []
    for _ in range(trials):
        t0 = time.perf_counter()
        step()                       # synchronize accelerator inside step()
        xs.append(time.perf_counter() - t0)
    xs.sort()
    return {
        "p50": xs[len(xs)//2],
        "p99": xs[int(len(xs)*0.99)],
        "mean": statistics.fmean(xs),
        "stdev": statistics.stdev(xs),
        "trials": trials,
    }
```

- Never report a single run for any latency or throughput number; state trial counts and
  either stdev or percentile spread in every table caption.
- Report tails (p95/p99) for anything serving-shaped; means alone hide the behavior
  systems reviewers care about most.
- Synchronize accelerators before timestamps — async launch makes GPUs look infinitely
  fast in naive harnesses.
- Interleave A/B trials (ABABAB, not AAABBB) so thermal drift and co-tenant noise hit
  both systems equally.
- Keep raw measurement logs; tables should be generated from logs by script, so the
  paper, the artifact, and reality cannot diverge.

## Disclosure floor for the paper itself

- Workload identity: exact models, datasets or traces, sequence-length/request-rate
  distributions, and how the workload was chosen (a named benchmark family beats a
  bespoke workload for credibility — reviewers know the MLPerf-style conventions).
- Baseline versions and their tuning budget, stated symmetrically with your system's.
- Total compute consumed and, where the paper argues cost efficiency, the price basis
  ($/GPU-hour source and date) behind any dollar figures.
- Energy numbers, if claimed, with the measurement method (whole-node meter vs.
  software counters) — the two can disagree wildly.
- What was *not* controlled, honestly: shared cluster, single hardware family, one
  precision mode. A scoped claim survives re-measurement; an unscoped one does not.

## Common measurement bugs this venue catches

Each of these has sunk real performance claims; check for them before a reviewer does.

- **Warm-cache flattery**: benchmarking after the dataset, weights, or autotuner cache
  is hot, while the baseline runs cold. Symmetrize or report both regimes.
- **Async mirage**: timing GPU work without device synchronization, measuring launch
  latency instead of execution.
- **Batch-mismatch comparisons**: your system at its best batch size versus the
  baseline at its default — a tuning-parity violation wearing a measurement disguise.
- **Coordinated omission**: measuring latency only for requests the system accepted,
  while it sheds load; report drop/timeout rates next to every latency figure.
- **Averaging across heterogeneous workloads**: a single mean over workloads of wildly
  different scales lets one workload buy the headline; report per-workload numbers.
- **Power-state contamination**: comparing runs taken at different GPU clock or
  thermal states; record clocks and lock them where the platform allows.

## Pre-submission reproducibility drill

1. Fresh-clone the repo on a machine that has never run the project; follow only the
   README. Every undocumented step found here is a future AE failure.
2. Regenerate the two most important tables from raw logs with one command each.
3. Diff regenerated numbers against the PDF; investigate any discrepancy beyond stated
   variance — this drill catches stale-table bugs that reviewers cannot, but artifact
   evaluators will.
4. Record the wall-clock and dollar cost of the full reproduction; put it in the
   appendix so others can budget.

## Cycle-volatility warning

Whether MLSys requires a reproducibility checklist or statement at submission time is a
per-cycle decision that could not be verified for 2026 (待核实) — check the current CFP
and OpenReview form fields rather than assuming either way. Artifact-evaluation badge
mechanics live in `mlsys-artifact-evaluation`.

## Output format

```text
[Claim under audit] <system-vs-baseline, workload, hardware>
[Environment pin] <hardware/driver/container/framework/precision status>
[Noise controls] <warmup/trials/interleaving/placement/tails reported?>
[Disclosure gaps] <workload provenance/baseline tuning/compute/cost/energy>
[Drill result] <fresh-machine reproduction outcome + cost>
[Fixes] <ordered, cheapest-first>
```
