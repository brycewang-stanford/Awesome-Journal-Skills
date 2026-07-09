# EACL Resources

Reference material behind the EACL skill pack. Where the `skills/` folder tells an agent what to do at
each stage, this folder gives it the raw material: a house-style writing target, an Anthology-verified
set of EACL exemplars to benchmark against, the exact official sources with their access dates, and a
pointer to shared reproducibility tooling for the August ARR cycle. None of it is an economics code kit.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite in EACL house style. Illustrative fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, verified EACL papers and avoid sibling-venue misattribution. |
| [`official-source-map.md`](official-source-map.md) | Confirm current EACL/ARR submission, review, commitment, formatting, and policy sources before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open the official ARR, OpenReview, EACL, and ACL Anthology surfaces and the stage-by-stage author checks. |
| [`code/README.md`](code/README.md) | Use the shared ML-conference reproducibility kit: experiment matrix, artifact checklist, and a dependency-free smoke checker for anonymous ARR supplements. This is not the econometrics code kit. |

## Scope note

EACL routes through ACL Rolling Review; treat this as an NLP-conference resource set, never as an
economics-journal one. The Stata/DiD/IV/RDD econometrics kit does not belong here. For experiment
planning, artifact packaging, seed and compute reporting, and anonymous-supplement smoke checks, defer
to the shared ML-conference kit and add EACL's own policy — single cycle, Limitations, Responsible NLP
checklist, commitment — on top of it.

## Suggested workflow

1. Route and frame with
   [`../skills/eacl-topic-selection`](../skills/eacl-topic-selection/SKILL.md) and
   [`../skills/eacl-writing-style`](../skills/eacl-writing-style/SKILL.md).
2. Stress-test evidence with [`../skills/eacl-experiments`](../skills/eacl-experiments/SKILL.md),
   [`../skills/eacl-reproducibility`](../skills/eacl-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm current official rules
   in [`official-source-map.md`](official-source-map.md) and [`external_tools.md`](external_tools.md)
   before the single ARR cycle deadline.
