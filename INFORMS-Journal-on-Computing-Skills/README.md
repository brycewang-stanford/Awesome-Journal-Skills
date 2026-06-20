# INFORMS Journal on Computing Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="INFORMS Journal on Computing Skills cover"></p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-ijoc-102a54)](https://pubsonline.informs.org/journal/ijoc)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://pubsonline.informs.org/journal/ijoc)

English | [简体中文](README.zh-CN.md)

Twelve agent skills for manuscripts targeted at **INFORMS Journal on Computing (IJOC)**. The pack is tuned to operations research and computing, algorithms, optimization, machine learning, simulation, and computational decision systems; it keeps the manuscript distinct from Operations Research, Management Science, Manufacturing & Service Operations Management, and ACM/IEEE computing venues and emphasizes computational OR contribution with transparent algorithms, benchmarks, and reproducibility.

**Official basis checked 2026-06** (re-check volatile details before submission): see [`resources/official-source-map.md`](resources/official-source-map.md).

## Why a separate stack?

| IJOC constraint | What it forces |
|-------------------------|----------------|
| Scope | The main claim must speak to operations research and computing, algorithms, optimization, machine learning, simulation, and computational decision systems |
| Sibling boundary | The paper must explain why it belongs here rather than Operations Research, Management Science, Manufacturing & Service Operations Management, and ACM/IEEE computing venues |
| Evidence standard | Designs, models, reviews, or qualitative evidence must match computational OR contribution with transparent algorithms, benchmarks, and reproducibility |
| Source discipline | Current process facts are cited or marked 待核实 |

## Quick Start

```text
/plugin marketplace add ./INFORMS-Journal-on-Computing-Skills
/plugin install informs-journal-on-computing-skills
```

Manual use: start with [`skills/ijoc-workflow/SKILL.md`](skills/ijoc-workflow/SKILL.md).

## Default Workflow

```text
ijoc-workflow → ijoc-topic-selection → ijoc-theory-development → ijoc-literature-positioning → ijoc-methods → ijoc-data-analysis → ijoc-contribution-framing → ijoc-tables-figures → ijoc-writing-style → ijoc-submission → ijoc-review-process → ijoc-rebuttal
```

## Skills

| # | Skill | What it does |
|---|-------|--------------|
| 1 | [`ijoc-workflow`](skills/ijoc-workflow/SKILL.md) | Workflow Router for IJOC manuscripts |
| 2 | [`ijoc-topic-selection`](skills/ijoc-topic-selection/SKILL.md) | Topic Selection for IJOC manuscripts |
| 3 | [`ijoc-theory-development`](skills/ijoc-theory-development/SKILL.md) | Theory Development for IJOC manuscripts |
| 4 | [`ijoc-literature-positioning`](skills/ijoc-literature-positioning/SKILL.md) | Literature Positioning for IJOC manuscripts |
| 5 | [`ijoc-methods`](skills/ijoc-methods/SKILL.md) | Methods for IJOC manuscripts |
| 6 | [`ijoc-data-analysis`](skills/ijoc-data-analysis/SKILL.md) | Data Analysis for IJOC manuscripts |
| 7 | [`ijoc-contribution-framing`](skills/ijoc-contribution-framing/SKILL.md) | Contribution Framing for IJOC manuscripts |
| 8 | [`ijoc-tables-figures`](skills/ijoc-tables-figures/SKILL.md) | Tables and Figures for IJOC manuscripts |
| 9 | [`ijoc-writing-style`](skills/ijoc-writing-style/SKILL.md) | Writing Style for IJOC manuscripts |
| 10 | [`ijoc-submission`](skills/ijoc-submission/SKILL.md) | Submission Preflight for IJOC manuscripts |
| 11 | [`ijoc-review-process`](skills/ijoc-review-process/SKILL.md) | Review Process for IJOC manuscripts |
| 12 | [`ijoc-rebuttal`](skills/ijoc-rebuttal/SKILL.md) | Rebuttal Strategy for IJOC manuscripts |

## Resources

- [`resources/README.md`](resources/README.md) — resource index
- [`resources/official-source-map.md`](resources/official-source-map.md) — official URLs and volatile checks
- [`resources/external_tools.md`](resources/external_tools.md) — databases, methods, and software aids
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — fictional before/after introduction
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real-paper slots with source discipline
- [`resources/code/`](resources/code/) — empirical code kit where applicable

## Related Links

- https://pubsonline.informs.org/journal/ijoc
- https://pubsonline.informs.org/page/ijoc/submission-guidelines

## License

MIT (c) 2026 Bryce Wang. See [LICENSE](LICENSE).
