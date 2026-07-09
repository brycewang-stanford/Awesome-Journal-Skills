---
name: socc-workflow
description: Use when planning an ACM SoCC project timeline from venue fit through the two-round abstract+paper deadlines, the rebuttal, notification, camera-ready, and presentation, with backward-planning offsets for a cloud-systems measurement paper and honest handling of the two-rounds-per-year cadence and the no-cross-round-resubmission rule.
---

# SoCC Workflow

Use this as the project-management skill for a SoCC submission. Replace every date with the current
official timetable and work backwards from the **round's abstract-registration cutoff** — which
precedes the paper deadline by about a week. SoCC — the ACM Symposium on Cloud Computing, jointly
sponsored by SIGMOD and SIGOPS — runs **two review rounds per year**, so the first planning
decision is *which round* you are genuinely ready for.

SoCC is a conference with **no standing editor-in-chief**; its rotating leadership is the
per-edition **General Chair(s)** and **Program Committee Co-Chairs** appointed under SIGMOD and
SIGOPS (SoCC 2026 PC Co-Chairs reported as Eric Lo and Ivan Beschastnikh, verified 2026-07-09 via
committee-page rendering; confirm on the live page). The cost model is conference registration; at
least one author presents.

## Milestones

- **Venue fit:** confirm SoCC over OSDI/NSDI/EuroSys/ATC and over SIGMOD/VLDB
  (`socc-topic-selection`), and confirm the contribution spans the systems-and-data intersection.
- **Evidence lock:** freeze the system/mechanism, the testbed or trace, the workloads, the
  baselines, and the measurement pipeline.
- **Round choice:** pick Round 1 or Round 2 knowing a Round-1 reject **cannot** be resubmitted to
  Round 2 the same year.
- **Abstract registration:** submit real title, abstract, authors, subject tags, and conflicts by
  the round's abstract cutoff.
- **Submission:** upload the anonymized acmart PDF and (where possible) the artifact link by the
  round's paper deadline (AoE).
- **Rebuttal:** during the round's author-response window, answer reviewers on the axes they raised.
- **Notification:** accept / reject for that round; archive reviews, rebuttal, and every version.
- **Acceptance:** prepare the camera-ready, pursue ACM artifact badges if the edition offers
  evaluation, register, and present in Singapore (SoCC 2026).

## Backward plan from a round's paper deadline

| Weeks out (heuristic) | Cloud-systems milestone |
|---|---|
| 10+ | System/mechanism feature-frozen; testbed or trace and baselines chosen |
| 8 | Experiments running; measurement harness logs throughput, latency, tail, and cost |
| 6 | Analysis done; cost-latency and tail results computed; baselines tuned with a documented budget |
| 4 | Full draft in acmart sigconf; artifact (trace-replay/testbed scripts) assembled and anonymized |
| 3 | Internal mock review by a systems reader and a data/measurement reader |
| 2 | Tail and cost results hardened; related-work delta sharpened; 12-page budget met |
| 1 | Dual-anonymous sweep on PDF and artifact (traces, cluster names, system names) |
| 0 | Abstract registered by its earlier cutoff, then paper + artifact link on HotCRP |

These offsets are planning heuristics only — anchor every one to the current Important Dates /
HotCRP deadlines page, never to a previous cycle's calendar.

## Two-rounds-per-year: the honest calendar reality

SoCC's twin-round model is a genuine advantage and a trap:

- **Advantage:** there are **two shots per calendar year** at the same venue (a winter/February
  round and a summer/July round for SoCC 2026), so a paper that misses one round is only months
  from the next.
- **Trap:** a paper **rejected in Round 1 may not be resubmitted to Round 2** the same year, so a
  rushed Round-1 submission does not buy a discounted retry — it costs you the year at SoCC. Submit
  to the round you can make *strong*, not merely the nearer one.
- As of 2026-07-09, the live target is **SoCC 2026 Round 2** (paper 14 Jul 2026); Round 1 (13 Feb
  2026) has passed.

## Failure modes by stage

- **Evidence still moving at week 4** forces last-minute measurement nobody has audited — the
  classic soundness reject for a systems paper.
- **Simulation-only at submission** invites the "does it hold on a real testbed?" reject from both
  sponsoring communities.
- **Reporting only the mean** — omitting tail latency and cost — reads as not understanding what a
  cloud paper is judged on.
- **Leaving the anonymized trace/artifact to the final week** is how a cluster name or provider
  hint leaks identity under dual-anonymous review.
- **Treating Round 1 as a free draft** and getting rejected forfeits the whole SoCC year.

## Coordination notes

- Assign one owner for the measurement harness and reproducibility package and another for the
  dual-anonymous sweep; shared ownership is how both slip.
- Archive the exact submitted PDF and artifact — the rebuttal must quote the paper precisely and
  stay anonymous.

## Output format

```text
[Current stage] idea / evidence / round-choice / submitted / rebuttal / accepted
[Target round] round 1 / round 2, with the next official deadline and source
[Critical path] <three tasks that determine readiness>
[Risk register] <page budget / anonymity / simulation-vs-testbed / tail+cost evidence / artifact>
[Owner map] <task -> person or role>
```
