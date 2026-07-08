# ACL NLP Reproducibility Code Adapter

ACL papers ship their evidence as anonymized OpenReview supplements audited
against the Responsible NLP checklist. Rather than duplicating tooling per
venue, this adapter points at the repository-wide ML conference methods kit —
a lightweight scaffold for experiment matrices, artifact checklists, and a
dependency-free smoke checker. (It is not the econometrics/Stata kit used by
the economics journal packs.)

## Shared Kit

| File | Role for an ACL supplement |
| --- | --- |
| [`README.md`](../../../shared-resources/ml-conference-methods/README.md) | Kit overview and conventions |
| [`experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md) | Plan runs/seeds/configs before results exist |
| [`reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md) | Generic artifact audit to run before the ACL-specific one |
| [`code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py) | Smoke-check the archive you intend to upload |

## Typical Use

```bash
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/anonymous-supplement
```

## What the kit cannot check

NLP-specific gaps stay your job: missing verbatim prompt files, absent model
outputs for re-scoring, undocumented annotator pay and agreement, dataset
license and intended-use statements, and checklist-to-paper consistency.
Those audits live in
[`acl-reproducibility`](../../skills/acl-reproducibility/SKILL.md) and
[`acl-artifact-evaluation`](../../skills/acl-artifact-evaluation/SKILL.md).
Policy questions resolve against
[`../official-source-map.md`](../official-source-map.md) and the live ARR
CFP — never against this kit.
