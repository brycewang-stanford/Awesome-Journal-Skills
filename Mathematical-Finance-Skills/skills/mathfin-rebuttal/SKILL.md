---
name: mathfin-rebuttal
description: Use when responding to a Mathematical Finance (Wiley) revise-and-resubmit — triages referee comments on theorem novelty, proof gaps, martingale and integrability conditions, assumption scope, counterexamples, exposition, numerical support, and financial-modelling relevance into a point-by-point letter plus aligned manuscript edits.
---

# R&R Rebuttal (mathfin-rebuttal)

## When to trigger

- A revision decision arrives from *Mathematical Finance*
- Referees identify proof gaps, unclear assumptions, missing novelty, or weak financial interpretation
- You need a point-by-point response letter and aligned manuscript edits

## Triage categories

1. **Proof correctness**: missing lemma, invalid theorem application, local/true
   martingale issue, integrability, measurability, boundary condition.
2. **Assumption scope**: too strong, too weak, unstated, or not financially interpretable.
3. **Novelty**: overlap with prior theorem, special-case concern, missing citation.
4. **Financial modelling relevance**: theorem correct but payoff unclear.
5. **Exposition**: notation, definitions, appendix navigation, numerical explanation.

## Response strategy

- Fix proof gaps directly; do not argue around them.
- When an assumption cannot be relaxed, explain why it is necessary and what it
  means financially.
- If novelty is questioned, compare theorem-by-theorem with the closest prior work.
- Add financial interpretation after formal statements, not only in the introduction.
- Move long derivations to appendices and point referees to exact page/line numbers.

## Objection-to-repair map

| Referee objection (typical phrasing) | Likely root cause | Repair that satisfies this venue |
| --- | --- | --- |
| "X is only a local martingale" | Missing uniform-integrability / Novikov-type condition | Add the integrability lemma; or weaken the conclusion to supermartingale and fix downstream claims |
| "Girsanov/Itô applied without checking hypotheses" | Cited theorem's conditions were not checked in your setting | Insert a verification step with explicit moment bounds, citing the precise theorem number |
| "The candidate strategy is not shown admissible" | Admissible set defined too loosely | Tighten the definition, prove membership, re-run the verification theorem |
| "This follows from [prior work] by a change of variables" | Novelty gap | Theorem-by-theorem comparison; isolate the hypothesis prior work cannot drop |
| "The proof of Lemma k is only sketched" | Routine step left informal | Write it out in the appendix; never answer with "standard" |
| "Where is the financial content?" | Payoff stated only in the abstract | Add interpretation remarks after each main theorem |

## When the referee exhibits a counterexample

Treat a counterexample as data about your hypotheses, not as an attack. First reproduce it and
check whether it satisfies your stated assumptions. If it does, the theorem is wrong as stated:
find the minimal additional hypothesis that excludes it, restate the result, and say plainly in
the letter that the referee found a genuine gap. If it does not, show precisely which labelled
assumption it violates and thank the referee for prompting a clarifying remark in the text.
Disputing a correct counterexample is the fastest route to rejection at a journal whose
referees verify arguments line by line.

## Worked vignette: defending a boundedness assumption

A referee asks why volatility is assumed bounded in a term-structure stability theorem and
suggests relaxing it. Response options, in descending strength: (1) relax it — prove the result
under linear growth plus a moment condition, if the localization survives; (2) keep it but show
necessity — exhibit an unbounded-volatility example where the conclusion fails; (3) keep it as
a convenience — state exactly which step uses it (a uniform estimate feeding a compactness
argument), explain why relaxation needs genuinely new tools, and record it as an explicit open
problem. Option 3 is acceptable at this venue only with the precise pointer to the step.

## Letter mechanics for a proofs journal

- Quote each comment verbatim, respond beneath it, and give page/equation/label coordinates
  for every change — referees re-verify proofs and need exact targets.
- Where a proof changed, summarize the new argument in two sentences in the letter so the
  referee can decide whether to re-read the full appendix.
- List any changes made beyond the referees' requests (renumbered assumptions, notation fixes)
  so nothing in the diff looks unexplained.
- Keep mathematical disagreement impersonal: counter with a lemma or a reference, never with
  an appeal to authority.

## Response paragraph pattern

```text
We thank the referee for identifying this issue. We have revised [theorem/lemma/
assumption] on page X and added [proof/detail] in Appendix Y. The revised argument
now verifies [condition], which is required for [external theorem/result]. We also
added a paragraph explaining the financial interpretation of this assumption.
```

## Output format

```text
[Decision type] major / minor
[Core mathematical issues] ...
[New proof work] ...
[Novelty clarification] ...
[Financial interpretation added] ...
[Next step] revise manuscript + response letter
```
