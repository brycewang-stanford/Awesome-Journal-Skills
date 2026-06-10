---
name: jet-rebuttal
description: Use when building the response letter for a Journal of Economic Theory (JET) revise-and-resubmit — address each single-anonymized referee's correctness, generality, and exposition points, supply corrected or strengthened proofs or counterexamples, and show exactly where the .tex was changed. For R&Rs; it does not invent referee taste.
---

# R&R Rebuttal (jet-rebuttal)

## When to trigger

- You received an R&R (or a reject-and-resubmit) from JET and must reply to referees
- A referee flagged a gap in a proof, an unstated assumption, or a missing case
- You need to position generalizations the editor and two referees asked for

## How JET R&Rs work

- Decisions come from the **editor** synthesizing **two-plus single-anonymized referee** reports.
  Because review is **single-blind**, referees may know your prior work — engage substance, not identity.
- For theory, the highest-stakes comments are about **correctness and scope**: an alleged hole in a
  proof, an assumption doing more work than acknowledged, a claimed "general" result that secretly
  needs finiteness/continuity/convexity, or a counterexample to a stated proposition.

## Response strategy

1. **Triage by severity.** Correctness issues first (a broken lemma sinks the paper), then generality
   and necessity-of-assumption questions, then exposition.
2. **For a proof gap:** either supply the corrected/complete argument or, if the result is false as
   stated, **narrow the claim** to what the proof supports and say so plainly. Never paper over a hole.
3. **For "is assumption X necessary?":** answer with a **counterexample** (X dropped → result fails) or
   a **generalization** (X weakened, result survives). Add the weaker statement as the new main result
   where credible.
4. **For exposition:** restate the theorem in the body, move heavy machinery to an appendix
   (`thm-restate`), and tighten notation.
5. **Show the diff.** Quote each comment, give a direct answer, and cite the **exact section / equation /
   theorem number** in the revised `.tex` that implements the change.

## Severity ladder for theory reports

| Report claim | Stakes | First move | Letter posture |
|---|---|---|---|
| "The proof of Lemma k has a gap" | paper-sinking if real | re-derive the step from scratch; do not pattern-match the old argument | corrected argument in full, or a narrowed claim |
| "Here is a counterexample to Proposition j" | decisive either way | verify it against every numbered assumption | if valid: thank, repair or narrow; if it violates an assumption: show which line fails |
| "Is Assumption A2 necessary?" | scope of the contribution | attempt the weakening; else construct the dropping-A2 example | a new Example or a generalized theorem |
| "This follows from [known theorem]" | originality | write out the claimed reduction or its failure point | the precise reason the known theorem does not apply |
| "Proofs are unreadable" | acceptance friction | restate theorems, add a lemma roadmap, offload to appendix | a table mapping moved material to new locations |

## When the referee's counterexample is right

1. **Verify first.** Check it satisfies all your numbered assumptions — many alleged
   counterexamples violate a regularity condition, and showing which line fails ends the issue.
2. **Locate the first false step.** If the example is valid, find the exact line of the proof it
   breaks; everything before that line survives.
3. **Repair or retreat.** Add the missing condition loudly (own the generality loss in the letter
   *and* the introduction), or restate the result at the strength the proof actually delivers.
4. **Credit it.** If the referee's example now appears in the paper, acknowledge the referee.

## Response-letter skeleton

```text
Editor summary (≤1 page, theorem-level):
  Theorem 1 unchanged; Proposition 2 narrowed (now requires A4 — see R1.3);
  new Example 3 shows A2 cannot be dropped (R2.1); Appendix C rewritten for readability.
Per referee, per point:
  [R1.3] "<verbatim comment>"
    → Type: correctness
    → Response: corrected the Lemma 2 step; the missing case is handled by new eq. (12)
    → Location: §4.2 and Appendix B.1; flagged in the attached latexdiff
Attachments: revised .tex, latexdiff PDF, this letter.
```

## Anti-patterns

- Defending a result you now know is false instead of narrowing it
- "We thank the referee" with no concrete change or location
- Adding assumptions silently to rescue a proof without flagging the reduced generality
- Re-disclosing or hiding generative-AI use inconsistently from the original submission

## Output format

```
【Referee N · Comment k】<verbatim>
  → Type: correctness | generality/necessity | exposition
  → Response: <corrected proof / counterexample / narrowed claim>
  → Change at: §x / Prop y / eq (z) in revised .tex
【Net effect】result strengthened / scope clarified / claim narrowed
```
