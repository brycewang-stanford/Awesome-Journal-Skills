---
name: fse-author-response
description: Use when drafting ESEC/FSE author responses, covering the initial-review rebuttal and — distinctively — the journal-style Major Revision response letter that must stay double-anonymous, map every reviewer request to a concrete tracked change, and survive re-review by the original reviewers under PACMSE.
---

# FSE Author Response

Use this after FSE reviews are released. FSE has **two distinct speaking turns**, and conflating
them is a common mistake: a short initial rebuttal, and — if you receive a **Major Revision** — a
full, journal-style **response letter** accompanying a revised paper that the original reviewers
re-read. Both must respect heavy double-anonymity: the letter itself must not reveal authors,
institutions, or repository ownership.

## Triage (both turns)

- Answer what affects the decision: significance, soundness, evidence quality, threats to validity,
  clarity, and open-science support.
- Use evidence that already exists or that the revision will concretely add — never a vague promise.
- Correct factual misreadings first; a reviewer who misread a table is often persuadable.
- Keep every word anonymous. Do not name your tool's real name, institution, grant, or a private
  repository, even to strengthen a point.

## Turn 1 — the initial rebuttal

Short and decision-focused. One decision-critical point per reviewer beats an exhaustive reply.
Concede what is true, correct what is misread, and point to exactly where the answer lives in the
submitted paper or artifact. Do not paste new results the reviewers cannot verify.

## Turn 2 — the Major Revision response letter (the distinctive FSE move)

A Major Revision is a genuine revise-and-resubmit. The letter is a **change ledger**: for every
reviewer request, either make the change and show it, or decline it with a reason.

```text
[R1.1] Reviewer request (quoted briefly)
       -> Action: DONE  | changed §4.2, added Table 3 (held-out projects), effect sizes reported
       -> Where: §4.2, Table 3; artifact/analysis/rq2.ipynb
[R1.2] Reviewer request
       -> Action: DECLINED (with reason) | the requested baseline assumes labels we cannot obtain
          without violating anonymity/ethics; added a threats note instead (§5.2)
[R2.1] Reviewer request
       -> Action: PARTIAL | added the ablation; the larger user study is out of scope for the
          revision window and is noted as future work
```

The rule that turns a Major Revision into an acceptance: **no silent omissions.** A request that
is neither done nor explicitly declined is what the second read punishes.

## Reviewer pushback patterns

| Pushback | What it signals | FSE-ready response |
|---|---|---|
| "The baseline is not tuned/fair" | Soundness doubt about the comparison | Re-run with an equal, documented budget; report the new numbers, or justify the choice |
| "This is a proxy for the real outcome" | Construct-validity objection | Add the audited subsample or bound the proxy; state the residual threat plainly |
| "Does this generalize beyond one ecosystem?" | External-validity limit | Add subjects, or scope the claim and name the limit as a threat |
| "The artifact does not run / is missing" | Open-science / verifiability gap | Fix and re-anonymize the artifact; describe the demo path in the letter |
| "Contribution overlaps prior work X" | Novelty/delta doubt | Sharpen the delta sentence; add the missing comparison |

## Anonymity in the letter (easy to slip)

- Refer to your own prior work in the third person, as in the paper.
- Describe artifact changes without linking to an identity-revealing repository; use the
  anonymized location.
- Do not thank a named collaborator or funder inside the response.

## Calibration

- Respond to the criterion the reviewer actually raised, not the one you would rather defend.
- Length and format norms for both turns vary by cycle; confirm the current instructions before
  sending.
- The PC discussion decides; write the letter as evidence for an advocate, and make the revised
  paper — not the letter — carry the argument.

## Output format

```text
[Turn] initial rebuttal / major-revision response letter
[Priority issue] <reviewer concern>
[Decision dimension] significance / soundness / evidence / threats / clarity / open-science
[Change ledger] <request -> DONE/PARTIAL/DECLINED + where in paper/artifact>
[Anonymity check] <no identity leak in the letter: passed/issues>
```
