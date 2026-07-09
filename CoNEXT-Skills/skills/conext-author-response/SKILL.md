---
name: conext-author-response
description: Use when drafting ACM CoNEXT author responses, covering the initial-review rebuttal and — distinctively — the one-shot "major" revision response letter that must stay double-anonymous, map every "minimum necessary change" to a concrete tracked edit, and survive a single re-review by the original reviewers and a shepherd under PACMNET.
---

# CoNEXT Author Response

Use this after CoNEXT reviews are released. CoNEXT has **two distinct speaking turns**, and
conflating them is a common mistake: a short initial rebuttal, and — if you receive a **one-shot
major revision** — a full, journal-style **response letter** accompanying a revised paper that the
original reviewers re-read exactly once. Both must respect double-anonymity: the letter itself must
not reveal authors, institutions, testbeds, or repository ownership.

## Triage (both turns)

- Answer what affects the decision: significance, soundness, measurement quality, baseline fairness,
  clarity, and reproducibility.
- Use evidence that already exists or that the revision will concretely add — never a vague promise.
- Correct factual misreadings first; a reviewer who misread a figure or a testbed setup is often
  persuadable.
- Keep every word anonymous. Do not name your system's real name, your institution, your operator
  partner, a grant, or a private repository, even to strengthen a point.

## Turn 1 — the initial rebuttal

Short and decision-focused. One decision-critical point per reviewer beats an exhaustive reply.
Concede what is true, correct what is misread, and point to exactly where the answer lives in the
submitted paper or artifact. Do not paste large new results the reviewers cannot verify in the time
they have.

## Turn 2 — the one-shot major-revision response letter (the distinctive CoNEXT move)

A major revision is a genuine, **one-shot** revise-and-resubmit against a list of **minimum
necessary changes**. The letter is a **change ledger**: for every item on that list (and every
substantive reviewer request), either make the change and show it, or decline it with a reason.

```text
[MNC-1] Minimum-necessary change (quoted briefly)
        -> Action: DONE  | added the real-buffer testbed run, §5.2, Table 3; effect sizes reported
        -> Where: §5.2, Table 3; artifact/testbed/rq2/
[MNC-2] Minimum-necessary change
        -> Action: DECLINED (with reason) | the requested baseline needs operator telemetry we
           cannot release without breaking anonymity/agreement; added a limitation note instead (§6.1)
[R2.1]  Reviewer request (not on the MNC list)
        -> Action: PARTIAL | added the ablation; the larger multi-site deployment is out of scope
           for the revision window and is noted as future work
```

The rule that turns a one-shot revision into an acceptance: **no silent omissions.** A
minimum-necessary change that is neither done nor explicitly declined is exactly what the single
second read punishes. Assume a **shepherd** will check each item against the revised PDF.

## Reviewer pushback patterns

| Pushback | What it signals | CoNEXT-ready response |
|---|---|---|
| "Evaluated in simulation, not on real hardware" | Platform-realism doubt | Add a testbed/deployment run on the real target, or scope the claim and name the gap as a limitation |
| "The baseline is not tuned/fair" | Soundness doubt about the comparison | Re-run with an equal, documented configuration; report the new numbers, or justify the choice |
| "Does this generalize beyond one path/network?" | External-validity limit | Add vantage points or subjects, or scope the claim and name the limit |
| "The measurement is a proxy for the real outcome" | Construct-validity objection | Add the ground-truth subset or bound the proxy; state the residual threat plainly |
| "The artifact does not run / is missing" | Reproducibility gap | Fix and re-anonymize the artifact; describe the run path in the letter |
| "Contribution overlaps prior work X" | Novelty/delta doubt | Sharpen the delta sentence; add the missing comparison |

## Anonymity in the letter (easy to slip)

- Refer to your own prior work in the third person, as in the paper.
- Describe artifact and testbed changes without linking to an identity-revealing repository or an
  internal hostname; use the anonymized location.
- Do not thank a named collaborator, operator partner, or funder inside the response.

## Calibration

- Respond to the criterion the reviewer actually raised, not the one you would rather defend.
- Length and format norms for both turns, and the exact revision window, vary by cycle; confirm the
  current instructions before sending.
- The TPC discussion and the shepherd decide; write the letter as evidence for an advocate, and make
  the revised paper — not the letter — carry the argument.
- Remember it is **one shot**: there is no second revision round, so leave nothing on the change list
  unaddressed.

## Output format

```text
[Turn] initial rebuttal / one-shot major-revision response letter
[Priority issue] <reviewer concern>
[Decision dimension] significance / soundness / measurement quality / baselines / clarity / reproducibility
[Change ledger] <minimum-necessary change -> DONE/PARTIAL/DECLINED + where in paper/artifact>
[Anonymity check] <no identity leak in the letter: passed/issues>
```
