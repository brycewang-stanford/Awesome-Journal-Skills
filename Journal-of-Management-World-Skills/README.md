# Management-World Skills

<p align="center">
  <img src="assets/cover.jpg" alt="《管理世界》 journal cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Management%20World-c0392b)](http://www.mwm.net.cn/)
[![Index](https://img.shields.io/badge/index-CSSCI-1f6feb)](http://www.mwm.net.cn/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **《管理世界》 (Management World)** — the top management and applied-economics journal in China.

This repository is opinionated. It is **not** a generic Chinese-economics writing toolbox. It is a **Management-World-specific** stack covering China-context topic selection, institutional-background framing, quasi-experimental identification suited to Chinese policy shocks, mechanism / heterogeneity analysis, CSSCI house style, policy implications, and R&R rebuttals.

---

## Why a Separate Management-World Skill Stack?

《管理世界》 imposes constraints that differ materially from AER / AEJ / top finance journals:

| Constraint                   | Management World                                       | Implication                                                  |
|------------------------------|--------------------------------------------------------|--------------------------------------------------------------|
| Topic must connect to China  | Required — Chinese institutional setting expected      | Pure methodological contributions rarely accepted             |
| Contribution sentence        | 4–5 explicit "边际贡献" bullets                         | Cannot rely on AER-style "problem → answer" narrative         |
| Literature review            | Stand-alone section, **Chinese + English** references | Missing canonical Chinese refs is a desk-reject signal        |
| Identification               | Prefers quasi-experimental (DID / IV / RDD / DML)      | Pure OLS + endogeneity discussion typically insufficient      |
| Institutional background     | Usually a dedicated section on policy timeline         | International-audience framing alone reads as "incomplete"   |
| Mechanism / Heterogeneity    | Near-mandatory for empirical papers                    | Empirical papers without mechanism tests rarely accepted     |
| Policy implications          | Mandatory closing section, actionable                  | Pure-academic contributions need explicit policy hooks       |
| Length                       | ~15–25k Chinese characters incl. exhibits              | Substantially longer than AER; full structure expected       |
| Abstract                     | 300–500 Chinese characters                             | "What we do + what we find" first, then significance         |

Generic "scientific writing" or "economics writing" skill packs do not address these constraints.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/management-world-skills
/plugin install management-world-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/management-world-skills.git
cd management-world-skills

mkdir -p ~/.claude/skills && cp -R skills/mw-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/mw-* ~/.codex/skills/
```

### First Prompt

```
Use mw-workflow to tell me which skill I should use next for my Management-World manuscript.
```

---

## Default Workflow

```text
mw-topic-selection
        ▼
mw-literature-review
        ▼
mw-institutional-background
        ▼
mw-identification
        ▼
mw-mechanism-heterogeneity
        ▼
mw-tables-figures
        ▼
mw-policy-implication
        ▼
mw-submission
        ▼
mw-rebuttal
```

`mw-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill                            | Purpose                                                       |
|---------------------------------|---------------------------------------------------------------|
| `mw-workflow`                    | Router — decides which sub-skill to invoke next               |
| `mw-topic-selection`             | China-context topic fit + contribution-sentence template       |
| `mw-literature-review`           | Bilingual literature-review structure                          |
| `mw-identification`              | Quasi-experimental design (DID / IV / RDD / DML)               |
| `mw-institutional-background`    | Policy / institutional-timeline section                        |
| `mw-mechanism-heterogeneity`     | Mechanism tests + heterogeneity cuts                           |
| `mw-tables-figures`              | Three-line tables, booktabs, footnote norms, figure aesthetics |
| `mw-policy-implication`          | Layered policy implications (short / mid / long term)          |
| `mw-submission`                  | Pre-submission checklist (format, word count, double-blind)    |
| `mw-rebuttal`                    | R&R response-letter structure                                  |

---

## What this repo does NOT do

- It will not write a submission-ready manuscript for you
- It does not simulate reviewer preferences (which are highly heterogeneous)
- It does not catalog 《管理世界》's rejection rate, impact factor, or other metadata
- It does not judge whether your China-context framing is "genuine" — that is the researcher's own call

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [AER-skills](https://github.com/brycewang-stanford/AER-skills) — American Economic Review
- [economic-research-skills](https://github.com/brycewang-stanford/economic-research-skills) — 《经济研究》

---

## License

MIT
