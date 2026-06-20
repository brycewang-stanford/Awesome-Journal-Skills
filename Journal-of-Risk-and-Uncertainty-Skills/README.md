# Journal of Risk and Uncertainty Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Journal of Risk and Uncertainty Skills cover"></p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-jru-102a54)](https://link.springer.com/journal/11166)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://link.springer.com/journal/11166)

English | [简体中文](README.zh-CN.md)

Twelve agent skills for manuscripts targeted at **Journal of Risk and Uncertainty (JRU)**. The pack is tuned to risk, uncertainty, decision theory, behavioral choice, insurance, and experimental evidence on risky decisions; it keeps the manuscript distinct from Experimental Economics, Journal of Economic Behavior and Organization, Games and Economic Behavior, and Management Science and emphasizes decision-theoretic clarity with careful measurement of risk and uncertainty.

**Official basis checked 2026-06** (re-check volatile details before submission): see [`resources/official-source-map.md`](resources/official-source-map.md).

## Why a separate stack?

| JRU constraint | What it forces |
|-------------------------|----------------|
| Scope | The main claim must speak to risk, uncertainty, decision theory, behavioral choice, insurance, and experimental evidence on risky decisions |
| Sibling boundary | The paper must explain why it belongs here rather than Experimental Economics, Journal of Economic Behavior and Organization, Games and Economic Behavior, and Management Science |
| Evidence standard | Designs, models, reviews, or qualitative evidence must match decision-theoretic clarity with careful measurement of risk and uncertainty |
| Source discipline | Current process facts are cited or marked 待核实 |

## Quick Start

```text
/plugin marketplace add ./Journal-of-Risk-and-Uncertainty-Skills
/plugin install jru-skills
```

Manual use: start with [`skills/jru-workflow/SKILL.md`](skills/jru-workflow/SKILL.md).

## Default Workflow

```text
jru-workflow → jru-topic-selection → jru-literature-positioning → jru-identification → jru-theory-model → jru-robustness → jru-tables-figures → jru-writing-style → jru-replication-package → jru-referee-strategy → jru-submission → jru-rebuttal
```

## Skills

| # | Skill | What it does |
|---|-------|--------------|
| 1 | [`jru-workflow`](skills/jru-workflow/SKILL.md) | Workflow Router for JRU manuscripts |
| 2 | [`jru-topic-selection`](skills/jru-topic-selection/SKILL.md) | Topic Selection for JRU manuscripts |
| 3 | [`jru-literature-positioning`](skills/jru-literature-positioning/SKILL.md) | Literature Positioning for JRU manuscripts |
| 4 | [`jru-identification`](skills/jru-identification/SKILL.md) | Identification Strategy for JRU manuscripts |
| 5 | [`jru-theory-model`](skills/jru-theory-model/SKILL.md) | Theory and Model Craft for JRU manuscripts |
| 6 | [`jru-robustness`](skills/jru-robustness/SKILL.md) | Robustness Strategy for JRU manuscripts |
| 7 | [`jru-tables-figures`](skills/jru-tables-figures/SKILL.md) | Tables and Figures for JRU manuscripts |
| 8 | [`jru-writing-style`](skills/jru-writing-style/SKILL.md) | Writing Style for JRU manuscripts |
| 9 | [`jru-replication-package`](skills/jru-replication-package/SKILL.md) | Replication Package for JRU manuscripts |
| 10 | [`jru-referee-strategy`](skills/jru-referee-strategy/SKILL.md) | Referee Strategy for JRU manuscripts |
| 11 | [`jru-submission`](skills/jru-submission/SKILL.md) | Submission Preflight for JRU manuscripts |
| 12 | [`jru-rebuttal`](skills/jru-rebuttal/SKILL.md) | Rebuttal Strategy for JRU manuscripts |

## Resources

- [`resources/README.md`](resources/README.md) — resource index
- [`resources/official-source-map.md`](resources/official-source-map.md) — official URLs and volatile checks
- [`resources/external_tools.md`](resources/external_tools.md) — databases, methods, and software aids
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — fictional before/after introduction
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real-paper slots with source discipline
- [`resources/code/`](resources/code/) — empirical code kit where applicable

## Related Links

- https://link.springer.com/journal/11166
- https://www.springer.com/journal/11166/submission-guidelines

## License

MIT (c) 2026 Bryce Wang. See [LICENSE](LICENSE).
