# SIGIR Resources

Action-oriented companions to the `skills/` directory: where the skills advise, these
files let an agent model a SIGIR-style paper against verified exemplars, check current
official sources, and package IR artifacts (run files, qrels, index recipes) to the
community's standard.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`official-source-map.md`](official-source-map.md) | Confirm every SIGIR 2026 fact used in this pack — URL, access date, what was verified, what stayed 待核实 — before giving deadline- or policy-sensitive advice. |
| [`external_tools.md`](external_tools.md) | Open the per-track pages, OpenReview groups, ACM authoring pipeline, and the IR tooling stack (trec_eval, ir_measures, ir_datasets, Anserini/PyTerrier). |
| [`exemplars/library.md`](exemplars/library.md) | Position against DOI-verified SIGIR papers (Ponte & Croft → ColBERT → LightGCN) and dodge the venue-misattribution traps (DPR=EMNLP, ANCE=ICLR, NCF=WWW). |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a fictional before/after rewrite into the SIGIR first-page arc: task + regime → mechanism failure → move → calibrated evidence. |
| [`code/README.md`](code/README.md) | Adapt the shared ML-conference reproducibility kit to IR: run-file coverage, one-command scoring, significance scripts, index-recipe pinning. |

## Scope note

This is an information-retrieval conference pack. The evidence unit is the run file
scored against qrels on a named collection — not the regression table (economics kits)
and not the leaderboard screenshot (generic ML). When another pack's resource conflicts
with the IR conventions here, the current SIGIR track pages win over both.

## Suggested workflow

1. Route with [`../skills/sigir-topic-selection`](../skills/sigir-topic-selection/SKILL.md)
   (the track fork matters more at SIGIR than at single-track venues), then calendar
   with [`../skills/sigir-workflow`](../skills/sigir-workflow/SKILL.md).
2. Build evidence under [`../skills/sigir-experiments`](../skills/sigir-experiments/SKILL.md)
   and [`../skills/sigir-reproducibility`](../skills/sigir-reproducibility/SKILL.md),
   packaging artifacts per [`code/README.md`](code/README.md).
3. Write with [`../skills/sigir-writing-style`](../skills/sigir-writing-style/SKILL.md)
   against [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) and
   [`exemplars/library.md`](exemplars/library.md).
4. Before upload, re-verify the live rules via [`official-source-map.md`](official-source-map.md)
   and run the [`../skills/sigir-submission`](../skills/sigir-submission/SKILL.md) audit.
