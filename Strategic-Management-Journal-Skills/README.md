# Strategic Management Journal Skills

<p align="center">
  <img src="assets/cover.svg" alt="Strategic Management Journal cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Strategic%20Management%20Journal-14635a)](https://onlinelibrary.wiley.com/journal/10970266)
[![Index](https://img.shields.io/badge/index-SSCI%20%2F%20FT50-1f6feb)](https://onlinelibrary.wiley.com/journal/10970266)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at the **Strategic Management Journal (SMJ)** — the flagship strategy journal, published by **Wiley** for the **Strategic Management Society (SMS)**.

This repository is opinionated. It is **not** a generic management-writing toolbox. It is an **SMJ-specific** stack covering strategy-grounded topic selection, theory development, literature positioning, identification-aware research design, endogeneity-defeating data analysis, contribution framing, self-contained exhibits, house style, Wiley Research Exchange submission, the multi-round review process, and R&R rebuttals.

> Note on accuracy: this pack describes **durable norms**. Volatile specifics (current editors, exact word/length limits, fees or open-access options, reference style) change over time — always verify them on the official SMJ Author Guidelines page before submitting.

---

## Why a Separate SMJ Skill Stack?

SMJ imposes constraints that differ materially from general-management journals (AMJ / ASQ) and from theory-only outlets (AMR):

| Constraint                | Strategic Management Journal                                       | Implication                                                  |
|---------------------------|-------------------------------------------------------------------|--------------------------------------------------------------|
| Discipline                | Strategy: firm performance & competitive advantage                | Generic "management" or pure-OB framing reads as off-fit     |
| Focal construct           | Performance / advantage outcome at the firm / BU / dyad level     | An individual-attitude DV is a scope misfit                  |
| Theory                    | Explicit causal mechanism, not signed predictions                 | "X relates to Y" with no logic is a theory weakness          |
| Identification            | Endogeneity must be confronted by design                          | Performance regressions with unaddressed endogeneity are the #1 rejection reason |
| Reverse causality         | Must be broken by design, not lags alone                          | Cross-sectional correlations read as non-causal              |
| Self-selection            | Selection into the strategic choice must be addressed             | Ignoring self-selection invites rejection                    |
| Methods bar               | Panel FE + IV / DID / matching / Heckman; placebos & robustness   | OLS-with-controls rarely suffices                            |
| Contribution              | A change in how strategy scholars think                           | A list of findings is not a contribution                     |
| Process                   | Wiley Research Exchange; action editor + multiple reviewers; multi-round | First-round Major Revision is normal and encouraging         |

Generic "scientific writing" or "management writing" skill packs do not address these constraints.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install smj-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/awesome-journal-skills.git
cd awesome-journal-skills/Strategic-Management-Journal-Skills

mkdir -p ~/.claude/skills && cp -R skills/smj-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/smj-* ~/.codex/skills/
```

### First Prompt

```
Use smj-workflow to tell me which skill I should use next for my Strategic Management Journal manuscript.
```

---

## Default Workflow

```text
smj-topic-selection
        ▼
smj-theory-development
        ▼
smj-literature-positioning
        ▼
smj-methods
        ▼
smj-data-analysis
        ▼
smj-contribution-framing
        ▼
smj-tables-figures
        ▼
smj-writing-style       (polish)
        ▼
smj-submission
        ▼
smj-review-process
        ▼
smj-rebuttal
```

`smj-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill                       | Purpose                                                                 |
|-----------------------------|-------------------------------------------------------------------------|
| `smj-workflow`              | Router — decides which sub-skill to invoke next                         |
| `smj-topic-selection`       | Strategy fit test (performance / advantage) + question sharpening       |
| `smj-theory-development`    | Mechanism-first argument and hypothesis craft                           |
| `smj-literature-positioning`| Enter a named conversation; theoretical gap, not a context gap          |
| `smj-methods`               | Sample, unit of analysis, measures, identification design               |
| `smj-data-analysis`         | Defeat endogeneity / reverse causality / selection; mechanism + robustness |
| `smj-contribution-framing`  | Make the contribution land as strategy theory, not generic management   |
| `smj-tables-figures`        | Self-contained exhibits, marginal-effects & event-study figures         |
| `smj-writing-style`         | Late-stage prose polish and house conventions                           |
| `smj-submission`            | Research Exchange preflight + checklist + manuscript template           |
| `smj-review-process`        | Read the decision letter; plan the revision around the gating concern   |
| `smj-rebuttal`              | Point-by-point R&R response-letter structure                            |

### Resources

- [`skills/smj-submission/templates/manuscript_template.md`](skills/smj-submission/templates/manuscript_template.md) — SMJ-style manuscript skeleton (abstract, hypotheses, variable table, identification section, references)
- [`skills/smj-submission/templates/checklist.md`](skills/smj-submission/templates/checklist.md) — 8-section pre-submission self-check
- [`resources/external_tools.md`](resources/external_tools.md) — strategy data sources (Compustat / CRSP / SDC / BoardEx / Orbis / patents) + Stata / R / Python identification toolkit

---

## Differences vs. AMJ / ASQ / AMR

| Dimension          | Strategic Management Journal      | AMJ / ASQ (general management)     | AMR (theory only)        |
|--------------------|-----------------------------------|------------------------------------|--------------------------|
| Core question      | Firm performance & advantage      | Broad organizational phenomena     | Conceptual advance       |
| Data               | Required (or strong qual/formal)  | Required                           | None                     |
| Identification bar | Very high (endogeneity central)   | High                               | N/A                      |
| Contribution test  | Advances **strategy** theory      | Advances management/OB theory      | New theory itself        |
| Most common reject  | Unaddressed endogeneity; off-strategy contribution | Fit / theory | Insufficient theoretical novelty |

---

## What This Repo Does Not Do

- It does not write a submission-ready manuscript for you
- It does not simulate a specific editor's or reviewer's preferences
- It does not track SMJ's rejection rate, impact factor, or current editorial board (verify those on the official page)
- It does not judge whether your contribution is genuinely novel — that is your call as the researcher

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [amj-skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/Academy-of-Management-Journal-Skills) — Academy of Management Journal
- [amr-skills](https://github.com/brycewang-stanford/awesome-journal-skills/tree/main/Academy-of-Management-Review-Skills) — Academy of Management Review (theory only)

---

## License

MIT
