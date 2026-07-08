# COLT Resources

Action-oriented companions to the COLT skill pack. The `skills/` directory advises;
this directory lets an agent model a theorem-first COLT paper, benchmark against
verified proceedings exemplars, and handle the (rare) numerical-illustration case
without importing empirical-venue machinery.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | Study a before-to-after rewrite of a learning-theory abstract/introduction into the COLT first-pages arc. Fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Position against real COLT papers verified on PMLR, organized by result type and technique, with volume-trap guardrails. |
| [`official-source-map.md`](official-source-map.md) | Check which COLT facts in this pack are verified (with sources and the 2026-07-08 access date) and which remain 待核实. |
| [`external_tools.md`](external_tools.md) | Jump to the live CFP, CMT portal, PMLR volumes, and the do-not-infer list. |
| [`code/README.md`](code/README.md) | Adapt the shared ML-conference kit to COLT's illustration-only code norms. |

## Scope Note

This is a pure learning-theory conference pack. There is no reproducibility-checklist
form, artifact badge, or experiments requirement to satisfy at COLT — do not import
those workflows from NeurIPS/ICML-style packs. The binding constraints are the ones in
`official-source-map.md`: the 12-page PMLR-format body, the single PDF with unlimited
appendix, double-anonymous review with an informed area chair, the parallel-submission
ban, and the CMT deadline.

## Suggested Workflow

1. Route the project with [`../skills/colt-topic-selection`](../skills/colt-topic-selection/SKILL.md)
   — full paper, open-problem piece, or a different venue entirely.
2. Lock the mathematics: [`../skills/colt-reproducibility`](../skills/colt-reproducibility/SKILL.md)
   for re-derivability and [`../skills/colt-artifact-evaluation`](../skills/colt-artifact-evaluation/SKILL.md)
   for the verification ledger.
3. Shape the document with [`../skills/colt-writing-style`](../skills/colt-writing-style/SKILL.md)
   and [`../skills/colt-supplementary`](../skills/colt-supplementary/SKILL.md), using
   [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) as the
   first-pages model and [`exemplars/library.md`](exemplars/library.md) as the
   positioning benchmark.
4. Before upload, run [`../skills/colt-submission`](../skills/colt-submission/SKILL.md)
   against the live CFP via [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md).
