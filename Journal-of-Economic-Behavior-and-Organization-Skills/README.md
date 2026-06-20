# Journal of Economic Behavior and Organization Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Journal of Economic Behavior and Organization Skills cover"></p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-jebo-102a54)](https://www.sciencedirect.com/journal/journal-of-economic-behavior-and-organization)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://www.sciencedirect.com/journal/journal-of-economic-behavior-and-organization)

English | [简体中文](README.zh-CN.md)

Twelve agent skills for manuscripts targeted at **Journal of Economic Behavior and Organization (JEBO)**. The pack is tuned to behavioral economics, organization, institutions, experiments, and decision-making outside frictionless textbook settings; it keeps the manuscript distinct from Experimental Economics, Games and Economic Behavior, Management Science, and Journal of Public Economics and emphasizes mechanism-forward behavioral evidence with transparent experimental or institutional design.

**Official basis checked 2026-06** (re-check volatile details before submission): see [`resources/official-source-map.md`](resources/official-source-map.md).

## Why a separate stack?

| JEBO constraint | What it forces |
|-------------------------|----------------|
| Scope | The main claim must speak to behavioral economics, organization, institutions, experiments, and decision-making outside frictionless textbook settings |
| Sibling boundary | The paper must explain why it belongs here rather than Experimental Economics, Games and Economic Behavior, Management Science, and Journal of Public Economics |
| Evidence standard | Designs, models, reviews, or qualitative evidence must match mechanism-forward behavioral evidence with transparent experimental or institutional design |
| Source discipline | Current process facts are cited or marked 待核实 |

## Quick Start

```text
/plugin marketplace add ./Journal-of-Economic-Behavior-and-Organization-Skills
/plugin install jebo-skills
```

Manual use: start with [`skills/jebo-workflow/SKILL.md`](skills/jebo-workflow/SKILL.md).

## Default Workflow

```text
jebo-workflow → jebo-topic-selection → jebo-literature-positioning → jebo-identification → jebo-theory-model → jebo-robustness → jebo-tables-figures → jebo-writing-style → jebo-replication-package → jebo-referee-strategy → jebo-submission → jebo-rebuttal
```

## Skills

| # | Skill | What it does |
|---|-------|--------------|
| 1 | [`jebo-workflow`](skills/jebo-workflow/SKILL.md) | Workflow Router for JEBO manuscripts |
| 2 | [`jebo-topic-selection`](skills/jebo-topic-selection/SKILL.md) | Topic Selection for JEBO manuscripts |
| 3 | [`jebo-literature-positioning`](skills/jebo-literature-positioning/SKILL.md) | Literature Positioning for JEBO manuscripts |
| 4 | [`jebo-identification`](skills/jebo-identification/SKILL.md) | Identification Strategy for JEBO manuscripts |
| 5 | [`jebo-theory-model`](skills/jebo-theory-model/SKILL.md) | Theory and Model Craft for JEBO manuscripts |
| 6 | [`jebo-robustness`](skills/jebo-robustness/SKILL.md) | Robustness Strategy for JEBO manuscripts |
| 7 | [`jebo-tables-figures`](skills/jebo-tables-figures/SKILL.md) | Tables and Figures for JEBO manuscripts |
| 8 | [`jebo-writing-style`](skills/jebo-writing-style/SKILL.md) | Writing Style for JEBO manuscripts |
| 9 | [`jebo-replication-package`](skills/jebo-replication-package/SKILL.md) | Replication Package for JEBO manuscripts |
| 10 | [`jebo-referee-strategy`](skills/jebo-referee-strategy/SKILL.md) | Referee Strategy for JEBO manuscripts |
| 11 | [`jebo-submission`](skills/jebo-submission/SKILL.md) | Submission Preflight for JEBO manuscripts |
| 12 | [`jebo-rebuttal`](skills/jebo-rebuttal/SKILL.md) | Rebuttal Strategy for JEBO manuscripts |

## Resources

- [`resources/README.md`](resources/README.md) — resource index
- [`resources/official-source-map.md`](resources/official-source-map.md) — official URLs and volatile checks
- [`resources/external_tools.md`](resources/external_tools.md) — databases, methods, and software aids
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — fictional before/after introduction
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real-paper slots with source discipline
- [`resources/code/`](resources/code/) — empirical code kit where applicable

## Related Links

- https://www.sciencedirect.com/journal/journal-of-economic-behavior-and-organization
- https://www.elsevier.com/journals/journal-of-economic-behavior-and-organization/0167-2681/guide-for-authors

## License

MIT (c) 2026 Bryce Wang. See [LICENSE](LICENSE).
