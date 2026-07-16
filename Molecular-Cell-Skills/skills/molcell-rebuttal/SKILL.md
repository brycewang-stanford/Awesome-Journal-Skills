---
name: molcell-rebuttal
description: Use after Molecular Cell reviews arrive to triage the decision, prioritize the (often mechanism-completing) new experiments by impact × feasibility, and draft a point-by-point response that is respectful, evidence-led, and closes the mechanistic gaps reviewers demand. Do not run before the experiments and revision are actually done.
---

# Reviewer Rebuttal (molcell-rebuttal)

## When to trigger

- A decision letter arrives (reject / reject-but-resubmit / major or minor revision).
- You have reviewer comments and need a strategy before running experiments.
- A revision is drafted and you need the point-by-point response letter.

## What's distinctive about Molecular Cell reviews

Molecular Cell reviewers are usually **molecular specialists** who probe the mechanism hard. The recurring theme is not breadth but **mechanistic completeness and rigor**: they push for the molecular step to be nailed down, alternatives excluded with separation-of-function experiments, and in-vitro claims validated in cells. Expect requests for **point mutants, reconstitutions, orthogonal biochemistry, or an additional structural/genomic control** — real bench work, not just rewriting.

## Step 0: read the editor's letter first

The **editor's** framing **outranks** individual reviewers. Identify:

- The decision type and whether a new review round is implied.
- Which concerns the editor **emphasizes** (load-bearing — address fully).
- Any **deal-breaker** the editor names (e.g., "the central mechanism needs a separation-of-function experiment" or "the in-vitro result must be shown in cells").

> The editor often signals which reviewer requests are essential versus optional. Weight the response accordingly — do not treat all reviewers as equal if the editor has prioritized.

## Triage every comment into 4 buckets

| Bucket             | Action                                                            |
|--------------------|------------------------------------------------------------------|
| **Do** (fair, feasible) | Run the experiment / make the change; show it; quote the new figure. |
| **Do-partial**     | Do what's feasible; explain the boundary with evidence.          |
| **Defend** (wrong/out of scope) | Push back respectfully, with data/citations — not assertion. |
| **Defer** (future work) | Acknowledge; add a sentence to the text; don't over-promise. |

Most rejections-on-revision come from **silently skipping** a load-bearing comment or **defending** when an experiment was actually required to complete the mechanism.

## Prioritize the experiments (impact × feasibility)

- Rank requested experiments by **(impact on the central mechanism) × (feasibility/time)**.
- The reviewer's #1 concern about the **molecular mechanism** must be answered with **data** — a point mutant, a reconstitution, an orthogonal assay — not prose. This is where Molecular Cell's rigor demand bites hardest.
- Cluster overlapping requests into one decisive experiment (e.g., a single separation-of-function allele that addresses two reviewers).
- If an experiment is infeasible, offer the **strongest orthogonal evidence** and explain why it closes the gap.
- Sequence long experiments (new constructs, cryo-EM re-processing, mouse crosses) early; don't let one assay become the critical path.

## Response-letter format

For each comment:

```
Reviewer N, Comment k: <verbatim quote of the reviewer>

Response: <what we did / our reasoning>. <Evidence: new Figure/panel, statistics.>
Changes: "<quoted new manuscript text>" (Results, p. X; new Figure Sk; STAR Methods).
```

- Open with a short thank-you and a 3–4 line summary of the **major new experiments** across the whole revision.
- Quote each comment **verbatim**; never paraphrase a reviewer in a way that softens their point.
- **Quote the new manuscript text and name the new figures** so the editor can verify without hunting.
- Use a consistent visual convention (reviewer text plain; response indented; manuscript quotes in italics/color).

## The "mechanism not established" demand (Molecular Cell-specific)

When a reviewer says the mechanism "is not established" or "could be indirect," this is the **most load-bearing** comment for a Molecular Cell paper. Either:
- add the experiment(s) that make the mechanism airtight — a **separation-of-function mutant** that breaks only the proposed step, a **reconstitution** from defined components, an **orthogonal method**, or an **in-cell/in-vivo** validation of an in-vitro claim, or
- **narrow the claim** so the conclusion matches the evidence — and re-check `molcell-fit`, because a narrowed mechanistic claim may now fit Cell Reports.

## Structure/genomics-specific reviewer asks

- If a reviewer questions a structural interpretation, expect to show map quality at the contested region, add validation, or test the interaction functionally (mutation of the interface).
- If a reviewer questions a genomics conclusion, expect requests for additional replicates, an orthogonal readout (e.g., CUT&RUN vs ChIP), or spike-in normalization.

## Tone rules

- Respectful and non-defensive, even when the reviewer misread the paper — if they misread it, the writing was unclear; fix the writing **and** explain.
- Concede real limitations explicitly; an honest limitation builds credibility.
- No sarcasm, no "as we clearly stated"; assume good faith.

## Output format

```
【Decision type】 reject / reject-resubmit / major / minor
【Editor's load-bearing concerns】 [...]
【Deal-breaker】 ... → plan to resolve
【Comment triage】 Do [...] / Do-partial [...] / Defend [...] / Defer [...]
【Experiment priority】 ranked by impact × feasibility; critical path noted
【Mechanism gap】 airtight? else add separation-of-function / reconstitution / in-cell validation (→ molcell-fit)
【Response letter】 drafted point-by-point with quoted changes + new figures
```

## Anti-patterns

- **Do not** silently skip a comment the editor emphasized.
- **Do not** defend by assertion where the reviewer asked for a separation-of-function experiment.
- **Do not** over-promise future work to dodge a needed mechanistic control.
- **Do not** draft the response before the experiments and revision are actually done.

> Confirm revision format and deadlines against the decision letter and the current Molecular Cell guidelines.
