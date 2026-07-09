---
name: icdm-review-process
description: Use when reasoning about the ICDM (IEEE International Conference on Data Mining) review machinery - the triple-blind mechanics, the Accept / Accept-as-Short / Reject outcome space, the mixed data-mining reviewer pool, PC Co-Chair decision-making, the traditional no-rebuttal posture, and how to read an ICDM decision packet.
---

# ICDM Review Process

Understand how ICDM decisions are actually made, so you can write for the process and read the
outcome correctly. ICDM's Research Track runs a **triple-blind** review, has a distinctive
**short-paper** outcome, and traditionally offers **no author rebuttal** — a very different shape
from OpenReview venues with public discussion.

## Triple-blind mechanics

- Author identities and referee identities are both concealed. Since 2011, referee names are
  hidden even from each other during discussion; only the **PC Co-Chairs** know who is who.
- Author names are disclosed **only after ranking and acceptance are finalized** — so nothing in
  the review can be swayed by who you are, for better or worse.
- Practical consequence: the paper is judged purely on the anonymized PDF and its cited
  anonymized artifact. Write for a reviewer who knows nothing about you.

## The outcome space

| Outcome | What it means | Your move |
|---|---|---|
| Accept (regular) | In as a full paper | Camera-ready at full length |
| **Accept as Short** | Contribution valued, but scoped/evidenced for short length | Compress to the short camera-ready (see `icdm-camera-ready`) |
| Reject | Not accepted this edition | Revise and route (SDM/CIKM/KDD next window) |

The Accept-as-Short outcome is ICDM's signature: a full submission can be offered acceptance at
short length rather than rejected outright. Plan for it (see `icdm-workflow`), because it arrives
with the notification and a compressed camera-ready deadline.

## The reviewer pool

- ICDM reviewers are data-mining specialists: algorithmic, graph, temporal, and applied-mining
  researchers. They reward a named mechanism, careful baselines, and defensible discovery, and
  they punish leaderboard-only novelty and un-checkable claims.
- The Applied Track (single-blind, new in 2026) draws a more application-oriented pool that
  weights deployment and measured real-world impact.
- Expertise varies within a paper's reviews; the self-contained body (no rebuttal to clarify) is
  your defense against a reviewer who misreads the setup.

## The no-rebuttal posture

- Historically ICDM has **no author-response window**; whether the current edition adds one is
  待核实 (see `icdm-author-response`). Assume none when planning.
- This makes the submitted PDF and cited artifact your *only* argument. Every likely reviewer
  question — baseline fairness, leakage, variance, scale — must be pre-answered on the page.
- A weakness "left for the rebuttal" is a weakness left unaddressed.

## Reading a decision packet

```text
1. Find the decision line: Accept / Accept-as-Short / Reject.
2. If Accept-as-Short, read reviews for WHAT to cut vs keep - the mechanism stays.
3. Cluster review concerns: correctness, baselines, novelty, scale, clarity, validity.
4. Separate factual misreadings (fixable in camera-ready framing) from real gaps
   (need new experiments -> next venue).
5. Note anything the reviewers could not see because it was missing from the PDF/artifact;
   that is your no-rebuttal lesson for next time.
```

## Vignette: reading an Accept-as-Short correctly

A paper comes back "accepted as a short paper": reviewers found the mechanism novel but felt one
of three experiments was under-developed. The wrong read is disappointment; the right read is a
scoping instruction. The team keeps the mechanism and its strongest experiment in the short body,
moves the two weaker experiments and all protocol detail to the cited repository, and ships a
tight short paper on time — the contribution is preserved, just at the length reviewers judged it
earned.

## Output format

```text
[Decision] Accept / Accept-as-Short / Reject
[Regime read] triple-blind (Research) / single-blind (Applied)
[Concern clusters] correctness / baselines / novelty / scale / clarity / validity
[Misreading vs gap] <which concerns are framing-fixable vs need new work>
[No-rebuttal lesson] <what was missing from PDF/artifact that reviewers needed>
[Next move] camera-ready / short-compression / revise-and-route
```
