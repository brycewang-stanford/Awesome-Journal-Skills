> **Illustrative teaching example.** The paper, system, dataset, and every number below are
> **fictional** and exist only to demonstrate SoCC house style. No real-paper facts, deployments,
> or results are stated, and no policy is invented. Corresponding skills:
> [`socc-writing-style`](../../skills/socc-writing-style/SKILL.md),
> [`socc-topic-selection`](../../skills/socc-topic-selection/SKILL.md), and
> [`socc-experiments`](../../skills/socc-experiments/SKILL.md).

# Worked Example: A SoCC-Style Abstract + Introduction (before → after)

This demonstrates the **SoCC first-page arc** from `socc-writing-style`:
**cloud-scale problem an operator recognizes → why current systems are inadequate at that scale →
the mechanism or measurement → evidence on a real/realistic deployment with cost and tail behavior
→ what changes for cloud practice** — with the SoCC expectations that the contribution lives at the
**systems-and-data intersection** (SIGMOD+SIGOPS), that evidence is **measured, not asserted**, and
that **cost and tail latency** are first-class, not afterthoughts.

The framing also reflects `socc-topic-selection`: SoCC is strongest when the lesson is about how
**cloud infrastructure is built, operated, scheduled, stored, or paid for at scale** — here,
tail-latency-aware autoscaling for serverless functions — rather than a pure OS-kernel result
(which routes to OSDI/ATC), a pure network-fabric result (NSDI), or a pure query-optimizer result
(SIGMOD/VLDB).

**Illustrative paper (fictional):** *"Tailspin: Tail-Aware Autoscaling for Serverless Functions
Under Bursty Load."* Fictional system: an autoscaler that provisions function instances from a
predicted tail-latency target instead of average CPU, evaluated on a replayed production
invocation trace.

---

## Before (buries the systems-and-data contribution — typical first-draft abstract + intro)

> **Abstract.** Serverless computing is popular. We build a new autoscaler for serverless
> functions that uses machine learning to predict load and scales instances accordingly. Our
> approach achieves good performance on our benchmark and outperforms a baseline, demonstrating the
> promise of ML for cloud resource management.
>
> **Introduction.** Cloud computing is important and serverless is growing fast. Many systems
> autoscale based on CPU utilization. In this paper we propose an ML-based autoscaler and evaluate
> it on some workloads, showing improvements. Section 2 covers related work, Section 3 our design,
> Section 4 evaluation, Section 5 discussion, and Section 6 concludes.

**What's wrong (against `socc-writing-style` / `socc-topic-selection` / `socc-experiments`):**

- **No operator-recognizable problem at scale on the first page** — it leads with "serverless is
  popular" and an ML win, not with the cost/tail pain a platform team actually feels. SoCC wants
  the cloud-systems problem up front.
- **Wrong evidence shape.** "Good performance on our benchmark" against an unnamed baseline says
  nothing about **tail latency under bursts** or **provisioning cost**, the outcomes that decide
  whether an operator adopts an autoscaler.
- **Cost and tail latency are invisible**, though they are the currency of a cloud paper; average
  CPU is exactly the proxy the paper should be replacing.
- **Model-as-contribution.** If the ML predictor were swapped for a simpler estimator, no cloud
  lesson is stated — the `socc-topic-selection` re-route signal that this may be an ML paper
  wearing a cloud title.
- **No reproducibility posture** — no mention of the trace, the testbed, the workload replay, or
  released code, which a SoCC reviewer from either sponsoring community looks for immediately.
- **Over-signposted roadmap** substituting for a contribution.

---

## After (SoCC arc — scale problem → inadequacy → mechanism → measured deployment → what changes)

