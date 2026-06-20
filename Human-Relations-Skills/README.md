# Human Relations Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Human Relations Skills cover"></p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-human%20relations-102a54)](https://journals.sagepub.com/home/hum)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://journals.sagepub.com/home/hum)

English | [简体中文](README.zh-CN.md)

Twelve agent skills for manuscripts targeted at **Human Relations (Human Relations)**. The pack is tuned to work, employment, organizations, social relations, power, identity, and critical management; it keeps the manuscript distinct from Organization Studies, Journal of Management Studies, Administrative Science Quarterly, and Work Employment and Society and emphasizes socially grounded organization research that links theory, context, and lived work.

**Official basis checked 2026-06** (re-check volatile details before submission): see [`resources/official-source-map.md`](resources/official-source-map.md).

## Why a separate stack?

| Human Relations constraint | What it forces |
|-------------------------|----------------|
| Scope | The main claim must speak to work, employment, organizations, social relations, power, identity, and critical management |
| Sibling boundary | The paper must explain why it belongs here rather than Organization Studies, Journal of Management Studies, Administrative Science Quarterly, and Work Employment and Society |
| Evidence standard | Designs, models, reviews, or qualitative evidence must match socially grounded organization research that links theory, context, and lived work |
| Source discipline | Current process facts are cited or marked 待核实 |

## Quick Start

```text
/plugin marketplace add ./Human-Relations-Skills
/plugin install human-relations-skills
```

Manual use: start with [`skills/humrel-workflow/SKILL.md`](skills/humrel-workflow/SKILL.md).

## Default Workflow

```text
humrel-workflow → humrel-topic-selection → humrel-theory-development → humrel-literature-positioning → humrel-methods → humrel-data-analysis → humrel-contribution-framing → humrel-tables-figures → humrel-writing-style → humrel-submission → humrel-review-process → humrel-rebuttal
```

## Skills

| # | Skill | What it does |
|---|-------|--------------|
| 1 | [`humrel-workflow`](skills/humrel-workflow/SKILL.md) | Workflow Router for Human Relations manuscripts |
| 2 | [`humrel-topic-selection`](skills/humrel-topic-selection/SKILL.md) | Topic Selection for Human Relations manuscripts |
| 3 | [`humrel-theory-development`](skills/humrel-theory-development/SKILL.md) | Theory Development for Human Relations manuscripts |
| 4 | [`humrel-literature-positioning`](skills/humrel-literature-positioning/SKILL.md) | Literature Positioning for Human Relations manuscripts |
| 5 | [`humrel-methods`](skills/humrel-methods/SKILL.md) | Methods for Human Relations manuscripts |
| 6 | [`humrel-data-analysis`](skills/humrel-data-analysis/SKILL.md) | Data Analysis for Human Relations manuscripts |
| 7 | [`humrel-contribution-framing`](skills/humrel-contribution-framing/SKILL.md) | Contribution Framing for Human Relations manuscripts |
| 8 | [`humrel-tables-figures`](skills/humrel-tables-figures/SKILL.md) | Tables and Figures for Human Relations manuscripts |
| 9 | [`humrel-writing-style`](skills/humrel-writing-style/SKILL.md) | Writing Style for Human Relations manuscripts |
| 10 | [`humrel-submission`](skills/humrel-submission/SKILL.md) | Submission Preflight for Human Relations manuscripts |
| 11 | [`humrel-review-process`](skills/humrel-review-process/SKILL.md) | Review Process for Human Relations manuscripts |
| 12 | [`humrel-rebuttal`](skills/humrel-rebuttal/SKILL.md) | Rebuttal Strategy for Human Relations manuscripts |

## Resources

- [`resources/README.md`](resources/README.md) — resource index
- [`resources/official-source-map.md`](resources/official-source-map.md) — official URLs and volatile checks
- [`resources/external_tools.md`](resources/external_tools.md) — databases, methods, and software aids
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — fictional before/after introduction
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real-paper slots with source discipline
- [`resources/code/`](resources/code/) — empirical code kit where applicable

## Related Links

- https://journals.sagepub.com/home/hum
- https://journals.sagepub.com/author-instructions/HUM

## License

MIT (c) 2026 Bryce Wang. See [LICENSE](LICENSE).
