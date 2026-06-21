# Annual Review of Psychology Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Annual Review of Psychology Skills cover"></p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-ARPsych-5a2a4a)](https://www.annualreviews.org/journal/psych)
[![Index](https://img.shields.io/badge/index-invited%20reviews-5a2a4a)](https://www.annualreviews.org/journal/psych)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://www.annualreviews.org/journal/psych)

English | [简体中文](README.zh-CN.md)

Twelve agent skills for **invited review articles** targeted at the **Annual Review of Psychology (ARPsych)** — the *Annual Reviews* (nonprofit) survey series, founded 1950 and among the highest-impact journals in the field. The pack is tuned to commissioned, authoritative reviews that synthesize a topic across cognitive, social, developmental, clinical, biological/neuro, I-O, and methods psychology for the whole field and adjacent disciplines. It keeps the manuscript distinct from *Psychological Bulletin* (submitted reviews/meta-analyses), *Annual Review of Clinical Psychology* (the clinical sister), and *Perspectives on Psychological Science* (essays), and it emphasizes the one thing that makes or breaks a review of record: an **organizing framework** that turns a literature into an argument.

**Official basis checked 2026-06** (re-check volatile details before delivery): see [`resources/official-source-map.md`](resources/official-source-map.md).

## Why a separate stack?

| ARPsych constraint | What it forces |
|--------------------|----------------|
| Invitation-only | Articles are **commissioned by the Editorial Committee**; you earn an invitation, you do not cold-submit (检索于 2026-06；以官网为准) |
| Review, not research | The artefact **appraises others' studies**; there is no preregistration or power analysis of your own |
| Organizing framework | A spine (taxonomy / process / levels / theory-contest) is the contribution; an annotated bibliography fails |
| Balance is editorial currency | The Committee judges **accuracy, rigor, and balance**; self-promotion and advocacy are punished |
| Broad readership | Authoritative **yet accessible** to a psychologist outside the subfield |
| Sibling boundary | Must belong here, not Psychological Bulletin / ARClinPsych / Perspectives |
| Source discipline | Current process facts are cited or marked 待核实 |

## Quick Start

```text
/plugin marketplace add ./Annual-Review-of-Psychology-Skills
/plugin install annual-review-of-psychology-skills
```

Manual use: start with [`skills/arpsych-workflow/SKILL.md`](skills/arpsych-workflow/SKILL.md).

## Default Workflow

```text
arpsych-workflow → arpsych-topic-selection → arpsych-proposal-and-commissioning → arpsych-literature-synthesis → arpsych-organizing-framework → arpsych-comprehensiveness-and-balance → arpsych-tables-figures → arpsych-writing-style → arpsych-transparency-and-reproducibility → arpsych-editor-strategy → arpsych-submission → arpsych-revision
```

## Skills

| # | Skill | What it does |
|---|-------|--------------|
| 1 | [`arpsych-workflow`](skills/arpsych-workflow/SKILL.md) | Workflow router for ARPsych invited reviews |
| 2 | [`arpsych-topic-selection`](skills/arpsych-topic-selection/SKILL.md) | Is the topic mature, important, and synthesis-ready? |
| 3 | [`arpsych-proposal-and-commissioning`](skills/arpsych-proposal-and-commissioning/SKILL.md) | The Editorial-Committee invitation cycle |
| 4 | [`arpsych-literature-synthesis`](skills/arpsych-literature-synthesis/SKILL.md) | Systematic, documentable coverage of the literature |
| 5 | [`arpsych-organizing-framework`](skills/arpsych-organizing-framework/SKILL.md) | The analytical spine that carries the review |
| 6 | [`arpsych-comprehensiveness-and-balance`](skills/arpsych-comprehensiveness-and-balance/SKILL.md) | Even-handed coverage; credibility weighting; no self-promotion |
| 7 | [`arpsych-tables-figures`](skills/arpsych-tables-figures/SKILL.md) | The framework figure and synthesis tables |
| 8 | [`arpsych-writing-style`](skills/arpsych-writing-style/SKILL.md) | The authoritative-yet-accessible ARPsych voice |
| 9 | [`arpsych-transparency-and-reproducibility`](skills/arpsych-transparency-and-reproducibility/SKILL.md) | Documented search; reproducible meta-analysis |
| 10 | [`arpsych-editor-strategy`](skills/arpsych-editor-strategy/SKILL.md) | Scope, length, deadlines, production timeline |
| 11 | [`arpsych-submission`](skills/arpsych-submission/SKILL.md) | Annual Reviews delivery preflight |
| 12 | [`arpsych-revision`](skills/arpsych-revision/SKILL.md) | Responding to the Editor and Committee |

## Resources

- [`resources/README.md`](resources/README.md) — resource index
- [`resources/official-source-map.md`](resources/official-source-map.md) — official Annual Reviews URLs and volatile checks
- [`resources/external_tools.md`](resources/external_tools.md) — databases, search tools, and meta-analysis software
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — fictional before/after introduction
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — web-verified real ARPsych articles + sibling guardrails

## Differences vs. sibling venues

| Venue | Intake | Artefact | This pack's stance |
|-------|--------|----------|--------------------|
| **Annual Review of Psychology** | invited by Editorial Committee | authoritative survey of record | the target — framework-first review craft |
| **Psychological Bulletin** | **submitted** | review / meta-analysis | route here if you want to submit a stand-alone meta-analysis |
| **Annual Review of Clinical Psychology** | invited (sister series) | clinical-science survey | route here if the audience is clinical scientists |
| **Perspectives on Psychological Science** | submitted | shorter, opinionated essay | route here for a provocative argument, not a survey |

## Related Links

- https://www.annualreviews.org/journal/psych
- https://www.annualreviews.org/page/authors/general-information
- https://www.annualreviews.org/page/authors/editorial-policies

## License

MIT (c) 2026 Bryce Wang. See [LICENSE](LICENSE).
