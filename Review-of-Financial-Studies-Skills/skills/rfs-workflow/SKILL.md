---
name: rfs-workflow
description: Use when deciding which rfs-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a The Review of Financial Studies (RFS) manuscript. Routes — does not replace — the specialized skills.
---

# RFS Manuscript Workflow (rfs-workflow)

## Overview

This is the router. It does not replace any specialized skill — it tells you **which rfs-* skill to use right now**.

Default assumption: unless the user says otherwise, treat the target as **The Review of Financial Studies (RFS)** — founded 1988 (first editor Michael Brennan), published by Oxford University Press for the Society for Financial Studies (SFS), one of the "top-3" finance journals alongside the *Journal of Finance* (AFA) and the *Journal of Financial Economics* (Elsevier). The current **Executive Editor is Tarun Ramadorai** (LSE / Imperial, term 2024–2027); the editor team includes Viral Acharya (NYU), Xavier Giroud (Columbia), Andrey Malenko (Boston College), Anna Pavlova (LBS), Clemens Sialm (UT Austin), David Sraer (Berkeley), and Jessica Wachter (Penn). RFS shares JF/JFE's high causal-inference and asset-pricing bar but has two distinctive levers JF/JFE do not share: (1) it is the **first finance/economics journal to run Registered Reports** (pre-results review; see Karolyi's 2014 editorial "Kick-Starting the Review Process," RFS 27(2)), and (2) it offers **dual submission with the SFS Cavalcade** conference. The governing tension at RFS is always **novelty AND rigor** — never one without the other.

## When to trigger

- The user asks "what should I do next?"
- A draft arrives and you must diagnose the current bottleneck
- The user is thrashing between empirics, writing, and revision
- A decision letter from RFS arrives and you must switch into rebuttal mode
- The user is unsure whether the paper is novel enough OR rigorous enough for RFS

## Routing table

| Current symptom                                                        | Next skill                     |
|------------------------------------------------------------------------|--------------------------------|
| Idea feels incremental / "me-too"; unsure it clears RFS's novelty bar  | `rfs-topic-selection`          |
| Related-work positioning is weak; unclear delta vs. JF/JFE/RFS papers  | `rfs-literature-positioning`   |
| Core claim is causal but design is OLS + controls / endogeneity open   | `rfs-identification`           |
| Design choices unsettled: panel, factor model, structural, sample      | `rfs-empirical-design`         |
| Main result exists but is fragile / multiple-testing not addressed     | `rfs-robustness`               |
| Tables overloaded; figures not publication-grade; SEs unclear          | `rfs-tables-figures`           |
| Main paper is bloated; checks/derivations belong elsewhere             | `rfs-internet-appendix`        |
| Prose is dense, hedged, or buries the contribution                     | `rfs-writing-style`            |
| Preparing to submit; need Editorial Express preflight + cover letter   | `rfs-submission`               |
| Choosing/excluding referees; anticipating reviewer objections          | `rfs-referee-strategy`         |
| Received an R&R or reject-and-resubmit; need a response letter         | `rfs-rebuttal`                 |

## Default order

1. `rfs-topic-selection` — lock the novel question + the contribution to finance theory/practice
2. `rfs-literature-positioning` — situate against JF/JFE/RFS and define the precise delta
3. `rfs-identification` — pin the causal-inference / asset-pricing identification strategy
4. `rfs-empirical-design` — sample construction, estimators, factor/structural choices
5. `rfs-robustness` — alternative specs, placebo, multiple-testing, out-of-sample
6. `rfs-tables-figures` — finalize main exhibits and standard-error reporting
7. `rfs-internet-appendix` — move proofs, extra tables, and details to the IA
8. `rfs-writing-style` — sharpen contribution framing and prose (polish stage)
9. `rfs-submission` — Editorial Express preflight + cover letter + fee/format checks
10. `rfs-referee-strategy` — referee suggestions and objection pre-mortem
11. `rfs-rebuttal` — after the decision letter

