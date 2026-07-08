---
name: vldb-reproducibility
description: Use when engineering reproducibility into a VLDB paper before submission, covering hardware and configuration disclosure, dataset and workload provenance, run-to-run variance in systems measurements, competitor-version pinning, figure-to-raw-data traceability, and the disclosure floor PVLDB reviewers apply to performance claims.
---

# VLDB Reproducibility

Use this while experiments are still running — reproducibility at a systems
venue is an experimental-design property, not a packaging step. The question a
PVLDB reviewer silently asks of every performance figure: *could a competent
lab, given this paper alone, land within noise of these curves?*

## The disclosure floor

Every performance claim needs its context recoverable from the paper (or its
cited artifact):

- **Hardware**: CPU model and count, memory, storage class and interface,
  network fabric, node count. "A commodity server" reproduces nothing.
- **Software**: OS, kernel where it matters (I/O experiments), compiler and
  flags, and the exact versions *and configurations* of every system measured
  — including yours.
- **Data**: source, size, skew characteristics; for generated data, the
  generator, its parameters, and its seed.
- **Workload**: query mix, arrival pattern, client counts, warm-up protocol,
  and run duration.
- **Measurement**: what was timed, from where, and what was excluded.

## Variance is a systems problem, not a seed problem

ML papers randomize over seeds; systems papers fight nondeterminism from
caches, compaction timing, JIT warm-up, thermal throttling, and noisy
neighbors. The floor:

| Practice | Rule of thumb |
|---|---|
| Repetitions | ≥3-5 runs per point; state the count |
| Reported statistic | Median or mean — say which; show spread when curves are close |
| Cache state | Declare warm or cold, and how you got there |
| Cloud runs | Same instance placement across systems; note the epoch |
| Background work | Disable or document (compaction, checkpoints, GC) |

A speedup smaller than the run-to-run spread is not a result; either tighten
the measurement or drop the claim.

## Competitor fairness ledger

Reviewers here often built the systems you compare against. For each baseline
record: version or commit, configuration changes from defaults, tuning effort
spent, and any feature disabled — then disclose that ledger in the paper.
An untuned competitor found by its author on the program committee is a
one-review rejection.

## Traceability from figure to raw data

```text
paper figure N
  <- plots/make_fig_N.py
  <- results/expN/*.csv        (raw, one file per run)
  <- run.sh expN --config configs/expN.yaml
  <- git tag paper-vN + Dockerfile digest
```

Build this chain during the project, not after acceptance. It is what makes
the revision window survivable — a reviewer-requested variation becomes a
config edit instead of archaeology — and it is exactly what the pVLDB
Reproducibility Committee will walk if you enter the evaluation.

## The repro-honesty paragraph

State in the paper what is *not* reproducible and why: proprietary traces,
production-only scale, licensed competitors. PVLDB's culture (availability
badges, mandatory EA&B evaluation) rewards declared limits and punishes
discovered ones. One honest paragraph outperforms a broken promise of full
reproducibility.

## Output format

```text
[Disclosure floor] met / gaps (hardware/software/data/workload/measurement)
[Variance handling] reps, statistic, spread shown — weak points
[Competitor ledger] complete / untuned or unpinned baselines listed
[Trace chain] figure->script->raw->tag intact / broken links
[Declared limits] <what is stated as non-reproducible and why>
[Highest-risk claim] <claim whose evidence would not survive a rerun>
```
