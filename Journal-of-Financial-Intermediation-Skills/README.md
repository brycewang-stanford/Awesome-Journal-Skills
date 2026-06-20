# Journal of Financial Intermediation Skills

<p align="center">
  <img src="assets/cover.svg" alt="Journal of Financial Intermediation cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-JFI-0b3d6b)](https://www.sciencedirect.com/journal/journal-of-financial-intermediation)
[![Field](https://img.shields.io/badge/field-Banking%20%26%20Intermediation-1f6feb)](https://www.sciencedirect.com/journal/journal-of-financial-intermediation)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at the **Journal of Financial Intermediation (JFI)** — an
Elsevier journal (ISSN 1042-9573) on **banking, financial intermediation, and the economics of financial
institutions and markets**, publishing both **theory** and **empirics** on banks, intermediaries,
corporate finance, regulation, and related financial-economics topics.

This repository is opinionated. It is **not** a generic finance-writing toolbox. It is a **JFI-specific**
stack built around the journal's real process: a US$500 non-refundable submission fee paid in **Editorial
Manager** before a paper is considered, an **active desk-rejection** policy, **single-anonymized
(single-blind)** review with at least one expert referee when sent out and a tightly limited appeal path, optional
free **SSRN preprint** posting, "your-paper-your-way" submission with an **author–date Elsevier** reference
style applied at proof, a **250-word abstract cap**, **1-7 English keywords**, optional Highlights,
Elsevier **Option C** research-data deposit / citation / link-or-explain rules, and a mandatory
**generative-AI disclosure**.

---

## Why a Separate JFI Skill Stack?

JFI imposes constraints that differ materially from a top-5 general-interest journal or a methods journal:

| Constraint           | JFI                                                                         | Implication                                                        |
|----------------------|-----------------------------------------------------------------------------|--------------------------------------------------------------------|
| Audience / scope     | Banking & financial intermediation specialists; theory **and** empirics     | A paper with no intermediation mechanism is off-fit                |
| Submission fee       | **US$500**, paid in Editorial Manager **before** review, non-refundable on desk-reject | Budget for it; pay before the editor will even consider the paper  |
| Screening            | **Active desk-rejection**; usually at least one expert referee if sent out; one appeal may be considered | A clean first screen matters; appeal is not a normal revision plan |
| Review model         | **Single-anonymized (single-blind)** — referees see your identity           | Anonymizing the body is not required (unlike double-blind venues)  |
| Preprints            | Free **SSRN** posting offered at submission; not prior publication          | You can circulate openly without prejudicing the outcome           |
| Submission metadata  | Abstract **<=250 words**, **1-7 English keywords**, optional Highlights     | The desk screen starts with concise metadata, not a long abstract  |
| Formatting           | "Your-paper-your-way"; **author–date** Elsevier style applied at proof      | Any consistent style at submission; clean author–year fields       |
| Data                 | Elsevier **Option C** deposit/cite/link-or-explain policy + Data Statement; `[dataset]` tag | No JAE/AER-style archive, but the data-sharing plan must be explicit |
| AI disclosure        | Mandatory declaration before the References                                  | Undisclosed generative-AI use is a compliance failure              |

Generic "finance writing" packs do not address these constraints. Volatile specifics (fees, editor roster,
open-access charges, and special calls) can change — **verify them on the official journal page**. Current
official basis was refreshed on 2026-06-20 in the source map.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/jfi-skills
/plugin install jfi-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/jfi-skills.git
cd jfi-skills

mkdir -p ~/.claude/skills && cp -R skills/jfi-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/jfi-* ~/.codex/skills/
```

### First Prompt

```
Use jfi-workflow to tell me which skill I should use next for my JFI manuscript.
```

---

## Default Workflow

```text
jfi-topic-selection
        ▼
jfi-literature-positioning
        ▼
jfi-identification-strategy
        ▼
jfi-data-analysis
        ▼
jfi-contribution-framing
        ▼
jfi-tables-figures
        ▼
jfi-writing-style          (polish)
        ▼
jfi-replication-and-data-policy
        ▼
jfi-review-process
        ▼
jfi-submission
        ▼
jfi-rebuttal
```

`jfi-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill                              | Purpose                                                                       |
|------------------------------------|-------------------------------------------------------------------------------|
| `jfi-workflow`                     | Router — decides which sub-skill to invoke next                               |
| `jfi-topic-selection`              | Banking / intermediation fit; theory-vs-empirics framing                      |
| `jfi-literature-positioning`       | Stake the contribution against the intermediation frontier                    |
| `jfi-identification-strategy`      | Causal design for banking empirics; assumptions/proof exposition for theory   |
| `jfi-data-analysis`                | Bank/loan-level panel analysis; numerical examples for theory papers          |
| `jfi-contribution-framing`         | Frame the mechanism and "why intermediaries matter" lesson                    |
| `jfi-tables-figures`               | Numbered exhibits with self-contained notes                                   |
| `jfi-writing-style`                | Author–date Elsevier style; numbered sections; make the mechanism land        |
| `jfi-replication-and-data-policy`  | Elsevier Option C, Data Statement, repository links, `[dataset]` tag          |
| `jfi-review-process`               | Single-blind, desk-reject, one-referee, limited-appeal realities             |
| `jfi-submission`                   | Editorial Manager preflight + US$500 fee + abstract/keywords + AI disclosure |
| `jfi-rebuttal`                     | Response-letter strategy when the editor and expert referee drive the outcome |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — bank/supervisory data (Call Reports, FDIC, DealScan, HMDA) + Stata / R / Python packages for banking empirics and theory toolkits
- [`resources/official-source-map.md`](resources/official-source-map.md) — official JFI URLs behind every current process fact, refreshed 2026-06-20

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate any specific editor's or referee's taste
- It does not freeze volatile metadata such as fees, editors, APCs, or special calls; re-check the official
  page before submission-ready advice
- It does not judge whether your contribution is genuinely original — that is the researcher's call

---

## Maintenance notes

- Reopen the live Guide for Authors before giving submission-ready advice.
- Re-check the editorial-board page before naming a Managing Editor or Co-Editor in a cover letter.
- Fees, editors, data policy, review model, and formatting rules can change.

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Journal of Financial Intermediation (official)](https://www.sciencedirect.com/journal/journal-of-financial-intermediation) — Elsevier

---

## License

MIT
