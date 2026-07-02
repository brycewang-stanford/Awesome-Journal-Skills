---
name: prl-revision
description: Use when responding to Physical Review Letters referee reports or editor decisions — point-by-point reply, resubmission, and the APS appeal route. Structures the response and revision; does not redraft the science from scratch.
---

# PRL Revision (prl-revision)

## When to trigger

- One or more APS referee reports have arrived
- You received an editor decision (revise / reject / reject-with-appeal-option)
- You need to write a point-by-point response letter
- You are weighing resubmission versus appeal versus retargeting to a PR journal

## Read the decision before drafting

APS decisions vary: invitation to revise, rejection that invites resubmission, or rejection on importance/breadth. Match your strategy to the decision:

| Decision                                              | Strategy                                                       |
|-------------------------------------------------------|----------------------------------------------------------------|
| Revise / minor                                        | Address every point; revise manuscript; resubmit promptly      |
| Reject but resubmission encouraged                    | Substantive revision + a response showing what changed         |
| Reject on importance/breadth (science sound)          | Decide: strengthen breadth case + appeal, or retarget PR journal|
| Reject on correctness                                 | Fix the science or retarget; do not appeal a valid technical flaw|

## Point-by-point response structure

For **each** referee comment:

1. **Quote** the comment verbatim (or faithfully paraphrase).
2. **Respond** — agree and act, or disagree with evidence.
3. **Point to the change** — name the exact location ("revised Sec. ..., new Fig. S3, added sentence in para ...").

Conventions that work with APS referees:

- Be **courteous and specific**; never dismissive, even with a hostile report.
- Quote new manuscript text in the reply so the referee sees the change without hunting.
- Mark changes in the manuscript (color or a marked-up version) per current APS practice.
- If you disagree, win on **evidence and physics**, not tone — add a control, a calculation, or a citation.
- Respect the length limit: revisions that add material must re-balance via `prl-length-management` and `prl-supplementary`.

## Worked micro-example: a response entry

**Referee:** "The claimed effect could arise from heating."

**Weak reply:** "We are confident heating plays no role."

**Strong reply:** "We agree this must be excluded. We have added a power-dependence measurement (new Fig. S4): the amplitude is unchanged over a decade of drive power. Sec. III now states: 'The amplitude is power-independent, excluding a thermal origin (SM Sec. S4).'"

The strong reply concedes the concern's legitimacy, answers with a *measurement* rather than confidence, and quotes the new sentence with its location — the pattern for every entry.

## Resubmission packaging

A PRL resubmission is judged as a package:

- **Summary of changes** — lead with the revision answering the decision letter's central concern.
- **One self-contained reply per referee** — do not make Referee B hunt through answers to Referee A.
- **Length re-certification** — added controls count against the deductible budget; state that the revised Letter still passes, or what moved to SM to compensate.
- **Timing** — resubmit complete rather than fast; a second round typically returns to the same referees.

## Handling the breadth/importance rejection specifically

This is the signature PRL outcome. Options:

- **Sharpen, don't inflate.** Make the broad-interest case concrete (`prl-results-framing`, `prl-cover-letter`) — a real cross-field consequence, not louder adjectives.
- **Appeal** through the defined APS route only if you have a substantive argument the editor/referee missed; appeals are not for re-arguing taste.
- **Retarget** to Phys. Rev. A–E / PR Research if the breadth case is genuinely weak — often the faster path to publication (`prl-scope-fit`).

## Checklist

- [ ] Every referee point has an explicit response
- [ ] Each response names the exact manuscript change location
- [ ] New text is quoted in the reply for the referee's convenience
- [ ] Disagreements are backed by evidence/physics, not tone
- [ ] A marked-up / change-highlighted manuscript is prepared
- [ ] Added material is re-balanced against the length limit
- [ ] The Letter still stands alone after revision
- [ ] If appealing, the appeal raises a substantive missed point, not taste
- [ ] If retargeting, the right PR journal is chosen via prl-scope-fit

## Anti-patterns

- A defensive or curt tone toward a difficult referee
- Claiming to have addressed a point without actually changing the text
- Adding rebuttal material that pushes the Letter over the length limit
- Appealing a sound technical rejection instead of fixing the science
- Re-arguing breadth with adjectives instead of a concrete consequence
- Letting revisions make the Letter depend on the SM

## Output format

```
【Decision type】revise / resubmit-encouraged / breadth-reject / correctness-reject
【Point-by-point】N comments — all addressed with locations?  yes / list gaps
【Tone】courteous + evidence-based?  yes / fix
【Length re-balanced after additions】yes / fix
【Stands alone after revision】yes / fix
【Path】resubmit / appeal (substantive?) / retarget via prl-scope-fit
【Next】prl-submission (resubmit) or prl-scope-fit (retarget)
```

> Decision categories, appeal procedures, and markup expectations are durable in spirit; verify the current process on the official APS / PRL author page.
