# Journal of Management Information Systems Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Journal of Management Information Systems Skills cover"></p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-jmis-102a54)](https://www.tandfonline.com/journals/mmis20)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://www.tandfonline.com/journals/mmis20)

English | [简体中文](README.zh-CN.md)

Twelve agent skills for manuscripts targeted at **Journal of Management Information Systems (JMIS)**. The pack is tuned to information systems, digital transformation, platforms, analytics, IT governance, and organizational impacts of technology; it keeps the manuscript distinct from MIS Quarterly, Information Systems Research, Journal of the AIS, and Management Science and emphasizes IS scholarship that connects technology mechanisms to organizational and managerial outcomes.

**Official basis checked 2026-06** (re-check volatile details before submission): see [`resources/official-source-map.md`](resources/official-source-map.md).

## Why a separate stack?

| JMIS constraint | What it forces |
|-------------------------|----------------|
| Scope | The main claim must speak to information systems, digital transformation, platforms, analytics, IT governance, and organizational impacts of technology |
| Sibling boundary | The paper must explain why it belongs here rather than MIS Quarterly, Information Systems Research, Journal of the AIS, and Management Science |
| Evidence standard | Designs, models, reviews, or qualitative evidence must match IS scholarship that connects technology mechanisms to organizational and managerial outcomes |
| Source discipline | Current process facts are cited or marked 待核实 |

## Quick Start

```text
/plugin marketplace add ./Journal-of-Management-Information-Systems-Skills
/plugin install jmis-skills
```

Manual use: start with [`skills/jmis-workflow/SKILL.md`](skills/jmis-workflow/SKILL.md).

## Default Workflow

```text
jmis-workflow → jmis-topic-selection → jmis-theory-development → jmis-literature-positioning → jmis-methods → jmis-data-analysis → jmis-contribution-framing → jmis-tables-figures → jmis-writing-style → jmis-submission → jmis-review-process → jmis-rebuttal
```

## Skills

| # | Skill | What it does |
|---|-------|--------------|
| 1 | [`jmis-workflow`](skills/jmis-workflow/SKILL.md) | Workflow Router for JMIS manuscripts |
| 2 | [`jmis-topic-selection`](skills/jmis-topic-selection/SKILL.md) | Topic Selection for JMIS manuscripts |
| 3 | [`jmis-theory-development`](skills/jmis-theory-development/SKILL.md) | Theory Development for JMIS manuscripts |
| 4 | [`jmis-literature-positioning`](skills/jmis-literature-positioning/SKILL.md) | Literature Positioning for JMIS manuscripts |
| 5 | [`jmis-methods`](skills/jmis-methods/SKILL.md) | Methods for JMIS manuscripts |
| 6 | [`jmis-data-analysis`](skills/jmis-data-analysis/SKILL.md) | Data Analysis for JMIS manuscripts |
| 7 | [`jmis-contribution-framing`](skills/jmis-contribution-framing/SKILL.md) | Contribution Framing for JMIS manuscripts |
| 8 | [`jmis-tables-figures`](skills/jmis-tables-figures/SKILL.md) | Tables and Figures for JMIS manuscripts |
| 9 | [`jmis-writing-style`](skills/jmis-writing-style/SKILL.md) | Writing Style for JMIS manuscripts |
| 10 | [`jmis-submission`](skills/jmis-submission/SKILL.md) | Submission Preflight for JMIS manuscripts |
| 11 | [`jmis-review-process`](skills/jmis-review-process/SKILL.md) | Review Process for JMIS manuscripts |
| 12 | [`jmis-rebuttal`](skills/jmis-rebuttal/SKILL.md) | Rebuttal Strategy for JMIS manuscripts |

## Resources

- [`resources/README.md`](resources/README.md) — resource index
- [`resources/official-source-map.md`](resources/official-source-map.md) — official URLs and volatile checks
- [`resources/external_tools.md`](resources/external_tools.md) — databases, methods, and software aids
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — fictional before/after introduction
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real-paper slots with source discipline
- [`resources/code/`](resources/code/) — empirical code kit where applicable

## Related Links

- https://www.tandfonline.com/journals/mmis20
- https://www.tandfonline.com/action/authorSubmission?show=instructions&journalCode=mmis20

## License

MIT (c) 2026 Bryce Wang. See [LICENSE](LICENSE).
