---
name: facct-author-response
description: Use when drafting ACM FAccT author responses — above all the Revise-round rebuttal that FAccT 2027 submits together with the revised paper, addressing Area-Chair-prioritized concerns from a mixed CS+law+social-science panel, mapping each to a concrete change, and surviving the re-review while keeping mutual anonymity (plus the short factual-correction rebuttal FAccT 2026 ran before its first decision).
---

# FAccT Author Response

Use this after FAccT reviews are released. In **FAccT 2027** there is **one speaking turn**: if you
receive a **Revise (major or minor)** decision on 22 December 2026, you submit the revised paper
**together with a rebuttal** by 28 January 2027, and both are **re-reviewed**. An Accept needs no
response; a Reject has no appeal. FAccT 2026 had **two** turns — a short pre-decision rebuttal for
factual corrections, then the revision — and the 2027 blog post explains that merging them ties the
response directly to the revised scholarship. Check which model the current cycle uses. Both must respect mutual anonymity: nothing
you write may reveal authors, institutions, field sites, or a repository owner.

## Triage (both turns)

- Answer what affects the decision: relevance and framing, correctness, depth of exposition, honest
  treatment of strengths **and** limitations, and — often decisive at FAccT — the reality of the
  harm and the care taken with affected people.
- Answer **each reviewer on the axis they raised**, including the out-of-field reviewer. A legal or
  qualitative objection is not noise to be waved off with a metric.
- Correct factual misreadings first; a reviewer who misread a subgroup table or a consent procedure
  is often persuadable.
- Keep every word anonymous — do not name your system's real name, your institution, your field
  site, your IRB, or a private repository, even to strengthen a point.

## The short pre-decision rebuttal (FAccT 2026 only; not in FAccT 2027)

If a cycle restores it: short and strictly for **factual corrections and misunderstandings**, plus signposting minor edits.
It is **not** a venue to re-argue substantive disagreement or to promise a new study — that is the
Revise round's job. Concede what is true, correct what is misread, and point to exactly where the
answer already lives in the submitted paper or supplementary material. Do not paste new results the
reviewers cannot verify in the current PDF.

## The Revise-round rebuttal (the distinctive FAccT move)

A Revise is a genuine revise-and-resubmit. The Area Chair's meta-review **summarizes and
prioritizes** the concerns; your job is to address that prioritized list in a revised paper of up
to **15 pages** (excluding references and endmatter) and a rebuttal explaining how. Final
calibration also involves the Senior Area Chairs. The response is a **change ledger**: for
every prioritized concern, either make the change and show it, or decline it with a reason.

```text
[AC.1] Prioritized concern (quoted briefly)
       -> Action: DONE  | added disaggregation by <group> (Table 3); reported the utility cost
       -> Where: §5.2, Table 3; analysis/rq2.ipynb (anonymized)
[AC.2] Prioritized concern (from the legal reviewer)
       -> Action: DONE  | corrected the doctrinal framing per §2; the "right" is now cited to <origin>
[AC.3] Prioritized concern
       -> Action: DECLINED (with reason) | the requested field study cannot be run in the window
          without re-consenting participants; added a bounded limitation instead (§6) and an
          Adverse Impacts note
```

The rule that turns a Revise into an acceptance: **no unaddressed prioritized concern.** A concern
that is neither done nor explicitly and reasonably declined is what the re-review punishes.

## Reviewer pushback patterns

| Pushback | What it signals | FAccT-ready response |
|---|---|---|
| "Results are aggregate; where is the subgroup harm?" | Disaggregation gap | Add per-group metrics with uncertainty; report the utility trade-off |
| "The proxy for the protected attribute is not valid" | Construct-validity doubt | Validate the proxy, report its error, bound the claim |
| "You speak for a community you did not study" | Standpoint/rigor objection | Add the community's data or scope the claim; note it in Positionality (at acceptance) |
| "The legal claim misreads the doctrine" | Cross-lane correctness | Fix the framing, cite the doctrine correctly, or narrow the legal claim |
| "This could be misused to justify deployment" | Adverse-impact concern | Strengthen the Adverse Impacts statement and the paper's caveats |

## Anonymity in the response (easy to slip)

- Refer to your own prior work in the third person, as in the paper.
- Describe changes to released code/data without linking to an identity-revealing repository; use
  the anonymized location.
- Do not thank a named collaborator, partner organization, or funder inside the response, and do not
  reveal the field site.

## Calibration

- Respond to the criterion the reviewer actually raised, not the one you would rather defend.
- In 2027 the rebuttal *accompanies* the revision: let the changed paper carry the argument and
  use the rebuttal to point to it, not to re-argue.
- Length and format norms for the rebuttal are not published on the 2027 CFP or Author Guide, and
  the process changed between 2026 and 2027 — confirm the current OpenReview instructions before
  sending.

## Output format

```text
[Turn] Revise-round rebuttal + revised paper / (2026-style) short rebuttal
[Priority issue] <reviewer or AC concern>
[Decision dimension] relevance / correctness / depth / strengths-and-limits / harm-and-ethics / discipline
[Change ledger] <prioritized concern -> DONE/PARTIAL/DECLINED + where in paper/artifact>
[Anonymity check] <no identity leak, no field-site/positionality reveal: passed/issues>
```
