---
name: aejpol-literature-positioning
description: Use when placing the contribution against the policy-evaluation literature and sharpening it as a policy answer for an AEJ: Economic Policy manuscript. Stakes the contribution and the policy-relevant "so what"; it does not write the full introduction or design the identification.
---

# Literature Positioning & Contribution Framing (aejpol-literature-positioning)

## When to trigger

- The contribution vs. existing policy evaluations is fuzzy, or sounds like "we add another estimate"
- A referee asks "what do we learn beyond [prior study of this or a similar policy]?"
- The literature review is a list of citations rather than a map of the open policy question
- You need to frame the contribution so the **policy lesson**, not the method, is the news

## How AEJ: Policy contributions are staked

At AEJ: Policy the contribution is a **better answer to a policy question**, not a new estimate for its own sake. Position the paper on three axes and make the policy reading the headline:

1. **The policy-design gap.** What does a policymaker still not know — the sign, the magnitude, the cost-effectiveness, the incidence, the optimal level, or the external validity of an existing estimate? State the gap as something a decision-maker would care about.
2. **The credibility upgrade.** If prior evidence exists, say why yours is more credible (cleaner design, better data, a policy variation that breaks a confound, a setting that fixes external-validity worries) — but only as a means to a sharper policy answer.
3. **The welfare/cost-benefit advance.** The distinctive AEJ: Policy move: convert estimates into a welfare or cost-benefit statement (MVPF, cost-per-outcome, incidence, deadweight loss) that prior work left implicit. This is often the real contribution.

### Positioning patterns that land
- *"Prior work estimates the effect; we show whether it is worth it"* (adds the cost-benefit reading).
- *"Estimates exist for setting A; we show they do/do not travel to the policy-relevant setting B"* (external validity for policy).
- *"The textbook prescription assumes X; we show the policy-relevant elasticity implies a different optimum"* (re-optimizing the policy).
- *"Reduced-form effects were known; we recover the sufficient statistic the welfare calculation needs"* (links to `aejpol-theory-model`).

### Citation discipline (AEA house)
Author–year throughout; cite the canonical methods papers behind your design (e.g., modern DID, RDD) and the **key policy-evaluation papers on this and adjacent policies** — referees expect you to know the policy literature, not only the econometrics.

## Checklist

- [ ] The open policy question is stated as a gap a decision-maker would recognize
- [ ] Contribution framed as a sharper policy answer, not "one more estimate"
- [ ] If prior estimates exist, the credibility or welfare upgrade is explicit
- [ ] At least one contribution bullet is a welfare/cost-benefit/distributional advance
- [ ] Both the relevant policy literature and the methods literature are cited (author–year)
- [ ] No overclaim of novelty that a referee can puncture with one citation

## Anti-patterns

- "We provide new evidence on X" with no statement of what was unknown and why it matters for policy
- A literature review that is a taxonomy of papers, not a map to the open policy question
- Claiming to be first while ignoring a close policy-evaluation paper (fast desk-reject signal)
- Positioning purely on identification cleverness with no policy-design or welfare advance
- Numbered `[1][2]` citations instead of AEA author–year

## Referee pushback mapped to the fix

- *"What do we learn beyond [prior study of this policy]?"* → State the specific policy-design gap (sign / magnitude / cost-effectiveness / incidence / external validity) you close, not "new evidence."
- *"This duplicates a known result."* → Lead with the credibility or welfare upgrade; show the prior estimate could not deliver the cost-benefit reading you do.
- *"Novelty is overstated."* → Cite the closest paper explicitly and scope your claim to the margin you actually advance.

## Worked vignette (illustrative)

A draft on a carbon tax says "we estimate the emissions response." Referees note three prior estimates exist. Repositioned: the prior estimates ignore the **revenue-recycling** margin; this paper recovers the response **and** the incidence of the recycled revenue, so it can state the **net welfare cost per ton abated** under alternative recycling rules (illustrative) — a cost-benefit advance no prior estimate delivered. The contribution is now a policy answer, not a fourth elasticity.

## How the three contribution bullets read in the intro

A strong AEJ: Policy intro states the contribution as up to three numbered moves, at least one of them a welfare advance: (1) **credibility** — "we exploit [variation] that prior work could not, removing [confound]"; (2) **magnitude / external validity** — "we provide the policy-relevant estimate for [population/scale] where prior estimates do not travel"; (3) **welfare** — "we convert the effect into [MVPF / cost-per-outcome / incidence], the object a policymaker needs." Keep each to one sentence and make the welfare bullet the one a reader remembers.

## Output format

```
【Open policy question / gap】what a decision-maker still does not know
【Closest prior work】1–3 papers + the specific limitation you address
【Contribution bullets】(a) credibility / (b) magnitude / (c) welfare-cost-benefit — ≥1 must be welfare
【Policy "so what"】one sentence a non-specialist policymaker would grasp
【Next step】aejpol-identification (design) or aejpol-theory-model (welfare mapping)
```
