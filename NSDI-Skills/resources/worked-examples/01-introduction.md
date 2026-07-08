> **Illustrative teaching example.** The system, workloads, deployments, and every
> number below are **fictional**, invented to demonstrate NSDI house style. No real
> paper, product, or policy is described, and nothing here overrides the current CFP.
> Companion skills: [`nsdi-writing-style`](../../skills/nsdi-writing-style/SKILL.md),
> [`nsdi-experiments`](../../skills/nsdi-experiments/SKILL.md), and
> [`nsdi-topic-selection`](../../skills/nsdi-topic-selection/SKILL.md).

# Worked Example: An NSDI-Style Abstract + Introduction (before → after)

The rewrite target is the NSDI opening arc: **operational pain → why the network/
distributed setting causes it → design principle → built system → trace-and-testbed
evidence → what a deployment would change**. NSDI reviewers read for a networking-stack
or distributed-systems contribution backed by realistic-scale measurement; a paper that
opens like a benchmark report or a protocol-theory note misses the venue's center.

**Fictional paper:** *"Ballast: Shifting Cross-Region RPC Retries Off the Congested
Path."* Fictional idea: a retry-budget protocol that lets datacenter RPC layers
coordinate retries with path-level congestion state instead of firing them blind.

---

## Before (how systems drafts typically open)

> **Abstract.** Remote procedure calls are fundamental to modern microservices.
> Unfortunately, retries can cause problems under congestion. We present Ballast, a
> novel retry management system. Ballast uses an adaptive algorithm to decide when to
> retry. Experiments show Ballast improves tail latency by up to 4.1x compared to
> existing approaches, demonstrating its effectiveness.
>
> **Introduction.** Microservices have become increasingly popular in recent years.
> Communication between services uses RPCs, and failures require retries. Existing
> retry mechanisms use fixed timeouts or exponential backoff, which can be suboptimal.
> We propose Ballast, which adapts retries intelligently. Our contributions are: (1) a
> new retry algorithm; (2) an implementation; (3) extensive experiments showing up to
> 4.1x improvement. The rest of this paper is organized as follows...

**Why this fails the NSDI read:**

- **No operational grounding.** "Retries can cause problems" — no trace, no incident
  shape, no scale. NSDI's culture expects the pain to be evidenced, not asserted.
- **The mechanism is a black box.** "An adaptive algorithm" names nothing another
  team could reuse; the design principle is the paper's actual product.
- **"Up to 4.1x" is a red flag** — a maximum over an undisclosed distribution, with no
  workload provenance and no tail percentile named.
- **No distributed-systems necessity.** Nothing explains why this is a *networked
  systems* problem rather than a local library tweak — the exact scope line the CFP
  draws ("no contribution to the design of networked systems or the networking stack"
  is out of scope).
- **Contribution list restates the paper's existence** (algorithm, implementation,
  experiments) instead of stating what is now known or possible.

---

## After (the NSDI arc)

> **Abstract.** In cross-region microservice deployments, the RPC layer's own
> recovery machinery is a first-order source of overload: retries issued during
> congestion add load precisely where capacity is scarcest. In a 21-day trace of a
> 3,000-service testbed replaying production-derived call graphs, retry traffic grew
> from 2% of RPCs at baseline to 34% during regional congestion events, and
> retry-amplified storms accounted for the worst 0.4% of end-to-end latencies. Blind
> per-caller policies (fixed timeout, exponential backoff, hedging) cannot see the
> path state that determines whether a retry helps or harms. We present **Ballast**, a
> retry-budget protocol in which the RPC layer leases per-path retry budgets from a
> congestion signal already carried by the transport, so retries are shifted in time
> and across replicas rather than fired into the congested path. Ballast runs
> unmodified applications on two open RPC frameworks. Across trace-replay and
> fault-injection experiments on an 80-node, three-region testbed, Ballast cuts p99.9
> end-to-end latency during congestion events by 2.1-3.4x relative to exponential
> backoff with jitter, while raising goodput 11% and never exceeding the retry budget
> observed in the incident-free baseline. We report medians over 10 replayed weeks
> with per-event breakdowns.
>
> **Introduction.** *(¶1 — the operational pain, evidenced.)* Every large RPC
> deployment carries a recovery mechanism that can defeat itself: when a region
> congests, callers time out and retry, and those retries land on the congested path.
> In our replayed traces (§2), retries during congestion events triple the offered
> load on the affected links while contributing almost nothing to goodput. *(¶2 — why
> the setting makes it hard.)* The information needed to make a retry useful — is the
> path congested, is a replica reachable another way, has the original request already
> been admitted — exists in the transport and load-balancing layers, but per-caller
> retry policies cannot see it; each caller optimizes locally and the fleet melts
> collectively. This is a coordination problem among distributed components, not a
> parameter-tuning problem. *(¶3 — the design principle, named.)* Ballast's principle
> is that **retries should spend a budget priced by the path, not a count chosen by
> the caller**: the transport exposes a per-path congestion lease, the RPC layer
> spends it on the retry (in time or across replicas) that the lease can afford.
> *(¶4 — built and measured.)* We implemented Ballast in two open-source RPC
> frameworks without application changes and evaluated it on an 80-node three-region
> testbed replaying 21 days of production-derived call graphs, with fault injection
> reproducing three incident classes. *(¶5 — claims, each with its evidence address.)*
> Ballast improves p99.9 latency during congestion 2.1-3.4x over tuned backoff (§6.2),
> holds goodput within 2% of an oracle that knows path state (§6.3), and degrades to
> baseline behavior when the congestion signal is absent (§6.4). We state where the
> lease abstraction breaks — sub-RTT incasts and single-replica services — in §7.

---

## What changed, mapped to the skills

| Move | Before | After | Skill |
| --- | --- | --- | --- |
| Pain evidenced | "retries can cause problems" | trace-quantified retry amplification | `nsdi-experiments` |
| Distributed necessity | absent | local policies cannot see path state | `nsdi-topic-selection` |
| Principle named | "adaptive algorithm" | budget priced by the path | `nsdi-writing-style` |
| Claim shape | "up to 4.1x" | p99.9 range over 10 replayed weeks, per-event | `nsdi-experiments` |
| Honest boundary | none | named failure regimes in §7 | `nsdi-writing-style` |
| Evidence addresses | none | every claim carries a section number | `nsdi-writing-style` |

Two further NSDI-specific notes. First, the "after" text keeps deployment claims
honest for a **testbed** paper — it says trace-replay on a testbed, not production
deployment; claiming operational experience you do not have is a track mismatch
(`nsdi-topic-selection`). Second, everything reviewers need sits in the 12-page body;
the appendix pages the CFP allows can hold protocol details, but the argument cannot
depend on them (`nsdi-supplementary`).

> Next: study the real openings in [`../exemplars/library.md`](../exemplars/library.md)
> — all five are free PDFs on `usenix.org` — and check current policy in
> [`../official-source-map.md`](../official-source-map.md).
