> **Illustrative teaching example.** The paper, system, numbers, and device below are
> **fictional** and exist only to demonstrate MobiSys house style. No real-paper facts,
> measurements, or results are stated, and no policy is invented. Corresponding skills:
> [`mobisys-writing-style`](../../skills/mobisys-writing-style/SKILL.md),
> [`mobisys-topic-selection`](../../skills/mobisys-topic-selection/SKILL.md), and
> [`mobisys-experiments`](../../skills/mobisys-experiments/SKILL.md).

# Worked Example: A MobiSys-Style Abstract + Introduction (before → after)

This demonstrates the **MobiSys first-page arc** from `mobisys-writing-style`:
**mobile pain → why current systems fail on the device → the system mechanism → on-device
evidence → why it matters as a deployable mobile service** — with the MobiSys rules that the
contribution is a *system that runs on real hardware*, that evidence is measured in latency,
energy, and memory, and that no claim outruns its measurement.

The framing also reflects `mobisys-topic-selection`: MobiSys is strongest when the
**behavior of a system on the device** is the contribution — here, a runtime that keeps
on-device inference within a latency-and-energy budget, not a new network architecture (which
would route to a machine-learning venue) and not a wireless mechanism (which would route to
MobiCom).

**Illustrative paper (fictional):** *"Thermenon: A Thermal-Aware Runtime for Sustained
On-Device Video Inference on Commodity Phones."* Fictional system: a scheduler that keeps a
CNN's frame-rate stable as the phone heats up, by trading model variants against the thermal
budget.

---

## Before (buries the contribution — typical first-draft abstract + intro)

> **Abstract.** Deep learning has transformed mobile computing. In this work we study video
> inference on smartphones, an important problem. We propose a new system that combines model
> optimization with scheduling and achieves strong performance on several phones, outperforming
> prior approaches in most settings.
>
> **Introduction.** On-device inference has been studied extensively. Many approaches exist,
> including quantization, pruning, and GPU offload. In this paper, we build a runtime that
> selects models and schedules inference to run efficiently on mobile devices. We evaluate on
> standard workloads and show our system works well. Section 2 reviews related work, Section 3
> describes the system, Section 4 presents experiments, and Section 5 concludes.

**What's wrong (against `mobisys-writing-style` / `mobisys-topic-selection` /
`mobisys-experiments`):**

- **No mobile-system contribution on the first page** — leads with "deep learning has
  transformed," not the on-device failure it fixes. MobiSys wants the system contribution up
  front.
- **The device constraint is hidden** — no thermal, energy, or latency budget is named, which
  is exactly the on-device reality a MobiSys reviewer looks for.
- **Overclaims** ("outperforming prior approaches in most settings," "works well") with **no
  measured quantity** — no latency distribution, energy figure, or thermal trace
  (`mobisys-experiments`).
- **No claim → measurement pairing:** "strong performance" is not tied to a frame-rate curve,
  a joules number, or a memory footprint.
- **Venue-misfit framing:** pitched as an ML result (route to a machine-learning venue) or a
  generic efficiency claim, not as a mobile-*system* whose device behavior is the point — the
  `mobisys-topic-selection` re-route signal.
- **Over-signposted roadmap** standing in for an argument.

---

## After (MobiSys arc — mobile pain → device failure → mechanism → on-device evidence → why it matters)

