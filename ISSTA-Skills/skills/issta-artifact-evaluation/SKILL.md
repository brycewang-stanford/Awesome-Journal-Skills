---
name: issta-artifact-evaluation
description: Use when packaging an ISSTA tool, benchmark, and results for the artifact-evaluation track, covering the ACM badges (Artifacts Available via Zenodo, Evaluated Functional and Reusable, Results Reproduced), the anonymous review-time copy, containerization, a runnable entry point, and what ISSTA artifact evaluators actually try first.
---

# ISSTA Artifact Evaluation

Use this to package evidence for ISSTA's artifact-evaluation track. ISSTA has a genuinely strong
artifact culture: a runnable tool and a shared benchmark are treated as normal, and the badges
carry weight. Reopen the current artifact call before packaging — the badge set and the archival
requirement are cycle-specific.

## The ACM badge targets

| Badge | What it certifies | What you must ship |
|---|---|---|
| Artifacts Available | The artifact is publicly, permanently retrievable | A DOI-issuing deposit (Zenodo) — a GitHub link alone does not qualify |
| Artifacts Evaluated — Functional | The artifact runs and does what the paper says | A working entry point, dependencies, and a documented expected output |
| Artifacts Evaluated — Reusable | Others can inspect, adapt, and build on it | Clean structure, real documentation, and configurability beyond the paper's runs |
| Results Reproduced | The paper's key results regenerate from the artifact | Scripts that produce the paper's tables/figures within stated tolerance |

Available is about *archival*; Functional and Reusable are about *engineering quality*; Results
Reproduced is about *matching the paper*. They are earned independently — decide which you are
going for before you package.

## Artifact plan

- Decide the badge set, then package to its bar. A Reusable badge needs documentation and structure
  a Functional-only artifact can skip.
- Ship the tool with a single documented entry point and a container or environment file, so an
  evaluator reaches a result without reconstructing your machine.
- Pin subjects and benchmark versions: the exact Defects4J revision, subject-program commit SHAs,
  and any fuzzing seed corpora, archived rather than referenced by name.
- Provide a results-regeneration path: a script that takes logged runs to the paper's tables, so
  "Results Reproduced" is a command, not an argument.
- Anonymize the review-time copy — repository owners, commit authors, container labels — because
  ISSTA artifact review is double-anonymous alongside the paper.
- After acceptance, make the Zenodo deposit public and citable, and record its DOI for the
  camera-ready badge display.

## What ISSTA evaluators try first

- The README's quick-start, then the single command that produces one headline number. If that
  fails on a clean machine, no amount of internal quality is visible.
- A small, fast subset that finishes in minutes, before any full multi-day fuzzing or
  symbolic-execution campaign. Ship a "smoke" configuration explicitly.
- The mapping from a paper claim to the artifact output that supports it; an artifact whose outputs
  cannot be tied back to Table N reads as unverifiable.

## Handling long-running and non-deterministic tools

Testing and analysis artifacts often run for hours and vary between runs. Package for that reality:

```text
artifact/
  README.md            # quick-start, smoke config, full config, expected outputs, runtime
  Dockerfile           # pinned toolchain and dependencies
  subjects/            # pinned subject SHAs or a fetch script that pins them
  run_smoke.sh         # minutes: reproduces one representative row
  run_full.sh          # hours/days: reproduces all tables
  results/             # logged raw outputs from the authors' runs
  scripts/tables.py    # regenerates paper tables from results/
```

State the run count and expected variance for non-deterministic results, and have the
regeneration script accept the evaluator's fresh runs as well as the shipped logs, so a partial
reproduction still lands on the paper's numbers within tolerance.

## Calibration anchors

- Evaluators are time-boxed; assume they run the smoke config and skim the full one. Design so the
  smoke path alone justifies Functional.
- Badge names, the Zenodo requirement, and any single-blind vs. double-blind detail vary by cycle;
  verify against the current artifact call rather than a past year.

## Output format

```text
[Badge target] Available / Functional / Reusable / Results Reproduced
[Entry point] <command + smoke runtime>
[Pinned subjects] <benchmark version / SHAs archived?>
[Reproduction level] turnkey / scripted / descriptive / weak
[Anonymity risks] <owners/authors/labels/paths>
[Fixes before upload] <ordered list>
```
