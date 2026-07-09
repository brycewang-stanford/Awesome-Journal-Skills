> **Illustrative teaching example.** The paper, mechanism, numbers, and setup below are
> **fictional** and exist only to demonstrate HPCA house style. No real-paper facts,
> workloads, or results are stated, and no policy is invented. Corresponding skills:
> [`hpca-writing-style`](../../skills/hpca-writing-style/SKILL.md),
> [`hpca-topic-selection`](../../skills/hpca-topic-selection/SKILL.md), and
> [`hpca-experiments`](../../skills/hpca-experiments/SKILL.md).

# Worked Example: An HPCA-Style Abstract + Introduction (before → after)

This demonstrates the **HPCA first-page arc** from `hpca-writing-style`:
**measured problem → why existing mechanisms miss it → the mechanism → behavior it
produces → what the numbers rest on** — with the HPCA rules that the mechanism-to-behavior
claim sits **on the first page**, the motivation is **quantified before the fix**, and
**every headline number names its instrument** (which simulator at which fidelity, or which
machine in which state), with no overclaiming when the workload set is narrow.

The framing also reflects `hpca-topic-selection`: HPCA is strongest when a **measured
microarchitectural cost** motivates a **buildable mechanism** whose behavior is shown on a
credible instrument — not when the contribution is a pure algorithm (which may route to a
theory venue) or a full programming-system co-design (which may route to ASPLOS).

**Illustrative paper (fictional):** *"Coalescing Irregular Prefetches with a Confidence-Gated
History Filter."* Fictional mechanism: a prefetcher that filters low-confidence irregular
accesses before they consume memory bandwidth.

---

## Before (buries the mechanism — typical first-draft abstract + intro)

> **Abstract.** Memory latency is a well-known bottleneck in modern processors. In this work
> we propose a new prefetcher that improves performance. Our design uses a history-based
> approach with a confidence mechanism and achieves strong speedups across many benchmarks,
> outperforming prior prefetchers in most cases.
>
> **Introduction.** Prefetching has been studied for decades. Many prefetchers exist,
> including stride, stream, and correlation-based designs. In this paper, we present a new
> prefetcher that tracks access history and uses a confidence counter to decide what to
> prefetch. We evaluate it on standard benchmarks and show it works well. Section 2 reviews
> related work, Section 3 describes our design, Section 4 presents results, and Section 5
> concludes.

**What's wrong (against `hpca-writing-style` / `hpca-topic-selection` / `hpca-experiments`):**

- **No measured problem on the first page** — "memory latency is a bottleneck" is a
  platitude, not a quantified cost. HPCA wants the *specific* pathology this paper attacks,
  with a number.
- **The mechanism is vague** — "a confidence mechanism" is not a checkable description; a
  reviewer cannot tell what is new versus a standard confidence counter.
- **Overclaims** ("outperforming prior prefetchers in most cases," "works well") with **no
  instrument named** — no simulator, no fidelity scope, no workload set, no baseline
  configuration (`hpca-experiments`).
- **No behavior-to-cause link**: "strong speedups" is not tied to the bandwidth the filter
  is supposed to save.
- **Venue-misfit framing**: pitched as a generic "improves performance" result rather than a
  mechanism whose *behavior* on the memory system is the contribution — the
  `hpca-topic-selection` signal to sharpen or re-route.
- **Over-signposted roadmap** standing in for an argument.

---

## After (HPCA arc — measured cost → gap → mechanism → behavior → instrument)

