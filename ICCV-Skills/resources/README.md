# ICCV Resources

Working materials behind the ICCV skill pack. The `skills/` directory carries the
advice; this directory carries what the advice stands on — the verified source trail,
real exemplars with venue verification, a fictional first-page rewrite, and the
reproducibility tooling adapter.

## Contents

| Resource | What it is for |
| --- | --- |
| [`official-source-map.md`](official-source-map.md) | The 14-source verification trail: 2025-cycle facts with URLs and access dates, the access-method disclosure (iccv.thecvf.com was not directly fetchable), the reported-facts list, and everything 待核实 — including the entire ICCV 2027 process. |
| [`external_tools.md`](external_tools.md) | Live official surfaces plus the five author-side verification passes (cycle, format, people, anonymity, attribution). |
| [`exemplars/library.md`](exemplars/library.md) | Seven venue-verified ICCV papers arranged as an era-by-era time-lapse (SIFT 1999 → BrickGPT 2025), each with a self-check question, plus the big-three misattribution guard list. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | A fictional 3D-reconstruction paper's abstract and introduction rebuilt to ICCV first-page standards, before → after, with a transfer checklist. |
| [`code/README.md`](code/README.md) | Adapter to the shared ML-conference reproducibility kit plus the five ICCV-only checks (same-day readiness, repo-citation scan, media metadata, foundation-model pins, table→command map). |

## Scope note

This is a computer-vision conference pack. It deliberately reuses the repo's shared
ML-conference tooling rather than duplicating it, and it contains no journal-style
or econometrics material. Facts about ICCV mechanics are 2025-cycle anchors —
biennial venues go stale in two-year steps, so the source map's 待核实 section is as
load-bearing as its verified section.

## A sensible route through the pack

1. **Decide** with [`../skills/iccv-topic-selection`](../skills/iccv-topic-selection/SKILL.md)
   and calendar it with [`../skills/iccv-workflow`](../skills/iccv-workflow/SKILL.md);
   sanity-check the venue's taste against [`exemplars/library.md`](exemplars/library.md).
2. **Build evidence** with [`../skills/iccv-experiments`](../skills/iccv-experiments/SKILL.md)
   and [`../skills/iccv-reproducibility`](../skills/iccv-reproducibility/SKILL.md),
   packaging via [`code/README.md`](code/README.md).
3. **Write** with [`../skills/iccv-writing-style`](../skills/iccv-writing-style/SKILL.md)
   and [`../skills/iccv-related-work`](../skills/iccv-related-work/SKILL.md), using
   [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) as the
   calibration example.
4. **Ship and defend** with the submission, supplementary, review-process,
   author-response, and camera-ready skills — after reopening the live pages listed
   in [`external_tools.md`](external_tools.md).
