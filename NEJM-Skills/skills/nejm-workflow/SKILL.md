---
name: nejm-workflow
description: Use when deciding which nejm-* sub-skill to invoke next, or when sequencing a clinical manuscript from significance test through response to reviewers for The New England Journal of Medicine. Routes — it does not replace — the specialized skills.
---

# NEJM Workflow Router (nejm-workflow)

## Overview

This is the router. It does not replace any specialized skill. It tells you **which nejm-* skill to use at the current stage** of a manuscript aimed at *The New England Journal of Medicine* (NEJM).

Default assumption: unless the user states otherwise, the target is **NEJM** (the flagship clinical journal), not *NEJM Evidence*, *NEJM AI*, or *NEJM Catalyst*. Those siblings share house style but differ in scope and audience — flag the difference if the user names one.

## When to trigger

- "What should I do next with this clinical manuscript?"
- A draft arrives and you must diagnose the current bottleneck.
- The user is switching between trial conduct, writing, and revision and has lost the thread.
- Reviews arrive from NEJM (often including a statistical reviewer) and you need to switch into response mode.

## The single most important gate

NEJM **rejects the large majority of submissions without external review**. The editorial bar is **practice-changing clinical impact backed by methodological rigor**, not merely a sound study. So the first question is never "is the analysis right?" — it is **"would this change how clinicians practice, and is it definitive enough to do so?"** Route to `nejm-fit` first, always.

## How NEJM differs from Lancet / JAMA / BMJ

- **NEJM**: famously **terse and plain**; Original Articles run a short main text (often ~2700 words); very high bar; **single-blind** review; favors large, definitive, practice-changing trials and landmark studies.
- **The Lancet**: similarly high bar, broader global-health and advocacy framing, structured abstract conventions of its own.
- **JAMA**: high bar with a strong structured-abstract and key-points discipline; large US clinical audience.
- **BMJ**: open-access, strong methods/registration culture, patient-partnership and open-data emphasis.

All four enforce ICMJE policy (trial registration, disclosures, data sharing), so the registration/reporting/ethics work transfers — but **format and tone do not**. Do not port a JAMA-styled manuscript across without re-styling abstract, references, and length.

## Article types (route by type)

- **Original Article** — definitive trials / major studies; full IMRAD; structured abstract.
- **Brief Report** — a smaller but important finding; shorter.
- **Review Article** — commissioned or vetted clinical synthesis.
- **Perspective / Editorial / Correspondence** — opinion and short-form; not original data.

## Routing table

| Current symptom                                                       | Next skill            |
|-----------------------------------------------------------------------|-----------------------|
| Not sure the result is practice-changing / definitive enough          | `nejm-fit`            |
| Trial not registered, or no protocol / statistical analysis plan ready | `nejm-study-design`  |
| Unsure which reporting checklist + flow diagram applies               | `nejm-reporting`      |
| No structured abstract; over 250 words; missing registration number   | `nejm-abstract`       |
| Main text bloated, over length, IMRAD unclear, discussion over-claims | `nejm-writing`        |
| P values without CIs; ITT unclear; subgroups over-interpreted         | `nejm-statistics`     |
| Need Table 1 / Kaplan–Meier / forest plot / CONSORT diagram done right | `nejm-figures-tables` |
| Missing IRB / consent / ICMJE disclosures / data-sharing statement     | `nejm-ethics`         |
| References not in Vancouver / ICMJE numbered style                     | `nejm-citation`       |
| About to submit; need a clinical preflight checklist                   | `nejm-submission`     |
| Received reviews (incl. a statistical reviewer) / an R&R decision       | `nejm-rebuttal`       |

## Default order

1. `nejm-fit` — clear the practice-changing / clinical-impact bar first
2. `nejm-study-design` — confirm registration + protocol + SAP and design rigor
3. `nejm-reporting` — pick the EQUATOR checklist and build the required diagram
4. `nejm-writing` — choose article type and hold the terse IMRAD form
5. `nejm-statistics` — CIs, ITT, multiplicity, pre-specified subgroups
6. `nejm-figures-tables` — Table 1, Kaplan–Meier, forest plots, CONSORT diagram
7. `nejm-ethics` — IRB, consent, ICMJE disclosures, data-sharing statement
8. `nejm-abstract` — structured ≤250-word abstract with registration number (late polish)
9. `nejm-citation` — Vancouver / ICMJE reference style (late polish)
10. `nejm-submission` — preflight (bundles cover letter + checklist templates)
11. `nejm-rebuttal` — after review

> `nejm-abstract` and `nejm-citation` are **late-stage polish**. Do not perfect the abstract before significance, design, and reporting are settled.

## Triage gate log

Run this gate sequence on any incoming clinical draft before routing. Answer each in order; the first NO names the next skill. Keep the filled-in log with the manuscript so co-authors see why work is sequenced this way.

```text
NEJM ROUTING TRIAGE — complete top to bottom, stop at the first NO
─────────────────────────────────────────────────────────────────
[ ] G1  Practice-changing? Would a clinician act differently on
        this result, and is it definitive enough to justify that?
        NO → nejm-fit (and consider a sibling journal instead)
[ ] G2  Prospectively registered, with protocol + SAP in hand?
        NO → nejm-study-design (surface this before any writing)
[ ] G3  Correct EQUATOR checklist chosen; flow diagram drafted?
        NO → nejm-reporting
[ ] G4  Main text terse IMRAD, near the ~2700-word Original
        Article norm, discussion free of over-claims?
        NO → nejm-writing
[ ] G5  CIs alongside P values; ITT stated; subgroups
        pre-specified and not over-read?
        NO → nejm-statistics
[ ] G6  Table 1 / Kaplan–Meier / forest plot / CONSORT diagram
        built to house conventions?              NO → nejm-figures-tables
[ ] G7  IRB, consent, ICMJE disclosures, data-sharing statement
        all present?                             NO → nejm-ethics
[ ] G8  Structured abstract ≤250 words with registration number?
        NO → nejm-abstract   (late polish only — after G1–G7)
[ ] G9  References in Vancouver / ICMJE numbered style?
        NO → nejm-citation   (late polish only)
ALL YES → nejm-submission; after reviews arrive → nejm-rebuttal
```

## Anti-patterns

- **Do not** skip `nejm-fit` and start polishing prose — the modal outcome is desk rejection.
- **Do not** start writing a trial up if it was **never prospectively registered** — route to `nejm-study-design` and surface that problem first.
- **Do not** draft a response to reviewers before the manuscript is actually revised.
- **Do not** assume Lancet/JAMA/BMJ formatting carries over unchanged.
