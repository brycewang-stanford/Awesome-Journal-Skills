---
name: vldb-artifact-evaluation
description: Use when preparing a PVLDB artifact for the pVLDB Reproducibility Evaluation or the ACM availability badge, covering the mandatory participation rule for EA&B papers, the four artifact surfaces evaluators rebuild, packaging for a rerun by strangers, and positioning for the Best Reproducible Paper Award at VLDB.
---

# VLDB Artifact Evaluation

Use this once a PVLDB paper is accepted (or when an EA&B submission is being
planned, since participation is not optional there). The pVLDB Reproducibility
Evaluation — run jointly with SIGMOD's effort since the 2018 push — has
committee members rebuild your experiment from your package. Two distinct
prizes exist: the ACM **availability** badge for sharing, and the
**Reproducible** outcome (with a Best Reproducible Paper Award) for surviving
an independent rerun.

## Who must play, who should

| Situation | Obligation |
|---|---|
| EA&B paper | Required: release all data and software, submit to evaluation |
| Regular research paper | Optional but strongly encouraged; badge on offer |
| Industrial paper with proprietary core | Availability of what can be shared; document the rest |
| Vision paper | Rarely applicable |

## The four surfaces evaluators rebuild

The committee's published expectations decompose an artifact into four layers.
Package each one explicitly:

1. **Prototype** — source code, build environment, configuration. A container
   image plus the Dockerfile that produced it is the community's default.
2. **Input data** — the datasets themselves, or deterministic generators with
   pinned seeds and a size knob, plus download scripts for public corpora.
3. **Workload** — the exact queries, client configuration, thread counts, and
   run durations behind every experiment, not a representative sample.
4. **Analysis** — scripts that transform raw measurements into each numbered
   figure and table in the PDF. This layer is the one authors most often skip
   and evaluators most often need.

## Design for a stranger's machine

- Assume the evaluator has no access to your cluster. Provide a scaled-down
  mode that demonstrates every claim's *shape* on one commodity machine, and
  document how the full-scale numbers were obtained.
- Pin everything: base images, package versions, competitor-system commits.
  "Latest" is where reruns go to die.
- Emit expected outputs and tolerances. A rerun that produces a plot is only
  useful if the evaluator can tell whether the plot is right — state which
  qualitative relationships must hold even when absolute numbers shift with
  hardware.
- Time-box honestly: state wall-clock cost per experiment so the committee can
  schedule, and mark the one experiment that best represents the paper if
  resources run short.

## Minimal package skeleton

```text
artifact/
  README.md          # claims map: figure/table -> command -> expected shape
  Dockerfile         # or image reference + build recipe
  data/get_data.sh   # fetch or generate, seeded
  workloads/         # exact configs per experiment
  run_one.sh <exp>   # single experiment, scaled-down default
  run_full.sh        # full-scale protocol, hardware stated
  plots/make_all.sh  # raw results -> paper figures
```

## Award positioning

Winning packages read like engineering products: one command to a first
result, claims mapped to figures, failures anticipated. If the evaluation
report will say "worked on the first try," you are in contention; if it says
"worked after correspondence with the authors," you got the badge and lost the
award. Current-cycle evaluation logistics and criteria wording: 待核实 on
`vldb.org/pvldb/reproducibility` before packaging.

## Output format

```text
[Track] EA&B-mandatory / voluntary / availability-only
[Surface coverage] prototype / data / workload / analysis — gaps listed
[Stranger test] scaled-down mode exists / cluster-only (risk)
[Pinning] images, versions, competitor commits — unpinned items
[First-command experience] <what happens>
[Fixes before submission to the committee] <ordered>
```
