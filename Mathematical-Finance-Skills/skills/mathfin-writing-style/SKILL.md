---
name: mathfin-writing-style
description: Use when polishing a Mathematical Finance (Wiley) manuscript's theorem-first exposition — definitions, numbered assumptions, theorem statements, proof sketches, appendices, notation discipline for a stochastic-analysis readership, numerical-experiment prose, and the financial-modelling intuition that accompanies each formal result.
---

# Writing Style (mathfin-writing-style)

## When to trigger

- The proofs are correct but the paper is hard to read
- The introduction states results without financial modelling intuition
- Definitions, assumptions, theorem numbering, or appendix references are inconsistent

## Style principles

- **Define before use.** Probability space, filtration, admissible strategies,
  integrability, market model, and payoff objects must be explicit.
- **Number assumptions and results.** Reuse labels consistently.
- **State theorem scope precisely.** Hypotheses and conclusions should be visible
  without searching prose.
- **Separate intuition from proof.** Give financial meaning before technical proof,
  then keep the proof self-contained.
- **Use appendices deliberately.** Put long derivations there while keeping the
  main text focused on result, intuition, and modelling payoff.

## Theorem paragraph pattern

```text
Under Assumptions (A1)-(A3), Theorem 2.1 establishes [formal result]. In financial
terms, this means [pricing/hedging/risk/portfolio interpretation]. The proof
combines [main tools] and is given in [location].
```

## Proof hygiene

- Check local martingale versus true martingale claims.
- State integrability and measurability conditions.
- Do not cite a theorem without verifying its hypotheses.
- Avoid "straightforward" for load-bearing steps.
- Keep notation stable across the main text and appendix.

## Symbol conventions the readership expects

| Object | Conventional usage | Drift to avoid |
| --- | --- | --- |
| Filtration | (F_t) with the usual conditions stated once | switching between F_t and F(t) |
| Physical / pricing measure | P / Q (or Q^*) | reusing Q for a generic measure mid-paper |
| Brownian motion | W under P; W^Q after Girsanov | the same W under both measures without comment |
| Admissible strategies | A or A(x), x the initial wealth | "admissible" used before A is defined |
| Wealth / value process | X^pi or V | V doubling as value function and value process |
| Value function | v(t,x), lowercase | v and V swapped between sections |
| Stopping times | tau, ranging over a defined family T_{t,T} | tau ranging over an unspecified set |
| Generator | L (or L^a in control problems) | applying L to functions outside its stated domain |

## Proof-sketch scaffold

Before each long proof, give a three-to-five sentence sketch:

```text
The proof proceeds in three steps. Step 1 establishes [a priori estimate] under (A2), which
yields the uniform integrability needed later. Step 2 constructs the candidate [object] via
[tool: Snell envelope / dual problem / fixed point]; this is where the new idea, [one phrase],
enters. Step 3 verifies optimality and uniqueness by [verification argument]. Steps 1 and 3
are standard given Step 2 and are deferred to Appendix B.
```

The sketch tells a referee where the novelty lives and which parts may be verified quickly —
exactly the separation of new idea from routine verification that this journal's culture
prizes.

## Sentence-level habits for stochastic-analysis prose

- Quantify every "small", "sufficiently regular", or "for t large" with a displayed condition.
- Write "P-a.s." or "for Lebesgue-a.e. t" — never leave the null-set sense ambiguous.
- Prefer "By Theorem 2.3 of [X], whose hypotheses hold by (A1) and Lemma 3.2," to a bare
  citation.
- Keep proofs in one tense (present), and let displayed equations carry the algebra, not prose.

## Notation ledger

Before polishing prose, create a notation ledger with columns for symbol, object, first definition,
assumptions, theorem use, and appendix use. Use it to find:

- one symbol used for multiple objects;
- objects introduced only inside proofs but needed in theorem statements;
- filtrations, measures, admissible sets, or payoff spaces that change silently;
- assumptions cited in prose but absent from the theorem statement;
- appendix notation that no longer matches the main text after revision.

Mathematical Finance readers will forgive technical density more readily than notation drift. A clean
ledger also shortens referee response time because every objection can be tied to a labelled object.

## Output format

```text
[Section] intro / model / theorem / proof / numerics / appendix
[Main clarity issue] ...
[Formal precision fix] ...
[Financial intuition fix] ...
[Next step] mathfin-submission
```
