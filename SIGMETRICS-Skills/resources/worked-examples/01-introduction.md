> **Illustrative teaching example.** The paper, model, trace, and every number below are
> **fictional** and exist only to demonstrate SIGMETRICS house style. No real-paper facts, systems,
> or results are stated, and no policy is invented. Corresponding skills:
> [`sigmetrics-writing-style`](../../skills/sigmetrics-writing-style/SKILL.md),
> [`sigmetrics-topic-selection`](../../skills/sigmetrics-topic-selection/SKILL.md), and
> [`sigmetrics-experiments`](../../skills/sigmetrics-experiments/SKILL.md).

# Worked Example: A SIGMETRICS-Style Abstract + Introduction (before → after)

This demonstrates the **SIGMETRICS first-page arc** from `sigmetrics-writing-style`:
**systems-performance problem → why current models/policies fall short → contribution (a model or
policy, ideally with a provable performance bound) → evidence that pairs analysis with measurement
or simulation → what changes for real systems** — with the SIGMETRICS expectations that the claim
is **rigorous** (an assumption-stated theorem, not just a plot), evidence is **proportional to the
claim**, and the **modeling assumptions and their validity** are visible from the start.

The framing also reflects `sigmetrics-topic-selection`: SIGMETRICS is strongest when a paper
**models, measures, and analyzes** system performance — here, a scheduling policy for a
disaggregated-memory tier with a proven tail-latency bound *and* a trace-driven evaluation — rather
than a pure systems-building result (which would route to NSDI/OSDI) or a pure network-measurement
result (which would route to IMC).

**Illustrative paper (fictional):** *"Rank-Aware Scheduling for Disaggregated Memory: A Tail-Latency
Bound and a Trace-Driven Evaluation."* Fictional contribution: a scheduling policy with a proven
bound on p99 fetch latency, validated in simulation and on a production-like trace.

---

## Before (buries the performance contribution — typical first-draft abstract + intro)

> **Abstract.** Disaggregated memory is increasingly popular. We propose a new scheduler that
> improves performance. Experiments on our testbed show large speedups over the default, achieving
> state-of-the-art latency. Our results demonstrate the promise of smarter scheduling for modern
> datacenters.
>
> **Introduction.** Datacenters are important and memory disaggregation is a hot topic. Existing
> schedulers are simple and do not perform well. In this paper we design a better scheduler and
> evaluate it, showing it is faster. Section 2 covers background, Section 3 our design, Section 4
> experiments, Section 5 related work, and Section 6 concludes.

**What's wrong (against `sigmetrics-writing-style` / `sigmetrics-topic-selection` / `sigmetrics-experiments`):**

- **No performance question and no model on the first page** — it leads with a trend and a vague
  "improves performance," not a precise metric (tail latency), a workload model, or a claim a
  reviewer can check. SIGMETRICS wants the performance contribution, stated rigorously, up front.
- **No analysis.** A SIGMETRICS reviewer expects a *why* — a model and ideally a proven bound — not
  only a testbed speedup. "State-of-the-art latency" with no theorem and no baseline definition is
  an NSDI-style systems claim wearing a SIGMETRICS title.
- **Assumptions and their validity are absent**, so the reader cannot tell when the result holds
  (which arrival process? which service distribution? heavy-tailed?).
- **Evidence is one testbed** with no simulation-vs-analysis agreement and no confidence intervals
  — the reviewer's first question ("does the model match measurement?") is unanswerable.
- **Over-signposted roadmap** substituting for a contribution statement.

---

## After (SIGMETRICS arc — problem → inadequacy → model+bound → analysis meets measurement → what changes)

