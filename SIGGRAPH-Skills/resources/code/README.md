# SIGGRAPH Replicability-Package Code Adapter

This directory routes SIGGRAPH authors to the repository-level shared tooling. It stays
deliberately thin: SIGGRAPH-specific *policy* (the ACM TOG journal-integrated dual-track model, the
1000-word rebuttal, conditional acceptance, the Graphics Replicability Stamp) lives in the skills
and in [`../official-source-map.md`](../official-source-map.md); reusable *tooling* lives in the
shared kits so packs do not carry diverging copies.

## Shared kits

- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
  — release-time checks that transfer to any code+data package.
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)
  — dependency-free smoke checker for package layout.
- [`../../../shared-resources/submission-readiness/readiness-checklist.md`](../../../shared-resources/submission-readiness/readiness-checklist.md)
  and [`../../../shared-resources/submission-readiness/response-to-referees.md`](../../../shared-resources/submission-readiness/response-to-referees.md)
  — generic pre-submission and response scaffolding; adapt the latter to the **1000-word, text-only
  rebuttal** in [`../../skills/siggraph-author-response/SKILL.md`](../../skills/siggraph-author-response/SKILL.md)
  (the SIGGRAPH rebuttal is far shorter and narrower than a journal response letter).

## Typical use for a SIGGRAPH package

```bash
# Smoke-check the supplemental code bundle before the Linklings upload
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/siggraph-supplemental/code
```

Treat the script as a layout smoke test only. Venue policy still comes from the current
technical-papers call and the SIGGRAPH skills for experiments, reproducibility, supplementary
material, and the replicability stamp.

## SIGGRAPH-specific checks the generic tooling cannot make

- **The results video is primary evidence.** No generic checker validates that your supplemental
  video opens on the headline result versus the strongest baseline, shows motion and failure cases,
  and is labeled and rights-cleared on every frame
  (`../../skills/siggraph-supplementary/SKILL.md`).
- **Results must regenerate deterministically.** Seed Monte Carlo renderers and stochastic
  simulations, state the comparison metric and tolerance, and bundle reference images so a reader —
  or a Graphics Replicability Stamp volunteer — reproduces a *figure*, not just a compile
  (`../../skills/siggraph-reproducibility/SKILL.md`, `../../skills/siggraph-artifact-evaluation/SKILL.md`).
- **Ship the assets, not just the code.** Graphics results need scenes, meshes, textures, and
  weights; a package that compiles but lacks its inputs reproduces nothing
  (`../../skills/siggraph-reproducibility/SKILL.md`).
- **Timings are checkable claims.** Record GPU/CPU, driver, resolution, and settings alongside
  every reported time (`../../skills/siggraph-experiments/SKILL.md`).
- **The stamp is community-run and post-acceptance.** GRSI/CRCG recognition and Software Heritage
  archiving are separate from SIGGRAPH's review and its ACM TOG camera-ready — not the ACM Artifact
  Badging scheme used at systems/SE venues (`../../skills/siggraph-artifact-evaluation/SKILL.md`).

This is not the econometrics/Stata kit used by the journal packs in this repository, and SIGGRAPH
evidence is not ML-leaderboard evidence: do not import DiD notebooks or single-metric benchmark
framing here — SIGGRAPH persuades with shown results, comparisons, and timings.
