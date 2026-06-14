# Journal of Financial Research Skills

<p align="center">
  <img src="assets/cover.svg" alt="《金融研究》 journal cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Journal%20of%20Financial%20Research-c0392b)](http://www.jryj.org.cn/)
[![Index](https://img.shields.io/badge/index-CSSCI-1f6feb)](http://www.jryj.org.cn/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **《金融研究》 (Journal of Financial Research, JFR)** — sponsored by the China Society for Finance and Banking, edited and published by the People's Bank of China research-institute editorial office, and the top finance journal in China (monthly; ISSN 1002-7246; CN 11-1268/F).

This repository is opinionated. It is **not** a generic finance-writing toolbox. It is a **Journal-of-Financial-Research-specific** stack built around the journal's defining bar: **rigorous identification PLUS concrete relevance to China's financial system**, and around its two parallel lines — **macro-finance** versus **micro corporate-finance**.

Verified journal facts live in [`resources/journal-profile.md`](resources/journal-profile.md) with source links.

---

## Why a Separate Stack?

《金融研究》 sits between the clean-causal economics journals and the management journals, with constraints that differ from both:

| Constraint | Journal of Financial Research | Implication |
|------------|-------------------------------|-------------|
| Discipline | Finance flagship, two lines | Macro-finance and micro corporate-finance need different framings |
| Identification | Policy shocks / high-frequency surprises | OLS-on-correlations gets desk-rejected |
| Mechanism | Financial channels | "Promotes / inhibits" without a channel is not enough |
| Institutional detail | China's financial system, stated accurately | Wrong regulatory caliber or market segmentation kills the paper |
| Policy implication | Monetary authority / regulators / institutions | More operational than 经济研究 |
| Abstract | ~200 characters, 3–5 keywords, 3 JEL codes | Lead with finding and channel |
| Notes | Numbered notes (①②③), continuous numbering | In-text-only citation off-style |

---

## The Twelve Skills

| Skill | Role |
|-------|------|
| `jfr-workflow` | Router — which skill next; cross-refs sibling journal packs |
| `jfr-fit-positioning` | Macro-finance vs micro corporate-finance; re-route if industrial / accounting |
| `jfr-topic-selection` | Pin down the finance question and contribution |
| `jfr-literature-review` | Enter the finance lineage, Chinese + English |
| `jfr-institutional-background` | China's financial-system detail, stated accurately |
| `jfr-identification` | Policy shocks (MPA / 资管新规 / LPR / 注册制), high-frequency surprises, DID, IV |
| `jfr-mechanism` | Financial channels: credit / risk-taking / balance-sheet / information |
| `jfr-heterogeneity` | Cut by ownership, bank type, region, market segment |
| `jfr-tables-figures` | Main tables / figures to journal house style |
| `jfr-policy-implication` | Addressed to monetary authority / regulators / institutions |
| `jfr-submission` | Preflight: notes, abstract/keywords/JEL, online system, anonymity |
| `jfr-rebuttal` | R&R response letter |

---

## Quick Start

### Option A — Claude Code Plugin

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install journal-of-financial-research-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
mkdir -p ~/.claude/skills && cp -R skills/jfr-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/jfr-* ~/.codex/skills/
```

---

> Editorial policy evolves. Treat these skills as opinionated heuristics, not official policy — always confirm against the journal's latest 来稿须知 at [www.jryj.org.cn](http://www.jryj.org.cn/).
