# The World Bank Economic Review Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="The World Bank Economic Review Skills cover"></p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-wber-102a54)](https://academic.oup.com/wber)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://academic.oup.com/wber)

English | [简体中文](README.zh-CN.md)

Twelve agent skills for manuscripts targeted at **The World Bank Economic Review (WBER)**. The pack is tuned to policy-relevant development economics, impact evaluation, institutions, trade, labor, agriculture, and poverty; it keeps the manuscript distinct from Journal of Development Economics, World Development, Economic Development and Cultural Change, and AEJ Applied and emphasizes development-policy evidence with transparent data construction and actionable interpretation.

**Official basis checked 2026-06** (re-check volatile details before submission): see [`resources/official-source-map.md`](resources/official-source-map.md).

## Why a separate stack?

| WBER constraint | What it forces |
|-------------------------|----------------|
| Scope | The main claim must speak to policy-relevant development economics, impact evaluation, institutions, trade, labor, agriculture, and poverty |
| Sibling boundary | The paper must explain why it belongs here rather than Journal of Development Economics, World Development, Economic Development and Cultural Change, and AEJ Applied |
| Evidence standard | Designs, models, reviews, or qualitative evidence must match development-policy evidence with transparent data construction and actionable interpretation |
| Source discipline | Current process facts are cited or marked 待核实 |

## Quick Start

```text
/plugin marketplace add ./World-Bank-Economic-Review-Skills
/plugin install wber-skills
```

Manual use: start with [`skills/wber-workflow/SKILL.md`](skills/wber-workflow/SKILL.md).

## Default Workflow

```text
wber-workflow → wber-topic-selection → wber-literature-positioning → wber-identification → wber-theory-model → wber-robustness → wber-tables-figures → wber-writing-style → wber-replication-package → wber-referee-strategy → wber-submission → wber-rebuttal
```

## Skills

| # | Skill | What it does |
|---|-------|--------------|
| 1 | [`wber-workflow`](skills/wber-workflow/SKILL.md) | Workflow Router for WBER manuscripts |
| 2 | [`wber-topic-selection`](skills/wber-topic-selection/SKILL.md) | Topic Selection for WBER manuscripts |
| 3 | [`wber-literature-positioning`](skills/wber-literature-positioning/SKILL.md) | Literature Positioning for WBER manuscripts |
| 4 | [`wber-identification`](skills/wber-identification/SKILL.md) | Identification Strategy for WBER manuscripts |
| 5 | [`wber-theory-model`](skills/wber-theory-model/SKILL.md) | Theory and Model Craft for WBER manuscripts |
| 6 | [`wber-robustness`](skills/wber-robustness/SKILL.md) | Robustness Strategy for WBER manuscripts |
| 7 | [`wber-tables-figures`](skills/wber-tables-figures/SKILL.md) | Tables and Figures for WBER manuscripts |
| 8 | [`wber-writing-style`](skills/wber-writing-style/SKILL.md) | Writing Style for WBER manuscripts |
| 9 | [`wber-replication-package`](skills/wber-replication-package/SKILL.md) | Replication Package for WBER manuscripts |
| 10 | [`wber-referee-strategy`](skills/wber-referee-strategy/SKILL.md) | Referee Strategy for WBER manuscripts |
| 11 | [`wber-submission`](skills/wber-submission/SKILL.md) | Submission Preflight for WBER manuscripts |
| 12 | [`wber-rebuttal`](skills/wber-rebuttal/SKILL.md) | Rebuttal Strategy for WBER manuscripts |

## Resources

- [`resources/README.md`](resources/README.md) — resource index
- [`resources/official-source-map.md`](resources/official-source-map.md) — official URLs and volatile checks
- [`resources/external_tools.md`](resources/external_tools.md) — databases, methods, and software aids
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — fictional before/after introduction
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real-paper slots with source discipline
- [`resources/code/`](resources/code/) — empirical code kit where applicable

## Related Links

- https://academic.oup.com/wber
- https://academic.oup.com/wber/pages/General_Instructions

## License

MIT (c) 2026 Bryce Wang. See [LICENSE](LICENSE).
