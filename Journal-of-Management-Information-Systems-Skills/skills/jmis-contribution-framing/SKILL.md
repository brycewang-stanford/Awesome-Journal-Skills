---
name: jmis-contribution-framing
description: Use when turning results into an explicit contribution for a Journal of Management Information Systems (JMIS) manuscript — an advance to an IS-management/economics conversation with theoretical and managerial implications. Frames the contribution and aligns intro/discussion; it does not position the literature (jmis-literature-positioning) or run the submission preflight (jmis-submission).
---

# Contribution Framing (jmis-contribution-framing)

## When to trigger

- Results exist but the "so what for IS management" is thin or implicit
- A reviewer or the EIC says the contribution is incremental or reads as a reference-discipline result
- The paper is a competent study with no clear advance to a JMIS conversation
- The introduction's "we show that…" sentences and the discussion's implications do not match

## What counts as a JMIS contribution

JMIS rewards a contribution to the **technology–organization–economics nexus**: a finding that changes what the IS field believes *and* what a manager, firm, platform, or policymaker should do about technology. Strong JMIS contributions:

- **Advance a named IS conversation** (IT value, platforms, e-commerce, IS economics, security/privacy, analytics) — not only a reference discipline.
- **Make the IT artifact essential** to the advance: delete the technology and the contribution collapses.
- **Carry a managerial/economic payload.** Beyond theory, say what changes for practice — pricing, governance, investment, design, policy. JMIS's identity makes the practical implication first-class, not an afterthought.
- **Match the genre's currency.** An empirical paper contributes a credibly identified effect and mechanism; an analytical paper contributes a new insight/comparative static; a design-science paper contributes a useful, evaluated artifact and generalizable design knowledge.

## Write the contribution as a claim narrower than your evidence

Translate results into three sentences: *what we did not know → what we now know → why it matters for IS theory and practice.* Then deliberately make the claim narrower than the evidence supports — overclaiming beyond the identification/proof/evaluation is the fastest route to reviewer distrust. Name the alternative explanation you ruled out and the boundary where the effect stops.

## Align the introduction and discussion

The contribution must appear explicitly, and consistently, in two places: the **introduction** ("we show that…", stated for an IS reader) and the **discussion**, which revisits it with implications for IS theory, for managers/firms/platforms, and — where apt — for policy, plus honest boundary conditions and future work. Do not leave the contribution for the reader to reconstruct from the results section.

## Decision ledger to hand to the next pass

Return rows of `claim / evidence / blocker / next edit` so the manuscript can be patched directly. If the contribution depends on a fact that is volatile (a process rule, a fee), reopen `resources/official-source-map.md` and name the one unresolved item.

## Worked vignette: narrowing the claim to fit the evidence (illustrative)

A results section supports: "the recommender redesign reduced marginal-seller retention on this marketplace over 2023–24." The discussion, though, claims "personalized ranking harms platform ecosystems." That overclaim invites a reviewer to list every boundary the paper did not test (other platforms, other periods, buyer-side gains). The JMIS-grade contribution states the narrower true claim, names what it does *not* establish (welfare, generalization across platform types), and converts the boundary into a managerial nuance: *aggressive personalization trades short-run match quality against long-run seller supply, so the optimal intensity depends on how supply-constrained the platform is.* Narrower claim, stronger paper, clearer practice implication.

## Referee pushback mapped to a framing fix

- *"Contribution is unclear / incremental."* → Lead with the three-sentence didn't-know → now-know → why-it-matters and name the exact IS belief you move.
- *"This is an economics finding, not an IS one."* → Make the IT artifact essential and the implication actionable for an IS decision-maker.
- *"You overclaim."* → State the narrower claim, name ruled-out alternatives and boundaries, and align the intro and discussion to it.

## Checklist

- [ ] A three-sentence contribution (didn't know → now know → why it matters) is drafted
- [ ] The advance is to a named IS conversation, not only a reference discipline
- [ ] The IT artifact is essential to the contribution
- [ ] A concrete managerial/economic implication is stated (not generic "implications for practice")
- [ ] The claim is narrower than the evidence; ruled-out alternatives and boundaries are named
- [ ] Intro "we show that…" and discussion implications state the same contribution
- [ ] The contribution verb matches the genre (identify / insight / evaluated artifact)
- [ ] Both a theoretical and a managerial/economic payload are named and reinforce each other

## Make the dual contribution explicit

JMIS prizes work that contributes to *both* IS theory and IS practice, and the journal's management identity means the practical side is not optional. State the theoretical contribution (what the IS field now believes) and the managerial/economic contribution (what a firm, platform, CIO, or policymaker should do) as two distinct, named payloads — not one blurred "implications" paragraph. The two should reinforce each other: the mechanism you theorized is *why* the managerial advice holds, and the managerial advice is the *stakes* that make the mechanism worth knowing. A paper that nails the theory but offers only generic practice advice, or vice versa, reads as half a JMIS contribution.

## Anti-patterns

- A reference-discipline contribution (pure econ/marketing/CS finding) with no IS advance
- "Implications for practice" as a throwaway paragraph with nothing actionable
- An implicit contribution the reader must infer from tables
- Overclaiming a causal or general effect the design cannot support
- A contribution sentence in the intro that the discussion silently contradicts
- Claiming a contribution whose verb mismatches the genre (e.g., "we propose a construct" for an empirical paper)
- A theory contribution with only generic practice advice, or strong practice with no theory — half a JMIS contribution
- A contribution that depends on a volatile process fact left unverified against the source map

## Calibrate the contribution to the genre's currency

The same result earns credit differently depending on the paper's genre, and overclaiming the wrong kind of contribution invites pushback. An **empirical** paper's currency is a credibly identified effect plus the mechanism behind it — its contribution sentence should foreground "we identify" and "the mechanism is," not "we propose a new construct." An **analytical** paper's currency is a non-obvious insight or comparative static — claim the surprising result, not the existence of a model. A **design-science / data-science** paper's currency is an evaluated, useful artifact and the generalizable design knowledge it embodies — claim utility against credible baselines and the transferable principle, not raw accuracy. Match the verb to the genre and the contribution lands; mismatch it and a referee will say the paper "claims more than its genre delivers."

## Test the contribution against the EIC's fit gate

Before handing off to exhibits and prose, read the contribution as the EIC will at intake: is this an advance to an IS-management/economics conversation, or a reference-discipline result with an IS setting? If a sharp colleague could say "this is really an economics/CS/marketing paper," the framing has not yet earned its place at JMIS. Strengthen the IS-artifact dependence and the managerial payload until the contribution is unambiguously an IS contribution — that is the single most common reason a competent paper is returned.

## Output format

```text
【Contribution (3 sentences)】didn't know → now know → why it matters
【IS conversation advanced】[stream]
【IT-artifact dependence】why the technology is essential
【Managerial/economic payload】concrete action that changes
【Claim vs. evidence】narrower? alternative ruled out? boundary stated?
【Decision ledger】claim / evidence / blocker / next edit rows
【Next step】jmis-tables-figures
```
