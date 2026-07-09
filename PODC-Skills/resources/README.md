# PODC Resources

Action-oriented resources for the PODC skill pack. The `skills/` give advice; this directory lets
an agent model a PODC-shaped result, benchmark against verified exemplars, and prepare the proof
appendix and any optional simulation for the lightweight double-blind, proofs-centric PODC process.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for a distributed-computing-theory paper (a fictional consensus result). Illustrative only; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, web-verified PODC papers across contribution shapes, and avoid sibling-venue confusion with DISC, SPAA, STOC/FOCS, and journals. |
| [`official-source-map.md`](official-source-map.md) | Confirm the current-cycle PODC dates, the 10-page-merits budget, the double-blind model, the Brief Announcements limits, and the no-artifact-track reality before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open the official PODC, HotCRP, `acmart`, and award surfaces, plus the cross-check sources (dblp, ACM DL, DMANET) for when the gateway blocks a direct fetch. |
| [`code/README.md`](code/README.md) | Adapt the optional-simulation / proof-checking tooling a theory paper may ship, and run the PODC-specific pre-submission checks the generic kit cannot make. |

## Scope Note

This is a **distributed-computing-theory** conference pack whose contribution is a **model, a
theorem, and a proof** — not an ML-conference pack and not a systems-measurement pack. Do not import
the OpenReview/PMLR machinery, the ACM artifact-badge workflow, or a benchmark-leaderboard framing.
PODC evidence is a **proof**: a precise model box, a result statement up front, tight or matching
bounds, and a self-contained proof appendix carried through a lightweight double-blind review with
no revision round. The `podc-artifact-evaluation` skill exists only to redirect artifact-culture
energy into proof-appendix and assumption rigor, because PODC has no artifact track.

## Suggested Workflow

1. Route and frame with
   [`../skills/podc-topic-selection`](../skills/podc-topic-selection/SKILL.md) and
   [`../skills/podc-writing-style`](../skills/podc-writing-style/SKILL.md) — deciding PODC vs.
   DISC/SPAA/STOC/PODS before writing is the highest-leverage move.
2. Build the result with [`../skills/podc-experiments`](../skills/podc-experiments/SKILL.md) (the
   theory analogue: tight/matching bounds and model stress-tests),
   [`../skills/podc-reproducibility`](../skills/podc-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm the live cycle in
   [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) before the HotCRP audit in
   [`../skills/podc-submission`](../skills/podc-submission/SKILL.md) — including the
   regular-vs-Brief-Announcement choice.
