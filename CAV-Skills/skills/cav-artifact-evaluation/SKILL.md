---
name: cav-artifact-evaluation
description: Use when packaging a CAV (Computer Aided Verification) artifact for the Artifact Evaluation Committee (AEC), covering the three badges (Available / Functional / Reusable), the two AE rounds (mandatory, pre-notification for Tool Papers; invited, post-notification and non-conditional for other categories), the smoke-test and full-review phases, the obligatory reviewer nomination, DOI-issuing archives, and verification-tool packaging (solvers, benchmarks, seeds, resource limits, proof witnesses).
---

# CAV Artifact Evaluation

Use this for the artifact track. CAV artifact evaluation is run by a dedicated **Artifact Evaluation
Committee (AEC)**, and since **CAV 2027** it runs in **two rounds** (verified 2026-11-24 on
`https://conferences.i-cav.org/2027/artifacts/`):

- **Round 1 — Tool Papers, mandatory.** The artifact is reviewed in parallel with the paper and must
  earn **at least the Functional badge**; a tool paper is accepted only if it passes both the paper
  review and AE. CAV 2027: registration 8 Mar 2027, submission 11 Mar 2027, smoke-test response
  22-25 Mar 2027, artifact and paper notification 23 Apr 2027. An exemption must be requested at
  paper submission, with reasons; it is at the PC and AE chairs' discretion.
- **Round 2 — all other categories, invited and non-conditional.** After notification; CAV 2027:
  registration 26 Apr 2027, submission 3 May 2027, smoke-test response 11-14 May 2027, artifact
  notification 28 May 2027.

Authors declare **artifact intent at submission time** and it is shared with reviewers. AE is
**single-blind**, so the artifact may carry your identity — but to preserve *reviewer* anonymity
you confirm you cannot track who downloads the artifact URL. Every artifact submission must
**nominate one distinct reviewer** (preferably a co-author, expected load about three artifacts),
and you may optionally consent to reviewers using an LLM during the smoke test only. Badges are
earned by AEC members actually running your package.

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

## How the AEC evaluates (two phases per round)

Each artifact is examined by AEC members across two phases (CAV 2026 stated at least two reviewers
per artifact; the CAV 2027 page does not state a number):

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

- For Regular and Application/Industrial/Case Study papers, artifact evaluation is **after**
  notification and **not** a condition of acceptance — plan it, but do not block the camera-ready
  on the badge outcome. For **Tool Papers** it **is** a condition of acceptance and happens before
  notification: start packaging before the paper deadline.
- Accepted artifact formats (CAV 2027): a Docker image (not just a Dockerfile), a VirtualBox `.ova`
  VM image, or a package for the CAV 2027 AE VM; the `.zip` must contain a README and a LICENSE.
- Badge names, the exact set offered, the round structure, and whether the AEC is single- or
  double-anonymous vary by cycle — CAV changed the tool-paper rule between 2026 and 2027; confirm on
  the current Artifact Evaluation page.

## Output format

```text
[Round] 1 (Tool Paper, mandatory, >= Functional) / 2 (other categories, optional)
[Target badges] Available / Functional / Reusable
[Nominated reviewer] <name, affiliation, aware of nomination? yes/no>
[Phase readiness] smoke test passes in <10 min on a clean machine? yes/no
[Contents] <tool/benchmarks(revision)/config(limits,seeds)/witnesses/license>
[Claim mapping] <claim -> command -> expected result present? yes/no>
[Archive] DOI-issuing repository chosen? yes/no
[Fixes before submission] <ordered list>
```
