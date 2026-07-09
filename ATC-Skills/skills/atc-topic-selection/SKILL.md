---
name: atc-topic-selection
description: Use when deciding whether a computer-systems project belongs at ATC (ACM SIGOPS Annual Technical Conference, formerly USENIX ATC) or should be routed to OSDI, SOSP, NSDI, EuroSys, FAST, or a workshop like HotOS/HotStorage — distinguishing ATC by its broad practical scope, its Deployed Systems / experience lane, the breadth-vs-selectivity trade, and the November/June calendar.
---

# ATC Topic Selection

Decide the venue before drafting. ATC — the ACM SIGOPS Annual Technical Conference, for about fifty
years the **USENIX Annual Technical Conference** — is the systems community's **broad, practical**
venue. It emphasizes **implementations and experimental results** across the whole systems stack and
takes a wider slice than the more selective OSDI/SOSP flagships. The decisive question is rarely "is
this systems?" but **"is this a solid, useful, measured systems result — and is ATC's breadth the
right home versus a more specialized or more selective venue?"**

## What ATC rewards

- **Built and measured systems** across a broad scope: operating systems, runtime systems, parallel
  and distributed systems, storage, networking, security and privacy, virtualization,
  hardware-software interaction, performance and workload characterization, reliability,
  availability, scalability, energy, and bug-finding / tracing / troubleshooting — "of all scales,
  from embedded devices to data centers and clouds."
- **Useful over merely novel.** A solid, well-engineered, carefully measured system that a flagship
  might call incremental is squarely in scope if it is real and the evaluation is honest.
- **Deployed-systems / experience papers.** ATC has a lane for papers about **real-world deployed
  systems that need not present new ideas** — they are judged on practical insight. (Continuity of
  the named track under SIGOPS is 待核实, but the appetite for experience papers is long-standing.)

## Sibling-venue routing table

| Signal in your project | Better home | Why |
|---|---|---|
| Solid, useful, measured systems work of broad interest; usefulness over novelty | **ATC** | The broad practical-systems venue; welcomes strong engineering + honest measurement |
| A large, novel systems contribution aimed at the flagship bar | **OSDI / SOSP** | More selective, novelty-forward; different calendars and no extended-abstract gate |
| The contribution is a **networked-systems** design (dataplane, protocols, RDMA, congestion) | **NSDI** | Networked-systems center; its own multi-deadline model |
| Broad systems, but EuroSys's cycle lands sooner or fits the community | **EuroSys** | The other broad SIGOPS-family systems conference; choose by calendar/pull |
| The core is **file and storage** systems depth | **FAST** | Storage's specialized home |
| A provocative idea or early design with argument but no built system | **HotOS / HotStorage / workshop** | Position/early-work venues; ATC wants a built, measured system |
| A real deployed system with practical lessons but no new idea | **ATC (Deployed Systems lane)** | ATC explicitly values experience papers |

## The breadth and deployed-systems tests

Two quick tests sharpen a borderline verdict:

- **Breadth-vs-selectivity test:** if the paper's strength is careful engineering and honest
  measurement of something genuinely useful — rather than a headline-novel mechanism — ATC's broad,
  practical bar fits better than OSDI/SOSP's selectivity. Do not withhold a solid, useful system
  from ATC because it is "not flagship-novel."
- **Deployed-systems test:** if the contribution is the *experience of running a real system at
  scale* — what broke, what you learned, what others should copy — ATC's experience lane is a real
  home, where "no new idea" is not a rejection reason.

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
[Calendar] compare ATC's June deadline / November conference with OSDI/NSDI/EuroSys/FAST dates
          -> route to the nearest honest fit; ATC 2026 is Hong Kong, Nov 15-18
[Bar]     is the paper "useful and solid" (ATC) or "novel and large" (OSDI/SOSP)? be honest
```

## Decision procedure

```text
[Audience]   who acts differently if the system works? -> systems builders/operators/researchers?
[Claim type] built-system / technique+implementation / architecture / experience / measurement study
[ATC vs flagship] solid+useful -> ATC; novel+large -> OSDI/SOSP
[Specialist check] network core -> NSDI; storage core -> FAST; idea-only -> HotOS/workshop
[Verdict]    ATC research track / Deployed Systems lane / sibling venue / workshop, with a one-line reason
```

Run this before the writing skills; a wrong venue decision wastes every later step. When the verdict
is ATC, continue with `atc-workflow` for the June-anchored calendar and `atc-writing-style` for the
self-standing extended abstract and the systems-paper shape.
