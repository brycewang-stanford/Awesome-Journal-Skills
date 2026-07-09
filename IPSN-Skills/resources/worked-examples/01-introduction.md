> **Illustrative teaching example.** The paper, dataset, hardware, and every number below are
> **fictional** and exist only to demonstrate IPSN house style. No real-paper facts, deployments, or
> results are stated, and no policy is invented. Corresponding skills:
> [`ipsn-writing-style`](../../skills/ipsn-writing-style/SKILL.md),
> [`ipsn-topic-selection`](../../skills/ipsn-topic-selection/SKILL.md), and
> [`ipsn-experiments`](../../skills/ipsn-experiments/SKILL.md).

# Worked Example: An IPSN-Style Abstract + Introduction (before → after)

This demonstrates the **IPSN first-page arc** from `ipsn-writing-style`:
**real sensing problem → why current sensing/processing is inadequate → contribution (an
information-processing method and/or a platform) → evidence on real hardware with ground truth →
the energy/latency/accuracy budget that makes it deployable.** IPSN expects the "information
processing" to be load-bearing (an estimator, an inference pipeline, an on-device model) and the
evidence to be measured on real sensors, not simulated in the abstract.

The framing also reflects `ipsn-topic-selection`: this is an **IP-track** paper (the contribution is
an on-device inference pipeline and its accuracy/energy trade-off), it lives in the **CPS-IoT Week**
world, and — importantly — it is written to be submitted to IPSN's **successor, SenSys**, since IPSN
no longer runs standalone.

**Illustrative paper (fictional):** *"MicroWake: A Contamination-Aware TinyML Pipeline for
Always-On Acoustic Event Detection on a Microcontroller."* Fictional artifact: a quantized on-device
model plus firmware that detects a target acoustic event within a fixed energy budget on a
battery-powered node.

---

## Before (buries the sensing contribution — typical first-draft abstract + intro)

> **Abstract.** Deep learning has revolutionized audio classification. We design a neural network
> that classifies acoustic events with high accuracy on a large audio dataset and outperforms prior
> models. We deploy it on an embedded device, showing the promise of AI for the Internet of Things.
>
> **Introduction.** Acoustic sensing is important. Many devices now use machine learning. In this
> paper we train a state-of-the-art model and evaluate it on an audio dataset, achieving strong
> accuracy. We then port it to a microcontroller. Section 2 covers related work, Section 3 our
> model, Section 4 experiments, Section 5 the deployment, and Section 6 concludes.

**What's wrong (against `ipsn-writing-style` / `ipsn-topic-selection` / `ipsn-experiments`):**

- **No sensing problem and no physical budget on the first page** — it leads with "deep learning
  revolutionized audio" and an accuracy win, not with a problem an always-on, battery-powered node
  actually faces (energy, latency, memory, false wakeups). IPSN wants the sensing contribution and
  its budget up front.
- **Wrong claim shape.** Offline accuracy on a curated dataset is not evidence that anything works
  on-device under an energy cap; the paper never reports joules per inference, RAM/flash footprint,
  or latency on the actual microcontroller.
- **No ground truth for the deployment.** "We deploy it" with no measured field performance,
  false-alarm rate, or comparison to labeled real audio is a deployment in name only.
- **Model-as-contribution.** If the model were swapped, no sensing lesson would remain — an
  `ipsn-topic-selection` signal that this may be an ML paper wearing a sensing title.
- **No platform detail** — an IP-track sensing paper still owes the reader the MCU, the sensor, the
  sampling regime, and the power measurement setup.
- **Over-signposted roadmap** substituting for an argument, and no artifact/dataset mention a
  double-blind reviewer will look for.

---

## After (IPSN arc — sensing problem → inadequacy → method/platform → real-hardware evidence → budget)

