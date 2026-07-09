---
name: socc-author-response
description: Use when drafting an ACM SoCC author response (rebuttal) during a round's response window, covering the single written turn, answering both the systems and the data/measurement reviewer, supplying the tail-latency and cost numbers reviewers ask for, staying within dual anonymity, and the fact that SoCC has no Major-Revision round to fall back on.
---

# SoCC Author Response

Use this after SoCC reviews are released, during the round's **author-response (rebuttal) window**
(SoCC 2026 Round 2: 10-12 Sep 2026). SoCC gives you **one written turn**, not a journal-style
revise-and-resubmit — there is no Major Revision to repair the paper in, so the rebuttal must do all
the persuading before the PC discussion decides. Because the reviewer pool is drawn from **both
SIGMOD and SIGOPS**, a winning rebuttal answers the *systems* reviewer and the *data/measurement*
reviewer, not one at the expense of the other.

## Triage

- Answer what affects the decision: significance of the cloud contribution, soundness of the
  mechanism, realism of the deployment or trace, and the measurement quality — especially **tail
  latency and cost**, the numbers reviewers most often say are missing.
- Prioritize by impact-times-fixability: a factual misreading you can correct, or a number you can
  supply from existing logs, moves more than a philosophical disagreement.
- Correct factual misreadings first; a reviewer who misread a table or a workload is often
  persuadable.
- Keep every word within dual anonymity: do not reveal your cluster, company, provider, trace
  provenance, or system's real name to strengthen a point.

## Structure the single turn

Short and decision-focused. Map each reviewer to the axis they raised:

```text
[R1 - systems] "Evaluated in simulation only?"
       -> We report the 200-node testbed run in Table 2 (already in the paper, §5.2); rebuttal
          clarifies it is a real deployment, not a simulator.
[R2 - measurement] "Tail latency not reported."
       -> p99 attainment is in Fig. 3; we add the p99.9 breakdown from existing logs and will
          include it in the final version.
[R3 - cost] "Cost claim unsupported."
       -> Provisioned instance-seconds vs. the CPU baseline are in Table 2; we clarify the pricing
          model used and the saving it implies.
```

Answer the reviewer on the axis they actually raised. Do not spend the systems reviewer's attention
defending a measurement point they did not make.

## Reviewer pushback patterns

| Pushback | What it signals | SoCC-ready response |
|---|---|---|
| "Simulation only / not a real system" | Systems realism doubt | Point to the testbed/deployment result, or scope the claim honestly |
| "Only average latency reported" | Missing the cloud outcome | Supply p95/p99 from existing logs; do not promise unrun experiments as fact |
| "Baseline is not tuned/fair" | Soundness of the comparison | Report the tuned-baseline number with an equal, documented budget |
| "Workload/trace is unrepresentative" | Measurement validity (data reviewer) | Justify the trace's provenance and scope; bound the external-validity limit |
| "Cost/economic claim hand-waved" | The adoption outcome is unproven | Give the cost breakdown and the pricing model behind it |
| "Overlaps prior cloud work X" | Novelty/delta doubt | Sharpen the one-sentence delta against the nearest SoCC/OSDI/NSDI work |

## What a SoCC rebuttal may and may not do

- **May:** cite numbers already in the paper the reviewer overlooked; report an analysis of
  *existing* logs (a tail percentile, a cost breakdown) that needs no new run; correct a
  misreading; commit to a concrete, bounded final-version change.
- **May not:** present major new experiments as if already done; reveal identity to make a point;
  argue taste; over-promise a revision that SoCC's accept/reject process has no round to verify.

## Anonymity in the rebuttal (easy to slip)

- Refer to your own prior work in the third person, as in the paper.
- Describe artifact or trace changes without linking to an identity-revealing repository or naming
  the source deployment.
- Do not thank a named collaborator, funder, or provider inside the response.

## Calibration

- Respond to the criterion the reviewer actually raised, not the one you would rather defend.
- Length and format of the response vary by cycle; confirm the current instructions and the
  character/word limit before sending.
- The PC discussion decides; the rebuttal is evidence for an advocate. Remember there is **no
  fallback revision round** — this turn is the paper's last word before the verdict.

## Output format

```text
[Round + window] round 1 / round 2; response window dates
[Priority issues] <one decision-critical concern per reviewer>
[Axis map] each concern -> systems | measurement/data | cost/tail | novelty
[Response ledger] <concern -> correction / existing-log number / tuned baseline / bounded final-version change>
[Anonymity check] <no cluster/provider/system-name/trace leak in the response: passed/issues>
```
