# Journal of International Money and Finance Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Journal of International Money and Finance Skills cover"></p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-jimf-102a54)](https://www.sciencedirect.com/journal/journal-of-international-money-and-finance)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://www.sciencedirect.com/journal/journal-of-international-money-and-finance)

English | [简体中文](README.zh-CN.md)

Twelve agent skills for manuscripts targeted at **Journal of International Money and Finance (JIMF)**. The pack is tuned to international finance, exchange rates, global banking, capital flows, and open-economy macro-finance; it keeps the manuscript distinct from Journal of International Economics, Journal of Monetary Economics, JMCB, and Journal of Financial Economics and emphasizes international-finance identification that respects exchange-rate regimes and cross-country comparability.

**Official basis checked 2026-06** (re-check volatile details before submission): see [`resources/official-source-map.md`](resources/official-source-map.md).

## Why a separate stack?

| JIMF constraint | What it forces |
|-------------------------|----------------|
| Scope | The main claim must speak to international finance, exchange rates, global banking, capital flows, and open-economy macro-finance |
| Sibling boundary | The paper must explain why it belongs here rather than Journal of International Economics, Journal of Monetary Economics, JMCB, and Journal of Financial Economics |
| Evidence standard | Designs, models, reviews, or qualitative evidence must match international-finance identification that respects exchange-rate regimes and cross-country comparability |
| Source discipline | Current process facts are cited or marked 待核实 |

## Quick Start

```text
/plugin marketplace add ./Journal-of-International-Money-and-Finance-Skills
/plugin install jimf-skills
```

Manual use: start with [`skills/jimf-workflow/SKILL.md`](skills/jimf-workflow/SKILL.md).

## Default Workflow

```text
jimf-workflow → jimf-topic-selection → jimf-literature-positioning → jimf-identification → jimf-empirical-design → jimf-robustness → jimf-tables-figures → jimf-internet-appendix → jimf-writing-style → jimf-submission → jimf-referee-strategy → jimf-rebuttal
```

## Skills

| # | Skill | What it does |
|---|-------|--------------|
| 1 | [`jimf-workflow`](skills/jimf-workflow/SKILL.md) | Workflow Router for JIMF manuscripts |
| 2 | [`jimf-topic-selection`](skills/jimf-topic-selection/SKILL.md) | Topic Selection for JIMF manuscripts |
| 3 | [`jimf-literature-positioning`](skills/jimf-literature-positioning/SKILL.md) | Literature Positioning for JIMF manuscripts |
| 4 | [`jimf-identification`](skills/jimf-identification/SKILL.md) | Identification Strategy for JIMF manuscripts |
| 5 | [`jimf-empirical-design`](skills/jimf-empirical-design/SKILL.md) | Empirical Design for JIMF manuscripts |
| 6 | [`jimf-robustness`](skills/jimf-robustness/SKILL.md) | Robustness Strategy for JIMF manuscripts |
| 7 | [`jimf-tables-figures`](skills/jimf-tables-figures/SKILL.md) | Tables and Figures for JIMF manuscripts |
| 8 | [`jimf-internet-appendix`](skills/jimf-internet-appendix/SKILL.md) | Internet Appendix for JIMF manuscripts |
| 9 | [`jimf-writing-style`](skills/jimf-writing-style/SKILL.md) | Writing Style for JIMF manuscripts |
| 10 | [`jimf-submission`](skills/jimf-submission/SKILL.md) | Submission Preflight for JIMF manuscripts |
| 11 | [`jimf-referee-strategy`](skills/jimf-referee-strategy/SKILL.md) | Referee Strategy for JIMF manuscripts |
| 12 | [`jimf-rebuttal`](skills/jimf-rebuttal/SKILL.md) | Rebuttal Strategy for JIMF manuscripts |

## Resources

- [`resources/README.md`](resources/README.md) — resource index
- [`resources/official-source-map.md`](resources/official-source-map.md) — official URLs and volatile checks
- [`resources/external_tools.md`](resources/external_tools.md) — databases, methods, and software aids
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — fictional before/after introduction
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real-paper slots with source discipline
- [`resources/code/`](resources/code/) — empirical code kit where applicable

## Related Links

- https://www.sciencedirect.com/journal/journal-of-international-money-and-finance
- https://www.elsevier.com/journals/journal-of-international-money-and-finance/0261-5606/guide-for-authors

## License

MIT (c) 2026 Bryce Wang. See [LICENSE](LICENSE).
