# Sociological Methods & Research Skills

<p align="center">
  <img src="assets/cover.svg" alt="Sociological Methods & Research cover" width="200">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-SMR-2a2a2a)](https://journals.sagepub.com/home/smr)
[![Field](https://img.shields.io/badge/field-Quantitative%20Methodology-1f6feb)](https://journals.sagepub.com/author-instructions/smr)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **Sociological Methods & Research (SMR)** — the
**SAGE** flagship for **quantitative and statistical methodology** in sociology and the social
sciences. SMR publishes papers that **develop, evaluate, or critically assess methods**: causal
inference, measurement and latent-variable models, structural equation models, multilevel and
longitudinal data, social network analysis, missing data, simulation, sequence analysis, and
(increasingly) computational social science and text-as-data. A competent application of an existing
method with **no methodological contribution** is out of scope.

This repository is opinionated. It is **not** a generic social-science writing toolbox, and it is
**not** an applied empirical pack repurposed for methods. It is an **SMR-specific** stack built around
a methods-journal craft: a clearly stated **method contribution**, **derived analytical properties**, a
**Monte Carlo simulation study** against real competitors, a **real-data empirical illustration** that
changes a substantive conclusion, and **released, reproducible software** SMR readers can actually run.

Official basis checked **2026-06** (检索于 2026-06；以官网为准): SAGE SMR home and author-instructions
pages, ScholarOne submission, ASA + DataCite citation style, ≤150-word non-parenthetical abstract,
double-anonymized review, data-and-code availability policy, and the generative-AI disclosure rule. See
[`resources/official-source-map.md`](resources/official-source-map.md) for exact source mapping and
unresolved **待核实** items.

---

## What Is SMR, and Why a Dedicated Stack?

SMR is a **methods** journal — its constraints differ from a substantive sociology journal (ASR/AJS)
and from its methods siblings:

| Constraint        | SMR                                                                              | Implication                                                          |
|-------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Scope             | **Develop / evaluate / critically assess** a method                              | An application with no method payoff is desk-reject territory        |
| The "result"      | The **method**, not the substantive finding                                      | Strip the dataset and a methods takeaway must remain                 |
| Evidence          | **Properties + Monte Carlo + real-data illustration**                            | Each property needs a finite-sample check; the simulation needs real competitors |
| Software          | **Released, reproducible** package expected                                       | A method with no usable code is one no one adopts                    |
| Publisher / owner | **SAGE**                                                                          | Submitted via **ScholarOne Manuscripts**                            |
| Review model      | **Double-anonymized**                                                             | Anonymize the manuscript, exhibits, code, and metadata              |
| Abstract          | **≤150 words, no parenthetical citations**                                        | "(Smith 2015)" is not allowed; "Smith (2015)" is                    |
| Style             | **ASA** in-text/references; **DataCite** for datasets                             | Not APA/Chicago-generic                                              |
| Transparency      | **Data-and-code availability statement** at submission; trusted repository        | Write it now, not at acceptance                                     |
| Disclosure        | **Generative-AI use** declared in the back matter                                 | None needed if no AI tool was used                                  |

Volatile specifics (current editor and term, OA charge, exact policy wording) change — items not
directly confirmed are marked **待核实** in
[`resources/official-source-map.md`](resources/official-source-map.md). **Verify on the official SAGE
page.**

### Distinct from its methods siblings

- **Sociological Methodology** (the **ASA annual**, also SAGE) — different editorial model and cadence;
  do not conflate it with SMR.
- **Psychological Methods** (APA) — psychology-facing measurement/statistics audience.
- **Political Analysis** — political-science methods. SMR is the **SAGE quantitative-sociology-methods**
  flagship for sociologists and social scientists broadly.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/sociological-methods-and-research-skills
/plugin install sociological-methods-and-research-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/sociological-methods-and-research-skills.git
cd sociological-methods-and-research-skills

mkdir -p ~/.claude/skills && cp -R skills/smr-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/smr-* ~/.codex/skills/
```

### First Prompt

```
Use smr-workflow to tell me which skill I should use next for my SMR manuscript.
```

---

## Default Workflow

```text
smr-topic-selection
        ▼
smr-method-contribution
        ▼
smr-literature-positioning
        ▼
smr-derivation-and-properties
        ▼
smr-simulation-studies
        ▼
smr-empirical-illustration
        ▼
smr-tables-figures
        ▼
smr-writing-style              (polish)
        ▼
smr-software-and-reproducibility
        ▼
smr-submission
        ▼
smr-rebuttal
```

`smr-workflow` is the router — it tells you which skill to use next based on where you are. The first
hard gate is **fit**: a method contribution, not an application.

---

## Skills

| Skill                                | Purpose                                                                       |
|--------------------------------------|-------------------------------------------------------------------------------|
| `smr-workflow`                       | Router — decides which sub-skill to invoke next                               |
| `smr-topic-selection`                | Is it a method contribution (develop/evaluate/assess), or an application?      |
| `smr-method-contribution`            | The new estimator/design/diagnostic and what it fixes vs. existing methods     |
| `smr-literature-positioning`         | Place against methods across sociology, statistics, econometrics, psychometrics, CSS |
| `smr-derivation-and-properties`      | Assumptions, identification, bias/consistency/efficiency, analytical properties |
| `smr-simulation-studies`             | Monte Carlo DGPs, competing methods, metrics, where the method wins/breaks      |
| `smr-empirical-illustration`         | A real-data demonstration that the method changes a substantive conclusion      |
| `smr-tables-figures`                 | Self-contained simulation grids and method-comparison exhibits in ASA style     |
| `smr-writing-style`                  | Methods-paper arc; ASA style; ≤150-word non-parenthetical abstract              |
| `smr-software-and-reproducibility`   | Released package + reproducible scripts + the data-and-code availability statement |
| `smr-submission`                     | ScholarOne preflight (anonymization, ASA, abstract, availability, AI disclosure) |
| `smr-rebuttal`                       | Verbatim-comment response strategy and revision plan                            |

### Resources

- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — before→after rewrite of a methods-paper introduction in SMR house style (fictional, clearly labeled)
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real, **Crossref-verified** SMR papers by method family, with a sibling-journal guard
- [`resources/official-source-map.md`](resources/official-source-map.md) — official SAGE URLs behind every fact, with 待核实 markers on unverified items
- [`resources/external_tools.md`](resources/external_tools.md) — discipline data sources, software ecosystems (R/Stata/Python/Mplus), ASA/DataCite, and reproducibility deposit

This is a **methods journal** pack: it does **not** vendor the venue-neutral applied causal-inference
code kit. SMR papers ship their own software (`smr-software-and-reproducibility`); the shared
[`reviewer-objection-checklist`](../shared-resources/empirical-methods/reviewer-objection-checklist.md)
and [`reporting-standards`](../shared-resources/empirical-methods/reporting-standards.md) are linked
only as **background** for stress-testing the empirical illustration.

---

## Differences vs. sibling methods journals

| Dimension          | SMR (this pack)                                | Sociological Methodology (ASA annual) | Psychological Methods (APA) | Political Analysis |
|--------------------|-----------------------------------------------|---------------------------------------|-----------------------------|--------------------|
| Owner / publisher  | **SAGE**                                       | ASA / SAGE                            | APA                         | Cambridge / SPM    |
| Cadence            | Continuous journal                             | **Annual volume**                     | Journal                     | Journal            |
| Core audience      | Sociology + social-science methodologists      | Sociology methodologists              | Psychology methodologists   | Political-science methodologists |
| Typical paper      | Estimator/diagnostic + sim + illustration + code | Often longer/programmatic methods     | Measurement/statistics for psych | Poli-sci methods |
| Citation style     | **ASA** (+ DataCite)                            | ASA                                   | APA                         | venue style        |

Confirm any cross-journal claim before relying on it; editorial models change.

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate any specific editor's or reviewer's taste
- It does not assert volatile metadata (current editor and term, OA charge, exact policy wording) — verify on the official SAGE page; unverified items are marked 待核实
- It does not decide whether your method is a genuine contribution — that is the researcher's call (the `smr-topic-selection` gate helps you self-assess)

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Sociological Methods & Research (SAGE Journals)](https://journals.sagepub.com/home/smr) — publisher home
- [SMR author instructions](https://journals.sagepub.com/author-instructions/smr) — submission guidelines and policies

---

## License

MIT
