---
name: icde-artifact-evaluation
description: Use when packaging IEEE ICDE code, data, workload generators, and logs as supplemental material whose availability reviewers score, and for any post-acceptance reproducibility or badge process the edition runs. Covers what a builder-heavy committee inspects first, making a data-systems benchmark turnkey, and single-blind packaging.
---

# ICDE Artifact Evaluation

Use this for evidence packaging around ICDE. ICDE expects authors to submit supplemental
material and **considers its availability in the evaluation**, so a strong artifact directly
raises the paper's floor even where no separate badge process runs. Confirm whether the current
edition also runs a post-acceptance reproducibility/badge track (待核实) before promising
evaluators anything.

## Artifact plan

- Decide what evidence a **builder** needs to believe the numbers: the system source, the
  workload generators, the baselines' configurations, the datasets or their construction
  scripts, seeds, and logs.
- Keep decision-critical evidence in the **paper or its figures**; the artifact demonstrates
  reproducibility, it does not replace the argument.
- Provide a **minimal reproduction map**: build steps, dependencies, hardware assumptions
  (especially the storage device), commands, expected outputs, runtime, and known
  nondeterminism sources.
- For restricted or proprietary data, give enough provenance and construction detail for a
  credible re-run without violating data-use terms.
- After acceptance, publish the **public, licensed, tagged** version whose commit produced the
  paper's numbers.

## What ICDE evidence reviewers open first

| Claim type | First artifact inspected | Common failure caught |
|---|---|---|
| Throughput/latency win | `run_small.sh` and the workload generator | Numbers cannot be regenerated; generator or seeds absent |
| "Mechanism causes the gain" | The ablation toggle in the code | The toggle does not exist; gain not isolable in the artifact |
| Baseline comparison | The baseline's config files | Baseline was untuned or run with defaults |
| Scale claim | The scale-factor sweep script | Only one scale factor is actually runnable |
| Cost/overhead claim | The instrumentation that measures cost | Cost is asserted but not measured anywhere |

Because ICDE reviewers are builders, they will **re-run a small benchmark** far sooner than they
will provision a cluster — make `run_small.sh` reproduce the headline crossover on one machine
in minutes before polishing anything else.

## Worked vignette: packaging a storage-engine benchmark

A submission proposes a write-optimized index validated on a telemetry trace and a synthetic
sweep.

- Ship the workload as a **parameterized generator** (append rate, append-to-scan ratio, key
  distribution), not constants buried in a driver, so reviewers can vary the regime.
- Record the **exact seed sequence and run count** behind every throughput and latency-tail
  figure; percentile claims are meaningless without them.
- Emit figures **directly from logged runs** so PDF and artifact numbers cannot drift.
- Include the **ablation switch** and the **baseline configs** so a reviewer can reproduce both
  the effect and the fair comparison.

## Single-blind and logistics anchors

- ICDE is single-blind: the artifact need **not** be anonymized — leave author names and history
  in place; spend the effort on making it build and run.
- Assume, absent a formal badge track, that only the **README and one entry script** get opened;
  design for that. If a badge/reproducibility process does run this edition, read its criteria
  before packaging.
- Upload size limits and accepted formats vary by edition; verify against the current CMT
  submission form.

## Output format

```text
[Artifact role] scored supplement / post-acceptance reproducibility / public archive
[Contents] <source / generators / baseline-configs / logs / claims-map>
[Turnkey check] <does run_small.sh reproduce the headline result? y/n>
[Isolability] <is the mechanism ablation runnable in the artifact? y/n>
[Hygiene] <secrets / caches / bloat removed>
[Fixes before upload] <ordered list>
```
