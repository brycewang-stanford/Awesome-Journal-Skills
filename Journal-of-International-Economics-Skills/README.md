# Journal of International Economics Skills

<p align="center">
  <img src="assets/cover.svg" alt="Journal of International Economics cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-JIE-13386b)](https://www.sciencedirect.com/journal/journal-of-international-economics)
[![Field](https://img.shields.io/badge/field-International%20Economics-1f6feb)](https://www.sciencedirect.com/journal/journal-of-international-economics)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at the **Journal of International Economics (JIE)** — published by **Elsevier**, the leading field journal spanning **both international trade and international macroeconomics/finance**. Its scope covers trade patterns and commercial policy, international institutions, exchange rates, open-economy macroeconomics, country/regional growth and development, international finance, international pricing, sovereign debt, international factor mobility, spatial economics, and international monetary and fiscal theory and policy. JIE publishes both empirical and theoretical work, which must be **original in its motivation or modelling structure**.

This repository is opinionated. It is **not** a generic economics-writing toolbox. It is a **JIE-specific** stack built around the two halves of the field — gravity/structural trade and open-economy macro/finance — and around JIE's actual process: a non-refundable submission fee, the expedited Prior Review Process, a 150-word abstract, and mandatory deposit of replication code and data in the journal's secure repository.

---

## Why a Separate JIE Skill Stack?

JIE imposes constraints that differ materially from a general-interest top-5 journal or a methods journal:

| Constraint              | JIE                                                                              | Implication                                                       |
|-------------------------|----------------------------------------------------------------------------------|------------------------------------------------------------------|
| Audience                | International economists — trade **and** international macro/finance              | The paper must speak to one of these two halves clearly          |
| Originality gate        | Original in **motivation or modelling structure**                                | A re-run of a known design on new data is off-fit                |
| Submission system       | **Editorial Manager** (Elsevier)                                                 | Not Editorial Express / ScholarOne — different upload flow       |
| Submission fee          | **USD 190 / EUR 169.20 / JPY 20,660** (USD 95 if all authors are PhD students)   | Budget for it; VAT added for relevant European authors           |
| Expedited path          | **Prior Review Process (PRP)** carrying AER/Econometrica/JPE/QJE/REStud letters+reports | Select 'PRP' as Article Type; no extra fee                       |
| Submission types        | Regular, **Short Paper** (≤6,000 words, ≤5 exhibits), or PRP                     | Pick the type that fits the contribution                         |
| Review model            | **Single anonymized**; suitable manuscripts typically go to at least two reviewers | Calibrate expectations before first submission                   |
| Abstract                | **≤ 150 words**, factual, single paragraph, references avoided                    | A long, citation-heavy abstract is off-template                  |
| Keywords                | **1-7 keywords**                                                                  | Choose field-discoverable terms                                  |
| References              | Elsevier applies the journal style **at proof** — submit in any consistent style | Required elements must be present; DOIs encouraged               |
| Data / code             | **Mandatory deposit** of programs and data in the JIE secure repository           | Build the Mendeley Data package as you go                        |
| Editor fit              | Suggest an **Editor or Co-Editor** whose profile matches the paper                 | Trade vs macro/finance routing matters                          |

Acceptance for regular submissions has historically run ~10-15%, with desk rejects around 25% (per Editor Costas Arkolakis's site). The official Guide for Authors and editorial-board pages were refreshed on 2026-06-20 for this pack; still verify fee amounts, editor roster, and portal links on the live pages before upload.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/jie-skills
/plugin install jie-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/jie-skills.git
cd jie-skills

mkdir -p ~/.claude/skills && cp -R skills/jie-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/jie-* ~/.codex/skills/
```

### First Prompt

```
Use jie-workflow to tell me which skill I should use next for my JIE manuscript.
```

---

## Default Workflow

```text
jie-topic-selection
        ▼
jie-literature-positioning
        ▼
jie-identification-strategy
        ▼
jie-data-analysis
        ▼
jie-contribution-framing
        ▼
jie-tables-figures
        ▼
jie-writing-style          (polish)
        ▼
jie-replication-and-data-policy
        ▼
jie-review-process
        ▼
jie-submission
        ▼
jie-rebuttal
```

`jie-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill                              | Purpose                                                                       |
|------------------------------------|-------------------------------------------------------------------------------|
| `jie-workflow`                     | Router — decides which sub-skill to invoke next                               |
| `jie-topic-selection`              | Fit to JIE's trade / macro-finance scope + the originality gate               |
| `jie-literature-positioning`       | Stake the contribution against the trade or open-economy frontier             |
| `jie-identification-strategy`      | Credible identification for trade (gravity, policy shocks) & open-economy macro |
| `jie-data-analysis`                | Empirical norms: PPML gravity, panels, structural estimation, robustness        |
| `jie-contribution-framing`         | Frame originality of motivation or modelling structure for the JIE audience    |
| `jie-tables-figures`               | Trade/macro exhibits with self-contained notes                                 |
| `jie-writing-style`                | JIE house style; 150-word abstract; theory + empirics balance                  |
| `jie-replication-and-data-policy`  | Mandatory code + data deposit in the JIE secure repository (Mendeley Data)      |
| `jie-review-process`               | How JIE handling, refereeing, and the PRP expedite option work                 |
| `jie-submission`                   | Editorial Manager preflight: fee, abstract, keywords, Article Type, editor fit  |
| `jie-rebuttal`                     | R&R response-letter strategy for trade / open-economy referees                 |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — trade data (Comtrade, BACI, CEPII gravity, WITS) + international macro/finance data (IMF IFS/BOP, BIS, EWN, Penn World Table) + Stata / R / Python / Dynare toolkits
- [`resources/official-source-map.md`](resources/official-source-map.md) — official JIE / Elsevier URLs behind the current process facts in this pack

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate any specific editor's or referee's taste
- It does not treat volatile metadata (current editors, exact fee, deposit rules, portal links) as evergreen — verify on the official page before submission
- It does not judge whether your motivation or model is genuinely original — that is the researcher's call

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Journal of International Economics (official)](https://www.sciencedirect.com/journal/journal-of-international-economics) — Elsevier

---

## License

MIT
