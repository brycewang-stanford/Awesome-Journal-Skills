> **Illustrative teaching example.** The system, dataset, device numbers, and every result below
> are **fictional** and exist only to demonstrate FAST house style. No real-paper facts, products,
> or measurements are stated, and no policy is invented. Corresponding skills:
> [`fast-writing-style`](../../skills/fast-writing-style/SKILL.md),
> [`fast-topic-selection`](../../skills/fast-topic-selection/SKILL.md), and
> [`fast-experiments`](../../skills/fast-experiments/SKILL.md).

# Worked Example: A FAST-Style Abstract + Introduction (before → after)

This demonstrates the **FAST first-page arc** from `fast-writing-style`:
**storage problem a practitioner recognizes → why current designs pay a storage cost → the design
or finding → evidence on real devices and workloads → what changes for storage systems** — with the
FAST expectations that the contribution is a *storage* contribution, evidence is measured in storage
terms (write amplification, tail latency, endurance, crash consistency) on **real hardware**, and
the device/workload setup is credible from the start.

The framing also reflects `fast-topic-selection`: FAST is strongest when the lesson is about how
storage is **laid out, written, cached, made durable, or kept consistent** — here, how a key-value
store spends flash writes — rather than a general systems result whose storage angle is incidental
(which would route to OSDI/ATC), and when the study could not simply be re-labeled as an OSDI or
EuroSys paper without loss of its storage core.

**Illustrative paper (fictional):** *"Frugal: Cutting Write Amplification in LSM Key-Value Stores by
Endurance-Aware Compaction."* Fictional artifact: a compaction scheduler that reorders and defers
LSM compactions to reduce bytes written to flash, evaluated on real consumer and datacenter SSDs.

---

## Before (buries the storage contribution — typical first-draft abstract + intro)

> **Abstract.** Key-value stores are everywhere. We present Frugal, a new key-value store with a
> smart compaction algorithm. Frugal is fast and achieves high throughput on our benchmark,
> outperforming a popular baseline. Our results show the promise of better compaction for modern
> storage.
>
> **Introduction.** Storage is important and SSDs are widely used. LSM-tree key-value stores such as
> the popular ones perform compaction, which can be slow. In this paper we design a better
> compaction scheduler and show it is faster on a benchmark. Section 2 covers background, Section 3
> our design, Section 4 experiments, and Section 5 concludes.

**What's wrong (against `fast-writing-style` / `fast-topic-selection` / `fast-experiments`):**

- **No storage problem on the first page** — it leads with "key-value stores are everywhere" and a
  throughput win, not the *storage cost* (write amplification and the flash endurance it consumes)
  that a storage reviewer cares about. FAST wants the storage contribution up front.
- **Wrong claim shape.** "High throughput on our benchmark" is not evidence about the design's real
  target. If the contribution is *endurance-aware* compaction, the headline metric must be **bytes
  written to flash / write amplification**, on real devices — not a single throughput bar.
- **No device reality.** No SSD models, no firmware, no fill level, no steady-state vs.
  fresh-out-of-box — a storage reviewer's first question ("on what hardware, in what state?") is
  unanswered.
- **System-as-contribution with an incidental storage angle.** If "faster compaction" is the whole
  point and flash endurance is a footnote, the paper reads as an OSDI/ATC systems paper, a
  `fast-topic-selection` re-route signal.
- **No availability posture** — no traces, no code, no mention of an artifact, which a double-blind
  FAST reviewer looks for immediately.
- **Over-signposted roadmap** substituting for an argument.

---

## After (FAST arc — storage problem → cost → design → real-device evidence → what changes)

