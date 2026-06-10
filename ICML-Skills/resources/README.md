# ICML Resources

Action-oriented resources for the ICML (International Conference on Machine Learning) skill pack. The
`skills/` give advice; this directory lets an agent **model** an ICML-style abstract/introduction and
**benchmark** against verified ICML exemplars. Pair these with the relevant
`skills/icml-*/SKILL.md`.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of an ML paper **abstract + introduction** in ICML house style — precise problem → originality gap → reviewer-evaluable contribution (method/theorem) → previewed evidence (baselines, ablation, variance) → bounded claim + proportionate impact statement. Illustrative fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified ICML papers** organized by method × topic, each confirmed in its PMLR/ICML proceedings volume. Design positioning only — no fabricated metrics. Includes a sibling-venue guard (ICML is **not** NeurIPS/ICLR/CVPR/AAAI/JMLR/UAI). |
| [`official-source-map.md`](official-source-map.md) | **ICML-specific policy & facts:** OpenReview submission, LaTeX-only style, 8-page body, anonymity/double-blind, supplementary-material classes, impact statement, lay summary, LLM/prompt-injection policy, and the authoritative `icml.cc/Conferences/2026` source list. The authoritative pack source. |
| [`external_tools.md`](external_tools.md) | External ICML tools and links (CFP, Author Instructions, Peer Review FAQ, OpenReview group, PMLR, format checker) — re-check every cycle. |
| [`code/README.md`](code/README.md) | Use the shared ML conference reproducibility kit: experiment matrix, artifact checklist, and a dependency-free smoke checker for anonymous reproduction packages. This is not the econometrics code kit. |

## Scope note: no econometric code kit vendored

This is a **machine-learning conference** pack, so the econometrics / causal-inference Stata + Python
code kit used by the economics journal packs is **deliberately not vendored here** — it is the wrong
discipline for ICML. For reproducible ML evidence, ICML's own reproducibility, experiments, and
supplementary-material guidance carry the load:

- [`../skills/icml-reproducibility/SKILL.md`](../skills/icml-reproducibility/SKILL.md) — code/data
  availability, seeds, compute disclosure, anonymized review package, exact commands.
- [`../skills/icml-experiments/SKILL.md`](../skills/icml-experiments/SKILL.md) — baselines, ablations,
  seed variance, leakage, compute fairness, and keeping decisive evidence in the main 8 pages.
- [`../skills/icml-supplementary/SKILL.md`](../skills/icml-supplementary/SKILL.md) — supplementary
  manuscript vs. code/data classes and anonymization.

## Suggested workflow

1. Decide fit and route with [`../skills/icml-topic-selection`](../skills/icml-topic-selection/SKILL.md)
   (ICML main vs. position paper vs. NeurIPS/ICLR/UAI/journal).
2. Draft the abstract + intro with
   [`../skills/icml-writing-style`](../skills/icml-writing-style/SKILL.md), modeling on
   [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md).
3. Position against close work with
   [`../skills/icml-related-work`](../skills/icml-related-work/SKILL.md), and benchmark the design
   against verified ICML papers in [`exemplars/library.md`](exemplars/library.md).
4. Stress-test evidence and reproducibility with
   [`../skills/icml-experiments`](../skills/icml-experiments/SKILL.md) and
   [`../skills/icml-reproducibility`](../skills/icml-reproducibility/SKILL.md).
5. Run the final submission audit with
   [`../skills/icml-submission`](../skills/icml-submission/SKILL.md); confirm policy facts in
   [`official-source-map.md`](official-source-map.md) and [`external_tools.md`](external_tools.md).
