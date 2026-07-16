---
name: jim-rebuttal
description: Use when responding to a Journal of International Marketing (JIM) decision letter — triaging reviewer demands, deciding whether to collect new-country data, and writing the point-by-point response. It manages the revision round; the upstream skills execute the actual fixes.
---

# Revision & Response Strategy (jim-rebuttal)

## When to trigger

- A JIM major/minor revision (or reject-and-resubmit) letter has arrived
- Reviewers demand new countries, invariance re-tests, or identification repairs and the team must decide what to concede
- Reviewers contradict each other about the paper's core
- The response letter is drafted but reads as defensive point-scoring

## First pass: decode the letter

Read the **AE's letter twice before the reviews once** — at AMA journals the AE synthesis tells you which reviewer comments are binding and which are optional color. Extract: (1) the must-do list the AE endorses; (2) the paper-threatening comments (identification, invariance, contribution) vs. the effort comments (additional analyses, exposition); (3) the disagreements the AE expects *you* to adjudicate. Build the master grid: comment → owner skill → planned action → concede/counter → evidence needed.

## The demands JIM revisions typically turn on

- **"Add another country / sample."** Decide on theory, not appeasement. Concede when the added country genuinely extends the dimension's range or breaks a confound the reviewer correctly spotted. Counter when the contrast already identifies the claim — show *why* with the confound audit from `jim-methods`, and offer a boundary-condition acknowledgment instead. New-country collection costs months; say so transparently and propose the timeline if you commit.
- **"Your invariance evidence is insufficient."** Almost always concede and upgrade: full ladder table, partial-invariance handling, alignment for many groups, and a restatement of which comparisons the results license (`jim-data-analysis`). If scalar invariance fails on re-test, renegotiate the framing honestly rather than hiding the casualty.
- **"Culture is asserted, not measured."** Add the individual-level cultural measure or the country-dimension moderation test; if the data cannot support it, reframe claims to institutional or development mechanisms actually measured (`jim-theory-development`).
- **"Endogeneity of the international choice."** Export/entry decisions are selected; respond with design-based fixes (selection models, FE, shock-based variation) plus a sensitivity analysis, not with a paragraph of reassurance.
- **"Contribution is incremental."** Rebuild the ledger (`jim-contribution-framing`) and show which prediction from the domestic canon the data reject. This is a framing battle — win it with a sharper theory delta, not adjectives.
- **A regional expert disputes your country narrative.** Treat as a gift: correct the institutional detail, cite regional sources, and show the result survives the corrected reading.

## Revise first, then write

Sequence the work: run every new analysis and settle the manuscript before polishing the letter — a response drafted around unfinished analyses drifts into promises. Keep a revision log (file, section, change, reason) so the summary-of-changes writes itself.

## Response-letter craft

- Open with a one-page summary of the major changes, keyed to the AE's must-do list.
- Reproduce every comment verbatim, numbered (AE.1, R1.1…); answer each with: the change made, where (page/section), and the evidence. Quote the revised passage in the letter — do not force reviewers to hunt.
- Concessions: gracious and complete ("The reviewer is right; we re-estimated… results in new Table 5"). Counters: respectful, evidence-first, and rare — three strong counters read as confidence; ten read as obstinacy.
- When R1 and R2 conflict, name the conflict, state your resolution, and anchor it to the AE's guidance.
- Every new analysis goes in the manuscript or Web Appendix, not only in the letter — the letter is not part of the published record.
- Keep the letter anonymous too: no author names, no identifying project details.
- Mind the caps: revisions must still fit 50 pages; big additions displace something (`jim-tables-figures` prunes).

## Round-two discipline

Address exactly what round one asked; introduce nothing new that was not requested — new material reopens review. If the AE added conditions in round two, treat them as the entire job. A conditional accept means execute the conditions verbatim and resist last-minute "improvements."

## Checklist

- [ ] AE synthesis decoded; must-do list separated from optional color
- [ ] Master grid built: every comment → action → owner skill → evidence
- [ ] New-country/new-study decisions made on theory and cost, stated transparently
- [ ] All analyses finished before the letter was polished
- [ ] Every comment reproduced and answered with page-referenced changes
- [ ] Counters limited to genuinely defensible points, evidence attached
- [ ] Revised manuscript still inside the 50-page cap; letter anonymized

## Anti-patterns

- Answering the AE's synthesis with silence while over-serving a tangential reviewer
- Collecting a token extra country that extends nothing but the timeline
- Hiding a failed invariance re-test behind a footnote
- "We thank the reviewer for this excellent comment" followed by no change
- Fighting every point — or conceding every point, including wrong ones
- Burying new results in the response letter where readers of the journal will never see them

## Output format

```text
【Decision】major / minor / reject-and-resubmit / conditional accept
【Must-do list】AE-endorsed items: [n]; paper-threatening: [which]
【Data decision】new country/study: yes (rationale + timeline) / no (defense)
【Grid status】comments mapped __ / __; analyses complete?
【Letter】verbatim comments + page-referenced changes + quoted revisions: pass/fix
【Counters】[n], each evidence-backed
【Next step】resubmit via ScholarOne → jim-review-process (round 2)
```
