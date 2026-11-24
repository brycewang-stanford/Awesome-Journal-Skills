---
name: jpe-rebuttal
description: Use when a Journal of Political Economy (JPE) decision letter (R&R or reject-with-encouragement) has arrived and you need to draft the response-to-referees letter and revision plan. Structures the response and the diff; it does not redo the analysis (route back to jpe-identification / jpe-theory-model / jpe-robustness first).
---

# R&R Response & Rebuttal (jpe-rebuttal)

## When to trigger

- A JPE R&R (or reject-with-encouragement-to-resubmit) letter has arrived
- You have referee reports and need a point-by-point response plan
- You are deciding which requests to implement, which to push back on, and how
- The revision is drafted and you need the response letter to accompany it

> Do the revisions *before* writing the letter. The letter documents changes already made; it should never promise work that is not in the revised manuscript.

## Reading the decision letter

- The **co-editor's letter** is the binding document (at JPE the handling co-editor — Chicago-centered board led by Esteban Rossi-Hansberg, or a companion lead editor: John List for JPE Microeconomics, Greg Kaplan for JPE Macroeconomics — writes it). Identify which referee points the co-editor flags as essential vs. optional and prioritize accordingly.
- Separate requests into: (a) must-do for the co-editor, (b) reasonable and cheap, (c) costly or wrong-headed. Negotiate (c) with evidence, not assertion.
- A JPE co-editor and referees care most about the *economic argument*: expect demands to strengthen the mechanism, address a GE/selection objection, or sharpen identification. Treat those as first-order.
- Plan replication readiness now: a conditional accept triggers the **JPE Data Editor's** reproducibility check and deposit to the **JPE Dataverse** (see `jpe-replication-package`).

## Response-letter structure

1. **Cover note to the co-editor**: thank them; summarize the 3–4 substantive changes; state how the paper is now stronger economically. One page.
2. **Point-by-point**, per referee, in the referee's order:
   - Quote (or paraphrase) the comment.
   - State the change made, with the new text/exhibit and where it now lives (section, table, page).
   - Where you disagree, respond with evidence and economic reasoning — concede what is fair, hold the line where you are right, and never be defensive.
3. **A summary of changes** mapping each major comment to the revised location, so the co-editor can verify at a glance.

Tone: respectful, concise, confident. Every response is either "done, here it is" or "we respectfully differ, and here is why." Avoid hedging and avoid over-promising future work.

## Handling the JPE-typical demands

- **"Strengthen the mechanism"** → route to `jpe-theory-model`; add the model result or the discriminating test, then report it.
- **"Address general equilibrium"** → bound or sign the equilibrium effect; if it materially changes the interpretation, say so honestly.
- **"Rule out alternative X"** → route to `jpe-robustness`; add the discriminating test, summarize in text, table in appendix.
- **"Identification is not convincing"** → route to `jpe-identification`; add diagnostics/falsification or reframe the claim to what the design supports.
- **Conflicting referees** → flag the conflict to the co-editor and explain the path you chose and why.

## Checklist

- [ ] Every referee point has an explicit response (none skipped)
- [ ] Each "done" response points to the exact revised location
- [ ] Disagreements backed by evidence/economic reasoning, framed respectfully
- [ ] Co-editor's essential requests all addressed first
- [ ] Mechanism / GE / identification demands treated as first-order
- [ ] Replication package on track for the JPE Data Editor if a conditional accept follows
- [ ] Revisions are actually in the manuscript before the letter is written
- [ ] Summary-of-changes table maps comments → locations
- [ ] No new claim is over-promised without being delivered

## Anti-patterns

- Writing the response letter before doing the revisions
- Skipping or merging referee points to seem responsive
- Defensive or dismissive tone toward a fair criticism
- Conceding a correct result because a referee pushed hard (defend it with evidence)
- Promising "future work" in place of an analysis the editor asked for now
- Ignoring the co-editor's prioritization and treating all comments as equal

## Output format

```
【Decision】R&R / reject-with-encouragement
【Co-editor's essential points】1... 2... 3...
【Per-referee plan】R1: [done / push-back + evidence] ; R2: ... ; R3: ...
【First-order (mechanism/GE/ID)】how addressed
【Revisions complete before letter】[y/n]
【Summary-of-changes table】drafted? [y/n]
【Replication readiness】code ready for JPE Data Editor on accept? [y/n]
【Next】resubmit via Editorial Manager (jpe-submission for format re-check)
```
