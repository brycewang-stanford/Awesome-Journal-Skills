---
name: restud-referee-strategy
description: Use when anticipating the referee pool and their likely objections for a The Review of Economic Studies (REStud) manuscript, and when pre-empting those objections in the paper before submission. Maps reviewers and hardens the paper against them; does not write the rebuttal (that is restud-rebuttal).
---

# REStud Referee Strategy (restud-referee-strategy)

## When to trigger

- Before submission, to pre-empt the objections a demanding referee will raise
- When choosing suggested / opposed referees in the submission form
- When deciding which robustness checks to include up front vs. hold in reserve
- When the design or model has a known soft spot you want to confront proactively

## How REStud refereeing works

REStud's official submission guidelines ask for author names and affiliations on the title page and do not describe blind review, so assume referees can see who you are while you cannot see them (see `restud-submission`). Papers are handled by editors drawn from the active frontier; the Joint Managing Editors (2026: Jan De Loecker, KU Leuven, IO/applied econometrics; Antonio Penta, UPF, micro theory / mechanism design; Jakub Steiner, Zurich/CERGE-EI, behavioral/information economics) span both theory and applied work, reflecting the journal's balanced identity — so anticipate either a theory-leaning or an applied-leaning reader depending on who handles you. REStud is also known for **demanding referees** and for **constructively developing strong papers across rounds**. Two implications:

1. The first report is rarely an accept; a strong paper typically earns an R&R with substantive requests. Plan the submission so the *first* report's requests are ones you can satisfy, not ones that kill the paper.
2. Referees expect state-of-the-art design (empirics) or complete, correct proofs (theory). The fastest path to rejection is a soft spot the referee can name in one sentence that you did not address.

## Mapping the referee pool

- **Identify the 3–5 most likely referees.** They are the inner-ring authors from `restud-literature-positioning` — the people whose work you are closest to. Assume the referee *is* the author of the nearest paper.
- **For each, predict the objection.** "This author will ask why we don't use their estimator / their data / their setting." Pre-empt it in the text.
- **Predict the methodological referee.** Beyond the topic expert, REStud often uses a methods-focused referee. For empirics, that means the modern-estimator and inference objections; for theory, the assumption-minimality and proof-completeness objections.

## Pre-empting, not hiding

- Address the single most plausible alternative explanation **in the main text**, not buried in an appendix.
- For the design's soft spot, include the diagnostic that confronts it (the placebo, the sensitivity bound, the alternative estimator) rather than hoping it goes unnoticed.
- Cite the likely referee's relevant work where genuinely relevant — not as flattery, but because their result is part of the positioning.

## Suggested / opposed referees

- **Suggested:** scholars who know the subfield, have relevant publications, and are not collaborators or advisors (conflicts disqualify them). Aim for genuine experts, not friends.
- **Opposed:** only with a real conflict (direct competitor with a working paper on the same question, a personal conflict). Over-listing opposed referees signals defensiveness.
- Verify the current submission system's referee-suggestion fields and limits on the journal's official page.

## Sequencing checks for the first round

Because REStud develops papers across rounds, structure the submission so the first report is survivable:

- **Front-load the design's hardest diagnostic.** Put the placebo / sensitivity bound / alternative estimator in the main text, so the referee sees you already did it.
- **Hold a reserve.** Keep one or two additional robustness exercises ready but not in the paper, so an R&R request can be answered with new evidence rather than a promise.
- **Anticipate the "scope" request.** Demanding referees often ask to extend the result (another setting, another mechanism, a generalization of the model). Decide in advance which extensions are feasible and which would turn it into a different paper.
- **Map theory and empirics consistency.** If the paper has both, the referee will check that the model's assumptions match the estimation sample — confirm this before they do.

## Checklist

- [ ] 3–5 likely referees identified from the inner-ring literature
- [ ] Predicted objection written for each, and pre-empted in the text
- [ ] Methods-referee objections (estimator / inference / proof-completeness) addressed
- [ ] Most plausible alternative explanation confronted in the main text
- [ ] Design soft spot has a diagnostic that addresses it
- [ ] Suggested referees are real experts, not collaborators
- [ ] Opposed referees limited to genuine conflicts

## Anti-patterns

- Submitting without asking "who referees this, and what will they want?"
- Hiding the design's soft spot and hoping the referee misses it (a demanding REStud referee will not)
- Suggesting friends as referees — editors discount obviously friendly suggestions
- Listing many opposed referees, which reads as defensiveness
- Treating the first report as a verdict rather than the start of a development process

## Output format

```
【LIKELY REFEREES】[author — predicted objection — pre-empted? where]
【METHODS-REFEREE RISKS】[estimator / inference / proof gaps]
【SOFT SPOT】<the one-sentence objection> — confronted in: <section>
【SUGGESTED REFEREES】[experts, non-conflicted]
【OPPOSED REFEREES】[genuine conflicts only, or "none"]
【NEXT SKILL】restud-submission
```
