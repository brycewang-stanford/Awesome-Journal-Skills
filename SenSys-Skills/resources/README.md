# SenSys Resources

Action-oriented resources for the SenSys skill pack. The `skills/` give judgment; this
directory lets an agent model a SenSys-shaped paper, benchmark against venue-verified
exemplars, and prepare a real-testbed artifact — without dragging in the economics or generic
ML kits that do not speak to embedded and sensing evidence.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`official-source-map.md`](official-source-map.md) | Confirm current-cycle SenSys identity, the two-deadline model, format, anonymity, and artifact rules — with the access-method note (why direct fetches 403'd) and the 待核实 register — before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open the live CFP, the per-edition HotCRP site, and the artifact system, then run the five author-side verification passes (round/clock, format, blindness, resubmission, artifact/deployment). |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, dblp-verified SenSys papers (Test-of-Time roll) and avoid mis-attributing MobiCom/NSDI/IPSN canon to SenSys. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite in SenSys house style for a low-power sensing / on-device-inference paper. Illustrative fictional paper; no policy invented. |
| [`code/README.md`](code/README.md) | Reach the shared reproducibility kit and the SenSys-specific checks (energy accounting, hardware provenance, sensor ground truth, on-device model footprint) the generic tooling cannot make. |

## Scope note

This is a **sensing / embedded-AI systems** pack for the merged SenSys venue, not an ML-theory
or empirical-economics pack. Do not import the Stata/DiD/IV/RDD econometrics kit, and do not
treat a benchmark accuracy table as sufficient evidence: at SenSys the currency is **measured
system behavior on real hardware** — energy per operation, duty cycle, on-device latency and
memory, deployment longevity, and sensor ground truth — read against the paper's claims.

## Suggested workflow

1. **Route and frame** with [`../skills/sensys-topic-selection`](../skills/sensys-topic-selection/SKILL.md)
   (is this SenSys after the merger, or MobiCom/MobiSys/a signal-processing venue?) and
   [`../skills/sensys-writing-style`](../skills/sensys-writing-style/SKILL.md) against the
   worked example.
2. **Build the evidence** with [`../skills/sensys-experiments`](../skills/sensys-experiments/SKILL.md)
   and [`../skills/sensys-reproducibility`](../skills/sensys-reproducibility/SKILL.md) plus
   [`code/README.md`](code/README.md) — energy, testbed, and ground-truth traces cannot be
   reconstructed after the deployment ends.
3. **Benchmark** against [`exemplars/library.md`](exemplars/library.md), then confirm the live
   rules in [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) before the HotCRP upload.
