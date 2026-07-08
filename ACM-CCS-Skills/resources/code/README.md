# ACM CCS Reproducibility Code Adapter

This directory routes CCS authors to the repository-level ML/CS conference methods kit.
It is deliberately thin: CCS-specific *policy* lives in the skills and in
`../official-source-map.md`; reusable *tooling* lives in the shared kit so that the
conference packs in this repository do not each carry a diverging copy.

## Shared kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

## Typical use for a CCS artifact

```bash
# Smoke-check the artifact package before submitting it to artifact evaluation
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/ccs-artifact-staging
```

## CCS-specific expectations the generic kit will not check

The smoke checker validates package hygiene, not venue policy. On top of it, verify by hand
(or with the skills) the things that are distinctively CCS:

- The 12-page main body must let reviewers judge novelty and soundness on its own; nothing
  decision-critical may live only in an appendix or the artifact (see
  `../../skills/ccs-supplementary/SKILL.md`).
- Artifacts target the ACM badge ladder — Available, Functional, Reusable, Results
  Reproduced — with one documented command per headline result (see
  `../../skills/ccs-artifact-evaluation/SKILL.md`).
- Attacks must name the exact target version and configuration; defenses must include an
  adaptive-attacker evaluation and measured overhead (see
  `../../skills/ccs-experiments/SKILL.md`).
- Dangerous artifacts (working exploits, malware, live tooling) need gating and a
  responsible-disclosure posture consistent with the paper's ethics section.
- Withheld artifacts require a CCS-accepted reason (license, disclosure embargo, subject
  safety) plus a partial, synthetic, or redacted substitute.

This is not the economics/Stata kit used by the journal packs in this repository; do not
import DiD/IV/RDD tooling here.
