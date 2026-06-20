# Journal of Law, Economics, and Organization Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Journal of Law, Economics, and Organization Skills cover"></p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-jleo-102a54)](https://academic.oup.com/jleo)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://academic.oup.com/jleo)

English | [简体中文](README.zh-CN.md)

Twelve agent skills for manuscripts targeted at **Journal of Law, Economics, and Organization (JLEO)**. The pack is tuned to law, economics, and organization with emphasis on contracts, institutions, governance, and organizational design; it keeps the manuscript distinct from Journal of Law and Economics, Journal of Legal Studies, Organization Science, and American Law and Economics Review and emphasizes institutional-economics argument that integrates legal rules, governance, and organizational mechanisms.

**Official basis checked 2026-06** (re-check volatile details before submission): see [`resources/official-source-map.md`](resources/official-source-map.md).

## Why a separate stack?

| JLEO constraint | What it forces |
|-------------------------|----------------|
| Scope | The main claim must speak to law, economics, and organization with emphasis on contracts, institutions, governance, and organizational design |
| Sibling boundary | The paper must explain why it belongs here rather than Journal of Law and Economics, Journal of Legal Studies, Organization Science, and American Law and Economics Review |
| Evidence standard | Designs, models, reviews, or qualitative evidence must match institutional-economics argument that integrates legal rules, governance, and organizational mechanisms |
| Source discipline | Current process facts are cited or marked 待核实 |

## Quick Start

```text
/plugin marketplace add ./Journal-of-Law-Economics-and-Organization-Skills
/plugin install jleo-skills
```

Manual use: start with [`skills/jleo-workflow/SKILL.md`](skills/jleo-workflow/SKILL.md).

## Default Workflow

```text
jleo-workflow → jleo-topic-selection → jleo-literature-positioning → jleo-identification → jleo-theory-model → jleo-robustness → jleo-tables-figures → jleo-writing-style → jleo-replication-package → jleo-referee-strategy → jleo-submission → jleo-rebuttal
```

## Skills

| # | Skill | What it does |
|---|-------|--------------|
| 1 | [`jleo-workflow`](skills/jleo-workflow/SKILL.md) | Workflow Router for JLEO manuscripts |
| 2 | [`jleo-topic-selection`](skills/jleo-topic-selection/SKILL.md) | Topic Selection for JLEO manuscripts |
| 3 | [`jleo-literature-positioning`](skills/jleo-literature-positioning/SKILL.md) | Literature Positioning for JLEO manuscripts |
| 4 | [`jleo-identification`](skills/jleo-identification/SKILL.md) | Identification Strategy for JLEO manuscripts |
| 5 | [`jleo-theory-model`](skills/jleo-theory-model/SKILL.md) | Theory and Model Craft for JLEO manuscripts |
| 6 | [`jleo-robustness`](skills/jleo-robustness/SKILL.md) | Robustness Strategy for JLEO manuscripts |
| 7 | [`jleo-tables-figures`](skills/jleo-tables-figures/SKILL.md) | Tables and Figures for JLEO manuscripts |
| 8 | [`jleo-writing-style`](skills/jleo-writing-style/SKILL.md) | Writing Style for JLEO manuscripts |
| 9 | [`jleo-replication-package`](skills/jleo-replication-package/SKILL.md) | Replication Package for JLEO manuscripts |
| 10 | [`jleo-referee-strategy`](skills/jleo-referee-strategy/SKILL.md) | Referee Strategy for JLEO manuscripts |
| 11 | [`jleo-submission`](skills/jleo-submission/SKILL.md) | Submission Preflight for JLEO manuscripts |
| 12 | [`jleo-rebuttal`](skills/jleo-rebuttal/SKILL.md) | Rebuttal Strategy for JLEO manuscripts |

## Resources

- [`resources/README.md`](resources/README.md) — resource index
- [`resources/official-source-map.md`](resources/official-source-map.md) — official URLs and volatile checks
- [`resources/external_tools.md`](resources/external_tools.md) — databases, methods, and software aids
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — fictional before/after introduction
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real-paper slots with source discipline
- [`resources/code/`](resources/code/) — empirical code kit where applicable

## Related Links

- https://academic.oup.com/jleo
- https://academic.oup.com/jleo/pages/General_Instructions

## License

MIT (c) 2026 Bryce Wang. See [LICENSE](LICENSE).
