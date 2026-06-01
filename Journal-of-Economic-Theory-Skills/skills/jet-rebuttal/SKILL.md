---
name: jet-rebuttal
description: Build the response letter for a Journal of Economic Theory (JET) revise-and-resubmit — address each single-anonymized referee's correctness, generality, and exposition points, supply corrected or strengthened proofs, and show exactly where the .tex was changed. For R&Rs; it does not invent referee taste.
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
