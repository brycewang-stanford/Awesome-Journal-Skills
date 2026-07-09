# IEEE VIS Replication-Package Code Adapter

This directory routes IEEE VIS authors to the repository-level shared tooling. It stays deliberately
thin: VIS-specific *policy* (the journal-integrated TVCG process, the two-phase conditional-accept
review, the Graphics Replicability Stamp, Open Practices, author-optional double-blind) lives in the
skills and in [`../official-source-map.md`](../official-source-map.md); reusable *tooling* lives in
the shared kits so packs do not carry diverging copies.

## Shared kits

- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
  — anonymous-review and public-release checks that transfer to any visualization supplemental
  package.
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)
  — dependency-free smoke checker for package layout.
- [`../../../shared-resources/submission-readiness/readiness-checklist.md`](../../../shared-resources/submission-readiness/readiness-checklist.md)
  and [`../../../shared-resources/submission-readiness/response-to-referees.md`](../../../shared-resources/submission-readiness/response-to-referees.md)
  — generic pre-submission and response scaffolding; adapt the latter to the conditional-accept
  summary-of-changes in [`../../skills/vis-author-response/SKILL.md`](../../skills/vis-author-response/SKILL.md).

## Typical use for a VIS package

```bash
# Smoke-check the anonymized supplemental archive before the PCS upload
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/vis-supplemental-staging
```

Treat the script as a layout smoke test only. Venue policy still comes from the current Call for Full
Papers and the VIS skills for experiments, reproducibility, and artifact/Replicability-Stamp work.

## VIS-specific checks the generic tooling cannot make

- **The supplemental video is a first-class deliverable.** Many VIS contributions (systems,
  interaction techniques) are judged by the video; check it plays, shows the real interaction, and —
  if double-blind — carries no affiliation slate, spoken name, visible username, or watermarked URL
  (`../../skills/vis-supplementary/SKILL.md`).
- **Encodings are justified by task, and colors are CVD-safe.** A layout smoke test cannot see
  whether a channel matches its task or whether a palette is colorblind-safe and grayscale-legible —
  that judgment lives in `../../skills/vis-experiments/SKILL.md` and `../../skills/vis-writing-style/SKILL.md`.
- **Figures regenerate from logged data.** For the Graphics Replicability Stamp, an independent
  volunteer must reproduce your figures/results from the public archive; provide a figure-to-script
  mapping, seeds/tolerances for GPU or stochastic output, and a one-command build
  (`../../skills/vis-artifact-evaluation/SKILL.md`).
- **Open Practices and preregistration are disclosed honestly.** The camera-ready form collects
  preprint/preregistration/open-data-and-code status; a study preregistration (e.g. on OSF) should
  be cited and its deviations reported (`../../skills/vis-reproducibility/SKILL.md`).

This is not the econometrics/Stata kit used by the journal packs in this repository, and VIS evidence
is not an ML leaderboard: do not import DiD notebooks or benchmark-accuracy framing here — VIS
evidence is task-justified encodings, controlled and perceptual studies, and reproducible figures.