> **Abstract.** Irregular-access prefetchers raise coverage but **waste memory bandwidth**:
> on bandwidth-bound regions, a large fraction of their prefetches are never used, and that
> traffic delays demand requests. We introduce a **confidence-gated history filter (CGHF)**
> that suppresses low-confidence irregular prefetches *before* they issue, spending bandwidth
> only where the history predicts reuse. On a set of irregular workloads modeled in a
> cycle-level out-of-order simulator with a validated DRAM timing model, CGHF holds the
> coverage of an aggressive history prefetcher while cutting useless prefetch traffic, and it
> narrows demand-request queuing in the bandwidth-bound phases where the baseline stalls. We
> report per-workload results, not only the mean, and state the simulator, its configuration,
> and the workload regions used. *(measured cost → gap → mechanism → behavior → instrument —
> all on the first page.)*
>
> **Introduction.** *(¶1 — measured problem + contribution, first breath.)* An aggressive
> irregular prefetcher can cover most long-latency misses, but on the bandwidth-bound phases
> that dominate our workloads, much of what it issues is **never used**, and that wasted
> traffic sits in front of demand requests. We present a mechanism, the **confidence-gated
> history filter**, that keeps the coverage while spending bandwidth only where reuse is
> likely.
>
> *(¶2 — gap: why existing mechanisms miss it.)* Existing prefetchers are insufficient for
> distinct, nameable reasons. Stride and stream prefetchers do not track the irregular
> patterns at issue, so they under-cover. History and correlation prefetchers cover the
> pattern but **issue regardless of bandwidth pressure**, so their benefit collapses exactly
> when the memory system is saturated. Throttling schemes react to congestion *after* it
> forms, paying the queuing cost before they back off. *(each prior line gets a specific
> failure, not a vague "prior work is limited.")*
>
> *(¶3 — the mechanism, checkably described.)* CGHF attaches a per-pattern confidence
> estimate to history entries and **gates issue on a threshold that tightens as measured
> bandwidth utilization rises**, so under pressure only high-confidence prefetches proceed.
> The added state is one small table alongside the existing history structure; we give its
> size and the gating logic in full. *(a reviewer can rebuild the mechanism from the text.)*
>
> *(¶4 — behavior + instrument, each number anchored.)* We model CGHF in a cycle-level
> out-of-order core with a DRAM timing model we validate against a documented reference, and
> we state the core width, cache hierarchy, and the sampled workload regions (Section 4). CGHF
> holds the baseline prefetcher's coverage while cutting its useless traffic, and the reduced
> traffic shortens demand-request queuing in the bandwidth-bound phases (Fig. 3, Table 2).
> **We report every workload, mark where CGHF is neutral, and give the DRAM model's validation
> error**, so the win is legible against the instrument rather than asserted. *(every claim →
> a figure/table and a named instrument.)*
>
> *(¶5 — why it matters + roadmap.)* The contribution is a prefetcher whose **behavior tracks
> the resource it competes for**: it converts bandwidth from a hazard the prefetcher ignores
> into a signal the prefetcher obeys. Section 2 characterizes the wasted-traffic problem;
> Section 3 details CGHF; Section 4 gives the methodology and results. *(brief roadmap, no
> over-signposting.)*

---

## Why the "after" meets the HPCA bar

Mapped to the skill checklists:

- **Mechanism-to-behavior claim on the first page** — the abstract and ¶1 state the measured
  cost, the mechanism, and the behavior before any implementation detail
  (`hpca-writing-style`: "put the mechanism-to-behavior claim on the first page").
- **Motivation quantified before the fix** — "much of what it issues is never used" and the
  characterization in Section 2 measure the problem, so the mechanism answers a number
  (`hpca-writing-style`; `hpca-topic-selection`: a measured cost justifies the mechanism).
- **Mechanism checkably described** — the gating logic and table size are given, so a
  reviewer can rebuild it, not guess (`hpca-writing-style`).
- **Every number names its instrument** — cycle-level simulator, validated DRAM model,
  stated core/cache configuration, and sampled regions; the DRAM model's validation error is
  reported (`hpca-experiments`: declare the fidelity contract, match claims to instruments).
- **No overclaiming** — per-workload results with neutral cases marked, not "outperforms in
  most cases" (`hpca-experiments`: report the distribution, not just the mean).
- **Right venue** — a measured microarchitectural cost met by a buildable mechanism whose
  memory-system *behavior* is the contribution — a strong HPCA fit rather than a pure-theory
  or full-stack-co-design re-route (`hpca-topic-selection`).
- **11-page discipline** — the characterization and mechanism carry the body while
  exhaustive per-configuration tables and the artifact live in the appendix and the anonymized
  mirror (`hpca-writing-style`; `hpca-supplementary`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, dblp-verified
> HPCA Test of Time papers** whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for HPCA-specific submission policy.
