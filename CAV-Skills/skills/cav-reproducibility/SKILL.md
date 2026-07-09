---
name: cav-reproducibility
description: Use when strengthening CAV (Computer Aided Verification) reproducibility, covering benchmark provenance (SV-COMP/SMT-COMP/HWMCC/VNN-COMP set revisions), pinned tool and baseline versions, resource limits and hardware, seeds for randomized/portfolio solvers, checkable proof witnesses/certificates for soundness claims, and consistency between the paper's tables and the artifact.
---

# CAV Reproducibility

Use this before submission and again before camera-ready. In computer-aided verification,
reproducibility is not a courtesy — a benchmark result is only meaningful relative to a **fixed
benchmark set, pinned tool versions, and a stated resource budget**, and a soundness claim is only
credible if it ships a **checkable witness**. The goal is that a competent reader could rerun your
evaluation and re-check your correctness claims and reach your conclusions.

## Evidence map

- Map each theorem, technique claim, and reported benchmark number to a **verifiable location** — a
  proof (body or appendix), a script in the artifact, or a table regenerated from logged runs.
- For techniques, give enough of the algorithm, parameters, and encoding that a reader could
  re-implement or rerun it.
- For benchmark evaluations, report the exact **benchmark set and revision**, the **baseline tools
  and versions**, the **resource limits** (per-instance time and memory), the **hardware and core
  count**, and the **number of runs**.
- For soundness claims, emit a **certificate/witness** (unsat proof, DRAT, an SV-COMP-style
  witness, an Isabelle/Coq script) and an independent checker — a bare "verified" verdict is not
  reproducible evidence.
- Keep the paper and the artifact **consistent**: a number in the PDF that no script regenerates is
  the contradiction reviewers read as carelessness.

## The reproducibility failure modes CAV reviewers know

| Claim in the paper | Weak answer | CAV-ready answer |
|---|---|---|
| "Faster than solver X" | "X was slower in our tests" | X vA.B, its documented config, same time/memory limit, same hardware; per-instance data in the artifact |
| "Solves N hard instances" | "on standard benchmarks" | The named division of set <revision R>, the exact instance list, the fetch/pin in the artifact |
| "Our result is sound/UNSAT" | asserted | The unsat proof + a bundled independent checker that accepts it |
| "Randomized search finds it" | one lucky run | Fixed seed(s), number of runs, variance reported |
| "Scales to large designs" | "large" | The size metric and the largest instance run, with the timeout that bounds it |

## Provenance and configuration pinning

```text
[Benchmarks] pin the set + revision (SV-COMP/SMT-COMP/HWMCC/VNN-COMP subset); archive the instance
             list and the fetch script, not just "the standard benchmarks"
[Tools]      record exact versions (yours and every baseline), build flags, and the commit/tag
[Limits]     state per-instance wall-clock and memory limits, core count, and the hardware/CPU
[Randomness] log seeds for portfolio/stochastic components; say what is and is not deterministic
[Witnesses]  ship proof certificates + an independent checker for every soundness/UNSAT claim
[Runs]       state the number of repetitions and how variance/timeouts were handled
```

## Degrees of reproducibility (state the one you achieved)

- **Turnkey:** one documented command reruns a benchmark subset and regenerates a table/figure from
  logged data (and re-checks the witnesses).
- **Scripted:** scripts exist but require documented manual steps, a large external benchmark
  download, or a long (multi-day) full run.
- **Descriptive:** prose detailed enough that a competent reader could rebuild the evaluation.

For CAV, aim turnkey for anything a reviewer might rerun quickly (a solver on a small bundled subset,
a witness check) and scripted-with-clear-instructions for a full multi-day benchmark sweep. Stating
the achieved level honestly beats promising turnkey behavior that fails on a clean machine.

## Vignette: a portfolio-solver evaluation

Consider a paper claiming a portfolio SMT technique is faster and stays sound. Its reproducibility
spine: the solver pinned to a commit with build flags; each baseline pinned to a released version and
its documented configuration; the benchmark division pinned to a revision with an archived instance
list; a uniform per-instance time/memory limit and stated hardware; logged seeds and repetition
count; a differential check against a trusted solver on all verdicts (no disagreements) plus unsat
proofs with a bundled checker; and analysis scripts that turn the logs into the paper's tables — with
one honest sentence about the parts (a proprietary hardware benchmark, say) that cannot be shared and
why.

## Consistency and camera-ready pass

- Before submission: every benchmark number traces to a logged run in the artifact; every soundness
  claim has a checkable witness; the artifact is anonymized for Regular/Application categories.
- Before camera-ready: swap anonymized links for a permanent, DOI-issuing archive, and align the
  artifact with the AEC badges you are pursuing (`cav-artifact-evaluation`).

## Output format

```text
[Claim inventory] <claim -> proof/witness or logged benchmark run>
[Benchmark provenance] set+revision / baseline versions / limits / hardware — pinned? yes/no
[Soundness evidence] witness + independent checker present? yes/no
[Reproducibility level] turnkey / scripted / descriptive, stated honestly
[Paper fixes] <must appear in the PDF>
[Artifact fixes] <additions before upload>
```
