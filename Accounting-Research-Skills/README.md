# Accounting Research Skills

<p align="center">
  <img src="assets/cover.svg" alt="《会计研究》 journal cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Accounting%20Research-c0392b)](https://www.asc.net.cn/AccountingResearch/MagazineProfile.aspx?type=profile)
[![Index](https://img.shields.io/badge/index-CSSCI%20%7C%20NSFC%20A-1f6feb)](https://www.asc.net.cn/AccountingResearch/MagazineProfile.aspx?type=profile)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **《会计研究》 (Accounting Research)** — the flagship journal of the Accounting Society of China (中国会计学会), the only accounting title among CSSCI sources, and an NSFC management-science Class-A journal (monthly; founded 1980; ISSN 1003-2886; CN 11-1078/F).

This repository is opinionated. It is **not** a generic empirical-finance toolbox. It is an **Accounting-Research-specific** stack built around the journal's defining bar: **archival capital-market empirics with accurate institutional / standard-setting detail and an information mechanism — distinguished from generic corporate finance.**

Verified journal facts live in [`resources/journal-profile.md`](resources/journal-profile.md) with source links.

---

## Why a Separate Stack?

《会计研究》 imposes constraints that differ from finance / management / economics journals (金融研究 / 南开管理评论 / 经济研究):

| Constraint | Accounting Research | Implication |
|------------|---------------------|-------------|
| Landing point | Accounting info / disclosure / audit / standards | A finance-mechanism story is off-fit — re-route |
| Institutional detail | Standard clauses + effective dates must be exact | Vague "policy background" reads as careless |
| Measurement | Accounting measures built transparently | Off-the-shelf proxy with no construction = reject risk |
| Identification | Exogenous standard / regulatory change preferred | Plain OLS rarely survives review |
| Mechanism | Information channel (asymmetry / disclosure / EM) | A pure pricing channel belongs in a finance journal |
| Contribution | Theory **and** standard-setter / regulator practice | "Enriches the literature" is not enough |
| Notes | Footnotes (当页下注), per-page numbering ①②… | Endnotes / in-text-only citations off-style |
| References | 著者—出版年制; Chinese then foreign | Numbered [1][2] style off-style |

---

## The Thirteen Skills

| Skill | Role |
|-------|------|
| `acr-workflow` | Router — which skill next |
| `acr-fit-positioning` | Accounting issue or finance mechanism? Re-route if finance |
| `acr-topic-selection` | Frame an accounting contribution, not a generic effect |
| `acr-literature-review` | Enter the accounting lineage (earnings quality / audit / disclosure) |
| `acr-institutional-standards` | Accurate standards / regulation: clauses, effective dates |
| `acr-measurement` | Discretionary accruals (modified Jones), conservatism (C-Score), disclosure indices |
| `acr-identification` | Exogenous standard / regulatory change (event study / DID) / PSM / Heckman |
| `acr-mechanism` | Information mechanism: cut asymmetry, raise disclosure, constrain EM |
| `acr-robustness` | Replace measures, control governance / institutional vars, placebo |
| `acr-tables-figures` | Economic-magnitude interpretation |
| `acr-implications` | Implications for standards / regulators / practice |
| `acr-submission` | Preflight: footnotes, reference style, online system, anonymity |
| `acr-rebuttal` | R&R response letter |

---

## Quick Start

### Option A — Claude Code Plugin

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install accounting-research-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
mkdir -p ~/.claude/skills && cp -R skills/acr-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/acr-* ~/.codex/skills/
```

---

> Editorial policy evolves. Treat these skills as opinionated heuristics, not official policy — always confirm against the journal's latest 投稿指南 at [asc.net.cn](https://www.asc.net.cn/AccountingResearch/MagazineProfile.aspx?type=tgzn).
