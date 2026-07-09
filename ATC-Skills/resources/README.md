# ATC Resources

Action-oriented resources for the ATC skill pack. The `skills/` give advice; this directory lets an
agent model an ATC-shaped systems paper, benchmark against verified exemplars, and prepare a
runnable artifact for the double-blind, two-round, shepherded ACM SIGOPS process.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after extended-abstract + introduction rewrite for a systems paper. Illustrative fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, verified USENIX ATC papers across contribution shapes, and avoid sibling-venue confusion with OSDI, SOSP, NSDI, EuroSys, and FAST. |
| [`official-source-map.md`](official-source-map.md) | Confirm the current-cycle ATC deadline, two-round review model, page budget, artifact badges, and the USENIX-to-SIGOPS transition status before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open the SIGOPS ATC, HotCRP, USENIX-legacy, and ACM surfaces, plus the cross-check sources for when the gateway blocks a direct fetch. |
| [`code/README.md`](code/README.md) | Use the shared replication-package tooling: a claim-to-experiment matrix, an artifact-badge checklist, and a dependency-free smoke checker for anonymized artifacts. |

## Scope note

This is a computer-**systems** conference pack: real implementations, measured performance, and
runnable artifacts. Do not import the OpenReview/PMLR machinery from the ML packs or the
Stata/DiD/IV econometrics kit from the journal packs. ATC evidence is systems evidence — testbeds,
end-to-end and microbenchmark measurements, tail-latency and variance reporting, and an inspectable
artifact — carried through a **two-round, extended-abstract, double-blind** review and a
**shepherded conditional acceptance**. And remember the venue moved: ATC 2026 is the first ACM
SIGOPS edition of what was USENIX ATC, so verify every mechanic against the current SIGOPS call.

## Suggested workflow

1. Route and frame with
   [`../skills/atc-topic-selection`](../skills/atc-topic-selection/SKILL.md) and
   [`../skills/atc-writing-style`](../skills/atc-writing-style/SKILL.md) — deciding ATC vs.
   OSDI/NSDI/EuroSys/FAST before writing, and making the extended abstract self-standing, are the
   highest-leverage moves.
2. Build evidence with [`../skills/atc-experiments`](../skills/atc-experiments/SKILL.md),
   [`../skills/atc-reproducibility`](../skills/atc-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm the live cycle in
   [`official-source-map.md`](official-source-map.md) and [`external_tools.md`](external_tools.md)
   before the HotCRP audit in [`../skills/atc-submission`](../skills/atc-submission/SKILL.md).
