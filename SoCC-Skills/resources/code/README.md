# ACM SoCC Reproducibility-Package Code Adapter

This directory routes SoCC authors to the repository-level shared tooling. It stays deliberately
thin: SoCC-specific *policy* (the two-round calendar, dual-anonymous review, the joint
SIGMOD+SIGOPS scope, ACM badging) lives in the skills and in
[`../official-source-map.md`](../official-source-map.md); reusable *tooling* lives in the shared
kits so packs do not carry diverging copies.

## Shared kits

- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
  — anonymous-review and public-release checks that transfer to any systems reproducibility
  package.
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)
  — dependency-free smoke checker for package layout.
- [`../../../shared-resources/submission-readiness/readiness-checklist.md`](../../../shared-resources/submission-readiness/readiness-checklist.md)
  and [`../../../shared-resources/submission-readiness/response-to-referees.md`](../../../shared-resources/submission-readiness/response-to-referees.md)
  — generic pre-submission and response scaffolding; adapt the latter to the SoCC rebuttal in
  [`../../skills/socc-author-response/SKILL.md`](../../skills/socc-author-response/SKILL.md).

## Typical use for a SoCC package

```bash
# Smoke-check the anonymized artifact before the HotCRP upload
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/socc-artifact-staging
```

Treat the script as a layout smoke test only. Venue policy still comes from the current
research-papers call and the SoCC skills for experiments, reproducibility, and artifact
evaluation.

## SoCC-specific checks the generic tooling cannot make

- **Reproduction is a systems reproduction, not a re-run of a notebook.** A SoCC artifact usually
  needs a **testbed or cluster description**, workload generators or **replayed traces**, and the
  measurement scripts that turn raw logs into the paper's throughput/latency/cost figures — not
  just a training script (`../../skills/socc-experiments/SKILL.md`).
- **Cost and tail latency must be reproducible, not only the mean.** The package should let an
  evaluator regenerate the **tail (p95/p99) and cost** numbers, and document the hardware, instance
  types, and run count that produced them (`../../skills/socc-reproducibility/SKILL.md`).
- **Traces and datasets are anonymized at submission and released at camera-ready.** Under
  dual-anonymous review, released traces, cluster names, provider hints, and repository owners must
  be scrubbed for the review artifact, then permanentized in a DOI-issuing archive afterward
  (`../../skills/socc-supplementary/SKILL.md`, `../../skills/socc-camera-ready/SKILL.md`).
- **ACM badges are the target where the edition offers evaluation.** A DOI-issuing archive
  (Zenodo / figshare / Software Heritage), an open license, and evaluator-proof reproduction docs
  target the ACM Available / Functional / Reusable / Reproduced badges; **whether SoCC runs a
  dedicated artifact-evaluation track for a given edition is 待核实** — confirm on the current call
  (`../../skills/socc-artifact-evaluation/SKILL.md`).

This is not the econometrics/Stata kit used by the journal packs in this repository, and SoCC
evidence is not an ML leaderboard: do not import DiD notebooks or single-accuracy-number framing
here. SoCC evidence is deployment-and-measurement evidence read by a joint SIGMOD+SIGOPS audience.