> **Abstract.** LSM-tree key-value stores write each key-value pair to flash many times over as data
> moves down the tree — write amplification that both slows writes and **consumes the SSD's finite
> program/erase budget**, shortening device life in write-heavy deployments. We show that a large
> fraction of these rewrites are avoidable: compaction schedules are chosen for read performance and
> ignore how many bytes they burn. We present **Frugal**, an endurance-aware compaction scheduler
> that defers and reorders compactions to cut bytes-written while bounding read amplification. On
> **three real SSDs (one datacenter, two consumer), at steady state after aging**, driven by
> **YCSB and two production-derived block traces**, Frugal reduces measured write amplification
> substantially versus a tuned baseline at comparable read latency, and we report the resulting
> change in projected drive lifetime with confidence intervals. Code, trace-replay scripts, and the
> aging protocol are in the artifact. *(storage problem → cost in endurance terms → design →
> real-device evidence → durability payoff — all on the first page.)*
>
> **Introduction.** *(¶1 — the storage problem, first breath.)* In write-heavy key-value
> deployments the scarce resource is not CPU but the **flash write budget**: every byte an LSM store
> rewrites during compaction is a byte subtracted from the SSD's endurance and added to tail
> latency. Operators feel this as drives wearing out ahead of schedule and as write stalls, yet
> compaction is still scheduled as if writes were free.
>
> *(¶2 — why the current state pays a storage cost.)* Standard compaction minimizes read
> amplification and space, treating device writes as an afterthought. On flash this is exactly
> backwards for write-heavy workloads: the schedule that reads best can rewrite the same data
> several extra times, and the cost lands on **endurance**, a resource no throughput benchmark
> reports. Prior tuning knobs trade space for reads; none is *endurance-aware*, and none is
> validated by bytes actually written to real devices.
>
> *(¶3 — contribution, stated as storage claims.)* We make two contributions. First, a
> **measurement** across real SSDs and workloads showing how much of LSM write amplification is
> schedule-induced and therefore avoidable. Second, **Frugal**, an endurance-aware compaction
> scheduler that cuts bytes-written while holding read amplification within a stated bound —
> evaluated for the metric that matters, device writes, not just throughput.
>
> *(¶4 — evidence on real devices, each claim paired.)* We tie every claim to device-level evidence:
> write amplification and bytes-written are measured from the SSDs' own counters (SMART / device
> logs), not estimated; experiments run **at steady state after a documented aging protocol**, with
> fill level and TRIM state stated; read-latency effects are reported as distributions including
> **p99/p99.9 tail latency**; and projected-lifetime change carries confidence intervals over
> repeated runs. Devices, firmware, workloads, and traces are listed in the artifact.
>
> *(¶5 — durability/consistency posture and what changes for storage.)* We state the central caveat
> plainly: bytes-written and endurance gains are **device- and firmware-specific**, so we report per
> device and bound generalization rather than claiming a universal factor; and we verify that
> deferring compactions does not weaken crash consistency, using a block-level record-and-replay
> test in the artifact. The payoff for practice is concrete: write-heavy deployments can extend
> drive life without trading away read latency. Section 2 gives LSM/flash background; Section 3
> Frugal's scheduler; Section 4 the real-device evaluation; caveats are argued alongside each
> result, not deferred. *(brief roadmap, no over-signposting.)*

---

## Why the "after" meets the FAST bar

Mapped to the skill checklists:

- **Storage contribution on the first page** — the abstract and ¶1 pose a flash-endurance/write
  problem and a device-write question before any throughput claim (`fast-writing-style`: "lead with
  the storage cost, measured in storage terms").
- **Evidence proportional to the claim, on real devices** — the claim is about *bytes written and
  endurance*, so the evidence is device-counter measurements at steady state on named SSDs with
  tail-latency distributions, not a single throughput bar (`fast-experiments`: match the metric to
  the storage claim; control device state).
- **Real-device reality engaged where it lives** — firmware, aging, fill level, TRIM, and
  per-device reporting are named in ¶4–¶5, and generalization is bounded rather than over-claimed
  (`fast-experiments`, `fast-reproducibility`).
- **Right venue, storage-lesson test passes** — the lesson (much LSM write amplification is
  schedule-induced and recoverable; endurance-aware scheduling recovers it) is a *storage* lesson
  that would lose its core if re-labeled a generic systems paper (`fast-topic-selection`).
- **Availability by default** — code, trace-replay scripts, and the aging protocol are in an
  artifact, matching FAST's double-blind, artifact-badge expectations
  (`fast-reproducibility`, `fast-artifact-evaluation`).
- **Consistency not sacrificed for the win** — a crash-consistency record-and-replay check confirms
  the durability property the change could have broken (`fast-experiments`: test the storage
  invariant your optimization risks).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified FAST
> papers** whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for FAST-specific submission policy and
> the two-deadline, one-shot-revision cycle.
