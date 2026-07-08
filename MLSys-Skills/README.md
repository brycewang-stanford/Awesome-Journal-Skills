# MLSys Skills

**English** | [简体中文](README.zh-CN.md)

Twelve agent skills for papers at the Conference on Machine Learning and Systems
(MLSys) — the venue for work where machine learning and computer systems constrain and
reshape each other. The pack covers the full lifecycle: deciding whether a project is
genuinely ML-systems co-design, choosing between the research and industrial tracks,
building an evaluation that survives systems reviewers, fitting the argument into the
10-page two-column body, surviving the venue's unusually short author-response window,
and converting acceptance into camera-ready publication on proceedings.mlsys.org plus
Availability / Functional / Reproducible artifact badges.

Official basis checked on 2026-07-08: the MLSys 2026 Call for Research Papers, the
first-ever Industrial Track CFP, the Call for Artifact Evaluations, the dates and
organizing-committee pages, the OpenReview conference group, the proceedings archive,
and the author-registration FAQ. Every cycle-specific fact is traced to its source URL
in [`resources/official-source-map.md`](resources/official-source-map.md), and items
that could not be verified live are explicitly flagged 待核实 there rather than guessed.

## What makes MLSys different

This pack is written around the venue's distinctives, not generic conference advice:

- **Two reviewer cultures.** Program committees mix ML researchers with systems,
  architecture, and compiler people; a paper must name a reusable mechanism (systems
  lens) *and* show quality is preserved (ML lens). Several skills teach writing and
  responding for both audiences at once.
- **Benchmark rigor as identity.** The MLPerf Training methodology was published in
  MLSys's own proceedings, and its measurement culture — defined workloads, run rules,
  tails not means — is the evaluation standard reviewers apply.
- **Badge-driven artifact evaluation.** A separate post-acceptance committee runs your
  code and awards Availability, Functional, and Reproducible badges, with Distinguished
  Artifact Awards on top; packaging for re-measurement is a first-class skill here.
- **A compressed rebuttal.** The 2026 cycle gave authors four days between review
  release and response deadline — rebuttal strategy at MLSys is a scheduling problem.
- **Two tracks since 2026.** The research track demands novelty under full double-blind;
  the industrial track wants production-scale design and benchmarks, novelty explicitly
  not required, with company identity allowed to remain visible.
- **Performance claims with four coordinates.** Throughput, latency tails, memory, and
  cost travel together; naked speedups are treated as marketing.

## Skills

### Getting in

- [`mlsys-topic-selection`](skills/mlsys-topic-selection/SKILL.md) — apply the co-design
  test, route against OSDI/SOSP/NSDI/ASPLOS/ATC/EuroSys and the ML conferences, choose
  research vs industrial track, and compress the contribution into one testable sentence.
- [`mlsys-experiments`](skills/mlsys-experiments/SKILL.md) — defend workload
  representativeness, enforce baseline tuning symmetry, report the
  throughput/latency/memory/cost quartet, and build ablations that attribute gains to
  mechanisms.
- [`mlsys-writing-style`](skills/mlsys-writing-style/SKILL.md) — open with a measured
  bottleneck, name the mechanism, structure the evaluation as research questions
  (including the mandatory "when does it not help" and "what does it cost"), and
  compress into 10 two-column pages.
- [`mlsys-related-work`](skills/mlsys-related-work/SKILL.md) — cover the five literature
  lanes of a field scattered across venues, cite version-pinned open-source systems,
  handle arXiv-first prior work, and write a delta statement both reviewer cultures
  accept.

### Submitting and being reviewed

- [`mlsys-submission`](skills/mlsys-submission/SKILL.md) — audit the 10-page body,
  separate appendix upload, full-author references, double-blind-with-arXiv-allowed
  anonymity, dual-submission exceptions, and desk-reject triggers.
- [`mlsys-supplementary`](skills/mlsys-supplementary/SKILL.md) — split body versus
  appendix knowing reviewers are not obliged to read the appendix, structure the
  separate file for auditability, and keep traces and configs blinded.
- [`mlsys-reproducibility`](skills/mlsys-reproducibility/SKILL.md) — pin the system
  layer from driver to interconnect, separate ML randomness from systems noise, choose
  trial counts and variance reporting, and run the fresh-machine drill.
- [`mlsys-review-process`](skills/mlsys-review-process/SKILL.md) — model the OpenReview
  pipeline, the two-culture reviewer pool, industrial-track review axes, and what
  decisions actually turn on.
- [`mlsys-author-response`](skills/mlsys-author-response/SKILL.md) — run the four-day
  response clock: hour-zero triage, the two runnable experiments, and reply skeletons
  for the classic systems-reviewer objections.

### After acceptance

