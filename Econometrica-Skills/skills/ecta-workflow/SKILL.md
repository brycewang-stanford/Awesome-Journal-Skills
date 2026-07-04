---
name: ecta-workflow
description: Use when deciding which ecta-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for an Econometrica manuscript. Routes — does not replace — the specialized skills.
---

# Econometrica Workflow (ecta-workflow)

## Overview

This is the router. It does not replace any specialized skill — it tells you **which
ecta-* skill to invoke at the current stage**.

Default assumption: unless the user says otherwise, the target is **Econometrica**, the
journal of the Econometric Society (published by Wiley; founded 1933) — the flagship for
**econometric methods and rigorous economic theory** (microeconomic, game, and decision
theory, plus mathematical economics). Its charter is the *unification of the
theoretical-quantitative and empirical-quantitative approaches, penetrated by constructive
and rigorous thinking*. The bar is mathematical rigor: a new method or theorem with a
**complete, correct proof**, generality, and a clear economic or inferential payoff.

This is the key re-slant from a sibling like AER / QJE / JPE / REStud: Econometrica's core
product is the **theorem or the estimator**, not a clean causal estimate of a policy effect.
A flawless applied difference-in-differences or RDD paper with an off-the-shelf method is
*off-fit here* even if it would headline a general-interest top-5 journal. Lineage that fits:
Heckman (1979, selection), Hansen (1982, GMM), Newey–West (1987, HAC), Rust (1987, NFXP),
Kahneman–Tversky (1979, prospect theory) — all Econometrica.

Econometrica papers come in two broad shapes; route accordingly:
- **Theory / methods** (econometric theory, micro / game / decision theory): the
  contribution is a theorem, an estimator with its asymptotics, or an axiomatic result.
- **Structural / empirical**: a method applied with care, or a structural model whose
  identification and estimation are the contribution. These still need the methodological
  spine and a replication package.

## When to trigger

- "What should I do next?" on an Econometrica-bound paper
- A draft arrives and you must diagnose the binding constraint
- You are oscillating between proofs, simulations, and writing and have lost the thread
- A decision letter / referee reports arrive and you need to switch to rebuttal mode

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Idea is vague; unsure the contribution is general / deep enough for Econometrica | `ecta-topic-selection` |
| Unsure how the result sits against the methods / theory literature it extends | `ecta-literature-positioning` |
| Estimator lacks identification conditions / asymptotic distribution; or axioms not pinned down | `ecta-identification` |
| Central theorem stated loosely; proof incomplete, hand-wavy, or missing regularity conditions | `ecta-theory-model` |
| Asymptotics with no finite-sample check; no Monte Carlo / edge-case analysis | `ecta-robustness` |
| Simulation tables / empirical exhibits unclear, overloaded, or non-self-contained | `ecta-tables-figures` |
| Prose is verbose, informal, or buries assumptions; not in terse formal house style | `ecta-writing-style` |
| Need to assemble code / data under the ES Data and Code Availability Policy (Data Editor + Zenodo) | `ecta-replication-package` |
| Want to anticipate what the handling co-editor and referees will attack | `ecta-referee-strategy` |
| Ready to submit; need Editorial Express preflight, 45-page check, + Supplemental Material assembly | `ecta-submission` |
| Received a revise-and-resubmit or conditional acceptance; need a response letter | `ecta-rebuttal` |

## Default order

1. `ecta-topic-selection` — fix the contribution: a general theorem or a method with real payoff
2. `ecta-literature-positioning` — locate the result precisely in the methods / theory lineage
3. `ecta-identification` — identification conditions + asymptotics (or axioms + existence/uniqueness)
4. `ecta-theory-model` — state the central theorem(s); build the proof strategy; check generality
5. `ecta-robustness` — Monte Carlo, finite-sample performance, regularity / edge cases
6. `ecta-tables-figures` — finalize simulation tables and any empirical exhibits
7. `ecta-writing-style` — terse formal polish; assumptions visible; theorem-numbered
8. `ecta-replication-package` — code (+ data) under the ES Data and Code Availability Policy
   (Data Editor reproducibility check at conditional acceptance; Zenodo deposit)
