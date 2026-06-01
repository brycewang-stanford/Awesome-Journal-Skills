---
name: ectheory-contribution-framing
description: Use to frame the central result of an Econometric Theory (ET) paper so its generality and importance are legible — stating the theorem and its scope up front, choosing Article vs Miscellanea framing, and matching the new editorial program's themed directions.
---

# Contribution Framing (ectheory-contribution-framing)

## When to trigger

- The result is proved but the introduction buries what is actually new and general
- You cannot state the main theorem and its scope in two or three sentences
- Deciding how to frame for a full **Article** (multiple contributions) vs a **Miscellanea** (one or two)
- You want to align with ET's Jan-2026 themed directions or the discussion-paper format

## How to frame a theory contribution for ET

ET readers reward **a clearly stated, general result whose importance is obvious from the
statement**. Frame the contribution in this order:

1. **The problem in econometrics** the result speaks to (an inference problem, a limit gap, a
   robustness failure), stated for a theorist who will recognize it instantly.
2. **The theorem in words**, then the scope: under what assumptions, in what environment
   (stationary/nonstationary, fixed/growing dimension), with what limiting behavior.
3. **The generality delta** — what special cases collapse to known results, and what is genuinely new.
4. **Consequences** — what becomes provable, computable, or robust because of this result; how it
   changes practice or further theory.

For an **Article**, the frame should foreground multiple contributions and the proof program; for a
**Miscellanea**, foreground the single sharp innovation, stated and proved concisely (~15 pages).

## Aligning with the current editorial program

From January 2026, ET (Editors-in-Chief Guggenberger, Su, Sun) emphasizes **invited papers with
discussions** and **themed special issues** — econometric theory for ML/AI, causal inference under
complex interference, robust inference and partial identification, high-dimensional and non-standard
environments, network/spatial econometrics. If your result speaks to one of these, frame the
contribution so that fit is explicit. The biennial **Peter C. B. Phillips Award** (best paper by a
scholar within 6 years of their first PhD) is a recognition program, not a submission track.

## Checklist

- [ ] Main theorem stated in words plus its scope, in the first page or two
- [ ] Generality delta vs known special cases made explicit
- [ ] Consequences for theory/practice stated, not just the formal result
- [ ] Article vs Miscellanea framing matched to the number of contributions
- [ ] Themed-direction fit articulated where applicable
- [ ] No overclaim beyond what the assumptions deliver (see ectheory-identification-strategy)

## Anti-patterns

- An introduction that recounts the proof steps before stating what is proved
- Hiding the main result on page 8 behind setup and notation
- Framing a single corollary as if it carried a full Article
- Claiming broad generality the theorem's assumptions do not support
- Treating the invited ET Interview or the Phillips Award as a submission target

## Output format

```
【Problem】the econometric inference/limit problem addressed
【Theorem in words】+ scope (assumptions, environment, limit)
【Generality delta】new vs known special cases
【Consequences】what becomes provable/robust/computable
【Frame】Article (multi-contribution) / Miscellanea (one or two)
【Themed fit】direction (if any)
【Next step】ectheory-data-analysis
```
