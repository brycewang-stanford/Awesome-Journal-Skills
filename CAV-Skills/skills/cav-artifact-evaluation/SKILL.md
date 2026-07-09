---
name: cav-artifact-evaluation
description: Use when packaging a CAV (Computer Aided Verification) artifact for the Artifact Evaluation Committee (AEC), covering the three badges (Available / Functional / Reusable), the smoke-test and full-review phases, ≥2 AEC reviewers per artifact, DOI-issuing archives, verification-tool packaging (solvers, benchmarks, seeds, resource limits, proof witnesses), and the fact that AE is invited, post-notification, and non-conditional.
---

# CAV Artifact Evaluation

Use this for the artifact track. CAV artifact evaluation is run by a dedicated **Artifact Evaluation
Committee (AEC)**, is **invited but optional** after notification, and — importantly — **final paper
acceptance is not conditional** on it. Authors declare **artifact intent at submission time**; the
actual AEC submission comes after acceptance, on the artifact track's own deadline (CAV 2026 artifact
registration: 22 Apr 2026). Two things to internalize: badges are earned by AEC members actually
running your package, and for anonymized paper categories the review-time material and the AEC
artifact are handled differently (the AEC artifact is post-notification, so de-anonymization is fine).

## The three badges (verify the current set and names)

| Badge | What it certifies | What earns it |
|---|---|---|
| Available | The artifact is permanently, publicly retrievable | Deposit in a **DOI-issuing archival repository** (Zenodo, figshare, Software Heritage) |
| Functional | The artifact is documented, consistent, complete, and exercisable | A clean-machine install, a working run, and documented expected outputs |
| Reusable | Quality significantly exceeds Functional; others can build on it | Functional **plus** a reuse license, clear structure, and easy-to-adapt docs; requires Available |

Available is a low-cost, high-value badge (archive the package with a DOI). Functional and Reusable
require the AEC's own run to succeed, so the failure mode is almost always "it did not build/run on
their machine," not "the idea was weak." Reusable additionally requires that the artifact already be
Available.

## How the AEC evaluates (two phases, ≥2 reviewers)

Each artifact is examined by **at least two** AEC members across two phases:

```text
[Smoke-test phase]  reviewers confirm the artifact downloads, unpacks, and the basic entry point
                    runs on a clean environment. Fix any friction here and you can still respond.
[Full-review phase] reviewers work through the claims: run the tool on the benchmarks, check the
                    documented outputs, and assess reusability for the Reusable badge.
```

Design so the **smoke test succeeds in the first ten minutes** on a fresh machine — a VM image or a
container removes most smoke-test failures.

## What AEC reviewers open first (verification-specific)

| Claim type | First thing inspected | Common failure caught |
|---|---|---|
| A solver / model checker / prover | Build/install + one benchmark run | Undocumented dependencies; only-builds-on-authors'-machine |
| A benchmark comparison | The scripts that reproduce the paper's table | Numbers in the PDF no script regenerates; unpinned benchmark set |
| A soundness claim | The witness/certificate + an independent checker | "Verified" verdict with no checkable proof |
| A randomized/portfolio tool | Seeds, resource limits, and core counts | Non-deterministic results with no fixed seed or stated limits |

## Packaging plan for a verification artifact

```text
[Container]    ship a Docker image or a VM (many CAV artifacts use a provided VM) with the tool
               pre-built; avoid "compile these dependencies by hand"
[README]       one-screen orientation: what it is, install, a smoke-test command, how to reproduce
               each table, expected runtime and outputs, and the hardware you used
[Benchmarks]   the exact benchmark set and revision (SV-COMP/SMT-COMP/HWMCC/VNN-COMP subset), or a
               documented fetch; state the subset and why
[Config]       resource limits (time/memory), core count, seeds for any randomized component
[Witnesses]    proof certificates / unsat proofs / verification witnesses + an independent checker
               where the claim is correctness
[Mapping]      an explicit table: paper claim -> script/command -> expected result
[License]      an OSI-approved license so the artifact can be badged Reusable
[Archive]      deposit in a DOI-issuing repository for the Available badge
```

## Worked vignette: packaging an SMT-solver + benchmark study

A Regular Paper contributes a solving technique and a benchmark comparison. To target Reusable and
Available: ship a Docker image with the solver pre-built; a `smoke.sh` that solves one bundled
instance in under a minute; a `reproduce/` directory whose scripts rerun the benchmark division under
the paper's exact time/memory limits and regenerate each table; the pinned benchmark-set revision (or
a fetch script); logged seeds for the portfolio; DRAT/unsat proofs with a bundled checker for the
UNSAT claims; a claim-to-command mapping in the README; and an Apache/MIT license. State honestly
which results are turnkey and which need the full (multi-day) benchmark run, and archive the whole
package on Zenodo for a DOI.

## Calibration

- Artifact evaluation is **after** notification and **not** a condition of acceptance — plan it, but
  do not block the camera-ready on the badge outcome.
- Badge names, the exact set offered, the phase structure, and whether the AEC is single- or
  double-anonymous vary by cycle — confirm on the current Artifact Evaluation page.

## Output format

```text
[Target badges] Available / Functional / Reusable
[Phase readiness] smoke test passes in <10 min on a clean machine? yes/no
[Contents] <tool/benchmarks(revision)/config(limits,seeds)/witnesses/license>
[Claim mapping] <claim -> command -> expected result present? yes/no>
[Archive] DOI-issuing repository chosen? yes/no
[Fixes before submission] <ordered list>
```
