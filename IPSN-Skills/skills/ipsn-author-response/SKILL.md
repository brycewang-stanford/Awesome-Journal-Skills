---
name: ipsn-author-response
description: Use when drafting an IPSN-lineage rebuttal, covering the double-blind response to sensor-systems reviewers on ground truth, baseline fairness, deployment realism, energy accounting, and simulation-vs-real-hardware doubts, without leaking identity and without promising experiments not yet run.
---

# IPSN Author Response

Use this after IPSN-lineage reviews are released. IPSN is conference-style: a short, decision-focused
**rebuttal** (verify the window and format on the current successor call), not a journal-style
revise-and-resubmit letter. The rebuttal must stay **double-blind** — no author names, institutions,
lab-named testbeds, or identity-revealing dataset/firmware links — and it must answer on the axes a
sensor-systems reviewer actually raised.

## Triage

- Answer what affects the decision: **evidence realism** (simulation vs real hardware), **soundness**
  of the method/platform, **baseline fairness**, **ground-truth validity**, **deployment honesty**,
  and **energy/latency accounting**.
- Use evidence that already exists or a number you can compute from data you already have — never a
  vague promise to run an experiment.
- Correct factual misreadings first; a reviewer who misread an energy table or a yield number is
  often persuadable.
- Keep every word anonymous. Do not name your board, testbed, institution, or a resolvable dataset
  DOI, even to strengthen a point.

## The rebuttal itself

Short and decision-focused. One decision-critical point per reviewer beats an exhaustive reply.
Concede what is true, correct what is misread, and point to exactly where the answer lives in the
submitted paper or artifact. Do not paste large new results the reviewers cannot verify in the
window.

```text
[R1 - "simulation only"]  -> Point to the real-hardware result already in §4.2 / Table 3 (measured on
                             the MCU), which the review may have missed; state the platform and clock.
[R2 - "baseline untuned"] -> Report the equal-condition comparison already logged; give the number and
                             where it lives; if a tuning was fixed, say the budget was equal and documented.
[R3 - "ground truth?"]    -> Name the surveyed reference and its own error; correct the misread that the
                             ground truth came from the model under test.
```

## Reviewer pushback patterns (sensor-systems flavored)

| Pushback | What it signals | IPSN-ready response |
|---|---|---|
| "Only simulated / no real hardware" | Evidence-realism doubt (often fatal) | Point to the on-device/in-field result if it exists; if it truly doesn't, concede and scope the claim rather than promise it |
| "Baseline is not a real alternative / untuned" | Soundness doubt about the comparison | Report the equal-condition numbers; name the tuning budget |
| "Energy is estimated, not measured" | Accounting doubt | Point to the instrumented-rail measurement and conditions; if only estimated, say so and bound it |
| "Deployment numbers look idealized" | Honesty doubt | Report yield, sync error, and failures as measured; do not sand off the losses |
| "Ground truth is circular / weak" | Construct doubt | Name the independent reference and its error; state the residual limit |
| "Wrong track / out of scope" | Track or venue mismatch | Clarify the primary contribution's track; hard to fully fix in rebuttal |

## Anonymity in the rebuttal (easy to slip)

- Refer to your own prior work in the third person, as in the paper.
- Describe artifact/firmware changes without linking to an identity-revealing repository; use the
  anonymized location.
- Do not thank a named collaborator, funder, or facility inside the rebuttal.
- Do not paste a board photo or a dataset DOI that reveals the lab.

## Calibration

- Respond to the criterion the reviewer actually raised, not the one you would rather defend.
- The PC discussion decides; write the rebuttal as evidence for an advocate, and let the measured
  evidence already in the paper carry the argument.
- IPSN is not a Major-Revision venue: there is usually no guaranteed second read, so a rebuttal that
  promises future experiments rarely helps. Confirm the current mechanics on the successor call.

## Output format

```text
[Turn] rebuttal (conference-style; confirm window/format on the current call)
[Priority issue] <reviewer concern>
[Decision dimension] evidence-realism / soundness / baseline / ground-truth / deployment-honesty / energy
[Answer] <where the answer lives in paper/artifact, or the honest concession + scope>
[Anonymity check] <no identity leak, incl. board photos / testbed names / dataset DOIs: passed/issues>
```
