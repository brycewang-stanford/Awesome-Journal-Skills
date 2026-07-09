---
name: pods-author-response
description: Use when drafting ACM PODS author responses, covering the short ~48-hour double-anonymous rebuttal that corrects misreadings of proofs and definitions, and — distinctively — the shepherded revision cover letter that maps every required item to a concrete change in the resubmitted paper and survives the shepherd's second read.
---

# PODS Author Response

Use this after PODS reviews are released. PODS has **two distinct speaking turns**, and conflating
them is a common mistake: a short **rebuttal** (about 48 hours, a few thousand characters) right after
reviews, and — if you receive a **revision** decision — a **revision cover letter** accompanying a
resubmitted paper that a **shepherd** re-reads. Both stay double-anonymous: do not reveal authors,
affiliations, or a named system, even to strengthen a point.

## Triage (both turns)

- Answer what affects correctness first: a claimed error in a proof, an unstated assumption, a
  mismatch between an upper and a lower bound, or an out-of-scope objection.
- Distinguish a **misreading** (the reviewer misunderstood a definition or missed an existing appendix
  proof — fixable now, in the rebuttal) from a **real gap** (a step that genuinely needs to be written
  — fixable only in the revision).
- Keep every word anonymous: no institution, no funder, no real system name, no "our earlier work"
  phrased in the first person.

## Turn 1 — the 48-hour rebuttal

Short and correctness-focused. The rebuttal exists to **clarify misunderstandings and factual errors
via pointers to the submitted paper** — not to present new mathematics.

- Point to the exact definition, lemma, or appendix proof the reviewer overlooked ("the proof the
  reviewer requests is already in Appendix B, Lemma 7").
- Concede a genuine error plainly and state whether it is fixable in a revision.
- Do **not** paste a new proof the reviewers cannot verify in 48 hours; promising an unwritten proof
  does not move a theory review — it flags the gap.

## Turn 2 — the revision cover letter (the distinctive PODS move)

A revision (minor or major) is a genuine shepherded second round. The cover letter is a **change
ledger**: for every required item, either make the change and show exactly where, or explain precisely
why it is unnecessary — and satisfy the shepherd.

```text
[R1.1] Required: "the complexity bound in Thm 3 is not justified"
       -> Action: DONE  | added the full accounting in §4.2 and the deferred steps in Appendix B
       -> Where: §4.2 (para 2), Appendix B (Lemma 7, revised)
[R1.2] Required: "state the assumption the lower bound rests on"
       -> Action: DONE  | Thm 4 now labeled as conditional on OMv; stated at point of use (§5)
[R2.1] Suggested: "extend the dichotomy to self-joins"
       -> Action: DECLINED (with reason) | self-joins need a different reduction; out of scope for the
          revision window, now stated as an explicit open problem (§7) rather than implied
```

The rule that turns a revision into an acceptance: **address every required item.** An item neither
done nor explicitly and defensibly declined is what the shepherd's read punishes.

## Reviewer pushback patterns

| Pushback | What it signals | PODS-ready response |
|---|---|---|
| "The proof of Thm X has a gap" | Correctness doubt | Fix the step in the revision and show it; if it is a misreading, point to the existing proof in the rebuttal |
| "The lower bound does not match the upper bound" | Optimality unproven | Close the gap, or scope the optimality claim to the model actually proved |
| "This assumption is hidden/unstated" | Rigor gap | Label the conditional result at its point of use; state the assumption explicitly |
| "The model trivializes the result" | Modeling objection | Defend the model as realistic, or adjust it and re-derive; do not ignore |
| "Overlaps prior result Y" | Novelty/delta doubt | Sharpen the theorem-level delta; add the missing comparison of results |

## Anonymity in the response (easy to slip)

- Refer to your own prior work in the third person, as in the paper.
- Describe revisions without linking to an identifying arXiv preprint or homepage; reference the
  in-PDF appendix location instead.
- Do not thank a named collaborator, advisor, or funder inside the rebuttal or cover letter.

## Calibration

- Respond to the criterion the reviewer raised (correctness, tightness, modeling, novelty), not the one
  you would rather defend.
- Length and format norms for both turns vary by cycle; confirm the current instructions before sending.
- The shepherd decides the revised paper; make the **paper**, not the letter, carry the corrected
  mathematics.

## Output format

```text
[Turn] 48-hour rebuttal / revision cover letter
[Priority issue] <reviewer concern>
[Decision dimension] correctness / tightness / modeling / significance / clarity
[Change ledger] <required item -> DONE/PARTIAL/DECLINED + where in paper/appendix>
[Anonymity check] <no identity leak in the response: passed/issues>
```
