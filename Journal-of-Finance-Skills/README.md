# Journal of Finance Skills

<p align="center">
  <img src="assets/cover.svg" alt="The Journal of Finance cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Journal%20of%20Finance-0b3d5c)](https://afajof.org/)
[![Index](https://img.shields.io/badge/index-SSCI-1f6feb)](https://afajof.org/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **The Journal of Finance (JF)** — the American Finance Association's (AFA) flagship **general-interest** finance journal, published by Wiley.

This repository is opinionated. It is **not** a generic finance-writing toolbox. It is a **JF-specific** stack covering general-interest topic selection, literature positioning, causal identification (corporate/empirical) and asset-pricing test design, robustness with multiple-testing discipline, the journal-hosted Internet Appendix, accessible exposition, submission via Manuscript Central / ScholarOne, the demanding multi-round referee process, and R&R rebuttals.

> Accuracy note: this pack describes **durable norms**, not volatile specifics. Always verify the current submission fee, AFA-membership rule, editor masthead, and formatting limits on the official JF / AFA author pages.

---

## Why a Separate Journal-of-Finance Skill Stack?

JF imposes constraints that differ materially from JFE, RFS, and field journals:

| Constraint              | The Journal of Finance                                              | Implication                                                  |
|-------------------------|--------------------------------------------------------------------|--------------------------------------------------------------|
| Audience                | Broad AFA readership across all areas of finance                   | Subfield-only papers are screened out; general interest is the gate |
| Scope                   | Asset pricing, corporate, microstructure, banking, household, international | Method-only or pure-theory papers often fit JFE/RFS better |
| Contribution            | Important, broadly interesting question + economic significance    | Statistical significance alone does not clear the bar         |
| Identification (corp.)  | Natural experiments, IV with defended exclusion, modern DID, RDD   | OLS + controls with unaddressed endogeneity is a red flag     |
| Test design (asset pr.) | Factor models, Fama–MacBeth/panel, correct SEs, multiple-testing   | Naive t > 2 from a signal search is treated as data mining    |
| Length & style          | Somewhat shorter, accessible; depth moves to the Internet Appendix | Long, technical papers that bury the result draw complaints   |
| Internet Appendix       | Journal-hosted; proofs and extra tables live online                | The main text stays focused; appendix items must be cited     |
| Process                 | Manuscript Central / ScholarOne; fee + AFA-membership norms        | Verify current fee/membership; expect multi-round review      |

Generic "scientific writing" or "economics writing" packs do not address these constraints.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/jf-skills
/plugin install jf-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/jf-skills.git
cd jf-skills

mkdir -p ~/.claude/skills && cp -R skills/jf-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/jf-* ~/.codex/skills/
```

### First Prompt

```
Use jf-workflow to tell me which skill I should use next for my Journal-of-Finance manuscript.
```

---

## Default Workflow

```text
jf-topic-selection
        ▼
jf-literature-positioning
        ▼
jf-identification        (corporate / empirical branch)
   or jf-empirical-design (asset-pricing branch)
        ▼
jf-robustness
        ▼
jf-tables-figures
        ▼
jf-internet-appendix
        ▼
jf-writing-style         (polish)
        ▼
jf-submission
        ▼
jf-referee-strategy
        ▼
jf-rebuttal
```

`jf-workflow` is the router — it tells you which skill to use next based on where you are. `jf-identification` and `jf-empirical-design` are branch siblings: the first for corporate/empirical causal claims, the second for asset-pricing tests.

---

## Skills

| Skill                        | Purpose                                                              |
|------------------------------|----------------------------------------------------------------------|
| `jf-workflow`                | Router — decides which sub-skill to invoke next                      |
| `jf-topic-selection`         | General-interest fit + economic-significance framing                 |
| `jf-literature-positioning`  | Marginal-contribution positioning against the finance literature      |
| `jf-identification`          | Causal identification (natural experiment / IV / DID / RDD)          |
| `jf-empirical-design`        | Asset-pricing test design (factors, Fama–MacBeth, SE corrections)    |
| `jf-robustness`              | Robustness battery + multiple-testing / out-of-sample discipline     |
| `jf-tables-figures`          | Clean, self-contained, publication-grade exhibits                    |
| `jf-internet-appendix`       | What lives online vs. in the main text; appendix structure           |
| `jf-writing-style`           | Accessible, general-interest exposition; lead with magnitude          |
| `jf-submission`              | Pre-submission preflight (portal, fee/membership, formatting, statements) |
| `jf-referee-strategy`        | Anticipate referee objections; suggested/opposed reviewers           |
| `jf-rebuttal`                | R&R response-letter structure and revision plan                      |

### Resources

- [`skills/jf-submission/templates/manuscript_template.md`](skills/jf-submission/templates/manuscript_template.md) — JF-oriented manuscript skeleton (title page, body, Internet Appendix, references)
- [`skills/jf-submission/templates/checklist.md`](skills/jf-submission/templates/checklist.md) — 8-section pre-submission self-check
- [`resources/external_tools.md`](resources/external_tools.md) — Empirical-finance data sources (CRSP / Compustat / TAQ / WRDS / Refinitiv) + Stata / R / Python packages

---

## Differences vs. JFE / RFS

| Dimension          | Journal of Finance              | JFE                              | RFS                               |
|--------------------|---------------------------------|----------------------------------|-----------------------------------|
| Emphasis           | General interest, accessibility | Depth, methodological heft       | Theory framing + mechanism        |
| Article length     | Somewhat shorter; depth online  | Tolerates longer, technical      | Often theory-anchored             |
| Best fit           | Broadly interesting finding     | Specialist, methods-heavy paper  | Structural / mechanism contribution |
| Technical detail   | Pushed to the Internet Appendix | More in the main text            | Model-driven                      |

If your paper is long, highly technical, or specialist, JFE or RFS may be the better home.

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Economic-Research-Journal-Skills](https://github.com/brycewang-stanford/economic-research-skills) — 《经济研究》

---

## License

MIT
