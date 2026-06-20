# IMF Economic Review Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="IMF Economic Review Skills cover"></p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-imfer-102a54)](https://link.springer.com/journal/41308)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://link.springer.com/journal/41308)

English | [简体中文](README.zh-CN.md)

Twelve agent skills for manuscripts targeted at **IMF Economic Review (IMFER)**. The pack is tuned to international macroeconomics, finance, development, policy, exchange rates, sovereign risk, and IMF-relevant evidence; it keeps the manuscript distinct from Journal of International Economics, JIMF, JMCB, and Economic Policy and emphasizes policy-facing international macro evidence with transparent country coverage and model assumptions.

**Official basis checked 2026-06** (re-check volatile details before submission): see [`resources/official-source-map.md`](resources/official-source-map.md).

## Why a separate stack?

| IMFER constraint | What it forces |
|-------------------------|----------------|
| Scope | The main claim must speak to international macroeconomics, finance, development, policy, exchange rates, sovereign risk, and IMF-relevant evidence |
| Sibling boundary | The paper must explain why it belongs here rather than Journal of International Economics, JIMF, JMCB, and Economic Policy |
| Evidence standard | Designs, models, reviews, or qualitative evidence must match policy-facing international macro evidence with transparent country coverage and model assumptions |
| Source discipline | Current process facts are cited or marked 待核实 |

## Quick Start

```text
/plugin marketplace add ./IMF-Economic-Review-Skills
/plugin install imf-economic-review-skills
```

Manual use: start with [`skills/imfer-workflow/SKILL.md`](skills/imfer-workflow/SKILL.md).

## Default Workflow

```text
imfer-workflow → imfer-topic-selection → imfer-literature-positioning → imfer-identification → imfer-theory-model → imfer-robustness → imfer-tables-figures → imfer-writing-style → imfer-replication-package → imfer-referee-strategy → imfer-submission → imfer-rebuttal
```

## Skills

| # | Skill | What it does |
|---|-------|--------------|
| 1 | [`imfer-workflow`](skills/imfer-workflow/SKILL.md) | Workflow Router for IMFER manuscripts |
| 2 | [`imfer-topic-selection`](skills/imfer-topic-selection/SKILL.md) | Topic Selection for IMFER manuscripts |
| 3 | [`imfer-literature-positioning`](skills/imfer-literature-positioning/SKILL.md) | Literature Positioning for IMFER manuscripts |
| 4 | [`imfer-identification`](skills/imfer-identification/SKILL.md) | Identification Strategy for IMFER manuscripts |
| 5 | [`imfer-theory-model`](skills/imfer-theory-model/SKILL.md) | Theory and Model Craft for IMFER manuscripts |
| 6 | [`imfer-robustness`](skills/imfer-robustness/SKILL.md) | Robustness Strategy for IMFER manuscripts |
| 7 | [`imfer-tables-figures`](skills/imfer-tables-figures/SKILL.md) | Tables and Figures for IMFER manuscripts |
| 8 | [`imfer-writing-style`](skills/imfer-writing-style/SKILL.md) | Writing Style for IMFER manuscripts |
| 9 | [`imfer-replication-package`](skills/imfer-replication-package/SKILL.md) | Replication Package for IMFER manuscripts |
| 10 | [`imfer-referee-strategy`](skills/imfer-referee-strategy/SKILL.md) | Referee Strategy for IMFER manuscripts |
| 11 | [`imfer-submission`](skills/imfer-submission/SKILL.md) | Submission Preflight for IMFER manuscripts |
| 12 | [`imfer-rebuttal`](skills/imfer-rebuttal/SKILL.md) | Rebuttal Strategy for IMFER manuscripts |

## Resources

- [`resources/README.md`](resources/README.md) — resource index
- [`resources/official-source-map.md`](resources/official-source-map.md) — official URLs and volatile checks
- [`resources/external_tools.md`](resources/external_tools.md) — databases, methods, and software aids
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — fictional before/after introduction
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real-paper slots with source discipline
- [`resources/code/`](resources/code/) — empirical code kit where applicable

## Related Links

- https://link.springer.com/journal/41308
- https://www.springer.com/journal/41308/submission-guidelines

## License

MIT (c) 2026 Bryce Wang. See [LICENSE](LICENSE).
