# World Development Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="World Development Skills cover"></p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-world%20development-102a54)](https://www.sciencedirect.com/journal/world-development)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://www.sciencedirect.com/journal/world-development)

English | [简体中文](README.zh-CN.md)

Twelve agent skills for manuscripts targeted at **World Development (World Development)**. The pack is tuned to development studies and development economics across poverty, institutions, sustainability, and policy implementation; it keeps the manuscript distinct from Journal of Development Economics, World Bank Economic Review, Economic Development and Cultural Change, and World Development Perspectives and emphasizes development evidence that connects identification to implementation, equity, and institutions.

**Official basis checked 2026-06** (re-check volatile details before submission): see [`resources/official-source-map.md`](resources/official-source-map.md).

## Why a separate stack?

| World Development constraint | What it forces |
|-------------------------|----------------|
| Scope | The main claim must speak to development studies and development economics across poverty, institutions, sustainability, and policy implementation |
| Sibling boundary | The paper must explain why it belongs here rather than Journal of Development Economics, World Bank Economic Review, Economic Development and Cultural Change, and World Development Perspectives |
| Evidence standard | Designs, models, reviews, or qualitative evidence must match development evidence that connects identification to implementation, equity, and institutions |
| Source discipline | Current process facts are cited or marked 待核实 |

## Quick Start

```text
/plugin marketplace add ./World-Development-Skills
/plugin install world-development-skills
```

Manual use: start with [`skills/worlddev-workflow/SKILL.md`](skills/worlddev-workflow/SKILL.md).

## Default Workflow

```text
worlddev-workflow → worlddev-topic-selection → worlddev-literature-positioning → worlddev-identification → worlddev-theory-model → worlddev-robustness → worlddev-tables-figures → worlddev-writing-style → worlddev-replication-package → worlddev-referee-strategy → worlddev-submission → worlddev-rebuttal
```

## Skills

| # | Skill | What it does |
|---|-------|--------------|
| 1 | [`worlddev-workflow`](skills/worlddev-workflow/SKILL.md) | Workflow Router for World Development manuscripts |
| 2 | [`worlddev-topic-selection`](skills/worlddev-topic-selection/SKILL.md) | Topic Selection for World Development manuscripts |
| 3 | [`worlddev-literature-positioning`](skills/worlddev-literature-positioning/SKILL.md) | Literature Positioning for World Development manuscripts |
| 4 | [`worlddev-identification`](skills/worlddev-identification/SKILL.md) | Identification Strategy for World Development manuscripts |
| 5 | [`worlddev-theory-model`](skills/worlddev-theory-model/SKILL.md) | Theory and Model Craft for World Development manuscripts |
| 6 | [`worlddev-robustness`](skills/worlddev-robustness/SKILL.md) | Robustness Strategy for World Development manuscripts |
| 7 | [`worlddev-tables-figures`](skills/worlddev-tables-figures/SKILL.md) | Tables and Figures for World Development manuscripts |
| 8 | [`worlddev-writing-style`](skills/worlddev-writing-style/SKILL.md) | Writing Style for World Development manuscripts |
| 9 | [`worlddev-replication-package`](skills/worlddev-replication-package/SKILL.md) | Replication Package for World Development manuscripts |
| 10 | [`worlddev-referee-strategy`](skills/worlddev-referee-strategy/SKILL.md) | Referee Strategy for World Development manuscripts |
| 11 | [`worlddev-submission`](skills/worlddev-submission/SKILL.md) | Submission Preflight for World Development manuscripts |
| 12 | [`worlddev-rebuttal`](skills/worlddev-rebuttal/SKILL.md) | Rebuttal Strategy for World Development manuscripts |

## Resources

- [`resources/README.md`](resources/README.md) — resource index
- [`resources/official-source-map.md`](resources/official-source-map.md) — official URLs and volatile checks
- [`resources/external_tools.md`](resources/external_tools.md) — databases, methods, and software aids
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — fictional before/after introduction
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real-paper slots with source discipline
- [`resources/code/`](resources/code/) — empirical code kit where applicable

## Related Links

- https://www.sciencedirect.com/journal/world-development
- https://www.elsevier.com/journals/world-development/0305-750X/guide-for-authors

## License

MIT (c) 2026 Bryce Wang. See [LICENSE](LICENSE).
