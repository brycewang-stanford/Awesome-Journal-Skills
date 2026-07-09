# ATC Replication-Package Code Adapter

This directory routes ATC authors to the repository-level shared tooling. It stays deliberately
thin: ATC-specific *policy* (the ACM SIGOPS transition, the two-round extended-abstract review,
double-blind reviewing, shepherded conditional acceptance, the Available/Functional/Reproduced
badges) lives in the skills and in [`../official-source-map.md`](../official-source-map.md);
reusable *tooling* lives in the shared kits so packs do not carry diverging copies.

## Shared kits

- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
  — anonymous-review and public-release checks that transfer to any systems replication package.
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)
  — dependency-free smoke checker for package layout.
- [`../../../shared-resources/submission-readiness/readiness-checklist.md`](../../../shared-resources/submission-readiness/readiness-checklist.md)
  and [`../../../shared-resources/submission-readiness/response-to-referees.md`](../../../shared-resources/submission-readiness/response-to-referees.md)
  — generic pre-submission and response scaffolding; adapt the latter to the ATC rebuttal and the
  shepherd's description-of-changes in [`../../skills/atc-author-response/SKILL.md`](../../skills/atc-author-response/SKILL.md).

## Typical use for an ATC package

```bash
# Smoke-check the anonymized artifact before the HotCRP upload
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/atc-artifact-staging
```

Treat the script as a layout smoke test only. Venue policy still comes from the current SIGOPS call
for papers, the call for artifacts, and the ATC skills for experiments, reproducibility, and
artifact evaluation.

## ATC-specific checks the generic tooling cannot make

- **The extended abstract must stand alone.** ATC 2026's first review round judges a two-page
  extended abstract that a reviewer may read *instead of* the full paper. The generic kit checks
  the code package, not the paper; verify the abstract carries the problem, contribution, and key
  result on its own (`../../skills/atc-writing-style/SKILL.md`).
- **Double-blind extends to the repository.** A linked repo, a system named after your group, or a
  cluster hostname in a log can de-anonymize the submission. Anonymize or mirror the artifact behind
  a blind service before upload (`../../skills/atc-submission/SKILL.md`).
- **Systems provenance is pinned.** Record kernel/OS versions, hardware (CPU/NIC/SSD models), commit
  SHAs, workload generators and traces, and warm-up/measurement windows — a package that cannot
  re-create the testbed re-runs a different experiment (`../../skills/atc-experiments/SKILL.md`).
- **A turnkey path to the headline numbers.** For the **Results Reproduced** badge an evaluator
  must regenerate the paper's main figures/tables from the artifact; ship a claim-to-script mapping
  and a small-scale mode for hardware they lack (`../../skills/atc-artifact-evaluation/SKILL.md`).
- **Badge readiness is a post-acceptance task.** A DOI-issuing archive, an open license, and
  evaluator-proof reuse docs target the Available/Functional/Reproduced badges on the AEC's own
  deadline, after conditional acceptance and shepherding
  (`../../skills/atc-artifact-evaluation/SKILL.md`).

This is not the econometrics/Stata kit used by the journal packs in this repository, and ATC
evidence is not ML-leaderboard evidence: do not import DiD notebooks or benchmark-score framing
here. ATC rewards measured systems behavior on real testbeds.
