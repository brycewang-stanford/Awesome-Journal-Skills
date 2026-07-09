# HPCA Resources

Action-oriented resources for the HPCA skill pack. The `skills/` give advice; this
directory lets an agent model an HPCA-style paper, benchmark against verified
Test-of-Time exemplars, and prepare evaluation and artifact material without
importing the wrong toolkit.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for a high-performance-architecture paper. Illustrative fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, dblp-verified HPCA Test of Time Award papers and avoid sibling-venue (ISCA/MICRO/ASPLOS) confusion. |
| [`official-source-map.md`](official-source-map.md) | Confirm current-cycle HPCA submission, review, formatting, and policy sources before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open official venue systems, the HotCRP portals, proceedings, and author-instruction links. |
| [`code/README.md`](code/README.md) | Adapt the shared conference reproducibility kit, plus the five architecture-specific checks (simulator pinning, figure traceability, workload licensing, machine state, evaluator budgets) the generic tooling skips. |

## Scope note

This is a computer-architecture pack whose evaluation culture is *machine-grade*:
cycle-level simulators with a declared fidelity scope, real silicon with pinned
firmware and captured governor/turbo state, or FPGA prototypes with reported
utilization. Do not import statistical-ML checklist habits (seeds-and-error-bars
alone) as if they were sufficient here, and do not import econometrics tooling at
all. The reproducibility scaffold is a smoke check, not a substitute for the
hardware-shaped checks the skills describe.

Note the venue-specific plumbing: HPCA is **IEEE-only (TCCA)**, so its badging is
**IEEE reproducibility badging** on a **separate AE HotCRP**, and its template and
rights forms are IEEE — never the ACM badge names, ACM AE policy, or DL conventions
you would use for ISCA, MICRO, or ASPLOS.

## Suggested workflow

1. Route and frame with
   [`../skills/hpca-topic-selection`](../skills/hpca-topic-selection/SKILL.md) and
   [`../skills/hpca-writing-style`](../skills/hpca-writing-style/SKILL.md).
2. Stress-test evidence with
   [`../skills/hpca-experiments`](../skills/hpca-experiments/SKILL.md),
   [`../skills/hpca-reproducibility`](../skills/hpca-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm
   current official rules in [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) before the July gate.
