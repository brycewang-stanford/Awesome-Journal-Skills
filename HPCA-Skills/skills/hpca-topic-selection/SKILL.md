---
name: hpca-topic-selection
description: Use when deciding whether a project is HPCA-shaped or better routed to ISCA, MICRO, ASPLOS, or a systems/theory venue, weighing whether the machine, the mechanism, or the measurement is the contribution, and whether the main track or the HPCA Industry track fits, from the winter seat of the architecture calendar.
---

# HPCA Topic Selection

Use this before committing a project to HPCA. The question is not "is this
architecture?" but "is the contribution a **measured microarchitectural cost met by a
buildable mechanism** whose behavior is shown on a credible instrument?" If yes, HPCA
fits; if the center of gravity is elsewhere, route deliberately.

## The three centers of gravity

Locate where the novelty actually lives:

- **The machine** — a new microarchitecture, structure, or organization is the point.
  Strong HPCA fit when the design is buildable and its behavior is measured.
- **The mechanism** — a control policy, prediction scheme, or protocol that improves
  an existing machine. HPCA fit when a quantified cost motivates it.
- **The measurement** — a characterization that becomes predictive or actionable.
  HPCA fit when the measurement yields a tool, not just an observation.

If the novelty is a pure algorithm with no machine consequence, or a full
language/OS/runtime co-design, HPCA is likely the wrong seat.

## Routing across the architecture year

| Signal | Likely venue |
|---|---|
| Measured cost → buildable mechanism, hardware-grade evaluation, ready by late July | **HPCA** |
| Broad "new idea in architecture," flagship framing, November-ready | ISCA |
| Microarchitecture depth, pipeline/structure focus, spring-ready | MICRO |
| Cross-layer co-design spanning architecture + PL/OS/runtime | ASPLOS |
| Deployed-system evidence rather than a research prototype | **HPCA Industry track** |
| Pure model/algorithm with no machine consequence | a theory or systems venue |

The calendar matters: HPCA's late-July deadline is the last major architecture gate
of the summer, so timing can decide routing as much as topic does. A project that
just missed a spring venue often lands naturally in the HPCA winter cycle.

## Main track vs Industry track

HPCA runs an **Industry track** alongside the main track. Route there when the
contribution is evidence from a *deployed or productized* system — the value is the
real-world measurement and the lessons, not a novel research mechanism. Route to the
main track when a new mechanism or machine is the claim.

## Fit test

Ask, in order:

1. **Is the cost measured?** Can you state the pathology this paper attacks with a
   number, before proposing the fix?
2. **Is the mechanism buildable?** Could a competent architect reimplement it from
   your description, with a stated hardware cost?
3. **Is the behavior shown on a credible instrument?** A cycle-level simulator with a
   declared fidelity scope, validated timing models, or real silicon with captured
   state?
4. **Does the contribution travel?** Would it generalize beyond one workload or one
   configuration?

Two or more "no" answers is a signal to sharpen the framing or re-route.

## Worked routing example

```text
[Project] A confidence-gated filter that suppresses useless irregular prefetches
[Center of gravity] mechanism (motivated by a measured bandwidth-waste cost)
[Cost measured?] yes — useless-traffic fraction on bandwidth-bound phases
[Buildable?] yes — one small table + gating logic, cost stated
[Instrument] cycle-level OoO sim + validated DRAM model
[Route] HPCA main track; if it were a deployed CPU's shipping prefetcher study -> Industry track
```

## Output format

```text
[Center of gravity] machine / mechanism / measurement
[HPCA fit] strong / plausible / weak
[Track] main / industry
[Fit-test failures] <which of the four questions answered "no">
[Recommended venue] HPCA / ISCA / MICRO / ASPLOS / other
[Reasoning] <one or two sentences>
```
