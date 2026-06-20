---
name: hrm-workflow
description: Use when deciding which hrm-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a Human Resource Management (Wiley "HRM") submission. Routes — it does not replace — the specialized skills.
---

# HRM Workflow Router (hrm-workflow)

## Overview

This is the router for a manuscript aimed at *Human Resource Management* — the **Wiley** US-based "HRM" journal (Online ISSN 1099-050X; Print ISSN 0090-4848), a leading outlet for strategic HRM, HR systems and practices, the employment relationship, talent, performance, and well-being, and HR's link to firm and unit outcomes. Its defining feature is a **dual contribution bar**: a paper must advance the academic literature (theoretically, empirically, and/or methodologically) **and** carry practical significance — clear implications for workforce policy or HRM practice. A purely psychological micro-paper with no HR-system or practice angle, or a purely managerial think-piece with no scholarly advance, sits at the desk-reject boundary.

Operational tells you are at HRM and not a sibling: HRM accepts the **full range** of designs (conceptual, empirical, meta-analytic, critical review; qualitative or quantitative; inductive, deductive, or abductive) and explicitly spans **micro, macro, and multi-level** phenomena; review is **double-blind** (anonymized manuscript + separate title page); the **Editor-in-Chief screens for fit and relevance before review**; references use **APA** style; Wiley's **data-availability** policy applies. Co-Editors-in-Chief: **Fang Lee Cooke; Shaun Pichler (Co-EIC from Jan 2025)** (检索于 2026-06；以官网为准). Submission via Wiley **ScholarOne / Manuscript Central** (检索于 2026-06；以官网为准).

## Sibling guard (do not confuse)

- **Human Resource Management Journal (HRMJ)** — a DIFFERENT, UK/CIPD-linked Wiley journal (ISSN 1748-8583); more critical/European employment-relations framing.
- **Personnel Psychology** and **Journal of Applied Psychology** — micro/psychometric, individual-level; HRM wants the HR-system, unit, or firm tie.
- **Academy of Management Journal** — broader management theory-test; HRM expects an HR-practice/policy payoff.

## When to trigger

- The user asks "what should I do next?" on an HRM-bound paper
- A draft's current bottleneck (fit, theory, design, evidence, exhibits, prose, submission, revision) is unclear
- Work is ping-ponging between framing, multilevel design, analysis, and the response letter
- A double-blind decision letter arrived and the user must switch into revision mode

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Scope/audience/outlet fit uncertain; no practice payoff | `hrm-topic-selection` |
| HRM/OB mechanism thin; hypotheses are bald predictions | `hrm-theory-development` |
| Contribution vs. HRMJ / PPsych / JAP / AMJ is fuzzy | `hrm-literature-positioning` |
| Design (multilevel, multi-source/wave, CMB, construct validity) shaky | `hrm-methods` |
| Estimation (HLM/SEM), aggregation, or qualitative coding needs work | `hrm-data-analysis` |
| The dual "so what — theory AND practice" claim is not sharp | `hrm-contribution-framing` |
| Exhibits dense; correlation table / interaction plots not reader-ready | `hrm-tables-figures` |
| Intro/abstract bury the idea; practitioner takeaway invisible | `hrm-writing-style` |
| Ready to submit; need ScholarOne preflight + anonymization check | `hrm-submission` |
| Want the desk-screen / double-blind / R&R timeline expectations | `hrm-review-process` |
| Received an R&R; need a response-letter strategy | `hrm-rebuttal` |

## Default order

1. `hrm-topic-selection` — lock an HR-system/practice question with a practice payoff
2. `hrm-theory-development` — build the HRM/OB mechanism and hypotheses (a priori)
3. `hrm-literature-positioning` — stake the contribution vs. HRMJ/PPsych/JAP/AMJ
4. `hrm-methods` — multilevel, multi-source/multi-wave, construct validity, CMB design
5. `hrm-data-analysis` — HLM/SEM, aggregation justification, mediation/moderation
6. `hrm-contribution-framing` — sharpen the dual theory-AND-practice claim
7. `hrm-tables-figures` — correlation table, model build-up, interaction plots
8. `hrm-writing-style` — make the idea and the takeaway land (abstract + intro last)
9. `hrm-submission` — ScholarOne preflight, anonymization, data statement
10. `hrm-review-process` — calibrate desk-screen and developmental R&R expectations
11. `hrm-rebuttal` — after the R&R

> `hrm-writing-style` is late-stage polish; do not rewrite the intro before the theory and the multilevel design settle.

## Routing by paper archetype

HRM publishes several archetypes, and the binding constraint differs. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| Strategic HRM / HR-system → firm performance | construct of the HR system + endogeneity of adoption | `hrm-methods` → `hrm-data-analysis` |
| Multilevel HR practices → employee attitudes/behavior | aggregation justification + cross-level model | `hrm-theory-development` → `hrm-methods` |
| Employment-relationship / social-exchange micro | common-method bias + temporal separation | `hrm-methods` |
| Qualitative / case (talent, change, well-being) | grounded rigor + transparent practice payoff | `hrm-theory-development` → `hrm-data-analysis` |
| Meta-analysis / critical review | coverage, coding reliability, HR-practice synthesis | `hrm-literature-positioning` → `hrm-data-analysis` |

## Worked routing example (illustrative)

A user says: "My firm-level study shows high-performance work systems raise productivity, but a reviewer says HPWS adoption is endogenous and the paper has no clear takeaway for HR directors." Two distinct HRM pushbacks: *adoption endogeneity* (owned by `hrm-methods` → `hrm-data-analysis`, where the identification strategy lives) and *the missing practice payoff* (owned by `hrm-contribution-framing`). Route to methods/data first; only once the HPWS coefficient is defensible (say it settles at a 0.18 SD productivity gain, illustrative) do you return to framing to spell out what an HR leader should do differently.

## Anti-patterns

- Treating HRM as interchangeable with **HRMJ** (the UK journal) — wrong portal, wrong house framing
- Submitting a micro/psychometric paper with no HR-system, unit, or firm tie (belongs at PPsych/JAP)
- Submitting a managerial essay with no scholarly advance (no theory/empirics/method contribution)
- Polishing prose before the multilevel design, contribution, and evidence hierarchy are stable
- Letting an online supplement carry claims the main text must establish

## Output format

```text
【Target】Human Resource Management (Wiley "HRM")
【Current bottleneck】fit / theory / positioning / design / evidence / exhibits / style / submission / revision
【Archetype】strategic-HRM / multilevel / employment-relationship / qualitative / meta-review
【Next skill】<one hrm-* skill>
【Reason】why this is the binding constraint
【Source check】official facts verified or marked 检索于 2026-06；以官网为准 / 待核实
```
