# USENIX FAST Replication-Package Code Adapter

This directory routes FAST authors to the repository-level shared tooling. It stays deliberately
thin: FAST-specific *policy* (the two-deadline USENIX cycle, double-blind review, one-shot
revision, the three USENIX artifact badges, storage-evidence norms) lives in the skills and in
[`../official-source-map.md`](../official-source-map.md); reusable *tooling* lives in the shared
kits so packs do not carry diverging copies.

## Shared kits

- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
  — anonymous-review and public-release checks that transfer to any systems replication package.
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)
  — dependency-free smoke checker for package layout.
- [`../../../shared-resources/submission-readiness/readiness-checklist.md`](../../../shared-resources/submission-readiness/readiness-checklist.md)
  and [`../../../shared-resources/submission-readiness/response-to-referees.md`](../../../shared-resources/submission-readiness/response-to-referees.md)
  — generic pre-submission and response scaffolding; adapt the latter to the one-shot-revision
  change ledger in [`../../skills/fast-author-response/SKILL.md`](../../skills/fast-author-response/SKILL.md).

## Typical use for a FAST package

```bash
# Smoke-check the anonymized artifact before the HotCRP upload
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/fast-artifact-staging
```

Treat the script as a layout smoke test only. Venue policy still comes from the current Call for
Papers, the Call for Artifacts, and the FAST skills for experiments, reproducibility, and artifact
evaluation.

## FAST-specific checks the generic tooling cannot make

- **Storage provenance is pinned.** Record exact **drive/SSD/NVM models and firmware versions**,
  host and kernel, filesystem/mkfs options, and the identifiers of every workload and trace (SNIA
  IOTTA IDs, YCSB workload letters, filebench/fio job files). A storage result that omits the device
  and firmware is not reproducible — nominally identical drives differ part-to-part and across
  firmware (`../../skills/fast-reproducibility/SKILL.md`).
- **Device state is controlled.** Note whether SSDs were preconditioned/aged, whether TRIM was on,
  and the fill level — steady-state vs. fresh-out-of-box numbers differ enough to change a
  conclusion (`../../skills/fast-experiments/SKILL.md`).
- **Crash-consistency claims ship their test harness.** If the paper claims consistency under power
  loss, the artifact carries the fault-injection or record-and-replay setup (e.g. block-level
  logging / replay tooling), not just the file-system code (`../../skills/fast-experiments/SKILL.md`).
- **Traces are available or documented.** Large workload traces are archived (or their access is
  documented) so the evaluation reproduces rather than re-samples; ship the replay scripts, not just
  the trace name (`../../skills/fast-reproducibility/SKILL.md`).
- **The artifact is double-blind at submission, badge-ready after.** At review time no owner
  strings, cluster paths, lab names, or identity-revealing trace-hosting URLs; after acceptance,
  swap in the public, licensed, DOI-issuing archive that targets the USENIX **Available / Functional
  / Reproduced** badges (`../../skills/fast-artifact-evaluation/SKILL.md`).
- **Endurance/long-run results state their budget.** Wear or aging experiments that took device-days
  or -weeks say so, and the artifact documents which results are turnkey and which require the full
  slow run (`../../skills/fast-experiments/SKILL.md`).

This is not the econometrics/Stata kit used by the journal packs in this repository, and FAST
evidence is not ML-leaderboard evidence: do not import DiD notebooks or benchmark-score framing
here.
