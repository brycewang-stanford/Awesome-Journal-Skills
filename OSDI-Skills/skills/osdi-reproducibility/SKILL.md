---
name: osdi-reproducibility
description: Use when building reproducibility into an OSDI systems project — recording hardware, configuration, workload, and measurement provenance while experiments run, keeping paper and artifact from drifting apart, and setting up for the post-acceptance sysartifacts evaluation and open-access scrutiny.
---

# OSDI Reproducibility

Make the numbers survivable. OSDI-specific hooks below (artifact timing, badge scope,
open-access exposure) are 2026-cycle facts verified 2026-07-08; the provenance
discipline is venue-independent engineering.

## Why the bar is high at OSDI specifically

Two venue mechanics raise the stakes beyond generic good practice:

- **USENIX proceedings are open access from day one.** Every reader on the internet —
  including the teams whose systems you outperformed — gets the free PDF immediately
  and can attempt your numbers. Errors get found publicly and fast.
- **Artifact evaluation happens after acceptance** (May 8, 2026, 8:59 pm PDT in the
  '26 cycle), when the experiments are months old. If provenance was not recorded
  while runs happened, the artifact reconstructs a memory, not an experiment.

Reproducibility at OSDI is therefore a *recording* problem during the project, not a
*packaging* problem at the end. Packaging is `osdi-artifact-evaluation`'s job; this
skill makes packaging possible.

## The provenance ledger

Maintain one machine-readable ledger, committed beside the code, updated by the run
scripts themselves — never by hand after the fact:

```yaml
# runs/2025-11-14-recovery-scale/ledger.yaml (written by the harness, per experiment)
experiment: recovery-vs-cluster-size      # maps to RQ in the experiment matrix
commit: 4f2c9e1 (system) / 8a11d02 (harness)
hardware: 64x c6525-25g (CloudLab), 25 GbE, NVMe model+fw recorded per node
os_kernel: Ubuntu 22.04, 5.15.0-91; mitigations=on; governor=performance
baseline_versions: replayfs v2.3.1 (tag), ckptstore rebuilt from paper (SHA)
workload: trace block-2025-w2, reconstruction script + source documented
runs: 10 per point; seeds 1..10; outliers kept, plotted as distribution
raw_output: s3://bucket/runs/2025-11-14/... (checksummed)
figures: fig7 <- plot_recovery.py @ 8a11d02 on raw_output
```

The last line is the anti-drift rule: **every figure in the paper regenerates from
checksummed raw output by a committed script**. If a figure cannot name its script and
input, the number it shows is unverifiable — by the AE committee and by you in June.

## What systems papers must pin down

| Dimension | Must record | Common omission that kills reruns |
|---|---|---|
| Hardware | Node model, NIC, storage device + firmware, topology | The NIC/firmware detail that made the difference |
| Software | Kernel version + relevant knobs, dependency lockfile | Sysctl and IRQ-affinity settings applied by hand |
| Baselines | Exact version/tag, tuning applied, build flags | "Default settings" that were quietly edited |
| Workloads | Trace provenance, generation seed, licensing | The preprocessing script that shaped the trace |
| Measurement | Warmup policy, window, timer source, run counts | Which runs were discarded and why |
| Environment | Cluster sharing, power/turbo state, time of run | Co-located tenants distorting tail latency |

Hardware access is the honest limit of systems reproducibility: a result needing 64
specific machines will not rerun on a laptop. The discipline is *disclosure plus
graceful degradation* — document the full testbed, and provide a scaled-down
configuration that exercises every code path even if it cannot reproduce headline
magnitudes.

## Determinism where it is cheap, honesty where it is not

Distributed systems are not bitwise-reproducible; do not pretend otherwise. Seed what
can be seeded (workload generation, placement decisions, fault-injection schedules),
report distributions over repeated runs for what cannot, and state which class each
reported number belongs to. A paper that says "recovery time varies ±8% run to run;
we report 10-run distributions" pre-empts the reviewer who reruns and gets a
different point value.

## Traces, data, and the licensing wall

Workload provenance is where systems reproducibility most often dies quietly:

- **Production-derived traces** usually cannot be redistributed. Decide the release
  posture *before* the evaluation depends on them: either obtain redistribution
  rights early, or build a documented reconstruction pipeline (statistical profile →
  generator → validation against the original) and treat the generator as part of
  the artifact.
- **Public traces** still need version pinning and checksums — public archives
  reorganize, and "the standard trace" is not an identifier.
- **Sensitive measurements** (multi-tenant clusters, user-facing services) need the
  anonymization step documented as code, because it changes distributions and a
  reproducer must know how.
- Whatever the posture, the paper states it in one honest sentence; discovering an
  unreleasable dataset during artifact evaluation reads far worse than declaring it
  in the submission.

The shared smoke checker in
[`../../resources/code/README.md`](../../resources/code/README.md) catches structural
gaps (missing README/manifest/license) but none of the above — licensing and
provenance are judgment calls only the authors can make.

## Timing against the 2026 cycle

- **During experiments (autumn)** — the ledger above, enforced by the harness.
- **Silent review window (Dec–Mar)** — freeze the testbed image, trace archives, and
  environment; the '26 Call for Artifacts encouraged preparing artifacts while the
  paper was under consideration, and a conditional accept may demand new runs on the
  frozen setup (`osdi-author-response`).
- **After notification (Mar 26)** — packaging sprint to the May 8 artifact deadline;
  in 2026 the badge evaluated was **Artifacts Available**, so permanent archiving is
  the floor — but a ledger-backed artifact is what makes the optional two-page
  Artifact Appendix in the final paper worth writing (`osdi-camera-ready`).

## The handoff test

The standing acceptance test for all of the above: a new group member, given only
the repository and the ledger, regenerates one paper figure on the scaled-down
configuration without asking anyone anything. Run it quarterly and before each
gate (submission, artifact deadline, final paper). Every question they are forced
to ask is a missing ledger entry; every mismatch they hit is drift between paper
and artifact that an AE evaluator — or a public reproducer holding the open-access
PDF — would have found later, with an audience.

## Output format

```text
[Ledger] exists + harness-written? gaps: <dimensions from the table>
[Figure regeneration] all figures script+input traceable? failures: <list>
[Determinism statement] seeded vs distributional numbers classified? yes/no
[Testbed freeze] image/trace archive frozen for the review window? yes/no
[AE readiness] distance from ledger to packageable artifact: <low/med/high>
```
