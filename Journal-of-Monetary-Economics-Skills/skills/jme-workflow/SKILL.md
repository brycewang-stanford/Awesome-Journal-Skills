---
name: jme-workflow
description: Use when deciding which jme-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through the "up or out" rebuttal for a Journal of Monetary Economics (JME) submission. Routes — it does not replace — the specialized skills.
---

# JME Workflow Router (jme-workflow)

## Overview

This is the router. It does not replace any specialized skill. It tells you **which jme-* skill to use at the current stage** of a manuscript aimed at the *Journal of Monetary Economics* (JME).

Default assumption: unless told otherwise, treat the target as JME — Elsevier's leading outlet for **monetary economics and macroeconomics broadly defined** (monetary theory and policy, central banking, business cycles, growth, financial intermediation, fiscal interactions, expectations), in both quantitative/DSGE and empirical/applied-policy modes. Operational tells you are at JME and not a generic top econ journal: submission via **Elsevier Editorial Manager** (`editorialmanager.com/monec/`); a **US$350 fee** (US$200 for full-time PhD students) charged **up front** (no fee on resubmission; half refunded on a direct return); **single anonymized** (single-blind) review with at least two reviewers; the distinctive **"up or out" first-revision rule** and the **~50% publication-likelihood threshold** for an R&R; a strict **40-page / ≤10 tables-and-figures** cap on accepted papers; a **100-word abstract** that may not begin with "This paper" or "We"; and the annual **Carnegie-Rochester-NYU Conference Series on Public Policy** issue. Editors are S. Borağan Aruoba (Maryland) and Eric Swanson (UC Irvine). Re-verify volatile specifics on the official page.

## When to trigger

- The user asks "what should I do next?"
- The user hands over a draft and needs the current bottleneck diagnosed
- Work is ping-ponging between the model, the empirics, writing, and the response letter
- A JME decision letter arrived (reject / revise-and-resubmit) and the user needs to switch modes

## Routing table

| Current symptom                                                          | Next skill                       |
|--------------------------------------------------------------------------|----------------------------------|
| Idea feels narrow / unclear fit with monetary-macro scope                | `jme-topic-selection`            |
| Contribution relative to the monetary-macro literature is fuzzy          | `jme-literature-positioning`     |
| The "what's new / why it matters for policy" pitch is undersold          | `jme-contribution-framing`       |
| Causal/structural identification of the shock or mechanism is undefended | `jme-identification-strategy`    |
| VAR/LP/DSGE estimation or moments need stress-testing                    | `jme-data-analysis`              |
| Too many exhibits for the 10-table-and-figure cap; IRFs unclear          | `jme-tables-figures`             |
| Prose buries the result; abstract begins with "This paper"/"We"          | `jme-writing-style`              |
| Need the ScienceDirect/Mendeley deposit + AI declaration ready           | `jme-replication-and-data-policy`|
| Want to understand single-blind review, two-referee, "up or out"         | `jme-review-process`             |
| Ready to submit via Editorial Manager; need the fee + 40-page preflight  | `jme-submission`                 |
| Received an R&R; the resubmission is "up or out"                         | `jme-rebuttal`                   |

## Default order

1. `jme-topic-selection` — confirm a first-order monetary/macro question and JME fit
2. `jme-literature-positioning` — stake the contribution against the frontier
3. `jme-contribution-framing` — sharpen the "what's new + policy lesson" claim
4. `jme-identification-strategy` — make the shock/mechanism identification credible
5. `jme-data-analysis` — VAR / local projections / DSGE estimation and robustness
6. `jme-tables-figures` — fit IRFs and tables under the ≤10 cap, online appendix for the rest
7. `jme-writing-style` — JME house style; 100-word abstract; author-date references
8. `jme-replication-and-data-policy` — ScienceDirect/Mendeley deposit + AI declaration
9. `jme-review-process` — understand single-blind, two-referee, "up or out", 50% threshold
10. `jme-submission` — Editorial Manager preflight (fee, 40 pages, line numbers, JEL codes)
11. `jme-rebuttal` — after the R&R (the resubmission must end in accept or reject)

> `jme-writing-style` is a late-stage polish. Do not rewrite the intro before the model and identification are settled — the argument will change.

## Decision shortcuts

- "Is my question monetary-macro enough for JME?" → `jme-topic-selection`
- "My TWFE/VAR shock is not really identified" → `jme-identification-strategy`
- "Should I report VAR and local projections?" → `jme-data-analysis`
- "I have 14 figures" → `jme-tables-figures`
- "My abstract starts with 'We'" → `jme-writing-style`
- "Editor may require my Dynare code" → `jme-replication-and-data-policy`
- "Submitting tomorrow; do I pay the fee now?" → `jme-submission`
- "Got an R&R — what does 'up or out' mean for me?" → `jme-rebuttal`

## Routing snapshot (copy, fill, keep at the top of the working notes)

```text
JME MANUSCRIPT ROUTING SNAPSHOT
================================================================
Venue          : Journal of Monetary Economics (Elsevier)
Portal         : Editorial Manager — editorialmanager.com/monec/
Editors        : S. Borağan Aruoba (Maryland) | Eric Swanson (UC Irvine)
Issue track    : [ ] regular   [ ] Carnegie-Rochester-NYU policy issue
Review model   : single-blind, at least two referees
Revision rule  : first revision is "up or out" — resubmission ends in
                 accept or reject; R&R only if publication likelihood
                 is judged roughly >= 50%

STAGE GATES — mark exactly one line CURRENT
[ ] G1  scope        question is aggregate/monetary ... jme-topic-selection
[ ] G2  positioning  frontier delta staked .......... jme-literature-positioning
[ ] G3  framing      "new + policy lesson" pitched .. jme-contribution-framing
[ ] G4  identification  shock/mechanism defended .... jme-identification-strategy
[ ] G5  estimation   VAR/LP/DSGE stress-tested ...... jme-data-analysis
[ ] G6  exhibits     IRFs/tables fit the cap ........ jme-tables-figures
[ ] G7  prose        house style applied ............ jme-writing-style
[ ] G8  deposit      replication package staged ..... jme-replication-and-data-policy
[ ] G9  process      review rules understood ........ jme-review-process
[ ] G10 submission   Editorial Manager preflight .... jme-submission
[ ] G11 rebuttal     up-or-out response drafted ..... jme-rebuttal

SUBMISSION PREFLIGHT (all must be Y before G10 closes)
[ ] Abstract <= 100 words; does NOT begin with "This paper" or "We"
[ ] Text + references + footnotes <= 40 pages (accepted-paper cap;
    online supplement exempt)
[ ] Tables + figures combined <= 10
[ ] Submission fee ready: US$350 (US$200 full-time PhD students),
    paid up front; no fee on resubmission
[ ] Generative-AI declaration included per Elsevier policy

BLOCKER LOG
- current bottleneck : ______________________________________
- routed sub-skill   : jme-__________________________________
- unverified fact to re-check on the official page: __________
```

Re-fill the snapshot after every decision letter: a reject closes the file; an R&R moves CURRENT straight to G11 with the up-or-out clock running.

## Anti-patterns

- **Do not** skip `jme-literature-positioning` and jump to estimation — referees judge the contribution first
- **Do not** polish exhibits while the shock identification or model is still shaky
- **Do not** treat the **40-page / ≤10 exhibit** cap as a final-stage edit — design for it from the start
- **Do not** let `jme-rebuttal` draft the response before the revised manuscript exists — and remember the resubmission is **up or out**, not another R&R round
