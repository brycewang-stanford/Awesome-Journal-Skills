---
name: aejmic-rebuttal
description: Use when drafting the response letter and revision plan after an American Economic Journal: Microeconomics (AEJ: Micro) R&R. Structures the reply to theory referees (correctness, generality, exposition) and editor; it does not re-derive the result (see aejmic-theory-model).
---

# R&R Rebuttal & Response Letter (aejmic-rebuttal)

## When to trigger

- An AEJ: Micro decision letter arrived with an R&R (minor or major)
- You have referee reports and need a response-letter strategy
- A referee disputes a proof, the generality, or the framing and you must decide concede vs. defend
- You are sequencing the revision so the most important changes land first

## How to respond to theory referees

AEJ: Micro referees are subject-matter experts who **verify proofs** and judge **generality and exposition**. The response letter must be precise, respectful, and point-by-point. Three recurring axes:

- **Correctness:** a disputed proof step. Either fix it (and show the corrected argument in the letter), or demonstrate the step is valid with the missing detail. Never wave it away.
- **Generality / robustness:** "does it extend to X?" Decide whether to (a) prove the extension, (b) add it to `aejmic-robustness` as a result, or (c) explain precisely why the boundary is where it is and add a remark. State the cost of each.
- **Exposition / scope:** "the mechanism is buried" or "the claim is too broad." Re-frame via `aejmic-writing-style` and bound the claim explicitly.

### Letter structure
- A short **cover note** to the editor summarizing the main changes and how the central concern was met.
- **Point-by-point** replies: quote the comment, state the change, point to the page/line and the new/updated proposition or proof.
- **Concede gracefully** where the referee is right; **defend with argument** (not assertion) where you disagree, and offer a compromise (a remark, a restricted claim) when full concession is wrong.
- Keep a **changelog** of every result that moved (new propositions, relabeled lemmas, added extensions).

### Triage the reports before drafting
Not all comments carry equal weight. Sort them:
- **Central (editor-flagged):** the concern the editor named as decisive — resolve it first and lead the cover note with it.
- **Correctness blockers:** any disputed proof or claim — must be fully closed, never deferred.
- **Generality requests:** decide per comment whether to prove, add a robustness result, or bound with a precise argument.
- **Exposition / framing:** usually cheap to grant; granting them buys goodwill for the points you defend.

### Reading the decision letter
- A **minor** R&R means the result stands; tighten and answer. A **major** R&R means at least one referee doubts the contribution or a proof — treat the central concern as the gate to acceptance.
- Distinguish what the **editor** requires (binding) from what a single referee merely **suggests** (negotiable). Address all, but prioritize by the editor's framing.

## Checklist

- [ ] Cover note to the editor: main changes + how the central concern was addressed
- [ ] Every referee comment answered point-by-point with a page/line pointer
- [ ] Disputed proof steps fixed or rigorously defended (no hand-waving)
- [ ] Each "does it extend?" met by a proof, a new robustness result, or a precise boundary argument
- [ ] Claims re-bounded where a referee found them too broad
- [ ] Concede where right; defend with argument where not; offer compromises
- [ ] Changelog of moved/added results kept for the editor and referees
- [ ] Replication package / proof appendix updated to match the revision

## Anti-patterns

- "We thank the referee and have addressed this" with no concrete change or pointer
- Defending a disputed proof step by restating it instead of completing it
- Adding every requested extension uncritically, bloating the paper (curate via `aejmic-robustness`)
- Conceding a correct result under pressure when a bounded claim was the right answer
- Letting the proof appendix or deposited code drift out of sync with the revised results

## Worked vignette (illustrative)

Referee 1 disputes the uniqueness claim; Referee 2 asks for a continuum extension; the editor wants the contribution sharpened. Strategy: (1) Correctness — uniqueness held only under a tie-breaking rule, so **restrict the claim** to "essentially unique" and prove it, conceding the over-statement. (2) Generality — the continuum extension survives, so **add it as Proposition 5** and cite it in the letter. (3) Scope — rewrite the intro to foreground the broad mechanism. The cover note tells the editor the central concern (uniqueness) is resolved by a precise, defensible restatement.

## Output format

```
【Decision】minor / major R&R
【Editor cover note】central concern + how met
【Point-by-point】each comment → change → page/line + result pointer
【Correctness】disputed steps fixed/defended? [Y/N]
【Generality】extend / new result / boundary argument — chosen per comment
【Concede vs. defend】log of each call
【Changelog + package sync】results that moved; appendix/code updated? [Y/N]
【Next step】resubmit via AEA system with the point-by-point response letter
```
