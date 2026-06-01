# Journal of Applied Econometrics Skills

<p align="center">
  <img src="assets/cover.svg" alt="Journal of Applied Econometrics cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-JAE-15436b)](https://onlinelibrary.wiley.com/journal/10991255)
[![Field](https://img.shields.io/badge/field-Applied%20Econometrics-1f6feb)](https://onlinelibrary.wiley.com/journal/10991255)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at the **Journal of Applied Econometrics (JAE)** — published by **John Wiley & Sons** since **1986** (ISSN 0883-7252 / 1099-1255, 7 issues/year), edited under Editor-in-Chief **Barbara Rossi**. JAE is the discipline's home for **empirical, replicable** economics that **applies and develops econometric techniques on real data** — papers are about *applications*, not pure econometric theory.

This repository is opinionated. It is **not** a generic econometrics-writing toolbox. It is a **JAE-specific** stack built around the journal's defining trait: **reproducibility**. Every result you report should be regeneratable from the plain-text data and code you deposit in the famous **JAE Data Archive**.

Official basis checked on 2026-06-01. See [`resources/official-source-map.md`](resources/official-source-map.md) for source URLs, access dates, and `待核实` items.

---

## Why a Separate JAE Skill Stack?

JAE imposes constraints that differ materially from a general-interest flagship (QJE) or a pure-theory journal (Econometrica):

| Constraint              | JAE                                                                      | Implication                                                       |
|-------------------------|--------------------------------------------------------------------------|-------------------------------------------------------------------|
| Scope                   | Applied econometrics — techniques applied to **real data**               | A pure-theory proof paper is off-fit                              |
| Hallmark                | **Replicability**: results must be regeneratable from deposited code/data | A non-reproducible result is a non-starter                        |
| Data policy             | **Mandatory JAE Data Archive deposit** on acceptance (unless confidential) | Plan archive-ready data + code from day one                       |
| Archive format          | Plain **ASCII / CSV** + readme; **`.dta` / SAS not acceptable alone**     | Export everything to text; never deposit a bare `.dta`            |
| Length                  | **Hard 35-page** article limit; online appendices **excluded**           | Put detail in unlimited online supporting material                |
| Abstract                | **100-word summary, no citations**; up to **six keywords**               | A long, citation-laden abstract is off-template                   |
| References              | **Any consistent style** ("Free Format")                                 | No house citation style is enforced                               |
| Review                  | **Single-blind**; Editor-in-Chief has final accept/reject                | Authors are not anonymized; reviewers are                         |
| Submission cap          | **≤ 3 papers per author** under review at once                           | Stagger your pipeline                                             |
| Special category        | Dedicated **Replication Article** track                                  | Replications (successful or not) are publishable here             |

Generic "scientific writing" or "econ writing" packs do not address these constraints. Volatile specifics (editors, APC figures, exact wording) change — **verify them on the official journal page** (several Wiley pages are bot-blocked; this pack flags such facts as `待核实`).

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/jape-skills
/plugin install jape-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/jape-skills.git
cd jape-skills

mkdir -p ~/.claude/skills && cp -R skills/jape-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/jape-* ~/.codex/skills/
```

---

## The Twelve Skills

| Skill | Role |
|-------|------|
| `jape-workflow` | End-to-end map of the JAE manuscript lifecycle |
| `jape-topic-selection` | Is this an *applied* (not pure-theory) econometrics fit for JAE? |
| `jape-literature-positioning` | Position against applied-econometrics precedent and JAE's own corpus |
| `jape-contribution-framing` | Frame the contribution as an application + replicable evidence |
| `jape-identification-strategy` | Credible empirical design on real data; assumptions defended |
| `jape-data-analysis` | Reproducible estimation, robust inference, archive-aware analysis |
| `jape-tables-figures` | Exhibits within the 35-page limit; detail pushed to online appendix |
| `jape-writing-style` | 100-word summary, six keywords, section structure, COI statement |
| `jape-replication-and-data-policy` | Archive-ready package: plain ASCII/CSV + readme + programs |
| `jape-review-process` | Single-blind review, Editor-in-Chief authority, what referees check |
| `jape-submission` | Editorial Express preflight; Free Format; three-paper cap |
| `jape-rebuttal` | Responding to single-blind referees on an R&R |

---

## Signature JAE Norms Encoded Here

- **JAE Data Archive (since 1994, now at ZBW):** accepted papers must deposit a complete set of non-confidential data and (typically) the programs that replicate every result.
- **Plain-text rule:** archive data must be ASCII/CSV with a readme; bare Stata `.dta` / SAS datasets are not acceptable.
- **Hard 35-page article** + unlimited online appendices that do **not** count toward the limit.
- **100-word, citation-free summary**; up to six keywords.
- **Citation-style agnostic** "Free Format" submission via **Editorial Express**.
- **Single-blind** review with **Editor-in-Chief** final authority; **≤ 3 papers** per author under review at once.
- A dedicated **Replication Article** category.

Sources and accessed dates for every fact: [`resources/official-source-map.md`](resources/official-source-map.md).

---

## Maintenance Notes

- Reopen the live Wiley author instructions before giving submission-ready advice.
- Keep source-map `待核实` items (the exact OA APC figure, the full co-editor roster) out of hard claims.
- Fees, editors, data policy, review model, and formatting rules can change — re-verify.

---

## License

MIT — see [LICENSE](LICENSE).

> Not affiliated with or endorsed by the Journal of Applied Econometrics, John Wiley & Sons, or the JAE Data Archive. Always confirm current requirements on the official journal and archive pages before submitting.
