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
- First submission can use any complete, consistent reference format; JET's proof-stage style is
  **name-year / author-year**, so `elsarticle-harv` is the safest LaTeX default.

## Theorem-delta table

Build a private table before writing related work:

| Closest theorem | Assumptions | Object/result | Your delta | Where proved |
|---|---|---|---|---|
| Paper A, theorem X | finite types, single crossing, etc. | existence/characterization/bound | weaker/general/new constructive result | Theorem 1 / Proposition 2 |

Only the strongest two or three rows belong in the manuscript. The table prevents vague "we extend"
language and makes overclaiming visible before a referee catches it.

## Subfield frontier maps

The comparison set differs by JET area; find the closest theorem inside the right lineage, name the
lineage in one clause, then jump straight to the single nearest result:

- **Mechanism design / auctions:** the Myerson optimal-auction and implementation lineage; typical
  deltas weaken the common prior, risk neutrality, or transferable utility.
- **Matching / market design:** the Gale–Shapley stability and Kelso–Crawford substitutes line;
  deltas relax substitutability or add contracts, constraints, or distributional objectives.
- **Decision theory / ambiguity:** Anscombe–Aumann-based axiomatizations (maxmin, variational,
  smooth ambiguity); deltas trade one axiom for a behaviorally weaker one.
- **Information design / persuasion:** the Bayesian-persuasion concavification line; deltas add
  senders, dynamics, or robustness to the receiver's beliefs.
- **Repeated games / dynamic contracts:** folk-theorem and recursive-contract traditions; deltas
  alter monitoring, commitment, or the discounting structure.

## Positioning-paragraph skeleton

```text
The closest result is [Author (Year), Theorem k], which proves [object] under [assumption set S].
Our Theorem 1 [weakens S to S' / covers the general (non-quasi-linear / infinite-type) case /
characterizes an object their analysis leaves open]. The techniques also differ: their argument
relies on [tool]; ours requires [new tool] because [what breaks under the weaker assumptions].
Relative to the applied literature on [topic], our contribution is the theorem itself, not a
new application of existing results.
```

## Vignette: placing an information-design result

A hypothetical paper characterizes optimal disclosure when the receiver is maxmin. Two candidate
anchors compete: the standard persuasion concavification theorem (delta: receiver ambiguity breaks
Bayesian updating, so the sender's value is no longer a concavification) and the robust-mechanism
literature (delta: the designer commits to information rather than transfers). Write both rows in
the theorem-delta table, then lead the related-work paragraph with the anchor whose **assumptions
you actually weaken** — the other becomes one supporting sentence, not a co-headline.

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
