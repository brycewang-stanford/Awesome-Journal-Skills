# AAAI Resources

Action-oriented resources for the AAAI Conference on Artificial Intelligence skill pack. The `skills/`
give advice; this directory lets an agent **act** — model an AAAI-style first page and benchmark against
verified main-conference exemplars. Pair these with the relevant `skills/aaai-*/SKILL.md`.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a paper **abstract + introduction** in AAAI house style (AI problem → contribution type → evidence on the first page, page-limited). Illustrative fictional paper; no AAAI policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified AAAI main-conference papers** organized by topic × method. Design positioning only — no fabricated metrics. Includes a sibling-confusion guard (AAAI is not IJCAI/NeurIPS/ICML/ICLR/ACL/CVPR/workshop/symposium/AI Magazine). |
| [`official-source-map.md`](official-source-map.md) | **AAAI-specific policy & facts:** OpenReview double-blind submission, two-phase review, 7-page technical limit, reproducibility checklist, supplementary-material rules, author limits, and AAAI AI-use policy. The authoritative pack source. |
| [`external_tools.md`](external_tools.md) | Official AAAI workflow links (conference page, Author Kit, CFP, submission instructions, review process, rebuttal FAQ) and author-side checks. |
| [`code/README.md`](code/README.md) | Use the shared ML conference reproducibility kit: experiment matrix, artifact checklist, and a dependency-free smoke checker for anonymous reproduction packages. This is not the econometrics code kit. |

## Scope note — no econometrics code kit vendored

This is an **AI-conference** pack. Unlike the economics journal packs, it deliberately does **not**
vendor the shared Stata/Python causal-inference econometrics kit: that econometrics pipeline is out of
scope for AAAI submissions. The local `code/` directory instead points to the shared ML-conference
reproducibility kit. Reproducibility for AAAI is handled through the venue's own reproducibility
checklist and supplementary ZIP categories — see
[`official-source-map.md`](official-source-map.md) and the
[`aaai-reproducibility`](../skills/aaai-reproducibility/SKILL.md) and
[`aaai-experiments`](../skills/aaai-experiments/SKILL.md) skills.

## Suggested workflow

1. Decide fit and frame with [`../skills/aaai-topic-selection`](../skills/aaai-topic-selection/SKILL.md)
   and [`../skills/aaai-writing-style`](../skills/aaai-writing-style/SKILL.md); model the abstract + intro
   on [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md).
2. Build the evidence with [`../skills/aaai-experiments`](../skills/aaai-experiments/SKILL.md) and
   [`../skills/aaai-reproducibility`](../skills/aaai-reproducibility/SKILL.md), keeping every claim mapped
   to an experiment.
3. Benchmark your framing against verified AAAI main-conference papers in
   [`exemplars/library.md`](exemplars/library.md).
4. Audit submission readiness with [`../skills/aaai-submission`](../skills/aaai-submission/SKILL.md), and
   confirm the current policy, page limit, and AI-use rules in
   [`official-source-map.md`](official-source-map.md) — reopen the official pages in
   [`external_tools.md`](external_tools.md), since AAAI rules are cycle- and track-specific.
