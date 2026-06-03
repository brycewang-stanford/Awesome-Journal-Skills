---
name: agsy-revision-and-rebuttal
description: Use when writing the response to an Agricultural Systems (AgSy) revision decision. AgSy review is single anonymized with at least two expert systems reviewers and an editor decision, and revisions often turn on model evaluation, sensitivity/uncertainty, and trade-off framing. The response must convert each reviewer without alienating the editor. Structures the response letter; it does not fabricate new results.
---

# Revision & Rebuttal (agsy-revision-and-rebuttal)

A revise decision at AgSy is a real chance — but systems reviewers tend to press on the **model**
(calibration, evaluation, sensitivity, uncertainty) and the **trade-off / decision framing**. The
response letter must move *every* reviewer toward yes while keeping the **editor** confident the
revision converges. Reviewers are not anonymous to you on their side (single anonymized), but keep the
tone professional and evidence-based.

## When to trigger

- A major/minor revision decision arrived and you are planning the revision + response letter
- Reviewers disagree (e.g., one wants more scenarios, another wants a simpler model)
- A reviewer requests additional evaluation, sensitivity, or uncertainty analysis
- Writing the cover note to the editor summarizing the revision

## Strategy

1. **Read the editor's letter as the rubric.** The editor signals which points are decisive — often
   model evaluation, uncertainty, or systems framing. Solve those first; the editor adjudicates
   disagreements among reviewers.
2. **One point-by-point response, every comment addressed.** Quote each comment, then respond. Never
   skip one — silence reads as non-compliance.
3. **Concede or rebut explicitly, with evidence.** For each: did what was asked (say where, with the new
   text/figure/table number, or the new sensitivity/uncertainty run), or push back **respectfully with
   a systems reason** (boundary, model structure, data, or scale). A well-argued disagreement beats a
   capitulation that weakens the analysis.
4. **Strengthen the model, don't just defend it.** Most AgSy revisions improve with an added
   **independent evaluation**, a **sensitivity / uncertainty** analysis, or a clearer **trade-off**
   exhibit. Offer these proactively where reviewers raise doubt.
5. **Reconcile conflicting reviewers openly.** When R1 wants more complexity and R2 wants parsimony, say
   so, choose a principled path (justified by the question and the decision relevance), and explain the
   tradeoff to the editor.
6. **Protect the systems contribution.** Resist changes that turn the paper back into a single-factor
   study or dilute the trade-off/decision message. Defend scope conditions rather than over-claiming.
7. **Keep the package in sync.** Update the deposited **data, code, and model** so new tables/figures
   remain reproducible (see `agsy-reproducibility-and-data-policy`).

## Response-letter format

For each reviewer comment:

```
> [Quoted reviewer comment]

Response: [What we did / why we respectfully disagree, with a systems reason].
Change: [Section/page/figure-table number; new evaluation/sensitivity run where relevant].
```

Open with a short **summary of the main changes** to the editor; group by reviewer; end each entry with
the location of every change so the editor can verify quickly.

## Anti-patterns

- Ignoring or merging away a comment without a visible response
- Adding scenarios/complexity that quietly contradict the original conclusion without acknowledging it
- Defensive or dismissive tone toward reviewers
- "We thank the reviewer" with no actual change or argued reason
- Letting the revised manuscript or new exhibits drift out of sync with the deposited package
- Conceding a change that collapses the systems framing just to please one reviewer

## Output format

```
【Editor's decisive points】addressed first? [list]
【Coverage】every reviewer comment answered? [Y/N]
【Concede vs rebut】each tagged with evidence + change location
【Model strengthened】added evaluation/sensitivity/uncertainty where pressed? [Y/N]
【Reviewer conflicts】reconciled and explained to editor? [Y/N]
【Contribution protected】systems framing + trade-off intact? [Y/N]
【Package updated】data/code/model in sync? [Y/N]
【Next】resubmit via Editorial Manager
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — review model, reviewer count, editor-decision policy
