# Journal of Quantitative & Technological Economics Skills

<p align="center">
  <img src="assets/cover.svg" alt="《数量经济技术经济研究》 journal cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-JQTE-c0392b)](https://www.jqte.net/)
[![Index](https://img.shields.io/badge/index-CSSCI%20%7C%20EconLit-1f6feb)](https://www.jqte.net/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **《数量经济技术经济研究》 (The Journal of Quantitative & Technological Economics, JQTE)** — the Chinese Academy of Social Sciences journal for quantitative economics and technical economics (monthly since 1984; ISSN 1000-3894; CN 11-1087/F; CSSCI / 北大核心 / EconLit).

This repository is opinionated. It is **not** a generic econometrics toolbox. It is a **JQTE-specific** stack built around the journal's defining bar: **measurement transparency, method-application value, and reproducibility over a forced causal-policy narrative.** The contribution here is usually *how well you measure / forecast / decompose*, not *how clean your identification is*.

Verified journal facts live in [`resources/journal-profile.md`](resources/journal-profile.md) with source links.

---

## Why a Separate Stack?

JQTE rewards a different contribution shape than the clean-causal flagships (经济研究 / 中国经济学季刊 / 中国工业经济):

| Constraint | JQTE | Implication |
|------------|------|-------------|
| Contribution | Measurement / method-application / forecasting | "We find X causes Y" is not the only path — and a weak causal story hurts |
| Method node | The method section is the centerpiece | Construction must be transparent and reproducible |
| Robustness | Sensitivity to method/parameter choices | "Different DEA/SFA spec, same conclusion?" matters more than placebo tests |
| Forecasting | Out-of-sample evaluation | In-sample fit alone is a desk-reject risk |
| IO / CGE | Data source, calibration, closure, scenario | Black-box software runs without setup detail get rejected |
| Notes | Footnotes, renumbered per page (脚式编排) | Endnotes / in-text citations off-style |
| Policy section | ≥ 1000 characters (except pure-method papers) | Implications must land on planning / forecasting / industry decisions |

> Do **not** force a causal story onto a measurement paper. If identification is the real contribution and it is clean, route to 经济研究 / 中国经济学季刊 instead.

---

## The Thirteen Skills

| Skill | Role |
|-------|------|
| `jqte-workflow` | Router — which skill next; cross-journal routing |
| `jqte-fit-positioning` | Measurement / forecasting / method-application vs clean causal — frame accordingly |
| `jqte-topic-selection` | Pick a measurement / forecasting / evaluation question with real value |
| `jqte-literature-review` | Method lineage + Chinese-data application gap, not a citation pile |
| `jqte-measurement` | TFP / Malmquist / DEA / SFA / index construction — transparent + sensitivity |
| `jqte-econometric-methods` | Time series / cointegration / mixed-frequency / panel / macro-econometrics |
| `jqte-forecasting` | Out-of-sample evaluation (RMSE / directional accuracy) |
| `jqte-io-cge` | Input-output / CGE / structural decomposition (SDA) — reproducibility |
| `jqte-sensitivity` | Measurement & parameter sensitivity, robustness |
| `jqte-tables-figures` | Quantitative interpretation, not just significance stars |
| `jqte-implications` | Planning / forecasting / industrial / technology decisions |
| `jqte-submission` | Preflight: footnotes, policy-length, online system |
| `jqte-rebuttal` | R&R response letter |

---

## Quick Start

### Option A — Claude Code Plugin

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install journal-of-quantitative-and-technological-economics-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
mkdir -p ~/.claude/skills && cp -R skills/jqte-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/jqte-* ~/.codex/skills/
```

---

> Editorial policy evolves. Treat these skills as opinionated heuristics, not official policy — always confirm against the journal's latest 投稿须知 at [jqte.net](https://www.jqte.net/).
