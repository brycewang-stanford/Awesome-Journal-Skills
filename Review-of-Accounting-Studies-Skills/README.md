# Review of Accounting Studies Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Review of Accounting Studies Skills cover"></p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-rast-102a54)](https://link.springer.com/journal/11142)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://link.springer.com/journal/11142)

English | [简体中文](README.zh-CN.md)

Twelve agent skills for manuscripts targeted at **Review of Accounting Studies (RAST)**. The pack is tuned to analytical, empirical, and experimental accounting research with strong economics foundations; it keeps the manuscript distinct from The Accounting Review, Journal of Accounting Research, Journal of Accounting and Economics, and Contemporary Accounting Research and emphasizes accounting research that links institutional reporting detail to credible economic mechanisms.

**Official basis checked 2026-06** (re-check volatile details before submission): see [`resources/official-source-map.md`](resources/official-source-map.md).

## Why a separate stack?

| RAST constraint | What it forces |
|-------------------------|----------------|
| Scope | The main claim must speak to analytical, empirical, and experimental accounting research with strong economics foundations |
| Sibling boundary | The paper must explain why it belongs here rather than The Accounting Review, Journal of Accounting Research, Journal of Accounting and Economics, and Contemporary Accounting Research |
| Evidence standard | Designs, models, reviews, or qualitative evidence must match accounting research that links institutional reporting detail to credible economic mechanisms |
| Source discipline | Current process facts are cited or marked 待核实 |

## Quick Start

```text
/plugin marketplace add ./Review-of-Accounting-Studies-Skills
/plugin install review-of-accounting-studies-skills
```

Manual use: start with [`skills/revacc-workflow/SKILL.md`](skills/revacc-workflow/SKILL.md).

## Default Workflow

```text
revacc-workflow → revacc-topic-selection → revacc-theory-development → revacc-literature-positioning → revacc-methods → revacc-data-analysis → revacc-contribution-framing → revacc-tables-figures → revacc-writing-style → revacc-submission → revacc-review-process → revacc-rebuttal
```

## Skills

| # | Skill | What it does |
|---|-------|--------------|
| 1 | [`revacc-workflow`](skills/revacc-workflow/SKILL.md) | Workflow Router for RAST manuscripts |
| 2 | [`revacc-topic-selection`](skills/revacc-topic-selection/SKILL.md) | Topic Selection for RAST manuscripts |
| 3 | [`revacc-theory-development`](skills/revacc-theory-development/SKILL.md) | Theory Development for RAST manuscripts |
| 4 | [`revacc-literature-positioning`](skills/revacc-literature-positioning/SKILL.md) | Literature Positioning for RAST manuscripts |
| 5 | [`revacc-methods`](skills/revacc-methods/SKILL.md) | Methods for RAST manuscripts |
| 6 | [`revacc-data-analysis`](skills/revacc-data-analysis/SKILL.md) | Data Analysis for RAST manuscripts |
| 7 | [`revacc-contribution-framing`](skills/revacc-contribution-framing/SKILL.md) | Contribution Framing for RAST manuscripts |
| 8 | [`revacc-tables-figures`](skills/revacc-tables-figures/SKILL.md) | Tables and Figures for RAST manuscripts |
| 9 | [`revacc-writing-style`](skills/revacc-writing-style/SKILL.md) | Writing Style for RAST manuscripts |
| 10 | [`revacc-submission`](skills/revacc-submission/SKILL.md) | Submission Preflight for RAST manuscripts |
| 11 | [`revacc-review-process`](skills/revacc-review-process/SKILL.md) | Review Process for RAST manuscripts |
| 12 | [`revacc-rebuttal`](skills/revacc-rebuttal/SKILL.md) | Rebuttal Strategy for RAST manuscripts |

## Resources

- [`resources/README.md`](resources/README.md) — resource index
- [`resources/official-source-map.md`](resources/official-source-map.md) — official URLs and volatile checks
- [`resources/external_tools.md`](resources/external_tools.md) — databases, methods, and software aids
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — fictional before/after introduction
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real-paper slots with source discipline
- [`resources/code/`](resources/code/) — empirical code kit where applicable

## Related Links

- https://link.springer.com/journal/11142
- https://www.springer.com/journal/11142/submission-guidelines

## License

MIT (c) 2026 Bryce Wang. See [LICENSE](LICENSE).
