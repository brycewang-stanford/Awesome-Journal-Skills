---
name: anmath-results-framing
description: Use when stating the main theorem(s) of a pure-mathematics manuscript precisely, establishing their significance, and positioning them against prior work for an Annals of Mathematics submission. Crafts statements and positioning; does not write the proof (see anmath-methods).
---

# Stating the Main Theorem(s) (anmath-results-framing)

## When to trigger

- Your main result is described in a paragraph but not stated as a precise theorem
- The introduction does not make the significance unmistakable in the first page
- Readers cannot tell which statement is the headline and which are corollaries
- You have not located your theorem relative to the prior state of the art

## How to state the main theorem

A reader should be able to find the precise main theorem on or near the first page and
understand exactly what is claimed without reading the proof.

1. **State it precisely and self-containedly.** Every hypothesis explicit; every object
   defined or referenced. No "under suitable conditions" hand-waving.
2. **Quantify the advance.** Make clear what is new: which hypothesis is removed, which
   bound is sharpened, which case is now covered, which conjecture is settled.
3. **Separate headline from consequences.** One (or few) Main Theorem(s); corollaries and
   special cases stated separately so the contribution is unambiguous.
4. **Give the sharpest true statement.** Do not under-claim out of caution or over-claim
   beyond what the proof delivers; the statement and the proof must match exactly.

## Framing shapes from verified Annals landmarks

Benchmark against the verified papers in `resources/exemplars/library.md`; each makes
its advance quantifiable in one sentence, in one of three shapes:

- **Settles a named conjecture** (Wiles 1995; Marques–Neves 2014): name the conjecture,
  state the theorem that closes it.
- **Breaks a quantitative barrier** (Zhang 2014): a modest-sounding bound whose point
  is that none existed — say exactly which barrier fell.
- **New method with reach** (Green–Tao 2008; Bhargava–Shankar 2015): the theorem is the
  headline, but the transferable technique is named too.

A result fitting none of these shapes should go back through anmath-scope-fit first —
framing cannot manufacture significance.

## Introduction architecture (Annals style)

| Element | Purpose |
|---------|---------|
| Problem and history | Why this question matters and what was known |
| Precise statement of Main Theorem | The headline, fully rigorous, early |
| What is new vs. prior work | Named comparison to the closest prior results |
| Consequences / corollaries | Why the result has reach |
| Method in one paragraph | A pointer to the proof idea (detail belongs to anmath-methods) |
| Organization of the paper | Section-by-section roadmap |

## Positioning against the literature

- Name the **closest prior results** and authors explicitly; state precisely what they
  proved and where your theorem goes beyond it (stronger hypothesis removed, sharper
  constant, new range, full generality).
- Engage carefully with **priority**: cite preprints/announcements you are aware of and
  state the relationship honestly. Claiming priority without engaging the record is a
  serious referee red flag.
- Do not rely on **unpublished or unverifiable** results for the core comparison; if a
  cited result is itself unpublished, say so and isolate your dependence on it.

## Micro-example: from vague paragraph to precise theorem

**Before:** "We prove strong new bounds for the discrepancy of such sequences under
mild conditions, improving earlier work."

**After:** "**Theorem 1.1.** *Let (x_n) satisfy (H1)–(H2). Then D_N(x) ≤ C(α) N^{−1/2}
log N for all N ≥ 2, where C(α) depends only on α.*" — plus one positioning sentence:
"This removes the smoothness hypothesis of [Prior, Theorem 2] and sharpens the exponent
from −1/3 to −1/2."

Named hypotheses, an explicit rate, stated constant dependence, a cited theorem
precisely exceeded — the Annals headline register.

## Checklist

- [ ] Main Theorem is stated precisely, with all hypotheses, near the first page
- [ ] The framing matches a landmark shape (conjecture settled / barrier broken / method with reach)
- [ ] It is clear which statement is the headline vs. corollaries
- [ ] The exact advance over prior work is quantified, not just asserted
- [ ] Closest prior results are named with authors and what they proved
- [ ] Priority relative to known preprints is engaged honestly
- [ ] The statement matches exactly what the proof delivers (no over/under-claim)
- [ ] MSC subject classification chosen to match the headline result

## Anti-patterns

- Burying the main theorem on page 8 after long preliminaries
- "We prove strong results about X" with no precise statement up front
- Claiming generality the proof does not actually establish
- Vague positioning ("improving earlier work") without naming the earlier work
- Asserting priority while ignoring a known competing announcement
- Listing five "main" theorems so the actual contribution is unclear

## Output format

```
【Main Theorem (precise)】...
【What is new vs. prior】removed-hypothesis / sharper-bound / settles-conjecture / ...
【Closest prior results】author (year): proved ...
【Corollaries / reach】...
【Priority note】no conflict / relationship to preprint X is ...
【MSC classes】primary ..., secondary ...
【Next step】anmath-methods (lay out the proof architecture)
```
