# Review of Economic Studies Skills

<p align="center">
  <img src="assets/cover.svg" alt="The Review of Economic Studies cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Review%20of%20Economic%20Studies-1f3a5f)](https://academic.oup.com/restud)
[![Index](https://img.shields.io/badge/index-Top--5%20Economics-1f6feb)](https://academic.oup.com/restud)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **The Review of Economic Studies (REStud)** — one of the "top-5" economics journals, run by The Review of Economic Studies Ltd and published by Oxford University Press.

This repository is opinionated. It is **not** a generic economics writing toolbox. It is a **REStud-specific** stack covering original-contribution topic selection, literature positioning, state-of-the-art causal identification, rigorous theory-model development with online-appendix proofs, demanding robustness, clean exhibits, REStud house style, replication packages, referee strategy, submission preflight, and multi-round R&R rebuttals.

REStud is historically European-rooted and famously **friendly to young scholars** — the annual REStud Tour / "May Meetings" showcases junior economists' job-market-stage work.

---

## Why a Separate REStud Skill Stack?

REStud sits alongside AER / QJE / JPE / Econometrica but its center of gravity is distinctive:

| Constraint            | Review of Economic Studies                                        | Implication                                                       |
|-----------------------|-------------------------------------------------------------------|-------------------------------------------------------------------|
| Scope                 | Theoretical **and** applied economics, all fields                 | Field-agnostic; a clean theory paper is as welcome as applied      |
| Hallmark contribution | A new model, a new identification strategy, or a striking new fact| "Competent application of a known toolkit" is not enough           |
| Bar                   | Originality + technical excellence + elegance                     | The economic payoff must be legible quickly                        |
| Identification        | State-of-the-art causal design **or** rigorous structural ID      | TWFE, weak IV, naive RDD are flagged; assumptions stated explicitly |
| Theory                | Complete, correct proofs in an **online appendix**                | Theory without a clear economic payoff is rejected                 |
| References            | Author-date (Harvard) style                                       | Numbered-reference style is off-house                              |
| Replication           | Data/code required for accepted empirical papers (OUP policy)     | Plan the deposit early; verify current rules                       |
| Refereeing            | Demanding referees; strong papers developed across rounds         | Treat the R&R as collaboration, not a verdict                      |
| Young scholars        | REStud Tour / May Meetings showcase junior work                   | One sharp contribution beats a sprawling paper                     |

Generic "scientific writing" or "economics writing" skill packs do not address these constraints. Volatile specifics (current editors, exact fees, exact word limits) change — this stack tells you the durable norms and sends you to the journal's official page to verify the numbers.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install restud-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/awesome-journal-skills.git
cd awesome-journal-skills/Review-of-Economic-Studies-Skills

mkdir -p ~/.claude/skills && cp -R skills/restud-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/restud-* ~/.codex/skills/
```

### First Prompt

```
Use restud-workflow to tell me which skill I should use next for my REStud manuscript.
```

---

## Default Workflow

```text
restud-topic-selection
        ▼
restud-literature-positioning
        ▼
restud-identification   ──┐  (empirical branch)
        ▼                 │
restud-theory-model     ──┘  (theory branch; both for theory-with-empirics)
        ▼
restud-robustness
        ▼
restud-tables-figures
        ▼
restud-writing-style    (polish)
        ▼
restud-replication-package
        ▼
restud-referee-strategy
        ▼
restud-submission
        ▼
restud-rebuttal
```

`restud-workflow` is the router — it tells you which skill to use next based on where you are. `restud-identification` and `restud-theory-model` are parallel branches.

---

## Skills

| Skill                         | Purpose                                                            |
|-------------------------------|--------------------------------------------------------------------|
| `restud-workflow`             | Router — decides which sub-skill to invoke next                    |
| `restud-topic-selection`      | Top-5 bar test + one-sentence original-contribution template       |
| `restud-literature-positioning`| Confront the closest 3–5 papers; state the marginal contribution  |
| `restud-identification`       | State-of-the-art causal design (DID / IV / RDD / SCM / RCT)        |
| `restud-theory-model`         | Model development; proofs to the online appendix; economic payoff  |
| `restud-robustness`           | Referee-anticipating checks; no result hinging on one specification |
| `restud-tables-figures`       | Booktabs tables, vector figures, one result per exhibit            |
| `restud-writing-style`        | Clear, economical prose; result-forward intro & abstract; author-date |
| `restud-replication-package`  | Data/code deposit, README, reproducibility audit (verify OUP policy) |
| `restud-referee-strategy`     | Map the referee pool; pre-empt the objections before submission    |
| `restud-submission`           | Pre-submission preflight + manuscript template (title page, format) |
| `restud-rebuttal`             | R&R response-letter structure; triage and revise-first discipline  |

### Resources

- [`skills/restud-submission/templates/manuscript_template.md`](skills/restud-submission/templates/manuscript_template.md) — REStud manuscript skeleton (abstract, theory & empirical spines, author-date references, online appendix)
- [`skills/restud-submission/templates/checklist.md`](skills/restud-submission/templates/checklist.md) — 8-section pre-submission self-check
- [`resources/external_tools.md`](resources/external_tools.md) — economics data sources (IPUMS, PSID, FRED, Compustat/CRSP, WDI, Comtrade …) + Stata / R / Python / structural packages

---

## Differences vs. Other Top-5 Stacks

| Dimension          | Review of Economic Studies        | AER                              | Econometrica                    |
|--------------------|-----------------------------------|----------------------------------|---------------------------------|
| Center of gravity  | Original contribution + elegance  | Cross-subfield interest / policy | Formal/methodological depth     |
| Theory             | First-class, payoff must be legible| Welcome with empirical hook     | Heavy machinery is the contribution |
| Young scholars     | Explicitly showcased (May Meetings)| —                               | —                               |
| Reference style    | Author-date                       | Author-date                      | Author-date                     |

If the paper is finance-specific (JF / JFE / RFS) or so abstract it is really a math paper, a different stack fits better.

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [AER-skills](https://github.com/brycewang-stanford/AER-skills) — American Economic Review
- [qje-skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/Quarterly-Journal-of-Economics-Skills) — Quarterly Journal of Economics

---

## License

MIT
