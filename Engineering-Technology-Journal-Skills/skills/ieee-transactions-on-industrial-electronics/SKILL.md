---
name: ieee-transactions-on-industrial-electronics
description: Use when targeting IEEE Transactions on Industrial Electronics (TIE) or deciding whether an industrial-application electronics, drives, or control manuscript fits this venue. Encodes the journal's fit, the experimentally-validated industrial-application bar, hardware-evidence rigor, house style, official-submission re-check, and desk-reject heuristics.
---

# IEEE Transactions on Industrial Electronics (ieee-transactions-on-industrial-electronics)

## Journal positioning

IEEE Transactions on Industrial Electronics (TIE), published by the IEEE
Industrial Electronics Society, is a flagship venue for the **application** of
electronics, control, instrumentation, and computational intelligence to
industrial systems: motor drives and motion control, power-electronics
applications, industrial informatics and communication, mechatronics, fault
diagnosis and condition monitoring, and robotics for industry. The defining
expectation is a concrete advance demonstrated on a real industrial problem and
**validated experimentally**, not a pure theory paper or a converter-topology
study with no system-level industrial framing. Its scope is broader on the
application side than `ieee-transactions-on-power-electronics`, whose center of
gravity is the converter/topology itself. This skill is a **fit /
venue-selection / re-framing** tool. It does not replace the journal's current
official author information. Before submitting, re-check the live IEEE TIE author
guidance and submission system.

## When to trigger

- The author names TIE for a drives, motion-control, industrial-informatics,
  mechatronics, or fault-diagnosis manuscript and wants a fit/framing check.
- A contribution must be re-framed from "we propose a method" into an
  industrial-application advance with experimental hardware evidence.
- The author is choosing between TIE and `ieee-transactions-on-power-electronics`,
  `ieee-transactions-on-automatic-control`, or `ieee-transactions-on-robotics`.
- The author needs TIE's experimental-validation bar and desk-reject heuristics.

## Scope & topic fit

- Motor drives and electrical machines control: field-oriented and
  direct-torque control, sensorless drives, multiphase and fault-tolerant drives.
- Motion control and mechatronics: servo systems, precision positioning,
  vibration suppression, and actuator/sensor integration for industrial machines.
- Power-electronics **applications** at the system level: renewable interfaces,
  grid-tied inverters, EV powertrains — framed by the industrial use, not the topology alone.
- Industrial informatics and the industrial IoT: real-time communication,
  edge/embedded computation, digital twins, and Industry 4.0 system integration.
- Fault diagnosis, prognosis, and condition monitoring of drives, machines, and
  power-electronic systems, with measured or realistically emulated fault data.
- Computational intelligence (learning, fuzzy, evolutionary methods) deployed in
  an industrial control/diagnosis loop, evaluated against an industrial baseline.

## Method & evidence bar

- **Experimental validation is expected**: a hardware prototype, test bench, or
  dSPACE/FPGA real-time implementation; simulation-only papers are a weak fit
  unless the contribution is explicitly a modeling/design framework with a strong rationale.
- Report the experimental setup completely: machine/converter ratings, switching
  frequency, controller hardware, sampling rate, and sensing, so results are reproducible.
- Benchmark against an established industrial method under matched operating
  conditions; quantify the improvement (efficiency, dynamic response, THD, ripple, accuracy).
- Demonstrate robustness to the realities of industrial operation: parameter
  variation, load disturbance, measurement noise, and transients — not only nominal steady state.
- Stability/convergence claims, where made, must be justified; for learning-based
  schemes, address generalization beyond the single rig.
- Position the advance against recent TIE-relevant literature, not a decade-old strawman.

## Structure & house style

- IEEE double-column format; TIE publishes full **Papers** and shorter
  contributions — match the article type to the contribution and re-check current
  definitions and length policy on the live guide.
- The introduction motivates an industrial need and the gap in existing practice,
  then states the contribution; survey-style introductions without a sharp gap are discouraged.
- Figures are load-bearing: control block diagrams, experimental waveforms with
  labeled scales, and comparison plots against the baseline method.
- A clear experimental-results section is central; tables should summarize
  quantitative comparisons under defined operating points.
- Keep the theory proportionate to the application contribution; deep proofs that
  dwarf the industrial result suggest a control-theory venue instead.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the IEEE Author Center
  anchors, then cite the current TIE-specific page you checked.
- Search the live site for "IEEE Transactions on Industrial Electronics information
  for authors" and follow the current ScholarOne/IEEE version.
- Re-check article types, page/length limits and any overlength/mandatory-page
  policy, and the IEEE double-column template.
- Confirm experimental-data, reproducibility, and any video/supplementary-material expectations.
- Re-check ORCID, competing-interests, funding, author-contribution, and AI-use
  disclosure requirements, and IEEE open-access options.
- If the live official instructions conflict with this skill, the official
  instructions win.

## Pre-submission self-check

- [ ] The contribution is an industrial-application advance, not a generic method with no industrial framing.
- [ ] Results are validated on hardware / a real-time platform; the setup is reported reproducibly.
- [ ] The improvement is quantified against an established industrial baseline under matched conditions.
- [ ] Robustness to parameter variation, load/disturbance, and transients is demonstrated.
- [ ] Theory is proportionate to the application; the paper is not a pure-theory submission.
- [ ] Article type and length fit current TIE limits; figures and tables carry the experimental story.

## Common desk-reject triggers

- Pure-theory or simulation-only paper with no experimental validation and no compelling reason.
- A converter-topology or power-stage study with no system-level industrial application framing.
- Incremental tweak to a known control/diagnosis scheme with marginal, unbenchmarked gains.
- A machine-learning paper using an industrial dataset as a label, with no deployment or industrial loop.
- Scope mismatch: control theory, communications, or signal processing with industry only as a keyword.

## Re-routing decision

- Converter topology / power-stage design as the core → `ieee-transactions-on-power-electronics`.
- General control theory with provable guarantees as the contribution → `ieee-transactions-on-automatic-control` / `automatica`.
- Robotics for manipulation/locomotion as the central result → `ieee-transactions-on-robotics`.
- Signal/biosignal processing as the core → `ieee-transactions-on-signal-processing`.
- Antenna/EM or instrumentation-measurement focus → `ieee-transactions-on-antennas-and-propagation` or a measurement venue.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] IEEE Transactions on Industrial Electronics
[Topic tags] <2–3 closest industrial-electronics subtopics>
[Application] <the industrial problem and the advance in one line>
[Method/evidence] <does the experimental validation clear TIE's hardware + benchmark bar?>
[Top risk] <the single most likely reason for rejection>
[Article type] Paper / shorter contribution
[Official items to re-check] <article type / length / template / experimental-data / disclosures>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