> **Abstract.** Always-on acoustic event detectors must run for months on a coin cell, yet the
> accurate models are trained and evaluated offline, where energy, memory, and false-wakeup cost are
> invisible. We present **MicroWake**, a TinyML pipeline that detects a target acoustic event on a
> Cortex-M microcontroller within a fixed energy budget, combining a quantized front-end with a
> two-stage wake/verify cascade that keeps the expensive stage asleep. On a battery-powered node we
> measure **energy per inference, RAM/flash footprint, and end-to-end latency** on the device
> itself, and evaluate detection against **hand-labeled real field audio** with false-alarm rates
> reported per hour. We isolate the model's contribution with a cascade-off ablation and a
> classical-DSP baseline, and we characterize the accuracy/energy Pareto frontier so a deployer can
> pick an operating point. Firmware, the quantized model, the labeled field recordings, and the
> power-measurement harness are in the artifact. *(sensing problem → inadequacy → method → on-device
> evidence → budget → artifact — all on the first page.)*
>
> **Introduction.** *(¶1 — the sensing problem, first breath.)* The scarcest resource on an
> always-on acoustic node is not accuracy but **energy**: a detector that is 2% more accurate but
> wakes the main processor twice as often may not survive a week in the field. The engineering
> question is therefore not "can a model classify this sound?" but **"can it detect the event within
> a fixed joule budget, on a real microcontroller, without drowning the deployer in false wakeups?"**
>
> *(¶2 — why the current state is inadequate.)* Prior work reports offline accuracy on curated
> corpora and, at best, a one-line "we ported it to an MCU." Neither measures the quantities that
> decide deployability: energy per inference, memory footprint against a few hundred kilobytes of
> RAM, latency under continuous sampling, and the false-alarm rate on messy field audio. Accuracy on
> clean clips is a **proxy**, not the outcome.
>
> *(¶3 — contribution, stated as sensing/information-processing claims.)* We make two contributions.
> First, **MicroWake**, a wake/verify cascade whose cheap first stage gates a more accurate second
> stage, with a quantized front-end sized to the MCU's memory. Second, an **on-device measurement**
> of the accuracy/energy trade-off across operating points, with false-alarm rates on real field
> audio — the evidence a deployer actually needs.
>
> *(¶4 — evidence on real hardware, each claim paired.)* We tie every claim to a measurement on the
> node: energy per inference from an instrumented power rail (Table 1); RAM/flash footprint and
> latency on the MCU (Table 2); detection and false-alarm-per-hour on hand-labeled field audio
> against a classical-DSP baseline and a cascade-off ablation (Fig. 2, Table 3); and the
> accuracy/energy Pareto frontier (Fig. 3). Firmware, model, labeled recordings, and the
> power-measurement harness are in the anonymized artifact.
>
> *(¶5 — the budget and what changes for sensing.)* We state the central threat plainly: field audio
> is site-specific, so we report per-site false-alarm rates and name the environments we did not
> test as an external-validity limit rather than claiming universality. The payoff is concrete: a
> deployer can meet a months-long lifetime at a stated detection/false-alarm operating point.
> Section 2 details the cascade; Section 3 the on-device measurement setup; Section 4 the field
> evaluation; limits are argued alongside each result, not deferred. *(brief roadmap, no
> over-signposting.)*

---

## Why the "after" meets the IPSN bar

Mapped to the skill checklists:

- **Sensing contribution and physical budget on the first page** — the abstract and ¶1 pose an
  energy-bounded always-on detection problem before any model detail (`ipsn-writing-style`: "lead
  with the sensing problem and its budget").
- **Evidence proportional to the claim** — the claim is about on-device deployability, so the
  evidence is energy/memory/latency measured **on the MCU** plus false-alarm rates on real field
  audio, not offline accuracy on clean clips (`ipsn-experiments`: match evidence to the claim shape,
  measure on real hardware with ground truth).
- **The model's marginal value is isolated** — a cascade-off ablation and a classical-DSP baseline
  pre-empt "did the learning actually help?" (`ipsn-experiments`).
- **Right venue and track** — the lesson (a cascade meets a joule budget at a stated operating
  point) survives swapping the model, so it is an IPSN **IP-track** sensing contribution, not an ML
  re-route (`ipsn-topic-selection`); and it is aimed at IPSN's successor, SenSys, at CPS-IoT Week.
- **Artifact by default** — firmware, quantized model, labeled recordings, and the power-measurement
  harness are in an anonymized artifact, matching the double-blind expectation and targeting the
  Best Research Artifact Award (`ipsn-reproducibility`, `ipsn-artifact-evaluation`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified IPSN
> papers** across the IP track, the SPOTS track, and real deployments, and
> [`../official-source-map.md`](../official-source-map.md) for IPSN-lineage policy and the SenSys
> merger.
