> **Illustrative teaching example.** The paper, system, numbers, and deployment below are
> **fictional** and exist only to demonstrate SenSys house style. No real-paper facts,
> datasets, or results are stated, and no policy is invented. Corresponding skills:
> [`sensys-writing-style`](../../skills/sensys-writing-style/SKILL.md),
> [`sensys-topic-selection`](../../skills/sensys-topic-selection/SKILL.md), and
> [`sensys-experiments`](../../skills/sensys-experiments/SKILL.md).

# Worked Example: A SenSys-Style Abstract + Introduction (before → after)

This demonstrates the **SenSys first-page arc** from `sensys-writing-style`:
**sensing/deployment pain → why existing systems fail on constrained hardware → the mechanism
you built → measured system behavior (energy, latency, accuracy under real conditions) → why it
generalizes.** The SenSys rules the arc encodes: the contribution is a **buildable mechanism**,
**energy/resource cost is a first-class metric**, and **every claim is paired with a
measurement on real hardware** — never an offline benchmark number standing in for deployed
behavior.

The framing also reflects `sensys-topic-selection`: SenSys is strongest when the contribution
is **a system that senses and computes under embedded constraints**, not a pure algorithm
(which routes to a signal-processing or ML venue) and not a mobile-networking mechanism (which
routes to MobiCom). Post-merger, an on-device-AI angle is in-scope when the *system* is the
contribution.

**Illustrative paper (fictional):** *"BatFree: A Batteryless Acoustic Event Classifier that
Runs Inference Between Energy-Harvesting Duty Cycles."* Fictional system: a microcontroller
node that harvests ambient energy, buffers audio, and runs a quantized classifier only when the
capacitor crosses a threshold.

---

## Before (buries the system in benchmark language)

> **Abstract.** Deep learning has transformed audio classification. We propose a new neural
> network for acoustic event detection that achieves high accuracy on a standard benchmark,
> outperforming prior models. Our approach is lightweight and suitable for IoT devices. We
> evaluate on a public dataset and show strong results.
>
> **Introduction.** Acoustic sensing is important for many applications. Many machine-learning
> methods exist for audio classification, but they are large. In this paper we design a small
> model and deploy it on a microcontroller. We show it works well and uses little power.
> Section 2 covers related work, Section 3 the model, Section 4 experiments, Section 5
> concludes.

**What's wrong (against `sensys-writing-style` / `sensys-topic-selection` / `sensys-experiments`):**

- **No system contribution on the first page** — leads with "deep learning has transformed,"
  not the embedded pain (intermittent power) or the mechanism. SenSys wants the *system* idea
  first.
- **Energy is a hand-wave** — "uses little power," "lightweight," with **no measurement method,
  no numbers, no duty-cycle model**. At SenSys energy is the headline metric, not an adjective.
- **Benchmark accuracy substitutes for deployed behavior** — "high accuracy on a standard
  benchmark" says nothing about behavior when power is intermittent and audio arrives during
  brownouts.
- **No claim → measurement pairing** — "works well" is tied to no figure, no on-device latency,
  no harvested-energy trace.
- **Venue-misfit framing** — pitched as a model-accuracy win (an ML-venue contribution), not as
  a system that survives intermittent energy (the `sensys-topic-selection` re-route signal).
- **Roadmap replaces an argument.**

---

## After (SenSys arc — pain → gap → mechanism → measured behavior → why it generalizes)

> **Abstract.** Batteryless acoustic sensors must classify events while their only power source
> — harvested ambient energy — disappears mid-computation, so a model that is accurate on a
> workstation still **loses events during brownouts** and **corrupts inference state across
> power failures**. We present **BatFree**, a batteryless node that (i) sizes its audio buffer
> and capacitor so a full inference fits inside one charge cycle, and (ii) checkpoints
> classifier state to non-volatile memory at layer boundaries so a power failure resumes rather
> than restarts. On a bench harvester reproducing indoor light, BatFree completes inference
> across power cycles where a checkpoint-free baseline never terminates, holds end-to-end event
> latency within a bounded window, and matches the wired model's accuracy on the same audio.
> We report energy per inference measured with a source-meter at 10 kHz, latency distributions
> over 1,000 events, and accuracy against manually labeled ground truth. *(pain → gap →
> mechanism → measured behavior — all on the first page.)*
>
> **Introduction.** *(¶1 — the embedded pain + the contribution.)* A batteryless classifier is
> only useful if it produces a label **before the capacitor drains**. Ambient harvesting
> delivers energy in unpredictable bursts, so an inference started at the wrong moment is
> abandoned and the event is lost. We built **BatFree**, a node that co-designs its **energy
> buffer** and its **inference checkpointing** so classification survives intermittent power.
>
> *(¶2 — gap: why existing systems are insufficient, each for a nameable reason.)* Prior
> approaches fail here for distinct reasons. Compressing the model shrinks compute but **ignores
> the arrival pattern of energy**, so a small model still dies mid-inference under a weak
> harvest. General intermittent-computing runtimes checkpoint **at fixed intervals**, adding
> non-volatile writes that **cost more energy than they save** for short inferences. Buffering
> all audio to flash defers the problem but **exhausts the energy budget** before any label is
> produced. *(each prior line gets a specific embedded failure, not "prior work is limited.")*
>
> *(¶3 — the mechanism + the constraint it respects.)* BatFree sizes the capacitor from the
> **measured energy of one full inference** plus a margin, and inserts checkpoints **only at
> layer boundaries**, where activation state is smallest, so a resume costs one small
> non-volatile write. The design assumes only that a single layer's compute fits within the
> minimum observed charge burst — a condition we measure and report, not assume.
>
> *(¶4 — measured behavior, each claim paired.)* We show BatFree terminates inference across
> power failures where the checkpoint-free baseline never returns a label (Fig. 3), holds
> per-event latency within a bounded window under a harvest trace (Table 2), and matches the
> wired model's accuracy on identical audio scored against manual labels (Table 3). **Energy per
> inference is measured with a source-meter at 10 kHz; latency is reported as a distribution
> over 1,000 events; accuracy carries its ground-truth protocol** (App. A). *(every claim → a
> figure, a table, or a measurement method.)*
>
> *(¶5 — why it generalizes + roadmap.)* The contribution is a **co-design recipe** — size the
> buffer to one inference, checkpoint at the cheapest state boundary — that applies to any
> intermittently powered classifier, not just audio. Section 3 details the energy model;
> Section 4 the deployment measurements. *(brief roadmap, no over-signposting.)*

---

## Why the "after" meets the SenSys bar

- **System contribution on the first page** — the abstract and ¶1 name the mechanism (buffer
  sizing + layer-boundary checkpointing) before any model detail (`sensys-writing-style`: lead
  with the buildable system).
- **Energy is first-class and measured** — energy per inference has a named instrument and
  sampling rate, not an adjective (`sensys-experiments`: report the measurement method).
- **Every claim paired with on-hardware evidence** — termination → Fig. 3; latency → Table 2;
  accuracy → Table 3 with a ground-truth protocol (`sensys-writing-style` claim→measurement map).
- **Deployed behavior over benchmark accuracy** — the win is *surviving intermittent power*,
  not a leaderboard delta (`sensys-topic-selection` fit test; `sensys-experiments`: evaluate
  under real conditions).
- **Honest ground truth** — accuracy is scored against documented manual labels, not an unstated
  reference (`sensys-reproducibility`).
- **Right venue** — the contribution is a **system that computes under an embedded energy
  constraint**, a strong SenSys fit rather than an ML-venue model-accuracy paper.

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, dblp-verified
> SenSys papers** whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for SenSys submission policy.
