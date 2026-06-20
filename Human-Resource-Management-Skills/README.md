# Human Resource Management Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Human Resource Management Skills cover"></p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-hrm-102a54)](https://onlinelibrary.wiley.com/journal/1099050x)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://onlinelibrary.wiley.com/journal/1099050x)

English | [简体中文](README.zh-CN.md)

Twelve agent skills for manuscripts targeted at **Human Resource Management (HRM)**. The pack is tuned to human resource management, talent, compensation, employment systems, workforce analytics, and HR strategy; it keeps the manuscript distinct from Personnel Psychology, Journal of Management, Human Relations, and Academy of Management Journal and emphasizes HR scholarship that connects people practices to organizational mechanisms and outcomes.

**Official basis checked 2026-06** (re-check volatile details before submission): see [`resources/official-source-map.md`](resources/official-source-map.md).

## Why a separate stack?

| HRM constraint | What it forces |
|-------------------------|----------------|
| Scope | The main claim must speak to human resource management, talent, compensation, employment systems, workforce analytics, and HR strategy |
| Sibling boundary | The paper must explain why it belongs here rather than Personnel Psychology, Journal of Management, Human Relations, and Academy of Management Journal |
| Evidence standard | Designs, models, reviews, or qualitative evidence must match HR scholarship that connects people practices to organizational mechanisms and outcomes |
| Source discipline | Current process facts are cited or marked 待核实 |

## Quick Start

```text
/plugin marketplace add ./Human-Resource-Management-Skills
/plugin install human-resource-management-skills
```

Manual use: start with [`skills/hrm-workflow/SKILL.md`](skills/hrm-workflow/SKILL.md).

## Default Workflow

```text
hrm-workflow → hrm-topic-selection → hrm-theory-development → hrm-literature-positioning → hrm-methods → hrm-data-analysis → hrm-contribution-framing → hrm-tables-figures → hrm-writing-style → hrm-submission → hrm-review-process → hrm-rebuttal
```

## Skills

| # | Skill | What it does |
|---|-------|--------------|
| 1 | [`hrm-workflow`](skills/hrm-workflow/SKILL.md) | Workflow Router for HRM manuscripts |
| 2 | [`hrm-topic-selection`](skills/hrm-topic-selection/SKILL.md) | Topic Selection for HRM manuscripts |
| 3 | [`hrm-theory-development`](skills/hrm-theory-development/SKILL.md) | Theory Development for HRM manuscripts |
| 4 | [`hrm-literature-positioning`](skills/hrm-literature-positioning/SKILL.md) | Literature Positioning for HRM manuscripts |
| 5 | [`hrm-methods`](skills/hrm-methods/SKILL.md) | Methods for HRM manuscripts |
| 6 | [`hrm-data-analysis`](skills/hrm-data-analysis/SKILL.md) | Data Analysis for HRM manuscripts |
| 7 | [`hrm-contribution-framing`](skills/hrm-contribution-framing/SKILL.md) | Contribution Framing for HRM manuscripts |
| 8 | [`hrm-tables-figures`](skills/hrm-tables-figures/SKILL.md) | Tables and Figures for HRM manuscripts |
| 9 | [`hrm-writing-style`](skills/hrm-writing-style/SKILL.md) | Writing Style for HRM manuscripts |
| 10 | [`hrm-submission`](skills/hrm-submission/SKILL.md) | Submission Preflight for HRM manuscripts |
| 11 | [`hrm-review-process`](skills/hrm-review-process/SKILL.md) | Review Process for HRM manuscripts |
| 12 | [`hrm-rebuttal`](skills/hrm-rebuttal/SKILL.md) | Rebuttal Strategy for HRM manuscripts |

## Resources

- [`resources/README.md`](resources/README.md) — resource index
- [`resources/official-source-map.md`](resources/official-source-map.md) — official URLs and volatile checks
- [`resources/external_tools.md`](resources/external_tools.md) — databases, methods, and software aids
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — fictional before/after introduction
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real-paper slots with source discipline
- [`resources/code/`](resources/code/) — empirical code kit where applicable

## Related Links

- https://onlinelibrary.wiley.com/journal/1099050x
- https://onlinelibrary.wiley.com/page/journal/1099050x/homepage/forauthors.html

## License

MIT (c) 2026 Bryce Wang. See [LICENSE](LICENSE).
