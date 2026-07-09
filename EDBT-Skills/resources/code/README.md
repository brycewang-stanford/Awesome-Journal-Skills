# EDBT Replication-Package Code Adapter

This directory routes EDBT authors to the repository-level shared tooling. It stays deliberately
thin: EDBT-specific *policy* (the multiple-cycle rolling process, the in-cycle revise-and-resubmit,
Microsoft CMT review, the OpenProceedings open-access publication, and database-systems
reproducibility) lives in the skills and in [`../official-source-map.md`](../official-source-map.md);
reusable *tooling* lives in the shared kits so packs do not carry diverging copies.

## Shared kits

- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
  — artifact and public-release checks that transfer to any systems replication package.
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)
  — dependency-free smoke checker for package layout.
- [`../../../shared-resources/submission-readiness/readiness-checklist.md`](../../../shared-resources/submission-readiness/readiness-checklist.md)
  and [`../../../shared-resources/submission-readiness/response-to-referees.md`](../../../shared-resources/submission-readiness/response-to-referees.md)
  — generic pre-submission and response scaffolding; adapt the latter to the EDBT revise-and-resubmit
  change letter in [`../../skills/edbt-author-response/SKILL.md`](../../skills/edbt-author-response/SKILL.md).

## Typical use for an EDBT package

```bash
# Smoke-check the artifact before the Microsoft CMT upload
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/edbt-artifact-staging
```

Treat the script as a layout smoke test only. Venue policy still comes from the current EDBT/ICDT
host-site call and the EDBT skills for experiments, reproducibility, and artifact evaluation.

## EDBT-specific checks the generic tooling cannot make

- **The claim shape is a database-systems claim.** Evidence must be workloads, datasets, scale, and
  fair, tuned baselines — not ML leaderboard scores and not econometric identification. Match the
  Experiments & Analysis standard where the paper's contribution *is* the measurement
  (`../../skills/edbt-experiments/SKILL.md`).
- **Provenance is pinned for a reproducible open-access record.** Record dataset versions and
  sources, workload/query-log derivation, hardware and cluster configuration, engine build/commit,
  and seeds; a package that cannot be re-run from the archive re-measures rather than reproduces
  (`../../skills/edbt-reproducibility/SKILL.md`).
- **The paper and the artifact agree.** Every number the reviewers weigh should trace to a script in
  the package; a value in the PDF that no script produces is the contradiction that reads as
  carelessness (`../../skills/edbt-reproducibility/SKILL.md`).
- **The open-access license is compatible.** EDBT publishes on OpenProceedings under CC-BY-NC-ND; the
  artifact should carry an OSI-approved code license and clear data terms, deposited in a DOI-issuing
  archive (Zenodo, figshare, Software Heritage) so the permanent record links resolve
  (`../../skills/edbt-camera-ready/SKILL.md`, `../../skills/edbt-artifact-evaluation/SKILL.md`).
- **Cycle and ban logic are not code checks.** Confirm the chosen cycle, the paper shape, and the
  12-month resubmission-ban status by hand against the current call — the smoke checker cannot see
  them (`../../skills/edbt-submission/SKILL.md`).

This is not the econometrics/Stata kit used by the journal packs in this repository, and EDBT
evidence is not ML-leaderboard evidence: do not import DiD notebooks or benchmark-score framing here.
