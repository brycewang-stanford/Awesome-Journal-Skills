---
name: jet-literature-positioning
description: Use when staking a Journal of Economic Theory (JET) contribution against the theory frontier — show precisely which assumption is weakened, which result is generalized, or which new phenomenon is characterized relative to the closest existing theorems. Positions the result; it is not a standalone survey.
---

# Literature Positioning (jet-literature-positioning)

## When to trigger

- Writing the related-work paragraph(s) for a JET theory paper
- A referee or editor may ask "how is this different from [closest existing theorem]?"
- You need to defend originality at the desk screen

## How JET wants the literature handled

JET spans general theory, so referees are expert in the **nearest existing results**, not a broad
empirical literature. Positioning is **theorem-relative**, not topic-relative. For each closest paper,
state the **delta in one of these precise forms**:

- **Weaker assumptions:** "X obtains the result under [strong condition]; we obtain it dropping/weakening
  it to [weaker condition]."
- **Greater generality:** "their characterization holds for [finite / quasi-linear / single-crossing]
  environments; ours covers [the general case]."
- **New object:** "no prior result characterizes [the equilibrium set / optimal mechanism / preference
  domain] in this environment; Theorem 1 does."
- **Tighter / constructive:** "existence was known; we give the [closed form / sharp bound / algorithm]."

## Reference-handling rules (JET-specific)

- **References cited in the abstract must be written out in full** — so cite sparingly there.
- **Keep unpublished results and personal communications out of the reference list**; lean on published
  theorems as the comparison set.
- Use the Elsevier reference style (`elsarticle-harv` name-year or `elsarticle-num`; the required one is
  **待核实** — confirm in the live guide).

## Theorem-delta table

Build a private table before writing related work:

| Closest theorem | Assumptions | Object/result | Your delta | Where proved |
|---|---|---|---|---|
| Paper A, theorem X | finite types, single crossing, etc. | existence/characterization/bound | weaker/general/new constructive result | Theorem 1 / Proposition 2 |

Only the strongest two or three rows belong in the manuscript. The table prevents vague "we extend"
language and makes overclaiming visible before a referee catches it.

## Anti-patterns

- A multi-page survey that never states *your* delta against the single closest theorem
- "We contribute to the literature on X" with no assumption- or generality-level comparison
- Citing working papers as the frontier when a published theorem already settles the comparison
- Vague novelty ("we extend the model") instead of naming the relaxed assumption

## Output format

```
【Closest result】<author, year, the theorem>
【Our delta】weaker assumption | greater generality | new object | tighter/constructive
【Stated as】"<one-sentence positioning to put in the intro>"
【Abstract cites】kept minimal + written in full? [Y/N]
【Next】jet-identification-strategy (assumptions & proof) / jet-contribution-framing
```
