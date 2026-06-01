---
name: mathfin-rebuttal
description: Use when responding to a Mathematical Finance revise-and-resubmit, especially comments about theorem novelty, proof gaps, assumptions, exposition, numerical support, or financial-modelling relevance.
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
