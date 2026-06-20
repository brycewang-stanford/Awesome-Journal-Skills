# The Journal of Politics Skills

<p align="center">
  <img src="assets/cover.svg" alt="The Journal of Politics cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-JOP-7a1f2b)](https://www.journals.uchicago.edu/journals/jop/about)
[![Field](https://img.shields.io/badge/field-Political%20Science-1f6feb)](https://spsa.net/about-spsa/journal-of-politics/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **The Journal of Politics (JOP)** — a leading
**general-interest** political-science journal, founded in **1939**, published by the **University of
Chicago Press** for the **Southern Political Science Association (SPSA)**. JOP is the oldest regional
political-science journal in the United States and a perennial top general-interest venue. It publishes
**theoretically innovative and methodologically diverse** research across **all subfields**: American
politics, comparative politics, formal theory, international relations, methodology, political theory,
public administration, and public policy.

This repository is opinionated. It is **not** a generic social-science writing toolbox and it is
**not** an APSR or AJPS pack with the names swapped. It is a **JOP-specific** stack built around the
two things that make JOP operate differently from its discipline-wide peers: a **page budget** rather
than a word count — **Research Articles ≤ 35 pages** and **Short Articles ≤ 10 pages**, double-spaced
12-point, inclusive of text, notes, references, and exhibits — and a data policy under which
**acceptance is contingent on replicability**, with a **JOP replication analyst** assigned at
**conditional acceptance** to assess the package you deposit in the **JOP Dataverse** before
publication.

---

## What Is JOP, and Why a Dedicated Stack?

JOP's constraints differ from a Cambridge/APSA flagship or a Wiley/MPSA field-quant journal:

| Constraint            | JOP                                                                            | Implication                                                       |
|-----------------------|--------------------------------------------------------------------------------|-------------------------------------------------------------------|
| Owner / publisher     | **SPSA** / **University of Chicago Press** (publisher since Jan 2015)           | Submitted via **Editorial Manager** (`editorialmanager.com/jop`)  |
| Scope                 | **General interest**, all subfields; "broad and encompassing" on theory/method | Empirical, formal, qualitative, and normative work all welcome    |
| **Length basis**      | **Pages, not words** — Research Article **≤ 35 pp**, Short Article **≤ 10 pp**  | Budget pages from day one; word-count habits mislead              |
| Page rules            | Double-spaced, **12-pt**, one-inch margins; **incl.** text, notes, refs, exhibits | Dense refs and big tables cost pages directly                   |
| Online Appendix       | **≤ 25 pages**, separate file, **excluded** from the 35                         | Push robustness grids and derivations out of the main text        |
| Review model          | **Double-blind**                                                               | Anonymize the manuscript; upload an anonymous version for review  |
| Abstract              | **≤ 150 words**, 4–5 keywords                                                  | Question + approach + findings; no citations in the abstract      |
| **Data policy**       | **Accepted contingent on replicability**; **JOP replication analyst** at conditional acceptance | Build a re-runnable package as you analyze; non-replicable = rejected |
| Style                 | **The JOP Style Guide** (house author-date)                                    | Pick one consistent style; not APSA-or-Chicago generic            |

Volatile specifics (editors and term, exact page/abstract limits, fee/APC, categories, policy wording)
change. [`resources/official-source-map.md`](resources/official-source-map.md) was refreshed on
2026-06-20 and separates direct SPSA/Dataverse evidence from UChicago Press rules surfaced through
official publisher search snippets; **re-open the live official page before submission.**

### Three differentiators worth internalizing

- **Pages, not words.** APSR and AJPS cap *words*; JOP caps *pages* (35 / 10, double-spaced 12-pt). The
  same paper can clear a word cap and still blow the page budget — plan exhibits and references for the
  page, and move the overflow into the **≤ 25-page Online Appendix**.
- **Shorter and faster by reputation.** JOP is known for tighter articles and an efficient review
  process. The **Short Article (≤ 10 pp)** route exists for a single crisp contribution; treat speed as
  a qualitative norm, not a guaranteed clock.
- **A replication analyst, not just a deposit.** JOP makes acceptance **contingent on replicability**
  and assigns a **JOP replication analyst** at conditional acceptance who checks your materials before
  publication — distinct from APSR's editorial-office reproduction check and AJPS's external
  third-party verifier. Non-replicable papers are rejected.

### Two submission categories

- **Research Article** — full original study, **≤ 35 pages** inclusive of text, notes, references, and
  tables/figures, with an **Online Appendix ≤ 25 pages** for supporting material.
- **Short Article** — a single, sharply focused contribution, **≤ 10 pages** on the same inclusive
  basis. Not a padded Research Article; do not describe it as a separate "Letters" track unless the
  current JOP category menu uses that label.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/jop-skills
/plugin install jop-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/jop-skills.git
cd jop-skills

mkdir -p ~/.claude/skills && cp -R skills/jop-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/jop-* ~/.codex/skills/
```

### First Prompt

```
Use jop-workflow to tell me which skill I should use next for my JOP manuscript.
```

---

## Default Workflow

```text
jop-topic-selection
        ▼
jop-literature-positioning
        ▼
jop-theory-building
        ▼
jop-research-design
        ▼
jop-data-analysis
        ▼
jop-tables-figures
        ▼
jop-writing-style          (fit the page budget)
        ▼
jop-replication-and-data-policy
        ▼
jop-review-process
        ▼
jop-submission
        ▼
jop-rebuttal
```

`jop-workflow` is the router — it tells you which skill to use next based on where you are. Start
`jop-replication-and-data-policy` **while you analyze**, not at acceptance: a **JOP replication analyst**
re-checks your package at conditional acceptance, and an unscripted analysis cannot be repaired under
deadline. Decide **Research Article vs Short Article** early, because the **page budget** shapes how
much you can carry in the main text.

---

## Skills

| Skill                                | Purpose                                                                       |
|--------------------------------------|-------------------------------------------------------------------------------|
| `jop-workflow`                       | Router — decides which sub-skill to invoke next                               |
| `jop-topic-selection`                | General-interest fit across subfields; pick Research Article vs Short Article |
| `jop-literature-positioning`         | Stake a broad contribution while staying double-blind                         |
| `jop-theory-building`                | Build the argument (formal, empirical, or normative) into a contribution      |
| `jop-research-design`                | Defend the design — causal inference, experiments, formal, qualitative        |
| `jop-data-analysis`                  | Analysis norms, uncertainty, robustness, reproducible-from-line-one           |
| `jop-tables-figures`                 | Self-contained, regenerated exhibits that respect the page budget             |
| `jop-writing-style`                  | The JOP Style Guide; land the paper within 35 / 10 pages                      |
| `jop-replication-and-data-policy`    | Re-runnable package for the JOP Dataverse + the replication analyst (signature)|
| `jop-review-process`                 | Double-blind review, desk screening, replicability-contingent acceptance      |
| `jop-submission`                     | Editorial Manager preflight (anonymity, page count, appendix ≤ 25 pp, abstract)|
| `jop-rebuttal`                       | R&R response letter for multiple reviewers + editor, kept anonymous           |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — political-science data sources (ANES / CES / V-Dem / CSES / COW / ACLED / MARPOR) + R / Stata / Python and qualitative/CAQDAS tooling, plus page-budget and replication-package conventions
- [`resources/official-source-map.md`](resources/official-source-map.md) — official UChicago Press / SPSA / Harvard Dataverse URLs behind every volatile process fact, refreshed 2026-06-20

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate any specific editor's or reviewer's taste
- It does not freeze volatile metadata (current editors and term, exact page/abstract limits, fee/APC, categories, policy wording) — verify on the live official page before uploading
- It does not run or pass the replication-analyst check for you — that is the JOP analyst's job; this pack only prepares a re-runnable package

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [The Journal of Politics (University of Chicago Press)](https://www.journals.uchicago.edu/journals/jop/about) — publisher home, instructions, policies
- [Journal of Politics at SPSA](https://spsa.net/about-spsa/journal-of-politics/) — owner, scope, editorial team

---

## License

MIT
