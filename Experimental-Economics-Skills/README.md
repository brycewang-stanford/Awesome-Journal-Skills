# Experimental Economics Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Experimental Economics Skills cover"></p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-experimental%20economics-102a54)](https://link.springer.com/journal/10683)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://link.springer.com/journal/10683)

English | [简体中文](README.zh-CN.md)

Twelve agent skills for manuscripts targeted at **Experimental Economics (Experimental Economics)**. The pack is tuned to laboratory, field, online, and artefactual experiments in economics; it keeps the manuscript distinct from JEBO, Games and Economic Behavior, Management Science, and Journal of Risk and Uncertainty and emphasizes protocol-transparent experimental economics with credible incentives and robust inference.

**Official basis checked 2026-06** (re-check volatile details before submission): see [`resources/official-source-map.md`](resources/official-source-map.md).

## Why a separate stack?

| Experimental Economics constraint | What it forces |
|-------------------------|----------------|
| Scope | The main claim must speak to laboratory, field, online, and artefactual experiments in economics |
| Sibling boundary | The paper must explain why it belongs here rather than JEBO, Games and Economic Behavior, Management Science, and Journal of Risk and Uncertainty |
| Evidence standard | Designs, models, reviews, or qualitative evidence must match protocol-transparent experimental economics with credible incentives and robust inference |
| Source discipline | Current process facts are cited or marked 待核实 |

## Quick Start

```text
/plugin marketplace add ./Experimental-Economics-Skills
/plugin install experimental-economics-skills
```

Manual use: start with [`skills/expecon-workflow/SKILL.md`](skills/expecon-workflow/SKILL.md).

## Default Workflow

```text
expecon-workflow → expecon-topic-selection → expecon-literature-positioning → expecon-identification → expecon-theory-model → expecon-robustness → expecon-tables-figures → expecon-writing-style → expecon-replication-package → expecon-referee-strategy → expecon-submission → expecon-rebuttal
```

## Skills

| # | Skill | What it does |
|---|-------|--------------|
| 1 | [`expecon-workflow`](skills/expecon-workflow/SKILL.md) | Workflow Router for Experimental Economics manuscripts |
| 2 | [`expecon-topic-selection`](skills/expecon-topic-selection/SKILL.md) | Topic Selection for Experimental Economics manuscripts |
| 3 | [`expecon-literature-positioning`](skills/expecon-literature-positioning/SKILL.md) | Literature Positioning for Experimental Economics manuscripts |
| 4 | [`expecon-identification`](skills/expecon-identification/SKILL.md) | Identification Strategy for Experimental Economics manuscripts |
| 5 | [`expecon-theory-model`](skills/expecon-theory-model/SKILL.md) | Theory and Model Craft for Experimental Economics manuscripts |
| 6 | [`expecon-robustness`](skills/expecon-robustness/SKILL.md) | Robustness Strategy for Experimental Economics manuscripts |
| 7 | [`expecon-tables-figures`](skills/expecon-tables-figures/SKILL.md) | Tables and Figures for Experimental Economics manuscripts |
| 8 | [`expecon-writing-style`](skills/expecon-writing-style/SKILL.md) | Writing Style for Experimental Economics manuscripts |
| 9 | [`expecon-replication-package`](skills/expecon-replication-package/SKILL.md) | Replication Package for Experimental Economics manuscripts |
| 10 | [`expecon-referee-strategy`](skills/expecon-referee-strategy/SKILL.md) | Referee Strategy for Experimental Economics manuscripts |
| 11 | [`expecon-submission`](skills/expecon-submission/SKILL.md) | Submission Preflight for Experimental Economics manuscripts |
| 12 | [`expecon-rebuttal`](skills/expecon-rebuttal/SKILL.md) | Rebuttal Strategy for Experimental Economics manuscripts |

## Resources

- [`resources/README.md`](resources/README.md) — resource index
- [`resources/official-source-map.md`](resources/official-source-map.md) — official URLs and volatile checks
- [`resources/external_tools.md`](resources/external_tools.md) — databases, methods, and software aids
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — fictional before/after introduction
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real-paper slots with source discipline
- [`resources/code/`](resources/code/) — empirical code kit where applicable

## Related Links

- https://link.springer.com/journal/10683
- https://www.springer.com/journal/10683/submission-guidelines

## License

MIT (c) 2026 Bryce Wang. See [LICENSE](LICENSE).
