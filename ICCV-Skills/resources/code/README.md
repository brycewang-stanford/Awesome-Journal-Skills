# ICCV ML Reproducibility Code Adapter

This directory adapts the repository-level ML-conference methods kit for ICCV work.
It is a pointer, not a copy: the shared kit provides the generic experiment-matrix,
artifact-checklist, and package-smoke-check tooling used across the ML/vision
conference packs.

## Shared kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

```bash
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/anonymous-code-package
```

## ICCV-specific checks the shared kit does not cover

Run these on top of the smoke check, because they encode 2025-cycle ICCV rules
(see [`../official-source-map.md`](../official-source-map.md)):

1. **Same-day readiness** — the code package ships *with* the paper (unified
   paper+supplement deadline since 2025); verify the archive builds and smoke-tests
   on the paper's internal freeze date, not after it.
2. **Repo-citation scan** — the paper and archive must not cite or link your public
   codebase (2025 anonymity rule); grep the PDF text and all README/config files for
   repository URLs and lab-identifying paths.
3. **Media-container metadata** — supplement videos carry author tags more often
   than PDFs; strip container metadata (`ffprobe`/`exiftool` passes are shown in
   [`../../skills/iccv-supplementary/SKILL.md`](../../skills/iccv-supplementary/SKILL.md)).
4. **Foundation-model pins** — checkpoint hashes, verbatim prompts, and vocabulary
   lists are part of the recipe at this venue
   ([`../../skills/iccv-reproducibility/SKILL.md`](../../skills/iccv-reproducibility/SKILL.md)).
5. **Table→command map** — `REPRODUCE.md` mapping each paper table/figure to one
   command; the shared checker verifies structure, not this mapping.

Venue policy always comes from the current official pages, not from this adapter;
the ICCV skills for submission, supplementary material, reproducibility, and
artifact evaluation hold the venue-specific reasoning.
