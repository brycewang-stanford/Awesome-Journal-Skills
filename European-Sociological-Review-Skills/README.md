# European Sociological Review Skills

<p align="center">
  <img src="assets/cover.svg" alt="European Sociological Review cover" width="200">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-ESR-1f5a66)](https://academic.oup.com/esr)
[![Field](https://img.shields.io/badge/field-Quantitative%20Sociology-1f6feb)](https://ecsrnet.eu/european-sociological-review-esr/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at the **European Sociological Review (ESR)** — the
**flagship quantitative-sociology journal of the European Consortium for Sociological Research (ECSR)**,
published by **Oxford University Press**. ESR publishes rigorous comparative and longitudinal
quantitative work: social stratification and mobility, education, labor markets, family and life course,
migration and ethnicity, attitudes, and cross-national European social structure — analyzed with
multilevel and SEM models, panel and event-history designs, comparative designs, and causal inference
where feasible, on harmonized survey data (ESS, EU-SILC, SOEP, EVS).

This repository is opinionated. It is **not** a generic social-science writing toolbox and it is
**not** a US-sociology or economics pack relabeled. It is an **ESR-specific** stack: a question with a
portable mechanism, comparative or longitudinal leverage, correct multilevel/measurement modeling, a
**completely anonymous** manuscript, submission through **ScholarOne**, a required **Data Availability
Statement**, and (for statistical/computational work) a **replication package** as a condition of
publication.

**Official basis checked 2026-06** (检索于 2026-06；以官网为准). Volatile specifics
(editors and term, exact caps, replication-policy dates, OA charges) change — items not directly
confirmed are marked **待核实** in
[`resources/official-source-map.md`](resources/official-source-map.md). **Verify on the official
journal page.**

---

## What Is ESR, and Why a Dedicated Stack?

ESR's constraints differ from a general or US-sociology journal:

| Constraint            | ESR                                                                           | Implication                                                       |
|-----------------------|-------------------------------------------------------------------------------|------------------------------------------------------------------|
| Scope                 | **European quantitative sociology**                                           | The paper needs a portable mechanism + comparative/longitudinal leverage |
| Premium on            | Macro–micro mechanism tested with rigorous quantitative design                | A single-country descriptive result is off-fit                   |
| Methods               | Multilevel / SEM, panel & event-history, comparative, causal where feasible   | Get the level, clustering, and measurement equivalence right     |
| Publisher / owner     | **Oxford University Press** / **ECSR**                                         | Submitted via **ScholarOne**, not Editorial Manager or Sage Track |
| Review model          | **Double-blind** — completely anonymous manuscript                            | You *may* self-cite, just not identifyingly                      |
| Length                | **Articles ~8,000 words** incl. endnotes + references; longer with justification | Endnotes and references count toward the target              |
| Abstract              | **≤200 words**, non-identifying                                               | Tighter than journals that allow 250                            |
| Style                 | English; **author-date** citations (e.g., "(Gans, 1962)")                     | OUP/ESR conventions                                             |
| Transparency          | **Data Availability Statement (required)** + **replication package** for statistical work (subs. from 1 Jan 2025) | A condition of publication, not a norm |
| Article types         | Research Articles, Comments/Replies, **Data Briefs**                          | A Data Brief showcases a data source, not a full causal argument |

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/european-sociological-review-skills
/plugin install european-sociological-review-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/european-sociological-review-skills.git
cd european-sociological-review-skills

mkdir -p ~/.claude/skills && cp -R skills/eursr-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/eursr-* ~/.codex/skills/
```

### First Prompt

```
Use eursr-workflow to tell me which skill I should use next for my ESR manuscript.
```

---

## Default Workflow

```text
eursr-topic-selection
        ▼
eursr-literature-positioning
        ▼
eursr-theory-building
        ▼
eursr-research-design
        ▼
eursr-data-analysis
        ▼
eursr-tables-figures
        ▼
eursr-writing-style          (polish)
        ▼
eursr-transparency-and-data
        ▼
eursr-review-process
        ▼
eursr-submission
        ▼
eursr-rebuttal
```

`eursr-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill                          | Purpose                                                                       |
|--------------------------------|-------------------------------------------------------------------------------|
| `eursr-workflow`               | Router — decides which sub-skill to invoke next                               |
| `eursr-topic-selection`        | Portable mechanism + comparative leverage; Article vs. Comment vs. Data Brief |
| `eursr-literature-positioning` | Place the contribution in a live comparative European debate                  |
| `eursr-theory-building`        | Build a macro–micro mechanism with a testable cross-level hypothesis          |
| `eursr-research-design`        | Defend the design — comparative, panel/event-history, multilevel, causal      |
| `eursr-data-analysis`          | Multilevel/longitudinal modeling, few-cluster inference, robustness           |
| `eursr-tables-figures`         | Clear, self-contained exhibits (excluded from the word count)                 |
| `eursr-writing-style`          | OUP author-date style; reach the comparative reader within ~8,000 words       |
| `eursr-transparency-and-data`  | Data Availability Statement + replication-package mandate                     |
| `eursr-review-process`         | Double-blind review, decisions, what reviewers weigh                          |
| `eursr-submission`             | ScholarOne preflight (anonymity, ~8,000 words, ≤200 abstract, DAS/package)    |
| `eursr-rebuttal`               | R&R response-letter strategy for multiple reviewers + editor                  |

### Resources

- [`resources/code/`](resources/code/) — reproducible Stata + Python causal-inference skeleton (base for the replication package)
- [`resources/external_tools.md`](resources/external_tools.md) — European data (ESS / EU-SILC / SOEP / EVS), ISCED/ISEI/EGP harmonization, multilevel / SEM / panel software
- [`resources/official-source-map.md`](resources/official-source-map.md) — official OUP / ECSR URLs behind every fact, with 待核实 markers
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — a before→after ESR-style introduction (fictional)
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real, web-verified ESR papers by method × topic

---

## Differences vs. Sibling Journals

| Journal | Owner / publisher | Identity vs. ESR |
|---------|-------------------|------------------|
| **European Sociological Review (ESR)** | ECSR / OUP | **This pack** — European quantitative-sociology flagship; comparative & longitudinal |
| American Sociological Review (ASR) | ASA / SAGE | US general flagship; all methods incl. theory & qualitative; Sage Track, $25 fee |
| American Journal of Sociology (AJS) | U. Chicago | US general; more theory/qualitative breadth |
| European Societies | ESA / Taylor & Francis | The ESA journal; broader, not the ECSR quantitative flagship |
| European Journal of Sociology | Cambridge UP | More theoretical/historical; not primarily quantitative |
| Sociological Methods & Research | SAGE | Methods journal, not substantive quantitative articles |

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate any specific editor's or reviewer's taste
- It does not assert volatile metadata (current editors and term, exact caps, policy dates, OA charges) — verify on the official page; unverified items are marked 待核实
- It does not decide whether your question carries a portable, comparative mechanism — that is the researcher's call

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [European Sociological Review (OUP)](https://academic.oup.com/esr) — publisher home
- [ESR at ECSR](https://ecsrnet.eu/european-sociological-review-esr/) — owner, scope, editorial information

---

## License

MIT
