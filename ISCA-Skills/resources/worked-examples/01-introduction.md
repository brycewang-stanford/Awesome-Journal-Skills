# Worked Example: An ISCA-Style Abstract + Introduction (before → after)

> **Illustrative teaching example.** The paper, mechanism, workloads, and every
> number below are **invented** to demonstrate ISCA first-page craft. No real
> paper is paraphrased, and no venue policy is asserted beyond what
> [`../official-source-map.md`](../official-source-map.md) verifies. Companion
> skills: [`isca-writing-style`](../../skills/isca-writing-style/SKILL.md),
> [`isca-experiments`](../../skills/isca-experiments/SKILL.md),
> [`isca-topic-selection`](../../skills/isca-topic-selection/SKILL.md).

**Fictional paper:** *"SlackCredit: Deadline-Aware Memory Scheduling for
Latency-Critical Cores Sharing DRAM with Streaming Accelerators."* Invented
premise: on SoCs where CPU cores and high-bandwidth accelerators share a memory
controller, the invented SlackCredit mechanism tracks per-request latency slack
and lets streaming traffic borrow bandwidth only against measured slack.

---

## Before (a typical first draft)

> **Abstract.** Modern systems-on-chip integrate CPUs and accelerators that
> share memory bandwidth, causing severe interference. Existing memory
> schedulers cannot handle this heterogeneity well. We propose SlackCredit, a
> novel memory scheduling framework that intelligently balances latency and
> bandwidth demands. Extensive simulations show SlackCredit improves
> performance by up to 41% while being highly practical.
>
> **Introduction.** Memory bandwidth is one of the most important resources in
> modern computer systems. With the rise of AI, accelerators are everywhere,
> and they compete with CPUs for DRAM. Many memory schedulers have been
> proposed over the years. However, they were designed for homogeneous
> multicore systems and perform poorly in heterogeneous settings. Motivated by
> this, we propose SlackCredit. Our contributions are: (1) we identify a new
> problem; (2) we design a novel scheduler; (3) we perform extensive
> evaluations demonstrating significant improvements.

### Why this fails the venue's bar

- **No measured motivation.** "Severe interference" and "perform poorly" are
  asserted, never shown. The ISCA reader expects characterization data before
  a proposal — the section that decides the paper's fate is missing
  (`isca-writing-style`, motivation section).
- **No mechanism visible.** "Intelligently balances" describes an aspiration.
  What state is kept, per what, updated when? The reviewer cannot mentally
  simulate anything on page 1.
- **Uncalibrated headline.** "Up to 41%" is the best case of an unnamed metric
  on unnamed workloads from an unnamed instrument — three violations in five
  words (`isca-experiments`, methodology contract).
- **"New problem" claim with no lineage.** Heterogeneous memory scheduling has
  neighbors; claiming novelty of the *problem* invites the committee's memory
  (`isca-related-work`).
- **Contribution list of activities**, not falsifiable statements.

---

## After (rebuilt to the ISCA bar)

> **Abstract.** On SoCs that share a DRAM subsystem between latency-critical
> cores and streaming accelerators, we measure that accelerator co-run inflates
> core p99 memory latency by 2.1-3.4× across our workload pairs, even under a
> state-of-the-art fairness-oriented scheduler, because fairness policies
> meter *bandwidth*, not *deadline slack*. We present SlackCredit, a memory-
> controller mechanism that tags each core request with measured slack —
> the gap between its predicted completion and the oldest dependent
> instruction's stall horizon — and admits accelerator bursts only against
> aggregate posted slack. SlackCredit adds 9.3 KB per memory channel and no
> pipeline changes. In cycle-level simulation (configuration in §5), it
> restores core p99 latency to within 8% of solo execution while sustaining
> 94% of accelerator throughput, versus 61% for strict core-priority
> scheduling; gains persist across a 16-workload-pair sweep and degrade
> gracefully when slack prediction is disabled.
>
> **Introduction (opening moves).** The first page shows one characterization
> figure: p99 core memory latency under accelerator co-run, normalized to solo,
> across workload pairs and three existing schedulers — establishing magnitude,
> breadth, and the failure of the natural baselines before SlackCredit is
> named. The insight sentence follows: *because streaming requests are
> deadline-tolerant at microsecond scale while core requests carry
> instruction-level deadlines, metering interference in units of measured slack
> — rather than bandwidth shares — removes tail inflation without idling the
> bus.* Contributions are stated as checkable claims: a slack-tagging mechanism
> with stated storage and update rules (§4); a characterization of why
> bandwidth-share fairness cannot bound tails (§3); an evaluation with
> per-pair results, an ablation disabling slack prediction, and a sensitivity
> sweep over credit granularity (§6); and stated limits — the mechanism
> assumes accelerator traffic tolerates ~µs deferral, and results are
> simulator-based with the fidelity scope declared in §5.

### What changed, move by move

| Move | Before | After |
| --- | --- | --- |
| Motivation | asserted adjective ("severe") | measured range (2.1-3.4× p99) with baselines already tried |
| Problem framing | "heterogeneity is hard" | a *named cause*: fairness meters bandwidth, deadlines live in slack |
| Mechanism on page 1 | "intelligently balances" | state (slack tags), policy (admit against posted slack), cost (9.3 KB/channel) |
| Headline | "up to 41%" | central result with metric, baseline, scope, and the losing case kept visible |
| Instrument honesty | "extensive simulations" | "cycle-level simulation (configuration in §5)" + fidelity scope named in the limits |
| Contributions | activity list | falsifiable claims with section pointers |
| Limits | absent | stated on page 1, which buys credibility for every number above it |

### Transfer checklist for your own first page

- [ ] One characterization figure a reviewer could cite back at you
- [ ] The insight sentence: structural cause → mechanism → behavioral effect
- [ ] Every added structure sized; every policy given its trigger
- [ ] Headline number carries metric + baseline + workload scope + instrument
- [ ] The best case is not impersonating the typical case
- [ ] A limitation appears before the fold — chosen, not confessed
