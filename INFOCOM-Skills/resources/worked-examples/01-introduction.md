> **Illustrative teaching example.** The paper, model, algorithm, and every number below are
> **fictional** and exist only to demonstrate INFOCOM house style. No real-paper facts, systems, or
> results are stated, and no policy is invented. Corresponding skills:
> [`infocom-writing-style`](../../skills/infocom-writing-style/SKILL.md),
> [`infocom-topic-selection`](../../skills/infocom-topic-selection/SKILL.md), and
> [`infocom-experiments`](../../skills/infocom-experiments/SKILL.md).

# Worked Example: An INFOCOM-Style Abstract + Introduction (before → after)

This demonstrates the **INFOCOM first-page arc** from `infocom-writing-style`:
**networking problem → system model and gap → contribution (analysis and/or design) → evidence on
real or simulated networks → what improves and where it does not** — with the INFOCOM expectations
that the contribution is legible to *both* an analytical and a systems reviewer, evidence is
**proportional to the claim**, and the paper is **defensive** because there is (traditionally) no
rebuttal to repair a missed objection.

The framing also reflects `infocom-topic-selection`: INFOCOM is strongest when a **model or
mechanism** is the contribution and the result is validated — here, an online edge-scheduling
algorithm with a provable competitive ratio *and* a trace-driven evaluation — rather than a built
system whose case is a real deployment (which would route to SIGCOMM/NSDI), and when the analysis
would be undersold by a systems-only framing.

**Illustrative paper (fictional):** *"Wait-Then-Serve: An Online Scheduler for Latency-Aware Edge
Offloading with a Competitive Guarantee."* Fictional artifact: a scheduling policy for dispatching
mobile tasks to edge servers, evaluated by proof and by simulation on a request trace.

---

## Before (buries the contribution — typical first-draft abstract + intro)

> **Abstract.** Edge computing is a hot topic. We propose a new scheduling scheme for edge
> offloading using a deep reinforcement learning model and a carefully designed reward. Our approach
> achieves low latency on a large simulation and outperforms baselines, showing the promise of AI
> for edge networks.
>
> **Introduction.** Edge computing is important and growing. Many works schedule tasks at the edge.
> In this paper we use a DRL agent to decide where to send tasks, and we evaluate it in simulation,
> showing strong results. Section II covers related work, Section III our approach, Section IV
> experiments, and Section V concludes.

**What's wrong (against `infocom-writing-style` / `infocom-topic-selection` / `infocom-experiments`):**

- **No networking problem or system model on the first page** — it leads with "edge computing is
  hot" and a model choice, not a scheduling problem a network operator recognizes, its topology, or
  its constraints.
- **Wrong claim shape and no guarantee.** INFOCOM's analytical reviewers expect a formulation; "low
  latency in a large simulation" with no model and no bound reads as an ML demo, not a networking
  contribution.
- **Model-as-contribution.** If the DRL agent were swapped for another learner, no networking lesson
  would remain — the `infocom-topic-selection` re-route signal that this belongs at an ML venue.
- **Undefended evaluation.** "Outperforms baselines" with no named simulator, no seeds, no
  confidence intervals, and no tuning — and there is no rebuttal to fix an "untuned baseline"
  objection later.
- **No limits stated**, so every objection the paper cannot answer is left open.
- **Over-signposted roadmap** substituting for an argument.

---

## After (INFOCOM arc — problem → model → contribution → evidence → limits)

