# CAV Replication-Package Code Adapter

This directory routes CAV authors to the repository-level shared tooling. It stays deliberately
thin: CAV-specific *policy* (the LNCS open-access process, two-stage review, partial
double-anonymity, AEC badges, benchmark reproducibility) lives in the skills and in
[`../official-source-map.md`](../official-source-map.md); reusable *tooling* lives in the shared
kits so packs do not carry diverging copies.

## Shared kits

- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
  — anonymous-review and public-release checks that transfer to any artifact package.
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)
  — dependency-free smoke checker for package layout.
- [`../../../shared-resources/submission-readiness/readiness-checklist.md`](../../../shared-resources/submission-readiness/readiness-checklist.md)
  and [`../../../shared-resources/submission-readiness/response-to-referees.md`](../../../shared-resources/submission-readiness/response-to-referees.md)
  — generic pre-submission and response scaffolding; adapt the latter to the CAV rebuttal in
  [`../../skills/cav-author-response/SKILL.md`](../../skills/cav-author-response/SKILL.md).

## Typical use for a CAV artifact

```bash
# Smoke-check the artifact package before the AEC submission
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/cav-artifact-staging
```

Treat the script as a layout smoke test only. Venue policy still comes from the current Call for
Papers, the Artifact Evaluation page, and the CAV skills for experiments, reproducibility, and
artifact evaluation.

## CAV-specific checks the generic tooling cannot make

- **Benchmark provenance is pinned.** Record the exact SV-COMP / SMT-COMP / HWMCC / VNN-COMP
  benchmark-set revision, the subset you ran and why, and the extraction date — "the standard
  benchmarks" without a revision is not reproducible
  (`../../skills/cav-experiments/SKILL.md`).
- **Solver versions, seeds, and resource limits are fixed.** For portfolio or randomized solvers,
  log the seed, the wall-clock and memory limits per instance, the number of cores, and the exact
  hardware — verification results are dominated by timeouts, so a comparison without a stated
  resource budget is meaningless (`../../skills/cav-reproducibility/SKILL.md`).
- **Soundness claims ship checkable evidence.** Where the paper claims correctness, include the
  proof certificate / unsat proof / verification witness (e.g., an SV-COMP-style witness, a DRAT
  proof, or an Isabelle/Coq proof script) and an independent checker, not just a "verified" verdict
  (`../../skills/cav-reproducibility/SKILL.md`).
- **The anonymity rule depends on category.** Regular and Application artifacts submitted for the
  double-blind paper review must be anonymized; Tool and Industrial papers are not double-blind.
  The **AEC** artifact (post-notification) is separate from any review-time artifact — do not
  conflate them (`../../skills/cav-artifact-evaluation/SKILL.md`).
- **Badges are the AEC's, on its own timeline.** Available (public DOI archive), Functional, and
  Reusable are earned by AEC members running your package across a smoke-test and a full-review
  phase, after notification and independent of camera-ready
  (`../../skills/cav-artifact-evaluation/SKILL.md`).

This is not the econometrics/Stata kit or the ML-leaderboard kit used by other packs in this
repository: CAV evidence is benchmark-and-proof evidence, so do not import DiD notebooks or
accuracy-table framing here.
