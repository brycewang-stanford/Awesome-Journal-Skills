<p align="center">
  <img src="assets/cover.svg" alt="Journal of Econometrics Skills" width="240">
</p>

<h1 align="center">Journal of Econometrics Skills (joe-skills)</h1>

<p align="center">
  An opinionated, twelve-skill agent stack for manuscripts targeted at the
  <a href="https://www.sciencedirect.com/journal/journal-of-econometrics"><b>Journal of Econometrics</b></a> (JoE) —
  the Elsevier flagship for <b>econometric methodology</b> (theory + applied methods).
</p>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-blue.svg"></a>
  <img alt="Skills: 12" src="https://img.shields.io/badge/skills-12-1f4e79">
  <img alt="Lang: en / zh-CN" src="https://img.shields.io/badge/docs-en%20%7C%20zh--CN-1f4e79">
</p>

> **English** | [简体中文](README.zh-CN.md)

## What this is

`joe-skills` is a Claude Code plugin: a bundle of twelve agent **skills** that encode how to take a paper from idea to acceptance at the *Journal of Econometrics* — a peer-reviewed Elsevier journal (founded 1973) for **substantive contributions to econometric methodology**: identification, estimation, testing, decision, and prediction problems in economic research, plus applications of econometric techniques. The center of gravity is a **new estimator, test, identification result, or asymptotic theory**, defended with proofs and **Monte Carlo evidence** — not a purely applied finding.

Each skill is tuned to JoE's actual norms, not a generic template. Co-Editors-in-Chief: **Michael Jansson** (UC Berkeley) and **Aureo de Paula** (UCL).

## Why JoE is different (and the skills reflect it)

| JoE reality | How the pack uses it |
|---|---|
| Current official links split portal guidance: ScienceDirect/new-submission links point to **Editorial Manager**; JoE Google Sites and resubmission materials still point to **Editorial Express** | `joe-submission`, `joe-workflow` start from the live official link and treat Editorial Express as resubmission/track-specific unless the live page directs otherwise |
| **USD $75 nonrefundable fee**, proof-of-payment uploaded *before* submission | `joe-submission` preflight makes the fee a blocking step |
| ScienceDirect source-file rules plus Editorial Express resubmission norms: editable source files for the Guide; PDF-only and ~40 pages inside the EE resubmission flow; **250-word** abstract | `joe-tables-figures`, `joe-writing-style`, `joe-submission` |
| **Single-anonymized** review; editor screen → ≥2 referees | `joe-review-process`, `joe-rebuttal` |
| Three tracks: **Regular / Annals / Themed** (Guest Associate Editors) | `joe-topic-selection`, `joe-review-process` |
| **elsarticle** LaTeX class; Elsevier **`[dataset]`** citations | `joe-writing-style`, `joe-replication-and-data-policy` |
| No universal JoE-specific central archive found; Elsevier encourages repository deposit and dataset citation | `joe-replication-and-data-policy` |
| Honorific **"Fellow of the Journal of Econometrics"** (4+ articles) | context in `joe-workflow` |

## The twelve skills

| # | Skill | Use it when |
|---|---|---|
| 1 | `joe-workflow` | Deciding which skill to use next; sequencing the whole manuscript |
| 2 | `joe-topic-selection` | Is this a real methodological contribution, or an applied paper? |
| 3 | `joe-literature-positioning` | Locating the advance against the nearest estimator/test |
| 4 | `joe-identification-strategy` | Assumptions, regularity conditions, asymptotics, proof plan |
| 5 | `joe-data-analysis` | Monte Carlo design (size/power) + empirical illustration |
| 6 | `joe-contribution-framing` | Saying why the result matters to econometrics |
| 7 | `joe-tables-figures` | Size/power tables and theory-illustrating figures |
| 8 | `joe-writing-style` | 250-word abstract, contribution-first intro, legible proofs |
| 9 | `joe-replication-and-data-policy` | Reproducible code/data under Elsevier norms |
| 10 | `joe-review-process` | Single-anonymized review, tracks, what referees look for |
| 11 | `joe-submission` | Live portal preflight (fee, files, abstract, track) |
| 12 | `joe-rebuttal` | Response letter + revised manuscript after a revision request |

## Default order

`joe-topic-selection` → `joe-literature-positioning` → `joe-identification-strategy` → `joe-data-analysis` → `joe-contribution-framing` → `joe-tables-figures` → `joe-writing-style` → `joe-replication-and-data-policy` → `joe-review-process` → `joe-submission` → `joe-rebuttal`. Use `joe-workflow` any time to find the current bottleneck.

## Repository layout

```
Journal-of-Econometrics-Skills/
├── .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── assets/cover.svg
├── resources/
│   ├── official-source-map.md     # every fact → official URL (accessed 2026-06-01)
│   └── external_tools.md          # simulation/estimation tooling for methodology
├── skills/
│   ├── joe-workflow/SKILL.md
│   ├── joe-topic-selection/SKILL.md
│   ├── joe-literature-positioning/SKILL.md
│   ├── joe-identification-strategy/SKILL.md
│   ├── joe-data-analysis/SKILL.md
│   ├── joe-contribution-framing/SKILL.md
│   ├── joe-tables-figures/SKILL.md
│   ├── joe-writing-style/SKILL.md
│   ├── joe-replication-and-data-policy/SKILL.md
│   ├── joe-review-process/SKILL.md
│   ├── joe-submission/
│   │   ├── SKILL.md
│   │   └── templates/checklist.md
│   └── joe-rebuttal/SKILL.md
├── LICENSE
└── README.md / README.zh-CN.md
```

## A note on verification

Journal policies change. The 2026-06-20 source refresh verified the fee, review model, abstract
limit, data-citation guidance, and the current portal split directly from official pages. Re-confirm
portal routing, open themed calls, and editor roster on the live official pages before relying on
them.

## License

[MIT](LICENSE) © 2026 Bryce Wang. Not affiliated with or endorsed by Elsevier or the Journal of Econometrics.
