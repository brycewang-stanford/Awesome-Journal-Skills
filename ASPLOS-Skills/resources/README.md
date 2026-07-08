# ASPLOS Resources

Action-oriented companions to the `skills/` directory. The skills give per-stage
advice; these files let an agent verify current-cycle ASPLOS mechanics, benchmark a
draft against award-validated exemplars, rehearse the two-page rapid-review test, and
package hardware-dependent artifacts.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`official-source-map.md`](official-source-map.md) | Trace every venue fact in this pack to an official URL with a 2026-07-08 access date, see the explicit 待核实 list, and read the access-method note about the blocked gateway. |
| [`external_tools.md`](external_tools.md) | Open the live CFP/HotCRP/AE surfaces and run five author-side verification passes before upload. |
| [`exemplars/library.md`](exemplars/library.md) | Study five Influential-Paper-Award-verified ASPLOS papers as contribution *shapes* (accelerator, scheduler, boundary redraw, workload study, runtime), each with a self-check question. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a fictional abstract + introduction rebuilt to survive the first-two-pages rapid review, before → after. |
| [`code/README.md`](code/README.md) | Adapt the shared conference reproducibility kit, plus the four hardware-shaped checks (simulator pinning, hardware dependencies, kernel/firmware state, badge mapping) the generic tooling skips. |

## Scope note

This is a systems-conference pack whose evaluation culture is *hardware-grade*:
simulators with stated accuracy limits, real silicon with pinned firmware, FPGA
prototypes with reported utilization. Do not import statistical-ML checklist habits
(seeds-and-error-bars alone) as if they were sufficient here, and do not import
econometrics tooling at all.

## Suggested route

1. **Fit first** — [`../skills/asplos-topic-selection`](../skills/asplos-topic-selection/SKILL.md)
   against the five exemplar shapes; if the project belongs at ISCA, PLDI, or SOSP,
   stop before formatting anything.
2. **Design the evidence** — [`../skills/asplos-experiments`](../skills/asplos-experiments/SKILL.md)
   and [`../skills/asplos-reproducibility`](../skills/asplos-reproducibility/SKILL.md)
   with [`code/README.md`](code/README.md) open beside the build.
3. **Write for the screen** — [`../skills/asplos-writing-style`](../skills/asplos-writing-style/SKILL.md)
   plus the worked example; the first two pages are the submission's survival organ.
4. **Verify, then upload** — [`external_tools.md`](external_tools.md) passes, then
   [`../skills/asplos-submission`](../skills/asplos-submission/SKILL.md) end to end.
5. **After the decision** — [`../skills/asplos-author-response`](../skills/asplos-author-response/SKILL.md)
   during the response window, then either the Major Revision path in
   [`../skills/asplos-review-process`](../skills/asplos-review-process/SKILL.md) or
   [`../skills/asplos-camera-ready`](../skills/asplos-camera-ready/SKILL.md) and
   [`../skills/asplos-artifact-evaluation`](../skills/asplos-artifact-evaluation/SKILL.md).
