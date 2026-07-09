---
name: issta-reproducibility
description: Use when strengthening ISSTA reproducibility and verifiability evidence, covering pinned subject programs and benchmark versions, random seeds and timeout budgets, non-determinism disclosure for fuzzing and analysis, claim-to-evidence traceability, tool availability statements, and keeping the artifact consistent with the paper's tables.
---

# ISSTA Reproducibility

Use this before submission and again before the artifact deadline. Verifiability and transparency
are named ISSTA evaluation criteria, so reproducibility is scored, not optional. Reopen the current
call and artifact instructions to confirm what the cycle requires.

## Evidence map

- Map each empirical claim — a detection rate, a coverage gain, a bug count, a speedup — to a
  verifiable location: a table, the artifact, or a logged run that a reader could regenerate.
- Pin the substrate: benchmark version (e.g. the Defects4J revision), subject-program commit SHAs,
  the extraction date of any mined corpus, and the exact toolchain versions. "The latest version"
  is not reproducible.
- Fix and report the stochastic knobs: random seeds, timeout budgets, iteration or generation
  counts, and hardware, because a fuzzing or search result at one budget says little about another.
- Disclose non-determinism honestly. Where results vary between runs, report the run count and the
  observed spread rather than a single golden run, and say which tables are means over runs.
- Give an availability statement: what is released, under what license, and where, or an honest
  reason for withholding (proprietary subjects, license terms) with enough detail for in-principle
  reproduction.
- Keep the artifact and the paper in lockstep; a table the artifact cannot regenerate is a
  verifiability failure the criteria will catch.

## Claim-to-evidence audit table

| Claim type | Minimum reproducibility evidence | Common failure caught |
|---|---|---|
| Detection / bug-finding rate | Labelled subjects + ground-truth labels archived | Rate reported against an unshared or hand-picked subject set |
| Coverage or analysis-precision gain | Subject SHAs, tool config, and the measurement script | Baseline run under a different configuration than the tool |
| Fuzzing throughput / bugs found | Seed corpus, time budget, run count, hardware | A single lucky campaign presented as typical |
| Speedup over a baseline | Same machine, same subjects, wall-clock protocol | Speedup measured on incomparable inputs |

Marking a stochastic result as if it were deterministic — no seed, no run count — is a recognizable
ISSTA red flag, because reviewers know these techniques do not produce the same number twice.

## Vignette: a fuzzing evaluation

Consider a paper claiming a new mutation strategy finds more bugs. Its reproducibility spine: the
seed corpus and target binaries pinned by hash; the CPU-time budget per campaign and the number of
repeated campaigns; the deduplication method for counting distinct bugs; a statement of which bugs
are previously known versus new; and a script that turns the raw campaign logs into the paper's
bug-count table — plus one honest sentence about variance across campaigns.

## Degrees of reproducibility

```text
Turnkey     one command regenerates each table from logged runs (aim for the smoke path)
Scripted    scripts exist but need documented manual steps or large external data
Descriptive prose detailed enough that a competent reader could rebuild the pipeline
```

For ISSTA, aim for at least a turnkey smoke path plus scripted full runs; long fuzzing or
symbolic-execution campaigns may stay scripted if the budget and variance are documented. Stating
the achieved level honestly beats promising turnkey behaviour that fails on a clean machine.

## Output format

```text
[Claim inventory] <claim -> evidence location>
[Substrate pinned] benchmark version / subject SHAs / toolchain: yes/no
[Stochastic disclosure] seeds / budgets / run count / variance: complete/partial/missing
[Availability] released / partially released / withheld-with-reason
[Paper fixes] <must appear in the body>
[Artifact fixes] <package or script additions>
```
