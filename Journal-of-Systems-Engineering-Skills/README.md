# Journal of Systems Engineering Skills

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Journal%20of%20Systems%20Engineering-c0392b)](https://jse.tju.edu.cn/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts submitted to **《系统工程学报》 (Journal of Systems Engineering)**, sponsored by the Systems Engineering Society of China and organized by Tianjin University.

This is not a generic writing bundle. It is built around the journal's verified coverage of systems-engineering theory, methods, and applications, and around recent work in complex systems, optimization and decision, networks and games, data-driven prediction, socioeconomic and financial systems, and engineering applications.

Verified facts and volatile submission requirements are separated in [`resources/official-source-map.md`](resources/official-source-map.md). The recent-issue basis is documented in [`resources/source-basis.md`](resources/source-basis.md).

---

## Why a Separate Stack?

The pack treats a manuscript as journal-specific only when the system boundary, interactions, feedback, or cross-level constraints materially change its model or evidence.

| Nearby venue | Route away from this pack when... |
|---|---|
| 《系统工程理论与实践》 | the center is a broader comprehensive economic-management or policy study and the system structure is not the main increment |
| 《管理科学学报》 | the primary deliverable is a mathematical model with theorem-proof-algorithm rigor and the application is mainly illustrative |
| 《中国管理科学》 | the center is a localized management decision model and computational application rather than a system-level mechanism |
| 《系统工程与电子技术》 | radar, communications, aerospace, equipment systems, or hardware performance is the principal object |
| 《控制与决策》 | controller, observer, state estimation, or control-algorithm performance is the main contribution |
| 《运筹与管理》 | a mature OR method solves a local scheduling, routing, or inventory problem without a necessary systems mechanism |

These are evidence-based routing heuristics, not editorial rules.

---

## The Twelve Skills

| Skill | Role |
|---|---|
| `jse-tju-workflow` | Route by manuscript stage and research strand |
| `jse-tju-fit-positioning` | Judge fit and give an operational rerouting rule |
| `jse-tju-topic-selection` | Build a testable systems problem |
| `jse-tju-literature-review` | Connect domestic, international, and recent journal literature |
| `jse-tju-system-modeling` | Close boundaries, variables, constraints, information, and solvability |
| `jse-tju-theory-analysis` | Design propositions, proofs, comparative statics, and boundaries |
| `jse-tju-algorithm-computation` | Design algorithms and fair computational evidence |
| `jse-tju-validation` | Match evidence to numerical, simulation, data, case, prediction, optimization, or empirical work |
| `jse-tju-robustness-reproducibility` | Stress-test results and document reproduction |
| `jse-tju-writing-tables-figures` | Apply the current journal template and writing conventions |
| `jse-tju-submission` | Run the official-domain submission preflight |
| `jse-tju-rebuttal` | Revise the manuscript and prepare a point-by-point response |

Default route:

```text
workflow → fit-positioning → topic-selection → literature-review
→ system-modeling → theory-analysis / algorithm-computation
→ validation → robustness-reproducibility
→ writing-tables-figures → submission → rebuttal
```

Use only the skills required by the manuscript.

---

## Quick Start

### Claude Code Plugin

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install jse-tju-skills
/reload-plugins
```

### Manual Copy for Claude Code or Codex

```bash
mkdir -p ~/.claude/skills && cp -R skills/jse-tju-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/jse-tju-* ~/.codex/skills/
```

Start with `jse-tju-workflow` and provide the research question, system boundary, main deliverable, current draft stage, and available evidence.

---

## Sources and Maintenance

- [`official-source-map.md`](resources/official-source-map.md): official facts, current submission information, unresolved items, and use locations.
- [`source-basis.md`](resources/source-basis.md): six-issue, thirty-article content profile.
- [`exemplars/library.md`](resources/exemplars/library.md): public metadata only; no article full text.
- [`external_tools.md`](resources/external_tools.md): research and execution tools.
- [`code/README.md`](resources/code/README.md): reproducible execution interface without duplicated large templates.

Editorial and submission requirements change. Confirm all volatile facts against the current official website before submission.

## License

[MIT](LICENSE)
