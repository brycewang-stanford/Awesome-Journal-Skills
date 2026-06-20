# Journal of Consumer Psychology Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Journal of Consumer Psychology Skills cover"></p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-jcp-102a54)](https://www.sciencedirect.com/journal/journal-of-consumer-psychology)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://www.sciencedirect.com/journal/journal-of-consumer-psychology)

English | [简体中文](README.zh-CN.md)

Twelve agent skills for manuscripts targeted at **Journal of Consumer Psychology (JCP)**. The pack is tuned to consumer psychology, judgment and decision-making, persuasion, emotion, identity, and consumption behavior; it keeps the manuscript distinct from Journal of Consumer Research, Journal of Marketing Research, Marketing Science, and Psychological Science and emphasizes psychological mechanism evidence tied to consumer behavior and marketing theory.

**Official basis checked 2026-06** (re-check volatile details before submission): see [`resources/official-source-map.md`](resources/official-source-map.md).

## Why a separate stack?

| JCP constraint | What it forces |
|-------------------------|----------------|
| Scope | The main claim must speak to consumer psychology, judgment and decision-making, persuasion, emotion, identity, and consumption behavior |
| Sibling boundary | The paper must explain why it belongs here rather than Journal of Consumer Research, Journal of Marketing Research, Marketing Science, and Psychological Science |
| Evidence standard | Designs, models, reviews, or qualitative evidence must match psychological mechanism evidence tied to consumer behavior and marketing theory |
| Source discipline | Current process facts are cited or marked 待核实 |

## Quick Start

```text
/plugin marketplace add ./Journal-of-Consumer-Psychology-Skills
/plugin install jcp-skills
```

Manual use: start with [`skills/jcp-workflow/SKILL.md`](skills/jcp-workflow/SKILL.md).

## Default Workflow

```text
jcp-workflow → jcp-topic-selection → jcp-theory-development → jcp-literature-positioning → jcp-methods → jcp-data-analysis → jcp-contribution-framing → jcp-tables-figures → jcp-writing-style → jcp-submission → jcp-review-process → jcp-rebuttal
```

## Skills

| # | Skill | What it does |
|---|-------|--------------|
| 1 | [`jcp-workflow`](skills/jcp-workflow/SKILL.md) | Workflow Router for JCP manuscripts |
| 2 | [`jcp-topic-selection`](skills/jcp-topic-selection/SKILL.md) | Topic Selection for JCP manuscripts |
| 3 | [`jcp-theory-development`](skills/jcp-theory-development/SKILL.md) | Theory Development for JCP manuscripts |
| 4 | [`jcp-literature-positioning`](skills/jcp-literature-positioning/SKILL.md) | Literature Positioning for JCP manuscripts |
| 5 | [`jcp-methods`](skills/jcp-methods/SKILL.md) | Methods for JCP manuscripts |
| 6 | [`jcp-data-analysis`](skills/jcp-data-analysis/SKILL.md) | Data Analysis for JCP manuscripts |
| 7 | [`jcp-contribution-framing`](skills/jcp-contribution-framing/SKILL.md) | Contribution Framing for JCP manuscripts |
| 8 | [`jcp-tables-figures`](skills/jcp-tables-figures/SKILL.md) | Tables and Figures for JCP manuscripts |
| 9 | [`jcp-writing-style`](skills/jcp-writing-style/SKILL.md) | Writing Style for JCP manuscripts |
| 10 | [`jcp-submission`](skills/jcp-submission/SKILL.md) | Submission Preflight for JCP manuscripts |
| 11 | [`jcp-review-process`](skills/jcp-review-process/SKILL.md) | Review Process for JCP manuscripts |
| 12 | [`jcp-rebuttal`](skills/jcp-rebuttal/SKILL.md) | Rebuttal Strategy for JCP manuscripts |

## Resources

- [`resources/README.md`](resources/README.md) — resource index
- [`resources/official-source-map.md`](resources/official-source-map.md) — official URLs and volatile checks
- [`resources/external_tools.md`](resources/external_tools.md) — databases, methods, and software aids
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — fictional before/after introduction
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real-paper slots with source discipline
- [`resources/code/`](resources/code/) — empirical code kit where applicable

## Related Links

- https://www.sciencedirect.com/journal/journal-of-consumer-psychology
- https://www.elsevier.com/journals/journal-of-consumer-psychology/1057-7408/guide-for-authors

## License

MIT (c) 2026 Bryce Wang. See [LICENSE](LICENSE).
