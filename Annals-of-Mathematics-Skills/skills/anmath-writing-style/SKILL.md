---
name: anmath-writing-style
description: Use when polishing the prose and rigor of a pure-mathematics manuscript for Annals of Mathematics — eliminating gaps, removing "clearly"/"it is easy to see", precise quantifiers, and consistent mathematical English. Late-stage polish; run only after the proof and architecture are fixed.
---

# Writing Style and Rigor (anmath-writing-style)

## When to trigger

- The proof is complete and you are tightening the prose
- You wrote "clearly", "obviously", "it is easy to see", or "trivially" and are not certain
- Quantifiers, hypotheses, or "the constant" are stated loosely
- The English is uneven or the register drifts between sections

## The cardinal rule: no hidden gaps

At Annals, an expert referee verifies the proof in detail. A logical gap — especially one
hidden behind softening words — is fatal. Treat every "clearly" as a debt to be paid or
deleted.

| Phrase | What to do |
|--------|-----------|
| "It is easy to see that ..." | Either show it in one line, or delete the claim if truly immediate |
| "Clearly / obviously ..." | Replace with the actual one-line reason, or cite the lemma |
| "A standard argument shows ..." | Name the standard argument and cite it precisely |
| "By a similar argument ..." | State exactly which prior argument and what changes |
| "It can be shown that ..." | Show it, or move it to a lemma with a proof |
| "Modulo routine modifications ..." | Spell out the modifications or do them |

If a step really is immediate, a single clause giving the reason is better than "clearly".

## Worked micro-example: paying the "clearly" debt

**Before:**

> Clearly f is uniformly continuous on K, so by a standard compactness argument the
> bound (3.2) holds with a constant independent of ε.

**After:**

> Since K is compact and f is continuous, f is uniformly continuous on K. Covering K by
> finitely many δ-balls with δ as in (3.1) and taking the maximum of the local bounds
> yields (3.2) with C = C(K, f) independent of ε.

Two debts are paid for one extra line: "clearly" becomes the one-clause reason, and
"a standard compactness argument" becomes the actual argument with the constant's
dependence recorded.

## Precision in statements and prose

- **Quantifiers explicit.** "For all ε > 0 there exists δ > 0" — never leave the order of
  quantifiers to the reader. State dependence of constants (e.g. "C depends only on n").
- **Hypotheses carried, not assumed.** Each lemma states its own hypotheses; do not rely
  on context the reader has to reconstruct.
- **One name per object.** Do not let a symbol mean two things; do not give one object two
  names across sections.
- **Define before use.** No symbol or term appears before it is introduced.
- **Match statement to proof.** The theorem proves exactly what it states — no more, no less.

## Mathematical English

- Consistent tense and register; complete sentences around displayed equations.
- "We" for authorial voice is conventional and fine; keep it consistent.
- Punctuate display equations as parts of sentences.
- Use `\eqref`/`\cref` so references stay correct after edits.
- Light language polish is welcome for non-native authors, but never at the cost of
  precision.

## How the Annals referee reads your prose

Review at this journal is single-blind expert verification, frequently stretching past
a year. Assume every softening word will be tested: the referee's default at "it is
easy to see" is to try to see it, and each failure erodes trust in the steps they
cannot check. A first "clearly" that conceals a subtlety invites a report that
re-derives everything and finds the real gap you missed.

## Checklist

- [ ] Every "clearly"/"easy to see"/"obviously" is either justified in a clause or removed
- [ ] Every softening word has been tested the way a verifying referee would test it
- [ ] "Standard"/"similar" arguments are named and cited precisely
- [ ] Quantifier order is explicit everywhere it matters
- [ ] Constant dependence is stated (what each constant depends on)
- [ ] Each lemma carries its own hypotheses
- [ ] No symbol is overloaded; nothing is used before definition
- [ ] The theorem statement matches exactly what the proof establishes
- [ ] Displayed equations are punctuated and referenced consistently

## Anti-patterns

- "It is easy to see" guarding a step that is not, in fact, easy — the classic fatal gap
- "By a similar argument" when the argument is not actually similar
- Loose quantifiers that hide an order-of-quantifiers error
- Constants introduced without saying what they depend on
- A lemma whose hypotheses live only in the surrounding prose
- Polishing language while a logical gap remains open

## Output format

```
【"clearly"/"easy to see" instances】N found → resolved: justified / removed / made-lemma
【Standard/similar arguments】named & cited: ...
【Quantifier / constant fixes】...
【Statement–proof match】confirmed / fix: ...
【Remaining open gaps】none / list (BLOCKER — return to anmath-methods)
【Next step】anmath-length-management
```
