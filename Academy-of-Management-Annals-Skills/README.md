# Academy of Management Annals Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Academy of Management Annals Skills cover"></p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-annals-102a54)](https://journals.aom.org/journal/annals)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://journals.aom.org/journal/annals)

English | [简体中文](README.zh-CN.md)

Twelve agent skills for manuscripts targeted at **Academy of Management Annals (Annals)**. The pack is tuned to commissioned and high-level reviews that synthesize management and organization research; it keeps the manuscript distinct from Academy of Management Review, Journal of Management, Journal of Management Studies, and Annual Review outlets and emphasizes field-defining synthesis that reorganizes theory rather than merely cataloging papers.

**Official basis checked 2026-06** (re-check volatile details before submission): see [`resources/official-source-map.md`](resources/official-source-map.md).

## Why a separate stack?

| Annals constraint | What it forces |
|-------------------------|----------------|
| Scope | The main claim must speak to commissioned and high-level reviews that synthesize management and organization research |
| Sibling boundary | The paper must explain why it belongs here rather than Academy of Management Review, Journal of Management, Journal of Management Studies, and Annual Review outlets |
| Evidence standard | Designs, models, reviews, or qualitative evidence must match field-defining synthesis that reorganizes theory rather than merely cataloging papers |
| Source discipline | Current process facts are cited or marked 待核实 |

## Quick Start

```text
/plugin marketplace add ./Academy-of-Management-Annals-Skills
/plugin install academy-of-management-annals-skills
```

Manual use: start with [`skills/amann-workflow/SKILL.md`](skills/amann-workflow/SKILL.md).

## Default Workflow

```text
amann-workflow → amann-topic-selection → amann-proposal-framing → amann-literature-synthesis → amann-organizing-framework → amann-evidence-standards → amann-tables-figures → amann-writing-style → amann-editor-strategy → amann-submission → amann-review-process → amann-revision
```

## Skills

| # | Skill | What it does |
|---|-------|--------------|
| 1 | [`amann-workflow`](skills/amann-workflow/SKILL.md) | Workflow Router for Annals manuscripts |
| 2 | [`amann-topic-selection`](skills/amann-topic-selection/SKILL.md) | Topic Selection for Annals manuscripts |
| 3 | [`amann-proposal-framing`](skills/amann-proposal-framing/SKILL.md) | Proposal Framing for Annals manuscripts |
| 4 | [`amann-literature-synthesis`](skills/amann-literature-synthesis/SKILL.md) | Literature Synthesis for Annals manuscripts |
| 5 | [`amann-organizing-framework`](skills/amann-organizing-framework/SKILL.md) | Organizing Framework for Annals manuscripts |
| 6 | [`amann-evidence-standards`](skills/amann-evidence-standards/SKILL.md) | Evidence Standards for Annals manuscripts |
| 7 | [`amann-tables-figures`](skills/amann-tables-figures/SKILL.md) | Tables and Figures for Annals manuscripts |
| 8 | [`amann-writing-style`](skills/amann-writing-style/SKILL.md) | Writing Style for Annals manuscripts |
| 9 | [`amann-editor-strategy`](skills/amann-editor-strategy/SKILL.md) | Editor Strategy for Annals manuscripts |
| 10 | [`amann-submission`](skills/amann-submission/SKILL.md) | Submission Preflight for Annals manuscripts |
| 11 | [`amann-review-process`](skills/amann-review-process/SKILL.md) | Review Process for Annals manuscripts |
| 12 | [`amann-revision`](skills/amann-revision/SKILL.md) | Revision Strategy for Annals manuscripts |

## Resources

- [`resources/README.md`](resources/README.md) — resource index
- [`resources/official-source-map.md`](resources/official-source-map.md) — official URLs and volatile checks
- [`resources/external_tools.md`](resources/external_tools.md) — databases, methods, and software aids
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — fictional before/after introduction
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real-paper slots with source discipline
- [`resources/code/`](resources/code/) — empirical code kit where applicable

## Related Links

- https://journals.aom.org/journal/annals
- https://aom.org/research/publishing-with-aom/author-resources

## License

MIT (c) 2026 Bryce Wang. See [LICENSE](LICENSE).
