# IEEE INFOCOM Replication-Package Code Adapter

This directory routes INFOCOM authors to the repository-level shared tooling. It stays deliberately
thin: INFOCOM-specific *policy* (the large-scale double-blind EDAS process, the IEEEtran page
budget, the early-reject phase, the traditional absence of a rebuttal, and the absence of a formal
artifact track) lives in the skills and in
[`../official-source-map.md`](../official-source-map.md); reusable *tooling* lives in the shared
kits so packs do not carry diverging copies.

## Shared kits

- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
  — anonymous-review and public-release checks that transfer to any networking replication package.
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)
  — dependency-free smoke checker for package layout.
- [`../../../shared-resources/submission-readiness/readiness-checklist.md`](../../../shared-resources/submission-readiness/readiness-checklist.md)
  — generic pre-submission scaffolding; adapt it to the EDAS abstract-then-paper flow and the
  double-blind sweep in [`../../skills/infocom-submission/SKILL.md`](../../skills/infocom-submission/SKILL.md).

## Typical use for an INFOCOM package

```bash
# Smoke-check an (optional) anonymized artifact before you link it in the submission
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/infocom-artifact-staging
```

Treat the script as a layout smoke test only. Venue policy still comes from the current Call for
Papers and the INFOCOM skills for experiments, reproducibility, and (optional) artifact release.

## INFOCOM-specific checks the generic tooling cannot make

- **There is no artifact-evaluation track, so a release is optional and self-directed.** Package for
  a skeptical reviewer's credibility and for post-publication reuse, not to pass an evaluator or earn
  an INFOCOM badge (none is confirmed; 待核实) — see
  [`../../skills/infocom-artifact-evaluation/SKILL.md`](../../skills/infocom-artifact-evaluation/SKILL.md).
- **The page budget counts appendices.** A full proof or a big table in an in-paper appendix eats
  the same nine-page text budget as the body; the smoke checker cannot see this — verify it against
  [`../../skills/infocom-supplementary/SKILL.md`](../../skills/infocom-supplementary/SKILL.md).
- **The submitted PDF must be self-defending.** Because there is (traditionally) no rebuttal, every
  number a reviewer might doubt needs a stated configuration, a proof, or a released script — see
  [`../../skills/infocom-experiments/SKILL.md`](../../skills/infocom-experiments/SKILL.md) and
  [`../../skills/infocom-author-response/SKILL.md`](../../skills/infocom-author-response/SKILL.md).
- **Simulation provenance is pinned.** For simulation studies, record the simulator and version,
  topology, traffic model, seeds, and run count; a package that cannot regenerate the paper's
  figures re-samples rather than reproduces
  ([`../../skills/infocom-reproducibility/SKILL.md`](../../skills/infocom-reproducibility/SKILL.md)).
- **De-anonymize only at camera-ready.** The review-time link (if any) is anonymized on an
  anonymizing host; the public DOI-issuing archive (Zenodo/IEEE DataPort/Software Heritage) with an
  open license comes after acceptance
  ([`../../skills/infocom-camera-ready/SKILL.md`](../../skills/infocom-camera-ready/SKILL.md)).

This is not the econometrics/Stata kit used by the journal packs in this repository, and INFOCOM
evidence is not ML-leaderboard evidence: do not import DiD notebooks or benchmark-score framing
here. INFOCOM evidence is a stated model with a proof, a seeded simulation, or a measurement study.
