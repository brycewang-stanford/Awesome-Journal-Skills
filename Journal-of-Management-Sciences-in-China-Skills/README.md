# Journal of Management Sciences in China Skills

<p align="center">
  <img src="assets/cover.svg" alt="《管理科学学报》 journal cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Journal%20of%20Management%20Sciences%20in%20China-c0392b)](https://jmsc.tju.edu.cn/)
[![Index](https://img.shields.io/badge/index-CSSCI%20%7C%20FMS--A-1f6feb)](https://jmsc.tju.edu.cn/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **《管理科学学报》 (Journal of Management Sciences in China, JMSC)** — the flagship quantitative / mathematical management-science journal co-sponsored by the **NSFC Management Science Division (国家自然科学基金委员会管理科学部)** and **Tianjin University** (monthly; ISSN 1007-9807; CN 12-1275/G3).

This repository is opinionated. It is **not** a generic management-writing toolbox. It is a **JMSC-specific** stack built around the journal's defining bar: **a rigorous model + proven propositions + an analyzed algorithm + numerical insight — NOT regression coefficients and policy talk.**

Verified journal facts live in [`resources/journal-profile.md`](resources/journal-profile.md) with source links.

---

## Why a Separate Stack?

JMSC is a 数理 (mathematical / quantitative) journal. Its bar differs sharply from empirical-causal journals (管理世界 / 经济研究) and theory-building journals (南开管理评论):

| Constraint | JMSC | Implication |
|------------|------|-------------|
| Deliverable | Model + proof + algorithm | "We find X affects Y" is off-fit |
| Contribution | New model / property / algorithm | Methodological, not policy |
| Rigor | Explicit assumptions, proven propositions | A model without proof is rejected |
| Algorithm | Complexity / convergence analysis | "It runs fast" is not analysis |
| Validation | Numerical / simulation study | Must validate theory + give managerial insight |
| Managerial point | Decision rule from the model | NOT "加强完善推进" slogans |
| Abstract / length | ≤ 300 chars; ≤ 8000 chars (review ≤ 12000) | Lead with model + result |
| Notes | Numbered refs 〔1〕, by order of appearance | In-text author-year off-style |

---

## The Twelve Skills

| Skill | Role |
|-------|------|
| `jmsc-workflow` | Router — which skill next; key fork is 数理 vs 经验实证 |
| `jmsc-fit-positioning` | On-target? Regression + policy / survey-SEM → re-route |
| `jmsc-problem-formulation` | Formalize the decision problem |
| `jmsc-model-building` | Variables / constraints / objective / assumptions explicit |
| `jmsc-proofs` | Propositions / theorems with proofs; logical completeness |
| `jmsc-algorithm` | Algorithm design; complexity / convergence analysis |
| `jmsc-numerical-experiments` | Simulation validating theory + managerial insight |
| `jmsc-behavioral-om` | Behavioral OM: experiment design, manipulation checks, identification |
| `jmsc-managerial-insights` | Decision rules from the model, not policy slogans |
| `jmsc-notation-style` | Unified notation, explicit assumptions, proofs in appendix |
| `jmsc-submission` | Preflight: formula / theorem typesetting, online system |
| `jmsc-rebuttal` | R&R response letter |

---

## Quick Start

### Option A — Claude Code Plugin

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install journal-of-management-sciences-in-china-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
mkdir -p ~/.claude/skills && cp -R skills/jmsc-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/jmsc-* ~/.codex/skills/
```

---

> Editorial policy evolves. Treat these skills as opinionated heuristics, not official policy — always confirm against the journal's latest 投稿指南/来稿须知 at [jmsc.tju.edu.cn](https://jmsc.tju.edu.cn/).
