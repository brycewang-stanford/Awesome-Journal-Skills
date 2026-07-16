---
name: aos-workflow
description: Use when deciding which aos-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for an Accounting, Organizations and Society (AOS) manuscript. Routes — it does not replace — the specialized skills.
---

# Accounting, Organizations and Society Workflow (aos-workflow)

## Overview

This is the router. It never does the stage work itself; its only job is to name **the one aos-* skill you should open right now**.

Default target: **Accounting, Organizations and Society (AOS)** — the flagship interdisciplinary accounting journal, launched in 1976 by Anthony Hopwood and published by **Elsevier** (ISSN 0361-3682). AOS exists to study accounting as a **social, organizational, behavioral and institutional phenomenon**, not merely as an input to security prices. Its pages mix qualitative field studies, experimental/behavioral work, surveys, historical and critical scholarship, and archival designs that carry genuine organizational or social theorizing. What AOS is **not** is a capital-markets outlet: a JAR/JAE/TAR-style archival-financial-economics paper with no social or organizational theory is the journal's canonical desk reject. Every routing decision below therefore starts from **which intellectual tradition your paper works in**, because the rigor bar, exemplars, and reviewer pool differ sharply between a Bourdieusian field study and a judgment-and-decision-making experiment.

> Current masthead (verified 2026-07-16): joint Editors-in-Chief **Marcia Annisette** (Schulich School of Business), **Martin Messner** (University of Innsbruck), and **Hun-Tong Tan** (Nanyang Technological University), supported by a large interdisciplinary editorial board. Submissions run through Editorial Manager (editorialmanager.com/AOS) under double-anonymized review. Editors and portal details change — re-check the official Elsevier/ScienceDirect pages before relying on any of this.

## When to trigger

- "What should I do next?" with a half-built AOS manuscript
- You have rich field material or clean experimental results but no argument about what they say to AOS
- A reviewer challenges your theorizing (qualitative), your construct operationalization (experimental), or your paper's fit with the journal's social/organizational mission
- An AOS decision letter arrived and you must switch into response mode
- You keep oscillating between coding data, reading theory, and rewriting the front end

## Routing table

| Current symptom                                                              | Next skill                   |
|------------------------------------------------------------------------------|------------------------------|
| Unsure the question is about accounting's organizational/social life at all  | `aos-topic-selection`        |
| Data exist but no theoretical lens (or the lens is decorative)               | `aos-theory-development`     |
| Front end lists citations without joining an AOS conversation                | `aos-literature-positioning` |
| Field access, case selection, experiment design, or ethics unsettled         | `aos-methods`                |
| Material collected; coding, analysis, or statistical treatment unclear       | `aos-data-analysis`          |
| Findings exist but the theoretical "so what" is thin                         | `aos-contribution-framing`   |
| Exhibits (data-structure tables, cell means, figures) weak or absent         | `aos-tables-figures`         |
| Prose reads like a hypothesis-mill or buries the argument                    | `aos-writing-style`          |
| Ready for Editorial Manager; need the preflight                              | `aos-submission`             |
| Want to understand how AOS editors and reviewers will treat the paper        | `aos-review-process`         |
| Revise-and-resubmit received; must plan the revision and letter              | `aos-rebuttal`               |

## Default order

1. `aos-topic-selection` — confirm the question belongs at the accounting–organization–society intersection
2. `aos-theory-development` — commit to a theoretical tradition and make it do real work
3. `aos-literature-positioning` — enter a live AOS conversation (the journal has 50 years of its own canon)
4. `aos-methods` — design the field study / experiment / survey / historical inquiry, with ethics settled early
5. `aos-data-analysis` — code, analyze, or estimate to the standard of your tradition
6. `aos-contribution-framing` — state what the paper changes in how we understand accounting's social life
7. `aos-tables-figures` — build exhibits that carry evidence, not decoration
8. `aos-writing-style` — polish the argumentative, theory-carrying prose AOS expects
9. `aos-submission` — Editorial Manager preflight (anonymized files, declarations, title page)
10. `aos-review-process` — calibrate for triage by the joint EiCs and interdisciplinary referees
11. `aos-rebuttal` — after an R&R, revise substantively, then draft the response

> Steps 7–8 are polish. Touching them while the theoretical lens or the empirical design is still moving wastes the work twice.

## Decision shortcuts

- "I have 60 interviews and no story" → `aos-theory-development`, not more fieldwork
- "My experiment works but reviewers may ask why it matters beyond psychology" → `aos-contribution-framing`
- "Is my archival tax paper an AOS paper?" → `aos-topic-selection` (probably not, unless the theorizing is social/institutional)
- "Which Foucault/Bourdieu/ANT sources does AOS itself rely on?" → `aos-literature-positioning`
- "Submitting this month — what does Editorial Manager want?" → `aos-submission`
- "Two reviewers from different disciplines disagree" → `aos-review-process` then `aos-rebuttal`

## Stage tracker (fill and re-run the router)

The *tradition* row governs everything downstream — a field study and an experiment share almost no stage-level standards at AOS. Set it first; then the top unfinished stage names the next skill.

```
AOS MANUSCRIPT — stage tracker
question   : [one sentence: which social/organizational aspect of accounting?]
tradition  : qualitative-field / experimental-behavioral / survey /
             historical-critical / archival-with-social-theory
target     : AOS (vs MAR / AAAJ / CPA / CAR / BRIA)  fit=[yes/borderline/no]

stage                             status        next skill
--------------------------------  ------------  ---------------------------
scope & tradition                 [done]        aos-topic-selection
theoretical lens                  [in-progress] aos-theory-development
conversation entry                [todo]        aos-literature-positioning
design, access & ethics           [todo]        aos-methods
coding / analysis / estimation    [todo]        aos-data-analysis
theoretical contribution          [todo]        aos-contribution-framing
exhibits                          [todo]        aos-tables-figures   (late)
prose                             [todo]        aos-writing-style    (late)
Editorial Manager preflight       [todo]        aos-submission
decision / R&R                    [—]           aos-review-process → aos-rebuttal

rule: the theoretical lens and the design must both be settled
      before any (late) row is touched.
```

## Anti-patterns

- **Do not** run a capital-markets manuscript through this stack hoping polish will fix the scope problem — AOS desk-rejects the genre, not the sentences.
- **Do not** give a qualitative field paper and a behavioral experiment the same analysis advice; their evidence logics are incommensurable.
- **Do not** open `aos-writing-style` while the paper still has no theoretical argument to express.
- **Do not** draft a rebuttal before the manuscript itself has actually changed.
