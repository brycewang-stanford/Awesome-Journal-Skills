# Journal of Money, Credit and Banking Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Journal of Money, Credit and Banking Skills cover"></p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-jmcb-102a54)](https://onlinelibrary.wiley.com/journal/15384616)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://onlinelibrary.wiley.com/journal/15384616)

English | [简体中文](README.zh-CN.md)

Twelve agent skills for manuscripts targeted at **Journal of Money, Credit and Banking (JMCB)**. The pack is tuned to monetary economics, banking, credit markets, financial intermediation, and macro-finance; it keeps the manuscript distinct from Journal of Monetary Economics, Review of Economic Dynamics, Journal of Finance, and Journal of Financial Intermediation and emphasizes policy-relevant macro-finance evidence with transparent timing and institutional detail.

**Official basis checked 2026-06** (re-check volatile details before submission): see [`resources/official-source-map.md`](resources/official-source-map.md).

## Why a separate stack?

| JMCB constraint | What it forces |
|-------------------------|----------------|
| Scope | The main claim must speak to monetary economics, banking, credit markets, financial intermediation, and macro-finance |
| Sibling boundary | The paper must explain why it belongs here rather than Journal of Monetary Economics, Review of Economic Dynamics, Journal of Finance, and Journal of Financial Intermediation |
| Evidence standard | Designs, models, reviews, or qualitative evidence must match policy-relevant macro-finance evidence with transparent timing and institutional detail |
| Source discipline | Current process facts are cited or marked 待核实 |

## Quick Start

```text
/plugin marketplace add ./Journal-of-Money-Credit-and-Banking-Skills
/plugin install jmcb-skills
```

Manual use: start with [`skills/jmcb-workflow/SKILL.md`](skills/jmcb-workflow/SKILL.md).

## Default Workflow

```text
jmcb-workflow → jmcb-topic-selection → jmcb-literature-positioning → jmcb-identification → jmcb-empirical-design → jmcb-robustness → jmcb-tables-figures → jmcb-internet-appendix → jmcb-writing-style → jmcb-submission → jmcb-referee-strategy → jmcb-rebuttal
```

## Skills

| # | Skill | What it does |
|---|-------|--------------|
| 1 | [`jmcb-workflow`](skills/jmcb-workflow/SKILL.md) | Workflow Router for JMCB manuscripts |
| 2 | [`jmcb-topic-selection`](skills/jmcb-topic-selection/SKILL.md) | Topic Selection for JMCB manuscripts |
| 3 | [`jmcb-literature-positioning`](skills/jmcb-literature-positioning/SKILL.md) | Literature Positioning for JMCB manuscripts |
| 4 | [`jmcb-identification`](skills/jmcb-identification/SKILL.md) | Identification Strategy for JMCB manuscripts |
| 5 | [`jmcb-empirical-design`](skills/jmcb-empirical-design/SKILL.md) | Empirical Design for JMCB manuscripts |
| 6 | [`jmcb-robustness`](skills/jmcb-robustness/SKILL.md) | Robustness Strategy for JMCB manuscripts |
| 7 | [`jmcb-tables-figures`](skills/jmcb-tables-figures/SKILL.md) | Tables and Figures for JMCB manuscripts |
| 8 | [`jmcb-internet-appendix`](skills/jmcb-internet-appendix/SKILL.md) | Internet Appendix for JMCB manuscripts |
| 9 | [`jmcb-writing-style`](skills/jmcb-writing-style/SKILL.md) | Writing Style for JMCB manuscripts |
| 10 | [`jmcb-submission`](skills/jmcb-submission/SKILL.md) | Submission Preflight for JMCB manuscripts |
| 11 | [`jmcb-referee-strategy`](skills/jmcb-referee-strategy/SKILL.md) | Referee Strategy for JMCB manuscripts |
| 12 | [`jmcb-rebuttal`](skills/jmcb-rebuttal/SKILL.md) | Rebuttal Strategy for JMCB manuscripts |

## Resources

- [`resources/README.md`](resources/README.md) — resource index
- [`resources/official-source-map.md`](resources/official-source-map.md) — official URLs and volatile checks
- [`resources/external_tools.md`](resources/external_tools.md) — databases, methods, and software aids
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — fictional before/after introduction
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real-paper slots with source discipline
- [`resources/code/`](resources/code/) — empirical code kit where applicable

## Related Links

- https://onlinelibrary.wiley.com/journal/15384616

## License

MIT (c) 2026 Bryce Wang. See [LICENSE](LICENSE).
