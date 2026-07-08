> **Illustrative teaching example.** The system, workloads, and every number below are
> **fictional**, invented solely to demonstrate how an MLSys first page should move. No real
> paper, product, or benchmark result is described, and no venue policy is invented.
> Corresponding skills: [`mlsys-writing-style`](../../skills/mlsys-writing-style/SKILL.md),
> [`mlsys-experiments`](../../skills/mlsys-experiments/SKILL.md), and
> [`mlsys-topic-selection`](../../skills/mlsys-topic-selection/SKILL.md).

# Worked Example: An MLSys-Style Abstract + Introduction (before → after)

An MLSys first page must do something neither a pure ML page nor a pure systems page does: it
must show a **bottleneck measured on a realistic ML workload**, a **named mechanism** that removes
it, and a **quantified system-level payoff** (throughput, latency, memory, or cost) with the
tradeoff stated honestly. Reviewers here are systems builders: adjectives without workloads read
as marketing, and engineering effort without an abstraction reads as a tech report.

**Illustrative paper (fictional):** *"LayerWeave: Overlapping KV-Cache Migration with Decode to
Serve Mixture-of-Experts Models Under Bursty Load."* Fictional mechanism: interleaving expert-
weight prefetch and KV-cache migration into decode-step bubbles on multi-GPU servers.

---

## Before (reads as a product announcement — typical first draft)

> **Abstract.** Large language models are transforming industry, but serving them is expensive.
> We present LayerWeave, a novel high-performance serving system for Mixture-of-Experts models.
> LayerWeave uses several optimizations to dramatically improve GPU utilization and achieves up
> to 3.4x higher throughput than existing systems. Our extensive experiments demonstrate that
> LayerWeave significantly outperforms all baselines across a wide range of settings.
>
> **Introduction.** MoE models are increasingly popular. However, serving them efficiently is
> challenging. Existing systems suffer from poor utilization. We built LayerWeave, which
> carefully overlaps communication and computation and includes many engineering optimizations.
> Experiments show large speedups. Section 2 covers background, Section 3 our design, Section 4
> evaluation, Section 5 related work.

**What a systems reviewer flags (against this pack's skills):**

- **No measured bottleneck.** "Poor utilization" is asserted, never quantified on a named
  workload — the reviewer cannot tell whether the problem is real or already solved.
- **"Up to 3.4x" with no workload context** — peak-case cherry-picking is the single fastest way
  to lose a systems reviewer's trust (`mlsys-experiments`: report distributions, not maxima).
- **No named mechanism.** "Several optimizations" and "many engineering optimizations" hide the
  research contribution; MLSys asks *what abstraction travels beyond this codebase?*
- **No tradeoff.** Every serving optimization costs something (latency tails, memory headroom,
  complexity); a page that admits no cost reads as unmeasured.
- **No baseline identity.** "Existing systems" unnamed means the comparison is unfalsifiable.

---

## After (bottleneck → insight → mechanism → measured payoff → tradeoff)

> **Abstract.** Serving Mixture-of-Experts LLMs under bursty request loads forces a choice
> between overprovisioning GPU memory for all experts or paying expert-swap stalls on the decode
> critical path. Profiling a 16-expert, 8-GPU deployment under a diurnal trace, we find decode
> stalls from expert migration consume 31% of GPU time at the 95th-percentile load (§2). Our
> insight is that decode steps leave predictable per-layer communication bubbles long enough to
> hide most migration traffic. **LayerWeave** schedules KV-cache and expert-weight movement into
> these bubbles via a lookahead planner over the token-level execution graph. On three open MoE
> models and two request traces, LayerWeave raises goodput 1.6-2.2x over the strongest tuned
> baseline at equal p99 latency, at the cost of 6% extra host memory for the migration plan; the
> gain shrinks to 1.1x under uniform (non-bursty) load. Code and traces are released for artifact
> evaluation. *(bottleneck quantified → insight → named mechanism → ranged payoff with baseline
> identity → honest tradeoff and scope limit.)*
>
> **Introduction.** *(¶1 — the bottleneck, measured.)* MoE inference multiplies model capacity
> without multiplying per-token FLOPs, but under real traffic it multiplies *data movement*:
> which experts are hot changes with the request mix. In our motivating measurement (§2), expert
> migration stalls the decode path for 31% of GPU time at peak load — a bottleneck that grows
> with expert count, not model size. *(the problem is a number on a workload, not an adjective.)*
>
> *(¶2 — why existing designs cannot fix it.)* Static expert placement avoids migration but
> wastes memory on cold experts; reactive swapping (the strategy in the systems we compare
> against) moves weights on demand, exactly when the decode path needs the interconnect;
> replicating hot experts helps only until the hot set shifts. Each existing point solves one
> corner of the load-shape space and pays for it elsewhere. *(each alternative gets a specific,
> mechanistic failure — not "prior work is limited.")*
>
> *(¶3 — insight and mechanism, named.)* Our observation is structural: per-layer all-to-all
> exchanges leave interconnect bubbles whose length is predictable one layer ahead. LayerWeave's
> planner treats migration as a scheduling problem over these bubbles — a small integer program
> solved incrementally per decode step — rather than as a caching problem. *(the contribution is
> the reusable idea: bubbles + lookahead scheduling, which another team could reimplement.)*
>
> *(¶4 — evaluation preview with tradeoffs.)* Across three MoE models and bursty/uniform traces,
> LayerWeave improves goodput 1.6-2.2x at matched p99 latency versus the strongest baseline after
> equal tuning effort; ablations attribute 70% of the gain to bubble scheduling and the rest to
> plan reuse (§6). LayerWeave adds 6% host memory and does not help under uniform load — we state
> where it should not be deployed. *(ranged claims, ablation attribution, and a stated
> non-win.)*

---

## Why the "after" clears the MLSys bar

- **Bottleneck first, with a number** — the paper earns its existence in one measured sentence,
  the move `mlsys-writing-style` calls the profiling hook.
- **Mechanism has a name and a shape** — "lookahead planner over decode bubbles" is an
  abstraction a reader can carry away; "many optimizations" is not.
- **Performance claims are ranged, baselined, and latency-constrained** — goodput at matched
  p99, against a *named, tuned* baseline (`mlsys-experiments`: equal-tuning discipline).
- **The tradeoff and the non-win are on page one** — 6% memory, no gain under uniform load.
  Systems reviewers reward this; its absence triggers the "what are they hiding" pass.
- **Artifact intent is declared early**, matching the venue's badge culture
  (`mlsys-artifact-evaluation`).

> Next: study real first pages from the verified papers in
> [`../exemplars/library.md`](../exemplars/library.md), and confirm current cycle rules through
> [`../official-source-map.md`](../official-source-map.md) before drafting to a deadline.
