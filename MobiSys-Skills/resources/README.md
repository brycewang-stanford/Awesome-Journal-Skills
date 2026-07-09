# MobiSys Resources

Action-oriented resources for the MobiSys skill pack. The `skills/` give advice; this
directory lets an agent model a MobiSys-style paper, benchmark against verified exemplars,
and prepare on-device reproducibility artifacts without importing the econometrics code kit.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for an on-device mobile-systems paper. Illustrative fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, metadata-verified MobiSys papers and avoid MobiCom/SenSys/OSDI misattribution. |
| [`official-source-map.md`](official-source-map.md) | Confirm current-cycle MobiSys submission, review, formatting, artifact, and organizer sources before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open official venue systems, HotCRP, proceedings, and organizer links, and run the per-cycle verification passes. |
| [`code/README.md`](code/README.md) | Use the shared ML-conference reproducibility kit plus MobiSys-only checks (device provenance, energy boundary, hardware-optional smoke run). This is not the econometrics code kit. |

## Scope note

This is a mobile-systems conference pack, not an empirical-economics journal pack. Do not copy
the Stata/DiD/IV/RDD econometrics kit here. Use the shared ML-conference resource for
experiment design, artifact packaging, seed/compute reporting, and anonymous-review package
checks, then add the MobiSys-specific device, energy, latency, and thermal checks the generic
tooling cannot make.

## Suggested workflow

1. Route and frame with
   [`../skills/mobisys-topic-selection`](../skills/mobisys-topic-selection/SKILL.md) and
   [`../skills/mobisys-writing-style`](../skills/mobisys-writing-style/SKILL.md).
2. Stress-test evidence with
   [`../skills/mobisys-experiments`](../skills/mobisys-experiments/SKILL.md),
   [`../skills/mobisys-reproducibility`](../skills/mobisys-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm current
   official rules in [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md).
