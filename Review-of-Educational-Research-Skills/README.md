# Review of Educational Research Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Review of Educational Research Skills cover"></p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Review%20of%20Educational%20Research-8a5a12)](https://journals.sagepub.com/home/rer)
[![Index](https://img.shields.io/badge/index-AERA%20%C2%B7%20SAGE-1a1a1a)](https://www.aera.net/Publications/Journals/Review-of-Educational-Research)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-skills-d97757)](https://github.com/brycewang-stanford/review-of-educational-research-skills)

English | [简体中文](README.zh-CN.md)

Twelve agent skills for **Review of Educational Research (RER)** systematic reviews, meta-analyses, and critical integrative syntheses. RER is the **American Educational Research Association's (AERA)** review journal of record, published by **SAGE** (founded 1931): it publishes **comprehensive, critical, integrative reviews of research bearing on education** and **does not publish original empirical research** unless it is incorporated in a broader review. Crucially — unlike an invited *Annual Review* — RER reviews are **submitted and peer-reviewed**, so the rigor of the **review itself** (a documented PRISMA search, reliable coding, defensible meta-analytic models, risk-of-bias and sensitivity analysis, and an organizing framework that advances theory or policy) is the contribution. This pack is built for that work: scoping a synthesis-worthy question, a preregistered protocol, systematic search and screening, the conceptual framework, comprehensiveness with robustness, PRISMA/MARS transparency, RER's masked APA-7 house style, submission, and revision.

**Official basis checked 2026-06**: see [`resources/official-source-map.md`](resources/official-source-map.md).

## Why a separate stack?

A review for RER is not a primary-research paper, and its constraints are specific:

| Constraint | What RER expects (检索于 2026-06；以官网为准) |
|---|---|
| Artefact | Comprehensive, **critical, integrative review** — no original empirical research of the author's own |
| Process rigor | Systematic reviews/meta-analyses need a documented search + **PRISMA flow**, reliable double-coding, risk-of-bias, and sensitivity analysis |
| Contribution | An **organizing framework that advances theory or policy** — not an annotated bibliography or a vote-count |
| Style | **APA 7th edition**; **abstract ≤ 150 words** + keywords; **Microsoft Word** (not PDF) |
| Review model | **Masked** review; only **limited-circulation** self-citations anonymized; unblinded title page + blinded manuscript + Author Bios |
| Reporting | Consult **PRISMA** + APA **Reporting Standards** (MARS/JARS); PROSPERO/OSF registration is good practice |

## Quick Start

```
/plugin marketplace add ./Review-of-Educational-Research-Skills
/plugin install review-of-educational-research-skills
```

Manual use: start with [`skills/revedres-workflow/SKILL.md`](skills/revedres-workflow/SKILL.md).

## Default Workflow

```
topic-selection → proposal-and-commissioning → literature-synthesis → organizing-framework
   → comprehensiveness-and-balance → tables-figures → writing-style
   → transparency-and-reproducibility → editor-strategy → submission → revision
                         (revedres-workflow routes at every step)
```

## Skills

| # | Skill | Role |
|---|-------|------|
| 1 | [`revedres-workflow`](skills/revedres-workflow/SKILL.md) | Route an RER review project |
| 2 | [`revedres-topic-selection`](skills/revedres-topic-selection/SKILL.md) | Test whether the question is synthesis-worthy and RER-scale |
| 3 | [`revedres-proposal-and-commissioning`](skills/revedres-proposal-and-commissioning/SKILL.md) | Write and preregister the protocol before searching |
| 4 | [`revedres-literature-synthesis`](skills/revedres-literature-synthesis/SKILL.md) | Run the systematic search and screen to a PRISMA flow |
| 5 | [`revedres-organizing-framework`](skills/revedres-organizing-framework/SKILL.md) | Turn the corpus into an analytic spine that advances theory/policy |
| 6 | [`revedres-comprehensiveness-and-balance`](skills/revedres-comprehensiveness-and-balance/SKILL.md) | Exhaustiveness, risk-of-bias, heterogeneity, sensitivity |
| 7 | [`revedres-tables-figures`](skills/revedres-tables-figures/SKILL.md) | PRISMA flow, forest/funnel plots, coding tables |
| 8 | [`revedres-writing-style`](skills/revedres-writing-style/SKILL.md) | Write the synthesizing RER voice in APA 7 |
| 9 | [`revedres-transparency-and-reproducibility`](skills/revedres-transparency-and-reproducibility/SKILL.md) | Coding reliability, open materials, PRISMA/MARS |
| 10 | [`revedres-editor-strategy`](skills/revedres-editor-strategy/SKILL.md) | Work with AERA/SAGE editor and reviewer expectations |
| 11 | [`revedres-submission`](skills/revedres-submission/SKILL.md) | Run the Manuscript Central preflight |
| 12 | [`revedres-revision`](skills/revedres-revision/SKILL.md) | Revise after the decision letter |

## Resources

- [`resources/README.md`](resources/README.md) — resource index
- [`resources/official-source-map.md`](resources/official-source-map.md) — official SAGE/AERA RER sources
- [`resources/external_tools.md`](resources/external_tools.md) — discovery, screening, coding, and meta-analysis tools
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — a before→after review introduction in RER style
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real, web-verified RER reviews by type

## Differences vs. sibling journals

| Journal | Relationship to RER |
|---|---|
| **AERJ / *AERA Open*** | AERA primary-research journals — send original empirical studies there, not to RER |
| ***Educational Researcher*** | Short AERA commentary, policy essays, methodological briefs — not comprehensive reviews (shares the `10.3102/` DOI stem) |
| ***Review of Research in Education*** | AERA's **commissioned** thematic review volumes — RER reviews are unsolicited and submitted |
| ***Psychological Bulletin*** | Psychology reviews — RER is the education review-of-record |
| **Annual Reviews** | **Invited** non-systematic overviews — RER reviews are submitted and judged on systematic rigor |

## License

MIT (c) 2026 Bryce Wang. See [LICENSE](LICENSE).
