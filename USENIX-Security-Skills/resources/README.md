# USENIX Security Resources

Action-oriented resources for the USENIX Security skill pack. The `skills/` give advice; this
directory lets an agent model a USENIX Security-style paper, benchmark against verified
exemplars, and prepare artifact and Open Science material without importing the economics
code kit.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`official-source-map.md`](official-source-map.md) | Confirm current-cycle USENIX Security submission, review, ethics, artifact, and formatting sources before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open official venue systems (HotCRP, CFP, Call for Artifacts, ethics guidelines, proceedings) and run the author-side verification passes. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, metadata-verified USENIX Security papers and avoid Big-Four sibling-venue confusion. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for a security measurement paper. Illustrative fictional paper; no vulnerability or vendor invented. |
| [`code/README.md`](code/README.md) | Use the shared ML/security-conference reproducibility kit: experiment matrix, artifact checklist, and a dependency-free smoke checker for artifact packages. This is not the econometrics code kit. |

## Scope Note

This is a security conference pack, not an empirical-economics journal pack. Do not copy the
Stata/DiD/IV/RDD econometrics kit here. Use the shared conference resource for experiment
design, artifact packaging, environment fingerprinting, and pre-submission package checks —
then layer the USENIX Security-specific skills (ethics, Open Science, two-phase artifact
evaluation, threat-model-faithful evaluation) on top.

## Suggested Workflow

1. Route and frame with
   [`../skills/usenixsec-topic-selection`](../skills/usenixsec-topic-selection/SKILL.md) and
   [`../skills/usenixsec-writing-style`](../skills/usenixsec-writing-style/SKILL.md).
2. Stress-test evidence with
   [`../skills/usenixsec-experiments`](../skills/usenixsec-experiments/SKILL.md),
   [`../skills/usenixsec-reproducibility`](../skills/usenixsec-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm current
   official rules in [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md).
