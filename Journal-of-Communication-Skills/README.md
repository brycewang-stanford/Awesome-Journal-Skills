# Journal of Communication Skills

<p align="center">
  <img src="assets/cover.svg" alt="Journal of Communication cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-JoC-c0532b)](https://academic.oup.com/joc)
[![Field](https://img.shields.io/badge/field-Communication-1f6feb)](https://www.icahdq.org/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at the **Journal of Communication (JoC)** — the
**flagship journal of the International Communication Association (ICA)**, published by **Oxford
University Press**. JoC publishes the best scholarship across the **whole field of communication**:
communication theory and methodology, media effects, political communication, health communication,
computational/text-as-data communication, and interpersonal/organizational communication —
quantitative, computational, qualitative, and critical/interpretive alike.

This repository is opinionated. It is **not** a generic social-science writing toolbox and it is
**not** a psychology or political-science pack repurposed for communication. It is a **JoC-specific**
stack: a question of **general significance to communication research**, an argument that speaks
**past its own subfield and platform**, a design defended on its own methodological terms,
**double-anonymous** preparation, and a **Data Availability Statement** with reproducibility and Open
Science Badge materials prepared as you write.

---

## What Is JoC, and Why a Dedicated Stack?

JoC's constraints differ from a field journal or a methods journal:

| Constraint            | JoC                                                                            | Implication                                                       |
|-----------------------|--------------------------------------------------------------------------------|-------------------------------------------------------------------|
| Scope                 | **Whole field** of communication research                                      | The paper must matter beyond one subfield or platform            |
| Premium on            | **General significance** + a clear theoretical contribution                    | A narrow, platform-only result is off-fit                        |
| Methods               | Quantitative, computational, qualitative, critical — judged on own terms       | Do not force one template onto every paper                       |
| Publisher / owner     | **Oxford University Press** / **ICA**                                           | Submitted via **Manuscript Central** (ScholarOne), not Editorial Manager |
| Review model          | **Double-anonymous**                                                            | Anonymize the main document *and* supplemental materials         |
| Fee                   | **No submission fee** stated; hybrid open-access APC after acceptance           | Do not budget a submission fee                                   |
| Length                | Main document **≤ 35 pages** (incl. refs/tables/figures); **abstract ≤ 150**    | Pages, not words, are the budget; everything counts              |
| Style                 | **APA 7th edition**; Word (.docx), 12-pt Times New Roman, double-spaced         | Not Chicago/LaTeX-generic; self-citations in the third person    |
| Transparency          | **Data Availability Statement required**; Open Science Badges available         | Build the statement and materials as you go                      |
| Distinctive format    | **JoC Forum** (3,000–6,000 words) alongside articles and special issues         | Choose the right format up front                                 |

Volatile specifics (editors and term, exact caps, fee/APC, policy wording) change — items not directly
confirmed are marked **待核实** in [`resources/official-source-map.md`](resources/official-source-map.md).
**Verify on the official journal page.**

### Submission formats

- **Original research articles** — the field's main research format; main document **≤ 35 pages**
  including abstract, text, references, tables, figures, and endnotes.
- **JoC Forum** — shorter, argument-driven contributions of **3,000–6,000 words** (see 待核实 on remit).
- **Special issues** — occasional themed collections via calls for papers.
- **Open Science Badges** — earn badges for **open data**, **open materials**, and **preregistration**.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/joc-skills
/plugin install joc-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/joc-skills.git
cd joc-skills

mkdir -p ~/.claude/skills && cp -R skills/joc-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/joc-* ~/.codex/skills/
```

### First Prompt

```
Use joc-workflow to tell me which skill I should use next for my Journal of Communication manuscript.
```

---

## Default Workflow

```text
joc-topic-selection
        ▼
joc-literature-positioning
        ▼
joc-theory-building
        ▼
joc-research-design
        ▼
joc-data-analysis
        ▼
joc-tables-figures
        ▼
joc-writing-style          (polish)
        ▼
joc-open-science-and-transparency
        ▼
joc-review-process
        ▼
joc-submission
        ▼
joc-rebuttal
```

`joc-workflow` is the router — it tells you which skill to use next based on where you are. If your
design is **prospective**, route to `joc-open-science-and-transparency` early to **preregister** and
plan your Open Science Badge materials; if your contribution is short and argument-driven, consider the
**JoC Forum** format.

---

## Skills

| Skill                                | Purpose                                                                       |
|--------------------------------------|-------------------------------------------------------------------------------|
| `joc-workflow`                       | Router — decides which sub-skill to invoke next                               |
| `joc-topic-selection`                | General-significance fit across communication; pick article vs. Forum         |
| `joc-literature-positioning`         | Speak past your subfield/platform; engage the literatures JoC readers expect  |
| `joc-theory-building`                | Build the argument into a portable communication-theory contribution          |
| `joc-research-design`                | Defend the design — experiments, surveys, content analysis, computational, qualitative |
| `joc-data-analysis`                  | Analysis norms, uncertainty, robustness, reliability, triangulation           |
| `joc-tables-figures`                 | Accessible, self-contained exhibits in APA style within the page budget       |
| `joc-writing-style`                  | APA 7th edition; reach the whole field within 35 pages / 150-word abstract    |
| `joc-open-science-and-transparency`  | Data Availability Statement; Open Science Badges; preregistration; exemptions |
| `joc-review-process`                 | Double-anonymous review, screening, format choice, decision categories        |
| `joc-submission`                     | Manuscript Central preflight (anonymization, page count, abstract, Word/APA)  |
| `joc-rebuttal`                       | R&R response-letter strategy for multiple reviewers + editor                  |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — communication data sources (ANES / CES / Pew / HINTS / GDELT / Media Cloud) + R / SPSS-PROCESS / Mplus / Python and qualitative/CAQDAS tooling
- [`resources/official-source-map.md`](resources/official-source-map.md) — official OUP / ICA URLs behind every fact, with 待核实 markers on unverified items

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate any specific editor's or reviewer's taste
- It does not assert volatile metadata (current editors and term, exact caps, fee/APC, policy wording) — verify on the official page; unverified items are marked 待核实
- It does not decide whether your question is of general significance to communication — that is the researcher's call

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Journal of Communication (Oxford Academic)](https://academic.oup.com/joc) — publisher home
- [International Communication Association](https://www.icahdq.org/) — owning society

---

## License

MIT
