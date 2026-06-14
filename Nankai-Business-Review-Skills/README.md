# Nankai Business Review Skills

<p align="center">
  <img src="assets/cover.svg" alt="《南开管理评论》 journal cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Nankai%20Business%20Review-c0392b)](https://nbr.nankai.edu.cn/)
[![Index](https://img.shields.io/badge/index-CSSCI-1f6feb)](https://nbr.nankai.edu.cn/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **《南开管理评论》 (Nankai Business Review, NBR)** — the top Chinese business-school journal, sponsored by Nankai University (Business School) and supervised by the Ministry of Education (founded 1998 from the earlier 《国际经贸研究》; ISSN 1008-3448; CN 12-1288/F).

This repository is opinionated. It is **not** a generic management-writing toolbox, and it is **not** an econometric-identification stack. It is an **NBR-specific** stack built around the journal's defining bar: **theory contribution + China context + measurement rigor**, delivered through survey-SEM, experiments, or multi-case / grounded-theory methods.

Verified journal facts live in [`resources/journal-profile.md`](resources/journal-profile.md) with source links.

---

## Why a Separate Stack?

NBR imposes constraints that differ from economics / macro-policy journals (经济研究 / 管理世界 / 中国工业经济) and from math-modeling journals (管理科学学报):

| Constraint | Nankai Business Review | Implication |
|------------|------------------------|-------------|
| Discipline | Theory-building management (OB / strategy / HRM / marketing / governance) | Macro policy-evaluation framing is off-fit |
| Contribution | Concept / proposition / framework that advances a management theory | "Regression is significant" is not a contribution |
| Hypotheses | Each backed by a theoretical mechanism | "We expect a positive relationship" gets desk-rejected |
| Measurement | Reliability (α, CR) + validity (convergent/discriminant, AVE) + CMV test | Borrowed scales with no psychometrics fail review |
| Method | Survey-SEM / experiment / multi-case — serves the theory | Causal-identification cleanliness is not the bar |
| China context | Context must enter the theory | A China sample is not contextualization |
| Abstract | 100–300 chars, 3–8 keywords, bilingual | Lead with the proposition, not background |

---

## The Twelve Skills

| Skill | Role |
|-------|------|
| `nbr-workflow` | Router — which skill next; cross-refs sibling journal stacks |
| `nbr-fit-positioning` | On-target? Re-route math models / macro policy elsewhere |
| `nbr-theory-gap` | Articulate the theoretical gap and the contribution |
| `nbr-hypothesis-development` | Every hypothesis backed by a mechanism, not intuition |
| `nbr-measurement` | Reliability (α, CR), validity (AVE), common-method-bias tests |
| `nbr-survey-sem` | SEM / mediation / moderation / moderated mediation / HLM |
| `nbr-experiment` | Manipulation checks, randomization, effect sizes |
| `nbr-qualitative-case` | Multi-case comparison / grounded coding / saturation & trustworthiness |
| `nbr-china-context` | How the China context changes construct relationships |
| `nbr-discussion-contribution` | Discussion that loops back and advances a theory |
| `nbr-submission` | Preflight: format, abstract limits, online system |
| `nbr-rebuttal` | R&R response letter |

---

## Quick Start

### Option A — Claude Code Plugin

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install nankai-business-review-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
mkdir -p ~/.claude/skills && cp -R skills/nbr-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/nbr-* ~/.codex/skills/
```

---

> Editorial policy evolves. Treat these skills as opinionated heuristics, not official policy — always confirm against the journal's latest 来稿规范说明 at [nbr.nankai.edu.cn](https://nbr.nankai.edu.cn/).
