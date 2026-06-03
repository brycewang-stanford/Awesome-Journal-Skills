# International Organization Skills

<p align="center">
  <img src="assets/cover.svg" alt="International Organization cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-IO-1b3a6b)](https://www.cambridge.org/core/journals/international-organization)
[![Field](https://img.shields.io/badge/field-International%20Relations-1f6feb)](https://www.cambridge.org/core/journals/international-organization/information/about-this-journal)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **International Organization (IO)** — widely regarded as
the **leading journal of international relations (IR)**, founded in **1947** and published by
**Cambridge University Press on behalf of the International Organization (IO) Foundation**. IO publishes
**generalizable theories** of international politics and the empirical and formal work that tests them
across **international institutions and law, cooperation and conflict, international political economy
(IPE), security, foreign policy, and IR theory** — welcoming **quantitative, formal/game-theoretic, and
qualitative** methods.

This repository is opinionated. It is **not** a generic social-science writing toolbox, and it is
**not** a generalist political-science pack (APSR / AJPS / JOP) with the names swapped. It is an
**IR-specialist** stack: the **international or cross-border phenomenon must be a major cause or
effect**, the contribution must be a **portable theory of international politics**, and the paper must
survive IO's distinctive **verification before final acceptance** — where IO staff **re-run your
quantitative results and check your formal-model proofs**, with materials deposited to the **IO
Dataverse** on Harvard Dataverse.

---

## What Is IO, and Why a Dedicated Stack?

IO's center of gravity differs from a discipline-wide flagship or a generalist field-quant journal:

| Constraint            | IO                                                                            | Implication                                                       |
|-----------------------|-------------------------------------------------------------------------------|------------------------------------------------------------------|
| Owner / publisher     | **IO Foundation** / **Cambridge University Press**                            | Submitted via **Editorial Manager**                              |
| Scope                 | **IR specialist** — institutions, conflict/cooperation, IPE, security, IR theory | The international level must be a **major cause or effect**    |
| Premium on            | **Generalizable theory** of international politics                             | A descriptive single-case/IGO study is off-fit                   |
| Methods               | Quantitative, **formal/game-theoretic**, qualitative — judged on own terms     | Formal proofs are first-class (and get verified)                 |
| Review model          | **Double-blind**                                                              | Anonymize; cite your own work in the **third person**            |
| Length                | **Research Article ≤ 14,000**; **Research Note ≤ 8,000**; **Essay ≤ 10,000**   | Counts include tables/figures/notes; **exclude** the bibliography |
| Supplementary material| **Should rarely exceed ~20 pages**, especially at initial submission           | Push robustness grids and proof details out of the main text      |
| Submission files      | **Abstract, word count, acknowledgments submitted separately**                 | They are not buried inside the manuscript                        |
| **Transparency**      | **Data/code at conditional acceptance; IO staff verify results + proofs before final acceptance** | Engineer a re-runnable package + checkable proofs from day one |

Volatile specifics (current editors and term, exact abstract cap, fee/APC, policy wording, article
types) change — items not directly confirmed are marked **待核实** in
[`resources/official-source-map.md`](resources/official-source-map.md). **Verify on the official page.**

### The signature differentiator: verification before final acceptance

Many journals ask for a replication package; IO **re-runs it and checks your proofs before publishing**.
Authors **do not** submit data at initial submission (consistent with double-blind review). At
**conditional acceptance** the editorial staff request data and command files; **IO staff re-run the
quantitative results and verify the proofs of formal models**, and editors **do not issue final
acceptance until all results of all reported analyses are confirmed.** On final acceptance, materials go
to the **IO Dataverse on Harvard Dataverse** (with a **DOI** cited in the article), a **Data
Availability Statement** appears before the references, and qualitative work is **strongly encouraged**
to deposit at the **Qualitative Data Repository (QDR)**.

### How IO differs from APSR / AJPS / JOP

- **APSR / AJPS / JOP are generalist** political-science venues; **IO is an IR specialist.** Your paper
  must be a contribution to **international relations**, not a domestic-politics result with
  international data attached.
- **Theory is the currency.** IO explicitly seeks **generalizable theories** of international politics —
  formal, rationalist, constructivist, or empirical — not a data exercise.
- **Formal work is verified too.** IO staff check **proofs of formal models** before final acceptance,
  not just re-run quantitative code.

### Three article types

- **Research Article** — full original IR study, generalizable theory + evidence, **≤ 14,000 words**.
- **Research Note** — one crisp IR contribution (a decisive test, a focused reappraisal, a measurement
  or theoretical advance), **≤ 8,000 words**. Not a padded Article.
- **Essay** — a conceptual, agenda-setting, or debate piece, **≤ 10,000 words** (confirm the current
  Essay remit on the live page — 待核实).

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/io-skills
/plugin install io-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/io-skills.git
cd io-skills

mkdir -p ~/.claude/skills && cp -R skills/io-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/io-* ~/.codex/skills/
```

### First Prompt

```
Use io-workflow to tell me which skill I should use next for my IO manuscript.
```

---

## Default Workflow

```text
io-topic-selection
        ▼
io-literature-positioning
        ▼
io-theory-building
        ▼
io-research-design
        ▼
io-data-analysis
        ▼
io-tables-figures
        ▼
io-writing-style          (polish)
        ▼
io-transparency-and-data-policy
        ▼
io-review-process
        ▼
io-submission
        ▼
io-rebuttal
```

`io-workflow` is the router — it tells you which skill to use next based on where you are. Its first job
is to confirm the paper is an **IR contribution** (the international phenomenon is a major cause or
effect) with a **generalizable theory**. Start `io-transparency-and-data-policy` **while you analyze**,
not at acceptance: IO staff **re-run your results and check your proofs before final acceptance**, and an
unscripted analysis or a hand-waved proof cannot be repaired under deadline.

---

## Skills

| Skill                                | Purpose                                                                       |
|--------------------------------------|-------------------------------------------------------------------------------|
| `io-workflow`                        | Router — decides which sub-skill to invoke next; confirms IR fit              |
| `io-topic-selection`                 | IR fit; international level as major cause/effect; pick the article type      |
| `io-literature-positioning`          | Enter an IR debate across rationalist/constructivist/IPE/security traditions  |
| `io-theory-building`                 | Build a generalizable IR theory (formal, rationalist, constructivist)         |
| `io-research-design`                 | Defend the design — dyadic/TSCS causal inference, cases, experiments, formal  |
| `io-data-analysis`                   | Analysis norms, dyadic inference, robustness, reproducible-from-line-one      |
| `io-tables-figures`                  | Self-contained, reproducible exhibits; the unit/level made explicit           |
| `io-writing-style`                   | Word caps, double-blind third-person self-citation, short author-date footnotes|
| `io-transparency-and-data-policy`    | Verify-before-final-acceptance package + IO Dataverse + DAS (the signature)   |
| `io-review-process`                  | Double-blind review, expert IR referees, verification before final acceptance |
| `io-submission`                      | Editorial Manager preflight (anonymity, word basis, separate abstract, ORCID) |
| `io-rebuttal`                        | R&R memo across paradigm-driven referees + editor, kept anonymous & verifiable|

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — IR data sources (COW / UCDP-PRIO / ACLED / UNGA voting / DESTA / AidData / V-Dem) + R / Stata / Python and dyadic/network/formal/CAQDAS tooling
- [`resources/official-source-map.md`](resources/official-source-map.md) — official IO / Cambridge / Harvard Dataverse URLs behind every fact, with 待核实 markers on unverified items

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate any specific editor's or reviewer's taste
- It does not assert volatile metadata (current editors and term, exact abstract cap, fee/APC, policy wording, article types) — verify on the official page; unverified items are marked 待核实
- It does not run or pass IO's verification for you — IO staff re-run your results and check your proofs; this pack only prepares a re-runnable package and a checkable proof appendix
- It does not decide whether your question is genuinely an international-relations contribution — that is the researcher's call

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [International Organization (Cambridge Core)](https://www.cambridge.org/core/journals/international-organization) — publisher home, author instructions, policies
- [International Organization (IO) Journal Dataverse](https://dataverse.harvard.edu/dataverse/IOJ) — replication materials on Harvard Dataverse

---

## License

MIT
