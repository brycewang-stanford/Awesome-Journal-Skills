# The Journal of Law and Economics Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="The Journal of Law and Economics Skills cover"></p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-jle-102a54)](https://www.journals.uchicago.edu/journals/jle/instruct)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://www.journals.uchicago.edu/journals/jle/instruct)

English | [简体中文](README.zh-CN.md)

Twelve agent skills for manuscripts targeted at **The Journal of Law and Economics (JLE)**. The pack is tuned to law and economics, regulation, property rights, contracts, liability, antitrust, and legal institutions; it keeps the manuscript distinct from Journal of Legal Studies, JLEO, American Law and Economics Review, and Journal of Public Economics and emphasizes economics-first legal analysis that respects doctrine, timing, and institutional assignment.

**Official basis checked 2026-06** (re-check volatile details before submission): see [`resources/official-source-map.md`](resources/official-source-map.md).

## Why a separate stack?

| JLE constraint | What it forces |
|-------------------------|----------------|
| Scope | The main claim must speak to law and economics, regulation, property rights, contracts, liability, antitrust, and legal institutions |
| Sibling boundary | The paper must explain why it belongs here rather than Journal of Legal Studies, JLEO, American Law and Economics Review, and Journal of Public Economics |
| Evidence standard | Designs, models, reviews, or qualitative evidence must match economics-first legal analysis that respects doctrine, timing, and institutional assignment |
| Source discipline | Current process facts are cited or marked 待核实 |

## Quick Start

```text
/plugin marketplace add ./Journal-of-Law-and-Economics-Skills
/plugin install jle-skills
```

Manual use: start with [`skills/jle-workflow/SKILL.md`](skills/jle-workflow/SKILL.md).

## Default Workflow

```text
jle-workflow → jle-topic-selection → jle-literature-positioning → jle-identification → jle-theory-model → jle-robustness → jle-tables-figures → jle-writing-style → jle-replication-package → jle-referee-strategy → jle-submission → jle-rebuttal
```

## Skills

| # | Skill | What it does |
|---|-------|--------------|
| 1 | [`jle-workflow`](skills/jle-workflow/SKILL.md) | Workflow Router for JLE manuscripts |
| 2 | [`jle-topic-selection`](skills/jle-topic-selection/SKILL.md) | Topic Selection for JLE manuscripts |
| 3 | [`jle-literature-positioning`](skills/jle-literature-positioning/SKILL.md) | Literature Positioning for JLE manuscripts |
| 4 | [`jle-identification`](skills/jle-identification/SKILL.md) | Identification Strategy for JLE manuscripts |
| 5 | [`jle-theory-model`](skills/jle-theory-model/SKILL.md) | Theory and Model Craft for JLE manuscripts |
| 6 | [`jle-robustness`](skills/jle-robustness/SKILL.md) | Robustness Strategy for JLE manuscripts |
| 7 | [`jle-tables-figures`](skills/jle-tables-figures/SKILL.md) | Tables and Figures for JLE manuscripts |
| 8 | [`jle-writing-style`](skills/jle-writing-style/SKILL.md) | Writing Style for JLE manuscripts |
| 9 | [`jle-replication-package`](skills/jle-replication-package/SKILL.md) | Replication Package for JLE manuscripts |
| 10 | [`jle-referee-strategy`](skills/jle-referee-strategy/SKILL.md) | Referee Strategy for JLE manuscripts |
| 11 | [`jle-submission`](skills/jle-submission/SKILL.md) | Submission Preflight for JLE manuscripts |
| 12 | [`jle-rebuttal`](skills/jle-rebuttal/SKILL.md) | Rebuttal Strategy for JLE manuscripts |

## Resources

- [`resources/README.md`](resources/README.md) — resource index
- [`resources/official-source-map.md`](resources/official-source-map.md) — official URLs and volatile checks
- [`resources/external_tools.md`](resources/external_tools.md) — databases, methods, and software aids
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — fictional before/after introduction
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real-paper slots with source discipline
- [`resources/code/`](resources/code/) — empirical code kit where applicable

## Related Links

- https://www.journals.uchicago.edu/journals/jle/instruct
- https://www.journals.uchicago.edu/toc/jle/current

## License

MIT (c) 2026 Bryce Wang. See [LICENSE](LICENSE).