> **Abstract.** Mobile edge platforms must dispatch latency-sensitive tasks to a small set of edge
> servers whose queues fluctuate, deciding for each arriving task whether to serve it now or wait
> for a less-loaded server — a choice made online, without knowing future arrivals. We model
> latency-aware edge offloading as an **online scheduling problem** and present **Wait-Then-Serve**,
> a policy that we prove achieves a **competitive ratio of (stated bound)** against the offline
> optimum under stated assumptions (A1-A3). On a request trace of (N) tasks across (M) edge servers,
> simulated in (named simulator) over (K) seeded runs, Wait-Then-Serve reduces median completion
> latency over the strongest tuned baseline by X% (95% CI ...), and we show the empirical gap tracks
> the analytical bound. We state the demand regime where the guarantee is loose. *(problem → model →
> guarantee → real-trace evidence → limits — all on the first page.)*
>
> **Introduction.** *(¶1 — the networking problem and setting, first breath.)* An edge platform sees
> a stream of latency-sensitive tasks and a handful of servers whose queues rise and fall. For each
> task it must decide, **online and irrevocably**, whether to serve immediately at a loaded server or
> wait briefly for a better one. Scheduling greedily inflates tail latency; waiting too long wastes
> the deadline. The engineering question is: **is there an online policy with a provable guarantee
> against the best offline schedule, that also wins on real traces?**
>
> *(¶2 — the model and why prior state is inadequate.)* We model the setting as online task
> assignment to parallel queues with switching delay (§III: topology, arrival and service
> assumptions A1-A3, objective). Prior INFOCOM optimization work assumes **offline** knowledge of
> arrivals; a SIGCOMM edge system schedules with a **heuristic** and reports measurements but no
> bound; a queueing analysis targets **mean delay**, not the tail our applications care about. None
> gives an online policy with a competitive guarantee for tail-latency-aware offloading.
>
> *(¶3 — contribution, stated as networking claims.)* We make two contributions. First, we
> **formulate** latency-aware online edge offloading and prove that **Wait-Then-Serve** is
> (bound)-competitive under A1-A3 (Theorem 1, proof sketch in §IV, full proof in the in-budget
> appendix). Second, we **evaluate** it on a real request trace, isolating where the guarantee is
> tight and where demand skew loosens it.
>
> *(¶4 — evidence, each claim paired.)* We tie every claim to its method: the competitive ratio is
> proved under stated assumptions (§IV); the empirical gains are measured in (named simulator) on a
> real trace over (K) seeded runs against the strongest prior policy **tuned with an equal,
> documented budget** and a simple immediate-serve baseline, with confidence intervals (Table I,
> Fig. 3); and we show the measured competitive gap matches the analytical prediction as load varies
> (Fig. 4). The simulator configuration and seeds are stated; we release the scripts and trace
> access.
>
> *(¶5 — limits and what improves.)* We state the central limit plainly: under **highly skewed
> demand** the bound is loose, and we show the empirical penalty (Fig. 5) rather than hiding it. The
> payoff for practice is a dispatcher operators can deploy with a worst-case guarantee instead of an
> unbounded heuristic. Section III gives the model; §IV the analysis; §V the evaluation; limits are
> argued alongside the results. *(brief roadmap, no over-signposting.)*

---

## Why the "after" meets the INFOCOM bar

Mapped to the skill checklists:

- **Problem and model on the first page** — the abstract and ¶1-2 pose a scheduling problem, its
  setting, and the gap before any algorithm detail (`infocom-writing-style`: "state the networking
  problem and system model first").
- **A model that does work** — the formulation yields Theorem 1, and the algorithm follows from the
  analysis (`infocom-topic-selection`: the analytical contribution is first-class, not decoration).
- **Evidence proportional to the claim** — a guarantee is *proved*, and the performance claim is a
  *seeded, tuned, interval-reported* simulation on a real trace, with the empirical gap checked
  against the bound (`infocom-experiments`: match the method to the claim).
- **Defensive, because there is no rebuttal** — the assumptions are stated (theory objection
  pre-empted), the baseline is tuned with a documented budget (systems objection pre-empted), and
  the loose-guarantee regime is disclosed (`infocom-author-response`: answer in the paper, not in a
  reply that will not come).
- **Right venue, model-swap test passes** — the lesson (an online policy with a competitive
  guarantee for tail-aware offloading) does not depend on a particular learner, so it is an INFOCOM
  contribution, not an ML re-route (`infocom-topic-selection`).
- **Within the budget** — the full proof lives in an **in-budget** appendix that counts toward the
  nine pages, not an imagined supplement (`infocom-supplementary`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified INFOCOM
> papers** whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for INFOCOM-specific submission policy and
> the review model.
