---
name: fast-experiments
description: Use when designing or auditing a USENIX FAST storage evaluation, covering real devices and firmware, device-state control (aging, preconditioning, fill, TRIM), standard workloads and traces (SNIA IOTTA, YCSB, filebench, fio), write amplification, tail latency, endurance and wear, crash-consistency testing, fair baselines, and matching the metric to the shape of each storage claim.
---

# FAST Experiments

Use this before submission when the storage evaluation is not yet locked. FAST reviewers are storage
people; the evaluation is where a good idea is won or lost, and the questions are storage-specific.
The organizing principle is **measure the storage cost you claim to change, on real hardware in a
realistic state** — not a throughput bar on a fresh drive.

## Evaluation audit

- **Match the metric to the storage claim.** A claim about *endurance* needs bytes-written / P/E
  cycles, not throughput; a claim about *responsiveness* needs **tail latency** (p99/p99.9), not the
  mean; a claim about *space* needs measured on-media footprint; a claim about *durability* needs a
  crash-consistency test. The wrong metric is the most common FAST reject.
- **Use real devices, and name them.** Model, capacity, interface (SATA/SAS/NVMe), and — critically
  — **firmware version**, plus host, kernel, and filesystem/mkfs options. Nominally identical drives
  differ part-to-part and across firmware; a result without the device table is not auditable.
- **Control device state.** SSDs must be **preconditioned to steady state** (fresh-out-of-box
  numbers flatter every design); report fill level and TRIM/discard state. For file systems, report
  whether the volume was **aged/fragmented** or empty — aging can dominate the result.
- **Drive with credible workloads and traces.** Standard generators (fio, filebench, YCSB for
  KV/DB) and archived traces (SNIA IOTTA block/object traces, production-derived traces) beat an
  ad-hoc microbenchmark. Ship the job files and replay scripts.
- **Choose fair baselines,** including the strongest prior system and a reasonable default, tuned
  with a documented, equal budget. An untuned or default-config baseline is a scored weakness.
- **Test the invariant your optimization risks.** If a change defers writes, batches, or reorders,
  show crash consistency still holds (record-and-replay / fault injection), not just that it is
  faster.
- **Design threats in, not on:** know before you run which confounds (device variance, thermal
  throttling, cache effects, contamination of a trace) will bite, and instrument to bound them.

## Claim-to-evidence design table

| Storage claim | Matching evidence | Reject pattern avoided |
|---|---|---|
| "Cuts write amplification / extends endurance" | Bytes-written from device counters (SMART/logs) at steady state; projected P/E budget | "Estimated WA on a fresh drive; no device counters" |
| "Lower/steadier latency" | Full latency distribution incl. p99/p99.9 under load | "Reports mean latency only" |
| "Scales to real capacities/workloads" | Real-sized datasets and standard traces on real devices | "Tiny dataset on a simulator" |
| "Preserves crash consistency" | Fault-injection / block-level record-and-replay recovery test | "Claims consistency, never crash-tests it" |
| "Faster than system X" | X tuned with equal, documented budget; same hardware and state | "Default-config or older-hardware baseline" |
| "Reliability finding generalizes" | Population, models, and duration stated; external validity bounded | "One model, one datacenter, claimed universal" |

## Device-state and measurement floor

```text
[Devices]      list model, capacity, interface, firmware; host, kernel, mkfs/mount options
[Steady state] precondition SSDs to steady state; state fill level and TRIM; disclose FOB vs. aged
[Warmup]       discard cold-cache warmup unless the cold path IS the claim; state cache/DRAM sizes
[Repeats]      multiple runs; report variance/CIs; note thermal or throttling effects
[Counters]     read WA, bytes-written, GC activity from device logs where available, not estimates
[Trace replay] replay archived traces with a documented tool; state timing fidelity (open vs. closed loop)
```

## Crash-consistency and durability testing

Durability claims are load-bearing at FAST and are frequently under-tested:

```text
[Model]     state the failure model (power loss, kernel panic, fsync semantics)
[Injection] use block-level record-and-replay or a fault injector to cut writes at many points
[Check]     verify the post-recovery state satisfies the invariant (no torn/lost committed data)
[Coverage]  report how many crash points / orderings were tested, not a single anecdote
```

## Provenance floor for traces and field studies

- Archive the *replayed* trace (or document access) and the replay scripts; a trace named but not
  shipped cannot be reproduced.
- For field/reliability studies, state the population, drive models, technology (SLC/MLC/TLC/QLC),
  duration, and how failures/replacements were defined and counted.
- Report how outliers, warmup, and defective units were handled — silent inclusion or exclusion
  skews every downstream number.

## Vignette: evaluating a compaction change for a KV store

Suppose the paper claims an endurance-aware compaction scheduler cuts bytes written. The matching
plan: run on **named SSDs at steady state** with firmware recorded; drive with **YCSB plus an
archived production trace**; measure **bytes-written from the device's own counters**, not the LSM's
estimate; report **read-latency distributions incl. p99.9** to prove the trade is bounded; compare
against the **tuned** stock compactor with an equal budget; and run a **crash-consistency
record-and-replay** test to confirm deferring compactions did not weaken durability — every number
traceable to a logged run in the artifact.

## Output format

```text
[Evaluation readiness] strong / adequate / weak
[Claim -> metric map] <claim: device/metric/statistic>
[Device reality] <models + firmware + state (steady/aged/fill/TRIM) stated? yes/no>
[Baseline fairness] <baseline -> tuned? equal budget? same hardware/state?>
[Durability check] <crash-consistency / fault-injection test present? yes/no>
[Threats-by-design] <device variance / warmup / trace contamination -> instrumentation>
[Decision-critical next run] <one experiment to add>
```
