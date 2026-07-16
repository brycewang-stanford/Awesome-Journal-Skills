---
name: ngeo-revision
description: Use when responding to Nature Geoscience referee reports or editor decisions — point-by-point reply, resubmission, and the Nature Portfolio appeal route. Structures the response and revision; does not redraft the science from scratch.
---

# Nature Geoscience Revision (ngeo-revision)

## When to trigger

- One or more Nature Geoscience referee reports have arrived
- You received an editor decision (revise / reject / reject-with-appeal-option / editorially rejected before review)
- You need to write a point-by-point response to referees
- You are weighing revision versus appeal versus retargeting to a community journal or *Communications Earth & Environment*

## Read the decision before drafting

Nature Portfolio decisions vary; match your strategy to the decision:

| Decision                                                | Strategy                                                          |
|---------------------------------------------------------|-------------------------------------------------------------------|
| Revise (major/minor)                                    | Address every referee point; revise; resubmit with response       |
| Reject but resubmission invited                         | Substantive new work/analysis + a response showing what changed   |
| Editorial reject before review (interest)               | Decide: strengthen breadth case + appeal, or retarget             |
| Reject after review on significance (science sound)     | Sharpen the broad-interest/mechanism case, appeal, or retarget    |
| Reject on a technical flaw                              | Fix the science or retarget; do not appeal a valid flaw           |

## Point-by-point response structure

For **each** referee comment:

1. **Quote** the comment verbatim (or faithfully paraphrase).
2. **Respond** — agree and act, or disagree with evidence.
3. **Point to the change** — name the exact location ("revised Methods subsection ..., new Fig. 3, new Supplementary Fig. S5, added sentence in para ...").

Conventions that work with Nature Portfolio referees:

- Be **courteous and specific**; never dismissive, even with a hostile report.
- Quote new manuscript text in the reply so the referee sees the change without hunting.
- Provide a **marked-up manuscript** alongside a clean version per current Nature practice.
- If you disagree, win on **evidence and Earth-system reasoning** — add an analysis, a validation, a dataset, or a citation, not tone.
- Respect the container: added material must re-balance via `ngeo-length-management` (main text ≤ ~3,000 words; extras to Methods/SI).
- Re-check data/code availability and the Reporting Summary if analyses changed.

## Worked micro-example: a response entry

**Referee:** "The circulation inference could reflect the choice of age model rather than a real lead–lag."

**Weak reply:** "We are confident the age model is not driving the result."

**Strong reply:** "We agree this must be excluded. We repeated the analysis under three alternative age models (new Supplementary Fig. S5 and Supplementary Table S3): the X ± Y-year lead is preserved in all cases. The Methods 'Age model' subsection now states this, and the main text adds: 'The lead is robust to the choice of age model (Methods; Supplementary Fig. S5).'"

The strong reply concedes the concern, answers with a *repeated analysis with uncertainty*, and quotes the new sentence with its location — the pattern for every entry.

## Resubmission packaging

A Nature Geoscience resubmission is judged as a package:

- **Summary of changes** — lead with the revision answering the editor's and referees' central concern (usually significance/breadth or grounding).
- **One self-contained reply per referee** — do not make Referee 2 hunt through answers to Referee 1.
- **Container re-certification** — added analyses count against the main-text limit and display-item ceiling; state that the revised Article still fits, or what moved to Methods/SI.
- **Availability + Reporting Summary refresh** — update data/code statements and the Reporting Summary for any new data or code.
- **Timing** — resubmit complete rather than fast; a revised manuscript typically returns to the same referees.

## Handling the interest/significance rejection specifically

This is the signature Nature Geoscience outcome. Options:

- **Sharpen, don't inflate.** Make the broad-interest case concrete (`ngeo-results-framing`, `ngeo-cover-letter`) — a real cross-field consequence and firmer grounding, not louder adjectives.
- **Appeal** through the Nature Portfolio appeal route only if you have a substantive point the editor/referee missed; appeals are slow and are not for re-arguing taste.
- **Retarget** to a community journal or *Communications Earth & Environment* / *Nature Communications* if the breadth case is genuinely weak — often the faster path to publication (`ngeo-scope-fit`).

## Checklist

- [ ] Every referee point has an explicit response
- [ ] Each response names the exact manuscript change location
- [ ] New text is quoted in the reply for the referee's convenience
- [ ] Disagreements are backed by evidence/Earth-system reasoning, not tone
- [ ] A marked-up and a clean manuscript are prepared
- [ ] Added material is re-balanced against the word/display-item limits
- [ ] Data/code availability and Reporting Summary updated for new analyses
- [ ] The main text still stands alone after revision
- [ ] If appealing, the appeal raises a substantive missed point, not taste
- [ ] If retargeting, the right venue is chosen via ngeo-scope-fit

## Anti-patterns

- A defensive or curt tone toward a difficult referee
- Claiming to have addressed a point without actually changing the text
- Adding rebuttal material that pushes the Article over the word/display-item limits
- Appealing a sound technical rejection instead of fixing the science
- Re-arguing breadth with adjectives instead of a concrete consequence and firmer grounding
- Letting revisions make the main text depend on the SI

## Output format

```
【Decision type】revise / resubmit-invited / interest-reject / technical-reject
【Point-by-point】N comments — all addressed with locations?  yes / list gaps
【Tone】courteous + evidence-based?  yes / fix
【Container re-balanced after additions】yes / fix
【Availability + Reporting Summary refreshed】yes / n/a
【Stands alone after revision】yes / fix
【Path】resubmit / appeal (substantive?) / retarget via ngeo-scope-fit
【Next】ngeo-submission (resubmit) or ngeo-scope-fit (retarget)
```

> Decision categories, appeal procedures, and markup expectations are durable in spirit; verify the current process on the official Nature Geoscience / Nature Portfolio author pages (Checked: 2026-07-16).
