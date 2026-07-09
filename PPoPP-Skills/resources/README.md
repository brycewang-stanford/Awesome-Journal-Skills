# PPoPP Resources

Action-oriented resources for the PPoPP skill pack. The `skills/` give advice; this directory lets
an agent model a PPoPP-shaped paper, benchmark against verified exemplars, and prepare a
reproducible parallel-performance artifact for the double-blind review and the CGO-shared,
post-acceptance artifact-evaluation track.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for a parallel-programming paper (a fictional lock-free index). Illustrative only; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, verified PPoPP papers across contribution shapes (runtimes, concurrent structures, graph frameworks, GPU), and avoid sibling-venue confusion with PLDI, CGO, POPL, ASPLOS, SPAA, and SC. |
| [`official-source-map.md`](official-source-map.md) | Confirm the current-cycle PPoPP deadline(s), the 10-page two-column budget, the double-blind + rebuttal model, and the artifact-badge policy before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open the official PPoPP, HotCRP, SIGPLAN, and ACM artifact surfaces, plus cross-check sources for when the gateway blocks a direct fetch. |
| [`code/README.md`](code/README.md) | Use the shared replication-package tooling, plus the parallel-measurement checks (pinning, topology, trend portability) the generic kit cannot make. |

## Scope note

This is a **parallel-programming** conference pack, not a compiler pack, a semantics pack, or an
architecture pack. Do not import a CGO/PLDI compiler-pass framing, a POPL proof-only framing, or an
ASPLOS microarchitecture framing. PPoPP evidence is **twin evidence**: an argument that the result
is **correct under concurrency** (races, linearizability/progress, the memory model) *and*
measurement that it **scales** (speedup curves, core/GPU sweeps, NUMA effects) against a strong,
real baseline — carried through a double-blind review with a single written rebuttal.

## Suggested workflow

1. Route and frame with
   [`../skills/ppopp-topic-selection`](../skills/ppopp-topic-selection/SKILL.md) and
   [`../skills/ppopp-writing-style`](../skills/ppopp-writing-style/SKILL.md) — deciding PPoPP vs.
   CGO/PLDI/POPL/ASPLOS before writing is the highest-leverage move.
2. Build evidence with [`../skills/ppopp-experiments`](../skills/ppopp-experiments/SKILL.md),
   [`../skills/ppopp-reproducibility`](../skills/ppopp-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md) — capturing hardware/topology at run time.
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm the live cycle in
   [`official-source-map.md`](official-source-map.md) and [`external_tools.md`](external_tools.md)
   before the HotCRP audit in
   [`../skills/ppopp-submission`](../skills/ppopp-submission/SKILL.md).
