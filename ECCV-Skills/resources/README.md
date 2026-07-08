# ECCV Resources

Action-oriented resources behind the ECCV skill pack. The `skills/` directory
advises; this directory lets an agent benchmark against venue-verified ECCV
papers, model an LNCS-format first page, and package supplements and artifacts
for the venue's two-phase (sealed → public) release pattern.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`official-source-map.md`](official-source-map.md) | Trace every 2026-cycle fact to its official URL and access date, see the access-method disclosure, and read the 待核实 list before trusting any deadline. |
| [`external_tools.md`](external_tools.md) | Open the live official surfaces and run the five author-side verification passes (clock, kit, policy, duty, record). |
| [`exemplars/library.md`](exemplars/library.md) | Position against five Springer-verified ECCV papers (COCO, SSD, Perceptual Losses, NeRF, RAFT) and dodge the big-three misattribution traps. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | Study a before → after rewrite of a fictional sparse-view reconstruction paper's first page against the ECCV bar. |
| [`code/README.md`](code/README.md) | Adapt the shared ML-conference reproducibility kit with five ECCV-specific checks (substrate pinning, metric provenance, media anonymity, repo-link ban, two-phase packaging). |

## Scope note

This is a computer-vision conference pack whose venue publishes through
**Springer LNCS with ECVA open-access mirrors** — not through CVF open access,
and not through PMLR. Format advice here assumes the single-column LNCS page
economy; do not import two-column CVF habits or any journal/econometrics kit.

## Suggested workflow

1. Decide the venue bet with
   [`../skills/eccv-topic-selection`](../skills/eccv-topic-selection/SKILL.md)
   and the calendar in [`../skills/eccv-workflow`](../skills/eccv-workflow/SKILL.md).
2. Build evidence with [`../skills/eccv-experiments`](../skills/eccv-experiments/SKILL.md)
   and [`../skills/eccv-reproducibility`](../skills/eccv-reproducibility/SKILL.md),
   packaging via [`code/README.md`](code/README.md).
3. Write against [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md)
   and [`exemplars/library.md`](exemplars/library.md), then verify every
   cycle-specific rule through [`official-source-map.md`](official-source-map.md)
   and [`external_tools.md`](external_tools.md) before upload.
