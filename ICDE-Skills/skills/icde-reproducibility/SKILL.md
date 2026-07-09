---
name: icde-reproducibility
description: Use when strengthening reproducibility evidence for an IEEE ICDE data-engineering paper: pinning hardware, storage devices, software versions, datasets and workload generators, seeds, and variance protocol; ensuring baseline-tuning fairness; tracing figures to raw logs; and packaging supplemental material whose availability ICDE scores.
---

# ICDE Reproducibility

Use this before submission and again before camera-ready. ICDE authors are expected to submit
supplemental material, and its availability is weighed in the evaluation — so reproducibility
is not optional polish, it is scored evidence.

## Evidence map

- Map each performance claim to a **verifiable location**: a figure regenerated from logged
  runs, a workload script, or a documented measurement in the supplement.
- **Pin the environment**: CPU, memory, storage device (the NVMe/SSD/HDD distinction changes
  results), OS and kernel, database/library versions, compiler flags, and any cluster topology.
- **Pin the data**: dataset provenance, construction steps, scale factors, and for synthetic
  data the **generator with its seeds** — a workload nobody can regenerate is not reproducible.
- **Pin the variance protocol**: how many runs, warm-up handling, how outliers are treated, and
  whether reported bars are standard deviations, confidence intervals, or percentiles.
- **Document baseline tuning**: the configuration and tuning budget given to each competitor.
  Reproducibility here means a reader can re-run the *fair* comparison, not just your system.
- **Trace figures to raw data**: emit tables and plots from logged results so the PDF numbers
  and the supplement cannot drift apart.

## Systems-reproducibility audit table

| Dimension | Weak answer | ICDE-ready answer |
|---|---|---|
| Hardware | "a modern server" | Exact CPU, RAM, storage device model, and topology |
| Data | "a large dataset" | Named dataset or a seeded generator with scale factors |
| Variance | one median number | N runs with declared spread and warm-up policy |
| Baselines | "we compared to X" | X's config and tuning budget, re-runnable |
| Figures | hand-entered numbers | Plots emitted from logged runs by a script |

## Degrees of reproducibility

- **Turnkey:** `run_all.sh` regenerates every figure from logged seeds on a documented machine;
  `run_small.sh` gives a fast subset for a reviewer with limited hardware.
- **Scripted:** scripts exist but need documented manual steps or restricted-data access.
- **Descriptive:** prose detailed enough that a competent engineer could rebuild the pipeline.

For ICDE, aim for **turnkey on the synthetic experiments** — a reviewer will re-run a generator
far sooner than they will provision a cluster — and **scripted** for large real-data or
proprietary-hardware runs, with deviations documented. State the level you actually achieved;
overpromising turnkey behavior that fails on a clean machine is worse than an honest "scripted."

## Vignette: a throughput-plus-latency paper

A submission claims higher ingestion at bounded read-latency cost. Its reproducibility spine:
the storage device and queue-depth settings, the workload generator with append-to-scan
parameters and seeds, the run count and percentile policy for the latency tails, the baseline
LSM's compaction configuration, and a `run_small.sh` that reproduces the headline crossover on
a single machine in minutes — plus one honest sentence on any result that needs the full
cluster.

## Single-blind note

- ICDE supplemental material need **not** be anonymized — names may stay on the repository and
  in commit history. Spend the saved effort on making the package actually run, not on scrubbing
  identity a double-blind venue would demand.

## Output format

```text
[Claim inventory] <claim -> evidence location>
[Environment pinned] complete / partial / missing <what>
[Variance protocol] <runs / spread type / warm-up>
[Baseline fairness] <tuning budgets documented? y/n>
[Reproduction level] turnkey / scripted / descriptive
[Fixes before submission] <ordered list>
```
