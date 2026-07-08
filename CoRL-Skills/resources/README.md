# CoRL Resources

Action-oriented companions to the twelve `skills/`. The skills carry the venue
methodology; this directory carries the things an agent should *open and use*:
verified sources, verified exemplar papers, a worked rewrite, and the
reproducibility tooling adapter.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`official-source-map.md`](official-source-map.md) | Trace every venue fact in this pack to a URL and a 2026-07-08 access date, see the access-method caveat (corl.org blocked direct fetches; read via search renderings), and get the explicit 待核实 list. |
| [`external_tools.md`](external_tools.md) | Open the live official surfaces and run the five author-side verification passes before any deadline-sensitive step. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against six PMLR-verified CoRL papers (2021–2025, two award anchors) and avoid the RSS/CoRL misattribution traps. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a fictional robot-learning abstract/introduction rebuilt from demo-speak to evidence-scale prose, change by change. |
| [`code/README.md`](code/README.md) | Reach the shared ML-conference repro kit and the robot-specific checks (simulator pins, hardware ledgers, video caps) it cannot perform. |

## Scope note

This is a robot-learning **conference** pack: evaluation-episode statistics,
sim-to-real evidence, supplementary video, OpenReview mechanics, PMLR
camera-ready. Do not import journal-style editor assumptions or the economics
code kits that live elsewhere in this repository — the shared resource for this
pack is the ML-conference methods kit only.

## Suggested route through the pack

1. **Route first**: [`../skills/corl-topic-selection`](../skills/corl-topic-selection/SKILL.md)
   decides whether the project should be here at all; sanity-check the verdict
   against [`exemplars/library.md`](exemplars/library.md).
2. **Design the evidence** while it can still change:
   [`../skills/corl-experiments`](../skills/corl-experiments/SKILL.md) +
   [`../skills/corl-reproducibility`](../skills/corl-reproducibility/SKILL.md) +
   [`code/README.md`](code/README.md).
3. **Write and package**: [`../skills/corl-writing-style`](../skills/corl-writing-style/SKILL.md)
   with the worked example open;
   [`../skills/corl-supplementary`](../skills/corl-supplementary/SKILL.md) for the
   video; [`../skills/corl-submission`](../skills/corl-submission/SKILL.md) as the
   final gate.
4. **Survive the process**: [`../skills/corl-review-process`](../skills/corl-review-process/SKILL.md)
   → [`../skills/corl-author-response`](../skills/corl-author-response/SKILL.md)
   → [`../skills/corl-camera-ready`](../skills/corl-camera-ready/SKILL.md), with
   [`official-source-map.md`](official-source-map.md) re-verified at each date-bearing step.
