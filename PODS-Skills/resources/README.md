# ACM PODS Resources

Action-oriented resources for the PODS skill pack. The `skills/` give advice; this directory lets
an agent model a PODS-shaped (theory) paper, benchmark against verified exemplars, and prepare the
proof appendix and full-version-on-arXiv package for the multi-cycle, lightweight double-anonymous,
revision-capable PODS process that publishes in the **PODS track of PACMMOD**.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for a database-theory paper that leads with a crisp model and a tight-bound claim. Illustrative fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, verified PODS papers across contribution shapes, and avoid confusion with SIGMOD/VLDB/ICDE (systems) and PODC (distributed computing). |
| [`official-source-map.md`](official-source-map.md) | Confirm the current-cycle PODS deadlines, page budget, review model, PACMMOD publication, and awards before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open the official PODS, PACMMOD, EasyChair, and sigmod.org award surfaces, plus the cross-check sources for when the gateway blocks a direct fetch. |
| [`code/README.md`](code/README.md) | Adapt the shared submission-readiness tooling to a theory paper: a claim-to-proof matrix, a proof-appendix checklist, and an anonymity sweep — no code artifact, because PODS has none. |

## Scope Note

This is a database-**theory** symposium pack. PODS is co-located with SIGMOD but its papers are
theorems, models, and bounds — not systems or benchmark results. Do **not** import a systems-DB
artifact-evaluation kit, a TPC-style benchmark harness, or an ML-leaderboard framing. PODS evidence
is a **correct, complete proof** with the appendix incorporated at submission and, by community norm,
a full version on arXiv. The review is multi-cycle, lightweight double-anonymous, with a shepherded
**revision** round, and the paper publishes in the **PACMMOD PODS track**.

## Suggested Workflow

1. Route and frame with
   [`../skills/pods-topic-selection`](../skills/pods-topic-selection/SKILL.md) and
   [`../skills/pods-writing-style`](../skills/pods-writing-style/SKILL.md) — deciding PODS vs.
   SIGMOD/ICALP/LICS before writing is the highest-leverage move.
2. Build and check the theory with
   [`../skills/pods-experiments`](../skills/pods-experiments/SKILL.md) (analyses, bounds, and
   separations) and [`../skills/pods-reproducibility`](../skills/pods-reproducibility/SKILL.md)
   (a self-contained, verifiable proof).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm the live cycle in
   [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) before the EasyChair audit in
   [`../skills/pods-submission`](../skills/pods-submission/SKILL.md).
