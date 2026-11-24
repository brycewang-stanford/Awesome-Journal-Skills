# Journal of Political Economy (JPE) Skills

<p align="center">
  <img src="assets/cover.svg" alt="Journal of Political Economy cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Journal%20of%20Political%20Economy-7a1f2b)](https://www.journals.uchicago.edu/journals/jpe/about)
[![Index](https://img.shields.io/badge/index-Top%20Five%20Economics-1f6feb)](https://www.journals.uchicago.edu/journals/jpe/about)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at the **Journal of Political Economy (JPE)** — a University of Chicago Press top-five economics journal, rooted in the Chicago price-theory tradition, now accompanied by field outlets (JPE: Microeconomics, JPE: Macroeconomics).

This repository is opinionated. It is **not** a generic economics-writing toolbox. It is a **JPE-specific** stack built around the journal's organizing question — *"What does economic theory predict, and does the evidence bear it out?"* — covering mechanism-driven topic selection, author-date literature positioning, credible causal identification, structural and price-theoretic modeling, robustness against rival mechanisms, economically legible exhibits, JPE house style, AEA-standard replication packages, referee pre-mortems, submission preflight, and R&R rebuttals.

> **Accuracy note.** Volatile specifics — the current editorial team, the exact submission fee, the precise word/format limits, and the latest data/code policy — change over time. This pack describes the journal's *durable* norms and tells you to verify current figures on the journal's official page.

---

## Why a Separate JPE Skill Stack?

JPE sits among the top-five but has a distinct house taste that differs materially from QJE / Econometrica / REStud:

| Constraint               | Journal of Political Economy                                          | Implication                                                      |
|--------------------------|----------------------------------------------------------------------|-----------------------------------------------------------------|
| Discipline               | Full breadth of economics, price-theory rooted                       | Strong in IO, labor, macro, public, theory, structural empirics |
| Core question            | "What does theory predict, and does evidence bear it out?"           | A bare causal effect with no mechanism is a half-paper          |
| Mechanism / theory       | Tight economic mechanism expected, even in empirical papers          | Atheoretical correlation mining is a desk-reject signal         |
| Identification bar       | Credible causal identification **and** economic interpretation       | OLS + controls rarely suffices on its own                       |
| Structural work          | Welcome; identification of parameters must be transparent            | "What identifies what" paragraph expected                       |
| Equilibrium reasoning    | General-equilibrium / incentive considerations scrutinized           | Partial-equilibrium stories that ignore GE are vulnerable       |
| References               | Author-date (Chicago/UChicago Press)                                 | Numbered/bracket citations are wrong house style                |
| Format                   | Theory + empirics integrated; proofs/robustness in appendices        | Online appendix carries the heavy material                      |
| Process                  | Editorial Manager; submission fee applies (verify)                   | Selective and demanding; fee step gates review                  |
| Replication              | Data/code required for accepted papers (AEA standard; verify)        | Reproducible master script + README expected                    |

Generic "scientific writing" or "economics writing" packs do not address these constraints.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install jpe-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/awesome-journal-skills.git
cd awesome-journal-skills/Journal-of-Political-Economy-Skills

mkdir -p ~/.claude/skills && cp -R skills/jpe-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/jpe-* ~/.codex/skills/
```

### First Prompt

```
Use jpe-workflow to tell me which skill I should use next for my JPE manuscript.
```

---

## Default Workflow

```text
jpe-topic-selection
        ▼
jpe-literature-positioning
        ▼
jpe-identification
        ▼
jpe-theory-model
        ▼
jpe-robustness
        ▼
jpe-tables-figures
        ▼
jpe-writing-style          (polish)
        ▼
jpe-referee-strategy
        ▼
jpe-replication-package
        ▼
jpe-submission
        ▼
jpe-rebuttal
```

`jpe-workflow` is the router — it tells you which skill to use next based on where you are. For JPE the model and the identification often iterate together: the model frequently disciplines the empirical specification.

---

## Skills

| Skill                          | Purpose                                                                       |
|--------------------------------|-------------------------------------------------------------------------------|
| `jpe-workflow`                 | Router — decides which sub-skill to invoke next                               |
| `jpe-topic-selection`          | JPE fit test (mechanism-driven question) + contribution framing               |
| `jpe-literature-positioning`   | Author-date intro arc + canonical-theory engagement                           |
| `jpe-identification`           | Credible identification (DID / IV / RDD / structural) **and** economic meaning |
| `jpe-theory-model`             | The model/mechanism that gives the result its economic interpretation         |
| `jpe-robustness`               | Specification robustness + rival-mechanism discrimination                     |
| `jpe-tables-figures`           | Economically legible exhibits in UChicago Press style                         |
| `jpe-writing-style`            | Spare, economics-first prose + author-date house conventions                  |
| `jpe-replication-package`      | AEA Data Editor–standard data/code package and README                         |
| `jpe-referee-strategy`         | Pre-mortem: price-theory / GE / identification objections                     |
| `jpe-submission`               | Editorial Manager preflight (format, references, fee, anonymity)              |
| `jpe-rebuttal`                 | R&R response-letter structure and revision plan                               |

### Resources

- [`skills/jpe-submission/templates/manuscript_template.md`](skills/jpe-submission/templates/manuscript_template.md) — JPE manuscript skeleton (section order, author-date references, variable table)
- [`skills/jpe-submission/templates/checklist.md`](skills/jpe-submission/templates/checklist.md) — 8-section pre-submission self-check
- [`resources/external_tools.md`](resources/external_tools.md) — economics data sources (IPUMS / Census-FSRDC / FRED / WRDS / Penn World Table) + Stata / R / Python / Julia packages for reduced-form, structural, and replication work

---

## Differences vs. QJE / Econometrica / REStud Skills

| Dimension            | JPE                                  | QJE                              | Econometrica                       | REStud                          |
|----------------------|--------------------------------------|----------------------------------|------------------------------------|---------------------------------|
| Lead criterion       | Economic mechanism + price theory    | Important question + clean ID    | Method / formal-theory novelty     | Technical depth, frontier slant |
| Reduced form         | Must connect to a model/mechanism    | Strong on its own if ID is clean | Needs a method/theory contribution | Welcome with rigor              |
| Structural work      | Core; identification transparent     | Common                           | Core                               | Core                            |
| Atheoretical paper   | Desk-reject risk                     | Risky                            | Off-fit                            | Risky                           |
| Citation style       | Author-date                          | Author-date                      | Author-date                        | Author-date                     |

If the paper is methodological with no economic application, Econometrica may fit better. If it is an atheoretical policy evaluation, reframe in `jpe-topic-selection` before targeting JPE.

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [AER-skills](https://github.com/brycewang-stanford/AER-skills) — American Economic Review
- [economic-research-skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/Economic-Research-Journal-Skills) — 《经济研究》 (Economic Research Journal)

---

## License

MIT
