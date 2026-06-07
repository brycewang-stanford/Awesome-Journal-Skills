# Economic-Research Skills

<p align="center">
  <img src="assets/cover.jpg" alt="《经济研究》 journal cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Economic%20Research-c0392b)](https://erj.ajcass.com/)
[![ISSN](https://img.shields.io/badge/ISSN-0577--9154-1f6feb)](https://erj.ajcass.com/)
[![Index](https://img.shields.io/badge/index-CSSCI%20%2F%20PKU%20core%20%2F%20AMI-1f6feb)](https://erj.ajcass.com/)
[![Skills](https://img.shields.io/badge/skills-18-blue)](skills/)
[![Code](https://img.shields.io/badge/code-Stata%20%2B%20Python-success)](resources/code/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **《经济研究》 (Economic Research Journal)** — the top economics journal in China (published by the Institute of Economics, CASS; ISSN 0577-9154; monthly; founded 1955). **18 skills** span the full lifecycle from topic selection to R&R rebuttal, shipping a **runnable Stata + Python code library**.

The stack is **dual-mode** — it both *diagnoses* a manuscript's bottleneck (templates, checklists) and *generates* publication-grade draft passages (introduction, mechanism, abstract, response letter) for you to refine.

It is **not** a generic Chinese-economics writing toolbox. It is an Economic-Research-specific methodology stack.

---

## Why a Separate Economic-Research Skill Stack?

《经济研究》 imposes constraints that differ materially from AER / AEJ / top finance journals (rows marked **[official]** are verified against the journal's own sources):

| Constraint                | Economic Research                                          | Implication                                                |
|---------------------------|------------------------------------------------------------|------------------------------------------------------------|
| Discipline                | Economics (macro / institutional / econometric / industry) | Pure-management or pure-case papers are off-fit            |
| Topic                     | Theory + China problem; anti "quant-for-its-own-sake" [official] | "Policy evaluation only" reads as a working paper      |
| Contribution sentences    | 3–5 explicit "边际贡献" bullets in intro                    | Cannot be a single paragraph                               |
| Literature review         | Bilingual; **canonical theory citations required**         | Missing canonical theory refs is a desk-reject signal      |
| Identification            | Quasi-experimental; modern estimators expected              | TWFE-only / OLS + controls often desk-rejected            |
| Mechanism                 | Near-mandatory; **step-wise mediation retired** (江艇 2022) | Estimate D→M, argue M→Y from theory — no endogenous mediation regression |
| References                | **Author-year (作者，年份)** [official]                     | **Not** numbered `[1][2]` / `[J][M]` style                 |
| Abstract                  | ~300-char 中文提要 + 5-element English Summary [official]    | English Summary needs a Chinese mirror for editing (not published; official sets no length) |
| Keywords                  | 3–5 + JEL codes                                            | Not 3–8                                                    |
| Policy implications       | "Significance" level, not action memos                     | Different from 《管理世界》 actionable-policy style         |
| Authorship                | ≤5 authors, ≤2 affiliations, one corresponding [official]  | Author info on a separate page; body anonymized            |

> Every fact above is verified and sourced in [`resources/official-source-map.md`](resources/official-source-map.md). Where the journal does not publish a hard limit (word/table/formula counts), the tools treat numbers as "rules of thumb — defer to the current author guidelines," never as hard assertions.

---

## The 18 Skills

**Framing:** `er-workflow` (router) · `er-topic-selection` · `er-introduction` · `er-literature-review` · `er-theory-hypotheses`

**Empirical core:** `er-data-sample` · `er-identification` · `er-mechanism` · `er-heterogeneity` · `er-robustness` · `er-tables-figures`

**Polish & submission:** `er-policy-implication` · `er-abstract` · `er-style` · `er-reviewer-lens` · `er-reproducibility` · `er-submission` · `er-rebuttal`

| Skill | Purpose |
|---|---|
| `er-workflow` | Router — decides which sub-skill to invoke next |
| `er-topic-selection` | Theoretical-grounding fit + contribution-sentence template |
| `er-introduction` | Five-part funnel intro, hook patterns, contribution teaser |
| `er-literature-review` | Bilingual structure + canonical-theory checklist + conversational review |
| `er-theory-hypotheses` | Theory section + testable hypothesis derivation |
| `er-data-sample` | Data note, formula-based variable table, descriptive stats |
| `er-identification` | Modern quasi-experimental design (staggered DID / IV / RDD / DML) |
| `er-mechanism` | Mechanism analysis — **post-江艇(2022)**: D→M + theory for M→Y |
| `er-heterogeneity` | Heterogeneity cuts: five-dimension priority + theory |
| `er-robustness` | Robustness system organized by identification threat |
| `er-tables-figures` | Three-line tables, variable table, figure aesthetics (code-exported) |
| `er-policy-implication` | Significance-level policy framing (not action-level) |
| `er-abstract` | 中文提要 + 5-element English Summary + blacklist scrub |
| `er-style` | Language polish: empty-significance → concrete contribution |
| `er-reviewer-lens` | Pre-submission self-audit of high-frequency reviewer critiques |
| `er-reproducibility` | One-click replication package + data-availability statement |
| `er-submission` | Pre-submission checklist + manuscript template |
| `er-rebuttal` | R&R response-letter structure |

---

## Runnable Code Library (Stata + Python)

[`resources/code/`](resources/code/) is a copy-and-run, one-click-reproducible empirical skeleton; command syntax is verified:

```
code/
 ├── stata/00_master.do        one-click master + fixed seed
 ├── stata/01_clean.do         merge, sample filtering, winsorize
 ├── stata/02_descriptive.do   summary stats + balance (three-line)
 ├── stata/03_did_modern.do    TWFE → Bacon → CS/BJS/SA/dCDH → event study
 ├── stata/04_iv.do            KP rk F + effective F + AR weak-IV-robust CI
 ├── stata/05_rdd.do           rdrobust bias-corrected CI + rddensity
 ├── stata/06_dml.do           ddml + pystacked multi-learner
 ├── stata/07_mechanism.do     D→M only (江艇 2022 stance)
 ├── stata/08_robustness.do    by-threat checks + placebo dist + wild bootstrap
 ├── stata/09_tables.do        esttab three-line tables + event-study figure
 └── python/                   clean_panel / dml_doubleml / event_study_plot
```

---

## Worked-Example Library (publication-grade, one case end-to-end)

[`resources/worked-examples/`](resources/worked-examples/) threads **one coherent empirical case** ("Golden Tax Phase III and firm TFP") through every section — introduction, theory & hypotheses, identification, mechanism (江艇 2022 stance), heterogeneity, robustness, abstract, policy, and an R&R response letter — with internally consistent numbers you can hold up as a target when revising a draft.

> The policy is real; all coefficients are illustrative and come from no published paper (see the directory's README disclaimer). It demonstrates the "generation" mode's quality bar: *"revise my draft to look like this."*

---

## Quick Start

```bash
/plugin marketplace add https://github.com/brycewang-stanford/Awesome-Journal-Skills
/plugin install economic-research-skills
/reload-plugins
```

Or copy manually: `mkdir -p ~/.claude/skills && cp -R skills/er-* ~/.claude/skills/`

First prompt:

```
Use er-workflow to tell me which skill I should use next for my Economic-Research manuscript.
```

---

## Methodological stance (what sets this apart from a generic writing assistant)

1. **Mechanism follows 江艇 (2022)**: drops step-wise mediation / Sobel / bootstrap indirect-effect shares; estimate D→M and argue M→Y from theory.
2. **Staggered DID must report a heterogeneity-robust estimator**: TWFE-only is flagged high-risk; ready-made commands for CS / BJS / SA / dCDH + Bacon decomposition + event study.
3. **Strict author-year references**: scrubs `[1][2]` / `[J][M]` / `[27,28,29]` numbered-citation residue.
4. **Exemplars only from verified papers**: avoids misattributing 《管理世界》 / 《中国工业经济》 classics to 《经济研究》 (see the source-map's pitfall table).

---

## What this repo does NOT do

- It does not judge whether your theoretical contribution is genuinely original — the researcher's call
- It does not simulate a specific reviewer (`er-reviewer-lens` only distills high-frequency, structural critiques for self-audit)
- It does not catalog rejection rates / impact factors
- Generated passages are **drafts** — verify and own them

---

## Related

- [Awesome-Journal-Skills](https://github.com/brycewang-stanford/Awesome-Journal-Skills) — Index of journal-specific skill packs
- [AER-skills](https://github.com/brycewang-stanford/AER-skills) — American Economic Review

---

## License

MIT
