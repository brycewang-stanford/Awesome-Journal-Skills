# Chinese-Public-Administration Skills

<p align="center">
  <img src="assets/cover.svg" alt="《中国行政管理》 journal cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Chinese%20Public%20Administration-c0392b)](https://www.cpaj.com.cn/)
[![Index](https://img.shields.io/badge/index-CSSCI-1f6feb)](https://www.cpaj.com.cn/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **《中国行政管理》 (Chinese Public Administration)** — a leading CSSCI journal sponsored by the Chinese Public Administration Society and one of the most authoritative outlets in China's public administration and governance field.

This repository is opinionated. It is **not** a generic Chinese social-science writing toolbox. It is a **Chinese-Public-Administration-specific** stack covering governance-theory topic selection, bilingual literature review, mixed quantitative-qualitative research design and causal inference, governance / policy-process mechanism analysis, cross-context heterogeneity, CSSCI house style, grounded-yet-actionable policy implications, and review-response rebuttals.

---

## Why a Separate Chinese-Public-Administration Skill Stack?

《中国行政管理》 imposes constraints that differ materially from economics journals (such as 《经济研究》) and from international PA journals (JPART / PAR / Governance):

| Constraint                | Chinese Public Administration                                       | Implication                                                  |
|---------------------------|--------------------------------------------------------------------|--------------------------------------------------------------|
| Discipline                | Public administration / governance / public policy                 | Pure-economics or pure-management papers are off-fit         |
| Theory anchor             | A PA theory frame is required (governance, NPM / NPS, policy-process) | "Data + regression only" reads as off-discipline           |
| Method pluralism          | Quantitative **and** qualitative both first-class                  | Normative, case, comparative, and empirical designs all OK   |
| Research-question fit     | Method must match the question, not the fashion                    | A quasi-experiment grafted onto a governance question fails  |
| China governance reality  | Topic must be anchored in real Chinese governance practice         | Abstract "global" framing without China context reads thin   |
| Mechanism                 | Governance / policy-process mechanism expected                     | "Effect without process" is weak for a PA reviewer           |
| Policy implications       | More actionable than economics journals, but must rest on analysis | The "强化/完善/健全/推进" four-verb filler is a reject signal |
| Length & exhibits         | Full-structure Chinese article; figures / tables as needed         | Working-paper-style fragments are off-fit                    |
| Abstract                  | Concise Chinese abstract; question → method → finding → significance | Empty-significance opening reads as filler                   |

Generic "social-science writing" or "economics writing" skill packs do not address these constraints.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/chinese-public-administration-skills
/plugin install chinese-public-administration-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/chinese-public-administration-skills.git
cd chinese-public-administration-skills

mkdir -p ~/.claude/skills && cp -R skills/cpa-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/cpa-* ~/.codex/skills/
```

### First Prompt

```
Use cpa-workflow to tell me which skill I should use next for my Chinese-Public-Administration manuscript.
```

---

## Default Workflow

```text
cpa-topic-selection
        ▼
cpa-literature-review
        ▼
cpa-identification     (research design: quant / qual / normative)
        ▼
cpa-mechanism
        ▼
cpa-heterogeneity
        ▼
cpa-tables-figures
        ▼
cpa-policy-implication
        ▼
cpa-abstract      (polish)
        ▼
cpa-style         (polish)
        ▼
cpa-submission
        ▼
cpa-rebuttal
```

`cpa-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill                     | Purpose                                                          |
|---------------------------|------------------------------------------------------------------|
| `cpa-workflow`            | Router — decides which sub-skill to invoke next                  |
| `cpa-topic-selection`     | Governance-theory fit + research-question + contribution framing |
| `cpa-literature-review`   | Bilingual PA-theory + China-governance literature structure      |
| `cpa-identification`      | Research design: quant (survey / admin data / DID-IV-RDD) + qual (case / process-tracing / grounded theory) + normative |
| `cpa-mechanism`           | Governance / policy-process mechanism (implementation, attention, central-local, incentives) |
| `cpa-heterogeneity`       | Cross-region / level / governance-context conditionality         |
| `cpa-tables-figures`      | Three-line tables, coding tables, process diagrams, exhibits     |
| `cpa-policy-implication`  | Actionable-but-grounded implications for government practice      |
| `cpa-abstract`            | Concise Chinese / English abstract + blacklist-phrase removal     |
| `cpa-style`               | Language polish: four-verb filler → grounded analytical claims    |
| `cpa-submission`          | Pre-submission checklist + manuscript template (format, anonymity)|
| `cpa-rebuttal`            | Review-response letter structure                                  |

### Resources

- [`skills/cpa-submission/templates/manuscript_template.md`](skills/cpa-submission/templates/manuscript_template.md) — Standard PA manuscript skeleton (abstract, theory frame, design, coding / variable table, references)
- [`skills/cpa-submission/templates/checklist.md`](skills/cpa-submission/templates/checklist.md) — 8-section pre-submission self-check
- [`resources/external_tools.md`](resources/external_tools.md) — Chinese public-administration data sources (CGSS / CFPS / government open data / policy-document corpora) + Stata / Python / R / NVivo packages

---

## Differences vs. Economic-Research Skills

| Dimension          | Chinese Public Administration         | Economic Research                  |
|--------------------|---------------------------------------|------------------------------------|
| Discipline         | Public administration / governance    | Economics (macro / institutional)  |
| Method             | Mixed quant + qual, normative welcome | Quantitative causal inference      |
| Theory anchor      | Governance / NPM-NPS / policy process | Economic theory                    |
| Policy framing     | Actionable for government practice, grounded | Significance / institutional |
| Case / qualitative | First-class                           | Rarely accepted                    |

---

## What this repo does NOT do

- It will not write a submission-ready manuscript for you
- It does not simulate reviewer preferences
- It does not catalog 《中国行政管理》's historical rejection rate, impact factor, or other metadata
- It does not judge whether your "theoretical contribution" is genuinely original — that is the researcher's own call
- It does not assert volatile specifics (current editorial board, exact publication fees, word limits) — defer to the journal's official "投稿须知"

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Economic-Research-Journal-Skills](https://github.com/brycewang-stanford/economic-research-skills) — 《经济研究》
- [management-world-skills](https://github.com/brycewang-stanford/management-world-skills) — 《管理世界》

---

## License

MIT
