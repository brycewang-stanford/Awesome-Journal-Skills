---
name: atc-reproducibility
description: Use when building the reproducibility story for an ATC (ACM SIGOPS Annual Technical Conference, formerly USENIX ATC) systems paper — pinning testbed and software environments, providing a turnkey path from the artifact to the headline numbers, and preparing an anonymized-but-runnable review package ahead of the Available/Functional/Reproduced badges.
---

# ATC Reproducibility

Build the reproducibility story alongside the system, not at the deadline. ATC has an active
artifact culture inherited from USENIX: reviewers expect a runnable, anonymized artifact at review
time, and after acceptance an Artifact Evaluation Committee awards **Available / Functional /
Reproduced** badges (see `atc-artifact-evaluation`). The through-line is that a systems result other
people can re-run is worth more than one they must take on faith — and systems provenance cannot be
reconstructed after the fact.

## Pin what you cannot reconstruct

Record these **at collection time**; none can be recovered at the deadline:

```text
[Hardware]   CPU/NIC/SSD models, core/memory counts, firmware/BIOS where it matters
[OS/kernel]  kernel version, distro, relevant sysctl/tuning, hugepages/NUMA settings
[Toolchain]  compiler, library, and runtime versions; build flags
[Workload]   trace source + extraction date, generator version + seeds, request mix
[Method]     warm-up window, measurement duration, run count, aggregation method
[Code]       commit SHAs for your system and every baseline; patches applied
```

## A turnkey path to the headline numbers

The single most valuable artifact property is that an evaluator can regenerate your paper's main
figures and tables:

- Ship a **claim-to-experiment map**: paper claim → script → expected figure/table → expected
  runtime.
- Provide a **one-command** entry point per headline result (`./run_fig3.sh`) that does setup, run,
  and plot.
- Give a **small-scale mode** for evaluators who lack your hardware (fewer nodes, a trace sample),
  and state clearly which results are full-scale-only and why.
- Log **expected outputs and tolerances** so an evaluator knows what "reproduced" looks like given
  measurement noise.

## Pinned, portable environments

- Prefer a **container (Dockerfile) or a pinned environment** (lockfile, `requirements`, Nix) over
  "install these 30 packages by hand."
- Where the result depends on kernel features or hardware (RDMA, SPDK, io_uring, specific NICs), say
  so explicitly and document the required host, since a container cannot abstract the hardware away.
- Include **traces/datasets** (or documented, durable access), not just the query that produced
  them.

## Anonymized-but-runnable review package

At submission the artifact must be **runnable yet double-blind**:

- No owner strings, cluster hostnames, lab or product names, or identity-revealing URLs in code,
  configs, logs, or commit metadata.
- Mirror any linked repository behind an **anonymizing service**; scrub `.git/` from archives.
- The system's own **name** can de-anonymize you — use a neutral placeholder if the real name is
  identifying, and reconcile it in the camera-ready.
- Verify the package runs from a **clean checkout** on a fresh machine — "works on the author's
  laptop" is the most common Functional failure.

## Honest reproducibility posture

- If a result cannot be shared (proprietary trace, confidential deployment), say so and why, and
  provide the closest reproducible substitute — silence reads as a weakness.
- Distinguish **reproducible** (same artifact, same numbers) from **replicable** (independent
  reimplementation) and claim only what you support.
- For experience/deployed-systems papers, provide what you can — configs, anonymized traces,
  analysis scripts — even when the production system itself cannot ship.

## Output format

```text
[Provenance] hardware/OS/toolchain/workload/method/code pinned at collection time? gaps?
[Turnkey] claim-to-experiment map + one-command runs + small-scale mode present? yes/no
[Environment] container or pinned lockfile? hardware dependencies documented?
[Anonymity] artifact runnable AND double-blind (no names/hosts/owner strings)? yes/no
[Clean-machine] runs from a fresh checkout on a clean host? yes/no
[Badge readiness] on track for Available / Functional / Reproduced? blockers?
```
