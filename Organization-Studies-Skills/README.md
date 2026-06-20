# Organization Studies Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Organization Studies Skills cover"></p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-os-102a54)](https://journals.sagepub.com/home/oss)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://journals.sagepub.com/home/oss)

English | [简体中文](README.zh-CN.md)

Twelve agent skills for manuscripts targeted at **Organization Studies (OS)**. The pack is tuned to organization theory, institutional theory, critical management, qualitative research, and process studies; it keeps the manuscript distinct from Administrative Science Quarterly, Organization Science, Journal of Management Studies, and Academy of Management Review and emphasizes organization-theory argument with careful positioning, reflexivity, and evidence-theory fit.

**Official basis checked 2026-06** (re-check volatile details before submission): see [`resources/official-source-map.md`](resources/official-source-map.md).

## Why a separate stack?

| OS constraint | What it forces |
|-------------------------|----------------|
| Scope | The main claim must speak to organization theory, institutional theory, critical management, qualitative research, and process studies |
| Sibling boundary | The paper must explain why it belongs here rather than Administrative Science Quarterly, Organization Science, Journal of Management Studies, and Academy of Management Review |
| Evidence standard | Designs, models, reviews, or qualitative evidence must match organization-theory argument with careful positioning, reflexivity, and evidence-theory fit |
| Source discipline | Current process facts are cited or marked 待核实 |

## Quick Start

```text
/plugin marketplace add ./Organization-Studies-Skills
/plugin install organization-studies-skills
```

Manual use: start with [`skills/orgstud-workflow/SKILL.md`](skills/orgstud-workflow/SKILL.md).

## Default Workflow

```text
orgstud-workflow → orgstud-topic-selection → orgstud-theory-development → orgstud-literature-positioning → orgstud-methods → orgstud-data-analysis → orgstud-contribution-framing → orgstud-tables-figures → orgstud-writing-style → orgstud-submission → orgstud-review-process → orgstud-rebuttal
```

## Skills

| # | Skill | What it does |
|---|-------|--------------|
| 1 | [`orgstud-workflow`](skills/orgstud-workflow/SKILL.md) | Workflow Router for OS manuscripts |
| 2 | [`orgstud-topic-selection`](skills/orgstud-topic-selection/SKILL.md) | Topic Selection for OS manuscripts |
| 3 | [`orgstud-theory-development`](skills/orgstud-theory-development/SKILL.md) | Theory Development for OS manuscripts |
| 4 | [`orgstud-literature-positioning`](skills/orgstud-literature-positioning/SKILL.md) | Literature Positioning for OS manuscripts |
| 5 | [`orgstud-methods`](skills/orgstud-methods/SKILL.md) | Methods for OS manuscripts |
| 6 | [`orgstud-data-analysis`](skills/orgstud-data-analysis/SKILL.md) | Data Analysis for OS manuscripts |
| 7 | [`orgstud-contribution-framing`](skills/orgstud-contribution-framing/SKILL.md) | Contribution Framing for OS manuscripts |
| 8 | [`orgstud-tables-figures`](skills/orgstud-tables-figures/SKILL.md) | Tables and Figures for OS manuscripts |
| 9 | [`orgstud-writing-style`](skills/orgstud-writing-style/SKILL.md) | Writing Style for OS manuscripts |
| 10 | [`orgstud-submission`](skills/orgstud-submission/SKILL.md) | Submission Preflight for OS manuscripts |
| 11 | [`orgstud-review-process`](skills/orgstud-review-process/SKILL.md) | Review Process for OS manuscripts |
| 12 | [`orgstud-rebuttal`](skills/orgstud-rebuttal/SKILL.md) | Rebuttal Strategy for OS manuscripts |

## Resources

- [`resources/README.md`](resources/README.md) — resource index
- [`resources/official-source-map.md`](resources/official-source-map.md) — official URLs and volatile checks
- [`resources/external_tools.md`](resources/external_tools.md) — databases, methods, and software aids
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — fictional before/after introduction
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real-paper slots with source discipline
- [`resources/code/`](resources/code/) — empirical code kit where applicable

## Related Links

- https://journals.sagepub.com/home/oss
- https://journals.sagepub.com/author-instructions/OSS

## License

MIT (c) 2026 Bryce Wang. See [LICENSE](LICENSE).
