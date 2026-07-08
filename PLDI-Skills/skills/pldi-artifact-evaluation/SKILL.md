---
name: pldi-artifact-evaluation
description: Use when packaging a PLDI artifact for the post-acceptance evaluation — earning the Functional, Reusable, and Available badges, archiving a DOI-stamped snapshot on Zenodo, containerizing toolchains and benchmark suites, and writing a README an evaluator can follow in a fresh VM.
---

# PLDI Artifact Evaluation

PLDI runs artifact evaluation **after** paper acceptance, deliberately separating
paper review from artifact review, and it accepts "any artifact authors wish to
submit, broadly defined" — compilers, proofs, benchmark suites, measurement
infrastructure (PLDI 2026 research-artifacts track, read 2026-07-08; AE co-chairs
for 2026 were Raphaël Monat and Qirun Zhang). Badges appear on the published
PACMPL article, so the artifact is part of the paper's permanent record.

## The badge ladder

| Badge | 2026-cycle criterion | What actually earns it |
|---|---|---|
| Functional | Artifact supports the paper's claims and works as documented | An evaluator reproduces your headline flow from the README alone |
| Reusable | Only awarded to Functional artifacts judged especially well packaged, documented, and designed for future research | Extension points documented; someone could swap in a new benchmark or pass |
| Available | Automatic once the complete artifact is archived publicly in an archival location | A Zenodo snapshot with a DOI — a lab GitHub link does not qualify |

Two structural kindnesses in the 2026 rules: artifacts are requested only after
acceptance, and there is **no artifact camera-ready deadline** because Zenodo
accepts new versions at any time. Use that slack for polish, not procrastination —
the evaluation itself still runs on the AE committee's timetable.

## Package for a hostile machine

Your evaluator has a laptop, a deadline, and no institutional access to your
cluster. Design for that:

```text
artifact/
  README.md            # claims covered, est. runtimes, kick-the-tires steps
  LICENSE
  Dockerfile           # pinned base image, pinned compiler versions
  claims.md            # paper claim -> script -> expected output, one row each
  scripts/
    smoke.sh           # <10 min: builds, runs one benchmark, checks one number
    reproduce_all.sh   # full run with per-experiment time estimates
  benchmarks/          # provenance + versions of every program measured
  results/expected/    # our outputs, for diffing
```

Rules of thumb that decide badges:

- **A ten-minute smoke test is the highest-leverage file in the archive.** Most
  negative AE experiences begin with a build that fails in minute one.
- **Pin everything**: compiler versions, benchmark-suite revisions, flags. "Latest
  LLVM" is a different artifact every month.
- **Map claims to scripts explicitly.** Evaluators check the paper's tables
  against your outputs; make the correspondence a table, not a scavenger hunt.
- **State hardware sensitivity honestly.** If speedups need AVX-512 or 64 GB of
  RAM, say so up front and provide a reduced-scale mode that still shows the
  trend.
- **For proof artifacts**, pin the proof assistant version and make `make check`
  verify the exact theorem names cited in the paper.

## Cross-check with the paper

The evaluation protocol inside the artifact must match what
`pldi-experiments` put in the paper: same warmup discipline, same repetition
counts, same statistics. An artifact that reruns 3 iterations when the paper
reports 30-run confidence intervals invites exactly the doubt AE exists to
dispel.

## 待核实 each cycle

Kick-the-tires/rebuttal phases, badge wording, submission format (VM vs
container), and the AE timetable are reset per edition — reread the current
research-artifacts track page before packaging.

## Output format

```text
[Badge target] Available / +Functional / +Reusable
[Smoke test] exists? runtime? passes in a fresh container?
[Claim map] paper table/claim -> script -> expected output (n rows)
[Pinning] compilers / benchmarks / base image / proof assistant
[Archive] Zenodo DOI minted? version matches camera-ready?
```
