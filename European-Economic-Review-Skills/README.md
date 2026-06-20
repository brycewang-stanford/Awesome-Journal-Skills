# European Economic Review Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="European Economic Review Skills cover"></p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-European%20Economic%20Review-102a54)](https://www.sciencedirect.com/journal/european-economic-review)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://www.editorialmanager.com/eerev)

English | [简体中文](README.zh-CN.md)

Twelve agent skills for manuscripts targeted at **European Economic Review (EER)**, Elsevier's general-interest economics journal for empirical and theoretical work across all fields. The pack routes a manuscript from broad-interest fit and literature positioning through identification or model craft, robustness, exhibits, writing style, replication readiness, referee strategy, submission preflight, and rebuttal.

**Official basis checked 2026-06** (re-check volatile fee, editor, portal, and policy details before use). Sources and unresolved items are in [`resources/official-source-map.md`](resources/official-source-map.md).

## Quick Start

```
/plugin marketplace add ./European-Economic-Review-Skills
/plugin install eer-skills
```

Manual use: start with [`skills/eer-workflow/SKILL.md`](skills/eer-workflow/SKILL.md), then follow its routing table.

## Skills

| # | Skill | Role |
|---|-------|------|
| 1 | [`eer-workflow`](skills/eer-workflow/SKILL.md) | Route the manuscript to the right EER skill |
| 2 | [`eer-topic-selection`](skills/eer-topic-selection/SKILL.md) | Test broad-interest fit versus field journals and JEEA/EJ |
| 3 | [`eer-literature-positioning`](skills/eer-literature-positioning/SKILL.md) | Place the contribution for a general economics readership |
| 4 | [`eer-identification`](skills/eer-identification/SKILL.md) | Stress-test empirical identification and inference |
| 5 | [`eer-theory-model`](skills/eer-theory-model/SKILL.md) | Tighten theory, mechanisms, or structural modeling |
| 6 | [`eer-robustness`](skills/eer-robustness/SKILL.md) | Organize specification, sample, and inference checks |
| 7 | [`eer-tables-figures`](skills/eer-tables-figures/SKILL.md) | Make exhibits legible and standard-error first |
| 8 | [`eer-writing-style`](skills/eer-writing-style/SKILL.md) | Shape abstract, highlights, and introduction for EER |
| 9 | [`eer-replication-package`](skills/eer-replication-package/SKILL.md) | Prepare data, code, and computational documentation |
| 10 | [`eer-referee-strategy`](skills/eer-referee-strategy/SKILL.md) | Anticipate scope, novelty, and credibility objections |
| 11 | [`eer-submission`](skills/eer-submission/SKILL.md) | Run the Editorial Manager preflight |
| 12 | [`eer-rebuttal`](skills/eer-rebuttal/SKILL.md) | Draft a disciplined response and revision plan |

## Resources

- [`resources/official-source-map.md`](resources/official-source-map.md) — source map for EER facts
- [`resources/code/`](resources/code/) — empirical Stata/Python code kit

## License

MIT (c) 2026 Bryce Wang. See [LICENSE](LICENSE).
