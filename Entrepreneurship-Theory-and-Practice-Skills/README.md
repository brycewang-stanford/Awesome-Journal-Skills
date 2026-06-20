# Entrepreneurship Theory and Practice Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Entrepreneurship Theory and Practice Skills cover"></p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-etp-102a54)](https://journals.sagepub.com/home/etp)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://journals.sagepub.com/home/etp)

English | [简体中文](README.zh-CN.md)

Twelve agent skills for manuscripts targeted at **Entrepreneurship Theory and Practice (ETP)**. The pack is tuned to entrepreneurship theory, new ventures, founder teams, entrepreneurial finance, ecosystems, and family business; it keeps the manuscript distinct from Journal of Business Venturing, Strategic Entrepreneurship Journal, Research Policy, and Academy of Management Journal and emphasizes entrepreneurship theory with credible venture-level evidence and boundary conditions.

**Official basis checked 2026-06** (re-check volatile details before submission): see [`resources/official-source-map.md`](resources/official-source-map.md).

## Why a separate stack?

| ETP constraint | What it forces |
|-------------------------|----------------|
| Scope | The main claim must speak to entrepreneurship theory, new ventures, founder teams, entrepreneurial finance, ecosystems, and family business |
| Sibling boundary | The paper must explain why it belongs here rather than Journal of Business Venturing, Strategic Entrepreneurship Journal, Research Policy, and Academy of Management Journal |
| Evidence standard | Designs, models, reviews, or qualitative evidence must match entrepreneurship theory with credible venture-level evidence and boundary conditions |
| Source discipline | Current process facts are cited or marked 待核实 |

## Quick Start

```text
/plugin marketplace add ./Entrepreneurship-Theory-and-Practice-Skills
/plugin install entrepreneurship-theory-and-practice-skills
```

Manual use: start with [`skills/etp-workflow/SKILL.md`](skills/etp-workflow/SKILL.md).

## Default Workflow

```text
etp-workflow → etp-topic-selection → etp-theory-development → etp-literature-positioning → etp-methods → etp-data-analysis → etp-contribution-framing → etp-tables-figures → etp-writing-style → etp-submission → etp-review-process → etp-rebuttal
```

## Skills

| # | Skill | What it does |
|---|-------|--------------|
| 1 | [`etp-workflow`](skills/etp-workflow/SKILL.md) | Workflow Router for ETP manuscripts |
| 2 | [`etp-topic-selection`](skills/etp-topic-selection/SKILL.md) | Topic Selection for ETP manuscripts |
| 3 | [`etp-theory-development`](skills/etp-theory-development/SKILL.md) | Theory Development for ETP manuscripts |
| 4 | [`etp-literature-positioning`](skills/etp-literature-positioning/SKILL.md) | Literature Positioning for ETP manuscripts |
| 5 | [`etp-methods`](skills/etp-methods/SKILL.md) | Methods for ETP manuscripts |
| 6 | [`etp-data-analysis`](skills/etp-data-analysis/SKILL.md) | Data Analysis for ETP manuscripts |
| 7 | [`etp-contribution-framing`](skills/etp-contribution-framing/SKILL.md) | Contribution Framing for ETP manuscripts |
| 8 | [`etp-tables-figures`](skills/etp-tables-figures/SKILL.md) | Tables and Figures for ETP manuscripts |
| 9 | [`etp-writing-style`](skills/etp-writing-style/SKILL.md) | Writing Style for ETP manuscripts |
| 10 | [`etp-submission`](skills/etp-submission/SKILL.md) | Submission Preflight for ETP manuscripts |
| 11 | [`etp-review-process`](skills/etp-review-process/SKILL.md) | Review Process for ETP manuscripts |
| 12 | [`etp-rebuttal`](skills/etp-rebuttal/SKILL.md) | Rebuttal Strategy for ETP manuscripts |

## Resources

- [`resources/README.md`](resources/README.md) — resource index
- [`resources/official-source-map.md`](resources/official-source-map.md) — official URLs and volatile checks
- [`resources/external_tools.md`](resources/external_tools.md) — databases, methods, and software aids
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — fictional before/after introduction
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real-paper slots with source discipline
- [`resources/code/`](resources/code/) — empirical code kit where applicable

## Related Links

- https://journals.sagepub.com/home/etp
- https://journals.sagepub.com/author-instructions/ETP

## License

MIT (c) 2026 Bryce Wang. See [LICENSE](LICENSE).
