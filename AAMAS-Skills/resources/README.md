# AAMAS Resources

Action-oriented resources for the AAMAS skill pack. The `skills/` give advice; this directory
lets an agent model an AAMAS-style paper, benchmark against verified exemplars from the
autonomous-agents and multiagent-systems literature, and prepare reproduction artifacts
without importing any economics or generic-ML kit wholesale.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for a multiagent paper, where agent interaction and an equilibrium or coordination claim lead the first page. Illustrative fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, dblp-verified AAMAS papers across MARL, security games, negotiation, and multiagent learning, and avoid sibling-venue confusion. |
| [`official-source-map.md`](official-source-map.md) | Confirm current-cycle AAMAS submission, review, track, formatting, and policy sources before giving submission-ready advice, with the 403 access-method note. |
| [`external_tools.md`](external_tools.md) | Open the official IFAAMAS/AAMAS CFP, submission, OpenReview, JAAMAS, and proceedings links. |
| [`code/README.md`](code/README.md) | Use the shared ML-conference reproducibility kit for experiment matrices, artifact checklists, and a dependency-free smoke check on an anonymous multiagent reproduction package. |

## Scope Note

This is an autonomous-agents and multiagent-systems conference pack, not a single-agent
deep-learning benchmark pack and not an empirical-economics journal pack. The distinctive
object here is **interaction**: strategy, incentives, equilibria, coordination, negotiation,
mechanism design, and multiagent learning dynamics. Use the shared ML-conference resource for
seed/compute reporting and anonymous-package hygiene, but let the AAMAS skills drive what
counts as evidence that an *interaction* claim is real.

## Suggested Workflow

1. Route and frame with
   [`../skills/aamas-topic-selection`](../skills/aamas-topic-selection/SKILL.md) and
   [`../skills/aamas-writing-style`](../skills/aamas-writing-style/SKILL.md).
2. Stress-test evidence with [`../skills/aamas-experiments`](../skills/aamas-experiments/SKILL.md),
   [`../skills/aamas-reproducibility`](../skills/aamas-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm current
   official track rules in [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) before the rebuttal and camera-ready stages.
