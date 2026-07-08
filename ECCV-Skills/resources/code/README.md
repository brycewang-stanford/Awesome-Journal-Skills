# ECCV Vision Reproducibility Code Adapter

This directory routes ECCV authors to the repo-level ML conference methods kit
and adds the checks that matter specifically for a vision submission headed to
Springer LNCS proceedings. It is not an econometrics code library.

## Shared Kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

## Typical Use

```bash
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/anonymous-supplement
```

Run it against the archive you intend to upload in the supplement week (the
trailing deadline one week after the paper — see
[`../../skills/eccv-supplementary/SKILL.md`](../../skills/eccv-supplementary/SKILL.md)).

## Five ECCV-specific checks the generic kit does not cover

1. **Substrate pinning** — every pretrained backbone, VLM, or SAM-style
   component named with an exact checkpoint identity and hash
   (`eccv-reproducibility`); "CLIP features" is not a config.
2. **Metric provenance** — evaluation scripts must name the reference
   implementation of each metric (mAP/mIoU/FID variants differ); a nonstandard
   metric is the artifact failure vision reviewers report most.
3. **Media anonymity** — video files, screenshots, and qualitative PDFs leak
   identity through watermarks and metadata channels code archives do not have
   (`eccv-supplementary` scrub list).
4. **Repo-link ban** — the submission PDF must not cite the authors' own public
   codebase under ECCV 2026 policy; the anonymous archive is the only
   review-time code channel.
5. **Two-phase plan** — the sealed review archive and the June-to-September
   public release are different deliverables with different rules
   (`eccv-artifact-evaluation`); keep one build script able to produce both.

Venue policy always comes from the live pages mapped in
[`../official-source-map.md`](../official-source-map.md), never from this
directory.