> **Abstract.** In disaggregated memory, remote-fetch **tail latency** governs application
> performance, yet the schedulers in use optimize mean latency and can inflate the p99 by
> reordering long fetches ahead of short ones. We model the fetch queue as an **M/G/1 with
> heavy-tailed service** and show that no size-oblivious policy bounds the tail; we then introduce
> **RankFetch**, a rank-based policy, and **prove that its p99 fetch latency is within a constant
> factor of the size-aware optimum under stated assumptions** (Thm. 1, with the assumptions and
> their empirical support in §3). We validate the bound two ways: a simulation across service-time
> distributions shows the analytic p99 curve matches measurement within its confidence interval
> (Fig. 4), and a **trace-driven evaluation on a production-like workload** shows RankFetch reduces
> measured p99 by a large margin over the default while preserving mean latency (Table 2, effect
> sizes and CIs reported). *(problem → inadequacy → model → theorem → analysis-meets-measurement →
> systems payoff — all on the first page.)*
>
> **Introduction.** *(¶1 — the performance problem, first breath.)* An application stalls on its
> slowest memory fetch, so in disaggregated memory the metric that decides user-visible performance
> is the **tail** of fetch latency, not its mean. Schedulers deployed today minimize mean latency;
> under heavy-tailed fetch sizes this can push a few long fetches ahead of many short ones and
> **inflate the p99** precisely when it matters most.
>
> *(¶2 — why the current state is inadequate.)* Prior scheduling analyses either assume light-tailed
> service, which real fetch-size distributions violate, or evaluate only mean response time. Neither
> tells an operator **whether any deployable policy can bound the tail**, nor by how much a
> size-aware policy could help. The question is not "is our scheduler faster on our testbed?" but
> **"is there a policy with a provable tail-latency guarantee under realistic, heavy-tailed
> service, and does it help on real workloads?"**
>
> *(¶3 — contribution, stated as a model, a theorem, and a validation.)* We make three
> contributions. First, an **M/G/1 model** of the fetch queue with heavy-tailed service and an
> impossibility observation: no size-oblivious policy bounds the p99 (§3). Second, **RankFetch**, a
> rank-based policy, with **Theorem 1** bounding its p99 within a constant factor of the size-aware
> optimum under stated assumptions. Third, a **two-track validation**: simulation confirming the
> analysis, and a trace-driven evaluation confirming the systems payoff.
>
> *(¶4 — evidence that pairs analysis with measurement.)* We tie every claim to evidence: the
> theorem's predicted p99 curve is overlaid on simulated measurements across three service
> distributions and agrees within confidence intervals (Fig. 4); the trace-driven p99 reduction is
> reported with effect sizes and bootstrap CIs over repeated runs on a production-like workload
> (Table 2); and we report where the assumptions of Theorem 1 hold and where they are stressed
> (§6). The model, simulator with logged seeds, trace-processing scripts, and the analysis
> notebooks are in the anonymized artifact.
>
> *(¶5 — assumption validity and what changes for systems.)* We state the central caveat plainly:
> Theorem 1 assumes fetch sizes are known or well-estimated at enqueue time; §6 quantifies the
> degradation under estimation error and bounds it. The payoff for practice is concrete: an operator
> can bound p99 with a policy that needs only a size estimate, not a redesigned memory tier.
> Section 3 develops the model and theorem; Section 4 the simulation validation; Section 5 the
> trace-driven evaluation; assumptions are argued where they are used, not deferred. *(brief
> roadmap, no over-signposting.)*

---

## Why the "after" meets the SIGMETRICS bar

Mapped to the skill checklists:

- **Performance contribution on the first page** — the abstract and ¶1 pose a precise metric (p99
  tail latency) and a checkable claim (a constant-factor bound) before any implementation detail
  (`sigmetrics-writing-style`: "lead with the performance contribution, stated rigorously").
- **Rigor: a model and a theorem, not just a plot** — the contribution is an M/G/1 model plus
  Theorem 1, with assumptions stated; the impossibility observation motivates the design
  (`sigmetrics-experiments`: analysis is evidence, and its assumptions are part of the claim).
- **Analysis meets measurement** — the theorem's predicted curve is validated against simulation
  *and* the systems payoff is shown on a trace, the SIGMETRICS signature of pairing a bound with
  measurement (`sigmetrics-experiments`: match evidence to the claim; validate the model).
- **Right venue, model-swap test passes** — the lesson (a rank-based policy provably bounds the
  tail, and it helps on real traces) is a *performance-evaluation* result, not a systems-building
  paper (NSDI/OSDI) or a pure measurement paper (IMC) (`sigmetrics-topic-selection`).
- **Assumption validity engaged where it lives** — the known-size assumption is named in ¶5 and its
  failure quantified in §6, not quarantined (`sigmetrics-writing-style`: state assumptions where
  the result uses them).
- **Reproducibility by default** — model, seeded simulator, trace-processing scripts, and analysis
  notebooks are in an anonymized artifact, matching SIGMETRICS's double-anonymous, reproducibility
  expectations (`sigmetrics-reproducibility`, `sigmetrics-artifact-evaluation`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified
> SIGMETRICS papers** whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for SIGMETRICS-specific submission policy
> and the rolling three-cycle POMACS model.
