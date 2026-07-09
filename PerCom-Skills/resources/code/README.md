# IEEE PerCom Reproducibility / Dataset Code Adapter

This directory routes PerCom authors to the repository-level shared tooling. It stays deliberately
thin: PerCom-specific *policy* (the double-blind rebuttal process, IEEE Xplore publication,
human-subjects and sensing-dataset expectations) lives in the skills and in
[`../official-source-map.md`](../official-source-map.md); reusable *tooling* lives in the shared
kits so packs do not carry diverging copies.

## Shared kits

- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
  — anonymous-review and public-release checks that transfer to any sensing replication package.
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)
  — dependency-free smoke checker for package layout.
- [`../../../shared-resources/submission-readiness/readiness-checklist.md`](../../../shared-resources/submission-readiness/readiness-checklist.md)
  and [`../../../shared-resources/submission-readiness/response-to-referees.md`](../../../shared-resources/submission-readiness/response-to-referees.md)
  — generic pre-submission and response scaffolding; adapt the latter to the bounded PerCom
  rebuttal in [`../../skills/percom-author-response/SKILL.md`](../../skills/percom-author-response/SKILL.md).

## Typical use for a PerCom package

```bash
# Smoke-check the anonymized sensing artifact before the HotCRP upload
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/percom-artifact-staging
```

Treat the script as a layout smoke test only. Venue policy still comes from the current Call for
Papers and the PerCom skills for experiments, reproducibility, and artifact evaluation.

## PerCom-specific checks the generic tooling cannot make

- **Human subjects and ethics are pinned.** A PerCom sensing dataset comes from real people:
  record the IRB/ethics-approval status, the consent and de-identification procedure, and what was
  removed (faces, voices, GPS, timestamps that re-identify) before the dataset can be released
  (`../../skills/percom-reproducibility/SKILL.md`).
- **Evaluation is cross-subject by default.** The package should regenerate **leave-one-subject-out
  / leave-one-session-out** results, not just a single pooled split, and report **F1 (macro and
  per-class)** on imbalanced activity labels — a script that only reproduces pooled accuracy hides
  the number reviewers care about (`../../skills/percom-experiments/SKILL.md`).
- **The double-blind artifact is anonymous too.** At submission, the dataset link, repository
  owner, sensor-testbed name, and lab-identifying paths must be scrubbed; cite your own prior
  dataset in the third person (`../../skills/percom-submission/SKILL.md`).
- **Sensing provenance is recorded.** Device models and firmware, sampling rates, sensor placement,
  labeling protocol and inter-annotator agreement, and preprocessing (filtering, windowing,
  normalization) must be documented so a reader can size a reproduction and not silently change the
  pipeline (`../../skills/percom-reproducibility/SKILL.md`).
- **Badge readiness is honest and cycle-checked.** Whether PerCom runs a formal reproducibility /
  artifact-evaluation track and which IEEE badges (Open Research Objects / Results Reproduced) it
  grants is **待核实** per edition; a DOI-issuing archive (IEEE DataPort, Zenodo) with an open
  license is the portable minimum (`../../skills/percom-artifact-evaluation/SKILL.md`).

This is not the econometrics/Stata kit used by the journal packs in this repository, and PerCom
evidence is not ML-leaderboard evidence: do not import DiD notebooks or pooled-accuracy leaderboard
framing here.
