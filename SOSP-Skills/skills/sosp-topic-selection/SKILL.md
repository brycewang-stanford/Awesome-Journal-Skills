---
name: sosp-topic-selection
description: Use when deciding whether a systems project is SOSP-shaped — a built and measured artifact embodying an extractable principle in operating and distributed systems — or better routed to OSDI, EuroSys, USENIX ATC, NSDI, FAST, ASPLOS, VLDB, MLSys, or HotOS, and when to make that call in the project's life.
---

# SOSP Topic Selection

Use this months before any deadline, when the routing decision is still cheap. SOSP
solicits work on "the design, implementation, analysis, evaluation, and deployment
of computer systems software" (2026 CFP at `sigops.org/s/conferences/sosp/2026/cfp.html`,
checked 2026-07-08) — a broad charter that in practice is filtered through one
question: *is there an operating-systems principle here, embodied in something built
and measured?*

## The three-part SOSP shape test

1. **Principle** — an extractable insight that outlives the artifact. Someone should
   be able to apply it while building a different system. "We made X fast" is not a
   principle; "X can be fast because responsibility R can move below interface I"
   is.
2. **Embodiment** — a real system that exists and runs. SOSP is hostile to
   simulation-only and design-only papers outside genuinely unusual cases; the
   venue's culture is build-and-measure.
3. **Evidence at the claim's scale** — an evaluation that could survive
   `sosp-experiments`. A principle about datacenter tails needs datacenter-shaped
   evidence.

A project passing all three is SOSP-shaped regardless of its subdomain: kernels,
virtualization, distributed systems, storage, verification, security architecture,
cloud infrastructure, and systems-for-ML have all produced recent SOSP programs.

## Routing table

| Signal from the project | Better home | Why |
|---|---|---|
| SOSP-shaped, but the posted SOSP deadline is far and OSDI's is near | OSDI | The venues are peer siblings, both annual since 2024; timing may decide (see `sosp-workflow`) |
| Solid engineering, deployment lessons, no extractable principle | USENIX ATC | ATC's practitioner center of gravity rewards experience and pragmatics |
| The contribution lives in protocols, routing, or the network path | NSDI | Networked-systems PC evaluates the right axis |
| Storage stack, file systems, flash/NVM specifics | FAST | Deep storage expertise in the room |
| The insight is at the hardware/software interface | ASPLOS | Architecture-adjacent reviewers |
| Query processing, transactions as data management | VLDB / SIGMOD | Database evaluation norms differ from systems norms |
| ML and systems reshape each other; ML-quality metrics load-bearing | MLSys | Needs reviewers fluent in both accuracy and throughput |
| Provocative early idea, no full system yet | HotOS | Position-paper venue; burns no full-paper novelty |
| European community timing, same standards | EuroSys | Full peer venue with its own cycle |

Routing is about the *center of gravity*, not exclusivity — plenty of storage and
network papers appear at SOSP when the principle is systemic rather than
domain-internal. The test: which PC can evaluate the paper's hardest claim?

## Timing the call

- **Project start**: choose the target family (SOSP/OSDI-tier vs domain venue),
  because it dictates the evaluation scale you must budget for.
- **First results**: run the shape test honestly. A missing principle at this stage
  is fixable — often the principle exists but the team hasn't extracted it. Write
  the one-sentence version; if it keeps coming out as a speedup report, reroute.
- **Three months out**: lock the venue. Late switches leak time into reformatting
  and re-framing that the evaluation needed.

```text
Shape-test worksheet

Principle (one sentence, no system name allowed): <...>
  - could a different team use it in a different system?      yes/no
Embodiment: what runs today end-to-end?                        <...>
Evidence scale: hardest claim <...> needs <workload/hardware>  budgeted? yes/no
Nearest published neighbor + venue:                            <paper, venue'yy>
Center of gravity (one): OS principle / networking / storage /
  architecture / data mgmt / ML-systems / engineering lessons
-> Route: SOSP | OSDI (timing) | <domain venue> | HotOS first
```

## Anti-patterns this venue punishes

- **The 10% paper**: a measured improvement on a known design with no new
  understanding — competent, publishable, not SOSP.
- **The unbuilt design**: elegant architecture, evaluation by argument. HotOS or a
  workshop first; SOSP later, with the system.
- **The scale flex**: impressive deployment numbers, but the lesson is "we had
  more machines." ATC will value the experience report more than a SOSP PC will.
- **The camouflaged domain paper**: a database or ML paper wearing systems
  vocabulary; the PC detects the mismatch at the meeting when the hardest claim
  needs expertise the room correctly declines to fake.

## Output format

```text
[Shape test] principle / embodiment / evidence-scale — pass/fail each
[Principle] the extracted one-liner
[Route] SOSP | sibling (named) + the deciding factor
[Timing] next posted deadline for the routed venue (never an implied one)
[Risk] the anti-pattern this project is closest to
```
