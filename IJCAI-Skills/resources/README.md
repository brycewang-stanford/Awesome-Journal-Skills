# IJCAI Resources

Action-oriented resources for the IJCAI (International Joint Conference on Artificial Intelligence) skill
pack. The `skills/` give advice; this directory lets an agent **act** — model an IJCAI-style first page and
benchmark against verified exemplars. Pair these with the relevant `skills/ijcai-*/SKILL.md`.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a paper **abstract + introduction** in IJCAI house style (broad AI, problem + gap + core idea + evidence, page-limited, contribution on page one). Illustrative fictional paper — no policy claims. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified IJCAI papers** organized by topic × method. Framing and design positioning only — no fabricated numbers. Includes a sibling-confusion guard (IJCAI is not AAAI/NeurIPS/ICML/ICLR/ACL/AAMAS/KR). |
| [`official-source-map.md`](official-source-map.md) | **IJCAI-specific policy & facts:** Chairing Tool submission, 7+2 page limit, two-phase review, double-blind anonymity, author response, reproducibility rubric, COI policy, and the authoritative source URLs. The authoritative pack source. |
| [`external_tools.md`](external_tools.md) | Official IJCAI workflow links and author-side submission checks. |
| [`code/README.md`](code/README.md) | Use the shared ML conference reproducibility kit: experiment matrix, artifact checklist, and a dependency-free smoke checker for anonymous reproduction packages. This is not the econometrics code kit. |

## Suggested workflow

1. Scope and frame with [`../skills/ijcai-topic-selection`](../skills/ijcai-topic-selection/SKILL.md) and
   [`../skills/ijcai-writing-style`](../skills/ijcai-writing-style/SKILL.md); model the abstract + intro on
   [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md).
2. Lock the experimental story with
   [`../skills/ijcai-experiments`](../skills/ijcai-experiments/SKILL.md) and the reproducibility evidence in
   [`../skills/ijcai-reproducibility`](../skills/ijcai-reproducibility/SKILL.md).
3. Benchmark your topic × method against verified IJCAI papers in
   [`exemplars/library.md`](exemplars/library.md).
4. Audit submission readiness with
   [`../skills/ijcai-submission`](../skills/ijcai-submission/SKILL.md); confirm current deadlines, page
   limits, anonymity, and LLM-use rules in [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) before upload.

## Scope note — no econometric code kit

This is an **AI-conference** pack. Unlike the economics journal packs, it deliberately does **not** vendor a
causal-inference / econometrics code kit (no Stata or DiD/IV/RDD pipeline): that toolchain is not the
methodology IJCAI submissions are built on. Empirical rigor for IJCAI is instead about strong baselines,
ablations, statistical evidence, reproducibility, and compute reporting — see
[`../skills/ijcai-experiments`](../skills/ijcai-experiments/SKILL.md) and
[`../skills/ijcai-reproducibility`](../skills/ijcai-reproducibility/SKILL.md). All IJCAI-specific policy lives
in [`official-source-map.md`](official-source-map.md), reopened against the current cycle's official pages.
