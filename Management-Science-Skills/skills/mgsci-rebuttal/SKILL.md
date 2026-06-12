---
name: mgsci-rebuttal
description: Use when planning and drafting the revision and point-by-point response for a Management Science (INFORMS) R&R — prioritizing the Department Editor's binding concerns, addressing analytical-proof or empirical-identification objections, preserving double-anonymization, and keeping the revision within the page cap and Data-and-Code-Disclosure requirements. It handles the post-decision response; it does not run a fresh submission (mgsci-submission).
---

# R&R Rebuttal (mgsci-rebuttal)

## When to trigger

- You received a major-revision (R&R) decision from Management Science
- You have reviewer reports and a Department Editor letter and must plan the response
- You are unsure which concerns are decisive versus advisory
- You need to fit a strengthened paper inside the invited-revision page cap

## Read the Department Editor's letter as the map

In Management Science the **Department Editor** synthesizes the reviews and signals which concerns are **binding**. Plan the revision around that letter first: list every point from the DE and each reviewer, mark each binding / important / advisory, and resolve any conflicts between reviewers by deferring to the DE's framing (note the conflict explicitly in your response).

## Address objections in the paper's lane

- **Analytical lane.** If a reviewer questions an assumption, either defend its necessity or show the result survives relaxing it (add an extension/robustness proposition). If a proof step is challenged, tighten the proof and, where useful, add a numerical illustration. Reframe comparative statics to make the managerial intuition unmistakable.
- **Empirical lane.** If identification is challenged, add the design test the reviewer expects (parallel-trends/event-study, alternative instruments, RDD continuity, placebo/falsification) rather than asserting validity. Add robustness across specs, samples, and measures.
- **Fit / contribution.** If the concern is cross-department fit or "so what," strengthen the contribution framing (see `mgsci-contribution-framing`) — make the decision relevance and cross-department travel explicit.

## Response-letter mechanics

- One **point-by-point** letter: quote each comment, then state precisely what changed and where (section/page/exhibit).
- Be **responsive, not defensive** — where you disagree, give evidence/argument and propose a compromise, never dismiss.
- Provide a **summary of changes** up front so the DE and reviewers see the headline improvements quickly.

## Preserve the rules on resubmission

- **Double-anonymization** still holds — keep the revised manuscript and response letter free of identifying language.
- **Page cap:** the invited revision must fit **47 pages double-spaced (25 lines/page)** or **32 pages 1.5-spaced (33 lines/page)**, 11-pt, 1-inch margins; **the online appendix is excluded** — move new proofs and secondary robustness there to stay within the limit.
- **Data and Code Disclosure:** update the replication package so it regenerates **every** main-text result in the revised paper; the Data Editor will verify it before publication.
- Keep author-year citation style and update references for any new work cited.

## Concern-triage table

The Department Editor's letter ranks concerns; treat each by type, not reviewer order.

| Concern type | Treatment in the revision |
|--------------|---------------------------|
| DE-flagged "binding" | Resolve fully; headline it in the summary of changes |
| Identification / proof correctness | Add the test or tighten the step; never assert |
| Cross-department fit / "so what" | Strengthen the contribution and travel case |
| Reviewer-only "advisory" | Address briefly; defer to DE on conflicts |

## Worked micro-example (illustrative): an R&R on a platform field experiment

The DE letter calls one concern binding: a referee argues the retention effect could be a novelty bump that fades. The author leads the response with the binding fix — a pre-registered 12-week follow-up showing the effect persists at roughly 3 points (illustrative) versus 4 at week 4 — placed in the main text, with extended tables moved to the online appendix to protect the page cap. A second referee wanted alternative clustering; the author adds it as a robustness column rather than asserting the original was fine. Each response quotes the comment, states the change, and gives section and exhibit. The structure (binding first, evidence not assertion, appendix offload) is the point.

## Referee-pushback patterns and the venue-specific fix

- **"You did not address the Department Editor's main concern."** Reorder the response so the binding DE point is resolved first and visibly.
- **"You asserted robustness instead of showing it."** Add the actual test (placebo, alternative spec, follow-up wave) the referee named.
- **"The revision is over the page cap."** Move new proofs and secondary tables to the online appendix, which is excluded from the count; confirm the current cap in the author guidelines.

## Anti-patterns

- Answering reviewers but ignoring the Department Editor's prioritization.
- Asserting robustness instead of adding the test the reviewer asked for.
- Letting the strengthened paper blow past the page cap by stuffing the counted body.
- A response letter that argues without showing the corresponding manuscript change.

## Output format

```
【DE binding concerns】[ranked]
【Per-comment plan】comment → change → location (section/page/exhibit)
【Lane fixes】proofs/assumptions OR identification/robustness added
【Fit/contribution】strengthened: yes/no
【Constraints】anonymized; within page cap; disclosure package updated: yes/no
【Next step】resubmit via ScholarOne (mgsci-submission for portal mechanics)
```
