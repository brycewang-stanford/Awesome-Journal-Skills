# American Educational Research Journal Skills

<p align="center">
  <img src="assets/cover.svg" alt="American Educational Research Journal cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-AERJ-a85d1b)](https://journals.sagepub.com/home/aer)
[![Field](https://img.shields.io/badge/field-Education%20Research-1f6feb)](https://www.aera.net/Publications/Journals/American-Educational-Research-Journal)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at the **American Educational Research Journal (AERJ)** —
the **flagship journal of the American Educational Research Association (AERA)**, founded in **1964**
and published by **SAGE**. AERJ publishes original peer-reviewed analyses that span the **whole field
of education research** — across all subfields, all levels of education and the lifespan, and all
forms of learning — using **quantitative, qualitative, and mixed methods** alike.

What makes AERJ structurally distinct is that it is **two separately edited sections** under one
cover: **Social and Institutional Analysis (SIA)** — political, cultural, social, economic, and
organizational issues in education — and **Teaching, Learning, and Human Development (TLHD)** — the
processes and outcomes of teaching, learning, and human development in formal and informal settings.

This repository is opinionated. It is **not** a generic social-science writing toolbox and it is
**not** an economics or psychology pack repurposed for education. It is an **AERJ-specific** stack: a
question of **broad significance to education research**, routed to the **right section**, an argument
anchored in a **conceptual or theoretical framework**, a design defended on **its own methodological
terms** (quant / qual / mixed), **masked** preparation in **APA 7th-edition** style, and reporting
that meets the **AERA Standards for Reporting on Empirical Social Science Research**.

---

## What Is AERJ, and Why a Dedicated Stack?

AERJ's constraints differ from a narrow specialty journal or a methods journal:

| Constraint            | AERJ                                                                          | Implication                                                       |
|-----------------------|-------------------------------------------------------------------------------|------------------------------------------------------------------|
| Scope                 | **Whole field** of education research, all levels and methods                 | The paper must matter beyond one subfield                        |
| Structure             | **Two separately edited sections** — SIA and TLHD                             | Pick the right section at submission; route to the right editors |
| Premium on            | **Broad significance** + a clear conceptual/theoretical framework             | A narrow, descriptive-only result is off-fit                     |
| Methods               | Quantitative, qualitative, and mixed methods — judged on their own terms      | Do not force one template onto every paper                       |
| Publisher / owner     | **SAGE** / **AERA**                                                           | Submitted via **ScholarOne Manuscript Central**                  |
| Review model          | **Masked (anonymous)**                                                        | Anonymize the manuscript; names only on the title page file      |
| Fee                   | **No submission fee** stated; AERA membership **not** required to submit      | Do not budget a submission fee (verify)                          |
| Length                | Manuscripts **~20–50 pages** (double-spaced, 12-pt, 1" margins, inclusive)    | Plan length including tables, figures, notes, references         |
| Abstract              | **100–120 words**                                                             | Tight, structured abstract                                       |
| Style                 | **APA 7th edition** (author-date)                                             | Not Chicago/AERA-house; ORCID for the corresponding author       |
| Reporting standards   | **AERA reporting standards** (empirical social science; humanities companion) | Report against the standard that matches your method             |

Volatile specifics (editors and section assignments, exact caps, fee/APC, portal URL, policy wording)
change — items not directly confirmed are marked **待核实** in
[`resources/official-source-map.md`](resources/official-source-map.md).
**Verify on the official journal page.**

### The two sections

- **Social and Institutional Analysis (SIA)** — political, cultural, social, economic, and
  organizational issues in education: policy, governance, equity, institutions, organizations.
- **Teaching, Learning, and Human Development (TLHD)** — processes and outcomes of teaching, learning,
  and human development across levels, in both formal and informal settings.
- Both sections publish across many disciplines and methods. **You choose the section at submission**;
  if it sits across both, name the better fit and say why.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/aerj-skills
/plugin install aerj-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/aerj-skills.git
cd aerj-skills

mkdir -p ~/.claude/skills && cp -R skills/aerj-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/aerj-* ~/.codex/skills/
```

### First Prompt

```
Use aerj-workflow to tell me which skill I should use next for my AERJ manuscript.
```

---

## Default Workflow

```text
aerj-topic-selection         (incl. SIA vs TLHD)
        ▼
aerj-literature-positioning
        ▼
aerj-theory-and-framework
        ▼
aerj-research-design         (quant / qual / mixed)
        ▼
aerj-data-analysis
        ▼
aerj-tables-figures
        ▼
aerj-writing-style           (polish)
        ▼
aerj-transparency-and-data-policy
        ▼
aerj-review-process
        ▼
aerj-submission
        ▼
aerj-rebuttal
```

`aerj-workflow` is the router — it tells you which skill to use next based on where you are and which
**section** (SIA or TLHD) fits. If your design is **prospective**, route to `aerj-research-design`
early to consider **preregistration**; if your contribution is conceptual or methodological, lean on
`aerj-theory-and-framework` and `aerj-literature-positioning`.

---

## Skills

| Skill                                | Purpose                                                                       |
|--------------------------------------|-------------------------------------------------------------------------------|
| `aerj-workflow`                      | Router — decides which sub-skill to invoke next; flags section fit            |
| `aerj-topic-selection`               | Broad-significance fit across the field; choose **SIA vs TLHD**               |
| `aerj-literature-positioning`        | Speak past your subfield; engage the literatures AERJ readers expect          |
| `aerj-theory-and-framework`          | Build the conceptual / theoretical framework that frames the contribution     |
| `aerj-research-design`               | Defend the design — quantitative, qualitative, or mixed methods in education   |
| `aerj-data-analysis`                 | Analysis norms (multilevel, IRT, qual coding), uncertainty, robustness         |
| `aerj-tables-figures`                | Accessible, self-contained exhibits in APA 7th-edition format                  |
| `aerj-writing-style`                 | APA 7th edition; reach the whole field within the length limit                 |
| `aerj-transparency-and-data-policy`  | AERA reporting standards; data availability; qualitative transparency          |
| `aerj-review-process`                | Masked review, desk screening, section routing, decision categories            |
| `aerj-submission`                    | ScholarOne preflight (masking, length, abstract, APA, ORCID, title page)       |
| `aerj-rebuttal`                      | R&R response-letter strategy for multiple reviewers + the section editor       |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — education-research data sources (NCES / ECLS / NAEP / SEDA / PISA / TIMSS / state SLDS / QDR) + R / Stata / Mplus / HLM and qualitative/CAQDAS tooling
- [`resources/official-source-map.md`](resources/official-source-map.md) — official AERA / SAGE URLs behind every fact, with 待核实 markers on unverified items

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate any specific editor's or reviewer's taste
- It does not assert volatile metadata (current editors and section assignments, exact caps, fee/APC, policy wording) — verify on the official page; unverified items are marked 待核实
- It does not decide whether your question is of broad significance to education research — that is the researcher's call
- It does not choose your section for you — it helps you reason about SIA vs TLHD

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [American Educational Research Journal (SAGE Journals)](https://journals.sagepub.com/home/aer) — publisher home
- [AERJ at AERA](https://www.aera.net/Publications/Journals/American-Educational-Research-Journal) — owner, sections, editors, policies

---

## License

MIT