- [`mlsys-camera-ready`](skills/mlsys-camera-ready/SKILL.md) — de-anonymize without
  leaking debris, restore production context with employer approval, reconcile
  rebuttal promises, and sequence against the artifact deadline and the reserved-ticket
  registration window.
- [`mlsys-artifact-evaluation`](skills/mlsys-artifact-evaluation/SKILL.md) — target
  badges honestly, tier claims by the hardware evaluators can access, package with
  pinned system layers, and stay responsive through the anonymous evaluation window.
- [`mlsys-workflow`](skills/mlsys-workflow/SKILL.md) — plan the annual cycle backward
  from the October deadline with GPU time as the critical path, pre-commit the
  response-week protocol, and assign the five ownership hats.

## How the skills chain together

A typical research-track project touches the pack in this order:

1. **Route** — `mlsys-topic-selection` runs the co-design test and the track decision;
   if the answer is "route elsewhere," stop here and save a year.
2. **Design the evidence** — `mlsys-experiments` fixes workloads, baselines, and the
   reporting quartet *before* GPU-hours are spent; `mlsys-reproducibility` sets up the
   measurement harness and environment pins at the same time, because retrofitting
   them after the sweep means re-running the sweep.
3. **Write** — `mlsys-writing-style` shapes the first page and the RQ-structured
   evaluation; `mlsys-related-work` builds the five-lane positioning;
   `mlsys-supplementary` splits body from the separately-uploaded appendix.
4. **Ship** — `mlsys-submission` runs the compliance and desk-reject audit;
   `mlsys-workflow` has been tracking gates and owners since step 1.
5. **Defend** — `mlsys-review-process` interprets the review packet;
   `mlsys-author-response` executes the four-day clock.
6. **Deliver** — `mlsys-camera-ready` and `mlsys-artifact-evaluation` run in parallel
   after acceptance, sharing the same weeks and mostly the same people.

Industrial-track projects skip nothing: they swap the novelty framing for design-
methodology depth and add an internal-approval owner (see `mlsys-workflow`).

## Who this pack is for

- Research groups deciding whether their systems result belongs at MLSys or at
  OSDI/ASPLOS/NSDI — and what changes if the answer is MLSys.
- Industry teams considering the (new in 2026) industrial track, where the bar is
  benchmark and methodology depth rather than novelty.
- Authors who have an acceptance and now face the camera-ready / artifact-evaluation /
  registration pile-up between late January and early April.
- Agents drafting, auditing, or responding on behalf of any of the above, with the
  source map keeping them honest about which facts are verified and which are 待核实.

## Resources

| Resource | Purpose |
| --- | --- |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional abstract/introduction rewritten from product-announcement voice into the MLSys arc: measured bottleneck → insight → named mechanism → ranged payoff → honest tradeoff. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five verified MLSys-native exemplars (FlexFlow/SOAP, MLPerf Training, FedProx, transformer-inference scaling, AWQ) plus the misattribution traps (vLLM, PipeDream, FlashAttention are *not* MLSys papers). |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Source URL and access date for every 2026-cycle fact, and the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live links: both CFPs, the AE call, dates page, OpenReview group, proceedings archive, registration FAQ. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter that bends the shared ML-conference reproducibility kit toward system-layer pinning and badge-tier packaging. |

## Verified 2026-cycle anchors (replace before reuse)

- Ninth conference, May 18-22, 2026, Hyatt Regency Bellevue; began as SysML (2018,
  Stanford), renamed MLSys with the 2020 Austin edition.
- Paper deadline October 30, 2025; reviews January 12; responses January 16;
  notifications January 25-26, 2026.
- Submissions: two-column, 10 pages excluding references, all authors listed per
  reference, unlimited appendix as a separate simultaneous upload that reviewers need
  not read.
- Double-blind with arXiv posting allowed; industrial-track papers hide author names
  but may keep company identity.
- Artifact evaluation: submission by March 8, 2026; window March 8 - April 8; badges
  Availability, Functional, Reproducible; Distinguished Artifact Awards.
- Leadership (rotates yearly): General Chair Luis Ceze; Program Chairs Zhihao Jia and
  Aakanksha Chowdhery. No APC; open proceedings at proceedings.mlsys.org.

## Maintenance notes

- Reopen mlsys.org, both CFPs, the AE call, and the OpenReview group before any
  deadline-sensitive advice; MLSys restructures its calls between cycles, and the
  Industrial Track is only one cycle old.
- Camera-ready limits, presentation obligations, AI-use policy, and all MLSys 2027
  facts were unverifiable on 2026-07-08 and are marked 待核实 — do not let an agent
  state them as fact until re-checked.
- Treat every 2026 date and page count in this pack as a historical anchor describing
  the venue's shape, never as the next cycle's rule.
