---
name: sci-rebuttal
description: Use after Science reviews arrive to triage the decision, prioritize experiments, and draft a point-by-point response that is respectful, evidence-led, and honest about limits. Do not run before the main text is actually revised.
---

# Reviewer Rebuttal (sci-rebuttal)

## When to trigger

- A decision letter arrives (reject / reject-but-resubmit / major or minor revision).
- You have reviewer comments and need a strategy before writing.
- A revision is drafted and you need the point-by-point response letter.

## Step 0: read the editor's letter first

The **editor's** framing outranks individual reviewers. Identify:

- The decision type and whether a new review round is implied.
- Which concerns the editor **emphasizes** (these are load-bearing — address fully).
- Any **deal-breaker** the editor names (e.g., "the central claim needs independent validation").

> A "reject but would consider a new submission" is an invitation gated on the deal-breaker. Don't treat it as a flat reject, but don't under-deliver either.

## Triage every comment into 4 buckets

| Bucket             | Action                                                            |
|--------------------|------------------------------------------------------------------|
| **Do** (fair, feasible) | Make the change; show it; quote the new text/figure.        |
| **Do-partial**     | Do what's feasible; explain the boundary with evidence.          |
| **Defend** (wrong/out of scope) | Push back respectfully, with data/citations — not assertion. |
| **Defer** (future work) | Acknowledge; add a sentence to the text; don't over-promise. |

Most rejections-on-revision come from **silently skipping** a load-bearing comment or **defending** when an experiment was actually needed.

## Prioritize the experiments

- Rank requested experiments by **(impact on the central claim) × (feasibility)**.
- The reviewer's #1 concern about the **main claim** must be answered with data, not prose.
- If an experiment is infeasible, offer the **strongest alternative evidence** and say why the alternative suffices.

## Response-letter format

For each comment:

```
Reviewer N, Comment k: <verbatim quote of the reviewer>

Response: <what we did / our reasoning>. <Evidence: new Fig./table, statistics.>
Changes: "<quoted new manuscript text>" (p. X, lines Y–Z; new fig. Sk).
```

- Open with a short thank-you and a 3–4 line summary of the **major changes** across the whole revision.
- Quote each comment verbatim; never paraphrase a reviewer in a way that softens their point.
- **Quote the new manuscript text** so the editor can verify without hunting.
- Use a consistent visual convention (e.g., reviewer text plain, your response indented, manuscript quotes in italics/color).

## Tone rules

- Respectful and non-defensive, even when the reviewer misread the paper — if they misread it, the writing was unclear; fix the writing **and** explain.
- Concede real limitations explicitly; an honest limitation paragraph builds credibility.
- No sarcasm, no "as we clearly stated" — assume good faith.

## Over-claiming watch (Science-specific)

If a reviewer says the conclusion outruns the data, this is the **most dangerous** comment for a Science paper. Either add the evidence or **narrow the claim** in the abstract, title, and last paragraph — and say you did. Re-run `sci-fit` if the narrowed claim weakens broad significance.

## Science-specific revision packet

Science revisions must preserve a compact, high-signal main story while moving
technical detail into the right support surface. Before writing the response,
map each requested change onto this packet:

| Science surface | Revision question |
|---|---|
| Main-text claim ladder | Which one or two claims still deserve main-text space after the revision? |
| Figures | Does the new evidence change the main figure logic, not just add another panel? |
| Supplementary materials | Are added methods, controls, statistics, and sensitivity checks easy to find from the response letter? |
| Cross-disciplinary readability | Can a broad Science editor understand why the new evidence changes confidence in the central claim? |
| Scope statement | If the claim narrows, did the abstract, title, first paragraph, and final paragraph all narrow together? |

Do not answer Science reviewers by simply accumulating supplementary analyses.
The response must explain how the revision sharpens the main claim, what moved
to supplementary materials, and why the core story still has Science-level
breadth after any narrowing.

## Output format

```
【Decision type】 reject / reject-resubmit / major / minor
【Editor's load-bearing concerns】 [...]
【Deal-breaker】 ... → plan to resolve
【Comment triage】 Do [...] / Do-partial [...] / Defend [...] / Defer [...]
【Experiment priority】 ranked by impact × feasibility
【Claim integrity】 any narrowing needed? (re-check sci-fit)
【Science revision packet】 main-text claim ladder / figures / supplementary materials / scope statement
【Response letter】 drafted point-by-point with quoted changes
```

## Anti-patterns

- **Do not** silently skip a comment the editor emphasized.
- **Do not** defend by assertion where the reviewer asked for data.
- **Do not** over-promise future work to dodge a needed experiment.
- **Do not** draft the response before the manuscript is actually revised.
