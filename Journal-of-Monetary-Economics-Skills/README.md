# Journal of Monetary Economics Skills

<p align="center">
  <img src="assets/cover.svg" alt="Journal of Monetary Economics cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-JME-13315c)](https://www.sciencedirect.com/journal/journal-of-monetary-economics)
[![Field](https://img.shields.io/badge/field-Monetary%20%26%20Macro-1f6feb)](https://www.sciencedirect.com/journal/journal-of-monetary-economics)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at the **Journal of Monetary Economics (JME)** — Elsevier's leading outlet for **monetary economics and macroeconomics broadly defined**: monetary theory and policy, central banking, business cycles, growth, financial markets and intermediation, fiscal–monetary interactions, expectations, and the macroeconomic effects of money and finance. JME publishes both theoretical and empirical work, including DSGE / quantitative macro and applied policy analysis, and dedicates **one issue each year to the Carnegie-Rochester-NYU Conference Series on Public Policy** (plus a periodic Swiss National Bank Study Center Gerzensee macro-policy issue).

This repository is opinionated. It is **not** a generic economics-writing toolbox. It is a **JME-specific** stack built around the journal's real constraints: an up-front submission fee, single-anonymized review, a strict length cap, a distinctive "up or out" first revision, and a ScienceDirect/Mendeley supplementary-materials policy.

---

## Why a Separate JME Skill Stack?

JME imposes constraints that differ materially from a generalist top-5 journal or a methods journal:

| Constraint              | JME                                                                          | Implication                                                          |
|-------------------------|------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Scope                   | Monetary economics & macro, broadly defined                                  | A pure micro estimate with no aggregation is off-fit                |
| Mode                    | Theoretical **and** empirical (DSGE / quantitative / applied policy)          | Both a clean model and a credibly identified shock are welcome      |
| Submission system       | Elsevier **Editorial Manager** (`editorialmanager.com/monec/`)               | Not a generic econ portal                                           |
| Submission fee          | **US$350** (US$200 full-time PhD), paid **up front**; half refunded on direct return | A manuscript is only considered after payment                       |
| Review model            | **Single anonymized** (single-blind), **≥ 2 reviewers**                       | Do **not** anonymize — referees know who you are                    |
| First revision          | **"Up or out"** — resubmission ends in accept or reject, no second R&R        | One revision must fully resolve every concern                       |
| R&R signal              | Invited only at **~50%** publication likelihood                              | An R&R is a strong (not guaranteed) signal                          |
| Length cap (accepted)   | **≤ 40 pages** text/refs/footnotes, **≤ 10 tables and figures** combined      | Push robustness to the online supplement (exempt)                   |
| Abstract                | **≤ 100 words**, may **not** start with "This paper" or "We"                  | Open with the finding or the question                               |
| References              | Author-date; journal titles **spelled out in full**; list after appendices    | Numbered/abbreviated styles read as off-template                    |
| Identification          | Identified shocks (high-frequency, narrative, proxy-SVAR, LP) or model-based  | A raw policy-rate change with no exogeneity argument fails          |
| Data policy             | Deposit data/code/appendices on **ScienceDirect / Mendeley Data**; AI declaration required | Editor may require materials as a condition of publication          |

Editors are **S. Borağan Aruoba** (University of Maryland) and **Eric Swanson** (University of California, Irvine; identified as editor-in-chief in Elsevier's editor interview). Generic "scientific writing" or "econ writing" packs do not address these constraints. Volatile specifics (editors, fee, page cap, policy wording) change — **verify them on the official journal page** (see [`resources/official-source-map.md`](resources/official-source-map.md)).

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/jme-skills
/plugin install jme-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/jme-skills.git
cd jme-skills

mkdir -p ~/.claude/skills && cp -R skills/jme-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/jme-* ~/.codex/skills/
```

### First Prompt

```
Use jme-workflow to tell me which skill I should use next for my JME manuscript.
```

---

## Default Workflow

```text
jme-topic-selection
        ▼
jme-literature-positioning
        ▼
jme-contribution-framing
        ▼
jme-identification-strategy
        ▼
jme-data-analysis
        ▼
jme-tables-figures
        ▼
jme-writing-style            (polish)
        ▼
jme-replication-and-data-policy
        ▼
jme-review-process
        ▼
jme-submission
        ▼
jme-rebuttal                 (the "up or out" revision)
```

`jme-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill                             | Purpose                                                                       |
|-----------------------------------|-------------------------------------------------------------------------------|
| `jme-workflow`                    | Router — decides which sub-skill to invoke next                              |
| `jme-topic-selection`             | Monetary-macro scope fit + the policy/conceptual payoff bar                   |
| `jme-literature-positioning`      | Stake the contribution against the monetary-macro frontier                    |
| `jme-contribution-framing`        | Sharpen the "what's new + policy lesson" claim for the ~50% R&R bar           |
| `jme-identification-strategy`     | Credible shock/mechanism identification (HF, narrative, proxy-SVAR, LP, model)|
| `jme-data-analysis`               | VAR / SVAR / local projections / DSGE estimation, IRFs, FEVDs, robustness      |
| `jme-tables-figures`              | Fit exhibits under the ≤10 cap; route the rest to the online supplement        |
| `jme-writing-style`               | JME house style — 100-word abstract, author-date refs, line numbers, JEL codes |
| `jme-replication-and-data-policy` | ScienceDirect / Mendeley deposit + Elsevier generative-AI declaration          |
| `jme-review-process`              | Single-blind, two-referee, "up or out", ~50% threshold, fee mechanics          |
| `jme-submission`                  | Editorial Manager preflight (fee, 40 pages, line numbers, JEL codes)           |
| `jme-rebuttal`                    | The single "up or out" R&R response-letter strategy                            |

### Resources

- [`resources/official-source-map.md`](resources/official-source-map.md) — official JME / Elsevier URLs behind every fact in this pack (accessed 2026-06-01), with unverified items marked **待核实**
- [`resources/external_tools.md`](resources/external_tools.md) — macro/monetary data sources (FRED, BIS, ECB, real-time data) and software (Dynare, MATLAB/Julia, Stata `lpirf`, R `lpirfs`/`vars`) for VAR/LP/DSGE work

---

## Differences vs. Other Top Journals

| Dimension          | JME                                       | Quarterly Journal of Economics        | Econometrica                  |
|--------------------|-------------------------------------------|---------------------------------------|-------------------------------|
| Lead with          | A monetary/macro shock or mechanism       | A big empirical-micro question        | A method / theorem            |
| Identification     | HF surprises / narrative / SVAR / LP / model | Natural experiment, figure-forward  | Estimator properties          |
| Review model       | Single-blind, "up or out"                 | Double-blind, few rounds              | Single/double-blind, slow     |
| Length             | Hard 40-page / ≤10 exhibit cap            | No hard cap, extensive appendix       | No hard cap                   |
| Fee                | US$350 up front (US$200 PhD)              | No submission fee                     | Submission fee                |

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate any specific editor's or referee's taste
- It does not assert volatile metadata (current editors, exact fee, deposit rules) — verify on the official page
- It does not claim a formal AEA/Econometrica-style mandatory replication-verification gate exists at JME (that is **待核实**; the confirmed policy is a deposit recommendation plus editor discretion)

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Quarterly-Journal-of-Economics-Skills](https://github.com/brycewang-stanford/qje-skills) — QJE pack
- [Journal of Monetary Economics (official)](https://www.sciencedirect.com/journal/journal-of-monetary-economics) — Elsevier / ScienceDirect

---

## License

MIT
