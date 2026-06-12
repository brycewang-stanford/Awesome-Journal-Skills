---
name: lancet-workflow
description: Use when deciding which lancet-* sub-skill to invoke next, or when sequencing a clinical or global-health manuscript from significance test through reviewer rebuttal for The Lancet. Routes — it does not replace — the specialized skills.
---

# Lancet Workflow Router (lancet-workflow)

## Overview

This is the router. It does not replace any specialized skill. It tells you **which lancet-* skill to use at the current stage** of a manuscript aimed at *The Lancet*.

Default assumption: unless the user states otherwise, the target is **The Lancet** (the flagship clinical/global-health weekly), not a Lancet family title (*Lancet Global Health*, *Lancet Public Health*, *EClinicalMedicine*, or a specialty journal such as *Lancet Oncology*). Family titles share house style but differ on scope and audience — flag the difference and route to `lancet-fit` if the user names one.

## When to trigger

- "What should I do next with this clinical manuscript?"
- A draft arrives and you must diagnose the current bottleneck.
- The user is moving between trial conduct, writing, and revision and has lost the thread.
- Reviews arrive from The Lancet (including a statistical reviewer) and you need rebuttal mode.

## The single most important gate

The Lancet rejects **most submissions without external review**. The editorial bar is not technical correctness alone — it is **clinical or public-health importance, global relevance, and impact on practice or policy**, often with an equity lens. So the first question is never "is the trial sound?" — it is **"does this change practice or policy for a globally relevant problem?"** Route to `lancet-fit` first, always.

## How The Lancet differs from NEJM / JAMA / BMJ

- **The Lancet** — international and global-health-forward; an explicit **advocacy voice**; strong on **health equity, public health, and policy**; large multi-country trials; article types include **Articles** (original research), **Seminars**, **Reviews**, **Comment**, and **Correspondence**, plus the Lancet family of specialty journals.
- **NEJM** — clinically definitive, often US-centric, conservative house style; no Research-in-context panel.
- **JAMA** — clinical + health-policy, structured abstracts, strong methods/statistics editing.
- **BMJ** — open access, generalist, strong on EBM and patient partnership; "What this paper adds" box.

The Lancet's distinctive artifacts are the **Research in context panel** (with a systematic-search Evidence-before-this-study section), the **Findings/Interpretation/Funding** abstract headings, and the explicit **role of the funding source** statement.

## Routing table

| Current symptom                                                       | Next skill                  |
|-----------------------------------------------------------------------|-----------------------------|
| Not sure it is clinically/globally important enough to change practice | `lancet-fit`               |
| Design/registration/protocol/SAP unclear; not yet registered          | `lancet-study-design`       |
| No CONSORT/STROBE/PRISMA checklist or flow diagram                     | `lancet-reporting`          |
| No Research in context panel, or it lacks a systematic search          | `lancet-research-in-context`|
| Abstract unstructured, over 300 words, wrong headings                  | `lancet-abstract`           |
| Main text over length; Discussion overstates; structure wanders        | `lancet-writing`            |
| Stats under-reported; bare P values; subgroups uncontrolled; ITT unclear | `lancet-statistics`       |
| Table 1, Kaplan–Meier, forest, or flow diagram missing/non-compliant    | `lancet-figures-tables`     |
| No declaration of interests / role of funding / data sharing / SAGER    | `lancet-ethics`             |
| About to submit; need a preflight checklist + cover letter              | `lancet-submission`         |
| Received reviews / an R&R decision (incl. statistical reviewer)         | `lancet-rebuttal`           |

## Default order

1. `lancet-fit` — clear the importance / global-relevance / policy bar first
2. `lancet-study-design` — registration, protocol + SAP, design rigor
3. `lancet-reporting` — EQUATOR guideline + flow diagram for the study type
4. `lancet-statistics` — pre-specified analysis, ITT, CIs, subgroups
5. `lancet-figures-tables` — Table 1, KM, forest, study-flow diagram
6. `lancet-research-in-context` — the signature three-part panel (systematic search)
7. `lancet-abstract` — structured abstract (Findings/Interpretation/Funding) ≤300 words
8. `lancet-writing` — main-text structure and length; cautious Discussion
9. `lancet-ethics` — declaration of interests, role of funding, data sharing, equity
10. `lancet-submission` — preflight + cover letter
11. `lancet-rebuttal` — after review

> `lancet-abstract`, `lancet-research-in-context`, and `lancet-writing` are largely **late-stage polish**. Do not perfect the abstract before registration and reporting compliance are settled.

## Decision shortcuts

- "This is solid but it's a single-centre confirmatory result" → `lancet-fit` (consider *EClinicalMedicine* / specialty title)
- "Enrollment started before we registered the trial" → `lancet-study-design` (a serious problem — flag immediately)
- "We have no CONSORT flow diagram" → `lancet-reporting`
- "We never did a systematic search of prior evidence" → `lancet-research-in-context`
- "Our abstract says Results and Conclusions" → `lancet-abstract` (Lancet uses Findings / Interpretation)
- "We report odds ratios but no absolute risk" → `lancet-statistics`
- "We didn't state who had final responsibility to submit" → `lancet-ethics` (role of the funding source)

## Worked routing example (illustrative)

A hypothetical multi-country RCT manuscript arrives mid-stream; the router resolves the bottleneck.

```
Symptoms reported:
  - "We think it's a Lancet paper but we're not sure it changes practice"  -> lancet-fit FIRST
  - "Registration date may be after first enrolment"                       -> lancet-study-design (flag)
  - "Abstract says Results / Conclusions"                                   -> lancet-abstract
  - "No Research in context panel"                                          -> lancet-research-in-context
Resolved order (illustrative):
  lancet-fit -> rung 4, GO
  -> lancet-study-design (confirm prospective registration; reconcile primary outcome)
  -> lancet-reporting (CONSORT + flow diagram)
  -> lancet-statistics -> lancet-figures-tables
  -> lancet-research-in-context -> lancet-abstract -> lancet-writing
  -> lancet-ethics -> lancet-submission -> (after decision) lancet-rebuttal
Gate rule: never start prose polish before lancet-fit clears; the modal outcome is
  rejection without review.
```

## Anti-patterns

- **Do not** skip `lancet-fit` and start polishing prose — the modal outcome is rejection without review.
- **Do not** draft the Research in context panel before the systematic search is actually run.
- **Do not** generate a rebuttal before the main text is actually revised.
- **Do not** treat the abstract or panel as optional formatting — they are load-bearing at triage.