> `rfs-writing-style` is a **late-stage polish** trigger. Do not run it while the identification or novelty story is still unsettled.

## Routing triage form

Complete the stage block top-down; the special-route block can override the default order
because RFS offers paths (Registered Reports, Cavalcade dual submission) its siblings do not.

```text
RFS ROUTING TRIAGE
-- stage block: answer in order, stop at the first "open" ------------------
novelty delta vs. JF/JFE/RFS stated in one sentence?   open -> rfs-topic-selection / rfs-literature-positioning
endogeneity story closed, not just acknowledged?       open -> rfs-identification
sample, estimators, factor/structural choices fixed?   open -> rfs-empirical-design
multiple-testing + placebo + out-of-sample handled?    open -> rfs-robustness
exhibits publication-grade with SEs/clustering noted?  open -> rfs-tables-figures
main text lean; overflow moved to the IA?              open -> rfs-internet-appendix
contribution visible in abstract + first page?         open -> rfs-writing-style
-- special routes: check before submitting ---------------------------------
[ ] strong design, results not yet collected      -> Registered Report path:
                                                     rfs-identification + rfs-empirical-design BEFORE data
[ ] paper headed to SFS Cavalcade                 -> flag dual submission in rfs-submission
[ ] public code release planned from day one     -> rfs-internet-appendix + rfs-submission early
-- terminal ----------------------------------------------------------------
submitting            -> rfs-submission then rfs-referee-strategy
decision letter back  -> rfs-rebuttal (manuscript first, letter second)
```

## Decision heuristics

- "I have clean data but no new question" → `rfs-topic-selection`
- "I cite the literature but cannot state my one-sentence delta" → `rfs-literature-positioning`
- "My DID is TWFE and I have not addressed staggered-adoption bias" → `rfs-identification`
- "My cross-sectional asset-pricing result rests on a self-selected factor" → `rfs-empirical-design`
- "I tested 40 predictors and reported the 3 that worked" → `rfs-robustness`
- "My main table has 11 columns and no clustering note" → `rfs-tables-figures`
- "Reviewers will want 20 more tables I cannot fit" → `rfs-internet-appendix`
- "The abstract hides what is new" → `rfs-writing-style`
- "I submit Friday" → `rfs-submission`
- "I want to suggest/exclude referees" → `rfs-referee-strategy`
- "I have three reports and an R&R" → `rfs-rebuttal`

## Differences vs. JF / JFE stacks

RFS overlaps heavily with the JF and JFE skill stacks on the causal-inference bar, but three RFS-specific facts change the routing:

- **Registered Reports route.** RFS accepts Registered Reports (Stage 1 design review → in-principle acceptance → Stage 2 results). If the user has a strong design but no results yet, or fears a "results-driven" desk reject, this is a real path JF/JFE do not offer. Route design-stage work through `rfs-identification` + `rfs-empirical-design` *before* data collection.
- **SFS Cavalcade dual submission.** A paper routed to the SFS Cavalcade conference can be considered jointly with RFS — a JF/JFE-absent on-ramp. Flag it in `rfs-submission`.
- **Code-release mandate.** RFS requires authors to **publicly release all code** underlying a published paper as a condition of publication; this hits `rfs-internet-appendix` and `rfs-submission` earlier than at journals with softer policies.

A technically clean paper that merely re-runs a known design on new data without a new question is a weak RFS fit even if it would survive at a field journal. Use the Executive Editor / editor roster above when running `rfs-referee-strategy` (do not suggest a handling editor as a referee).

## Anti-patterns

- **Do not** skip `rfs-literature-positioning` and jump to identification — reviewers judge the contribution first.
- **Do not** let `rfs-tables-figures` polish exhibits before identification and robustness hold up.
- **Do not** let `rfs-rebuttal` draft a response letter before the manuscript itself is revised.
- **Do not** pursue rigor while ignoring novelty (or novelty while ignoring rigor) — RFS rejects both halves alone.
