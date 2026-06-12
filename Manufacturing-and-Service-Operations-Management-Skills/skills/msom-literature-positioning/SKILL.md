---
name: msom-literature-positioning
description: Use when positioning a Manufacturing & Service Operations Management (M&SOM) manuscript within the operations-management literature — engaging the canonical OM streams (inventory, queueing, supply-chain contracting, revenue management, service operations, empirical OM), selecting the target editorial Department, and stating the operational conversation the paper joins.
---

# Literature Positioning (msom-literature-positioning)

## When to trigger

- Your front end reads as "no one has studied X" rather than joining an OM conversation
- A reviewer says the relevant operations stream is not engaged
- You are unsure which of the six Departments the related work points to
- You need to distinguish your contribution from close OM antecedents

## Join an operations conversation, not a generic gap

M&SOM positions itself as the **premier journal for the operations management research community**. Position the paper inside the established OM streams it speaks to — e.g., inventory/supply-chain (newsvendor, base-stock, contracting and coordination), queueing and service operations, revenue management and pricing, platforms and matching, sustainable/healthcare operations, or empirical/data-driven OM. State the **operational conversation** you join and what you change in it, rather than claiming a void.

## Let the citations point to a Department

The literature you engage should make your **target Department** obvious to an editor — Manufacturing & Supply Chain Operations; Services, Platforms & Revenue Management; Environment, Health & Society; Operational Innovation; Analytics in OM; or the Practice Platform. Scattering across departments signals an unfocused contribution. Cite the foundational results your model or estimation builds on (the policy structures, the contracting benchmarks, the identification strategies) so reviewers see you stand on the right shoulders.

## Distinguish from close antecedents on the operational lever

Differentiate not by "different data" but by the **operational decision or mechanism** you newly capture: a richer model primitive, a relaxed assumption that changes the optimal policy form, a previously untested operational channel, or a credibly identified effect a prior analytical paper only conjectured. Analytical-vs-empirical complementarity is a strong position: empirically testing a structural prediction, or analytically explaining an empirical regularity.

## Checklist

- [ ] Two to four canonical OM streams explicitly engaged
- [ ] Target Department evident from the citation pattern
- [ ] Foundational results your contribution builds on are cited
- [ ] Differentiation stated in terms of the operational lever/mechanism, not just setting
- [ ] Contribution framed as joining/advancing a conversation, not filling a void

## Anti-patterns

- "No prior work has examined…" gap-spotting with no engaged OM stream.
- Citing across all six departments so the fit is ambiguous.
- Differentiating only by dataset or industry, not by the operations mechanism.
- Ignoring the closest analytical or empirical antecedent because it is inconvenient.


## Positioning pass for Manufacturing & Service Operations Management

Run this as a concrete capability pass. First lock the process bottleneck, decision policy, queue/inventory/service mechanism, and implementation constraint; then test whether the manuscript addresses operations reviewers who look for service/manufacturing process insight, implementable policies, and operational performance evidence.

- **Primary move:** Build a three-column map: incumbent conversation, unresolved tension, and this manuscript's delta; include one sibling-venue omission that would make a referee doubt the fit.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against Management Science for broader OR/MS reach, Production and Operations Management for wider OM readership, Operations Research for method-first theory; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Worked micro-example (illustrative)

Vignette: an empirical study of a ride-hailing platform testing whether surge pricing reduces driver idle time. Weak positioning is "no paper has studied surge and idle time." M&SOM positioning instead anchors on the matching-and-pricing-in-service-platforms conversation (Services, Platforms & Revenue Management), cites the revenue-management and queueing antecedents the design builds on, and states the delta as an *operational mechanism*: surge reallocates supply across a spatial queue, and the paper credibly identifies the idle-time elasticity that prior analytical platform models only conjectured. Empirically testing a structural prediction is a strong M&SOM position and makes the target department self-evident.

## Referee-pushback patterns and the venue fix

- *"You frame a void instead of joining a conversation."* → Replace "no one has studied X" with the OM stream you advance and the specific tension you resolve in it.
- *"The closest antecedent is uncited / waved off."* → Engage it head-on and differentiate on the operational lever, not on dataset or industry.
- *"Fit is ambiguous across departments."* → Prune citations that pull toward a second department; let one stream dominate so routing is unambiguous.

## Output format

```
【OM streams engaged】...
【Implied Department】...
【Foundational works cited】...
【Differentiation】operational lever/mechanism that is new ...
【Conversation joined】...
【Next step】msom-methods
```
