---
name: conbio-conservation-relevance-and-implications
description: Use when sharpening the conservation significance and actionable implications of a Conservation Biology manuscript. The journal requires results to have direct, transferable implications for conserving biological diversity and to bridge science and practice. Frames the so-what and the recommendations; it does not overstate evidence or fabricate impact.
---

# Conservation Relevance & Implications (conbio-conservation-relevance-and-implications)

This is the skill that makes a paper a *Conservation Biology* paper. The journal exists to publish
science with **direct implications for the conservation of biological diversity**, so the contribution
must connect evidence to **decisions** — what to protect, manage, restore, or prioritize — and do so in
a way that **travels beyond the focal case**. Sharpen the so-what without over-claiming.

## When to trigger

- Drafting the final paragraph of the Introduction and the implications part of the Discussion
- A reviewer said the work is "sound but the conservation relevance is unclear" or "too local"
- Translating a statistical result into a management or policy recommendation
- Deciding whether the framing fits an **Essay** or **Conservation Practice and Policy** instead

## Build the conservation argument

1. **State the decision.** Whose decision does this inform — a manager, an agency, a planner, a
   community? What action becomes better-supported by your result?
2. **Make implications proportional to evidence.** Recommend exactly what the design supports, with its
   uncertainty. A correlational result motivates a hypothesis or a precautionary step, not a mandate.
3. **Make it transferable.** Generalize the lesson: the mechanism, the decision rule, or the conditions
   under which the finding applies elsewhere. Avoid "for our site only."
4. **Bridge science and practice.** Translate jargon into the terms a practitioner uses; state the
   feasibility, cost, or tradeoffs of the recommended action where you can.
5. **Name scope conditions and risks.** Where does the implication hold or fail? What could go wrong if
   acted on? Acknowledge values and tradeoffs (biodiversity vs. livelihoods) honestly.

## The actionability test (journal-specific)

In one sentence: *"Because we found ___, a conservation decision-maker should ___ (under conditions
___), with ___ confidence."* If you cannot complete it without overstating, either strengthen the
design (`conbio-study-design`) or reframe the contribution (`conbio-topic-selection`).

## The proportionality ladder (match the claim to the design)

Reviewers reject implications that outrun the evidence, so calibrate the verb to the design that
produced it:

- **Correlational / single-site** → *raise a hypothesis* or *justify a precautionary step*; never a
  mandate. ("Edge density is associated with lower occupancy, warranting caution when siting clearings.")
- **Space-for-time or unreplicated BACI** → *support a conditional recommendation* with stated scope.
- **Staggered / replicated before-after with detection modeling** → *support a sequencing or targeting
  rule* a manager can act on (as in the hedgerow worked example).
- **Projection (PVA / SDM / climate)** → *bound the recommendation by the projection's uncertainty*;
  state the assumptions that, if wrong, flip the advice.

If the design sits lower on the ladder than the recommendation you want to make, either strengthen the
design (`conbio-study-design`) or lower the verb — do not borrow certainty the data do not have.

## Before → after: an implications paragraph

- **Before (vague):** *"Our results have important implications for conservation and highlight the need
  for further management action to protect biodiversity in the study region."* — names no decision, no
  actor, no transferable rule; a desk-rejection tell.
- **After (actionable, transferable, proportional):** *"Because recovery was roughly twice as fast at
  well-connected sites, a manager spending a fixed restoration budget should sequence field-edge
  restoration to link existing habitat first. This sequencing rule — not our region's occupancy total —
  is what transfers to other fragmented systems, and it holds only where rapid recovery is the goal and
  connectivity varies across candidate sites."*

The "after" completes the actionability sentence, names the decision-maker, states scope conditions, and
generalizes the mechanism rather than the local number.

## Anti-patterns

- "Has implications for conservation" with no specific decision or action named
- Policy mandates built on correlational or single-site evidence
- Implications that only apply to the study system (no transferability)
- Borrowing a stronger verb than the design supports (see the proportionality ladder)
- Ignoring tradeoffs, costs, or social dimensions of the recommended action
- Overstating certainty of projections (PVA/SDM/climate) when arguing for action


## Operating pass for Conservation Biology

Treat this skill as an executable review pass, not a prose hint. First lock the species/system threat, conservation decision, and uncertainty relevant to action; then judge whether the current manuscript answers the venue's real reader: conservation-science reviewers who ask whether evidence changes biodiversity, management, or policy action.

- **Do the pass:** Return a claim-evidence-risk ledger rather than a prose-only diagnosis; every recommendation must point to a manuscript location or missing artifact.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against Biological Conservation for applied conservation breadth, Global Change Biology for climate/ecosystem process, Ecology Letters for theory-forward ecology; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Submission-ready gate:** do not give final advice until the pack's `resources/official-source-map.md` has been checked for upload-week rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Conservation problem】the decision at stake
【Finding → implication】what the result supports, proportional to evidence
【Actionability sentence】the one-line test, completed honestly
【Transferability】where/for whom else it applies
【Scope + tradeoffs】conditions, costs, risks acknowledged
【Next】conbio-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — conservation-intervention and evidence databases
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — scope: direct conservation implications and transferability
