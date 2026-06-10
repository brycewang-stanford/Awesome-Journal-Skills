---
name: gcb-revision-and-rebuttal
description: Use when writing the response to a Global Change Biology (GCB) revise decision. A revision must address every reviewer point with evidence, defend the global-change mechanism and uncertainty treatment, and keep the archived data/code in sync. Structures the response letter; it does not fabricate new results.
---

# Revision & Rebuttal (gcb-revision-and-rebuttal)

A GCB **major/minor revision** is a real chance — but expert reviewers will check whether you actually
addressed mechanism, scale, uncertainty, and reproducibility. The response letter must convert each
reviewer with evidence while protecting the global-change contribution, and the revised manuscript must
stay consistent with the **archived data and code**.

## When to trigger

- A revise decision arrived and you are planning the revision + response letter
- Reviewers disagree and you must reconcile their demands
- A reviewer requests analyses that would change the paper's claims
- Updating the manuscript while keeping the data/code archive in sync

## Strategy

1. **Treat the handling editor's letter as the global-change rubric.** It flags which concerns are
   decisive — usually the strength of the driver-to-response mechanism, the scale of inference, or the
   uncertainty treatment. Resolve those before the smaller comments.
2. **Answer every reviewer point in a single numbered table.** Reproduce each comment, then give your
   response beneath it; an unanswered comment reads as evasion to expert ecological reviewers.
3. **For each comment, either revise or argue back with evidence.** Where you complied, cite the new
   figure/panel/equation/line; where you disagree, ground the pushback in the mechanism, the experimental
   or modelling design, or the data — a defensible biogeochemical argument lands better than a reflexive
   concession that erodes the result.
4. **Defend mechanism, scale, and uncertainty head-on.** GCB referees routinely press on extrapolation
   from plot to ecosystem/biome, on confounding and pseudoreplication, and on whether uncertainty was
   propagated — meet each with a new robustness, sensitivity, or ensemble analysis rather than prose.
5. **Surface reviewer disagreements rather than papering over them.** When two referees pull in opposite
   directions, name the conflict, pick the path the evidence supports, and explain the tradeoff to the
   editor.
6. **Re-sync the deposited archive.** Refresh the **data and code (DOI)** deposit so every new table and
   figure reproduces, and revise the data availability statement to match (see
   `gcb-reporting-and-data-policy`).

## Response-letter format

Per comment, keep the quote-then-answer structure expert referees expect:

```
> [Reviewer comment, verbatim]

Reply: [the revision made, or the mechanism/design/data reason for disagreeing].
Where: [figure / panel / equation / line number in the revised manuscript].
```

Lead with a brief editor-facing digest of the headline changes (new mechanism evidence, scale
qualifications, added uncertainty analyses); organize by referee; close each item with the exact
location so the editor can spot-check quickly.

## Triage table for the most common GCB reviewer demands

Sort the comments before drafting. This maps the recurring global-change critique to the response that
lands with expert ecological reviewers.

| Reviewer demand | Best response | Trap to avoid |
|-----------------|---------------|---------------|
| "Mechanism is correlative" | Add the path model or process evidence that tests it | Restating correlation as causation |
| "Scaling from plot to globe" | Propagate scaling uncertainty; qualify the claim | Dropping the scaling rather than bounding it |
| "Pseudoreplication" | Re-fit at the true unit; show it holds | Defending the original error verbally |
| "No uncertainty propagation" | Add an ensemble/sensitivity analysis | Prose reassurance with no new analysis |
| "Two reviewers disagree" | Name the conflict; pick the evidenced path | Silently siding with one referee |

## Worked micro-example (illustrative)

A warming-experiment paper draws a major revision. Reviewer 1 calls the soil-carbon feedback
"correlative"; Reviewer 2 wants the plot result scaled to the biome. The response adds a
structural-equation model isolating the microbial pathway (R1) and an ensemble scaling with a propagated
95% interval labelled as illustrative bounds (R2), then notes the two referees pull in opposite
directions on generality and resolves toward the conservative, evidence-supported scale. Each reply
cites the new panel and line; the archived code is re-tagged so the figures reproduce. Illustrative.

## Anti-patterns

- Folding a comment into the revision silently, with no traceable reply
- Caving to a request that severs the driver-to-response logic just to placate a referee
- A combative or dismissive register toward reviewers
- "We thank the reviewer" attached to no concrete edit or reasoned rebuttal
- Slipping in analyses that undercut the original claim without flagging the shift
- Revised figures whose numbers no longer match the archived data and code

## Output format

```
【Editor's decisive points】addressed first? [list]
【Coverage】every reviewer comment answered? [Y/N]
【Concede vs rebut】each tagged with evidence + change location
【Mechanism/scale/uncertainty】defended with added analyses? [Y/N]
【Reviewer conflicts】reconciled and explained to editor? [Y/N]
【Archive updated】data/code DOI + availability statement in sync? [Y/N]
【Next】resubmit via ScholarOne
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — decision categories, review model, and data policy
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — robustness/uncertainty and archiving tooling
