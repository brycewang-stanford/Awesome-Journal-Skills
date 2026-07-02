---
name: cc-workflow
description: Use when deciding which cc-* sub-skill to invoke next, or when sequencing a Cancer Cell (Cell Press) manuscript from scope check through peer-review revision. Routes — it does not replace — the specialized skills.
---

# Cancer Cell Workflow (cc-workflow)

## Overview

This is the router. It does not replace any specialized skill — it tells you **which cc-* skill to use at your current stage** of a Cancer Cell (Cell Press) molecular / translational oncology manuscript.

Default assumption: unless the user says otherwise, treat the target as **Cancer Cell**, where the bar is a clear molecular mechanism validated across orthogonal systems (cells + in vivo + ideally human data), reported with STAR Methods rigor, framed for translational relevance without overclaiming.

## When to trigger

- The user asks "what should I do next?"
- A draft arrives and you must diagnose the current bottleneck
- Work is thrashing between experiments, figures, and writing
- A decision letter / reviewer reports arrive and you must switch into revision mode

## Routing table

| Current symptom                                                        | Next skill                  |
|------------------------------------------------------------------------|-----------------------------|
| Unsure whether the story is a Cancer Cell paper at all                 | `cc-scope-fit`              |
| Mechanism rests on one system (cells only / no in vivo / no human data) | `cc-study-design`           |
| Controls, replicates, randomization, or blinding are unclear           | `cc-study-design`           |
| No Key Resources Table; cell lines unauthenticated; antibodies unvalidated | `cc-reporting-standards` |
| `n` undefined, pseudo-replication risk, wrong test, error bars unlabeled | `cc-statistics`            |
| Representative images with no quantification; multi-panel figure messy | `cc-figures-tables`         |
| Need Summary / Highlights / eTOC blurb / graphical abstract            | `cc-structured-abstract`    |
| Missing IACUC/IRB approval, consent, biosafety, or data-availability statement | `cc-ethics-registration` |
| Prose overclaims; Results read like a lab notebook; weak Discussion    | `cc-writing-style`          |
| Need a cover letter framing fit and significance                       | `cc-cover-letter`           |
| About to submit and need a final preflight                             | `cc-submission`             |
| Reviewer reports arrived; need a point-by-point response               | `cc-peer-review-revision`   |

## Default order

1. `cc-scope-fit` — confirm mechanism + translational relevance before investing more
2. `cc-study-design` — design / audit orthogonal validation, controls, replicates, in vivo rigor
3. `cc-reporting-standards` — STAR Methods, Key Resources Table, authentication, RRIDs
4. `cc-statistics` — define `n`, pick tests, correct for multiplicity, label error bars
5. `cc-figures-tables` — multi-panel mechanistic figures with quantification + image integrity
6. `cc-structured-abstract` — Summary, Highlights, eTOC blurb, graphical abstract
7. `cc-ethics-registration` — approvals, consent, biosafety, data-deposition statements
8. `cc-writing-style` — Cell Press prose and claim calibration (polish stage)
9. `cc-cover-letter` — significance / fit / suggested reviewers
10. `cc-submission` — pre-submission preflight
11. `cc-peer-review-revision` — after reviewer reports

> `cc-writing-style` and `cc-structured-abstract` are **late-stage polish** — do not finalize them while the mechanism or in vivo validation is still missing.

## Decision shortcuts

- "It's only in cell lines" → `cc-study-design` (add in vivo / human validation)
- "Reviewers will ask if the cell line is authenticated" → `cc-reporting-standards`
- "I used n=3 wells from one experiment" → `cc-statistics` (pseudo-replication)
- "I have a beautiful blot but no densitometry" → `cc-figures-tables`
- "My title promises a therapy but I have no in vivo efficacy" → `cc-scope-fit` then `cc-writing-style`
- "No GEO accession yet" → `cc-ethics-registration` / `cc-submission`
- "Three reviewers, consultative cross-review" → `cc-peer-review-revision`

## Differences vs. JAMA-style clinical packs

If the work is a clinical trial or epidemiological cohort with patient-level outcomes as the core unit, a clinical-trial pack (CONSORT / STROBE / registration) fits better. Cancer Cell's unit is a **mechanism validated across systems**, not a trial endpoint.

## Worked routing example

> "We have RNA-seq showing MARK7 correlates with CAF activation in a patient cohort, plus a knockdown
> migration phenotype in one PDAC line. We want to submit to Cancer Cell."

Route it:

1. `cc-scope-fit` — a correlation + single-line phenotype is **off-fit** on both pillars; the mechanism
   is not established and there is no in vivo/orthogonal validation. Gate here first.
2. `cc-study-design` — plan the missing spine: in vivo perturbation in an immunocompetent model, a
   second cell system, and a mechanistic intermediate linking MARK7 to the phenotype.
3. Only once that evidence exists do `cc-reporting-standards` → `cc-statistics` → `cc-figures-tables`
   apply; drafting front matter (`cc-structured-abstract`, `cc-writing-style`) before then is premature.

The router's job is to stop a promising-but-thin story from being polished into a confident desk reject.

## Stage diagnosis cues

| What the user says | Likely stage | Route |
|--------------------|--------------|-------|
| "Is this even a Cancer Cell paper?" | Pre-scope | `cc-scope-fit` |
| "Reviewers will ask about in vivo" | Design gap | `cc-study-design` |
| "My Methods feel thin" | Reporting | `cc-reporting-standards` |
| "Is n=3 wells enough?" | Statistics | `cc-statistics` |
| "The blot has no quantification" | Display | `cc-figures-tables` |
| "The Summary buries the finding" | Front matter | `cc-structured-abstract` |
| "I have no GEO accession" | Ethics/deposition | `cc-ethics-registration` |
| "Final check before upload" | Preflight | `cc-submission` |
| "Three reviewers came back" | Revision | `cc-peer-review-revision` |

## Anti-patterns

- **Do not** skip `cc-scope-fit` — editors triage on mechanism + translational fit first
- **Do not** let `cc-figures-tables` polish panels before `cc-statistics` has fixed `n` and tests
- **Do not** let `cc-peer-review-revision` draft a response before the revised experiments / text exist
- **Do not** route to front-matter polish while the in vivo or human-validation spine is still missing
- **Do not** treat a presubmission inquiry as a substitute for the scope gate — run `cc-scope-fit` regardless
