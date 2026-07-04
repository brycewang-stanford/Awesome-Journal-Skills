---
name: jfe-workflow
description: Use when deciding which jfe-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a Journal of Financial Economics (JFE) manuscript. Routes — it does not replace — the specialized skills.
---

# JFE Workflow Router (jfe-workflow)

## Overview

This is the router. It does not do the work of any specialized skill; it tells you **which jfe-* skill to use at the current stage** of a Journal of Financial Economics (JFE) manuscript.

Default assumption: unless you say the target is a different outlet, work to JFE's culture — nuts-and-bolts methodological rigor, exhaustive robustness, and credible identification. JFE papers are typically more technical, longer, and more robustness-heavy than JF, and the referee culture rewards thoroughness over a single clever result.

JFE at a glance (verify on jfinec.com): Elsevier/North-Holland, ISSN 0304-405X, founded 1974 by Michael C. Jensen; Editor-in-Chief Toni M. Whited (Michigan) with co-editors at Kellogg, Wharton, and NYU Stern; submit via **editorialmanager.com/finec** with a **US$850** fee (discounted by referee-earned submission rights; no fee on R&R); **100-word abstract**, double-spaced author-date format; mandatory **code + non-proprietary-data** deposit to Mendeley Data for post-2021 submissions; the **Jensen Prize** (corp fin) and **Fama-DFA Prize** (asset pricing) are its best-paper awards.

## When to trigger

- You ask "what should I do next?" on a JFE-bound paper
- You hand over a draft and need the current bottleneck diagnosed
- You keep bouncing between empirics, writing, and the response letter and have lost the thread
- You received a JFE decision letter and need to switch into revision mode

## Routing table

| Current symptom                                                      | Next skill                  |
|----------------------------------------------------------------------|-----------------------------|
| Idea is vague; unsure it clears the JFE contribution bar             | `jfe-topic-selection`       |
| Related-work section is a list; unclear how you differ from JF/RFS   | `jfe-literature-positioning`|
| Empirics are OLS + controls; identification is undefended            | `jfe-identification`        |
| Design choices unsettled (factor construction, estimator, SE, GMM)   | `jfe-empirical-design`      |
| Main result exists but is fragile / under-stressed                   | `jfe-robustness`            |
| Tables overloaded; figures unclear; not JFE house style              | `jfe-tables-figures`        |
| Robustness, proofs, and extra tests are crowding the main text       | `jfe-internet-appendix`     |
| Prose is vague, hedged, or buries the contribution                   | `jfe-writing-style`         |
| Ready to submit; need a preflight checklist                          | `jfe-submission`            |
| Want to anticipate and pre-empt likely referee objections            | `jfe-referee-strategy`      |
| Received an R&R and need to write the response                       | `jfe-rebuttal`              |

## Default order

1. `jfe-topic-selection` — lock the contribution and economic question
2. `jfe-literature-positioning` — situate against the top-3 finance frontier
3. `jfe-identification` — make the causal/inference design defensible
4. `jfe-empirical-design` — factor construction, estimators, standard errors, GMM
5. `jfe-robustness` — stress every result until it does not break
6. `jfe-tables-figures` — finalize main exhibits
7. `jfe-internet-appendix` — move proofs and supplementary tests off the main text
8. `jfe-writing-style` — polish prose to JFE register
9. `jfe-submission` — pre-submission preflight
10. `jfe-referee-strategy` — pre-empt objections before and during review
11. `jfe-rebuttal` — after the R&R

> `jfe-writing-style` and parts of `jfe-tables-figures` are **late-stage polish**. Do not burn effort there while identification or the core design is still unsettled — JFE referees will not be charmed by clean tables sitting on a weak design.

## Bottleneck triage card

Answer the questions in order and stop at the **first "no"** — that is the skill to invoke now. Everything below the first "no" is premature polish.

```text
JFE bottleneck triage — run top to bottom, stop at first "no"
-------------------------------------------------------------------------
Q1  Can you state the contribution in one sentence a co-editor
    would care about?                          no -> jfe-topic-selection
Q2  Does related work say why JF/RFS haven't already covered it?
                                               no -> jfe-literature-positioning
Q3  Would the identification survive a hostile referee report?
    (staggered-DID bias addressed? instrument defended?)
                                               no -> jfe-identification
Q4  Are factor construction, estimator, SEs, and GMM choices
    settled and justified?                     no -> jfe-empirical-design
Q5  Does the result survive the obvious alternative specs a
    thorough JFE referee will run?             no -> jfe-robustness
Q6  Are main exhibits readable and in JFE house style?
                                               no -> jfe-tables-figures
Q7  Are proofs and extra tests offloaded to the Internet Appendix?
                                               no -> jfe-internet-appendix
Q8  Is the prose at JFE register, contribution up front,
    abstract at 100 words?                     no -> jfe-writing-style
-------------------------------------------------------------------------
All yes -> jfe-submission (editorialmanager.com/finec preflight: fee,
           Mendeley Data code/data deposit), then jfe-referee-strategy.
Decision letter arrived -> revise first, then jfe-rebuttal.
```

## Decision shortcuts

- "I have data but no sharp economic question" -> `jfe-topic-selection`
- "Related work doesn't say why JF or RFS wouldn't already cover this" -> `jfe-literature-positioning`
- "DID is two-way FE with staggered adoption and I haven't addressed the bias" -> `jfe-identification`
- "I sort on a characteristic but haven't justified the factor or the breakpoints" -> `jfe-empirical-design`
- "Result holds in the baseline but I haven't tried obvious alternative specs" -> `jfe-robustness`
- "Main table has 12 columns and no one can read it" -> `jfe-tables-figures`
- "Referee will want 20 extra tables I can't fit" -> `jfe-internet-appendix`
- "Submitting this week" -> `jfe-submission`
- "Reviewer 2 will ask about endogeneity / multiple testing" -> `jfe-referee-strategy`
- "Got three referee reports back" -> `jfe-rebuttal`

## Differences vs. the JF and RFS stacks

JFE is published by **Elsevier** and is editor-driven (Whited + co-editors), unlike **JF** (American Finance Association, Wiley) and **RFS** (Society for Financial Studies, Oxford UP) — so the fee structure, the `finec` Editorial Manager portal, and the masthead are all JFE-specific; do not recycle a JF/RFS cover letter. If the paper is a shorter, idea-forward piece where a single clean result carries the day, the JF stack may fit better; if it leans heavily on theory or method, the RFS stack may fit better. The core JFE difference: referees reward methodological thoroughness and exhaustive robustness, the Internet Appendix is expected to be deep and is appended to the main file, and the US$850 fee plus referee-earned submission rights shape the whole submission economy. Verify each journal's current scope on its official page.

## Anti-patterns

- **Do not** skip `jfe-literature-positioning` and jump to identification — referees first ask "why is this not already known?"
- **Do not** let `jfe-tables-figures` beautify exhibits while the design is still contested
- **Do not** let `jfe-rebuttal` draft a response letter before you have actually revised the manuscript and re-run the affected results
