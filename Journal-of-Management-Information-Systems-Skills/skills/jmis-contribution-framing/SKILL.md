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

## Checklist

- [ ] A three-sentence contribution (didn't know → now know → why it matters) is drafted
- [ ] The advance is to a named IS conversation, not only a reference discipline
- [ ] The IT artifact is essential to the contribution
- [ ] A concrete managerial/economic implication is stated (not generic "implications for practice")
- [ ] The claim is narrower than the evidence; ruled-out alternatives and boundaries are named
- [ ] Intro "we show that…" and discussion implications state the same contribution

## Anti-patterns

- A reference-discipline contribution (pure econ/marketing/CS finding) with no IS advance
- "Implications for practice" as a throwaway paragraph with nothing actionable
- An implicit contribution the reader must infer from tables
- Overclaiming a causal or general effect the design cannot support
- A contribution sentence in the intro that the discussion silently contradicts

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
