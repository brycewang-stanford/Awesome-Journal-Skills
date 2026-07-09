# MobiCom Resources

Working materials that back the `skills/` directory: verified sources, real exemplar
papers, a style rewrite, and a reproducibility adapter. The skills tell an agent what to
do; these files hold the evidence and the checkable references for a mobile/wireless-
networking submission.

## Contents

| Resource | Use it to... |
| --- | --- |
| [`official-source-map.md`](official-source-map.md) | Trace every venue fact in the pack to a dated official URL, read the access-method note (sigmobile.org, hotcrp.com, and dblp.org all 403'd direct fetches), and see the explicit 待核实 list. |
| [`external_tools.md`](external_tools.md) | Open the live MobiCom surfaces (CFP, HotCRP `/deadlines`, artifact call) and run the five author-side verification passes. |
| [`exemplars/library.md`](exemplars/library.md) | Position against five venue-verified MobiCom papers (2000-2013) and dodge the RADAR/XORs/WiSee-demo misattribution traps across INFOCOM, SIGCOMM, and NSDI. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | Watch a fictional backscatter-link paper's abstract and introduction get rebuilt into the MobiCom measured-evidence arc. |
| [`code/README.md`](code/README.md) | Reach the shared reproducibility kit and see which MobiCom-specific artifact properties (radio provenance, channel conditions, energy) it cannot check. |

## Scope note

This is a mobile-computing and wireless-networking conference pack. Evidence here means
over-the-air measurement, real-device testbeds, channel and mobility conditions, and
energy — not regression tables and not simulation alone. Do not import econometrics tooling
from the journal packs; the shared ML/systems kit under `shared-resources/` is the right
base, with the MobiCom-specific gaps listed in [`code/README.md`](code/README.md).

## A suggested route through the pack

1. **Fit first:** [`../skills/mobicom-topic-selection`](../skills/mobicom-topic-selection/SKILL.md)
   against the CFP scope and the MobiSys/SenSys/SIGCOMM/NSDI/WiSec routing map, then compare
   your plan with [`exemplars/library.md`](exemplars/library.md).
2. **Calendar next:** [`../skills/mobicom-workflow`](../skills/mobicom-workflow/SKILL.md) —
   the summer/winter pair decides which edition you are writing for and whether the radio
   experiments fit before the round closes.
3. **Build the evidence:** [`../skills/mobicom-experiments`](../skills/mobicom-experiments/SKILL.md)
   plus [`../skills/mobicom-reproducibility`](../skills/mobicom-reproducibility/SKILL.md)
   and the [`code/README.md`](code/README.md) adapter while the testbed is still up.
4. **Write and audit:** [`../skills/mobicom-writing-style`](../skills/mobicom-writing-style/SKILL.md)
   with [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md), then
   [`../skills/mobicom-submission`](../skills/mobicom-submission/SKILL.md) against
   [`external_tools.md`](external_tools.md) before upload.
5. **After the notification:** [`../skills/mobicom-author-response`](../skills/mobicom-author-response/SKILL.md)
   for the rebuttal or the one-shot revision;
   [`../skills/mobicom-artifact-evaluation`](../skills/mobicom-artifact-evaluation/SKILL.md)
   and [`../skills/mobicom-camera-ready`](../skills/mobicom-camera-ready/SKILL.md) if the
   letter says accept.
