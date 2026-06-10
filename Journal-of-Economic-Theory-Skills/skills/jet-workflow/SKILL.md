---
name: jet-workflow
description: Use when routing a Journal of Economic Theory (JET) manuscript — decides which jet- sub-skill to invoke next across the theorem-proof lifecycle, from theory-first scope check through Editorial Manager submission and single-anonymized R&R. Use first when unsure where to start.
---

# JET Workflow Router (jet-workflow)

## When to trigger

- "I want to send a theory paper to JET — where do I start?"
- You have a result but are unsure whether it clears JET's theory-first scope gate
- You need the next step after identification of assumptions, drafting, or a referee report

## What JET is (so the router routes correctly)

The *Journal of Economic Theory* is Elsevier's flagship general economic-theory venue (ISSN
0022-0531). The deciding criterion is a **rigorous, original theoretical contribution** —
mechanism design, information economics, decision theory, game theory, matching, market design,
political economy, finance and macro/monetary theory. Empirical, experimental, quantitative, or
computational work is welcome **only when firmly grounded in theory**. House style is
theorem-proof, typeset in LaTeX (Elsevier `elsarticle`). Review is **single anonymized
(single-blind)** with a floor of **at least two referees** after an editor desk screen.

## Default order

```text
jet-topic-selection          (is this a JET-scope theoretical contribution?)
        ▼
jet-literature-positioning   (stake the result against the theory frontier)
        ▼
jet-identification-strategy  (assumptions, results, proof architecture, generality)
        ▼
jet-contribution-framing     (state the theorem and why it matters)
        ▼
jet-data-analysis            (numerical examples / computation — only if any)
        ▼
jet-tables-figures           (schematic exhibits, notation discipline)
        ▼
jet-writing-style            (elsarticle theorem-proof prose; polish)
        ▼
jet-replication-and-data-policy (encouraged, not required; reproducible computation)
        ▼
jet-review-process           (what single-anonymized refereeing expects)
        ▼
jet-submission               (Editorial Manager preflight, .tex source, AI disclosure)
        ▼
jet-rebuttal                 (response letter on an R&R)
```

## Router diagnostics

- No theorem sentence yet -> `jet-topic-selection`.
- Closest theorem unclear -> `jet-literature-positioning`.
- Assumptions or proof dependencies unclear -> `jet-identification-strategy`.
- Theorem is right but buried -> `jet-contribution-framing`.
- Computation is doing too much work -> `jet-data-analysis`.
- Figures introduce notation drift -> `jet-tables-figures`.
- Source/package facts are volatile -> `jet-submission` and `resources/official-source-map.md`.

The next skill should always reduce one JET desk/referee risk: off-scope empirics, overclaimed theorem,
hidden assumption, unreadable proof, notation drift, or unsupported submission fact.

## Output format

```
【Where you are】<stage>
【Use next】jet-<skill>
【Why】<one line tied to JET's theory-first bar>
【Open 待核实】<lead editor / fee / length if relevant>
```
