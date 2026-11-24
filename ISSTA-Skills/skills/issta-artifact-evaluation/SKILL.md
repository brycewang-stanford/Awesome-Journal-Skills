---
name: issta-artifact-evaluation
description: Use when packaging an ISSTA tool, benchmark, and results for the artifact-evaluation track, covering the ACM badges (Artifacts Available via a DOI-issuing archive, Evaluated Functional and Reusable; Results Reproduced only where the call offers it), the anonymous review-time copy, the required container/VM packaging and README/REQUIREMENTS/STATUS/LICENSE files, a runnable entry point, and what ISSTA artifact evaluators actually try first.
---

# ISSTA Artifact Evaluation

Use this to package evidence for ISSTA's artifact-evaluation track. ISSTA has a genuinely strong
artifact culture: a runnable tool and a shared benchmark are treated as normal, and the badges
carry weight. Reopen the current artifact call before packaging — the badge set and the archival
requirement are cycle-specific. The latest posted call (ISSTA 2026, re-read 2026-11-24) is voluntary,
for accepted research papers, does not alter acceptance, and awards **up to two** badges among
Functional, Reusable and Available; the ISSTA 2027 AE call was not yet posted.

## The ACM badge targets

| Badge | What it certifies | What you must ship |
|---|---|---|
| Artifacts Available | The artifact is publicly, permanently retrievable | A DOI-issuing deposit (Zenodo, FigShare, Dryad or similar) — a GitHub link alone does not qualify |
| Artifacts Evaluated — Functional | The artifact runs and does what the paper says | A working entry point, dependencies, and a documented expected output |
| Artifacts Evaluated — Reusable | Others can inspect, adapt, and build on it | Clean structure, real documentation, and configurability beyond the paper's runs |
| Results Reproduced (only if offered) | The paper's key results are confirmed independently | ISSTA 2026 AE did not award ACM "Results Validated" badges; the ISSTA 2027 call mentions Results Reproduced for replicability-study artifacts — check the 2027 AE call |

Available is about *archival*; Functional and Reusable are about *engineering quality* (Reusable
includes Functional, so in practice you aim for Available plus one of them). Decide which you are
going for before you package, and state it in the required STATUS file with a short justification.

## Artifact plan

- Decide the badge set, then package to its bar. A Reusable badge needs documentation and structure
  a Functional-only artifact can skip.
- Ship the tool as a Container (Docker, Podman) or VM (OVF/OVA) image — the 2026 call requires
  one — with a single documented entry point, plus README (a Getting Started guide finishable in
  30 minutes, then step-by-step reproduction naming which claims the artifact does and does not
  support), REQUIREMENTS, STATUS and LICENSE files in plain text or PDF.
- Pin subjects and benchmark versions: the exact Defects4J revision, subject-program commit SHAs,
  and any fuzzing seed corpora, archived rather than referenced by name.
- Provide a results-regeneration path: a script that takes logged runs to the paper's tables, so
  reproducing the paper is a command, not an argument.
- Anonymize the review-time copy that accompanies the paper — repository owners, commit authors,
  container labels — because paper review is double-anonymous and one reviewer checks the
  artifact. For the AE submission itself, host on a platform that does not track IP addresses, to
  protect evaluator anonymity.
- Expect a kick-the-tires phase with a 4-day author response window; fix setup issues then.
- After acceptance, make the archived deposit public and citable, and record its DOI for the
  camera-ready badge display and the Data Availability section.

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
- Badge names, the archival requirement, and anonymity details vary by cycle; verify against the
  current artifact call rather than a past year.

## Output format

```text
[Badge target] Available / Functional / Reusable
[Entry point] <command + smoke runtime>
[Pinned subjects] <benchmark version / SHAs archived?>
[Reproduction level] turnkey / scripted / descriptive / weak
[Anonymity risks] <owners/authors/labels/paths>
[Fixes before upload] <ordered list>
```
