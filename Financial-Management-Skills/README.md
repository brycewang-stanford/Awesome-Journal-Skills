# Financial Management Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Financial Management Skills cover"></p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-fm-102a54)](https://onlinelibrary.wiley.com/journal/1755053x)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://onlinelibrary.wiley.com/journal/1755053x)

English | [简体中文](README.zh-CN.md)

Twelve agent skills for manuscripts targeted at **Financial Management (FM)**. The pack is tuned to corporate finance, investments, market institutions, and applied financial decision-making; it keeps the manuscript distinct from Journal of Corporate Finance, Journal of Banking and Finance, JFQA, and Review of Financial Studies and emphasizes applied finance evidence that ties estimates to managerial or market decisions.

**Official basis checked 2026-06** (re-check volatile details before submission): see [`resources/official-source-map.md`](resources/official-source-map.md).

## Why a separate stack?

| FM constraint | What it forces |
|-------------------------|----------------|
| Scope | The main claim must speak to corporate finance, investments, market institutions, and applied financial decision-making |
| Sibling boundary | The paper must explain why it belongs here rather than Journal of Corporate Finance, Journal of Banking and Finance, JFQA, and Review of Financial Studies |
| Evidence standard | Designs, models, reviews, or qualitative evidence must match applied finance evidence that ties estimates to managerial or market decisions |
| Source discipline | Current process facts are cited or marked 待核实 |

## Quick Start

```text
/plugin marketplace add ./Financial-Management-Skills
/plugin install financial-management-skills
```

Manual use: start with [`skills/finman-workflow/SKILL.md`](skills/finman-workflow/SKILL.md).

## Default Workflow

```text
finman-workflow → finman-topic-selection → finman-literature-positioning → finman-identification → finman-empirical-design → finman-robustness → finman-tables-figures → finman-internet-appendix → finman-writing-style → finman-submission → finman-referee-strategy → finman-rebuttal
```

## Skills

| # | Skill | What it does |
|---|-------|--------------|
| 1 | [`finman-workflow`](skills/finman-workflow/SKILL.md) | Workflow Router for FM manuscripts |
| 2 | [`finman-topic-selection`](skills/finman-topic-selection/SKILL.md) | Topic Selection for FM manuscripts |
| 3 | [`finman-literature-positioning`](skills/finman-literature-positioning/SKILL.md) | Literature Positioning for FM manuscripts |
| 4 | [`finman-identification`](skills/finman-identification/SKILL.md) | Identification Strategy for FM manuscripts |
| 5 | [`finman-empirical-design`](skills/finman-empirical-design/SKILL.md) | Empirical Design for FM manuscripts |
| 6 | [`finman-robustness`](skills/finman-robustness/SKILL.md) | Robustness Strategy for FM manuscripts |
| 7 | [`finman-tables-figures`](skills/finman-tables-figures/SKILL.md) | Tables and Figures for FM manuscripts |
| 8 | [`finman-internet-appendix`](skills/finman-internet-appendix/SKILL.md) | Internet Appendix for FM manuscripts |
| 9 | [`finman-writing-style`](skills/finman-writing-style/SKILL.md) | Writing Style for FM manuscripts |
| 10 | [`finman-submission`](skills/finman-submission/SKILL.md) | Submission Preflight for FM manuscripts |
| 11 | [`finman-referee-strategy`](skills/finman-referee-strategy/SKILL.md) | Referee Strategy for FM manuscripts |
| 12 | [`finman-rebuttal`](skills/finman-rebuttal/SKILL.md) | Rebuttal Strategy for FM manuscripts |

## Resources

- [`resources/README.md`](resources/README.md) — resource index
- [`resources/official-source-map.md`](resources/official-source-map.md) — official URLs and volatile checks
- [`resources/external_tools.md`](resources/external_tools.md) — databases, methods, and software aids
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — fictional before/after introduction
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real-paper slots with source discipline
- [`resources/code/`](resources/code/) — empirical code kit where applicable

## Related Links

- https://onlinelibrary.wiley.com/journal/1755053x
- https://www.fma.org/financial-management

## License

MIT (c) 2026 Bryce Wang. See [LICENSE](LICENSE).
