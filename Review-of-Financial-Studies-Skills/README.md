# RFS Skills

<p align="center">
  <img src="assets/cover.svg" alt="The Review of Financial Studies cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Review%20of%20Financial%20Studies-1b2a4a)](https://academic.oup.com/rfs)
[![Index](https://img.shields.io/badge/index-SSCI%20%7C%20top--3%20finance-1f6feb)](https://academic.oup.com/rfs)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **The Review of Financial Studies (RFS)** — published by Oxford University Press for the Society for Financial Studies (SFS), and one of the "top-3" finance journals alongside the *Journal of Finance* and the *Journal of Financial Economics*.

This repository is opinionated. It is **not** a generic finance-writing toolbox. It is an **RFS-specific** stack built around the journal's governing tension — **novelty AND rigor** — covering novel-question topic selection, literature positioning, causal and asset-pricing identification, empirical/structural design, robustness and multiple-testing discipline, publication-grade exhibits, the journal-hosted Internet Appendix, house style, ScholarOne submission, referee strategy, and multi-round rebuttals.

---

## Why a Separate RFS Skill Stack?

RFS shares JF/JFE's high causal-inference bar but adds constraints of its own:

| Constraint                | The Review of Financial Studies                                  | Implication                                                  |
|---------------------------|-------------------------------------------------------------------|--------------------------------------------------------------|
| Discipline                | Finance (asset pricing, corporate, household, fintech, climate)   | Pure non-finance or undertheorized papers are off-fit        |
| Core test                 | **Novelty AND rigor** — both, simultaneously                      | A clean but "me-too" paper is a weak fit; so is novelty alone |
| Receptivity to new work   | Notably open to new questions, data, methods, and theory+empirics | Genuinely new framings are rewarded, not penalized           |
| Identification            | Same causal-inference bar as JF/JFE (natural experiments, IV, RDD, modern DID) | OLS + controls on a causal claim is a desk-reject risk |
| Asset pricing             | Correct/clustered SEs, OOS tests, multiple-testing discipline     | A new predictor without data-mining defense is rejected      |
| Theory + empirics         | Welcomed and expected to be integrated                            | A model and an unrelated regression read as two papers       |
| Internet Appendix         | Journal-hosted; refereed alongside the paper                      | Robustness/proofs/data detail belong there, cross-referenced |
| Process                   | ScholarOne / Manuscript Central; fee + SFS norms; multi-round     | Demanding revision; verify current fee/policy on the RFS site |

Generic "scientific writing" or "finance writing" packs do not address these constraints.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/rfs-skills
/plugin install rfs-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/rfs-skills.git
cd rfs-skills

mkdir -p ~/.claude/skills && cp -R skills/rfs-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/rfs-* ~/.codex/skills/
```

### First Prompt

```
Use rfs-workflow to tell me which skill I should use next for my RFS manuscript.
```

---

## Default Workflow

```text
rfs-topic-selection
        ▼
rfs-literature-positioning
        ▼
rfs-identification
        ▼
rfs-empirical-design
        ▼
rfs-robustness
        ▼
rfs-tables-figures
        ▼
rfs-internet-appendix
        ▼
rfs-writing-style       (polish)
        ▼
rfs-submission
        ▼
rfs-referee-strategy
        ▼
rfs-rebuttal
```

`rfs-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill                         | Purpose                                                              |
|-------------------------------|----------------------------------------------------------------------|
| `rfs-workflow`                | Router — decides which sub-skill to invoke next                      |
| `rfs-topic-selection`         | Novelty-plus-rigor fit test + contribution-claim template            |
| `rfs-literature-positioning`  | Define the precise delta vs. JF/JFE/RFS and prior work               |
| `rfs-identification`          | Causal & asset-pricing identification (DID / IV / RDD / event study) |
| `rfs-empirical-design`        | Sample construction, estimators, factor/structural design            |
| `rfs-robustness`              | Fragility battery + multiple-testing / out-of-sample discipline      |
| `rfs-tables-figures`          | Self-contained tables, SE reporting, event-study figures             |
| `rfs-internet-appendix`       | What lives in the journal-hosted IA vs. the main paper               |
| `rfs-writing-style`           | Contribution framing + prose polish (novelty legible early)          |
| `rfs-submission`              | ScholarOne preflight + cover letter + manuscript template            |
| `rfs-referee-strategy`        | Suggested/opposed referees + objection pre-mortem                    |
| `rfs-rebuttal`                | Multi-round R&R response-letter structure                            |

### Resources

- [`skills/rfs-submission/templates/manuscript_template.md`](skills/rfs-submission/templates/manuscript_template.md) — RFS-style manuscript skeleton (abstract, sections, variable table, references, Internet Appendix, cover letter)
- [`skills/rfs-submission/templates/checklist.md`](skills/rfs-submission/templates/checklist.md) — 8-section pre-submission self-check
- [`resources/external_tools.md`](resources/external_tools.md) — finance data sources (CRSP / Compustat / TAQ / WRDS / OptionMetrics) + Stata / R / Python packages

---

## Differences vs. JF / JFE Skills

| Dimension            | Review of Financial Studies          | Journal of Finance / JFE                  |
|----------------------|--------------------------------------|-------------------------------------------|
| Identification bar   | Top-3 causal-inference standard      | Top-3 causal-inference standard           |
| Novelty receptivity  | **Especially open** to new questions/data/methods | Open, but RFS most explicitly rewards it |
| Theory + empirics    | Integrated structural/theory welcomed | Welcomed (JFE), strong at JF too         |
| House quirk          | Journal-hosted Internet Appendix is central | Similar; details differ per journal |
| Distinctive risk     | "Rigorous but not novel" me-too paper | Same family of risks                      |

These three journals overlap heavily; this stack is tuned to the RFS lever — novelty made credible.

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Journal-of-Finance-Skills](https://github.com/brycewang-stanford/journal-of-finance-skills) — *Journal of Finance*
- [Economic-Research-Journal-Skills](https://github.com/brycewang-stanford/economic-research-skills) — 《经济研究》

---

## License

MIT
