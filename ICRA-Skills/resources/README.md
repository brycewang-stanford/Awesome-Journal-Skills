# ICRA Resources

Action-oriented companions to the twelve `skills/`. The skills advise; this
directory lets an agent verify venue facts, benchmark against real ICRA papers,
model the house style on a worked example, and scaffold a robotics artifact.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`official-source-map.md`](official-source-map.md) | Trace every venue fact in the pack to a source URL with an access date, see what remains 待核实, and read the access-method caveat for the `ieee-icra.org` year-sites. |
| [`external_tools.md`](external_tools.md) | Open the live official surfaces (year-site, PaperPlaza, RA-L pages, IEEE Xplore) and run the five pre-upload verification passes. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against five DOI-verified ICRA papers across five topic lanes, and avoid the LOAM/ORB-SLAM/KITTI venue misattributions. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a fictional robotics abstract + introduction rebuilt from demo-speak into the ICRA task-physics-numbers arc, before → after. |
| [`code/README.md`](code/README.md) | Adapt the shared ML-conference reproducibility kit, plus the five robotics-specific checks (claim tiers, hardware ledger, video compliance, media anonymity, ROS pinning) it cannot do. |

## Scope note

This is a robotics conference pack. The evidence culture here is hardware trials,
rosbags, and video attachments — not held-out test sets alone — so use the shared
ML kit only for package hygiene, and let the robotics deltas in `code/README.md`
and the skills carry the venue-specific weight. Nothing in this directory
overrides the current year's official pages.

## Suggested route

1. **Route first**: [`../skills/icra-topic-selection`](../skills/icra-topic-selection/SKILL.md)
   decides direct-ICRA vs the RA-L pathway vs a sibling venue; the exemplars
   library shows what accepted shapes look like per topic lane.
2. **Build evidence early**: [`../skills/icra-experiments`](../skills/icra-experiments/SKILL.md)
   and [`../skills/icra-reproducibility`](../skills/icra-reproducibility/SKILL.md)
   with the code adapter, while banking video footage per
   [`../skills/icra-supplementary`](../skills/icra-supplementary/SKILL.md).
3. **Write to the bar**: [`../skills/icra-writing-style`](../skills/icra-writing-style/SKILL.md)
   against the worked example's after-state.
4. **Verify then upload**: [`official-source-map.md`](official-source-map.md) +
   [`external_tools.md`](external_tools.md), then the full
   [`../skills/icra-submission`](../skills/icra-submission/SKILL.md) audit.
