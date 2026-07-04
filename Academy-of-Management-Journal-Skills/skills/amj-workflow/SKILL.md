---
name: amj-workflow
description: Use when deciding which amj-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for an Academy of Management Journal (AMJ) manuscript. Routes — it does not replace — the specialized skills.
---

# Academy of Management Journal Workflow (amj-workflow)

## Overview

This is the router. It does not replace any specialized skill; it tells you **which amj-* skill to use right now** for your AMJ manuscript.

Default assumption: unless the user says otherwise, treat the target as AMJ — the premier *empirical* management journal published by the Academy of Management (AOM), founded in 1958 and published bimonthly (Feb/Apr/Jun/Aug/Oct/Dec). AMJ's stated mission is "to publish empirical research that tests, extends, or builds management theory and contributes to management practice." It explicitly welcomes **all empirical methods** — qualitative, quantitative, field, laboratory, meta-analytic, and mixed — and judges every manuscript on **three criteria**: a strong empirical contribution, a meaningful theoretical contribution, and practical relevance. The non-negotiable bar: a strong empirical study that **also makes a clear theoretical contribution**. Reviewers and the action editor will ask "what new theory do we learn?" as insistently as "is the method sound?" Both must pass.

> Editorial team changes: Gary A. Ballinger (University of Virginia, McIntire) is the incoming Editor-in-Chief whose team began receiving submissions on 1 July 2025; verify the current masthead at journals.aom.org/journal/amj. Impact factor and acceptance rate fluctuate (2023 JCR IF ≈ 9.5) — treat any figure as **approximate** and confirm on the official page.

## When to trigger

- "What should I do next?" with a half-built AMJ manuscript
- You have a dataset and a result but no clear theoretical story
- A reviewer/editor pushes on "theoretical contribution" and you are unsure which stage is the real bottleneck
- You received an AMJ decision letter (R&R or reject-and-resubmit) and need to switch into response mode
- You keep bouncing between theory, method, and writing without a plan

## Routing table

| Current symptom                                                        | Next skill                  |
|------------------------------------------------------------------------|-----------------------------|
| Idea is vague; not sure it is theory-driven or AMJ-fit                 | `amj-topic-selection`       |
| Hypotheses are descriptive; no clear theoretical mechanism             | `amj-theory-development`    |
| Front end reads as gap-spotting; canonical theory not engaged          | `amj-literature-positioning`|
| Design may not match the question (level, source, timing, causality)   | `amj-methods`               |
| Have data; unsure about measurement validity, CMB, endogeneity, models | `amj-data-analysis`         |
| Results exist but the "so what for theory" is thin                     | `amj-contribution-framing`  |
| Tables/figures cluttered, off house style, or not self-explanatory     | `amj-tables-figures`        |
| Prose is jargon-heavy, passive, or buries the argument                 | `amj-writing-style`         |
| Ready to submit; need the ScholarOne preflight                         | `amj-submission`            |
| Want to understand how AMJ review/decisions work before/after submit   | `amj-review-process`        |
| Received an R&R; need to plan and draft the response                   | `amj-rebuttal`              |

## Default order

1. `amj-topic-selection` — lock a theory-driven question with AMJ fit
2. `amj-theory-development` — build the mechanism and derive hypotheses *a priori*
3. `amj-literature-positioning` — engage canonical theory; state the conversation you join
4. `amj-methods` — match design to the question (level, source, timing, causal logic)
5. `amj-data-analysis` — measurement validity, CMB, endogeneity, the right estimator
6. `amj-contribution-framing` — turn results into an explicit theoretical contribution
7. `amj-tables-figures` — finalize main exhibits in AOM house style
8. `amj-writing-style` — full-manuscript prose polish (Front-loaded argument, active voice)
9. `amj-submission` — ScholarOne preflight (anonymization, format, files)
10. `amj-review-process` — set expectations for the developmental, multi-round process
11. `amj-rebuttal` — after an R&R, plan revisions then draft the response letter

> `amj-tables-figures` and `amj-writing-style` are **late-stage polish**. Do not invoke them while the theoretical contribution or identification is still unsettled — you will polish an argument you may still have to rebuild.

## Stage card

Fill this in before asking "what next?" — route to the first gate still marked `no`.

```yaml
# AMJ manuscript stage card
manuscript: <working title>
gates:
  theory_driven_question_locked: no    # amj-topic-selection
  mechanism_and_a_priori_hypotheses: no # amj-theory-development
  conversation_engaged_not_gap_spotted: no # amj-literature-positioning
  design_matches_question: no          # amj-methods
  measurement_cmb_endogeneity: no      # amj-data-analysis
  theoretical_contribution_explicit: no # amj-contribution-framing
  exhibits_aom_house_style: no         # amj-tables-figures
  prose_front_loaded_active: no        # amj-writing-style
  scholarone_preflight_done: no        # amj-submission
decision_letter_in_hand: no            # yes -> amj-review-process, then amj-rebuttal
route_to: <first gate above still "no">
```

## Decision shortcuts

- "I have a finding but no theory story" → `amj-topic-selection` then `amj-theory-development`
- "My intro says 'no one has studied X'" (gap-spotting) → `amj-literature-positioning`
- "Hypotheses are just 'A relates to B'" → `amj-theory-development`
- "Single-source, single-wave, self-report" → `amj-data-analysis` (common-method bias)
- "Archival design, treatment may be endogenous" → `amj-methods` then `amj-data-analysis`
- "Reviewer says contribution is incremental" → `amj-contribution-framing`
- "Submitting tomorrow" → `amj-submission`
- "Got an R&R with 3 reviewers" → `amj-review-process` then `amj-rebuttal`

## Difference vs. AMR / ASQ / SMJ stacks

- **AMJ**: empirical contribution that *also* advances theory — data and theory weighted equally. AOM journal; 40-page main-body limit; ScholarOne at mc.manuscriptcentral.com/AMJ.
- **AMR** (theory-only): a *sister AOM journal* with no data — the contribution is a novel, internally consistent theory, typically ~25-30 double-spaced pages excluding references. Use an AMR stack.
- **ASQ**: Cornell/SAGE journal (not AOM); empirical or theoretical, prizes deep contextual/qualitative work and bold framing.
- **SMJ**: Strategic Management Society / Wiley journal (not AOM); strategy-focused, performance and competitive-advantage questions, often archival.

If your paper has no original data and is purely conceptual, AMJ is the wrong venue — target AMR.

## Anti-patterns

- **Do not** skip `amj-theory-development` and jump to analysis — AMJ rejects atheoretical "gap-spotting."
- **Do not** let `amj-tables-figures` beautify exhibits before the model and contribution are settled.
- **Do not** let `amj-rebuttal` draft a response letter before you have actually revised the manuscript.
- **Do not** treat `amj-writing-style` as a substitute for a real theoretical contribution — polish cannot rescue thin theory.
