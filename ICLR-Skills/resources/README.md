# ICLR Resources

Action-oriented resources for the ICLR (International Conference on Learning Representations) skill pack.
The `skills/` give advice; this directory lets an agent **act** — model an ICLR-style abstract +
introduction, benchmark against verified ICLR exemplars, and confirm ICLR-specific policy before a
deadline. Pair these with the relevant `skills/iclr-*/SKILL.md`.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of an ICLR **abstract + introduction** in house style (first-page insight, declared contribution type, each claim matched to a verifiable experiment, reviewer-navigation path, honest limitation). Illustrative **fictional** paper — no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified ICLR papers** organized by topic × method. Design positioning only — no fabricated metrics. Includes a sibling-confusion guard (ICLR is not NeurIPS / ICML / CVPR / AAAI / ACL). |
| [`official-source-map.md`](official-source-map.md) | **ICLR-specific policy & facts:** OpenReview double-blind submission, 2026 page limits, reciprocal reviewing, LLM-use disclosure, Code of Ethics/Conduct, dual-submission and supplementary rules, plus the cycle-volatile items to re-check. The authoritative pack source. |
| [`external_tools.md`](external_tools.md) | Official ICLR workflow links (CFP, Author Guide, Reviewer Guide, OpenReview group, LLM policy) and author-side anonymity/artifact checks. |
| [`code/README.md`](code/README.md) | Use the shared ML conference reproducibility kit: experiment matrix, artifact checklist, and a dependency-free smoke checker for anonymous reproduction packages. This is not the econometrics code kit. |

## ML-conference pack — note on scope

This is an **ML-conference** pack. It deliberately does **not** vendor the econometrics code kit (the
Stata + Python causal-inference pipeline shipped with the economics journal packs): that kit targets
DID / IV / RDD / DML empirical-micro pipelines, which are not the ICLR contribution shape. ICLR work is
verified through **reproducible artifacts, seeds, ablations, and compute reporting** (see
[`../skills/iclr-reproducibility/SKILL.md`](../skills/iclr-reproducibility/SKILL.md) and
[`../skills/iclr-experiments/SKILL.md`](../skills/iclr-experiments/SKILL.md)) rather than a vendored
econometrics toolkit. Use an anonymized code/artifact repository per the Author Guide instead.

## Suggested workflow

1. **Scope and route** with [`../skills/iclr-topic-selection`](../skills/iclr-topic-selection/SKILL.md):
   confirm the project is ICLR-shaped (a representation/optimization/generative/graph/analysis insight)
   rather than NeurIPS/ICML/CVPR/AAAI/ACL-shaped.
2. **Frame the paper** with [`../skills/iclr-writing-style`](../skills/iclr-writing-style/SKILL.md) and
   model the abstract + intro on [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md)
   (first-page insight, declared contribution type, reviewer-navigation path).
3. **Stress-test evidence** with [`../skills/iclr-experiments`](../skills/iclr-experiments/SKILL.md) and
   [`../skills/iclr-reproducibility`](../skills/iclr-reproducibility/SKILL.md): each claim → one
   experiment, multi-seed variance, isolating ablation, compute disclosure.
4. **Benchmark** against verified ICLR papers in [`exemplars/library.md`](exemplars/library.md); study how
   a simple, verifiable claim carries a community-wide lesson.
5. **Clear submission** with [`../skills/iclr-submission`](../skills/iclr-submission/SKILL.md), confirming
   OpenReview/anonymity/page-limit/LLM-disclosure facts in
   [`official-source-map.md`](official-source-map.md) and the live links in
   [`external_tools.md`](external_tools.md). ICLR policy is cycle-specific — reopen the current CFP and
   Author Guide before acting.
