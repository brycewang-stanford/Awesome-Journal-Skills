# Communication Research Skills

<p align="center">
  <img src="assets/cover.svg" alt="Communication Research cover" width="200">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Communication%20Research-23457a)](https://journals.sagepub.com/home/crx)
[![Field](https://img.shields.io/badge/field-Communication%20Science-1f6feb)](https://journals.sagepub.com/home/crx)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **Communication Research (CR)** — SAGE's **quantitative,
social-scientific** journal of communication science. CR concentrates on **hypothesis-testing
experiments and surveys** with rigorous measurement and explicit theory: media effects and processing,
persuasion and message effects, interpersonal and organizational communication, health and political
communication, and new-media use and effects.

This repository is opinionated. It is **not** a generic social-science writing toolbox, and it is
**not** the *Journal of Communication* (the all-paradigm ICA flagship) repurposed. It is a
**CR-specific** stack: a communication-science question with a **tested mechanism** (mediation /
moderation), a design defended on quantitative terms with **valid, reliable measurement**, **APA**
statistical reporting (effect sizes and standard deviations), **double-anonymized** preparation, and a
**data-availability statement** with reproducible materials prepared as you write.

---

## What Is CR, and Why a Dedicated Stack?

CR's constraints differ from a generalist or a qualitative communication journal:

| Constraint        | Communication Research                                                        | Implication                                                      |
|-------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------|
| Scope             | **Quantitative, social-scientific** communication science                    | Qualitative/interpretive work is off-fit — re-route to a sibling |
| Premium on        | A **tested mechanism** (mediation/moderation), not a bare effect             | A main effect with no process rarely clears the bar             |
| Methods           | Experiments, panel surveys, content analysis with reliability                | Match a quantitative design with valid measurement             |
| Publisher         | **SAGE Publishing** (founded 1974; bimonthly)                                | Submitted via **SAGE Track** (ScholarOne)                      |
| Review model      | **Double-anonymized**; **two independent reviews** to back a Revise/Accept   | Anonymize main doc *and* supplements; satisfy two experts      |
| Length            | Manuscript **≤ 45 pages, double-spaced, inclusive of references**            | References count; move detail to the online supplement         |
| Style / reporting | **APA**; report **effect sizes and standard deviations**                     | Stars-only tables are an APA-reporting failure here            |
| Transparency      | **Data-availability statement**; open materials/data; preregistration        | Build the statement and materials as you go                    |
| Measurement       | Validated scales (alpha/omega, CFA); intercoder reliability; CMV control     | Reviewers probe construct validity, not just reliability       |

Volatile specifics (editors and term, exact caps, fee/APC, data/ORCID requirement level) change — items
not directly confirmed are marked **待核实** in
[`resources/official-source-map.md`](resources/official-source-map.md). **Verify on the official SAGE
journal page** (检索于 2026-06；以官网为准).

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/communication-research-skills
/plugin install communication-research-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/communication-research-skills.git
cd communication-research-skills

mkdir -p ~/.claude/skills && cp -R skills/commres-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/commres-* ~/.codex/skills/
```

### First Prompt

```
Use commres-workflow to tell me which skill I should use next for my Communication Research manuscript.
```

---

## Default Workflow

```text
commres-topic-selection
        ▼
commres-literature-positioning
        ▼
commres-theory-building
        ▼
commres-research-design
        ▼
commres-data-analysis
        ▼
commres-tables-figures
        ▼
commres-writing-style          (polish)
        ▼
commres-transparency-and-data
        ▼
commres-review-process
        ▼
commres-submission
        ▼
commres-rebuttal
```

`commres-workflow` is the router — it tells you which skill to use next based on where you are. If your
design is **prospective**, route to `commres-transparency-and-data` early to **preregister**; most CR
papers loop theory ↔ design ↔ measurement several times before writing-style.

---

## Skills

| Skill                          | Purpose                                                                       |
|--------------------------------|-------------------------------------------------------------------------------|
| `commres-workflow`             | Router — decides which sub-skill to invoke next                               |
| `commres-topic-selection`      | Quantitative, theory-testing fit; a tested mechanism, not platform novelty     |
| `commres-literature-positioning` | Position against prior empirical tests; build to numbered hypotheses          |
| `commres-theory-building`      | Constructs, mechanism, and numbered hypotheses (mediation/moderation)         |
| `commres-research-design`      | Defend experiments / panel surveys / content analysis on quantitative terms   |
| `commres-data-analysis`        | ANOVA/regression/SEM, mediation with bootstrap CIs, APA reporting, robustness |
| `commres-tables-figures`       | Self-contained, accessible APA exhibits showing effect sizes and uncertainty  |
| `commres-writing-style`        | Cumulative social-science prose; APA; the 45-page limit                       |
| `commres-transparency-and-data`| Data-availability statement; open materials/data; preregistration; ORCID      |
| `commres-review-process`       | Double-anonymized review; the two-independent-review requirement              |
| `commres-submission`           | SAGE Track preflight (anonymization, 45-page cap, APA reporting, DAS)         |
| `commres-rebuttal`             | R&R response strategy for two demanding quantitative reviewers + editor       |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — communication data sources (ANES / CES / Pew / HINTS / GDELT) + R / SPSS-PROCESS / Mplus / Python, with a measurement/reliability/SEM focus
- [`resources/official-source-map.md`](resources/official-source-map.md) — official SAGE/CR URLs behind every fact, with 待核实 markers on unverified items
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — a fictional CR-style introduction + abstract
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real, web-verified CR papers by method × topic
- [`resources/code/`](resources/code/) — vendored reproducible Stata + Python analysis skeleton

---

## Differences vs. Sibling Journals

| Journal | Owner / publisher | Paradigm | This pack's guard |
|---------|-------------------|----------|-------------------|
| **Communication Research** | SAGE | **Quantitative, social-scientific** | the home venue for hypothesis-testing communication science |
| Journal of Communication | ICA / Oxford UP | All-paradigm, field-wide flagship | broader and not exclusively quantitative — re-route generalist/interpretive work |
| Human Communication Research | ICA / Oxford UP | Interpersonal / HCR | re-route interpersonal-theory-testing work that fits HCR better |
| New Media & Society | SAGE | Digital media, often more qualitative | re-route platform-focused or qualitative digital-media work |

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate any specific editor's or reviewer's taste
- It does not assert volatile metadata (current editors and term, exact caps, fee/APC, requirement levels) — verify on the official page; unverified items are marked 待核实
- It does not decide whether your study is quantitative and theory-testing enough for CR — that is the researcher's call

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Communication Research (SAGE Journals)](https://journals.sagepub.com/home/crx) — publisher home
- [CR Submission Guidelines (SAGE)](https://journals.sagepub.com/author-instructions/crx) — author instructions

---

## License

MIT
