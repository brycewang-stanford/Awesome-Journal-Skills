---
name: icsme-author-response
description: Use when drafting an IEEE ICSME author response during the double-anonymous author-response period, covering the early-decision cut that decides whether you respond at all, answering the PC's specific "Response Recommended" questions with existing evidence, staying anonymous, and doing it in one round with no Major Revision safety net.
---

# ICSME Author Response

Use this after ICSME early decisions are released. ICSME gives authors **one speaking turn**, and
whether you get it at all is decided first: at the start of the author-response period, papers are
sorted into **Accept**, **Reject**, or **Response Recommended**. Only "Response Recommended" papers
write a rebuttal, and because there is **no Major Revision round**, that rebuttal is the last word
before the final decision.

## First: read which bucket you are in

- **Early Accept** — do not write a defensive response; move to camera-ready and the ROSE artifact.
- **Early Reject** — no response is requested; a response would not be read. Reroute or rebuild.
- **Response Recommended** — you are in contention. The PC has specific questions; the rest of this
  skill is for you.

## Triage the questions the PC actually asked

- Answer the **specific questions the PC raised** in the response invitation first — they are what
  the discussion will turn on. A rebuttal that ignores the flagged questions to relitigate the
  reviews' tone is wasted.
- Use evidence that **already exists** in the submitted paper or artifact. ICSME cannot accept "we
  will add this" — there is no revision round to add it in. Point to where the answer lives.
- Correct factual misreadings first; a reviewer who misread a change-history table or a mining
  criterion is often persuadable within one round.
- Keep every word anonymous. Do not name your tool's real name, your own subject system, your
  institution, grant, or a private repository, even to strengthen a point.

## Structure a single-round ICSME rebuttal

Short and decision-focused. Address the PC's questions in priority order; one decisive answer per
reviewer beats an exhaustive reply.

```text
[Q1 - reviewer question, quoted briefly]
     -> Answer: the held-out result they asked for is already in Table 3 (§4.2); we clarify it here
     -> Evidence: §4.2, Table 3; artifact/analysis/rq2 logs (anonymized location)
[Q2 - "is the baseline tuned fairly?"]
     -> Answer: both tools ran with the equal, documented budget in §4.1; we restate the setting
[Q3 - "does this generalize beyond one ecosystem?"]
     -> Answer: we scope the claim to the studied systems and name it as an external-validity
        threat in §5.2; we cannot add subjects in this round and do not claim we can
```

The rule that wins a single-round rebuttal: **answer what was asked with what already exists, and
concede cleanly what you cannot show.** Overclaiming a fix you cannot make in a non-revision process
is what a careful PC catches.

## Reviewer pushback patterns

| Pushback | What it signals | ICSME-ready response |
|---|---|---|
| "The baseline is not tuned/fair" | Soundness doubt about the comparison | Point to the equal, documented budget already in the paper; restate the numbers |
| "This is a proxy for the real maintenance outcome" | Construct-validity objection | Point to the audited subsample or bound the proxy; state the residual threat |
| "Does this hold beyond one system's history?" | External-validity limit | Scope the claim to the studied systems; name the threat — do not promise new mining |
| "The mined corpus is not reproducible" | Open-science / provenance gap | Point to pinned SHAs, extraction dates, and the anonymized dataset in the artifact |
| "Overlaps prior maintenance work X" | Novelty/delta doubt | Sharpen the delta sentence against X using what is already in the paper |

## Anonymity in the response (easy to slip)

- Refer to your own prior maintenance/evolution work in the third person, as in the paper.
- Describe the artifact without linking to an identity-revealing repository or your public org.
- Do not name the real subject system if naming it would reveal the authors; use the anonymized
  descriptor from the paper.
- Do not thank a named collaborator or funder inside the response.

## Calibration

- Respond to the criterion the reviewer actually raised, not the one you would rather defend.
- There is no second round: do not defer the answer to a "camera-ready version" the PC has not seen.
- The PC discussion decides; the response is evidence for an advocate in that discussion, not a
  closing argument.
- Response length and format vary by cycle; confirm the current instructions before sending.

## Output format

```text
[Bucket] early accept / response recommended / early reject
[PC question] <the specific question being answered>
[Decision dimension] significance / soundness / evidence / threats / clarity / open-science
[Answer ledger] <question -> answer + where the supporting evidence already lives>
[Anonymity check] <no identity leak in the response: passed/issues>
```
