# China Economic Quarterly Skills

<p align="center">
  <img src="assets/cover.svg" alt="《经济学(季刊)》 journal cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-China%20Economic%20Quarterly%20(CEQ)-c0392b)](https://www.nsd.pku.edu.cn/cbw/jjxjk/index.htm)
[![Index](https://img.shields.io/badge/index-CSSCI-1f6feb)](https://www.nsd.pku.edu.cn/cbw/jjxjk/index.htm)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **《经济学(季刊)》 (China Economic Quarterly, CEQ)** — the Peking University / CCER (now National School of Development) journal that sits **closest to international top-field economics standards** among Chinese-language outlets (founded 2001; six issues per year since 2021; ISSN 2095-1086; CN 11-6010/F).

This repository is opinionated. It is **not** a generic econometrics toolbox. It is a **CEQ-specific** stack built around the journal's defining bar: **credible identification + international legibility over everything else.** CEQ is the strictest Chinese economics journal on methodology, and the least tolerant of policy sloganeering.

Verified journal facts live in [`resources/journal-profile.md`](resources/journal-profile.md) with source links.

---

## Why a Separate Stack?

CEQ imposes constraints that differ from sibling Chinese econ journals (经济研究 / 中国工业经济 / 金融研究 / 世界经济):

| Constraint | China Economic Quarterly | Implication |
|------------|--------------------------|-------------|
| Paradigm | International top-field; reviewers overseas-trained | "国内实证套路" framing reads as dated |
| Identification | Structural OR clean quasi-experiment | OLS + controls as causal gets desk-rejected |
| Modern DID | Staggered/heterogeneity batteries mandatory | Bare TWFE on staggered timing is a reject |
| Inference | Clustering rationale, weak-IV-robust, multiple testing | Default robust SEs are not enough |
| Contribution | Benchmarked to specific field papers | "丰富了相关研究" is not a contribution |
| Exhibits | Figures over tables (event-study / bin-scatter) | Table-only results under-sell the design |
| Abstract | English abstract ≤ 100 words, must read to field peers | Many readers only read the English abstract + figures |
| Citations | In-text author-date (页内夹注), 3 JEL codes | Footnote-style citation is off-format |

---

## The Twelve Skills

| Skill | Role |
|-------|------|
| `ceq-workflow` | Router — which skill next |
| `ceq-fit-positioning` | Is this on-target for CEQ? Re-route if not |
| `ceq-topic-selection` | Clean causal / model-able / internationally-legible topics |
| `ceq-literature-review` | Precise contribution vs. specific field papers; 中英文献 |
| `ceq-identification` | Structural OR quasi-experiment; assumptions made explicit |
| `ceq-modern-did` | Staggered / heterogeneous treatment-effect compliance |
| `ceq-inference` | Clustering, weak-IV-robust, multiple testing, standard errors |
| `ceq-mechanism` | Channel / mechanism evidence |
| `ceq-figures` | Event-study / bin-scatter / model-fit — figures over tables |
| `ceq-abstract-english` | English abstract + field-benchmarked contribution statement |
| `ceq-submission` | Preflight: system, format, reproducibility, anonymity |
| `ceq-rebuttal` | R&R response letter |

---

## Quick Start

### Option A — Claude Code Plugin

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install china-economic-quarterly-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
mkdir -p ~/.claude/skills && cp -R skills/ceq-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/ceq-* ~/.codex/skills/
```

---

> Editorial policy and publication frequency evolve (the title says "季刊" but CEQ has run six issues per year since 2021). Treat these skills as opinionated heuristics, not official policy — always confirm against the journal's latest 投稿须知 at [nsd.pku.edu.cn/cbw/jjxjk](https://www.nsd.pku.edu.cn/cbw/jjxjk/index.htm) and the facts in [`resources/journal-profile.md`](resources/journal-profile.md).
