---
name: atc-topic-selection
description: Use when deciding whether a computer-systems project belongs at ATC (ACM SIGOPS Annual Technical Conference, formerly USENIX ATC) or should be routed to OSDI, SOSP, NSDI, EuroSys, FAST, or a workshop like HotOS/HotStorage — distinguishing ATC by its broad practical scope, its Operational Systems Track, the breadth-vs-selectivity trade, the two-submissions-per-author cap, and the January-deadline / June–July-conference calendar of ATC 2027.
---

# ATC Topic Selection

Decide the venue before drafting. ATC — the ACM SIGOPS Annual Technical Conference, for about fifty
years the **USENIX Annual Technical Conference** (retired by USENIX after ATC '25) — is the systems
community's **broad, practical**
venue. It emphasizes **implementations and experimental results** across the whole systems stack and
takes a wider slice than the more selective OSDI/SOSP flagships. The decisive question is rarely "is
this systems?" but **"is this a solid, useful, measured systems result — and is ATC's breadth the
right home versus a more specialized or more selective venue?"**

## What ATC rewards

- **Built and measured systems** across a broad scope (ATC 2027 call, re-verified 2026-11-24):
  operating systems, runtime systems, parallel and distributed systems, storage, networking, ML for
  systems and systems for ML, security and privacy, virtualization, software-hardware interactions,
  performance evaluation and workload characterization, reliability, availability, scalability,
  energy and power management, and bug-finding / tracing / troubleshooting. Submissions with new
  artifacts (traces, data, code, tools) are valued more highly.
- **Useful over merely novel — but not incremental.** A solid, well-engineered, carefully measured
  system that a flagship might call modest is in scope if it is real and the evaluation is honest;
  yet "too small or incremental over the prior state of the art" is an explicit round-one reject
  reason, so the delta must be clear by page 2.
- **Systems only.** Papers whose main contribution is outside systems research may be desk-rejected;
  quantum-computing work without clear systems contributions is out of scope.
- **Operational Systems Track.** ATC 2027 solicits papers on the design, implementation, analysis,
  and deployment experience of real systems and networks, judged on the **new insights, data, or
  lessons** they bring — "merely reporting on something in production is insufficient." Such papers
  may identify the organization behind the system. (USENIX ATC '25 called its equivalent the
  Deployed Systems Track.)

## Sibling-venue routing table

| Signal in your project | Better home | Why |
|---|---|---|
| Solid, useful, measured systems work of broad interest; usefulness over novelty | **ATC** | The broad practical-systems venue; welcomes strong engineering + honest measurement |
| A large, novel systems contribution aimed at the flagship bar | **OSDI / SOSP** | More selective, novelty-forward; different calendars (OSDI '27 closes December 8, 2026) |
| The contribution is a **networked-systems** design (dataplane, protocols, RDMA, congestion) | **NSDI** | Networked-systems center; its own multi-deadline model |
| Broad systems, but EuroSys's cycle lands sooner or fits the community | **EuroSys** | The other broad SIGOPS-family systems conference; choose by calendar/pull |
| The core is **file and storage** systems depth | **FAST** | Storage's specialized home |
| A provocative idea or early design with argument but no built system | **HotOS / HotStorage / workshop** | Position/early-work venues; ATC wants a built, measured system |
| A real deployed system with deep, new lessons but no new mechanism | **ATC (Operational Systems Track)** | Judged on insights, data, and lessons, not novelty |

## The breadth, operational-systems, and author-cap tests

Two quick tests sharpen a borderline verdict:

- **Breadth-vs-selectivity test:** if the paper's strength is careful engineering and honest
  measurement of something genuinely useful — rather than a headline-novel mechanism — ATC's broad,
  practical bar fits better than OSDI/SOSP's selectivity. Do not withhold a solid, useful system
  from ATC because it is "not flagship-novel."
- **Operational-systems test:** if the contribution is the *experience of running a real system* —
  what broke, what you learned, what others should copy — ATC's Operational Systems Track is a real
  home, provided the paper discusses deeply what is new in those lessons.
- **Author-cap test:** each author may be on at most **two** ATC 2027 submissions. If a group has
  more candidates, route the weaker fits elsewhere now rather than losing all of an author's papers
  to a desk reject.

## Evidence maturity, without the ladder cliché

Fit is necessary but not sufficient: the same idea sits at different doors depending on how far the
system has come. An idea with an argument but no implementation is a **HotOS**-style position paper;
a prototype measured only on inputs you chose needs a real testbed and workloads before the research
track; a networked-systems design whose contribution is the network belongs at **NSDI**. Submitting
one step early earns a "promising, but build and measure it" and costs a cycle.

## Cheap reconnaissance before committing

```text
[Scope]   scan the last two ATC programs (dblp: USENIX ATC; the SIGOPS ATC page) for your subarea
          -> several recent papers = a reviewer pool exists; none = opening or mismatch
[Citations] is your bibliography majority systems venues (ATC/OSDI/SOSP/NSDI/EuroSys/FAST)?
          -> majority elsewhere => reviewers read you as a visitor; naturalize the intro first
[Calendar] compare ATC 2027's 19 January 2027 deadline / 28 June - 1 July 2027 Rennes conference
          with OSDI/NSDI/EuroSys/FAST dates -> route to the nearest honest fit
          (ATC 2026, Hong Kong, 15-18 November 2026, has met)
[Bar]     is the paper "useful and solid" (ATC) or "novel and large" (OSDI/SOSP)? be honest
```

## Decision procedure

```text
[Audience]   who acts differently if the system works? -> systems builders/operators/researchers?
[Claim type] built-system / technique+implementation / architecture / experience / measurement study
[ATC vs flagship] solid+useful -> ATC; novel+large -> OSDI/SOSP
[Specialist check] network core -> NSDI; storage core -> FAST; idea-only -> HotOS/workshop
[Verdict]    ATC research track / Operational Systems Track / sibling venue / workshop, with a one-line reason
```

Run this before the writing skills; a wrong venue decision wastes every later step. When the verdict
is ATC, continue with `atc-workflow` for the January-anchored calendar and `atc-writing-style` for
self-standing first two pages and the systems-paper shape.
