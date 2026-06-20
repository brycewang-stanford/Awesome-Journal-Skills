# Journal of Accounting and Economics (JAE) Skills

<p align="center">
  <img src="assets/cover.svg" alt="Journal of Accounting and Economics cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-JAE-b8520a)](https://www.sciencedirect.com/journal/journal-of-accounting-and-economics)
[![Publisher](https://img.shields.io/badge/publisher-Elsevier%20%7C%20est.%201979-1f6feb)](https://www.sciencedirect.com/journal/journal-of-accounting-and-economics)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at the **Journal of Accounting and Economics (JAE)** — the Elsevier journal founded in **1979** by Ross L. Watts and Jerold L. Zimmerman as the home of **positive (economics-based) accounting research**.

This repository is opinionated. It is **not** a generic "accounting writing" toolbox. It is a **JAE-specific** stack built around JAE's defining bar: an argument that **applies economic theory to explain accounting phenomena**, tested with large-sample archival data or built as an analytical economic model. It covers the role of accounting within the firm, the information content of accounting numbers in capital markets, accounting in financial contracting and the monitoring of agency relationships, the determination of accounting standards, and the regulation of corporate disclosure and the accounting profession — plus identification-focused design, Elsevier house-style exhibits, the Editorial Manager submission flow, double-anonymized review, and R&R rebuttals.

> Durable norms only. Editors, the submission fee, Highlights/keyword/JEL requirements, and the data-sharing policy change — always verify on the official JAE Guide for Authors (ScienceDirect) and Elsevier policy pages.

---

## Why a Separate JAE Skill Stack?

JAE imposes constraints that differ materially from behavioral, normative, or generic management journals:

| Constraint              | Journal of Accounting and Economics                                  | Implication                                                  |
|-------------------------|----------------------------------------------------------------------|--------------------------------------------------------------|
| Discipline              | Positive (economics-based) accounting — Watts-Zimmerman tradition     | Normative, behavioral, or practitioner work is off-fit       |
| Core bar                | Apply economic theory to explain an accounting phenomenon            | A bare Compustat correlation reads as fishing                |
| Theory                  | Agency, information economics, contracting, political-cost mechanisms | Atheoretical "A relates to B" is a reject signal             |
| Method                  | Large-sample archival econometrics + analytical modeling             | Lab experiments and design-science are off-fit               |
| Identification          | Natural experiments, DiD, IV, RD; firm/year FE; two-way clustering   | Pooled OLS presented as causal is punished                   |
| Contribution            | What economic understanding of accounting changes?                   | "First to study X" is not a contribution                     |
| Format                  | Elsevier author-date (Harvard); numbered sections; mandatory Highlights | Vancouver references and missing JEL codes fail preflight |
| Process                 | Editorial Manager; fee-bearing submission; double-anonymized; editor-final | Desk-reject / Article-Transfer redirect for off-fit papers |
| Data policy             | **Voluntary** sharing (Elsevier policy), **no** mandated archive     | Unlike JAR/JFE, no replication package is required           |

Generic "scientific writing" or "social-science methods" packs do not address these constraints.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/jae-skills
/plugin install jae-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/jae-skills.git
cd jae-skills

mkdir -p ~/.claude/skills && cp -R skills/jae-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/jae-* ~/.codex/skills/
```

### First Prompt

```
Use jae-workflow to tell me which skill I should use next for my JAE manuscript.
```

---

## Default Workflow

```text
jae-topic-selection
        ▼
jae-theory-development
        ▼
jae-literature-positioning
        ▼
jae-methods
        ▼
jae-data-analysis
        ▼
jae-contribution-framing
        ▼
jae-tables-figures
        ▼
jae-writing-style        (polish)
        ▼
jae-submission
        ▼
jae-review-process
        ▼
jae-rebuttal
```

`jae-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill                       | Purpose                                                                 |
|-----------------------------|-------------------------------------------------------------------------|
| `jae-workflow`              | Router — decides which sub-skill to invoke next                         |
| `jae-topic-selection`       | Economics-based question + JAE fit test (vs. JAR/TAR/RAST/JFE)          |
| `jae-theory-development`    | Agency/information/contracting mechanisms; a priori predictions         |
| `jae-literature-positioning`| Joining the positive-accounting conversation; problematization          |
| `jae-methods`               | Identification design (natural experiments, DiD, IV, RD) or modeling     |
| `jae-data-analysis`         | Sample waterfall, firm/year FE, two-way clustering, robustness          |
| `jae-contribution-framing`  | Explicit economic contribution statement + discussion                   |
| `jae-tables-figures`        | Variable defs, descriptives, regression tables, event-study/DiD figures |
| `jae-writing-style`         | Economics-paper prose, Elsevier author-date, Highlights/keywords/JEL     |
| `jae-submission`            | Editorial Manager preflight (anonymization, fee, Highlights, JEL)       |
| `jae-review-process`        | How JAE review/decisions work; the JAE Conference pipeline              |
| `jae-rebuttal`              | R&R revision and point-by-point response letter                         |

### Resources

- [`resources/official-source-map.md`](resources/official-source-map.md) — every JAE fact used here, its official URL, live-check boundary, and refreshed date (2026-06-20)
- [`resources/external_tools.md`](resources/external_tools.md) — positive-accounting data sources (Compustat / CRSP / I/B/E/S / Execucomp / DealScan / Audit Analytics via WRDS), econometric software (Stata `reghdfe`/`ivreg2`/`csdid`, SAS, R `fixest`), and Elsevier/LaTeX writing tools

---

## Differences vs. JAR / TAR / RAST / JFE

| Dimension          | JAE                                  | JAR                          | TAR                          | JFE (finance)                |
|--------------------|--------------------------------------|------------------------------|------------------------------|------------------------------|
| Core identity      | Positive (economics-based) accounting| Top-3 archival accounting    | AAA flagship, broad tent     | Financial economics          |
| Signature methods  | Archival econometrics + modeling     | Archival, identification     | Experimental/analytical/archival | Archival asset pricing/corp |
| Replication policy  | **Voluntary** (no mandate)           | **Mandatory** code/data      | Varies                       | **Mandatory** Mendeley deposit |
| Submission fee     | Fee-bearing; check current JAE amount | Varies                       | Varies                       | Varies                       |
| Editorial model    | Compact editor-final model; live-check names | Editor + AEs                 | Senior + area editors        | Editors + AEs                |

If your paper is normative, behavioral-experimental, or has little accounting content, JAE is the wrong venue.

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — index of journal-specific skill packs

---

## License

MIT
