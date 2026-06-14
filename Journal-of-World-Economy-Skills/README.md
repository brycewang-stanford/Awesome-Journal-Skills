# Journal of World Economy Skills

<p align="center">
  <img src="assets/cover.svg" alt="《世界经济》 journal cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-The%20Journal%20of%20World%20Economy-c0392b)](https://www.jweonline.cn/)
[![Index](https://img.shields.io/badge/index-CSSCI-1f6feb)](https://www.jweonline.cn/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **《世界经济》 (The Journal of World Economy)** — the flagship international / open-economy journal of the China Academy of Social Sciences, jointly run by the Chinese Society of World Economy and the CASS Institute of World Economics and Politics (IWEP) (monthly; ISSN 1002-9621; CN 11-1138/F).

This repository is opinionated. It is **not** a generic empirical-economics writing toolbox. It is a **Journal-of-World-Economy-specific** stack built around the journal's defining bar: **the international / open-economy dimension and explicit transmission channels — not domestic policy evaluation dressed up with one "global" sentence.**

Verified journal facts live in [`resources/journal-profile.md`](resources/journal-profile.md) with source links.

---

## Why a Separate Stack?

《世界经济》 imposes constraints that differ from the domestic empirical journals (经济研究 / 中国工业经济 / 金融研究 / 经济学季刊):

| Constraint | Journal of World Economy | Implication |
|------------|--------------------------|-------------|
| Lens | International / open-economy is the identity | A closed-economy paper is off-fit, however clean |
| Question | Causal questions in an open economy | "Domestic policy evaluation" reads off-target |
| Mechanism | Trade / investment / financial / expectation channel | "It promoted exports" without a channel is thin |
| Literature | Trade & international-finance classics + frontier | Citing only domestic empirics fails the dialogue |
| Data | Customs micro / cross-country panel / GVC / I-O | Generic provincial panels rarely fit |
| Identification | External shocks + shift-share / gravity | Modern shift-share inference critiques must be met |
| Policy | Opening-up policy (trade, FX, capital account) | Domestic-operational suggestions miss the level |
| Notes | Footnotes (页下注), references at the end | Endnotes / in-text-only citations off-style |
| Abstract | 内容提要 ≤ 300 chars, 3–5 keywords | Lead with the open-economy finding |

---

## The Twelve Skills

| Skill | Role |
|-------|------|
| `jwe-workflow` | Router — which skill next |
| `jwe-fit-positioning` | Does the open-economy dimension hold up? Re-route if not |
| `jwe-topic-international` | Causal question seen through an international lens |
| `jwe-literature-review` | Dialogue with trade / international-finance classics & frontier |
| `jwe-data-sources` | Customs micro, cross-country panels, GVC / input-output (KWW, MRIO) |
| `jwe-identification` | External shocks + shift-share / gravity (with inference critiques) |
| `jwe-transmission-channel` | Trade / investment / financial / expectation channels |
| `jwe-heterogeneity` | Slice by exposure / firm / country / margin |
| `jwe-tables-figures` | Main tables and figures, house style |
| `jwe-policy-implication` | Opening-up policy level, not operational to-dos |
| `jwe-submission` | Preflight: footnotes, www.jweonline.cn, anonymity |
| `jwe-rebuttal` | R&R response letter |

---

## Quick Start

### Option A — Claude Code Plugin

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install journal-of-world-economy-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
mkdir -p ~/.claude/skills && cp -R skills/jwe-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/jwe-* ~/.codex/skills/
```

---

> Editorial policy evolves. Treat these skills as opinionated heuristics, not official policy — always confirm against the journal's latest 投稿须知 at the official editorial site [www.jweonline.cn](https://www.jweonline.cn/). The submission system has migrated before and third-party "agent submission" sites exist; use only the official entry.
