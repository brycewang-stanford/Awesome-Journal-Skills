# Journal of Management Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Journal of Management Skills cover"></p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-jomgmt-102a54)](https://journals.sagepub.com/home/jom)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://journals.sagepub.com/home/jom)

English | [简体中文](README.zh-CN.md)

Twelve agent skills for manuscripts targeted at **Journal of Management (JOMgmt)**. The pack is tuned to management theory and empirical work across organizational behavior, strategy, HR, entrepreneurship, and research methods; it keeps the manuscript distinct from Academy of Management Journal, Strategic Management Journal, Organization Science, and Journal of Management Studies and emphasizes theory-driven management research with clean construct logic and robust empirical design.

**Official basis checked 2026-06** (re-check volatile details before submission): see [`resources/official-source-map.md`](resources/official-source-map.md).

## Why a separate stack?

| JOMgmt constraint | What it forces |
|-------------------------|----------------|
| Scope | The main claim must speak to management theory and empirical work across organizational behavior, strategy, HR, entrepreneurship, and research methods |
| Sibling boundary | The paper must explain why it belongs here rather than Academy of Management Journal, Strategic Management Journal, Organization Science, and Journal of Management Studies |
| Evidence standard | Designs, models, reviews, or qualitative evidence must match theory-driven management research with clean construct logic and robust empirical design |
| Source discipline | Current process facts are cited or marked 待核实 |

## Quick Start

```text
/plugin marketplace add ./Journal-of-Management-Skills
/plugin install journal-of-management-skills
```

Manual use: start with [`skills/jmgmt-workflow/SKILL.md`](skills/jmgmt-workflow/SKILL.md).

## Default Workflow

```text
jmgmt-workflow → jmgmt-topic-selection → jmgmt-theory-development → jmgmt-literature-positioning → jmgmt-methods → jmgmt-data-analysis → jmgmt-contribution-framing → jmgmt-tables-figures → jmgmt-writing-style → jmgmt-submission → jmgmt-review-process → jmgmt-rebuttal
```

## Skills

| # | Skill | What it does |
|---|-------|--------------|
| 1 | [`jmgmt-workflow`](skills/jmgmt-workflow/SKILL.md) | Workflow Router for JOMgmt manuscripts |
| 2 | [`jmgmt-topic-selection`](skills/jmgmt-topic-selection/SKILL.md) | Topic Selection for JOMgmt manuscripts |
| 3 | [`jmgmt-theory-development`](skills/jmgmt-theory-development/SKILL.md) | Theory Development for JOMgmt manuscripts |
| 4 | [`jmgmt-literature-positioning`](skills/jmgmt-literature-positioning/SKILL.md) | Literature Positioning for JOMgmt manuscripts |
| 5 | [`jmgmt-methods`](skills/jmgmt-methods/SKILL.md) | Methods for JOMgmt manuscripts |
| 6 | [`jmgmt-data-analysis`](skills/jmgmt-data-analysis/SKILL.md) | Data Analysis for JOMgmt manuscripts |
| 7 | [`jmgmt-contribution-framing`](skills/jmgmt-contribution-framing/SKILL.md) | Contribution Framing for JOMgmt manuscripts |
| 8 | [`jmgmt-tables-figures`](skills/jmgmt-tables-figures/SKILL.md) | Tables and Figures for JOMgmt manuscripts |
| 9 | [`jmgmt-writing-style`](skills/jmgmt-writing-style/SKILL.md) | Writing Style for JOMgmt manuscripts |
| 10 | [`jmgmt-submission`](skills/jmgmt-submission/SKILL.md) | Submission Preflight for JOMgmt manuscripts |
| 11 | [`jmgmt-review-process`](skills/jmgmt-review-process/SKILL.md) | Review Process for JOMgmt manuscripts |
| 12 | [`jmgmt-rebuttal`](skills/jmgmt-rebuttal/SKILL.md) | Rebuttal Strategy for JOMgmt manuscripts |

## Resources

- [`resources/README.md`](resources/README.md) — resource index
- [`resources/official-source-map.md`](resources/official-source-map.md) — official URLs and volatile checks
- [`resources/external_tools.md`](resources/external_tools.md) — databases, methods, and software aids
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — fictional before/after introduction
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real-paper slots with source discipline
- [`resources/code/`](resources/code/) — empirical code kit where applicable

## Related Links

- https://journals.sagepub.com/home/jom
- https://journals.sagepub.com/author-instructions/JOM

## License

MIT (c) 2026 Bryce Wang. See [LICENSE](LICENSE).
