# ACM CCS Resources

Action-oriented resources for the ACM CCS skill pack. The `skills/` give advice; this
directory lets an agent model a CCS-style security paper, benchmark against verified
exemplars, and prepare artifacts without importing an unrelated code kit.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for a CCS security paper — threat model on the first page, calibrated claims, evidence pairing. Illustrative fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, verified CCS papers (including Test-of-Time winners) and avoid sibling-venue misattribution. |
| [`official-source-map.md`](official-source-map.md) | Confirm current-cycle CCS submission, review, format, ethics, and artifact sources before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open official venue systems, HotCRP cycle sites, proceedings, and author-instruction links. |
| [`code/README.md`](code/README.md) | Use the shared ML/CS conference reproducibility kit: experiment matrix, artifact checklist, and a dependency-free smoke checker for reproduction packages. |

## Scope note

This is a security-conference pack, not an ML or economics pack. The advice centers on threat
models, adaptive-attack evaluation, responsible disclosure, ethics sections, and ACM artifact
badges. The shared reproducibility kit under `code/` is a generic smoke check only — CCS
policy always comes from the current CFP and call for artifacts.

## Suggested workflow

1. Route and frame with
   [`../skills/ccs-topic-selection`](../skills/ccs-topic-selection/SKILL.md) and
   [`../skills/ccs-writing-style`](../skills/ccs-writing-style/SKILL.md).
2. Stress-test evidence with [`../skills/ccs-experiments`](../skills/ccs-experiments/SKILL.md),
   [`../skills/ccs-reproducibility`](../skills/ccs-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm current
   official rules in [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md).
