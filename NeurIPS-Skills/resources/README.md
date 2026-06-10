# NeurIPS Resources

Action-oriented resources for the NeurIPS skill pack. The `skills/` give advice; this directory lets an
agent **benchmark and model** a NeurIPS-style paper against verified facts and exemplars. Pair these with
the relevant `skills/neurips-*/SKILL.md`.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a machine-learning paper **abstract + introduction** in NeurIPS house style (problem → gap → contribution type → previewed evidence → limitation), with claims anchored to baselines/theorems/ablations and reproducibility/checklist norms. Illustrative **fictional** paper — invents no policy. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified NeurIPS / NIPS papers** organized by method × topic, plus a sibling-confusion guard (ICML / ICLR / CVPR / NAACL papers explicitly excluded). Design positioning only — no fabricated numbers. |
| [`official-source-map.md`](official-source-map.md) | **NeurIPS-specific policy & facts:** current-cycle CFP, Main Track Handbook, mandatory Paper Checklist, OpenReview, the MLRC/reproducibility track, and the official source URLs. The authoritative pack source. |
| [`external_tools.md`](external_tools.md) | External tools and services referenced by the pack (proceedings, OpenReview, Software Heritage, code-release guidance). |
| [`code/README.md`](code/README.md) | Use the shared ML conference reproducibility kit: experiment matrix, artifact checklist, and a dependency-free smoke checker for anonymous reproduction packages. This is not the econometrics code kit. |

## Note on scope (ML venue — no econometrics code kit)

NeurIPS is a **machine-learning conference**, not an empirical-economics journal. The Stata/Python
causal-inference code kit vendored into the economics packs (e.g. QJE) is **deliberately not vendored
here** — it is not the right discipline-appropriate resource for a NeurIPS submission. The discipline
fit for this pack is method/theory/empirical-ML rigor, reproducibility, and the NeurIPS checklist, which
the worked example and exemplars target directly. Reproducibility and experiment expectations live in
[`../skills/neurips-reproducibility/SKILL.md`](../skills/neurips-reproducibility/SKILL.md) and
[`../skills/neurips-experiments/SKILL.md`](../skills/neurips-experiments/SKILL.md).

## Suggested workflow

1. Scope and frame with [`../skills/neurips-topic-selection`](../skills/neurips-topic-selection/SKILL.md)
   and [`../skills/neurips-writing-style`](../skills/neurips-writing-style/SKILL.md); model the
   abstract/intro on [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md).
2. Stress-test evidence with
   [`../skills/neurips-experiments`](../skills/neurips-experiments/SKILL.md) and
   [`../skills/neurips-reproducibility`](../skills/neurips-reproducibility/SKILL.md).
3. Benchmark design against verified NeurIPS/NIPS papers in
   [`exemplars/library.md`](exemplars/library.md).
4. Confirm submission, checklist, and track policy in
   [`official-source-map.md`](official-source-map.md), and reach external systems via
   [`external_tools.md`](external_tools.md) — always re-checking the current cycle, since NeurIPS rules
   change every year.