9. `ecta-referee-strategy` — red-team the proofs and the generality claim
10. `ecta-submission` — Editorial Express preflight, 45-page limit, Supplemental Material assembly
11. `ecta-rebuttal` — after the R&R / conditional-acceptance letter

> `ecta-writing-style` is a **late polish stage** — do not polish prose while the central
> theorem or its proof is still unstable. Likewise, do not build tables before the
> identification / asymptotics are settled.

## Submission-package tree

Keep the working directory shaped like the final Editorial Express upload from day one —
the Zenodo deposit and Data Editor check arrive at conditional acceptance, when it is too
late to reconstruct a replication folder from scratch:

```text
econometrica-submission/
├── main.pdf                 # ≤45 pages incl. references and appendices
├── supplement.pdf           # Supplemental Appendix, ≤25 pages
├── cover-letter.pdf         # ES membership stated; fee tier noted
├── replication/             # ES Data and Code Availability Policy
│   ├── README.md            # exact commands regenerating every exhibit
│   ├── code/                # Monte Carlo + estimation scripts
│   └── data/                # raw data, or access instructions if proprietary
└── working-notes/           # not uploaded — internal gates
    ├── theorem-ledger.md    # per theorem: statement / proof / regularity conditions
    └── referee-redteam.md   # output of ecta-referee-strategy
```

A purely theoretical paper drops `data/` but keeps `code/` if any result is verified
numerically; an estimator paper's "data" may be entirely its simulation code.

## Decision mnemonics

- "I have a result but I'm not sure it's general enough" → `ecta-topic-selection`
- "A referee will ask how this differs from [classic estimator/theorem]" → `ecta-literature-positioning`
- "My estimator is consistent but I never derived its limiting distribution" → `ecta-identification`
- "My proof says 'it is easy to see that'" → `ecta-theory-model`
- "I report asymptotics but never simulated finite samples" → `ecta-robustness`
- "My size/power table has eight columns and no notes" → `ecta-tables-figures`
- "My intro is three pages of motivation before any result" → `ecta-writing-style`
- "I can't regenerate Table 2 from a clean checkout" → `ecta-replication-package`
- "Where will the referee find the hole?" → `ecta-referee-strategy`
- "Submitting tomorrow" → `ecta-submission`
- "Three reports back, all asking for more generality" → `ecta-rebuttal`

## Differences vs. applied-economics packs (AER / QJE / JPE / REStud)

If the contribution is an *application* — a causal estimate of a policy effect, with the
method off-the-shelf — an applied general-interest pack (e.g., AER / QJE / JPE / REStud
skills) is the better fit. The core difference:

- **Econometrica**: the contribution is the *method or theorem* — generality, complete
  proofs, asymptotics, and finite-sample evidence are the product. A purely theoretical
  paper carries no replication package; an estimator paper's "data" may be entirely its
  Monte Carlo code.
- **General-interest applied**: the contribution is the *answer to an economic question* —
  identification of a specific effect carries the paper, and a clean empirical narrative
  matters more than a new limit theorem.

Concrete Econometrica-specific facts that are *wrong* for those siblings: at least one
author must be a member of the **Econometric Society** to submit; the **45-page** limit
(incl. references and appendices) plus a ≤**25-page** Supplemental Appendix; submission via
**Editorial Express** with an **ES-member submission fee** (US$125 regular / US$50 student
from 2025); and replication is governed by the **Econometric Society** Data and Code
Availability Policy with **Data Editor** checks and a **Zenodo** deposit — not the AEA Data
Editor / openICPSR pipeline the AER/AEJ packs assume.

## Anti-patterns

- **Do not** skip `ecta-identification` / `ecta-theory-model` and jump to simulations —
  referees read the proofs first.
- **Do not** let `ecta-tables-figures` polish exhibits before the asymptotics are settled.
- **Do not** let `ecta-writing-style` smooth prose over a proof gap — fix the math first.
- **Do not** let `ecta-rebuttal` draft a response before the revised theorems and code are done.
