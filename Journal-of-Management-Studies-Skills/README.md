# Journal of Management Studies Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Journal of Management Studies Skills cover"></p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-jms-102a54)](https://onlinelibrary.wiley.com/journal/14676486)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://onlinelibrary.wiley.com/journal/14676486)

English | [简体中文](README.zh-CN.md)

Twelve agent skills for manuscripts targeted at **Journal of Management Studies (JMS)**. The pack is tuned to management and organization studies, strategy, entrepreneurship, innovation, OB, and critical perspectives; it keeps the manuscript distinct from Journal of Management, Organization Studies, AMJ, AMR, and Strategic Management Journal and emphasizes conceptually rich management scholarship that makes theory travel beyond one setting.

**Official basis checked 2026-06** (re-check volatile details before submission): see [`resources/official-source-map.md`](resources/official-source-map.md).

## Why a separate stack?

| JMS constraint | What it forces |
|-------------------------|----------------|
| Scope | The main claim must speak to management and organization studies, strategy, entrepreneurship, innovation, OB, and critical perspectives |
| Sibling boundary | The paper must explain why it belongs here rather than Journal of Management, Organization Studies, AMJ, AMR, and Strategic Management Journal |
| Evidence standard | Designs, models, reviews, or qualitative evidence must match conceptually rich management scholarship that makes theory travel beyond one setting |
| Source discipline | Current process facts are cited or marked 待核实 |

## Quick Start

```text
/plugin marketplace add ./Journal-of-Management-Studies-Skills
/plugin install jms-skills
```

Manual use: start with [`skills/jms-workflow/SKILL.md`](skills/jms-workflow/SKILL.md).

## Default Workflow

```text
jms-workflow → jms-topic-selection → jms-theory-development → jms-literature-positioning → jms-methods → jms-data-analysis → jms-contribution-framing → jms-tables-figures → jms-writing-style → jms-submission → jms-review-process → jms-rebuttal
```

## Skills

| # | Skill | What it does |
|---|-------|--------------|
| 1 | [`jms-workflow`](skills/jms-workflow/SKILL.md) | Workflow Router for JMS manuscripts |
| 2 | [`jms-topic-selection`](skills/jms-topic-selection/SKILL.md) | Topic Selection for JMS manuscripts |
| 3 | [`jms-theory-development`](skills/jms-theory-development/SKILL.md) | Theory Development for JMS manuscripts |
| 4 | [`jms-literature-positioning`](skills/jms-literature-positioning/SKILL.md) | Literature Positioning for JMS manuscripts |
| 5 | [`jms-methods`](skills/jms-methods/SKILL.md) | Methods for JMS manuscripts |
| 6 | [`jms-data-analysis`](skills/jms-data-analysis/SKILL.md) | Data Analysis for JMS manuscripts |
| 7 | [`jms-contribution-framing`](skills/jms-contribution-framing/SKILL.md) | Contribution Framing for JMS manuscripts |
| 8 | [`jms-tables-figures`](skills/jms-tables-figures/SKILL.md) | Tables and Figures for JMS manuscripts |
| 9 | [`jms-writing-style`](skills/jms-writing-style/SKILL.md) | Writing Style for JMS manuscripts |
| 10 | [`jms-submission`](skills/jms-submission/SKILL.md) | Submission Preflight for JMS manuscripts |
| 11 | [`jms-review-process`](skills/jms-review-process/SKILL.md) | Review Process for JMS manuscripts |
| 12 | [`jms-rebuttal`](skills/jms-rebuttal/SKILL.md) | Rebuttal Strategy for JMS manuscripts |

## Resources

- [`resources/README.md`](resources/README.md) — resource index
- [`resources/official-source-map.md`](resources/official-source-map.md) — official URLs and volatile checks
- [`resources/external_tools.md`](resources/external_tools.md) — databases, methods, and software aids
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — fictional before/after introduction
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real-paper slots with source discipline
- [`resources/code/`](resources/code/) — empirical code kit where applicable

## Related Links

- https://onlinelibrary.wiley.com/journal/14676486
- https://onlinelibrary.wiley.com/page/journal/14676486/homepage/forauthors.html

## License

MIT (c) 2026 Bryce Wang. See [LICENSE](LICENSE).