> **Abstract.** Continuous on-device video inference is fast for the first minute and then
> **collapses**: as a commodity phone heats up, the SoC throttles, and a CNN that ran at 30
> fps drops to a stuttering 11 fps with no warning to the app. Existing efficiency methods —
> quantization, pruning, GPU offload — lower the *average* cost but ignore the **thermal
> trajectory**, so they throttle just the same under sustained load. We present **Thermenon**,
> a thermal-aware runtime that keeps frame rate stable by switching among pre-profiled model
> variants **against a live thermal-headroom estimate**, degrading accuracy gracefully instead
> of dropping frames. On four commodity phones under a 20-minute sustained workload, Thermenon
> holds frame rate within a target band while the throttle-oblivious baseline falls below it
> after 6 minutes, at a bounded accuracy cost, and at lower energy-per-frame. We report frame
> rate, energy-per-frame, and skin temperature as distributions over 10 runs per device.
> *(pain → device failure → mechanism → on-device evidence → measured, all on the first page.)*
>
> **Introduction.** *(¶1 — pain + contribution, first breath.)* An on-device vision app is only
> usable if it holds its frame rate for as long as the user points the camera. In practice a
> phone **throttles under sustained inference**, and today's runtimes have no answer: they were
> tuned for peak, not for the tenth minute. We present **Thermenon**, a runtime that keeps
> frame rate inside a target band as the device heats, by trading model accuracy for thermal
> headroom at run time.
>
> *(¶2 — why current systems fail on the device.)* Existing methods fall short for specific,
> nameable reasons. Static quantization and pruning fix a **single operating point**, so a
> model tuned to run cool at peak still throttles once skin temperature crosses the limit.
> GPU/DSP offload moves heat around the SoC but does not **bound** it. Cloud offload trades the
> thermal problem for a network-latency-and-privacy problem the app was built to avoid. None of
> them **observes the thermal trajectory and acts on it**, which is the gap Thermenon fills.
>
> *(¶3 — the mechanism + the device budget it respects.)* Thermenon pre-profiles a small family
> of model variants for accuracy, latency, and power on each target SoC, then at run time reads
> a thermal-headroom estimate and picks the heaviest variant that will not push the device past
> its throttle point in the next window. The budget it respects is explicit — a per-device skin
> temperature limit and a target frame-rate band — and the runtime never blocks the camera
> pipeline. *(the constraint is named, the way MobiSys expects an on-device budget to be.)*
>
> *(¶4 — on-device evidence, each claim paired.)* Thermenon holds frame rate within the target
> band for the full 20-minute run on all four phones (Fig. 1), where the baseline drops below
> the band after 6 minutes; it does so at a bounded top-1 accuracy cost (Table 1) and at lower
> **energy-per-frame** measured on an external power monitor (Fig. 2). **All results are
> reported as distributions over 10 runs per device**, with the phone models, OS builds,
> ambient temperature, and power-instrument setup in App. A. *(every claim → figure, table, or
> reproducibility location.)*
>
> *(¶5 — why it matters as a deployable service + roadmap.)* The contribution is to make
> sustained on-device inference a **thermal-budgeted system problem** with a runtime answer,
> deployable on unmodified commodity phones without cloud or kernel changes. Section 2 profiles
> the throttling behavior; Section 3 designs the runtime; Section 4 evaluates it on four
> devices. *(brief roadmap, no over-signposting.)*

---

## Why the "after" meets the MobiSys bar

Mapped to the skill checklists:

- **System contribution on the first page** — the abstract and ¶1 state the on-device failure,
  the mechanism, and the target band before any model detail (`mobisys-writing-style`: "put the
  mobile-system contribution in the first page").
- **The device budget is explicit** — a skin-temperature limit and a frame-rate band are named,
  the on-device constraint a MobiSys reviewer checks for (`mobisys-topic-selection`: the result
  must depend on the device, not abstract away from it).
- **Every claim paired with a measurement** — frame-rate stability → Fig. 1; accuracy cost →
  Table 1; energy → Fig. 2; reproducibility → App. A (`mobisys-writing-style` and
  `mobisys-experiments` claim→evidence map).
- **No overclaiming** — "within a target band" with **distributions over 10 runs per device**,
  not "outperforms in most settings"; energy and latency are measured, not asserted
  (`mobisys-experiments`: report distributions on real hardware).
- **Real hardware, named** — four commodity phones with OS builds, ambient temperature, and a
  power instrument, not "a mobile device" (`mobisys-reproducibility`: device/OS/instrument
  provenance).
- **Right venue** — the contribution is a **mobile-systems runtime** whose device behavior is
  the result, so it is a strong MobiSys fit rather than a machine-learning re-route or a MobiCom
  wireless paper (`mobisys-topic-selection` fit test).
- **12-page discipline** — the profiling study and full protocol are pushed toward the appendix
  while the body stays self-contained (`mobisys-writing-style`: the 12 double-column pages carry
  the argument's spine).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, metadata-verified
> MobiSys papers** whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for MobiSys-specific submission policy.
