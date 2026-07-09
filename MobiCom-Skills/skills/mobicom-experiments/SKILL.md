---
name: mobicom-experiments
description: Use when designing or auditing the evaluation of a MobiCom submission — building real-device testbeds, choosing RF and channel measurement methodology, injecting realistic mobility and interference, profiling energy on hardware, picking tuned baselines, and reporting distributions so wireless reviewers see where the mechanism wins and breaks.
---

# MobiCom Experiments

MobiCom's evidence culture is physical: a mobile/wireless mechanism is believed when it is
**measured over the air, on real hardware, under conditions that resemble deployment**. A
simulation-only or single-run evaluation reads as under-done here. Design the evaluation as
a set of questions about the mechanism, then build the smallest measurement campaign that
answers them on real radios.

## Questions before measurements

Write the evaluation's subsection titles as questions first — *Does the mechanism hold under
mobility? What does it cost in energy at rest? When does the channel defeat it?* — then
design one experiment per question. The inverted approach (run everything, narrate the
survivors) produces the benchmark tour that MobiCom reviews call unfocused.

A minimal matrix for a wireless-mechanism paper:

| Question | Experiment | Metrics that answer it |
|---|---|---|
| Does it work in the motivating condition? | over-the-air run under the target channel/mobility | delivery rate, goodput, SNR/BER distribution |
| What does it cost when idle? | baseline with no stress | energy-per-bit, power draw, CPU/airtime overhead |
| Why does it work? | component breakdown / ablation | per-mechanism contribution |
| Does it scale? | node / distance / density sweeps | knee location, per-node or per-meter curve |
| When does it break? | interference, deep fades, high mobility | the regime where baselines win |
| Does it hold over time? | multi-hour or multi-day runs | drift, stability, tail behavior |

## Measurement methodology reviewers check

- **State the RF setup completely:** radio/SDR model and firmware, carrier frequency,
  bandwidth, transmit power, antenna and gain, and receiver chain. A number without its
  radio context is not interpretable.
- **Name the channel condition:** distance, line-of-sight vs multipath, ambient
  interference, and how you characterized it (RSSI/CSI traces, coherence time). Do not let
  "in our lab" stand in for a channel description.
- **Make mobility explicit:** walker paths, speeds, and schedules for mobility experiments,
  and a stationary control. "Under mobility" without the traces is unverifiable.
- **Report ground-truth honestly:** how position, gesture, or decode-correctness truth was
  obtained, and its own error, since a sensing result is only as good as its reference.

## Energy is a first-class metric

Battery and harvested-energy claims are common at MobiCom and are held to instrument-level
scrutiny:

```text
Energy report checklist:
  instrument: power monitor / shunt + DAQ, sampling rate
  quantity: energy-per-bit or per-operation, not just average power
  boundary: what is inside the measured envelope (radio only? whole tag?)
  budget: for harvested/batteryless designs, the source and the duty cycle
```

An energy claim that cannot be re-derived from a described measurement setup should not
survive your own audit.

## Baselines on tuned hardware

- Compare against the **incumbent people actually run**, configured the way its own
  documentation prescribes — an untuned baseline is the most common credibility wound in
  systems and wireless reviewing.
- Include the **do-less** baseline: the trivial fix (more power, a fixed high rate, another
  antenna). If the mechanism cannot beat it at equal cost, that is the finding.
- When a competitor cannot be run (proprietary radio, unavailable hardware), reimplement and
  label it a reimplementation, or compare on published numbers with the configuration deltas
  stated.

## Distributions, not superlatives

- Report **percentiles and confidence intervals** for delivery, latency, and throughput
  claims; a single "up to N×" without the distribution behind it is a review risk
  (`mobicom-writing-style`).
- Show **CDFs** for headline results and repeat runs across enough channel realizations,
  days, or walker paths to expose run-to-run spread; state what varies between repeats.
- Wireless results are **time- and place-dependent** — a result from one room at one hour is
  not a claim about the mechanism until the spread is characterized.

## Audit checklist

- [ ] Every evaluation subsection answers a named question.
- [ ] RF setup, channel condition, and mobility fully specified per experiment.
- [ ] Energy measured with a described instrument and boundary, not estimated.
- [ ] Incumbent-grade baseline present and tuned; do-less baseline present.
- [ ] Percentiles + distributions for headline metrics; multi-run spread reported.
- [ ] At least one condition the mechanism does not win, discussed rather than buried.
- [ ] Numbers in abstract/intro regenerate from the recorded runs.
- [ ] A hardware-optional or downscaled variant exists for artifact evaluators
      (`mobicom-artifact-evaluation`).

## Output format

```text
[Evidence form] over-the-air testbed / deployment / trace / simulation (claimed vs actual)
[Question map] question -> experiment -> metric (gaps flagged)
[RF+channel] setup and conditions specified? y/n per headline experiment
[Energy] measured, with instrument and boundary? y/n
[Baseline audit] incumbent tuned? do-less present?
[Break condition] regime where the mechanism loses: <named or MISSING>
[Priority additions] ordered by review-risk reduction per testbed-week
```
