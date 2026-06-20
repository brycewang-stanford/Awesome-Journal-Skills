---
name: jmcb-referee-strategy
description: Use when anticipating referee objections for a Journal of Money, Credit and Banking (JMCB) manuscript before submission (or before resubmitting), so the paper pre-empts the predictable monetary/banking pushbacks. Hardens the paper against its own reviewers; it does not draft the response letter (see jmcb-rebuttal).
---

# Referee Strategy (jmcb-referee-strategy)

## When to trigger

- The paper is near submission and you want to find the objections before a referee does
- You are unsure which editorial desk / referee type the paper will draw and how to address each
- A prior rejection's reports show a recurring objection you have not yet defused
- The contribution is sound but the paper has obvious unguarded flanks (shock cleanliness, demand contamination, inference)

## Who reviews at JMCB, and what they attack

JMCB papers are typically refereed by **monetary/banking specialists** who hold strong priors about mechanisms and are quick to spot the field's classic failures. Anticipate the reviewer *type* your paper will draw and pre-empt their reflexes:

| Referee type | What they reliably attack | Pre-empt by |
|---|---|---|
| Monetary-macro empiricist | shock contamination (information effect, anticipation); SVAR ordering; IRF inference | clean, info-robust shock; ordering/restriction sensitivity in the body |
| Banking micro-econometrician | demand vs. supply; clustering; M&A/identifier hygiene | firm×time FE; two-way clustering; merger-adjusted panel |
| Structural/quant modeler | what disciplines parameters; policy-invariance of the counterfactual | parameter-to-moment map; Lucas-critique defense |
| Policy-oriented reader | "so what for a central bank?"; magnitude plausibility | explicit policy lever; magnitudes benchmarked to known estimates |

## Building the pre-emption map

1. **List the three objections most likely to sink the paper**, by referee type, ranked by damage.
2. For each, decide whether to **fix it now** (add the analysis), **answer it in the text** (a paragraph that defuses it), or **flag it as a scoped limitation** (honest boundary). Most should be fixed or answered in the body, not deferred.
3. **Benchmark your magnitudes** against the canonical literature — a transmission elasticity or deposit beta that is an order of magnitude off the consensus will draw fire; pre-empt by situating it.
4. **Address the sibling-journal reflex** — a referee may think "this belongs at JME/JBF." Make the policy/monetary framing in the intro answer that before it is raised.
5. **Pre-write the hard-question answers** so that, if the report comes, the analysis already exists (this feeds `jmcb-rebuttal`).

## The standard objection arsenal at JMCB

These recur often enough that you should assume at least two will appear; pre-empting them in the body converts a likely revision round into a faster one:

- **"Your monetary shock is not exogenous."** The information effect, anticipation, and policy-rule endogeneity are the first things a macro referee tests. Have the info-robust version ready.
- **"This is demand, not supply."** For any bank-lending result, the demand-vs-supply identification is the reflexive objection. Firm×time fixed effects (or the single-vs-multi-bank-firm split) is the expected answer.
- **"Inference is overstated."** Two-way clustering, few-cluster corrections, and serial-correlation-robust bands are checked routinely on panels and time series.
- **"The magnitude is implausible / off-consensus."** A number far from the canonical literature without explanation reads as an artifact.
- **"Why JMCB and not JME/JBF?"** Implicitly a scope objection; if unanswered it can become a transfer recommendation rather than a revision.
- **"It does not replicate / the data are not reproducible."** Given the journal's archive history, vagueness about data construction or code draws fire early.

## Editor desk awareness

JMCB runs multiple editors with different specializations (monetary-macro vs. banking). The desk a paper draws shapes which referees and which objections dominate. You cannot choose the desk, but you can make the cover letter and intro speak to whichever lens is most likely — a banking paper should pre-empt the banking-econometrics objections most forcefully, a monetary-macro paper the shock-identification ones. Confirm current desks (待核实) before tailoring the cover letter.

## Checklist

- [ ] Top three likely objections listed by referee type and ranked by damage
- [ ] Each objection has a decided response: fix now / answer in text / scoped limitation
- [ ] Shock cleanliness (info effect) and demand-vs-supply pre-empted if applicable
- [ ] Inference (clustering, few-cluster, serial correlation) pre-empted
- [ ] Headline magnitudes benchmarked against the canonical literature
- [ ] The "why JMCB not JME/JBF" reflex answered in the intro
- [ ] Hard-question analyses pre-built so the rebuttal can cite them

## Anti-patterns

- Submitting with an obvious unguarded flank (raw-residual shock, one-way clustering) and hoping no one notices
- Treating every objection as fixable by an appendix table rather than a tightened argument
- Ignoring magnitude plausibility — a result far off consensus with no explanation invites rejection
- Leaving the sibling-journal question unanswered, so a referee recommends transfer instead of revision
- Writing defensive prose now that pre-argues with a referee who has not yet objected

## Limitations, stated on your terms

A short, honest limitations passage in the paper disarms referees more effectively than silence. State the scope conditions a referee would otherwise flag — the local nature of the estimate, the single-country sample, the regime the result is identified in — and frame each as a bounded claim rather than a weakness to be discovered. The aim is that the referee's objection is already acknowledged and scoped in your words, leaving them to evaluate the contribution rather than to "catch" an unstated flaw.

## Worked vignette (illustrative)

Before submitting a paper on monetary transmission through bank capital, the authors war-game the reviews. The banking referee will ask whether the lending response is demand; they pre-empt with firm×quarter fixed effects and say so in the body. The macro referee will question the shock; they use info-robust surprises and add an ordering-sensitivity panel. The policy reader will ask "so what?"; the intro now names capital regulation as the targetable lever. When the actual report later raises exactly the demand objection, the answer — and the table — already exist, turning a potential reject into a one-round revision.

## Turn the war-game into pre-built defenses

The payoff of anticipating objections is that the analysis exists before the report does. For each top objection, run the defensive analysis now and keep it ready — even if it lives in the online appendix at submission. When the report later raises that exact point, the response is "see Appendix B.4, which we already provide," and the revision is a single round rather than two. This is the highest-leverage use of pre-submission time: the objections you cannot pre-empt in the body, you pre-answer in the drawer. It also feeds directly into `jmcb-rebuttal`, where these pre-built tables become the point-by-point responses.

## Output format

```text
【Journal】Journal of Money, Credit and Banking
【Skill】jmcb-referee-strategy
【Likely referee types】which specialists this paper draws
【Top objections】3 ranked by damage, tagged by referee type
【Response per objection】fix now / answer in text / scoped limitation
【Magnitude benchmark】headline situated vs. canonical estimates
【Sibling reflex】how the intro answers "why not JME/JBF"
【Feeds】jmcb-rebuttal (pre-built answers) / back to jmcb-robustness or jmcb-identification if a fix is needed
【Next skill】jmcb-rebuttal
```
