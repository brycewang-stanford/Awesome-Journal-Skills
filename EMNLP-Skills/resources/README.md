# EMNLP Resources

Action-oriented resources for the EMNLP skill pack. The `skills/` directory gives advice; this
directory lets an agent model an EMNLP-style paper, benchmark against Anthology-verified
exemplars, and prepare reproducibility artifacts without dragging in the economics code kit.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | Watch a fictional multilingual-summarization first page rebuilt from architecture-first to phenomenon-first. Illustrative only; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against six real EMNLP papers verified on the ACL Anthology, with an anti-misattribution guard for sibling ACL-family venues. |
| [`official-source-map.md`](official-source-map.md) | Confirm the current EMNLP/ARR sources — cycle dates, format, checklist, commitment — before giving submission-ready advice, including the access-method note and the 待核实 list. |
| [`external_tools.md`](external_tools.md) | Open the live conference and ARR surfaces and run the five author-side verification passes. |
| [`code/README.md`](code/README.md) | Use the shared ML conference reproducibility kit plus the NLP-specific checks (prompts, model snapshots, decoding parameters, annotation materials) it cannot automate. |

## Scope Note

This is an empirical-NLP conference pack. Its evidence culture is datasets, baselines,
significance tests, human evaluation, and error analysis — not identification strategies or
regression tables. Do not copy the econometrics kit here; use the shared ML-conference kit and
the NLP adapter checks in `code/README.md`.

## Suggested Workflow

1. Route and frame with
   [`../skills/emnlp-topic-selection`](../skills/emnlp-topic-selection/SKILL.md) and
   [`../skills/emnlp-writing-style`](../skills/emnlp-writing-style/SKILL.md); sanity-check the
   framing against [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md).
2. Stress-test the evidence with
   [`../skills/emnlp-experiments`](../skills/emnlp-experiments/SKILL.md),
   [`../skills/emnlp-reproducibility`](../skills/emnlp-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm the live cycle
   rules in [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) before upload or commitment.
