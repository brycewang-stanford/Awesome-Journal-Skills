# China Industrial Economics Skills

<p align="center">
  <img src="assets/cover.svg" alt="《中国工业经济》 journal cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-China%20Industrial%20Economics-c0392b)](https://ciejournal.ajcass.com/)
[![Index](https://img.shields.io/badge/index-CSSCI-1f6feb)](https://ciejournal.ajcass.com/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **《中国工业经济》 (China Industrial Economics)** — the flagship journal of the CASS Institute of Industrial Economics and a top CSSCI journal for industrial organization, firm behavior, innovation, regional and digital economy (monthly; ISSN 1006-480X; CN 11-3536/F).

This repository is opinionated. It is **not** a generic empirics toolbox. It is a **China-Industrial-Economics-specific** stack built around the journal's defining bar: **empirical engineering — clean China-policy quasi-experiments, an exhaustive robustness "arms race," mechanism + heterogeneity with economic interpretation, and ACTIONABLE industrial policy.** Its motto is 理论顶天，实践立地 ("theory reaching the sky, practice grounded in earth").

The journal is famous for publishing its own methodological-norm guides — most notably **Jiang (2022), CIE 2022:5, on mediation/moderation** — which is why this stack treats the three-step mediation method as suspect.

Verified journal facts live in [`resources/journal-profile.md`](resources/journal-profile.md) with source links.

---

## Why a Separate Stack?

《中国工业经济》 imposes constraints that differ from sibling economics journals (经济研究 / 管理世界 / 金融研究 / 世界经济):

| Constraint | China Industrial Economics | Implication |
|------------|----------------------------|-------------|
| Profile | Empirical engineering (实证工程化) | Pure-theory or single-table empirics off-fit |
| Identification | Multi-period DID / event study | TWFE on staggered timing without heterogeneity-robust estimators = desk reject |
| Mechanism | Split-channel / moderation | Three-step mediation is suspect (Jiang 2022) |
| Heterogeneity | Multi-dimensional + economic meaning | "East/central/west" alone is too thin |
| Robustness | The arms race — done in full | A thin robustness section gets returned |
| Tables | Economic-magnitude interpretation | Reporting only significance stars is not enough |
| Policy | Actionable: who, which node, what | Differs from 经济研究's significance-level implications |
| Abstract | 450–500 chars, 3–5 keywords | Lead with the contribution |
| Notes | Footnotes (页下注) + 实引 references | Endnotes / in-text-only citations off-style |
| Reproducibility | Data + code on acceptance | Have them ready before submitting |

---

## The Thirteen Skills

| Skill | Role |
|-------|------|
| `cie-workflow` | Router — which skill next; cross-refs sibling journal packages |
| `cie-fit-positioning` | Is this on-target? Re-route if theory-heavy / management / finance / trade |
| `cie-topic-selection` | Policy quasi-experiment / firm behavior / IO / digital economy + 3–5 contributions |
| `cie-literature-review` | Gap-driven 述评, not a citation pile |
| `cie-institutional-background` | Accurate policy detail, pilot lists, timing |
| `cie-did-identification` | Multi-period DID / event study; parallel trends + placebo + heterogeneity-robust estimators (mandatory) |
| `cie-mechanism` | Split-channel / moderation; cautious with three-step mediation |
| `cie-heterogeneity` | Multi-dimensional cuts with economic interpretation |
| `cie-robustness` | The signature robustness arms race |
| `cie-tables-figures` | Three-line tables + economic-magnitude reading after every key table |
| `cie-policy-implication` | Actionable: who, at which node, does what |
| `cie-submission` | Preflight: footnotes, 实引, online system, data/code, anonymity |
| `cie-rebuttal` | External-review / R&R response letter |

---

## Quick Start

### Option A — Claude Code Plugin

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install china-industrial-economics-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
mkdir -p ~/.claude/skills && cp -R skills/cie-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/cie-* ~/.codex/skills/
```

---

> Editorial policy evolves. Treat these skills as opinionated heuristics, not official policy — always confirm against the journal's latest 投稿（修改）指南 at [ciejournal.ajcass.com](https://ciejournal.ajcass.com/).
