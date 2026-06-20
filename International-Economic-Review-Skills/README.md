# International Economic Review Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="International Economic Review Skills cover"></p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-ier-102a54)](https://onlinelibrary.wiley.com/journal/14682354)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://onlinelibrary.wiley.com/journal/14682354)

English | [简体中文](README.zh-CN.md)

Twelve agent skills for manuscripts targeted at **International Economic Review (IER)**. The pack is tuned to general-interest economics with a distinctive theory, econometrics, macro, micro, and international reach; it keeps the manuscript distinct from QJE, JPE, REStud, Econometrica, The Economic Journal, and European Economic Review and emphasizes formal economics argument with enough intuition for a broad journal audience.

**Official basis checked 2026-06** (re-check volatile details before submission): see [`resources/official-source-map.md`](resources/official-source-map.md).

## Why a separate stack?

| IER constraint | What it forces |
|-------------------------|----------------|
| Scope | The main claim must speak to general-interest economics with a distinctive theory, econometrics, macro, micro, and international reach |
| Sibling boundary | The paper must explain why it belongs here rather than QJE, JPE, REStud, Econometrica, The Economic Journal, and European Economic Review |
| Evidence standard | Designs, models, reviews, or qualitative evidence must match formal economics argument with enough intuition for a broad journal audience |
| Source discipline | Current process facts are cited or marked 待核实 |

## Quick Start

```text
/plugin marketplace add ./International-Economic-Review-Skills
/plugin install ier-skills
```

Manual use: start with [`skills/ier-workflow/SKILL.md`](skills/ier-workflow/SKILL.md).

## Default Workflow

```text
ier-workflow → ier-topic-selection → ier-literature-positioning → ier-identification → ier-theory-model → ier-robustness → ier-tables-figures → ier-writing-style → ier-replication-package → ier-referee-strategy → ier-submission → ier-rebuttal
```

## Skills

| # | Skill | What it does |
|---|-------|--------------|
| 1 | [`ier-workflow`](skills/ier-workflow/SKILL.md) | Workflow Router for IER manuscripts |
| 2 | [`ier-topic-selection`](skills/ier-topic-selection/SKILL.md) | Topic Selection for IER manuscripts |
| 3 | [`ier-literature-positioning`](skills/ier-literature-positioning/SKILL.md) | Literature Positioning for IER manuscripts |
| 4 | [`ier-identification`](skills/ier-identification/SKILL.md) | Identification Strategy for IER manuscripts |
| 5 | [`ier-theory-model`](skills/ier-theory-model/SKILL.md) | Theory and Model Craft for IER manuscripts |
| 6 | [`ier-robustness`](skills/ier-robustness/SKILL.md) | Robustness Strategy for IER manuscripts |
| 7 | [`ier-tables-figures`](skills/ier-tables-figures/SKILL.md) | Tables and Figures for IER manuscripts |
| 8 | [`ier-writing-style`](skills/ier-writing-style/SKILL.md) | Writing Style for IER manuscripts |
| 9 | [`ier-replication-package`](skills/ier-replication-package/SKILL.md) | Replication Package for IER manuscripts |
| 10 | [`ier-referee-strategy`](skills/ier-referee-strategy/SKILL.md) | Referee Strategy for IER manuscripts |
| 11 | [`ier-submission`](skills/ier-submission/SKILL.md) | Submission Preflight for IER manuscripts |
| 12 | [`ier-rebuttal`](skills/ier-rebuttal/SKILL.md) | Rebuttal Strategy for IER manuscripts |

## Resources

- [`resources/README.md`](resources/README.md) — resource index
- [`resources/official-source-map.md`](resources/official-source-map.md) — official URLs and volatile checks
- [`resources/external_tools.md`](resources/external_tools.md) — databases, methods, and software aids
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — fictional before/after introduction
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real-paper slots with source discipline
- [`resources/code/`](resources/code/) — empirical code kit where applicable

## Related Links

- https://onlinelibrary.wiley.com/journal/14682354
- https://onlinelibrary.wiley.com/page/journal/14682354/homepage/forauthors.html

## License

MIT (c) 2026 Bryce Wang. See [LICENSE](LICENSE).
