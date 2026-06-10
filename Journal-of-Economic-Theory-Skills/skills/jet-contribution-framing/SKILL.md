---
name: jet-contribution-framing
description: Use when framing the contribution of a Journal of Economic Theory (JET) paper so its theoretical advance is unmistakable — lead with the theorem, state why the result matters for the relevant theory, and right-size the claim to exactly what the proof delivers. For JET's theory-first bar; it does not overclaim.
---

# Contribution Framing (jet-contribution-framing)

## When to trigger

- Writing the abstract and introduction of a JET theory paper
- A desk editor must see the theoretical contribution within the first page
- You need to make sure the claim does not exceed the proof

## What JET rewards

JET accepts a paper because it is a **rigorous, original theoretical contribution**. Framing must put
the **theorem first** and make its significance legible to the matching editor and two expert
referees. A JET introduction is not a story arc around data — it is a precise statement of *what is now
known that was not before*.

## The framing template

1. **The question, theoretically posed.** What property of mechanisms / equilibria / preferences /
   markets is at stake?
2. **The result, stated as a theorem.** One sentence the abstract can carry: "We characterize / prove
   that / show existence of ...". Because **abstract references must be written in full**, cite at most
   one or two anchor results there.
3. **Why it matters.** Which prior result it weakens an assumption of, generalizes, or overturns — the
   delta from jet-literature-positioning.
4. **What it does *not* claim.** Name the scope (finite types, specific domain) so referees do not read
   in a stronger claim than the proof supports.
5. **Subfield signal.** State the area (mechanism design, decision theory, matching, …) so routing
   reaches the right editor.

## Right-sizing the claim

- Distinguish **characterization** vs. **existence** vs. **comparative statics** — claim only the one(s)
  you proved.
- Avoid "general" / "robust" / "essentially" unless the theorem literally says so.
- If a result holds only under an extra condition, say it in the abstract, not a footnote.

## Referee-proof contribution sentence

Before finalizing, rewrite the main contribution in this syntax:

```text
Under [assumptions], we prove [result type] for [environment], which [weakens/generalizes/constructs]
[closest theorem] by [precise delta].
```

Every bracket should map to a theorem statement or a cited frontier result. If a bracket is rhetorical
rather than formal, the framing is ahead of the proof.

## Result-type framing matrix

Different JET result types demand different lead verbs and carry different overclaiming risks:

| Result type | Lead verb in abstract | What the intro must promise | Typical framing risk |
|---|---|---|---|
| Characterization | "We characterize ..." | the full set of mechanisms/preferences/equilibria satisfying the property | writing "if and only if" when only sufficiency is proved |
| Existence | "We prove existence of ..." | the conditions plus the route (fixed point, constructive, lattice) | implying uniqueness or computability the proof never delivers |
| Uniqueness / comparative statics | "We show the equilibrium is unique / monotone in ..." | the order structure doing the work | asserting comparative statics outside the proved parameter region |
| Impossibility | "No mechanism satisfying A1–A3 can ..." | the exact axiom set, with tightness examples per axiom | letting readers infer a stronger informal reading than the axioms support |
| Counterexample paper | "We construct an example showing ..." | why the example overturns a folk presumption | underselling — a decisive counterexample is a JET contribution in its own right |

## Worked vignette: framing a mechanism-design result

Hypothetical paper: with two maxmin bidders holding a finite set of priors, the revenue-maximizing
auction is a posted price. The framing pass:

- **Question, theoretically posed:** how does bidder ambiguity reshape optimal selling?
- **Theorem sentence:** "Under Assumptions 1–3 (maxmin bidders, finite prior set, independent
  values), we characterize the seller-optimal mechanism and show it is a posted price."
- **Why it matters:** it overturns the exclusion-at-the-margin logic of the Bayesian optimal auction
  once the common-prior assumption is dropped.
- **Scope guardrail:** two bidders, finite prior sets; does NOT claim the result for
  smooth-ambiguity preferences — say so in the abstract.
- **Subfield signal:** mechanism design *and* decision theory under ambiguity — name both, since
  JET routes by editor field.

## Calibration: how accepted JET introductions tend to run

- Introductions commonly run a few pages: the motivating economic question opens, an informal
  statement of the main theorem appears early, then positioning and a roadmap. Patterns vary by
  subfield — calibrate against recent JET issues in your area, and confirm against the journal's
  current author guidelines for any formal length rules.
- The abstract stays formal and short; the introduction carries the intuition.

## Anti-patterns

- An empirical-style narrative intro that buries the theorem
- Overclaiming generality the proof does not reach
- An abstract with a sweeping claim and a much narrower theorem in §3
- Selling motivation while leaving the actual statement vague

## Output format

```
【One-line theorem】<abstract sentence>
【Why it matters】weakens/generalizes/overturns <closest result>
【Scope guardrail】holds under <conditions>; does NOT claim <X>
【Subfield】<routing area>
【Next】jet-writing-style (polish) / jet-submission
```
