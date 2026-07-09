---
name: edbt-artifact-evaluation
description: Use when preparing an EDBT database-systems artifact and reproducibility package, covering what evaluators check first for systems papers, a turnkey run path, pinned workloads and environments, DOI-issuing archival for the open-access OpenProceedings record, and the higher stakes for Experiments & Analysis papers.
---

# EDBT Artifact Evaluation

Use this for the artifact and reproducibility package. EDBT's community values re-runnable
database-systems work, and the published record is **open access on OpenProceedings**, so a clean,
archived package strengthens the paper and its permanent citation. Two things to internalize: an
artifact is judged by an evaluator actually *running* it, and the review-time package (possibly
anonymized) is not the same deliverable as the permanent, DOI-archived package cited at
camera-ready.

> **待核实:** whether the current EDBT cycle runs a formal artifact-evaluation track, offers a
> reproducibility badge, and makes it optional or required is decided per edition — confirm on the
> current host-site call. The engineering below applies regardless of whether a badge is on offer.

## What evaluators open first (database-systems flavor)

| Claim type | First thing inspected | Common failure caught |
|---|---|---|
| A system / operator | The build + one run command | Undocumented deps; only-builds-on-authors'-cluster |
| A scalability result | The harness that sweeps sizes/nodes | Numbers with no script; hard-coded to one cluster |
| An Experiments & Analysis study | The comparison harness that regenerates every table | Only the authors' system tuned; missing configs |
| A data/workload contribution | The derivation scripts + the derived data | Description shipped, data missing; provenance unpinned |

Assume an evaluator gives your package a bounded time budget on a machine that is not yours. Design
for the first ten minutes — a clean build and a small demo run — to succeed.

## Packaging plan

```text
[Container]   ship a Dockerfile or a pinned environment (build recipe / lockfile); avoid
              "install these 40 things and configure the cluster by hand"
[README]      one-screen orientation: what it is, how to build, how to run a demo, how to reproduce
              each result, expected runtime and outputs, and what needs a big cluster
[Mapping]     an explicit table: paper claim -> script -> expected result (table/figure)
[Workloads]   the derived workload/query-log itself (or a documented access path), with pinned
              dataset versions, not just a query
[Environment] the hardware/cluster spec assumed, and a reduced-scale path a reviewer can actually run
[License]     an OSI-approved code license and clear data terms, compatible with the CC-BY-NC-ND record
[Archive]     deposit in a DOI-issuing repository (Zenodo, figshare, Software Heritage) for the
              permanent, citable record
```

## Review-time package vs. permanent package

- **At submission:** if the cycle is double-blind (**待核实** per cycle), the package must be
  anonymized — no owner strings, cluster names, lab paths, or identity-revealing links; if
  single-blind, still scrub stale paths and credentials.
- **After acceptance:** deposit the de-anonymized, licensed package in a DOI-issuing archive; this is
  the version the camera-ready cites and the permanent open-access record points to.

## Worked vignette: packaging an operator + evaluation

A paper contributes a query-processing operator and a cluster evaluation. To make it re-runnable:
ship a container with the engine and operator pre-built; a `run_demo.sh` that runs the operator on a
small bundled workload in under a minute; a `reproduce/` directory whose scripts regenerate each
table from logged results and, where feasible, from a fresh reduced-scale run; a claim-to-script
mapping in the README; the derived workloads with pinned dataset versions; and an Apache/MIT license.
State honestly which results are turnkey at small scale and which need the full cluster.

## Calibration

- The full-cluster experiments may not be turnkey on an evaluator's machine — provide a reduced-scale
  path and say clearly what it does and does not reproduce.
- For an **Experiments & Analysis** paper the artifact stakes are highest: the whole comparison
  should regenerate, with every system's configuration documented, because the study *is* the
  contribution.
- Confirm the current cycle's artifact/reproducibility process, any badge, and its anonymity rules on
  the host-site call (**待核实**).

## Output format

```text
[Package role] review-time (anonymized?) / permanent DOI-archived
[Contents] <system/build / workloads / harness / provenance / license>
[Ten-minute test] does build + demo succeed on a clean machine? yes/no
[Claim mapping] <claim -> script -> expected result present? yes/no>
[Scale honesty] <what is turnkey small-scale vs. needs a cluster>
[Archive] DOI-issuing repository + compatible license? yes/no
[Fixes before upload] <ordered list>
```
