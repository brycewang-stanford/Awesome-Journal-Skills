# Social Sciences in China Skills

<p align="center">
  <img src="assets/cover.svg" alt="《中国社会科学》 journal cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Social%20Sciences%20in%20China-c0392b)](https://sscp.cssn.cn/)
[![Index](https://img.shields.io/badge/index-CSSCI-1f6feb)](https://sscp.cssn.cn/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **《中国社会科学》 (Social Sciences in China)** — the flagship journal of the Chinese Academy of Social Sciences and the most prestigious cross-disciplinary social-science journal in China (monthly; ISSN 1002-4921; CN 11-1211/C).

This repository is opinionated. It is **not** a generic social-science writing toolbox. It is a **Social-Sciences-in-China-specific** stack built around the journal's defining bar: **思想分量与原创理论贡献 over methodological sophistication.**

Verified journal facts live in [`resources/journal-profile.md`](resources/journal-profile.md) with source links.

---

## Why a Separate Stack?

《中国社会科学》 imposes constraints that differ from disciplinary journals (经济研究 / 管理世界 / 社会学研究):

| Constraint | Social Sciences in China | Implication |
|------------|--------------------------|-------------|
| Discipline | Cross-disciplinary flagship | Niche single-discipline empirical notes are off-fit |
| Problem level | 重大理论与现实问题 (制度 / 文明 / 治理) | Policy-evaluation framing reads as a working paper |
| Contribution | Original concept / proposition / framework | "We find X affects Y" is not enough |
| Knowledge system | 中国自主知识体系; theory dialogue | Verifying imported theory ≠ contribution |
| Method | Pluralist; method serves the thesis | Technique cannot replace theoretical argument |
| Abstract | 200–300 characters, 3–5 keywords | Lead with the proposition, not background |
| Notes | Footnotes (页下注) | Endnotes / in-text citations off-style |

---

## The Eleven Skills

| Skill | Role |
|-------|------|
| `ssc-workflow` | Router — which skill next |
| `ssc-fit-positioning` | Is this on-target? Re-route if not |
| `ssc-topic-problematic` | Elevate to a 重大问题 / problematic |
| `ssc-theory-contribution` | Original concept / proposition / framework; 自主知识体系 |
| `ssc-literature-dialogue` | Enter the theory lineage, not a citation pile |
| `ssc-argumentation` | Concept rigor + argument chain |
| `ssc-evidence` | Quantitative / qualitative / historical — method serves the thesis |
| `ssc-style` | Scholarly register; kill policy-report tone |
| `ssc-abstract-keywords` | 200–300-char abstract + 3–5 keywords |
| `ssc-submission` | Preflight: footnotes, online system, anonymity |
| `ssc-rebuttal` | External-review response letter |

---

## Quick Start

### Option A — Claude Code Plugin

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install social-sciences-in-china-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
mkdir -p ~/.claude/skills && cp -R skills/ssc-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/ssc-* ~/.codex/skills/
```

---

> Editorial policy evolves. Treat these skills as opinionated heuristics, not official policy — always confirm against the journal's latest 投稿须知 at [sscp.cssn.cn](https://sscp.cssn.cn/).
