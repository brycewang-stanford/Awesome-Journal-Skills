---
name: jimf-referee-strategy
description: Use when anticipating and pre-empting referee objections before submitting a Journal of International Money and Finance (JIMF) manuscript. Maps the likely international-finance pushbacks to fixes you make now; it does not draft the post-decision response (jimf-rebuttal).
---

# Referee Strategy (jimf-referee-strategy)

## When to trigger

- The paper is near submission and you want to see it through a JIMF referee's eyes first
- You suspect a predictable objection (endogeneity, "it's just the GFC," US-centrism) is unanswered
- You need to decide which checks to run *now* versus hold in reserve for a revision
- The contribution is solid but the framing invites a "wrong journal" or "incremental" rejection

## How JIMF referees read a paper

A JIMF referee is usually an international-finance specialist who will probe three things in order: **is the contribution genuinely international and non-incremental; is the identification credible against global confounders; and is the result robust to the field's standard fragility checks (episode, dollar, regime, measure).** The most common reasons for rejection are not statistical errors but (1) thin international content, (2) a causal claim that is really a correlation with a global driver, and (3) results that do not survive dropping the obvious episode or the US. Anticipate these.

| Predictable JIMF objection | Pre-empt it now by |
|----------------------------|--------------------|
| "This is incremental / not enough new for an international audience" | Stake the contribution against the named frontier program (jimf-literature-positioning) |
| "This belongs at JIE / JME / JMCB / JFE" | Draw the sibling boundary explicitly in the intro and cover letter |
| "Your causal claim is the global financial cycle, not your variable" | Add time FE / push-pull interaction so within-time variation identifies (jimf-identification) |
| "Your surprise is contaminated by the information channel" | Purge / sign-correct the surprise and show the test |
| "It's just the 2008 crisis / the dollar" | Drop the episode; drop the US; use NEER (jimf-robustness) |
| "Policy is endogenous to the outcome" | Argue timing exogeneity; instrument; placebo countries |
| "Your inference ignores cross-country dependence" | Two-way clustering / Driscoll–Kraay / wild bootstrap |
| "EPFR isn't BoP flows" / measurement dispute | Declare and defend the measure; show the alternative (jimf-empirical-design) |
| "No policy takeaway" | Add a bounded, defensible implication for a central bank / IMF reader |

## Building the pre-emption plan

1. **Triage by lethality.** A "wrong journal" or "global-confounder" objection can sink the paper; a "typo in Table 3" cannot. Fix the lethal ones before submission, even at the cost of delay.
2. **Decide visible vs. reserve.** Put the answers to the top three objections in the main text (the editor reads it); hold lower-priority checks in the online appendix or in reserve for the revision so you have something to give.
3. **Pre-write the hard paragraph.** For the single most dangerous objection, draft the paragraph you would write in a response letter now — if you cannot write it convincingly, the paper is not ready.
4. **Suggest reviewers who know the program** (if the journal asks) and avoid conflicts; a referee from the right sub-literature is more likely to see the contribution.
5. **Use the cover letter to frame the contribution and the journal fit** so the editor does not desk-reject on a "scope" reflex.

## Distinguishing this skill from jimf-rebuttal

Referee strategy is *pre-submission*: you are the adversary, simulating the report before it exists so you can fix the lethal objections while it is cheap. Rebuttal is *post-decision*: a real report has arrived and you respond. Use this skill to decide what to run and what to hold before you press submit; switch to `jimf-rebuttal` once a decision letter is in hand. The two share a threat vocabulary (global-confounder, drop-US, inference, scope) but differ in leverage: before submission you can re-architect; after, you are negotiating within the editor's framing.

## Worked vignette (illustrative)

Before submitting a paper on capital-control effectiveness, the author audits it as a referee. The lethal objection: controls are imposed when flows surge, so the timing is endogenous, and any "effectiveness" is mean-reversion. The pre-emption: foreground an institutional feature that makes the *timing* plausibly exogenous (a control triggered by a calendar rule or an external mandate, not the flow level), add placebo countries that faced the same global surge without imposing controls, and put the pre-trend test in the main text. The author also pre-writes the response paragraph; finding it hard to write convincingly, they add a difference-in-differences against the placebo set before submission rather than after.

## Reading the JIMF process to set expectations

JIMF is a high-volume Elsevier field journal: desk-rejection on scope/incrementality is real, and turnaround and acceptance rates vary (待核实 — do not quote a specific figure). Two practical implications for strategy: (1) the editor's first decision is often a scope/fit triage, so the cover letter and intro must make the international contribution unmissable; (2) reports tend to be empirical and specific (the "drop the US," "rule out the GFCy," "fix the clustering" family) rather than abstract, so pre-empting the concrete checks is more valuable than polishing framing alone.

## Checklist

- [ ] The three most lethal objections identified and answered in the main text
- [ ] "Wrong journal" pre-empted by an explicit sibling boundary (JIE/JME/JMCB/JFE)
- [ ] The global-confounder objection answered with time FE / push-pull, not just controls
- [ ] The "drop the episode / drop the US" checks are in the paper before a referee asks
- [ ] Inference objection pre-empted (clustering/dependence handled)
- [ ] A bounded policy takeaway present for the policy-economist referee
- [ ] "Wrong journal" managed on title, first paragraph, and cover letter simultaneously
- [ ] Load-bearing checks are in the paper; only discretionary checks held in reserve
- [ ] A reserve of lower-priority checks held for the revision

## Anti-patterns

- Submitting with the obvious "it's the GFC / it's the dollar" objection unaddressed and hoping the referee misses it
- Burying the answer to the most dangerous objection in a footnote or the appendix
- Treating a scope/"wrong journal" risk as unmanageable instead of framing the fit in the cover letter
- Front-loading every robustness check so there is nothing left to offer in a revision
- Suggesting reviewers with conflicts, or from the wrong sub-literature who will miss the contribution
- Assuming a clever identification excuses thin international content — JIMF's first filter is the international margin

## The "wrong journal" risk is the one to manage hardest

Because JIMF sits among close siblings, a non-trivial share of rejections are scope decisions rather than quality decisions. Manage this on three surfaces simultaneously: the **title** (lead with the international object — exchange rate, capital flow, spillover, sovereign), the **first paragraph** (state the open-economy question, not the data), and the **cover letter** (one sentence on why this is *international money and finance* and not JIE/JME/JMCB/JFE). If a careful reader could still finish the abstract unsure whether the paper is international, the scope risk is unmanaged and a fix is cheaper now than a transfer later.

## Choosing what to hold in reserve

A revision is a negotiation, and it helps to enter it with checks the referee will be glad to receive. Put the lethal answers (global-confounder, drop-US, drop-episode, inference) in the submitted paper, but keep a few credible-but-secondary checks — an alternative GFCy proxy, a sub-period split, an additional placebo set — ready to deploy in the first response. This signals responsiveness and gives the referee a visible win without re-architecting the paper. Do not, however, withhold a check the result actually needs to be believed: reserve is for the discretionary, not the load-bearing.

## Output format

```text
【Journal】Journal of International Money and Finance
【Skill】jimf-referee-strategy
【Top 3 lethal objections】<scope / global-confounder / robustness / inference / measurement>
【Answered in main text】each lethal objection addressed before review? [Y/N]
【Sibling-boundary pre-empt】JIE/JME/JMCB/JFE framed? [Y/N]
【Policy takeaway】bounded implication present? [Y/N]
【Reserve checks】held for revision: <list>
【Next skill】jimf-rebuttal (after a decision letter arrives)
```
