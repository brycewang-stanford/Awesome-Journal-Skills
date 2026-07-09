> **Illustrative teaching example.** The paper, system, testbed, and every number below are
> **fictional** and exist only to demonstrate SIGCOMM house style. No real-paper facts, datasets, or
> results are stated, and no policy is invented. Corresponding skills:
> [`sigcomm-writing-style`](../../skills/sigcomm-writing-style/SKILL.md),
> [`sigcomm-topic-selection`](../../skills/sigcomm-topic-selection/SKILL.md), and
> [`sigcomm-experiments`](../../skills/sigcomm-experiments/SKILL.md).

# Worked Example: A SIGCOMM-Style Abstract + Introduction (before → after)

This demonstrates the **SIGCOMM first-page arc** from `sigcomm-writing-style`:
**operational pain (measured) → why current mechanisms cannot fix it → design principle → system →
evidence at real scale/tail → why it generalizes** — with the SIGCOMM norms that the contribution is a
**networking mechanism, not a tuned deployment**, that **motivation is quantified**, and that **evaluation
reports the distribution (tails), not just the mean**, on a testbed, trace, or deployment.

The framing also reflects `sigcomm-topic-selection`: SIGCOMM is strongest when the contribution is a
**networking-stack mechanism validated under realistic traffic** — here, a load-balancing principle backed
by data-center trace replay, not an ML model win (which would route elsewhere) and not a wireless
physical-layer result (which routes to MobiCom).

**Illustrative paper (fictional):** *"Backlog-Aware Flowlet Steering for Lossless Data-Center Fabrics."*
Fictional mechanism: a switch-local scheme that reroutes flowlets by queue backlog to cut tail
flow-completion time under incast.

---

## Before (buries the contribution — typical first-draft abstract + intro)

> **Abstract.** Data centers are increasingly important for modern applications. Congestion in data-center
> networks is a well-known problem. We propose a new load-balancing system that reroutes traffic to avoid
> congested paths and improves performance. We implement our system and evaluate it in simulation, showing
> that it outperforms existing approaches in most cases.
>
> **Introduction.** Data-center networks carry huge amounts of traffic. Many load-balancing schemes have
> been proposed, including ECMP, flow-level hashing, and various adaptive methods. In this paper, we
> present a new approach that monitors the network and moves traffic away from hotspots. We evaluate our
> approach using a simulator and show it works well across several workloads. Section 2 covers background,
> Section 3 describes our system, Section 4 presents results, and Section 5 concludes.

**What's wrong (against `sigcomm-writing-style` / `sigcomm-topic-selection` / `sigcomm-experiments`):**

- **No measured pain on the first page** — "congestion is a well-known problem" asserts the motivation
  instead of quantifying it. SIGCOMM wants the operational cost stated in numbers (which percentile, how
  bad, under what traffic).
- **No design principle** — "moves traffic away from hotspots" is a behavior, not a stated invariant or
  mechanism. Reviewers cannot tell what idea is being defended.
- **Simulation-only, mean-only** — "outperforms in most cases" with no tail, no testbed, no trace. At
  SIGCOMM a single-run, mean-only, simulator result reads as under-evaluated for a fabric claim.
- **No claim → evidence pairing** — "works well" is tied to nothing measurable.
- **Venue-blur framing** — pitched as generic "performance," not as a networking-stack mechanism with a
  clear place in the fabric; nothing signals why this is SIGCOMM rather than a systems-generic venue.
- **Roadmap padding** substituting for an argument.

---

## After (SIGCOMM arc — measured pain → gap → principle → system → tail evidence → generality)

