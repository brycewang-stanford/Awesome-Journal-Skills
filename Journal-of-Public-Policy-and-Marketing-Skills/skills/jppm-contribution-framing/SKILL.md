---
name: jppm-contribution-framing
description: Use when sharpening the policy contribution of a Journal of Public Policy & Marketing (JPP&M) manuscript — the 300-word Policy Contribution Statement, regulator-actionable implications, and the line between evidence and advocacy. Frames the contribution; it does not produce the estimates (jppm-data-analysis).
---

# Contribution Framing (jppm-contribution-framing)

## When to trigger

- The Policy Contribution Statement draft is generic or missing one of its three required elements
- The implications section says "policymakers should consider" and stops
- Findings are solid but you cannot connect them to a decision anyone faces
- The paper drifts into recommending policies the data never tested
- Reviewers might read the framing as advocacy rather than evidence

## The Policy Contribution Statement is the contribution

JPP&M requires every submission to open the main document with a **Policy Contribution Statement of at most 300 words** (it does not count against the 50-page cap). It must do three things, per the journal's guidelines: (1) name the **policy conversation** the paper initiates or joins; (2) state how the manuscript **moves understanding beyond** the existing marketing-and-public-policy literature; (3) identify **which specific policy stakeholders** are affected and **how**. Treat this statement as the paper's thesis, not an administrative form — editors use it for desk-screening and reviewers read it first. If the statement cannot be written crisply, the problem is upstream (fit or evidence), not wording.

A working shape: *"Agencies X and Y are currently deciding D. Existing work establishes A but cannot tell them B. Using [design], we show E [magnitude, for whom]. This implies stakeholder X should [specific action within its authority], while marketers subject to the rule should [specific response]."*

## The actionability test

For each implication, ask four questions; all must pass:

1. **Named actor** — a specific body (FTC, FDA, CFPB, USDA, state AGs, a self-regulatory program like CARU/NAD, an NGO, or firms facing the rule), not "policymakers."
2. **Within authority** — the action lies inside that actor's legal instruments. Recommending the FTC set nutrition standards, or the FDA police deceptive pricing, signals the authors don't know the terrain.
3. **Evidence-linked** — the recommended choice is one the paper's contrasts or estimates actually inform. If you tested icon vs. text warnings, you can advise on format — not on whether warnings beat taxes.
4. **Concrete enough to implement or reject** — a reader at the agency could put it into a rule, guidance, enforcement priority, or comment letter tomorrow.

Marketers are stakeholders too: what should a compliant firm change in labeling, targeting, data practice, or claims substantiation? A JPP&M implication set that speaks to both the regulator and the regulated is stronger than one that lectures only the agency.

## Evidence, not advocacy

JPP&M welcomes normatively motivated questions but punishes advocacy untethered from results. Discipline the frame: report what the intervention does *and does not* achieve; keep recommendation strength proportional to identification strength (a lab study "suggests"; a well-identified evaluation "shows"); surface the trade-offs (costs to firms, burden on consumers, speech concerns) even when they cut against the preferred conclusion. Papers that acknowledge the strongest counterargument to their own implication read as trustworthy; papers that hide it read as briefs.

## Calibrating claims to evidence

- **Scope**: bound the claim to the tested population, product category, and format; flag the extrapolation needed to reach the policy scale.
- **Magnitude honesty**: lead with the decision-unit effect and its CI, not with the significance.
- **Null and backfire results are contributions**: "the mandated format does not help, and here is why" is publishable and policy-critical here — do not bury it.
- **One primary implication**: a single well-defended recommendation beats a scattershot list of six.

## Checklist

- [ ] Policy Contribution Statement ≤300 words, covering conversation / advance / stakeholders
- [ ] Every implication names an actor, sits within its authority, and is evidence-linked
- [ ] Implications address both regulator and regulated marketers where relevant
- [ ] Recommendation strength matches identification strength
- [ ] Trade-offs and the strongest counterargument are stated
- [ ] Nulls, boundary conditions, and unintended effects appear in the framing, not the footnotes

## Anti-patterns

- **The bolted-on paragraph**: a consumer study with policy vocabulary appended in the discussion — JPP&M's signature desk reject
- **Ghost-actor implications**: advice addressed to "policymakers" or "society"
- **Authority errors**: recommendations outside the named agency's legal instruments
- **Advocacy leakage**: recommendation strength driven by conviction rather than estimates
- **Implication inflation**: six recommendations from one manipulation
- **Buried backfire**: an unintended consequence found in the data but absent from the statement

## Output format

```text
【Policy Contribution Statement】conversation / advance / stakeholders (≤300 words, drafted)
【Primary implication】named actor + instrument + specific action
【Marketer-facing implication】what regulated firms should change
【Evidence link】which estimate licenses each recommendation
【Trade-offs stated】costs, burdens, counterargument acknowledged? [Y/N]
【Next skill】jppm-tables-figures
```
