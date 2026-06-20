# Research Policy Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Research Policy Skills cover"></p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-research%20policy-102a54)](https://www.sciencedirect.com/journal/research-policy)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://www.sciencedirect.com/journal/research-policy)

English | [简体中文](README.zh-CN.md)

Twelve agent skills for manuscripts targeted at **Research Policy (Research Policy)**. The pack is tuned to innovation, science policy, technology management, entrepreneurship, R&D, and knowledge production; it keeps the manuscript distinct from Strategic Management Journal, Management Science, Industrial and Corporate Change, and Journal of Business Venturing and emphasizes innovation-policy argument linking mechanisms, institutions, and technology evidence.

**Official basis checked 2026-06** (re-check volatile details before submission): see [`resources/official-source-map.md`](resources/official-source-map.md).

## Why a separate stack?

| Research Policy constraint | What it forces |
|-------------------------|----------------|
| Scope | The main claim must speak to innovation, science policy, technology management, entrepreneurship, R&D, and knowledge production |
| Sibling boundary | The paper must explain why it belongs here rather than Strategic Management Journal, Management Science, Industrial and Corporate Change, and Journal of Business Venturing |
| Evidence standard | Designs, models, reviews, or qualitative evidence must match innovation-policy argument linking mechanisms, institutions, and technology evidence |
| Source discipline | Current process facts are cited or marked 待核实 |

## Quick Start

```text
/plugin marketplace add ./Research-Policy-Skills
/plugin install research-policy-skills
```

Manual use: start with [`skills/respol-workflow/SKILL.md`](skills/respol-workflow/SKILL.md).

## Default Workflow

```text
respol-workflow → respol-topic-selection → respol-theory-development → respol-literature-positioning → respol-methods → respol-data-analysis → respol-contribution-framing → respol-tables-figures → respol-writing-style → respol-submission → respol-review-process → respol-rebuttal
```

## Skills

| # | Skill | What it does |
|---|-------|--------------|
| 1 | [`respol-workflow`](skills/respol-workflow/SKILL.md) | Workflow Router for Research Policy manuscripts |
| 2 | [`respol-topic-selection`](skills/respol-topic-selection/SKILL.md) | Topic Selection for Research Policy manuscripts |
| 3 | [`respol-theory-development`](skills/respol-theory-development/SKILL.md) | Theory Development for Research Policy manuscripts |
| 4 | [`respol-literature-positioning`](skills/respol-literature-positioning/SKILL.md) | Literature Positioning for Research Policy manuscripts |
| 5 | [`respol-methods`](skills/respol-methods/SKILL.md) | Methods for Research Policy manuscripts |
| 6 | [`respol-data-analysis`](skills/respol-data-analysis/SKILL.md) | Data Analysis for Research Policy manuscripts |
| 7 | [`respol-contribution-framing`](skills/respol-contribution-framing/SKILL.md) | Contribution Framing for Research Policy manuscripts |
| 8 | [`respol-tables-figures`](skills/respol-tables-figures/SKILL.md) | Tables and Figures for Research Policy manuscripts |
| 9 | [`respol-writing-style`](skills/respol-writing-style/SKILL.md) | Writing Style for Research Policy manuscripts |
| 10 | [`respol-submission`](skills/respol-submission/SKILL.md) | Submission Preflight for Research Policy manuscripts |
| 11 | [`respol-review-process`](skills/respol-review-process/SKILL.md) | Review Process for Research Policy manuscripts |
| 12 | [`respol-rebuttal`](skills/respol-rebuttal/SKILL.md) | Rebuttal Strategy for Research Policy manuscripts |

## Resources

- [`resources/README.md`](resources/README.md) — resource index
- [`resources/official-source-map.md`](resources/official-source-map.md) — official URLs and volatile checks
- [`resources/external_tools.md`](resources/external_tools.md) — databases, methods, and software aids
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — fictional before/after introduction
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real-paper slots with source discipline
- [`resources/code/`](resources/code/) — empirical code kit where applicable

## Related Links

- https://www.sciencedirect.com/journal/research-policy
- https://www.elsevier.com/journals/research-policy/0048-7333/guide-for-authors

## License

MIT (c) 2026 Bryce Wang. See [LICENSE](LICENSE).
