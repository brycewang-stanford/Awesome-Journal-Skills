---
name: nsdi-topic-selection
description: Use when judging whether a project belongs at NSDI, picking among its research, operational-systems, and frontiers tracks, or re-routing to SIGCOMM, OSDI, SOSP, FAST, or SIGMETRICS — testing the networking-stack contribution, the CFP's out-of-scope lines, and which of the two yearly deadlines to aim at.
---

# NSDI Topic Selection

Venue choice at NSDI is a scope question before it is a quality question. The notes
below reflect the NSDI '27 Call for Papers as rendered on 2026-07-08; the scope
paragraph, track list, and exclusions are rewritten each edition, so reread
`usenix.org/conference/nsdi27/call-for-papers` before committing a team to a deadline.

## The scope sentence that decides most cases

The CFP's negative space is unusually explicit. Three families are declared out of
scope regardless of quality:

1. Work with **no contribution to the design of networked systems or the networking
   stack** — a distributed application that merely *uses* the network is not enough.
2. **Hardware architecture** and **physical-layer** contributions (beamforming,
   modulation, and similar).
3. **Sensing and localization** work.

The positive test is the venue's full name: design principles, implementation, and
**practical evaluation** of networked and distributed systems. Ask: *which layer of a
networked system does this change, and what realistic traffic has been pushed through
the change?* If neither clause has an answer, no amount of polish fixes the fit.

## Three tracks, three evidence contracts

NSDI '27 reviews three tracks; the choice is made at submission and sets the bar the
paper is judged against.

| Track | Contract with reviewers | Wrong-track failure mode |
|---|---|---|
| Research | New design + implementation + practical evaluation | Prototype thin on evaluation reads as unfinished |
| Operational systems | Real-world use of a deployed system; anonymization relaxed (system/company names may stay) | Research prototype dressed as "operational" has no experience to report |
| Frontiers | Bold, high-novelty idea; complete evaluation not required | Incremental idea with partial results reads as an excuse, not a frontier |

The frontiers track is the newest lever: it exists precisely for work that fails the
research track's evaluation bar *because the idea is early*, not because the
experiments were skipped. Do not use it to launder an under-evaluated conventional
design.

## Routing among the siblings

```text
Where does the center of gravity sit?  (verify each venue's live CFP)
network/distributed system, built + measured      -> NSDI (research)
deployed at scale, lessons are the contribution   -> NSDI (operational systems)
early, reshapes how a problem is framed           -> NSDI (frontiers)
protocol/measurement result, networking community
  but no built-system requirement                 -> SIGCOMM
host OS, runtime, or kernel is the object         -> OSDI / SOSP
storage stack end to end                          -> FAST
performance modeling / queueing analysis          -> SIGMETRICS
mobile/wireless system with PHY entanglement      -> MobiCom (PHY itself: out of NSDI scope)
```

The NSDI/OSDI boundary is the one most often argued. Both are USENIX systems venues,
but they cut the stack differently: when the *network or the distributed coordination*
is the object of design, the work is NSDI's; when the *host* — kernel, scheduler,
memory, storage — is the object and the network is plumbing, it is OSDI/SOSP material.
A useful probe: delete the multi-node aspect from the evaluation. If the contribution
survives on one machine, NSDI reviewers will notice too.

The NSDI/SIGCOMM boundary is cultural as much as topical: overlapping communities, but
NSDI expects a built system whose design is validated end to end, while a
measurement-only or protocol-analysis paper without an implementation story travels
better to SIGCOMM. ML topics cut both ways at NSDI: *systems for ML* and *ML for
systems* are named in scope, but a paper whose delta is model accuracy has left the
venue.

## Calendar as a routing input

NSDI's two deadlines per edition change the routing calculus in ways single-deadline
siblings cannot match. As of 2026-07-08:

- NSDI '27 **spring** deadline (papers April 23, 2026) has passed; notification lands
  July 23, 2026.
- NSDI '27 **fall** deadline is open: abstracts September 10, papers September 17,
  2026 (11:59 pm US EDT).

Consequences worth planning around: a near-ready project can target September rather
than waiting most of a year; a spring submission that draws a **one-shot revision**
gets a structured second life at a later deadline (`nsdi-review-process`); but a
spring **rejection without revision** locks the paper out of the fall deadline — so
submitting a half-built system "to get feedback" costs a real option. Eight
submissions per author is the cap across both deadlines.

## Borderline cases, adjudicated

Recurring gray zones and how the scope sentence resolves them:

- **ML training/serving system:** in scope when the contribution is communication,
  placement, or coordination across machines ("systems for ML"); out when the delta
  is model quality with a distributed backdrop.
- **Measurement study:** strong at NSDI when it ends in a design consequence — a
  mechanism, defense, or operator-actionable finding; measurement without
  consequence travels better to IMC.
- **Single-host networking stack (kernel bypass, NIC offload):** genuinely
  contested territory with OSDI; NSDI-favored when end-to-end, multi-node behavior
  is the object of evaluation.
- **Wireless system:** in scope above the physical layer; the moment the
  contribution is beamforming or modulation, the CFP's exclusion applies.

## Fit probes before committing a deadline

- Name the networking-stack or distributed-design element that is new. One sentence,
  no adjectives.
- Name the realistic traffic: which trace, testbed, or deployment exercises the
  design? "We will find a workload later" means the fall deadline, not this one.
- Name the operational constraint the design respects (failure domains, incremental
  deployability, tail behavior) — NSDI's reviewer culture reads for these.
- Confirm the honest track. Deployment stories need a deployment; frontiers ideas need
  genuine novelty, not missing baselines.
- Check the exclusion list once more — sensing/localization and PHY work get desk
  attention, not sympathy.

## Output format

```text
[NSDI fit] strong / arguable / out of scope (cite which scope clause)
[Stack element changed] <one sentence>
[Realistic traffic] <trace / testbed / deployment named, or "missing">
[Track] research / operational / frontiers (why this contract)
[Deadline math] fall '26-09-17 vs next spring; option cost if rejected
[Re-route] SIGCOMM / OSDI / SOSP / FAST / SIGMETRICS / MobiCom + reason
```
