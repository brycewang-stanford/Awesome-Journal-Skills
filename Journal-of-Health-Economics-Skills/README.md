# Journal of Health Economics Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Journal of Health Economics Skills cover"></p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-jhe-102a54)](https://www.sciencedirect.com/journal/journal-of-health-economics)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://www.sciencedirect.com/journal/journal-of-health-economics)

English | [简体中文](README.zh-CN.md)

Twelve agent skills for manuscripts targeted at **Journal of Health Economics (JHE)**. The pack is tuned to health economics, insurance, provider incentives, medical technology, health policy, and health behavior; it keeps the manuscript distinct from American Journal of Health Economics, Journal of Public Economics, Health Economics, and AEJ Economic Policy and emphasizes policy-relevant causal evidence with institutional health-system detail.

**Official basis checked 2026-06** (re-check volatile details before submission): see [`resources/official-source-map.md`](resources/official-source-map.md).

## Why a separate stack?

| JHE constraint | What it forces |
|-------------------------|----------------|
| Scope | The main claim must speak to health economics, insurance, provider incentives, medical technology, health policy, and health behavior |
| Sibling boundary | The paper must explain why it belongs here rather than American Journal of Health Economics, Journal of Public Economics, Health Economics, and AEJ Economic Policy |
| Evidence standard | Designs, models, reviews, or qualitative evidence must match policy-relevant causal evidence with institutional health-system detail |
| Source discipline | Current process facts are cited or marked 待核实 |

## Quick Start

```text
/plugin marketplace add ./Journal-of-Health-Economics-Skills
/plugin install jhe-skills
```

Manual use: start with [`skills/jhe-workflow/SKILL.md`](skills/jhe-workflow/SKILL.md).

## Default Workflow

```text
jhe-workflow → jhe-topic-selection → jhe-literature-positioning → jhe-identification → jhe-theory-model → jhe-robustness → jhe-tables-figures → jhe-writing-style → jhe-replication-package → jhe-referee-strategy → jhe-submission → jhe-rebuttal
```

## Skills

| # | Skill | What it does |
|---|-------|--------------|
| 1 | [`jhe-workflow`](skills/jhe-workflow/SKILL.md) | Workflow Router for JHE manuscripts |
| 2 | [`jhe-topic-selection`](skills/jhe-topic-selection/SKILL.md) | Topic Selection for JHE manuscripts |
| 3 | [`jhe-literature-positioning`](skills/jhe-literature-positioning/SKILL.md) | Literature Positioning for JHE manuscripts |
| 4 | [`jhe-identification`](skills/jhe-identification/SKILL.md) | Identification Strategy for JHE manuscripts |
| 5 | [`jhe-theory-model`](skills/jhe-theory-model/SKILL.md) | Theory and Model Craft for JHE manuscripts |
| 6 | [`jhe-robustness`](skills/jhe-robustness/SKILL.md) | Robustness Strategy for JHE manuscripts |
| 7 | [`jhe-tables-figures`](skills/jhe-tables-figures/SKILL.md) | Tables and Figures for JHE manuscripts |
| 8 | [`jhe-writing-style`](skills/jhe-writing-style/SKILL.md) | Writing Style for JHE manuscripts |
| 9 | [`jhe-replication-package`](skills/jhe-replication-package/SKILL.md) | Replication Package for JHE manuscripts |
| 10 | [`jhe-referee-strategy`](skills/jhe-referee-strategy/SKILL.md) | Referee Strategy for JHE manuscripts |
| 11 | [`jhe-submission`](skills/jhe-submission/SKILL.md) | Submission Preflight for JHE manuscripts |
| 12 | [`jhe-rebuttal`](skills/jhe-rebuttal/SKILL.md) | Rebuttal Strategy for JHE manuscripts |

## Resources

- [`resources/README.md`](resources/README.md) — resource index
- [`resources/official-source-map.md`](resources/official-source-map.md) — official URLs and volatile checks
- [`resources/external_tools.md`](resources/external_tools.md) — databases, methods, and software aids
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — fictional before/after introduction
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real-paper slots with source discipline
- [`resources/code/`](resources/code/) — empirical code kit where applicable

## Related Links

- https://www.sciencedirect.com/journal/journal-of-health-economics
- https://www.elsevier.com/journals/journal-of-health-economics/0167-6296/guide-for-authors

## License

MIT (c) 2026 Bryce Wang. See [LICENSE](LICENSE).
