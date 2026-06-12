---
name: agsy-impact-and-implications
description: Use when articulating why an Agricultural Systems (AgSy) result matters — its relevance for farm design, management, decision support, or policy. AgSy values systems analysis that informs a decision, so this is what separates an AgSy paper from a methods demo. It frames implications honestly within the model's scope; it does not over-claim or invent impact.
---

# Impact & Implications (agsy-impact-and-implications)

AgSy publishes systems analysis that **informs a decision** — how to design or manage a farm, what
trade-off a policy faces, where to intervene in a food system. A technically sound model with no
decision relevance reads as a methods demo. This skill turns systems results into **honest, scoped
implications** without over-claiming.

## When to trigger

- Writing the discussion, implications, or conclusion section
- The model and evaluation are sound but the "so what for decisions" is thin
- A reviewer said the paper is "academic," "no clear application," or "over-claims its policy reach"
- Framing recommendations for farmers, advisers, or policymakers

## How to frame implications

1. **Name the decision.** Who decides what differently because of this result — a farmer choosing a
   rotation, an adviser targeting an intervention, a policymaker weighing an instrument?
2. **State the trade-off, not a single "best."** Systems results are about trade-offs and synergies; an
   honest implication says "option A gains X but costs Y," and for whom.
3. **Scope it to the system and the evidence.** Implications hold within the system boundary, scales,
   and conditions you modelled and evaluated. Say where they likely do **not** transfer.
4. **Be honest about uncertainty.** Tie the strength of the recommendation to the uncertainty from
   `agsy-data-and-model-evaluation`. Do not let a wide ensemble become a confident policy claim.
5. **Connect to the bigger system.** Where relevant, link the farm/landscape result to food security,
   environment, climate, or livelihoods — the interactions AgSy cares about.

## The decision-relevance test (AgSy-specific)

Write one sentence: *"Because of this analysis, [actor] should weigh [option] differently because the
system trades off ___ against ___, under conditions ___."* If you cannot, the paper has results but no
implications — strengthen the framing or the scenario design.

## Anti-patterns

- A discussion that only restates results with no decision relevance
- Recommending a single "optimal" option while hiding the trade-off
- Generalizing beyond the modelled system, scales, or conditions
- A confident policy claim resting on high-uncertainty output
- Implications that ignore the social/economic side of the system

## Worked micro-example: scoping a claim honestly (illustrative)

A climate-adaptation analysis finds shifting sowing dates raises modelled gross margin under a drier
ensemble. Three drafts of the implication, weakest to strongest:

- *Over-claim:* "Farmers should shift sowing dates to adapt to climate change." — generalizes past the
  modelled system, scales, and conditions.
- *Bare result:* "Sowing-date shifts increased simulated margin." — true but no decision, no trade-off.
- *Scoped (the move):* "Under the drier ensemble, advisers for rainfed mixed farms in this region could
  weigh earlier sowing, which raises modelled margin ~6% but increases wet-year failure risk ~10%
  (illustrative); the trade-off and the wide ensemble make it a contingent recommendation, not a rule."

## Referee pushback → the AgSy-specific fix

- *"The paper over-claims its policy reach."* → Re-scope to the modelled system, scales, and conditions;
  state explicitly where the result does not transfer.
- *"No clear application."* → Name the actor and the decision margin; write the decision-relevance
  sentence and tie it to a scenario.
- *"A single 'best' option is recommended."* → Surface the trade-off and report what each option gives
  up, and for whom.
- *"The recommendation outruns the uncertainty."* → Match recommendation strength to the ensemble width.


## Implication pass for Agricultural Systems

Run this as a concrete capability pass. First lock the system boundary, actor decision, model/data linkage, and sustainability or food-security tradeoff; then test whether the manuscript addresses agricultural-systems reviewers who expect crop, farm, value-chain, environment, and policy components to be connected rather than listed.

- **Primary move:** Name the actor, decision margin, system tradeoff, and evidence limit; do not let broad impact language outrun the design.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against Field Crops Research for plot-level agronomy, Global Food Security for policy synthesis, Agricultural Economics for economics-first work; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Decision】who acts differently and how
【Trade-off】what is gained vs. given up, for whom
【Scope】system boundary / scales / conditions where it holds (and not)
【Uncertainty-matched】recommendation strength tied to uncertainty? [Y/N]
【Wider link】food security / environment / climate / livelihoods
【Next】agsy-reproducibility-and-data-policy
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — food-system data and trade-off/decision tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — AgSy scope: decision and policy relevance of systems analysis
