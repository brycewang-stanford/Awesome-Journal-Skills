---
name: sensys-reproducibility
description: Use when making a SenSys result reproducible across a different testbed — capturing energy-measurement method, hardware and firmware provenance, sensor ground-truth protocol, and deployment conditions while the testbed is still live, and deciding early which traces and firmware can legally and safely ship.
---

# SenSys Reproducibility

A SenSys result is reproducible when someone on **different hardware** can understand — and, from
your traces, re-obtain — your numbers. The threat is not messy code; it is **provenance that
evaporates when the deployment ends**. Energy measured without its method, accuracy scored
against forgotten ground truth, and firmware whose toolchain is unrecorded cannot be reproduced
at any price once the testbed is torn down. Capture it while the nodes are still powered.

## Capture it live, not later

| Provenance | Capture while live | Why it cannot be reconstructed |
|---|---|---|
| **Energy method** | Instrument model, sampling rate, integration boundaries, sleep floor | A stored current number loses its method; "42 µA" of what phases? |
| **Hardware** | MCU/SoC part + clock, sensor config, radio + TX power, board revision, battery/harvester spec | A later "same board" is rarely bit-identical |
| **Firmware** | Sources + toolchain version + compiler flags, pinned | A rebuild on a new toolchain shifts timing and energy |
| **Ground truth** | Reference protocol + the reference's own error | Labels without their protocol are unfalsifiable |
| **Deployment** | Placement, environment, duration, node uptime/failures | Conditions are gone once the deployment ends |
| **Harvest input** | Energy-source trace (light/RF/vibration), buffer sizing | Behavior across brownouts is unreproducible without the input |

## The reproducibility that matters is cross-hardware

Reproducing your own result on your own testbed proves little. The SenSys bar is that a
**different lab** can interpret a mismatch: when their number differs from yours, the provenance
tells them *why* (different MCU clock, different harvest input) rather than leaving them to guess.
Ship **recorded traces** so the analysis can be re-run even by someone who lacks your hardware —
this is what turns a deployment result into a reproducible one and underpins the trace-replay
path in `sensys-artifact-evaluation`.

```text
Minimum reproducible bundle for a SenSys figure:
  traces/fig4_power.csv        # raw power samples + timestamps
  traces/fig4_sensor.csv       # the sensor stream behind the same figure
  analysis/reproduce_fig4.py   # regenerates Fig. 4 from the two traces
  ENERGY.md                    # instrument, rate, integration boundaries
  HARDWARE.md                  # part numbers, clocks, board rev, harvester spec
  firmware/ + toolchain.lock   # pinned build that produced the traces
```

## Decide early what can ship

Some SenSys artifacts carry release constraints that a purely computational paper never faces:

- **Sensor data of people or spaces** may need consent, anonymization, or aggregation before it
  can be released — decide at collection time, because retroactive consent is usually impossible.
- **Firmware and hardware designs** may touch third-party IP or a vendor NDA; confirm what is
  releasable before promising an Available badge.
- **Deployment locations** can be sensitive (critical infrastructure, private property); scrub
  identifying detail from released traces.

Resolving these late forces a choice between a weak artifact and a broken promise. Resolve them in
the experiment plan (`sensys-experiments`).

## Reproducibility checklist

```text
[ ] Energy method (instrument, rate, boundaries) recorded, not just the number.
[ ] Hardware provenance: parts, clocks, board revision, battery/harvester spec.
[ ] Firmware sources + pinned toolchain + compiler flags archived.
[ ] Ground-truth protocol and the reference's own error documented.
[ ] Deployment conditions + honest uptime/failure log captured while live.
[ ] Harvest-input traces + buffer sizing stored for batteryless results.
[ ] Recorded traces shipped so figures re-generate without your hardware.
[ ] Release constraints (consent, NDA, location) resolved at collection time.
```

## Output format

```text
[Live-capture] which provenance is captured vs. still at risk while the testbed runs
[Cross-HW]     can a different lab interpret a mismatch from what you shipped? Y/N
[Traces]       do shipped traces regenerate the headline figures without hardware? Y/N
[Release]      consent/NDA/location constraints resolved? open items
[Open]         the provenance whose loss would most damage reproducibility
```
