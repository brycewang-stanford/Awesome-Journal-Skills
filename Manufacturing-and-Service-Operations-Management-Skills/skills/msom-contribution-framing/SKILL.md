---
name: msom-contribution-framing
description: Use when turning analytical or empirical results into an explicit operations contribution for a Manufacturing & Service Operations Management (M&SOM) manuscript — stating the managerial implication, the new operational insight, and why an operations decision is central, including the structured-abstract framing M&SOM requires.
---

# Contribution Framing (msom-contribution-framing)

## When to trigger

- Results exist but the "so what for operations" is implicit or thin
- A Department Editor says the contribution is incremental or the OM core is unclear
- You are writing the introduction's contribution paragraph or the structured abstract
- You must make the managerial implication explicit, not optional

## Make the operational insight explicit

M&SOM judges manuscripts on **importance, originality, clarity, validity, and relevance**, and gates on an **operations decision being central**. State plainly: *what operational decision does this paper change, and how?* For analytical work, the contribution is usually the **structure** of the optimal policy and the **comparative statics** a manager can act on (e.g., "stock-up-to a threshold that rises in lead-time variability"). For empirical work, it is a **credibly identified operational effect** and the policy it implies. Avoid framing the contribution as a methodological novelty alone — the operations insight must lead.

## Managerial relevance is a required, sectioned component

M&SOM requires a **structured abstract** (≤ 300 words, no technical jargon): **Problem definition**, **Methodology-results**, and **Managerial implications**. Managerial relevance is therefore not optional framing — it is an explicitly sectioned deliverable. Write the contribution paragraph and the abstract so each required section is answerable in one or two plain-language sentences a practitioner could follow.

## Route the contribution to the right Department

Frame the contribution in the vocabulary of your target Department (supply chain, services/revenue management, sustainability/health, operational innovation, analytics, or practice). If the work is field-driven, consider whether the **Practice Platform** is the better home; a perspective piece is an **OM Forum** banner article, not a standard contribution.

## Checklist

- [ ] One sentence: the operational decision this paper changes and how
- [ ] Analytical: policy structure + actionable comparative statics stated
- [ ] Empirical: identified effect + the operational policy it implies stated
- [ ] Structured abstract drafted with all three required sections, ≤300 words, jargon-free
- [ ] Contribution framed in the target Department's terms
- [ ] Operations centrality reaffirmed (not a method-only contribution)

## Anti-patterns

- Leading with "we develop a new model/estimator" and burying the operational insight.
- A structured abstract missing the Managerial-implications section or stuffed with notation.
- Claiming generic "implications for managers" with no operational lever named.
- Framing the work outside any department's scope.


## Contribution pass for Manufacturing & Service Operations Management

Run this as a concrete capability pass. First lock the process bottleneck, decision policy, queue/inventory/service mechanism, and implementation constraint; then test whether the manuscript addresses operations reviewers who look for service/manufacturing process insight, implementable policies, and operational performance evidence.

- **Primary move:** Translate the result into who learns what, which mechanism changes, and which alternative explanation is ruled out; keep the claim narrower than the evidence.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against Management Science for broader OR/MS reach, Production and Operations Management for wider OM readership, Operations Research for method-first theory; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Worked micro-example (illustrative)

The premium clause M&SOM rewards is the **managerial insight that survives the model** — a sentence a department editor can repeat to a practitioner.

Vignette: a staffing model for a hospital emergency department where physicians flex between fast-track and main-track queues. Suppose the numerical study reports — illustratively — that flexing 15% of physician-hours cuts the 90th-percentile wait from 48 to 31 minutes at equal headcount. Through the contribution rules: the **decision changed** is the roster split between dedicated and flexible hours; the **insight** is that the optimal flex share *rises in arrival-rate asymmetry between tracks*; the **managerial sentence** — "hold about an eighth of capacity flexible when loads diverge" — slots into the Managerial-implications section.

## Referee-pushback patterns and the venue fix

- *"Tractable, but the result has no managerial takeaway."* → Add the decision rule plus its comparative static; lead with it, not the theorem.
- *"This is a Management Science / Operations Research paper — where is the operations decision?"* → Re-anchor on the operating lever; cut framing that foregrounds the method's generality. If the managerial-implications subsection just restates results, rewrite it as plain-language advice with the magnitude attached.

## Output format

```
【Operational decision changed】...
【Structure / identified effect】...
【Managerial implication】plain language ...
【Structured abstract】Problem definition / Methodology-results / Managerial implications (≤300 words)
【Department fit】...
【Next step】msom-tables-figures
```
