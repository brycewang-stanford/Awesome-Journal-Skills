---
name: sensys-topic-selection
description: Use when deciding whether a project belongs at SenSys after the 2026 merger absorbed IPSN and IoTDI — testing whether the contribution is a built, measured sensing/embedded/IoT/on-device-AI system rather than a pure algorithm, a mobile-networking mechanism, or an offline ML result, and routing misfits to MobiCom, MobiSys, or an ML/DSP venue.
---

# SenSys Topic Selection

SenSys accepts a **system you built and measured under embedded constraints**. The 2026 merger
of SenSys, IPSN, and IoTDI widened the mandate — low-power networked sensing, embedded systems,
IoT, and on-device AI now share one venue — but it did not soften the systems bar: a strong
SenSys paper still has a **buildable mechanism** whose value is shown in **energy, latency,
memory, and deployment behavior on real hardware**, not in a proof or a leaderboard delta.

## The fit test

Ask these in order; a "no" is a routing signal, not a verdict on the work's quality.

1. **Is there a system?** Can you point to the artifact — firmware, a node, a protocol, a
   deployment — that embodies the contribution? A pure algorithm with no embedded realization
   is a signal-processing or ML contribution.
2. **Do embedded constraints bind?** Does energy, memory, compute, bandwidth, or intermittent
   power actually shape the design? If the method would run unchanged on a workstation, the
   constraint is not doing work and SenSys is a weak fit.
3. **Is the evidence physical?** Are the headline numbers **measured on hardware** — current
   draw, duty cycle, on-device latency, deployment uptime — or are they simulation/offline
   accuracy? SenSys reviewers discount simulation-only and single-run results.
4. **Is sensing or embedded computation central?** SenSys is about turning **physical signals
   into information under resource limits**, or computing on constrained nodes — not about the
   wireless link itself (that is MobiCom) or the mobile application platform (that is MobiSys).

## Routing table

| If the core contribution is... | The likely home is... | Because |
|---|---|---|
| A built sensing system measured on real hardware for energy/latency/accuracy | **SenSys** | The merged venue's center of mass |
| Low-power networked sensing / mote-class protocols (formerly IPSN) | **SenSys** (post-merger) | IPSN's community joined SenSys in 2026 |
| IoT design/implementation, edge deployments (formerly IoTDI) | **SenSys** (post-merger) | IoTDI's community joined SenSys in 2026 |
| An on-device / TinyML model with measured footprint on an MCU | **SenSys** | Embedded-AI systems are in-scope after the merger |
| A wireless link, PHY/MAC, or over-the-air networking mechanism | **MobiCom** | The mechanism is the radio, not the sensing system |
| A mobile-platform / smartphone systems contribution | **MobiSys** | The platform, not embedded sensing under energy limits |
| A new estimator/algorithm with no embedded realization | **an ML or DSP venue** | The contribution is the math, not a built system |
| A datacenter/OS/networking systems result | **NSDI / OSDI / SIGCOMM** | Not sensing/embedded and not energy-bound |

## Post-merger boundary calls

The merger creates new adjacencies to reason about explicitly:

- **On-device AI vs. an ML paper.** If the novelty is model *architecture or accuracy*, it is an
  ML venue. If the novelty is **running inference within a real MCU's RAM/flash/energy budget**
  — quantization-for-hardware, intermittent-power inference, on-sensor compute — it is SenSys.
- **IoT deployment vs. an applications paper.** A deployment is SenSys when the **system design
  or measurement methodology** is the contribution, not merely that a known stack was installed.
- **Sensing vs. signal processing.** A new algorithm belongs at a DSP venue unless it is
  **embodied and measured on the constrained node** where it must actually run.

```text
Fit self-check (answer before choosing SenSys):
[ ] There is a concrete built system/artifact, not only a method.
[ ] An embedded constraint (energy/memory/compute/power) shapes the design.
[ ] Headline numbers are measured on real hardware, not simulation-only.
[ ] Sensing or on-node computation — not the radio or the app platform — is central.
[ ] If on-device AI: the claim is measured footprint/latency, not offline accuracy.
```

## When two venues both fit

Some work genuinely spans SenSys and MobiCom (e.g. a sensing system that also innovates on its
link). Route by **where the reviewable novelty lives**: if a reviewer would spend most of their
judgment on the sensing/embedded system and its energy behavior, submit to SenSys and treat the
link as engineering; if the defensible novelty is the wireless mechanism, submit to MobiCom.
Pick one — a paper straddling both usually reads as under-contributing to each.

## Output format

```text
[Verdict]  SenSys fit: strong / plausible / weak
[System]   the concrete artifact that embodies the contribution
[Constraint] which embedded limit binds the design (energy/memory/compute/power)
[Evidence] hardware-measured? or simulation/offline (a re-route risk)
[Reroute]  if weak — target venue + the one sentence that would move it
[Open]     any post-merger boundary ambiguity to resolve before committing
```
