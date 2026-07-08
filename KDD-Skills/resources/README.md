# KDD Resources

Working materials for the KDD skill pack. The `skills/` directory holds the advice; this
directory is where an agent can model a KDD-register first page, benchmark against
DOI-verified KDD papers, and assemble the code/deployment evidence the venue's
no-links-in-rebuttal rule makes so consequential.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | Rewrite a generic-ML abstract/introduction into the KDD register: data regime, mechanism, scale evidence, availability. Fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Position against real, DOI-verified KDD papers (XGBoost, node2vec, DeepWalk, metapath2vec, Ad Click Prediction) and dodge ICDM/NeurIPS/RecSys misattribution traps. |
| [`official-source-map.md`](official-source-map.md) | Check which 2026-cycle facts are verified (dual cycles, page budgets, ADS deployment rule, no-links rebuttal) and which remain 待核实. |
| [`external_tools.md`](external_tools.md) | Jump to the track CFPs, OpenReview groups, ACM DL proceedings, and the per-cycle author checks. |
| [`code/README.md`](code/README.md) | Adapt the shared ML-conference reproducibility kit for mining experiments and ADS deployment packages. |

## Scope Note

This pack serves a two-track ACM conference, not a journal: there is no standing editor,
no revise-and-resubmit letter (the closest analogue is the cross-cycle Resubmit
decision), and formatting authority belongs to the ACM template plus the current track
CFP. Keep the econometrics tooling out; the shared ML-conference kit covers what KDD
artifacts need.

## Suggested Workflow

1. Route first: [`../skills/kdd-topic-selection`](../skills/kdd-topic-selection/SKILL.md)
   decides Research vs ADS (vs the Datasets/Benchmarks or AI-for-Sciences tracks) before
   a word is written, then [`../skills/kdd-workflow`](../skills/kdd-workflow/SKILL.md)
   picks the cycle.
2. Build evidence: [`../skills/kdd-experiments`](../skills/kdd-experiments/SKILL.md) and
   [`../skills/kdd-reproducibility`](../skills/kdd-reproducibility/SKILL.md) with
   [`code/README.md`](code/README.md); ADS papers gather post-launch metrics early.
3. Write and check: [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md)
   for the register, [`exemplars/library.md`](exemplars/library.md) for positioning, then
   [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) before anything deadline-sensitive ships.
