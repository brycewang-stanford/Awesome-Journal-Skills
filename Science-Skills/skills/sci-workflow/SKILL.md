---
name: sci-workflow
description: Use when deciding which sci-* sub-skill to invoke next, or when sequencing a manuscript from significance test through reviewer rebuttal for Science (AAAS). Routes — it does not replace — the specialized skills.
---

# Science Workflow Router (sci-workflow)

## Overview

This is the router. It does not replace any specialized skill. It tells you **which sci-* skill to use at the current stage** of a manuscript aimed at *Science* (AAAS).

Default assumption: unless the user states otherwise, the target is **Science** (the flagship research journal), not *Science Advances*, *Science Translational Medicine*, or other family titles. Family titles share house style but differ on scope and length — flag the difference if the user names one.

## When to trigger

- "What should I do next with this draft?"
- A draft arrives and you must diagnose the current bottleneck.
- The user is switching between experiments, writing, and revision and has lost the thread.
- Reviews arrive from Science and you need to switch into rebuttal mode.

## The single most important gate

Science rejects **most submissions without external review**. The editorial bar is **broad significance and general interest**, not technical correctness alone. So the first question is never "is the science right?" — it is **"does this clear the desk-reject filter for a general audience?"** Route to `sci-fit` first, always.

## Routing table

| Current symptom                                              | Next skill          |
|-------------------------------------------------------------|---------------------|
| Not sure the result is broad/general-interest enough        | `sci-fit`           |
| Result is significant but the "why it matters" is buried    | `sci-framing`       |
| No one-sentence summary; abstract reads narrow/jargon-heavy  | `sci-abstract`      |
| Unsure whether this is a Research Article or a Report; over length | `sci-writing` |
| Figures over panel/word budget; fonts/colors non-compliant  | `sci-figures`       |
| Stats under-reported; n/error bars/tests unclear; not reproducible | `sci-statistics` |
| No data/code/materials availability plan                    | `sci-data`          |
| References not in Science numbered style                     | `sci-citation`      |
| Need an editor-facing pitch for why Science should review it | `sci-cover-letter`  |
| About to submit; need a preflight checklist                 | `sci-submission`    |
| Received reviews / an R&R decision                           | `sci-rebuttal`      |

## Default order

1. `sci-fit` — clear the broad-significance / general-interest bar first
2. `sci-framing` — lock the conceptual advance and the "why now"
3. `sci-writing` — choose format (Research Article vs Report) and hold length
4. `sci-figures` — finalize display items within budget
5. `sci-statistics` — rigor & reproducibility reporting
6. `sci-data` — data / code / materials availability
7. `sci-abstract` — abstract + one-sentence summary (late polish)
8. `sci-citation` — reference style pass
9. `sci-cover-letter` — significance-forward editor pitch
10. `sci-submission` — preflight
11. `sci-rebuttal` — after review

> `sci-abstract` and `sci-citation` are **late-stage polish**. Do not perfect the abstract before the significance and format are settled.

## Decision shortcuts

- "A specialist would care, but would a geneticist *and* a physicist?" → `sci-fit`
- "My intro starts with background, not with the advance" → `sci-framing`
- "My Report main text is 4,000 words" → `sci-writing` (Reports target ~2,500)
- "Methods are in the main text" → `sci-writing` (Reports push Methods to Supplementary)
- "Bar chart with no individual data points / no n" → `sci-statistics` + `sci-figures`
- "No accession numbers / no code repo" → `sci-data`
- "Editor needs to see the hook in 3 sentences" → `sci-cover-letter`

## How Science differs from its siblings and from Nature

- **Science (Reports / Research Articles)** vs **Science Advances** (open-access, broader acceptance, longer): if the work is solid but not top-1% general interest, Advances may be the realistic target — say so.
- **Science vs Nature**: both gate on broad significance, but Science requires a **one-sentence summary** and uses a **single numbered reference list with full author names**; Nature uses a different reference and summary-paragraph convention. Do not copy a Nature-formatted manuscript over without a style pass (`sci-citation`, `sci-abstract`).

## Stage ledger (copy into the conversation and keep it updated)

Track the manuscript's position in the pipeline with this ledger so every routing decision is explicit and auditable:

```text
SCIENCE (AAAS) MANUSCRIPT STAGE LEDGER
======================================
Target venue      : Science | Science Advances | reroute → ______
Format            : Report | Research Article | undecided
Stage gates (mark ✓ / ✗ / n/a, with date):
  [ ] sci-fit          significance rung ≥3, general-interest test passed
  [ ] sci-framing      one-sentence advance locked; why-now named
  [ ] sci-writing      format chosen; main text within word budget
  [ ] sci-figures      display items ≤ budget; fonts/colors compliant
  [ ] sci-statistics   n, tests, effect sizes, error bars reported
  [ ] sci-data         deposition + accession numbers + availability statement
  [ ] sci-abstract     ≤125-word abstract + one-sentence summary
  [ ] sci-citation     numbered refs, order of appearance, full author lists
  [ ] sci-cover-letter significance-forward editor pitch drafted
  [ ] sci-submission   preflight checklist clean
  [ ] sci-rebuttal     (post-review only) point-by-point response
Current bottleneck : ______            Next skill: sci-______
Open risks         : over-claiming? length? missing deposition? ______
```

Re-emit the ledger after each sub-skill completes; a gate marked ✗ upstream (especially `sci-fit`) invalidates every ✓ downstream of it.

## Anti-patterns

- **Do not** skip `sci-fit` and start polishing prose — the modal outcome is desk rejection.
- **Do not** let `sci-figures` beautify panels before the format/length decision in `sci-writing`.
- **Do not** generate a rebuttal before the main text is actually revised.
