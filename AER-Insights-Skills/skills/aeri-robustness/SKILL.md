---
name: aeri-robustness
description: Use when deciding which robustness checks belong in the few in-text words of an American Economic Review: Insights (AER: Insights) short-format manuscript versus the online Supplemental Appendix. Triages checks against the length cap; it does not design the identification (see aeri-identification).
---

# Robustness — Triage Against the Cap (aeri-robustness)

## When to trigger

- The robustness section is sprawling and competing with the result for word budget
- You have ten checks and at most one or two can appear in-text
- A referee will ask for a check the short paper has no room to add in full
- Unsure what is load-bearing robustness vs. reassurance that can go online

## The short-format robustness problem

A standard paper answers every threat in-text; AER: Insights **cannot**. With **≤7,000 words (minus 200 per exhibit, ≤5 exhibits)**, robustness must be **triaged**: keep in-text only the **one or two checks that, if they failed, would kill the headline result**, and move everything else to the Supplemental Appendix (which has no length cap but is read only by skeptics and the data editor). The skill is deciding the *minimum credible set* of in-text checks and signposting the rest in a single sentence.

## The triage rule

For each candidate check, ask: **"If a referee saw only the main text, would the absence of this check make them disbelieve the headline result?"**

| Answer | Placement |
|--------|-----------|
| Yes — it defends the core identifying assumption | **In-text** (1–2 max), often a single robustness exhibit or a sentence |
| No — it reassures but the result survives without seeing it | **Supplemental Appendix**, named in one in-text sentence |
| It is really an extension / new question | Appendix or a different paper, not "robustness" |

## What usually earns an in-text slot

- The one check that directly tests the **central identifying assumption** (e.g., pre-trends for DiD, the donut/bandwidth for RDD, the exclusion falsification for IV).
- A single **specification curve summary** or a one-line "results are stable across N specifications (Appendix Table X)" rather than the full grid.
- For an experiment: the pre-registered primary outcome's robustness to attrition bounds.

## What goes to the Supplemental Appendix

- Alternative bandwidths, functional forms, sample windows, fixed-effect structures
- Placebo tests beyond the single most informative one
- Heterogeneity splits (these are not robustness; they are extensions)
- Multiple-testing-adjusted versions, alternative clustering, leave-one-out

## Signposting economically

Use **one sentence** to point to the appendix: "The result is robust to [list] (Supplemental Appendix Section X; Tables X1–X6)." This buys credibility for the price of a sentence and keeps the word budget for the insight. Reproduce nothing in-text that the sentence already covers.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). AER: Insights is a short format built around one decisive result, so the body/appendix split is even tighter — run the design cleanly the first time.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER, accounts for
  cross-test correlation) or `benjamini_hochberg` — report the adjusted threshold.
- **OVB sensitivity:** `oster_delta` / `sensemakr` — the confounder strength that would
  overturn the headline.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists the missing checks and the
  exact `suggest_function` for each — no guessing the battery.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Keep the decisive checks in the body and the exhaustive (now actually-run) battery in
the appendix. See the executed chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Every candidate check classified by the triage rule
- [ ] **≤2 robustness items in-text**, each defending the core assumption
- [ ] All other checks in the Supplemental Appendix, **named in one in-text sentence**
- [ ] Heterogeneity treated as extension (appendix), not in-text robustness
- [ ] In-text robustness fits within the five-exhibit budget shared with the result
- [ ] No significance asterisks; SEs / confidence sets reported

## Anti-patterns

- A full in-text robustness section that blows the word/exhibit cap
- Reproducing the appendix robustness grid in the main text
- Treating heterogeneity splits as "robustness" to justify keeping them in-text
- Omitting the central-assumption check to save space (it must stay)
- No signpost to the appendix, leaving referees unsure the checks exist

## Output format

```
【Core-assumption check (in-text)】<the 1–2 that must stay>
【Signpost sentence】"Robust to [list] (Suppl. Appendix §X, Tables …)."
【To the appendix】alt bandwidths / forms / placebos / heterogeneity / clustering
【Exhibit budget】in-text robustness uses __ of 5 exhibits
【Next step】aeri-tables-figures
```
