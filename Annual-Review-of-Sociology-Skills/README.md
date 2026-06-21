# Annual Review of Sociology Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Annual Review of Sociology Skills cover"></p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-ARSoc-1f5135)](https://www.annualreviews.org/content/journals/soc)
[![Index](https://img.shields.io/badge/index-review%20series-1f5135)](https://www.annualreviews.org/content/journals/soc)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://www.annualreviews.org/content/journals/soc)

English | [简体中文](README.zh-CN.md)

Twelve agent skills for **invited review articles** targeted at the **Annual Review of Sociology (ARSoc)** — the Annual Reviews (nonprofit) sociology survey series (founded 1975), whose Editorial Committee commissions authoritative reviews synthesizing sociology subfields (stratification, culture, organizations, networks, race/ethnicity, gender, demography, political and economic sociology) for sociologists across the discipline. Because ARSoc publishes no original empirical findings, the pack replaces identification and replication-package craft with **review craft**: scoping a synthesis-worthy subfield, the commissioning intake route, systematic comprehensive coverage, imposing an analytical spine instead of an annotated bibliography, fairness across schools and methods, who-found-what exhibits, the authoritative-yet-accessible voice that closes on a research agenda, and the transparency of the coverage account.

**Official basis checked 2026-06** (re-check volatile details before delivery): see [`resources/official-source-map.md`](resources/official-source-map.md).

## Why a separate stack?

| ARSoc constraint | What it forces |
|------------------|----------------|
| Intake | The Editorial Committee **commissions** topics/authors; **unsolicited manuscripts are not accepted** — you pitch a *topic*, not a finished paper |
| Artefact | An **invited review** that synthesizes others' work — no identification strategy, no replication package of your own |
| Audience | Accessible to **sociologists outside the subfield**, not only specialists |
| Spine | The contribution is an **analytical framework**, not an annotated bibliography |
| Balance | Even-handedness across theoretical **schools and methods** (quant, qual, computational, theoretical); no self-promotion |
| Sibling boundary | Distinct from **ASR / AJS** (primary research), **Sociological Theory** (theory development), and the sister **Annual Review of Psychology / Economics** |
| Source discipline | Editors, limits, style, and open-access status are cited or marked 待核实 |

## Quick Start

```text
/plugin marketplace add ./Annual-Review-of-Sociology-Skills
/plugin install annual-review-of-sociology-skills
```

Manual use: start with [`skills/arsoc-workflow/SKILL.md`](skills/arsoc-workflow/SKILL.md).

## Default Workflow

```text
arsoc-workflow → arsoc-topic-selection → arsoc-proposal-and-commissioning → arsoc-literature-synthesis →
arsoc-organizing-framework → arsoc-comprehensiveness-and-balance → arsoc-tables-figures → arsoc-writing-style →
arsoc-transparency-and-reproducibility → arsoc-editor-strategy → arsoc-submission → arsoc-revision
```

## Skills

| # | Skill | What it does |
|---|-------|--------------|
| 1 | [`arsoc-workflow`](skills/arsoc-workflow/SKILL.md) | Workflow router for ARSoc invited reviews |
| 2 | [`arsoc-topic-selection`](skills/arsoc-topic-selection/SKILL.md) | Is the subfield ARSoc-scale? The four fit tests |
| 3 | [`arsoc-proposal-and-commissioning`](skills/arsoc-proposal-and-commissioning/SKILL.md) | The invited/commissioning intake route and topic pitch |
| 4 | [`arsoc-literature-synthesis`](skills/arsoc-literature-synthesis/SKILL.md) | Systematic coverage across schools and methods |
| 5 | [`arsoc-organizing-framework`](skills/arsoc-organizing-framework/SKILL.md) | Imposing the analytical spine (vs. annotated bibliography) |
| 6 | [`arsoc-comprehensiveness-and-balance`](skills/arsoc-comprehensiveness-and-balance/SKILL.md) | Completeness, selectivity, and fairness across schools/methods |
| 7 | [`arsoc-tables-figures`](skills/arsoc-tables-figures/SKILL.md) | Who-found-what tables and the conceptual figure |
| 8 | [`arsoc-writing-style`](skills/arsoc-writing-style/SKILL.md) | The authoritative-accessible voice + forward-agenda close |
| 9 | [`arsoc-transparency-and-reproducibility`](skills/arsoc-transparency-and-reproducibility/SKILL.md) | Coverage account + any meta-analysis the review computes |
| 10 | [`arsoc-editor-strategy`](skills/arsoc-editor-strategy/SKILL.md) | Working with the Committee + the annual-volume timeline |
| 11 | [`arsoc-submission`](skills/arsoc-submission/SKILL.md) | Annual Reviews delivery preflight |
| 12 | [`arsoc-revision`](skills/arsoc-revision/SKILL.md) | Responding to Committee/referee feedback on a review |

## Resources

- [`resources/README.md`](resources/README.md) — resource index
- [`resources/official-source-map.md`](resources/official-source-map.md) — official URLs and volatile checks
- [`resources/external_tools.md`](resources/external_tools.md) — databases, synthesis tools, deposit repositories
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — fictional before/after review introduction
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real, web-verified ARSoc articles + guarded slots

This pack ships no `code/` directory: an ARSoc review reports no primary estimates, so there is no empirical replication kit. The shared method references are background only — used to *appraise* the studies a review synthesizes, not to run analysis of your own.

## Differences vs. sibling venues

| Venue | Relationship to ARSoc |
|-------|------------------------|
| **ASR / AJS** | Sociology's primary-research flagships — original empirical findings; ARSoc reviews them, it does not compete |
| **Sociological Theory** | Theory *development*, not a survey of accumulated evidence |
| **Annual Review of Psychology / Economics** | Sister Annual Reviews series; same commissioning model, adjacent disciplines |
| **Handbook chapter** | Deeper, longer, exhaustive; ARSoc reviews are bounded and accessible across subfields |

## Related Links

- https://www.annualreviews.org/content/journals/soc
- https://www.annualreviews.org/page/authors/general-information
- https://www.annualreviews.org/page/authors/editorial-policies

## License

MIT (c) 2026 Bryce Wang. See [LICENSE](LICENSE).
