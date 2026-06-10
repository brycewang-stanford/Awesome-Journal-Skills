---
name: jfqa-workflow
description: Use when routing a Journal of Financial and Quantitative Analysis (JFQA) manuscript — decides which jfqa-* skill to use next across topic selection, literature positioning, identification, data analysis, contribution framing, tables/figures, writing style, the code-sharing archive, review process, submission preflight, and R&R rebuttal. Start here when unsure what to do next.
---

# JFQA Workflow Router (jfqa-workflow)

Use this skill to orient a manuscript aimed at the **Journal of Financial and Quantitative Analysis (JFQA)** — an empirical and quantitative finance journal published by **Cambridge University Press** for the **University of Washington Foster School of Business**. It prints **less than 9%** of the 1,000+ papers submitted yearly, so every stage should clear a high bar before you spend the **$350** non-refundable-by-$75 submission fee.

## When to trigger

- "Where do I start / what's next for my JFQA paper?"
- You have results but are unsure whether the design, framing, or archive is JFQA-ready.
- You received a decision letter and need to route to rebuttal or resubmission.

## Routing map

```
jfqa-topic-selection          → is this a JFQA-fit finance question?
        ▼
jfqa-literature-positioning   → stake the contribution vs. the finance frontier
        ▼
jfqa-identification-strategy  → credible design (sorts/FMB, panel FE, DID, IV, RDD, event study)
        ▼
jfqa-data-analysis            → estimation, clustering, robustness, economic magnitudes
        ▼
jfqa-contribution-framing     → one-paragraph ≤100-word abstract + intro contribution
        ▼
jfqa-tables-figures           → finance-standard exhibits with self-contained notes
        ▼
jfqa-writing-style            → polish for a finance audience
        ▼
jfqa-replication-and-data-policy → build the JFQA Dataverse code/data archive
        ▼
jfqa-review-process           → what double-anonymous JFQA review involves
        ▼
jfqa-submission               → Editorial Manager preflight (PDF, fee, formatting)
        ▼
jfqa-rebuttal                 → R&R response letter
```

## Output format

```
【Stage】where the manuscript is now
【Next skill】single jfqa-* skill to invoke
【Why】one-line rationale tied to a JFQA constraint
【Watch-outs】fee/refund, 100-word abstract, anonymization, code policy, prior-rejection disclosure
```

Always confirm volatile specifics on the official pages (see resources/official-source-map.md).

## Router diagnostics

Ask the manuscript owner for the current bottleneck:

- **Question/scope** unclear or outside finance: `jfqa-topic-selection`.
- **Closest finance competitor** missing: `jfqa-literature-positioning`.
- **Design credibility** weak: `jfqa-identification-strategy`.
- **Results not reproducible or magnitudes missing**: `jfqa-data-analysis`.
- **Abstract or first page too diffuse**: `jfqa-contribution-framing`.
- **Exhibits unreadable without text**: `jfqa-tables-figures`.
- **Archive, pseudo data, or exception timing unresolved**: `jfqa-replication-and-data-policy`.

The route should always reduce one JFQA-specific screen risk: fit, 100-word abstract, anonymization,
identification, economic magnitude, code-sharing, fee/prior-rejection disclosure, or exhibit readability.

## Stage gates before spending the fee

| Gate | Exit criterion | JFQA risk averted |
|---|---|---|
| G1 Scope | the question scores high on the topic-selection rubric | $75 retained on a desk reject, plus months |
| G2 Design | identifying variation stated in one defensible sentence | the endogeneity report that kills most empirical R&Rs |
| G3 Numbers | headline magnitude expressed in finance units, scaled | the "only statistically significant" complaint |
| G4 Package | `run_all` regenerates every exhibit; pseudo-data plan set | a scramble at acceptance under the Code Sharing Policy |
| G5 Preflight | ≤ 100-word abstract, anonymized text-searchable PDF, disclosures drafted | formatting/anonymity strikes and the one-year-ban trap |

Do not let a manuscript pass a later gate while an earlier one is open; JFQA's screens fire in roughly this order.

## Worked routing call (illustrative)

A manuscript arrives with strong results but a 138-word abstract, firm-only clustered standard errors never checked against a two-way scheme, and no pseudo-data plan for its CRSP/Compustat extracts. Route in this order: jfqa-contribution-framing first (the abstract cap is a hard constraint and the cheapest fix), then jfqa-data-analysis (inference robustness changes table contents, so it must precede exhibit polish), then jfqa-replication-and-data-policy (pseudo data takes days, and any exception must ride on the initial submission), and only then jfqa-submission. The principle: hard journal constraints and anything that can change numbers come before taste-level polish.

## Re-entry points after a decision

- Desk reject → jfqa-topic-selection or jfqa-contribution-framing, depending on whether fit or framing failed.
- Reject after review, planning a substantially modified return → rebuild through the full chain and add the prior-rejection disclosure at jfqa-submission.
- R&R → jfqa-rebuttal, looping back into jfqa-identification-strategy or jfqa-data-analysis for each evidentiary demand.

## What can run in parallel

- The Dataverse archive build (jfqa-replication-and-data-policy) can proceed alongside writing-style polish; both consume the frozen results, not each other.
- Exhibit notes (jfqa-tables-figures) and the abstract (jfqa-contribution-framing) share the same headline magnitudes — draft them in one sitting so the numbers cannot diverge.
- Anonymization is not a stage; it is a property every stage must preserve from first draft to resubmission.
