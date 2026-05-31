# Economic-Research Skills

<p align="center">
  <img src="assets/cover.jpg" alt="《经济研究》 journal cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Economic%20Research-c0392b)](http://www.erj.cn/)
[![Index](https://img.shields.io/badge/index-CSSCI-1f6feb)](http://www.erj.cn/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **《经济研究》 (Economic Research Journal)** — the top economics journal in China, designated by the State Council Academic Degrees Committee.

This repository is opinionated. It is **not** a generic Chinese-economics writing toolbox. It is an **Economic-Research-specific** stack covering topic selection with theoretical grounding, bilingual literature review, modern quasi-experimental identification, mechanism / heterogeneity analysis, CSSCI house style, policy implications, and R&R rebuttals.

---

## Why a Separate Economic-Research Skill Stack?

《经济研究》 imposes constraints that differ materially from AER / AEJ / top finance journals:

| Constraint                | Economic Research                                          | Implication                                                |
|---------------------------|------------------------------------------------------------|------------------------------------------------------------|
| Discipline                | Economics (macro / institutional / econometric / industry) | Pure-management or pure-case papers are off-fit            |
| Topic                     | Theoretical contribution + China problem                   | "Policy evaluation only" reads as a working paper          |
| Contribution sentences    | 3–5 explicit "边际贡献" bullets in intro                    | Cannot be a single paragraph                               |
| Literature review         | Bilingual; **canonical theory citations required**         | Missing canonical theory refs is a desk-reject signal      |
| Identification            | Quasi-experimental + careful endogeneity discussion        | OLS + controls often desk-rejected                         |
| Mechanism                 | Near-mandatory                                             | Empirical papers without mechanism rarely accepted         |
| Heterogeneity             | Strongly preferred                                         | Often requested in R&R if missing                          |
| Policy implications       | Mandatory; framed as "significance" rather than "actions"  | Different from 《管理世界》 actionable-policy style         |
| Length                    | ~15–25k Chinese characters incl. exhibits                  | Substantially longer than AER; full structure expected     |
| Abstract                  | 200–400 Chinese characters                                 | "What we do + what we find" first, then significance       |

Generic "scientific writing" or "economics writing" skill packs do not address these constraints.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/economic-research-skills
/plugin install economic-research-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/economic-research-skills.git
cd economic-research-skills

mkdir -p ~/.claude/skills && cp -R skills/er-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/er-* ~/.codex/skills/
```

### First Prompt

```
Use er-workflow to tell me which skill I should use next for my Economic-Research manuscript.
```

---

## Default Workflow

```text
er-topic-selection
        ▼
er-literature-review
        ▼
er-identification
        ▼
er-mechanism
        ▼
er-heterogeneity
        ▼
er-tables-figures
        ▼
er-policy-implication
        ▼
er-abstract      (polish)
        ▼
er-style         (polish)
        ▼
er-submission
        ▼
er-rebuttal
```

`er-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill                     | Purpose                                                        |
|--------------------------|----------------------------------------------------------------|
| `er-workflow`             | Router — decides which sub-skill to invoke next                |
| `er-topic-selection`      | Theoretical-grounding fit + contribution-sentence template      |
| `er-literature-review`    | Bilingual structure + canonical-theory checklist               |
| `er-identification`       | Quasi-experimental design (DID / IV / RDD / DML)               |
| `er-mechanism`            | Mechanism-analysis paths and writing template                  |
| `er-heterogeneity`        | Heterogeneity cuts: five-dimension priority                    |
| `er-tables-figures`       | Three-line tables, variable-definition table, figure aesthetics |
| `er-policy-implication`   | Significance-level policy framing (not action-level)           |
| `er-abstract`             | 200–400 字摘要五句法 + 黑名单短语清除                          |
| `er-style`                | Language polish: empty-significance → concrete contribution     |
| `er-submission`           | Pre-submission checklist + manuscript template (format, word count, double-blind) |
| `er-rebuttal`             | R&R response-letter structure                                  |

### Resources

- [`skills/er-submission/templates/manuscript_template.md`](skills/er-submission/templates/manuscript_template.md) — Standard manuscript skeleton (abstract, variable table, references)
- [`skills/er-submission/templates/checklist.md`](skills/er-submission/templates/checklist.md) — 8-section pre-submission self-check
- [`resources/external_tools.md`](resources/external_tools.md) — Chinese economic-research data sources (CSMAR / Wind / CNRDS / CFPS / CHARLS) + Stata / Python / R packages

---

## Differences vs. Management-World Skills

| Dimension          | Economic Research               | Management World                   |
|--------------------|---------------------------------|------------------------------------|
| Discipline         | Economics (macro / institutional) | Management + applied economics  |
| Policy framing     | Significance (macro / qualitative) | Actionable (ministry-level)    |
| Case / qualitative | Rarely accepted                 | Accepted                           |
| Theory citations   | **Required**                    | Optional                           |
| Writing style      | Theoretical rigor               | Practical relevance                |

---

## What this repo does NOT do

- It will not write a submission-ready manuscript for you
- It does not simulate reviewer preferences
- It does not catalog 《经济研究》's historical rejection rate, impact factor, or other metadata
- It does not judge whether your "theoretical contribution" is genuinely original — that is the researcher's own call

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [AER-skills](https://github.com/brycewang-stanford/AER-skills) — American Economic Review
- [management-world-skills](https://github.com/brycewang-stanford/management-world-skills) — 《管理世界》

---

## License

MIT
