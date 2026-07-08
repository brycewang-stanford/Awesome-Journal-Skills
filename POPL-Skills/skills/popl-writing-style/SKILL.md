---
name: popl-writing-style
description: Use when drafting or revising POPL prose — building the informal-to-formal ramp from a motivating program to definitions to a sharply stated main theorem, keeping notation coherent across 25 pages of text, writing proof sketches that name the hard case, and framing significance as an idea other PL researchers can reuse.
---

# POPL Writing Style

A POPL paper convinces twice: informally, that the problem is real and the idea
natural; formally, that the theorems are exactly true. The craft is the ramp between
the two. The 25-pages-of-text budget (POPL 2027 call, read 2026-07-08) is generous
compared with old conference caps — the failure mode is not compression but
*unmotivated formalism*.

## The informal-to-formal ramp

1. **Open with a program, not a framework.** Page 1 should show concrete code or a
   concrete derivation that misbehaves — the phenomenon your formalism explains.
2. **State the contribution as a sharp claim.** "We prove type soundness for λ_X
   with feature Y, the first such result without assumption Z" beats any paragraph
   of positioning.
3. **Walk the example through the machinery** before generalizing: the reader should
   predict each definition because the example demanded it.
4. **Main theorem by the end of the overview section**, at least informally: what is
   proved, under what assumptions, and what is *not* claimed.
5. Only then the full calculus — and every rule shown in the body should be a rule
   the text actually discusses (`popl-supplementary` takes the rest).

## Notation is load-bearing

| Symptom | Cost at review | Repair |
|---|---|---|
| Same meta-variable for terms and types | Reviewers misread a rule, file a soundness doubt | One notation table, enforced by grep |
| Definitions used pages before they appear | "Paper is unreadable" reviews | Definition-before-use audit on every draft |
| Ambient hypotheses ("we assume all contexts well-formed" once, on p. 6) | Counterexamples that your hidden assumption excludes | Number assumptions; cite by number in each theorem |
| Overloaded ⊢ with no annotation | Rule-reading errors in the response phase | Subscript every judgment form |

## Proof sketches that earn trust

A body sketch is not a shortened proof; it is a *risk disclosure*. Name the induction
measure, name the case that fails naively, and say what saves it:

```text
Proof sketch (Thm 4.1). By induction on the typing derivation. The interesting
case is T-Close: the naive IH is too weak because the closure captures a
context extension. We strengthen the statement to quantify over all well-formed
extensions (Lem 4.3); the remaining cases are routine and mechanized (Sound.v).
```

A reviewer who reads that sketch knows you met the hard case, and the appendix or
mechanization confirms it.

## Significance, POPL-flavored

- Frame the payoff as **transferable**: "the proof method applies to any calculus
  with property P," "the logic is parametric in the memory model."
- Do not oversell breadth a theorem does not have; scoping sentences ("we treat the
  sequential fragment; concurrency is future work") pre-empt the significance
  reviewer rather than arming them.
- Avoid empirical-style adjectives ("fast," "practical") unless `popl-experiments`
  backs them; at this venue an unsupported "practical" is an invited objection.
- Related-work sentences state technical deltas, not lists (`popl-related-work`).

## Output format

```text
[Ramp audit] <page where a concrete example appears / where the main claim is first stated>
[Notation risks] <overloads, forward references, ambient assumptions>
[Sketch quality] <per main theorem: hard case named? measure named?>
[Overclaim scan] <sentences claiming more than the theorems>
[Cut list] <formal material in the body that no text discusses>
```
