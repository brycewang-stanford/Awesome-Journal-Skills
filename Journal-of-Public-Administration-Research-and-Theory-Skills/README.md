# Journal of Public Administration Research and Theory Skills

<p align="center">
  <img src="assets/cover.svg" alt="Journal of Public Administration Research and Theory cover" width="200">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-JPART-1f5135)](https://academic.oup.com/jpart)
[![Field](https://img.shields.io/badge/field-Public%20Administration-1f6feb)](https://www.pmranet.org/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at the **Journal of Public Administration Research and Theory
(JPART)** — the **theory-and-research flagship of public administration**, established in **1991**,
published by **Oxford University Press** on behalf of the **Public Management Research Association
(PMRA)**. JPART publishes the highest-quality **theoretical and empirical** work on the public sector:
bureaucratic behavior, public service motivation, red tape, representative bureaucracy, performance
management, collaborative and network governance, and behavioral public administration.

This repository is opinionated. It is **not** a generic social-science writing toolbox, and it is **not**
a policy-evaluation pack. It is a **JPART-specific** stack: a contribution to **public-management
theory**, a named **mechanism**, a design defended on increasingly **experimental and causal** terms,
**double-blind** preparation, and a **public release of data and software code** as a condition of
publication.

---

## What Is JPART, and Why a Dedicated Stack?

JPART's constraints differ from a broad PA journal or a policy-analysis venue:

| Constraint            | JPART                                                                               | Implication                                                       |
|-----------------------|-------------------------------------------------------------------------------------|------------------------------------------------------------------|
| Premium on            | A contribution to **public-management theory** + rigorous empirics                  | A stand-alone policy finding is off-fit                           |
| Mechanism             | A **named mechanism**, not just an effect                                            | "We test X in setting Y" is not enough                           |
| Methods               | Increasingly **experimental and causal**; multilevel; mixed methods                  | Confront common-method bias and selection head-on               |
| Publisher / owner     | **Oxford University Press** / **PMRA**                                               | Submitted via **Editorial Express**, not ScholarOne/Editorial Manager |
| Review model          | **Double-blind**, detailed and developmental                                         | Anonymize the manuscript; identifiers on the cover sheet only    |
| Length                | **~12,000 words including abstract, tables, and references**                         | The cap counts references — prune citation padding              |
| Abstract              | State **theory → method/data → results → implications for theory**                   | Lead with the theoretical approach                              |
| Keywords              | **3–5**; first three signal **theory, research theme, method**                       | Not a free-form tag list                                        |
| Style                 | **OUP author-date** with DOIs                                                        | Reference list alphabetical, DOIs required                      |
| Transparency          | **Public release of data + code** as a condition of publication; Data Availability Statement | Build the package as you go; release is mandatory       |

Volatile specifics (editors and term, exact caps, fee/APC, policy wording) change — items not directly
confirmed are marked **待核实** in [`resources/official-source-map.md`](resources/official-source-map.md).
**Verify on the official journal page** (检索于 2026-06；以官网为准).

### Distinguish JPART from its siblings

- **Public Administration Review (PAR)** — broader, more integrative and practitioner-facing.
- **JPAM** — policy analysis and program evaluation.
- **Governance** — comparative institutions of government, lighter on public-management mechanisms.
- **JPART** — public-management **theory** tested with rigorous (often experimental/causal) empirics.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/jpart-skills
/plugin install jpart-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/jpart-skills.git
cd jpart-skills

mkdir -p ~/.claude/skills && cp -R skills/jpart-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/jpart-* ~/.codex/skills/
```

### First Prompt

```
Use jpart-workflow to tell me which skill I should use next for my JPART manuscript.
```

---

## Default Workflow

```text
jpart-topic-selection
        ▼
jpart-literature-positioning
        ▼
jpart-theory-building
        ▼
jpart-research-design
        ▼
jpart-data-analysis
        ▼
jpart-tables-figures
        ▼
jpart-writing-style          (polish)
        ▼
jpart-transparency-and-data
        ▼
jpart-review-process
        ▼
jpart-submission
        ▼
jpart-rebuttal
```

`jpart-workflow` is the router — it tells you which skill to use next based on where you are, and it
enforces the journal's defining gate: **is there a public-management theory contribution?** If the theory
slot is empty, it routes back to theory-building or topic-selection before letting you move forward.

---

## Skills

| Skill                            | Purpose                                                                       |
|----------------------------------|-------------------------------------------------------------------------------|
| `jpart-workflow`                 | Router — decides which sub-skill to invoke next; enforces the theory gate      |
| `jpart-topic-selection`          | Public-management theory fit; venue choice vs. PAR / JPAM / Governance         |
| `jpart-literature-positioning`   | Name the PA conversation you advance; engage the theory you claim to test      |
| `jpart-theory-building`          | Build the argument into a theory move (extend / test / bound / overturn)       |
| `jpart-research-design`          | Defend the design — experiments, causal observational, multilevel, mixed       |
| `jpart-data-analysis`            | Analysis norms; common-method bias and selection; robustness; reproducibility  |
| `jpart-tables-figures`           | Self-contained, accessible exhibits that show mechanism and magnitude          |
| `jpart-writing-style`            | OUP author-date; theory-first abstract; ~12,000-word cap (incl. refs)          |
| `jpart-transparency-and-data`    | Public data + code release; Data Availability Statement; exemptions            |
| `jpart-review-process`           | Double-blind, developmental review; desk screening; decision categories        |
| `jpart-submission`               | Editorial Express preflight (anonymization, word count, keywords, DOIs, DAS)   |
| `jpart-rebuttal`                 | R&R response-letter strategy protecting the theory contribution                |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — PA data sources (FEVS / FedScope / ICMA / Form 990 / QoG) + survey/experiment platforms + R / Stata / Python packages
- [`resources/official-source-map.md`](resources/official-source-map.md) — official OUP / JPART URLs behind every fact, with 待核实 markers on unverified items
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — before→after JPART-style introduction (fictional)
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real, web-verified JPART papers by PA theory × method
- [`resources/code/`](resources/code/) — reproducible Stata + Python causal-inference skeleton

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate any specific editor's or reviewer's taste
- It does not assert volatile metadata (current editors and term, exact caps, fee/APC, policy wording) — verify on the official page; unverified items are marked 待核实
- It does not decide whether your question is a public-management theory contribution — that is the researcher's call

---

## Differences vs. Sibling Journals

| Journal | Owner / publisher | Identity | Do not send… |
|---------|-------------------|----------|--------------|
| **JPART** | PMRA / OUP | Public-management **theory** + rigorous empirics | a stand-alone policy finding |
| PAR | ASPA / Wiley | Broad, integrative, practitioner-facing | a narrow theory-test only meant for specialists |
| JPAM | APPAM / Wiley | Policy analysis and program evaluation | a pure management-theory mechanism paper |
| Governance | Wiley | Comparative institutions of government | a US-agency behavioral mechanism with little institutional theory |

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Journal of Public Administration Research and Theory (Oxford Academic)](https://academic.oup.com/jpart) — publisher home
- [Public Management Research Association (PMRA)](https://www.pmranet.org/) — owning society

---

## License

MIT
