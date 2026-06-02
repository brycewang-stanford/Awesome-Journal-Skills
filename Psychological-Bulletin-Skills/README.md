# Psychological Bulletin Skills

<p align="center">
  <img src="assets/cover.svg" alt="Psychological Bulletin cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Psychological%20Bulletin-6a1b4d)](https://www.apa.org/pubs/journals/bul)
[![Field](https://img.shields.io/badge/field-Psychology%20Synthesis-1f6feb)](https://www.apa.org/pubs/journals/bul)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **Psychological Bulletin** — the **American
Psychological Association's (APA) flagship outlet for integrative research reviews and
meta-analyses**, founded in **1904** and among the highest-impact journals in psychology.
Psychological Bulletin **"publishes syntheses of research in scientific psychology"**: systematic
reviews, meta-analyses, meta-reviews, meta-synthesis, and rigorous qualitative reviews.

This repository is opinionated. It is **not** a generic psychology-writing toolbox, and it is **not**
the Psychological Science or JPSP pack with the names swapped — those journals publish **primary
empirical studies**; Psychological Bulletin **does not**. The deliverable here is a **synthesis, not a
study**. So this is a **review/meta-analysis-specific** stack: a **meta-analyzable** question, a
**systematic PRISMA search**, transparent **eligibility + double-coding**, **random-effects** synthesis,
**moderator and publication-bias** diagnostics, a **theoretical contribution** built from the synthesis,
**MARS/PRISMA/JARS** reporting, **APA 7th-edition** style, **masked** review, and a transparent,
**preregistered** protocol.

---

## What Is Psychological Bulletin, and Why a Dedicated Stack?

Psychological Bulletin's constraints differ sharply from a primary-study journal:

| Constraint            | Psychological Bulletin                                                          | Implication                                                       |
|-----------------------|--------------------------------------------------------------------------------|------------------------------------------------------------------|
| Publisher / owner     | **American Psychological Association (APA)**                                    | Submitted via APA **Editorial Manager**                          |
| What it publishes     | **Research syntheses** — systematic reviews, **meta-analyses**, meta-reviews, meta-synthesis, qualitative reviews | Build a synthesis, **not** an original study      |
| What it does NOT do   | **No original primary empirical studies**; original **theory** → *Psychological Review* | Off-fit if your contribution is new data or pure theory  |
| Core method           | **Meta-analysis** + systematic review of an existing literature                | The "data" are prior studies; the unit is the **effect size**    |
| Review model          | **Masked** review (author identity withheld from reviewers)                    | Anonymize the manuscript; neutralize self-citations              |
| Abstract              | **≤ 250 words**                                                                | On a separate page                                               |
| Style                 | **APA Publication Manual, 7th edition**                                         | Author-date; APA headings and tables                             |
| Reporting standards   | **MARS** (meta-analysis) · **PRISMA** (systematic review) · **JARS** (quant/mixed) | Use the matching standard for your synthesis type           |
| Transparency          | Transparent reporting for empirical work incl. meta-analyses (**TOP**, since Feb 1 2022); supply **database, codebook, scripts** | Build the package as you code |
| Preregistration       | State whether design/hypotheses were preregistered and where; **PROSPERO**/OSF | Register the protocol **before** screening                       |
| Fee                   | **No submission fee** stated                                                   | Verify any post-acceptance open-access APC                       |

Volatile specifics (current editor and term, exact TOP level, abstract/length wording, accepted review
types, fee/APC) change — items not directly confirmed are marked **待核实** in
[`resources/official-source-map.md`](resources/official-source-map.md).
**Verify on the official APA journal page.**

### What counts as a Psychological Bulletin paper

- **Meta-analysis** — quantitatively pool effect sizes across studies (random-effects, heterogeneity).
- **Systematic review** — exhaustive, PRISMA-documented search and appraisal of a literature.
- **Meta-review / meta-synthesis** — synthesize across prior reviews or qualitative findings.
- **Qualitative / narrative review** — rigorous, integrative evaluation where a database resists pooling.

> The single most common off-fit: submitting an original empirical study, or pure new theory. Those
> belong to other APA journals (*Psychological Review* for theory). Bulletin synthesizes what exists.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/psychbull-skills
/plugin install psychbull-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/psychbull-skills.git
cd psychbull-skills

mkdir -p ~/.claude/skills && cp -R skills/psychbull-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/psychbull-* ~/.codex/skills/
```

### First Prompt

```
Use psychbull-workflow to tell me which skill I should use next for my Psychological Bulletin review.
```

---

## Default Workflow

```text
psychbull-topic-selection          (is it review-worthy / meta-analyzable?)
        ▼
psychbull-literature-search-strategy   (systematic search; PRISMA; databases)
        ▼
psychbull-inclusion-and-coding     (eligibility; double-coding; reliability)
        ▼
psychbull-meta-analysis-methods    (effect sizes; random effects; heterogeneity)
        ▼
psychbull-moderators-and-bias      (meta-regression; publication-bias diagnostics)
        ▼
psychbull-theory-integration       (turn the synthesis into a contribution)
        ▼
psychbull-tables-figures           (forest / funnel plots; PRISMA diagram)
        ▼
psychbull-writing-style            (APA 7th; MARS/JARS; ≤ 250-word abstract)
        ▼
psychbull-open-science-and-transparency
        ▼
psychbull-submission
        ▼
psychbull-rebuttal
```

`psychbull-workflow` is the router — it tells you which skill to use next based on where you are. The
first real decision is whether the question is **review-worthy and meta-analyzable**, and which
**synthesis type** (meta-analysis / systematic / qualitative) fits the literature. Register the
**protocol** (PROSPERO/OSF) before screening.

---

## Skills

| Skill                                   | Purpose                                                                       |
|-----------------------------------------|-------------------------------------------------------------------------------|
| `psychbull-workflow`                    | Router — decides which sub-skill to invoke next                               |
| `psychbull-topic-selection`             | Test review-worthiness / meta-analyzability; pick the synthesis type          |
| `psychbull-literature-search-strategy`  | Systematic, reproducible search across databases; PRISMA documentation        |
| `psychbull-inclusion-and-coding`        | Eligibility criteria, double-coding, codebook, inter-rater reliability        |
| `psychbull-meta-analysis-methods`       | Effect-size extraction, random-effects models, heterogeneity (I²/τ²)          |
| `psychbull-moderators-and-bias`         | Meta-regression, publication-bias diagnostics, sensitivity/robustness         |
| `psychbull-theory-integration`          | Turn the synthesis into a theoretical contribution, not just a table          |
| `psychbull-tables-figures`              | Forest/funnel plots, PRISMA flow diagram, MARS-ready tables                   |
| `psychbull-writing-style`               | APA 7th; MARS/PRISMA/JARS structure; the ≤ 250-word abstract                  |
| `psychbull-open-science-and-transparency` | Preregistration (PROSPERO/OSF), TOP, database + codebook + scripts          |
| `psychbull-submission`                  | Editorial Manager preflight (masking, abstract, MARS/PRISMA checklists)       |
| `psychbull-rebuttal`                    | Respond to R&R across reviewers + editor without breaking the synthesis       |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — search/screening (PsycINFO, Covidence, Rayyan), meta-analysis software (`metafor`, `robumeta`, Stata `meta`, CMA), bias diagnostics, and MARS/PRISMA/JARS standards
- [`resources/official-source-map.md`](resources/official-source-map.md) — official APA / MARS / PRISMA / PROSPERO / TOP URLs behind every fact, with 待核实 markers on unverified items

---

## What This Repo Does Not Do

- It does not write a submittable review or run your meta-analysis for you
- It does not simulate any specific editor's or reviewer's taste
- It does not assert volatile metadata (current editor and term, exact TOP level, abstract/length rules, fee/APC, policy wording) — verify on the official APA page; unverified items are marked 待核实
- It does not decide whether your question is review-worthy or whether the literature is poolable — that is the researcher's call
- It does not turn an original empirical study into a Bulletin paper — that is a category error; synthesize existing work instead

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Psychological Bulletin (APA)](https://www.apa.org/pubs/journals/bul) — owner, scope, submission guidelines
- [APA MARS / JARS](https://apastyle.apa.org/jars) · [PRISMA](http://www.prisma-statement.org/) · [PROSPERO](https://www.crd.york.ac.uk/prospero/) — reporting standards and protocol registration

---

## License

MIT