> **Abstract.** In lossless data-center fabrics, incast bursts push switch queues to their pause threshold,
> and today's load balancers react too late: ECMP is congestion-oblivious, and flow-level adaptive schemes
> rebalance on RTT-scale signals that lag the sub-RTT queue buildup that actually triggers pause. On a
> 128-server testbed replaying a production RPC trace, this shows up as a **3.1x inflation of 99th-percentile
> flow-completion time** for short flows during incast. We present **backlog-aware flowlet steering (BFS)**,
> a switch-local mechanism that reroutes at **flowlet** granularity using instantaneous egress-queue backlog
> as the steering signal, so rerouting tracks congestion at the timescale it forms without reordering flows.
> BFS requires no end-host changes and no new switch hardware beyond backlog counters already exposed by
> commodity ASICs. On the same testbed it **reduces 99th-percentile short-flow FCT by 2.4x** versus the
> adaptive baseline at matched throughput, and we confirm the effect across three incast ratios and two
> buffer sizes, reporting medians and 99th percentiles over 20 trace replays. *(measured pain → gap →
> principle → deployability → tail evidence — all on the first page.)*
>
> **Introduction.** *(¶1 — the pain, quantified, first breath.)* Lossless data-center fabrics using
> priority flow control turn transient queue buildup into network-wide pause, and pause is what inflates
> the tail that latency-sensitive RPCs feel. On our 128-server testbed replaying a production RPC workload,
> incast episodes lift 99th-percentile short-flow completion time by **3.1x** even though mean utilization
> stays moderate — the cost lives entirely in the tail, which is exactly what a mean-throughput view hides.
>
> *(¶2 — gap: why current mechanisms cannot fix it.)* Existing load balancers miss this for distinct,
> nameable reasons. ECMP hashes flows to paths **congestion-obliviously**, so an unlucky hash collision
> under incast is never corrected. Flow-level adaptive schemes do sense congestion, but they act on
> **RTT-scale** feedback and at **flow** granularity, so they respond after the queue has already crossed
> the pause threshold and they cannot split a heavy flow without reordering it. Endpoint-driven schedulers
> assume host-stack changes that many operators cannot deploy fleet-wide. *(each prior line gets a specific
> failure, not a vague "prior work is limited.")*
>
> *(¶3 — the design principle.)* BFS rests on one principle: **steer at the timescale and granularity at
> which congestion forms.** Congestion in these fabrics forms **sub-RTT** and at the granularity of
> **flowlets** — bursts separated by idle gaps larger than the path-delay difference. BFS therefore reroutes
> flowlets on **instantaneous egress-queue backlog**, a signal local to the switch, so a steering decision
> reflects the queue that is actually filling, and flowlet gaps make the reroute reordering-safe by
> construction. *(the invariant is stated, not implied.)*
>
> *(¶4 — system + evidence, each claim paired.)* We implement BFS on a programmable-switch data plane using
> backlog counters commodity ASICs already expose (Section 3), so it needs no host changes and no new
> hardware. On the 128-server testbed it cuts 99th-percentile short-flow FCT by **2.4x** against the
> adaptive baseline **at matched aggregate throughput** (Section 5.1, Table 2); the win holds across three
> incast ratios (Section 5.2) and two switch-buffer sizes (Section 5.3); and a deliberate adversarial
> workload where flowlet gaps vanish maps the **break point** where BFS degrades to ECMP (Section 5.4). All
> numbers are medians and 99th percentiles over **20 trace replays**, with the trace, topology, and
> configuration in the artifact (Section 6). *(every claim → a table, a sweep, or a documented break
> point.)*
>
> *(¶5 — why it generalizes + roadmap.)* The contribution is not one scheme but the principle that
> **congestion response should match the timescale and granularity of congestion formation**, which applies
> to any lossless fabric exposing a local backlog signal. Section 2 characterizes the incast tail;
> Section 3 presents the mechanism; Sections 4-5 evaluate on the testbed and trace. *(brief roadmap, no
> over-signposting.)*

---

## Why the "after" meets the SIGCOMM bar

Mapped to the skill checklists:

- **Measured pain on the first page** — the abstract and ¶1 quantify the tail cost (3.1x P99 inflation)
  before any design detail (`sigcomm-writing-style`: "lead with the operational cost, in numbers").
- **A design principle, not a point fix** — "steer at the timescale and granularity congestion forms" is a
  stated invariant the rest of the paper defends (`sigcomm-writing-style`: name the principle).
- **Every claim paired with evidence** — P99 win → Table 2; robustness → incast-ratio and buffer sweeps;
  honesty → the mapped break point (`sigcomm-experiments` claim→evidence map).
- **Tails, not means** — results are medians and 99th percentiles over 20 replays at **matched
  throughput**, not "outperforms in most cases" (`sigcomm-experiments`: report the distribution and hold
  the fair variable fixed).
- **Deployability argued** — no host changes, no new hardware beyond exposed counters; SIGCOMM rewards
  mechanisms that fit the deployed stack (as DCTCP did with existing ECN).
- **Right venue** — a networking-stack mechanism validated under realistic traffic is a strong SIGCOMM
  fit, not an ML-systems or wireless-physical-layer re-route (`sigcomm-topic-selection` fit test).
- **12-page discipline** — the tail characterization, mechanism, and core evaluation carry the body; extra
  sweeps and trace details go to appendix and artifact (`sigcomm-writing-style`: spend the 12 pages on the
  argument's spine).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, venue-verified SIGCOMM papers**
> whose first pages execute this arc, and [`../official-source-map.md`](../official-source-map.md) for
> SIGCOMM-specific submission policy.
