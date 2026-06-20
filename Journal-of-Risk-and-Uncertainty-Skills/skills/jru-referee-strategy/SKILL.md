---
name: jru-referee-strategy
description: Use when anticipating likely referee objections for a Journal of Risk and Uncertainty (JRU) manuscript before submission. Wargames the report a risk/uncertainty specialist would write; it does not invent evidence or citations.
---

# Referee Strategy (jru-referee-strategy)

## When to trigger

- The draft is nearly done and you want to pre-empt the objections a JRU referee will raise
- You are choosing what to put in the main text vs. the appendix to disarm predictable pushback
- The paper makes a strong EU-vs-alternatives claim and you expect a referee from the camp it challenges
- You suspect the elicitation or the VSL identification has a soft spot a specialist will find

## Who reviews for JRU, and what they hunt for

JRU's reviewer pool is specialized — decision theorists, experimental risk researchers, and VSL/insurance empiricists, under a single-blind model typical of Springer econ journals (待核实). Each subculture has a signature objection. Wargame the report by reading the paper as each of these referees would.

| Referee type | Their reflex objection | Pre-empt by |
|--------------|------------------------|-------------|
| Decision theorist | "The representation has no behavioral content / the reference point is fit, not fixed" | Stating one prediction the model forbids; fixing the reference point a priori (`jru-theory-model`) |
| Experimentalist | "The elicitation is not incentive-compatible / it confounds u and w" | Defending the mechanism's IC assumptions; a design that separates curvature from weighting (`jru-identification`) |
| VSL / empirical economist | "Selection into risky jobs / publication-selection bias is ignored" | Selection probes and engagement with the meta-analytic benchmark (`jru-identification`, `jru-robustness`) |
| EU loyalist | "A risk-averse EU agent with a pessimistic belief explains this" | Deriving a comparative static EU cannot produce; separating beliefs from preferences |
| Methods skeptic | "Functional form drives the result" | Showing the parameter is stable across CRRA/CARA/expo-power and EU/non-EU (`jru-robustness`) |

## How to wargame

1. Assign the paper to its two most likely referee types and write their harshest one-paragraph objection each.
2. For every objection, decide: already answered (point to the section), answerable with existing data (add an exhibit), or a genuine limitation (state it candidly).
3. Move the evidence that disarms the top objection **into the main text** — do not leave your best defense in an appendix the referee may skim.
4. Pre-write the limitations paragraph: the objections you cannot fully resolve, stated before the referee does.
5. Hand off to `jru-submission` once the predictable objections are either answered or openly conceded.

## The questions a JRU report almost always asks

Regardless of referee type, certain questions recur in this journal's reports. Have an answer ready for each:

- *What exactly does your model predict that expected utility does not?* — the single most common decision-theory probe.
- *How do you separate utility curvature from probability weighting (or risk from ambiguity)?* — the measurement probe.
- *Is the elicitation incentive-compatible, and under what assumptions?* — the experimental probe.
- *Does the headline parameter survive a different functional form?* — the methods probe.
- *For VSL/insurance: is the effect a preference, or a belief / selection artifact?* — the empirical probe.

If any of these has no crisp answer in the main text, fix the paper before the referee writes the report.

## Worked second pass: choosing what to promote

After wargaming, rank the objections by lethality and move the *one* analysis that defuses the most lethal objection into a numbered main-text result, not a robustness footnote. A referee who finds the decisive check in Appendix C may still write "the authors do not address X" simply because they did not reach it. Promotion is cheap insurance in a single-blind specialist process where the referee's first impression carries weight.

## Checklist

- [ ] The two most likely referee types are named and their sharpest objection written out
- [ ] The decision-theorist's "no behavioral content" objection is pre-empted
- [ ] The experimentalist's incentive-compatibility / u-vs-w objection is pre-empted
- [ ] The EU-loyalist alternative explanation is addressed with a discriminating prediction
- [ ] For VSL/insurance: selection and publication-selection objections are met
- [ ] The best defense lives in the main text, not an appendix
- [ ] A candid limitations paragraph states what cannot be resolved

## Suggesting and excluding reviewers

In a small specialist pool the reviewer suggestions carry weight:

- **Suggest** scholars who work on your exact primitive and method, including some who might disagree but would review fairly — a credible suggestion list signals you know the field.
- **Exclude** only genuine conflicts (advisors, recent coauthors, direct rivals with a stake) and say why briefly; a long exclusion list reads as fear of scrutiny.
- Anticipate that the editor may still pick a referee from the camp your paper challenges — write the paper to survive that draw, do not try to route around it.

## Anti-patterns

- Writing only for a friendly referee and ignoring the camp the paper challenges
- Leaving the decisive robustness check in the appendix where a skimming referee misses it
- Treating "a referee might dislike non-EU" as unanswerable instead of giving EU its fair test
- Hiding a known limitation and hoping no specialist notices — they will
- Generic "reviewer 2" cynicism instead of mapping objections to this journal's actual subcultures

## Worked vignette (illustrative)

A CPT-based experiment expects two referees: a decision theorist and an EU loyalist. The theorist's objection — "your reference point is chosen to fit" — is pre-empted by fixing it to the status quo a priori and showing the fit is not improved by freeing it. The loyalist's objection — "risk-averse EU with pessimism does the same" — is met by a treatment that varies probabilities at fixed outcomes, producing the inverse-S weighting that EU cannot generate. Both defenses are promoted into the main text before submission.

## Output format

```text
【Journal】Journal of Risk and Uncertainty
【Skill】jru-referee-strategy
【Verdict】defensible / patch / concede
【Likely referees】<two types>
【Top objection】<one paragraph> → answered / addable / limitation
【Best defense location】main text [Y/N]
【Limitations stated】[Y/N]
【Source status】verified / 待核实 / not asserted
【Next skill】jru-submission
```
