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
(single-blind)** review with a minimum of one expert referee and a **final** editorial decision, optional
free **SSRN preprint** posting, "your-paper-your-way" submission with an **author–date Elsevier** reference
style applied at proof, **up to 6 JEL codes** and a max of **6 keywords**, Elsevier **data-sharing** and
**Data Statement** norms, and a mandatory **generative-AI disclosure**.

---

## Why a Separate JFI Skill Stack?

JFI imposes constraints that differ materially from a top-5 general-interest journal or a methods journal:

| Constraint           | JFI                                                                         | Implication                                                        |
|----------------------|-----------------------------------------------------------------------------|--------------------------------------------------------------------|
| Audience / scope     | Banking & financial intermediation specialists; theory **and** empirics     | A paper with no intermediation mechanism is off-fit                |
| Submission fee       | **US$500**, paid in Editorial Manager **before** review, non-refundable on desk-reject | Budget for it; pay before the editor will even consider the paper  |
| Screening            | **Active desk-rejection**; min. one expert referee; editor's decision **final** | A clean first screen matters; there is no appeal                   |
| Review model         | **Single-anonymized (single-blind)** — referees see your identity           | Anonymizing the body is not required (unlike double-blind venues)  |
| Preprints            | Free **SSRN** posting offered at submission; not prior publication          | You can circulate openly without prejudicing the outcome           |
| Classification       | **Up to 6 JEL codes** + max **6 keywords**                                   | An economics-discipline convention many finance authors miss       |
| Formatting           | "Your-paper-your-way"; **author–date** Elsevier style applied at proof      | Any consistent style at submission; clean author–year fields       |
| Data                 | Elsevier **data-sharing** + published **Data Statement**; `[dataset]` tag    | No JAE/AER-style mandatory code archive, but sharing is expected   |
| AI disclosure        | Mandatory declaration before the References                                  | Undisclosed generative-AI use is a compliance failure              |

Generic "finance writing" packs do not address these constraints. Volatile specifics (current editors,
exact fee amount, length caps) change or could not be confirmed from a dated official source — **verify
them on the official journal page**. Items we could not confirm are marked **待核实** in the source map.

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
| `jfi-replication-and-data-policy`  | Elsevier data-sharing, Data Statement, `[dataset]` tag                        |
| `jfi-review-process`               | Single-blind, desk-reject, one-referee, final-decision realities             |
| `jfi-submission`                   | Editorial Manager preflight + the US$500 fee + JEL/keywords + AI disclosure   |
| `jfi-rebuttal`                     | Response-letter strategy under a final, unappealable decision                 |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — bank/supervisory data (Call Reports, FDIC, DealScan, HMDA) + Stata / R / Python packages for banking empirics and theory toolkits
- [`resources/official-source-map.md`](resources/official-source-map.md) — official JFI URLs behind every fact, with accessed dates and **待核实** flags

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate any specific editor's or referee's taste
- It does not assert volatile metadata (current Editor-in-Chief, exact fee amount, length caps) — these are
  marked **待核实** and must be verified on the official page
- It does not judge whether your contribution is genuinely original — that is the researcher's call

---

## Maintenance notes

- Reopen the live Guide for Authors before giving submission-ready advice.
- Keep source-map **待核实** items out of hard claims (fee amount, current editors, length/abstract caps).
- Fees, editors, data policy, review model, and formatting rules can change.

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Journal of Financial Intermediation (official)](https://www.sciencedirect.com/journal/journal-of-financial-intermediation) — Elsevier

---

## License

MIT
