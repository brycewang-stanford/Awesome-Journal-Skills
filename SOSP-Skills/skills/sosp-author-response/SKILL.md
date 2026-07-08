---
name: sosp-author-response
description: Use when drafting a SOSP author response during the pre-PC-meeting rebuttal window, keeping it within the venue's norms — correcting factual errors, answering direct reviewer questions, staying near the 500-word guidance, and never introducing new experiments, new data, or promises of future work.
---

# SOSP Author Response

Use this when SOSP reviews land and the response window opens. SOSP's response phase
has an unusually narrow charter, stated in the CFP (verified 2026-07-08 for the 2026
cycle): responses exist to **correct factual errors in the reviews** and to **answer
questions reviewers explicitly posed**. They must not add new experiments or data,
describe work done since submission, or promise follow-up work. Submitting a response
is optional, and while no hard cap is stated, authors are strongly encouraged to stay
**under 500 words**.

## What the response can and cannot do

The response is read by a program committee that will discuss the paper live at a PC
meeting. Its job is to remove false obstacles before that discussion, not to renegotiate
the paper.

| Move | Allowed at SOSP? | Why |
|---|---|---|
| "Review B states we hold the lock across I/O; §4.2 shows it is released before the write" | Yes | Factual correction, cites the submitted text |
| Answering "how does this behave when the log fills?" with what the submission already supports | Yes | Direct reviewer question |
| "We have since run the benchmark on 128 nodes and..." | No | New data after the deadline |
| "We will add a comparison against X in the final version" | No | Promised work |
| Re-arguing novelty against a reviewer's taste judgment | Technically allowed, usually wasted words | Not a factual error |
| Pointing to the supplementary document for detail the reviewer missed | Yes, sparingly | It was part of the submission |

## Hour-zero triage

Read all reviews once without drafting anything, then classify every negative point:

1. **Factual error** — the review misstates what the paper says or does. Highest
   priority; these are the response's reason to exist.
2. **Missed content** — the answer is in the paper but the reviewer did not find it.
   Respond with a section/figure pointer and one sentence of restatement.
3. **Direct question** — answer it crisply from the submitted material.
4. **Judgment call** — "not novel enough," "evaluation could be broader." Spend at most
   one sentence, or zero; the PC meeting will weigh these, and defensive prose does not
   move systems reviewers.

If categories 1-3 are empty, seriously consider not responding: an optional response
that only pushes back on judgments can read worse than silence.

## Budgeting 500 words

- Open with two sentences maximum of thanks and framing; no summary of the paper.
- Order points by expected impact on the PC discussion, not by reviewer order.
- Quote the review's exact claim in a few words before rebutting, so a PC member
  skimming during the meeting can follow without the full review open.
- Cite the submission by section, figure, or table number every time — the submitted
  PDF is the only evidence you are allowed to use.

```text
Response skeleton (target < 500 words total)

We thank the reviewers. We correct three factual points and answer two questions.

[Factual] Rev A: "the design requires a second network round trip."
It does not: the token is piggybacked on the existing ack (§3.3, Fig. 4).

[Factual] Rev C: "no failure experiments."
§5.4 and Table 6 report crash-restart and partition runs on the same workloads.

[Question] Rev B asked how recovery time scales with log size.
Recovery replays only the tail past the last checkpoint; §4.5 gives the bound
and Fig. 9 measures it at three log sizes.

[Clarification] Rev A read the consistency guarantee as per-object; it is
per-session (§2, invariant I2). The distinction affects the Rev A example: ...
```

## Tone calibration for a single-track PC

Every accepted SOSP paper is discussed in front of the whole committee, so your
response's audience is wider than the three or four people who reviewed it. Write so a
non-reviewer PC member encountering the paper for the first time at the meeting sees
authors who are precise, unrattled, and honest about limits. Concede real weaknesses in
one clean sentence ("The evaluation does not include workload X; the submitted results
cover Y and Z") rather than burying them — a concession you volunteer is a footnote at
the meeting, one you dodge becomes the meeting's topic.

## Common failure modes

- Spending the word budget proportionally to review length instead of review influence.
- Correcting five trivialities and leaving the one score-driving misreading to last.
- Smuggling in a new number "for context" — chairs notice, and it taints the compliant
  parts of the response.
- Addressing reviewers by name-like inference ("as the senior reviewer notes...");
  reviews are anonymous in both directions.
- Writing 900 words because no hard limit exists. The 500-word guidance is a signal
  about attention at the PC meeting, not a formality.

## Output format

```text
[Respond at all?] yes / no (categories 1-3 empty)
[Point map] <review point -> factual error / missed content / question / judgment>
[Word budget] <allocation across points, total target>
[Concession] <the one weakness to own explicitly>
[Compliance check] no new data / no promises / submission-only citations
```
