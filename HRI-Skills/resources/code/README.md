# HRI Study-Materials & Replication Adapter

This directory routes HRI authors to the repository-level shared tooling. It stays deliberately
thin: HRI-specific *policy* (the five-track model, two-phase double-blind review, human-subjects
ethics, the video figure, the honest limits of reproducing an embodied study) lives in the skills
and in [`../official-source-map.md`](../official-source-map.md); reusable *tooling* lives in the
shared kits so packs do not carry diverging copies.

## Shared kits

- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
  — anonymous-review and public-release checks that transfer to any code/data artifact.
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)
  — dependency-free smoke checker for package layout.
- [`../../../shared-resources/empirical-methods/reporting-standards.md`](../../../shared-resources/empirical-methods/reporting-standards.md)
  and [`../../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md)
  — reporting and objection scaffolding for human-subjects statistics; pair with
  [`../../skills/hri-experiments/SKILL.md`](../../skills/hri-experiments/SKILL.md).
- [`../../../shared-resources/submission-readiness/response-to-referees.md`](../../../shared-resources/submission-readiness/response-to-referees.md)
  — generic response scaffolding; adapt it to the single HRI **rebuttal** in
  [`../../skills/hri-author-response/SKILL.md`](../../skills/hri-author-response/SKILL.md).

## Typical use for an HRI package

```bash
# Smoke-check the anonymized artifact (code + de-identified data + study materials) before PCS upload
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/hri-artifact-staging
```

Treat the script as a layout smoke test only. Venue policy still comes from the current full-papers
call and the HRI skills for experiments, reproducibility, supplementary/video, and submission.

## HRI-specific checks the generic tooling cannot make

- **The video and de-identified data are anonymized too.** Double-blind extends past the PDF: the
  **video** must not show faces, hearable participant/experimenter voices, or lab logos at review
  time, and de-identified data must not carry re-identifying free text
  (`../../skills/hri-supplementary/SKILL.md`).
- **Human-subjects governance is documented.** IRB/ethics approval (or an explicit exemption
  rationale), an informed-consent summary, and any deception/debriefing protocol are part of the
  package, not an afterthought — HRI binds authors to ACM's human-participants policy
  (`../../skills/hri-experiments/SKILL.md`).
- **The robot behavior is specified, not just described.** For a Wizard-of-Oz study, log the
  wizard's control mapping, what was and was not autonomous, and error rates; for an autonomous
  condition, pin the software version and parameters so the *stimulus* is reproducible even when the
  human data are not (`../../skills/hri-reproducibility/SKILL.md`).
- **Reproducibility has honest limits.** An embodied human study cannot be "re-run" like a
  benchmark: the reusable artifact is the **study materials, analysis code, de-identified data, and
  robot-behavior specs** that let another team *replicate the procedure*, and the paper should say
  so plainly rather than overclaim (`../../skills/hri-reproducibility/SKILL.md`,
  `../../skills/hri-artifact-evaluation/SKILL.md`).

This is not the econometrics/Stata kit used by the journal packs in this repository, and HRI
evidence is not ML-leaderboard evidence: do not import DiD notebooks or benchmark-score framing
here. HRI's currency is a credible human-subjects study of an embodied robot.
