---
name: hpca-artifact-evaluation
description: Use when packaging an HPCA artifact for the voluntary post-acceptance evaluation on the separate AE HotCRP: scoping reproducibility tiers, preparing simulator- and silicon-heavy workflows for cold-start evaluators, budgeting their wall-clock time, and earning IEEE reproducibility badges.
---

# HPCA Artifact Evaluation

Use this to prepare an HPCA artifact for the badge round. HPCA's artifact evaluation
is **voluntary, post-acceptance, and run on a separate HotCRP**
(`hpca<year>ae.hotcrp.com`) under **IEEE reproducibility badging** — not the ACM
Artifact Review and Badging policy the ACM-touched siblings use. Package for the IEEE
pipeline and for an evaluator who has never seen your infrastructure.

## Scope the reproducibility tiers

Not every claim can be reproduced cheaply. Decide, per headline result, what an
evaluator can realistically achieve and say so:

- **Full reproduction** — the evaluator regenerates the headline numbers from source.
  The strongest badge target; reserve it for results whose pipeline you can shrink to
  fit an evaluator's budget.
- **Regeneration from logs** — the evaluator rebuilds figures from provided raw
  output when a full run is too long or needs licensed workloads.
- **Inspection** — the evaluator confirms the code implements the mechanism when
  hardware or license constraints block execution.

State each result's tier in the artifact README so evaluators are not surprised.

## Package for a cold-start evaluator

The evaluator has no license to your workloads, no copy of your machine, and a fixed
time budget. Design for that:

| Obstacle | What to ship |
|---|---|
| No workload license | Recipe + checksums, plus one free workload that runs the full pipeline |
| No access to your machine | Container/script that builds on a clean host; pinned dependencies |
| Long simulations | Reduced-input variants of the headline runs, with measured runtimes |
| Silicon-only results | Captured machine-state logs + an inspection path when re-running is impossible |
| Unclear entry point | A top-level `run.sh` that reproduces one headline figure end to end |

## Budget the evaluator's wall-clock

An artifact that "reproduces everything" in three days of compute will not be fully
reproduced. Provide reduced-input variants of the headline experiments with **stated
per-step runtimes**, so an evaluator can plan and finish inside the AE window. Put the
expensive full runs behind a clearly labeled optional path.

## Mirror ↔ release

The anonymized artifact mirror used during review becomes the de-anonymized public
release at the badge round. De-anonymize deliberately: restore author names, add the
real repository, and check that nothing was left blinded that should now be open —
and nothing personal was left in that should not.

## Packaging pass

```text
1. Per-result tier declared (full / regeneration / inspection)
2. Cold-start build works on a clean host (container or script, pinned deps)
3. One free workload exercises the full pipeline end to end
4. Reduced-input variants with measured per-step runtimes provided
5. Licensed workloads reduced to recipe + checksums
6. run.sh reproduces one headline figure without hand-holding
7. De-anonymized for release; README states tiers and expected runtimes
```

## Output format

```text
[AE readiness] Ready / Needs work / Not ready
[Tiers] results with a declared tier / total
[Cold start] clean-host build passes? (Y/N)
[Budget] reduced variants + runtimes stated? (Y/N)
[Badge target] full-reproduction results / total
[Top gaps] <ordered>
```

Reopen the current AE page for the badge set, the calendar, and the submission
mechanics — the IEEE badge names and AE timeline are per-edition.
