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
