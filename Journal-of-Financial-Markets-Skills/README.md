# Journal of Financial Markets Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Journal of Financial Markets Skills cover"></p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-jfm-102a54)](https://www.sciencedirect.com/journal/journal-of-financial-markets)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://www.sciencedirect.com/journal/journal-of-financial-markets)

English | [简体中文](README.zh-CN.md)

Twelve agent skills for manuscripts targeted at **Journal of Financial Markets (JFM)**. The pack is tuned to market microstructure, asset pricing, liquidity, trading, and financial-market design; it keeps the manuscript distinct from Journal of Finance, Journal of Financial Economics, Review of Financial Studies, and Management Science and emphasizes precise institutional detail, clean market data, and careful measurement of frictions.

**Official basis checked 2026-06** (re-check volatile details before submission): see [`resources/official-source-map.md`](resources/official-source-map.md).

## Why a separate stack?

| JFM constraint | What it forces |
|-------------------------|----------------|
| Scope | The main claim must speak to market microstructure, asset pricing, liquidity, trading, and financial-market design |
| Sibling boundary | The paper must explain why it belongs here rather than Journal of Finance, Journal of Financial Economics, Review of Financial Studies, and Management Science |
| Evidence standard | Designs, models, reviews, or qualitative evidence must match precise institutional detail, clean market data, and careful measurement of frictions |
| Source discipline | Current process facts are cited or marked 待核实 |

## Quick Start

```text
/plugin marketplace add ./Journal-of-Financial-Markets-Skills
/plugin install jfm-skills
```

Manual use: start with [`skills/jfm-workflow/SKILL.md`](skills/jfm-workflow/SKILL.md).

## Default Workflow

```text
jfm-workflow → jfm-topic-selection → jfm-literature-positioning → jfm-identification → jfm-empirical-design → jfm-robustness → jfm-tables-figures → jfm-internet-appendix → jfm-writing-style → jfm-submission → jfm-referee-strategy → jfm-rebuttal
```

## Skills

| # | Skill | What it does |
|---|-------|--------------|
| 1 | [`jfm-workflow`](skills/jfm-workflow/SKILL.md) | Workflow Router for JFM manuscripts |
| 2 | [`jfm-topic-selection`](skills/jfm-topic-selection/SKILL.md) | Topic Selection for JFM manuscripts |
| 3 | [`jfm-literature-positioning`](skills/jfm-literature-positioning/SKILL.md) | Literature Positioning for JFM manuscripts |
| 4 | [`jfm-identification`](skills/jfm-identification/SKILL.md) | Identification Strategy for JFM manuscripts |
| 5 | [`jfm-empirical-design`](skills/jfm-empirical-design/SKILL.md) | Empirical Design for JFM manuscripts |
| 6 | [`jfm-robustness`](skills/jfm-robustness/SKILL.md) | Robustness Strategy for JFM manuscripts |
| 7 | [`jfm-tables-figures`](skills/jfm-tables-figures/SKILL.md) | Tables and Figures for JFM manuscripts |
| 8 | [`jfm-internet-appendix`](skills/jfm-internet-appendix/SKILL.md) | Internet Appendix for JFM manuscripts |
| 9 | [`jfm-writing-style`](skills/jfm-writing-style/SKILL.md) | Writing Style for JFM manuscripts |
| 10 | [`jfm-submission`](skills/jfm-submission/SKILL.md) | Submission Preflight for JFM manuscripts |
| 11 | [`jfm-referee-strategy`](skills/jfm-referee-strategy/SKILL.md) | Referee Strategy for JFM manuscripts |
| 12 | [`jfm-rebuttal`](skills/jfm-rebuttal/SKILL.md) | Rebuttal Strategy for JFM manuscripts |

## Resources

- [`resources/README.md`](resources/README.md) — resource index
- [`resources/official-source-map.md`](resources/official-source-map.md) — official URLs and volatile checks
- [`resources/external_tools.md`](resources/external_tools.md) — databases, methods, and software aids
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — fictional before/after introduction
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real-paper slots with source discipline
- [`resources/code/`](resources/code/) — empirical code kit where applicable

## Related Links

- https://www.sciencedirect.com/journal/journal-of-financial-markets
- https://www.elsevier.com/journals/journal-of-financial-markets/1386-4181/guide-for-authors

## License

MIT (c) 2026 Bryce Wang. See [LICENSE](LICENSE).