> **Abstract.** Serverless platforms bill by the millisecond and promise elasticity, yet operators
> routinely over-provision to defend tail latency during bursts — paying for idle capacity to hide
> a problem that average-utilization autoscalers cannot see. We characterize this gap on a replayed
> **production invocation trace of 3.1 billion calls across 1,900 functions** and show that
> CPU-driven autoscaling meets the **p99 latency target only a minority of the time** under bursty
> arrivals while sustaining large idle cost. We present **Tailspin**, an autoscaler that provisions
> from a predicted **tail-latency** target rather than average CPU. On the replayed trace and a
> 200-node testbed, Tailspin holds p99 within the target across the burst regimes we test while
> **cutting provisioned instance-seconds substantially** versus the CPU baseline and a
> reactive-queue baseline; we report cost-latency Pareto curves, a cold-start sensitivity analysis,
> and the regimes where the predictor helps and where it does not. Trace-replay harness, testbed
> scripts, and configurations are released. *(scale problem → inadequacy → mechanism → measured
> cost/tail evidence → honest limits — all on the first page.)*
>
> **Introduction.** *(¶1 — the operator problem, first breath.)* On a serverless platform the two
> numbers that matter are **tail latency** and **the bill**, and they pull against each other. To
> keep p99 acceptable during traffic bursts, teams pre-warm and over-provision — buying idle
> instance-seconds to paper over the moments an autoscaler reacts too late. The systems question is
> not "can we predict load?" but **"can we provision directly from a tail-latency target so an
> operator stops trading money for tail?"**
>
> *(¶2 — why current systems are inadequate at scale.)* Production autoscalers scale on **average
> CPU or concurrency**, signals that lag bursty, short-lived function invocations and say nothing
> about the *distribution* of latency. Reactive queue-length schemes fire after the tail has
> already been missed. Neither controls the outcome operators are billed against, and both leave
> the cost-versus-tail trade-off implicit rather than as a knob.
>
> *(¶3 — contribution, stated as systems-and-data claims.)* We make two contributions. First, a
> **measurement** of the cost-versus-tail gap of CPU-driven autoscaling on a large replayed
> invocation trace, quantifying how much idle capacity current practice buys to defend p99.
> Second, **Tailspin**, an autoscaler that closes the loop on a **tail-latency SLO** and exposes
> the cost-latency trade-off as an explicit target — evaluated as a built system, not a simulation
> alone.
>
> *(¶4 — evidence on a real/realistic deployment, each claim paired.)* We tie every claim to
> measurement: the cost-tail gap is quantified on the replayed trace (Fig. 1); Tailspin's p99
> attainment and provisioned instance-seconds are reported on a 200-node testbed against a CPU
> autoscaler and a reactive-queue baseline, both tuned with a documented budget (Table 2);
> cost-latency Pareto curves show the trade-off (Fig. 3); and a cold-start sensitivity analysis
> bounds where prediction error hurts (Fig. 4). The trace-replay harness and testbed scripts are
> released for reproduction.
>
> *(¶5 — honest limits and what changes for cloud practice.)* We state the central limit plainly:
> the trace is from one provider and one region, so the burst structure may not generalize, and we
> scope the claim to the arrival regimes tested rather than to serverless in general. The payoff is
> concrete: operators can set a tail SLO and let the platform find the cheapest provisioning that
> meets it, instead of over-buying to hide the tail. Section 2 presents the measurement; Section 3
> Tailspin's controller; Section 4 the evaluation; limitations are discussed alongside the results,
> not deferred. *(brief roadmap, no over-signposting.)*

---

## Why the "after" meets the SoCC bar

Mapped to the skill checklists:

- **Operator problem on the first page** — the abstract and ¶1 pose a cost-versus-tail problem a
  platform team recognizes before any predictor detail (`socc-writing-style`: "lead with the
  cloud-systems contribution, in cost and tail terms").
- **Evidence measured, not asserted** — the claim is about tail latency and provisioning cost, so
  the evidence is p99 attainment and instance-seconds on a replayed trace and a real testbed with
  tuned baselines, not "good performance on our benchmark" (`socc-experiments`: match the
  measurement to the claim, report cost and tail).
- **Systems-and-data intersection** — a *measurement* of production traces (the SIGMOD-flavored
  half) plus a *built autoscaler* (the SIGOPS-flavored half) in one paper, which is exactly SoCC's
  joint identity (`socc-topic-selection`).
- **Right venue, model-swap test passes** — the lesson (provision from a tail SLO, expose the
  cost-tail knob) survives swapping the predictor, so it is a cloud-systems contribution, not an ML
  re-route (`socc-topic-selection`).
- **Reproducibility by default** — the trace-replay harness, testbed scripts, and configurations
  are released, matching SoCC's systems-and-data reproducibility expectations
  (`socc-reproducibility`, `socc-artifact-evaluation`).
- **Honest baselines and limits** — tuned CPU and reactive-queue baselines, Pareto curves, a
  sensitivity analysis, and a stated single-provider external-validity limit pre-empt the
  reviewer's first objections (`socc-experiments`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified SoCC
> papers** whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for SoCC-specific submission policy and
> the two-round cycle.
