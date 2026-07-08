---
name: mlsys-topic-selection
description: Use when deciding whether a project belongs at MLSys rather than OSDI, SOSP, NSDI, ASPLOS, ATC, EuroSys, or the ML conferences, testing for genuine ML-systems co-design, choosing between the research and industrial tracks, and sharpening the systems-for-ML or ML-for-systems framing before writing starts.
---

# MLSys Topic Selection

Use this before writing begins. MLSys exists for work where machine learning and computer
systems constrain each other — the CFP spans **systems for ML** (training, inference,
serving, compilers, runtimes, specialized hardware, hardware-efficient methods,
benchmarks and tooling) and **ML for systems** (learned scheduling, LLM-driven hardware
design and system optimization), plus adjacent lanes like federated learning, compound AI
and agent systems, privacy/security for ML, and data preparation (2026 topics list,
verified 2026-07-08). Fit failures here are usually routing failures: strong work aimed
at the wrong reviewer pool.

## The co-design test

Ask two questions; MLSys wants both answers to be yes.

1. Does an ML property (model structure, training dynamics, tolerance to approximation,
   request patterns of ML workloads) shape the system design?
2. Does a systems property (memory hierarchy, interconnect, scheduling, cost) shape the
   ML method or its evaluation?

One yes is a re-routing signal: pure systems novelty exercised on an ML workload belongs
at a general systems venue; pure ML novelty measured for speed belongs at an ML venue.

## Routing table

| Project's center of gravity | Better venue | Why |
|---|---|---|
| New OS/storage/scheduling abstraction, ML is one workload among several | OSDI / SOSP / ATC / EuroSys | Their reviewers reward general-purpose systems depth |
| Network protocol or datacenter fabric for training traffic | NSDI / SIGCOMM | Networking-first reviewer pool |
| Microarchitecture or accelerator design | ASPLOS / ISCA / MICRO | Hardware evaluation norms (simulators, RTL) differ |
| New learning algorithm; efficiency is one experiment | NeurIPS / ICML / ICLR | Algorithmic novelty is the contribution |
| HPC-scale training on supercomputers | SC / HPDC | HPC evaluation culture |
| Mechanism where ML and system constraints genuinely interlock | **MLSys** | This is the house genre |
| Production ML system's design + deep benchmarks, limited novelty | **MLSys industrial track** (2026+) | Novelty explicitly not required there |
| Early idea, workshop-scale evidence | An MLSys-adjacent workshop first | Expanded workshop papers can return with chair approval |

## Signals your project is MLSys-shaped

- The abstract's key number is a systems metric (goodput, p99, memory, $/token) achieved
  *because of* an ML-aware design decision — not incidentally.
- The natural reviewer nightmare is "is this workload representative?" rather than "is
  this theorem tight?" or "is this abstraction general?"
- The related work splits across systems venues and ML venues — no single community owns
  the problem (see `mlsys-related-work`).
- You can promise an artifact whose evaluation is meaningful on hardware a committee can
  access — badge culture is part of this venue's identity.
- The contribution survives this compression: *"We observed [ML property]; therefore we
  built [mechanism]; which yields [measured system payoff] at [stated cost]."*

## Track choice within MLSys (2026 structure)

- **Research track**: previously unpublished ideas, full double-blind, novelty judged
  against both literatures.
- **Industrial track**: built-at-scale systems, design methodology and detailed
  benchmarks required, novelty not required, company identity may remain visible.
  Choosing it for a paper whose real asset is a clever new mechanism undersells the
  mechanism; choosing research track for a deployment report gets it rejected for
  novelty. Route by the paper's strongest honest asset.

## Sharpening moves before committing

```text
Fill these four lines; blanks are routing information.
  ML property exploited:      ______________________
  System constraint engaged:  ______________________
  Named mechanism:            ______________________
  Headline systems metric:    ______  on workload ______  vs baseline ______
If "named mechanism" is blank            -> industrial track or a workshop.
If "ML property" is blank                -> general systems venue.
If "system constraint" is blank          -> ML venue.
If the metric line is blank              -> not ready for any venue; measure first.
```

- Check the current cycle's topics list before finalizing — the venue's emphasis has
  drifted fast (the 2026 list added compound AI/agent systems and LLM-driven hardware
  design; assume continued drift).
- Consider the calendar honestly: MLSys is annual (October deadline in the 2026 cycle).
  If the project peaks in March, a systems venue with a nearer deadline may serve the
  work better than a seven-month hold.

## Vignette: three borderline projects, routed

- **A learned cost model inside a query optimizer, evaluated on analytics workloads.**
  ML-for-systems is in scope, but the reviewer pool that can judge query optimization
  depth sits at database venues. Route to MLSys only if the contribution is the
  learning-systems machinery (training-data collection, drift handling, inference
  latency budget); route to a DB venue if it is optimizer quality.
- **An INT4 quantization method with strong accuracy and a fast custom kernel.** If the
  paper's spine is the accuracy-preservation insight, ML venues fit; it becomes
  MLSys-shaped when the kernel/runtime co-design carries equal weight and the
  evaluation leads with latency-quality tradeoffs on real serving stacks — the AWQ
  pattern in `../../resources/exemplars/library.md`.
- **A cluster scheduler for mixed training/inference jobs, evaluated in simulation
  only.** Topic fits; evidence does not — simulation-only evaluation of a systems
  claim is a recognized weak pattern here. Either add a real-cluster deployment at
  modest scale or target a venue where simulation is the norm.

## Anti-patterns that fail the fit test

- "We ported X to GPUs and it is faster" — engineering without an insight that travels.
- "Our new attention variant, with a latency table" — ML paper wearing a systems hat.
- "A survey of serving systems" — MLSys publishes measured contributions, not surveys.
- "Our company's stack, described" without benchmarks — even the industrial track
  demands measurement depth.
- "Faster than a two-year-old baseline" — in a field whose systems improve monthly,
  a stale comparison fails the fit test before the novelty question is even reached.
- "We propose a benchmark" with no run rules or quality targets — the venue that
  published MLPerf holds benchmark papers to benchmark-committee standards.

## Output format

```text
[Fit] strong MLSys / MLSys-possible / route elsewhere
[Co-design test] ML->system: yes/no ; system->ML: yes/no
[Track] research / industrial / workshop-first
[Best alternative venue] <venue + reason>
[Contribution compression] observed -> built -> measured -> cost
[Next action] <measurement, mechanism naming, track decision, or reroute>
```
