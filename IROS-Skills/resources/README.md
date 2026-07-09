# IROS Resources

Action-oriented resources for the IROS skill pack. The `skills/` give advice; this directory lets an
agent model an IROS-style paper, benchmark against verified exemplars, and prepare embodied-evidence
artifacts without importing an ML-benchmark or econometrics kit.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for an intelligent-robots-and-systems paper. Illustrative fictional system; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, DOI-verified IROS papers and avoid sibling-venue confusion with ICRA, RSS, and CoRL. |
| [`official-source-map.md`](official-source-map.md) | Confirm current-cycle IROS submission, review, video, and camera-ready sources before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open official venue surfaces and run the five author-side verification passes (geometry, anonymity, video, evidence, timing). |
| [`code/README.md`](code/README.md) | Use the shared ML-conference reproducibility kit as a scaffold, plus the robotics-specific checks it cannot make. |

## Scope note

This is an embodied-robotics conference pack, not an ML-benchmark or empirical-economics pack. The
contribution IROS rewards is a working intelligent system with credible robot evidence — hardware,
task distributions, trials, resets, failure taxonomies, and honest sim-to-real deltas. Use the shared
kit for repository scaffolding and seed/compute reporting, but read the robotics checks in
`code/README.md`, because a green reproducibility script does not prove a robot did anything.

## Suggested workflow

1. Route and frame with
   [`../skills/iros-topic-selection`](../skills/iros-topic-selection/SKILL.md) and
   [`../skills/iros-writing-style`](../skills/iros-writing-style/SKILL.md).
2. Stress-test evidence with [`../skills/iros-experiments`](../skills/iros-experiments/SKILL.md),
   [`../skills/iros-reproducibility`](../skills/iros-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md); bank video footage as you go per
   [`../skills/iros-supplementary`](../skills/iros-supplementary/SKILL.md).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm current official
   rules in [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) before the PaperPlaza upload.
