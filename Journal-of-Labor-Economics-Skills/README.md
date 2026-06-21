# Journal of Labor Economics Skills

<p align="center">
  <img src="assets/cover.svg" alt="Journal of Labor Economics cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-JOLE-1a3c6e)](https://www.journals.uchicago.edu/journals/jole/about)
[![Field](https://img.shields.io/badge/field-Labor%20Economics-1f6feb)](https://www.journals.uchicago.edu/journals/jole/about)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at the **Journal of Labor Economics (JOLE)** — a
general-interest, peer-reviewed **quarterly** covering international research in labor economics,
published by the **University of Chicago Press** for the **Society of Labor Economists (SOLE)**.

JOLE publishes both theoretical and applied/empirical work on the behavior and outcomes of labor markets:
wages and earnings, employment and unemployment, human capital and education, labor supply and demand,
household and family economics, discrimination, unions, migration, and labor-market institutions and
policy. This repository is opinionated. It is **not** a generic economics-writing toolbox — it is a
**JOLE-specific** stack tuned to how this journal actually screens, reviews, and publishes labor
economics.

---

## Why a Separate JOLE Skill Stack?

JOLE imposes constraints that differ materially from a top-5 flagship or a double-blind journal:

| Constraint              | JOLE                                                                                  | Implication                                                                |
|-------------------------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| Audience                | General-interest **within labor economics**                                            | The question must matter to labor economists broadly, not one niche        |
| Submission fee          | **$100 (SOLE members) / $175 (non-members)**, since July 1, 2018                        | Non-refundable even on desk reject; decision withheld until the fee is paid |
| Review model            | **Single-blind** (referees anonymous, authors named)                                   | Do **not** anonymize — the opposite of double-blind journals               |
| Title page              | All co-authors' names, institutions, emails                                            | Required up front; references are **not** blinded                          |
| Abstract                | **100 words**                                                                          | Very short — every word counts                                             |
| Length                  | Normally **≤ 20,000 words**, full-page table/figure = **500 words**                     | A hard word economy; exhibits cost against the limit                       |
| References              | **Chicago author-date**, in-text **chronological then alphabetical**, "et al." for 3+   | Purely alphabetical in-text ordering reads as off-template                 |
| Submission system       | **Editorial Manager** (`editorialmanager.com/jole`)                                     | Not Editorial Express, not ScholarOne                                       |
| Data policy             | Deposit data + programs + docs to the **JOLE Dataverse** (AER policy, adopted Feb 2009) | Empirical papers publish only if replicable                                |
| Society tie             | Official journal of **SOLE**                                                            | Membership lowers the submission fee                                        |

Generic "scientific writing" or "econ writing" skill packs do not address these constraints. Live portal
prompts, fee wording, editor rosters, and deposit instructions can change, so run the source-map live
checks before upload. See [`resources/official-source-map.md`](resources/official-source-map.md) for
every fact and its status.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/jole-skills
/plugin install jole-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/jole-skills.git
cd jole-skills

mkdir -p ~/.claude/skills && cp -R skills/jole-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/jole-* ~/.codex/skills/
```

### First Prompt

```
Use jole-workflow to tell me which skill I should use next for my JOLE manuscript.
```

---

## Default Workflow

```text
jole-topic-selection
        ▼
jole-literature-positioning
        ▼
jole-identification-strategy
        ▼
jole-data-analysis
        ▼
jole-contribution-framing
        ▼
jole-tables-figures
        ▼
jole-writing-style        (polish)
        ▼
jole-replication-and-data-policy
        ▼
jole-review-process
        ▼
jole-submission
        ▼
jole-rebuttal
```

`jole-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills (12)

| Skill                              | Purpose                                                                            |
|------------------------------------|------------------------------------------------------------------------------------|
| `jole-workflow`                    | Router — decides which sub-skill to invoke next                                    |
| `jole-topic-selection`             | Labor-market fit + the "matters to labor economists broadly" bar                   |
| `jole-literature-positioning`      | Stake the contribution against the labor literature (Chicago author-date norms)    |
| `jole-identification-strategy`     | Credible labor identification (DID / IV / RDD / RCT / AKM)                          |
| `jole-data-analysis`               | Labor empirical norms: CPS/ACS/registers, wage decompositions, robustness          |
| `jole-contribution-framing`        | Frame the contribution for a general labor audience                                |
| `jole-tables-figures`              | Exhibit economy under the 20,000-word / 500-words-per-page rule                    |
| `jole-writing-style`               | House style + the 100-word abstract + Chicago author-date                          |
| `jole-replication-and-data-policy` | JOLE Dataverse deposit + AER data policy (adopted Feb 2009)                         |
| `jole-review-process`              | Single-blind review, fee, Editorial Manager, what referees expect                  |
| `jole-submission`                  | Editorial Manager preflight (fee, title page, 100-word abstract, non-anonymized)   |
| `jole-rebuttal`                    | R&R response-letter strategy for labor referees                                    |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — labor data sources (CPS/ACS/IPUMS,
  LEHD/QWI, NLSY/PSID, registers) + Stata/R/Python packages (AKM, DID, RDD, Oaxaca, RIF)
- [`resources/official-source-map.md`](resources/official-source-map.md) — official JOLE URLs and the
  verification status behind every fact in this pack

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate any specific editor's or referee's taste
- It does not replace the live submission screen; re-check portal prompts, fees, editor conflicts, and
  data-policy wording before upload
- It does not judge whether your labor question is genuinely novel — that is the researcher's call

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Journal of Labor Economics (official)](https://www.journals.uchicago.edu/journals/jole/about) — University of Chicago Press
- [Society of Labor Economists (SOLE)](https://www.sole-jole.org/) — the journal's sponsoring society

---

## License

MIT
