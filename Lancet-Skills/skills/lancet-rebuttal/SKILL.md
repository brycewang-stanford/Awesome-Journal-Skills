---
name: lancet-rebuttal
description: Use after Lancet reviews arrive (including the statistical reviewer and the editor's letter) to triage the decision, answer statistical and clinical comments, and draft a point-by-point response that quotes the reviewer, gives evidence, quotes the revised manuscript text, and keeps causal language cautious. Do not run before the main text is actually revised.
---

# Reviewer Rebuttal (lancet-rebuttal)

## When to trigger

- A decision letter arrives (reject / major or minor revision).
- You have clinical and statistical reviewer comments and need a strategy before writing.
- A revision is drafted and you need the point-by-point response letter.

## Step 0: read the editor's letter first

The **editor's** framing outranks individual reviewers. Identify:

- The decision type and whether a new review round is implied.
- Which concerns the editor **emphasises** (load-bearing — address fully).
- Any **deal-breaker** the editor names (e.g., "the primary analysis must follow the pre-specified SAP," "registration timing must be clarified," "the causal claim must be softened").

> A "we would consider a revised manuscript" is an invitation gated on the deal-breaker. Don't treat it as a flat reject, but don't under-deliver.

## The statistical reviewer is its own track

The Lancet routinely uses a **statistical reviewer**. Treat their comments as a distinct, high-priority track:

- Answer with the **pre-specified analysis** and SAP references; show CIs and absolute effects.
- If asked to add an analysis, add it and label pre-specified vs post-hoc honestly.
- Address ITT/per-protocol, missing-data handling, multiplicity, and subgroup interaction concerns with actual re-analysis, not prose.

## Triage every comment into 4 buckets

| Bucket             | Action                                                            |
|--------------------|------------------------------------------------------------------|
| **Do** (fair, feasible) | Make the change; show it; quote the new text/table/figure.  |
| **Do-partial**     | Do what is feasible; explain the boundary with evidence.         |
| **Defend** (incorrect/out of scope) | Push back respectfully, with data/citations — not assertion. |
| **Defer** (future work) | Acknowledge; add a sentence to the text; don't over-promise. |

Most rejections-on-revision come from **silently skipping** a load-bearing comment or **defending** where a re-analysis was actually needed.

## Response-letter format

For each comment:

```
Reviewer N (or Statistical Reviewer), Comment k: <verbatim quote of the reviewer>

Response: <what we did / our reasoning>. <Evidence: new table/figure, re-analysis,
effect with 95% CI.>
Changes: "<quoted new manuscript text>" (p. X, lines Y–Z; new table/figure/appendix).
```

- Open with a short thank-you and a 3–4 line summary of the **major changes** across the revision.
- Quote each comment verbatim; never paraphrase in a way that softens the reviewer's point.
- **Quote the new manuscript text** so the editor can verify without hunting.
- Use a consistent visual convention (reviewer text plain; response indented; manuscript quotes in italics/colour).

## Tone and causal-language rules (Lancet-specific)

- Respectful and non-defensive; if a reviewer misread the paper, the writing was unclear — fix the writing **and** explain.
- Keep **causal language cautious**: if a reviewer says the conclusion outruns the design (e.g., causal claim from observational data, or a superiority claim from a non-inferiority trial), this is the most dangerous comment — either add evidence or **narrow the claim** in the title, abstract Interpretation, and Discussion, and say you did.
- Concede real limitations explicitly; an honest limitations paragraph builds credibility.

## Update the Research in context panel if the evidence base changed

If new studies appeared during review, **re-run or update the systematic search** and revise "Evidence before this study" and "Implications of all the available evidence" accordingly — and note this in the response (see `lancet-research-in-context`).

## The Lancet-specific reviewer comments and how to land them

The comments that decide a Lancet revision cluster around the venue's identity: registration integrity, the statistical reviewer's re-analysis requests, claim calibration, and the global-health/equity framing. The fix for each is concrete, never rhetorical — the editor verifies it against quoted new text.

| Reviewer comment | The venue-specific fix |
|------------------|------------------------|
| "Trial not prospectively registered." | Disclose exact registration/enrolment dates; if retrospective, flag it and explain — do not bury it |
| "Primary outcome switched." | Reconcile to the registered outcome, or document the dated change; label post-hoc analyses |
| "Causal claim outruns the design." | Narrow the title, abstract Interpretation, and Discussion; say you narrowed it |
| "Global-health relevance / equity not addressed." | Add the LMIC/PROGRESS-Plus framing in Interpretation; coordinate with `lancet-fit` |
| "Statistical reviewer: add ITT/sensitivity analysis." | Run the re-analysis; report effect + 95% CI; show it as a new table, not prose |
| "Reporting checklist incomplete." | Complete and page/line-map the EQUATOR checklist; resubmit as a supplement |

## Worked micro-example (illustrative — not a real exchange)

A statistical-reviewer comment on a hypothetical superiority RCT, answered the Lancet way.

```
Statistical Reviewer, Comment 3: "The primary analysis is reported as per-protocol.
For a superiority trial, the intention-to-treat population should lead."

Response: We agree. We have made the pre-specified ITT analysis primary, with
per-protocol as a labelled sensitivity analysis. The conclusion is unchanged.
Evidence (illustrative): ITT response 60.0% vs 50.2%, absolute risk difference
9.8 pp (95% CI 5.4-14.2; p=0.0003); per-protocol 62.1% vs 50.0% (RD 12.1 pp,
95% CI 7.3-16.9) -> consistent.
Changes: "The primary analysis was by intention to treat..." (p. 8, lines 12-19;
new Table 2 row; appendix table S4 for per-protocol).
```

The request is answered with an actual re-analysis carrying effects and 95% CIs, the ITT/per-protocol order is corrected, and the new manuscript text is quoted so the editor can verify without hunting — the pattern that converts a statistical-reviewer comment into an accept.

## Output format

```
【Decision type】 reject / major / minor
【Editor's load-bearing concerns】 [...]
【Deal-breaker】 ... → plan to resolve
【Statistical-reviewer track】 [...] → re-analyses planned
【Comment triage】 Do [...] / Do-partial [...] / Defend [...] / Defer [...]
【Claim integrity】 any narrowing of causal/practice claims needed? (re-check lancet-fit)
【Panel update】 systematic search re-run? Evidence-before / Implications revised? yes/no
【Response letter】 drafted point-by-point with quoted changes
```

## Anti-patterns

- **Do not** silently skip a comment the editor emphasised.
- **Do not** answer a statistical-reviewer request for re-analysis with prose alone.
- **Do not** defend an over-reaching causal claim — narrow it.
- **Do not** draft the response before the manuscript is actually revised.
