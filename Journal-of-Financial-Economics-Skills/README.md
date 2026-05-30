# JFE Skills

<p align="center">
  <img src="assets/cover.svg" alt="Journal of Financial Economics cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Journal%20of%20Financial%20Economics-c0392b)](https://www.journals.elsevier.com/journal-of-financial-economics)
[![Index](https://img.shields.io/badge/index-SSCI%20%2F%20Top--3%20Finance-1f6feb)](https://www.journals.elsevier.com/journal-of-financial-economics)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at the **Journal of Financial Economics (JFE)** — published by Elsevier and one of the "top-3" finance journals, known for rigorous, methodologically demanding empirical corporate finance and asset pricing.

This repository is opinionated. It is **not** a generic finance-writing toolbox. It is a **JFE-specific** stack covering topic fit, literature positioning, credible identification, the nuts-and-bolts empirical design JFE is famous for, an exhaustive robustness battery, exhibit craft, the journal-hosted Internet Appendix, house writing style, submission, referee strategy, and R&R rebuttals.

> JFE volatile specifics — current editors, the exact submission fee, the impact factor, and the precise data-availability and anonymity rules — change over time. This pack describes durable norms and tells you to verify the specifics on the journal's official page.

---

## Why a Separate JFE Skill Stack?

JFE imposes constraints that differ materially from JF and RFS, even though all three are top-3 finance journals:

| Constraint              | Journal of Financial Economics                                  | Implication                                                  |
|-------------------------|------------------------------------------------------------------|--------------------------------------------------------------|
| Discipline              | Empirical corporate finance & asset pricing (plus supporting theory) | Pure theory with thin empirics is a harder sell             |
| Methodological bar      | Nuts-and-bolts rigor; technical, line-by-line scrutiny           | Sloppy measurement or estimation is fatal                    |
| Identification          | Natural experiments, IV, staggered DID, RDD; explicit endogeneity | "OLS + controls" rarely carries the headline                 |
| Robustness              | Exhaustive; every alternative explanation ruled out              | A fragile result is a classic rejection                      |
| Inference (asset pricing) | Correct/clustered SEs, out-of-sample, multiple-testing discipline | A factor ignoring multiple testing is a red flag             |
| Internet Appendix       | Journal-hosted; deep — proofs and robustness live there          | A thin appendix signals thin robustness                      |
| Length / depth          | Typically longer and more robustness-heavy than JF               | Expect a full, demanding structure                           |
| Review process          | Multiple demanding rounds; thorough referees                     | The response letter is judged almost as closely as the paper |

Generic "scientific writing" or "finance writing" skill packs do not address these constraints.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/jfe-skills
/plugin install jfe-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/jfe-skills.git
cd jfe-skills

mkdir -p ~/.claude/skills && cp -R skills/jfe-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/jfe-* ~/.codex/skills/
```

### First Prompt

```
Use jfe-workflow to tell me which skill I should use next for my JFE manuscript.
```

---

## Default Workflow

```text
jfe-topic-selection
        ▼
jfe-literature-positioning
        ▼
jfe-identification
        ▼
jfe-empirical-design
        ▼
jfe-robustness
        ▼
jfe-tables-figures
        ▼
jfe-internet-appendix
        ▼
jfe-writing-style       (polish)
        ▼
jfe-submission
        ▼
jfe-referee-strategy
        ▼
jfe-rebuttal
```

`jfe-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill                        | Purpose                                                              |
|------------------------------|----------------------------------------------------------------------|
| `jfe-workflow`               | Router — decides which sub-skill to invoke next                      |
| `jfe-topic-selection`        | Contribution and economic-question fit test                          |
| `jfe-literature-positioning` | Positioning against the top-3 finance frontier                       |
| `jfe-identification`         | Credible causal design (natural experiments, IV, staggered DID, RDD) |
| `jfe-empirical-design`       | Factor construction, Fama–MacBeth/GMM, clustered SEs, multiple testing |
| `jfe-robustness`             | The exhaustive robustness battery JFE is known for                   |
| `jfe-tables-figures`         | Readable, self-contained exhibits in house style                     |
| `jfe-internet-appendix`      | Journal-hosted appendix: proofs, robustness, supplementary tests     |
| `jfe-writing-style`          | Precise, evidence-forward prose; no overclaiming                     |
| `jfe-submission`             | Pre-submission preflight + manuscript template                       |
| `jfe-referee-strategy`       | Anticipate and pre-empt referee objections                           |
| `jfe-rebuttal`               | R&R response-letter structure for demanding rounds                   |

### Resources

- [`skills/jfe-submission/templates/manuscript_template.md`](skills/jfe-submission/templates/manuscript_template.md) — JFE-style manuscript skeleton (abstract, variable-definition table, exhibit and reference conventions)
- [`skills/jfe-submission/templates/checklist.md`](skills/jfe-submission/templates/checklist.md) — 8-section pre-submission self-check
- [`resources/external_tools.md`](resources/external_tools.md) — finance data sources (CRSP / Compustat / TAQ / IBES / Dealscan via WRDS) + Stata / R / Python packages

---

## Differences vs. JF and RFS Skills

| Dimension          | Journal of Financial Economics       | Journal of Finance (JF)            | Review of Financial Studies (RFS) |
|--------------------|--------------------------------------|------------------------------------|-----------------------------------|
| Emphasis           | Methodological rigor + robustness    | A clean, idea-forward result       | Theory + methodology depth        |
| Typical length     | Longer, robustness-heavy             | Often tighter                      | Variable                          |
| Internet Appendix  | Deep, expected                       | Used                               | Used                              |
| Best fit           | Exhaustively-stress-tested empirics  | A single decisive finding          | Method/theory contributions       |

Confirm each journal's current scope on its official page before choosing a target.

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate a specific editor's preferences
- It does not store JFE's rejection rate, impact factor, or current fee — verify those on the official page
- It does not judge whether your contribution is genuinely novel — that is your call

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Journal of Finance Skills](https://github.com/brycewang-stanford/journal-of-finance-skills) — JF
- [Review of Financial Studies Skills](https://github.com/brycewang-stanford/rfs-skills) — RFS

---

## License

MIT
