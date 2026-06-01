# Production and Operations Management (POM) Skills

<p align="center">
  <img src="assets/cover.svg" alt="Production and Operations Management cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-POM-0b4f6c)](https://www.poms.org/journal)
[![Publisher](https://img.shields.io/badge/publisher-SAGE%20%7C%20POMS-1f6feb)](https://journals.sagepub.com/home/PAO)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **Production and Operations Management (POM)** — the flagship journal of the **Production and Operations Management Society (POMS)**, published by **SAGE** (since January 2024; previously Wiley-Blackwell). ISSN 1059-1478.

This repository is opinionated. It is **not** a generic "operations writing" toolbox. It is a **POM-specific** stack built around the journal's defining bar: a rigorous study — by whatever method — that is of **significant interest to practicing operations managers** *and* makes a **substantial contribution to knowledge and practice**. It covers topic selection, OM model/theory development, literature positioning, method-fit and analysis across POM's research traditions (analytical/mathematical modeling, empirical OM, behavioral/experimental OM, operations data science), contribution framing, exhibits, prose, ScholarOne submission to a **Department Editor**, the review process, and R&R rebuttals.

> Durable norms only. Editors, fees, the department roster, and exact limits change — always verify on the official POMS author-instructions page and the SAGE journal page. Items we could not confirm are marked **待核实** in `resources/official-source-map.md`.

---

## Why a Separate POM Skill Stack?

POM imposes constraints that differ materially from theory-only management journals or capital-markets finance/accounting journals:

| Constraint              | Production and Operations Management                                  | Implication                                                            |
|-------------------------|----------------------------------------------------------------------|-----------------------------------------------------------------------|
| Discipline              | Operations management & supply chain (the full breadth of OM)        | Pure non-OM economics, OB, or marketing papers are off-fit            |
| Core bar                | Significant interest to practicing OM **and** substantial contribution | Elegant model with no managerial insight reads as a math exercise     |
| Routing                 | Submit to **one named Department** (Behavioral Ops, SCM, Healthcare Ops, Sustainable Ops, OM Data Analytics, interface depts…) | Wrong department = misrouting; the cover letter must target one       |
| Method                  | No method mandated; anchored in analytical modeling, with empirical, behavioral, and data-science tracks | The method must *fit* the question and be executed rigorously          |
| Practice-relevance gate | "So what for the operations manager?" is weighted alongside rigor    | Insight-free technique is a reject signal                              |
| Format                  | **32-page** hard cap (incl. references, appendices, tables, figures); 1.5 spacing, 11-pt | Proofs/extra material move to the **unlimited online e-companion**     |
| Abstract                | ≤ 350 words, **no formulas / references / abbreviations**; title ≤ 25 words | Discipline required up front                                          |
| Review                  | **Double-blind**; remove names and acknowledgments                   | Self-identifying citations/notes break anonymity                      |
| Resubmission            | Rejected papers may **not** be resubmitted to the same *or a different* department unless invited | Stricter than most peers — one shot per paper                         |
| Disclosure              | Cover letter must list **same-data / related prior work**            | Undisclosed data overlap is a serious integrity issue                 |

Generic "scientific writing" or "social-science methods" packs do not address these constraints.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/pom-skills
/plugin install pom-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/pom-skills.git
cd pom-skills

mkdir -p ~/.claude/skills && cp -R skills/pom-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/pom-* ~/.codex/skills/
```

### First Prompt

```
Use pom-workflow to tell me which skill I should use next for my POM manuscript.
```

---

## Default Workflow

```text
pom-topic-selection
        ▼
pom-theory-development
        ▼
pom-literature-positioning
        ▼
pom-methods
        ▼
pom-data-analysis
        ▼
pom-contribution-framing
        ▼
pom-tables-figures
        ▼
pom-writing-style        (polish)
        ▼
pom-submission
        ▼
pom-review-process
        ▼
pom-rebuttal
```

`pom-workflow` is the router — it tells you which skill to use next based on where you are and which research tradition (analytical / empirical / behavioral / data-science) your paper belongs to.

---

## Skills

| Skill                       | Purpose                                                                              |
|-----------------------------|--------------------------------------------------------------------------------------|
| `pom-workflow`              | Router — decides which sub-skill to invoke next; identifies your method track        |
| `pom-topic-selection`       | OM question + POM fit test + target Department selection                              |
| `pom-theory-development`    | Build the model/mechanism: assumptions, equilibria, propositions, or hypotheses      |
| `pom-literature-positioning`| Join an OM conversation; position against the right department's prior work           |
| `pom-methods`               | Match method (optimization/stochastic/game-theory/empirical/behavioral/ML) to the question |
| `pom-data-analysis`         | Execute & report: proofs and numerics, or identification, estimation, robustness     |
| `pom-contribution-framing`  | State the managerial insight + the contribution to OM knowledge and practice          |
| `pom-tables-figures`        | Result tables, sensitivity/comparative-statics plots, model schematics                |
| `pom-writing-style`         | Front-loaded argument, author-year citations, 32-page discipline, e-companion split   |
| `pom-submission`            | ScholarOne preflight: department routing, double-blind, 350-word abstract, same-data disclosure |
| `pom-review-process`        | How POM department review/decisions work; the no-resubmission rule                   |
| `pom-rebuttal`              | R&R revision and point-by-point response to the Department Editor and referees         |

### Resources

- [`resources/official-source-map.md`](resources/official-source-map.md) — every venue fact with its official URL and accessed date; unverified items marked **待核实**
- [`resources/external_tools.md`](resources/external_tools.md) — solvers (Gurobi / CPLEX / Mosek), modeling languages (AMPL / Pyomo / JuMP), simulation (Arena / AnyLogic / SimPy), econometrics (Stata / R `fixest`), experiments (oTree / Prolific), and data science (scikit-learn / forecasting)

---

## Differences vs. M&SOM / MS-Operations / JOM / IJOPM

| Dimension          | POM                                            | M&SOM                              | Management Science (Ops)         | JOM / IJOPM                     |
|--------------------|------------------------------------------------|------------------------------------|----------------------------------|---------------------------------|
| Society / publisher| POMS / SAGE                                     | INFORMS                            | INFORMS                          | various / Elsevier              |
| Breadth            | Full breadth of OM, **department-routed**       | OM, more model-leaning             | Broad management, OM department  | Often more empirical / process  |
| Signature emphasis | Rigor **and** practicing-manager relevance      | Modeling + empirical OM            | Methodological depth             | Empirical OM, OM practice       |
| Format quirk       | 32-page cap + unlimited e-companion; no resubmit| INFORMS limits                     | INFORMS limits                   | publisher-specific              |

POM's defining structural norm is **submission to a named Department Editor** plus a **practice-relevance gate** — pick the right department before you submit.

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — index of journal-specific skill packs

---

## License

MIT
