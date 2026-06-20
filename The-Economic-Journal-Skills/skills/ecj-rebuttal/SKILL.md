---
name: ecj-rebuttal
description: Use when a The Economic Journal (EJ) decision letter (R&R or reject-with-encouragement) has arrived and you need to draft the response-to-referees letter and revision plan. Structures the response and the diff; it does not redo the analysis (route back to ecj-identification / ecj-theory-model / ecj-robustness first).
---

# R&R Response & Rebuttal (ecj-rebuttal)

## When to trigger

- An EJ R&R (or reject-with-encouragement-to-resubmit) letter has arrived
- You have referee reports and need a point-by-point response plan
- You are deciding which requests to implement, which to push back on, and how
- The revision is drafted and you need the response letter to accompany it

> Do the revisions *before* writing the letter. The letter documents changes already made; it should never promise work that is not in the revised manuscript.

## Reading the decision letter

- The **editor's letter** is the binding document (at EJ a handling editor coordinates the report; editor-in-chief **Francesco Lippi**, verified 2026-06-20). Identify which referee points the editor flags as essential vs. optional and prioritize accordingly.
- Separate requests into: (a) must-do for the editor, (b) reasonable and cheap, (c) costly or wrong-headed. Negotiate (c) with evidence, not assertion.
- An EJ editor and referees care most about the *economic argument* **and broad interest**: expect demands to strengthen the mechanism, broaden the relevance / bound the generality, or sharpen identification. Treat those as first-order.
- Plan replication readiness now: acceptance triggers the **EJ Data Editor's** pre-acceptance reproducibility check and a **Zenodo** deposit (see `ecj-replication-package`).

## Response-letter structure

1. **Cover note to the editor**: thank them; summarize the 3–4 substantive changes; state how the paper is now stronger economically and more broadly relevant. One page.
2. **Point-by-point**, per referee, in the referee's order:
   - Quote (or paraphrase) the comment.
   - State the change made, with the new text/exhibit and where it now lives (section, table, page).
   - Where you disagree, respond with evidence and economic reasoning — concede what is fair, hold the line where you are right, and never be defensive.
3. **A summary of changes** mapping each major comment to the revised location, so the editor can verify at a glance.

Tone: respectful, concise, confident. Every response is either "done, here it is" or "we respectfully differ, and here is why." Avoid hedging and avoid over-promising future work. Because EJ review is **single-blind**, you already know the report is read by referees who see your identity — keep the tone collegial.

## Handling the EJ-typical demands

- **"Broaden the relevance / it reads too narrow"** → route to `ecj-topic-selection` / `ecj-literature-positioning`; make the general lesson and external relevance explicit, or bound the claim honestly.
- **"Strengthen the mechanism"** → route to `ecj-theory-model`; add the model result or the discriminating test, then report it.
- **"Rule out alternative X"** → route to `ecj-robustness`; add the discriminating test, summarize in text, table in appendix.
- **"Identification is not convincing"** → route to `ecj-identification`; add diagnostics/falsification or reframe the claim to what the design supports.
- **"Improve the exposition"** → route to `ecj-writing-style`; at EJ this is substantive, not cosmetic — take it seriously.
- **Conflicting referees** → flag the conflict to the editor and explain the path you chose and why.

## Checklist

- [ ] Every referee point has an explicit response (none skipped)
- [ ] Each "done" response points to the exact revised location
- [ ] Disagreements backed by evidence/economic reasoning, framed respectfully
- [ ] Editor's essential requests all addressed first
- [ ] Broad-interest / mechanism / identification demands treated as first-order
- [ ] Exposition improvements taken seriously (EJ bar)
- [ ] Replication package on track for the EJ Data Editor if acceptance follows
- [ ] Revisions are actually in the manuscript before the letter is written
- [ ] Summary-of-changes table maps comments → locations
- [ ] No new claim is over-promised without being delivered

## Anti-patterns

- Writing the response letter before doing the revisions
- Skipping or merging referee points to seem responsive
- Defensive or dismissive tone toward a fair criticism
- Conceding a correct result because a referee pushed hard (defend it with evidence)
- Promising "future work" in place of an analysis the editor asked for now
- Dismissing an exposition request as cosmetic when at EJ it carries weight
- Ignoring the editor's prioritization and treating all comments as equal

## Output format

```
【Decision】R&R / reject-with-encouragement
【Editor's essential points】1... 2... 3...
【Per-referee plan】R1: [done / push-back + evidence] ; R2: ... ; R3: ...
【First-order (broad-interest/mechanism/ID)】how addressed
【Exposition】improvements made? [y/n]
【Revisions complete before letter】[y/n]
【Summary-of-changes table】drafted? [y/n]
【Replication readiness】code ready for EJ Data Editor on accept? [y/n]
【Next】resubmit via Editorial Express (ecj-submission for format re-check)
```
