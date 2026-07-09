---
name: mobicom-supplementary
description: Use when deciding what goes in the MobiCom 12-page double-column body versus references, optional appendices, and HotCRP fields — placing channel-model derivations, full protocols, and extended measurements outside the cap, keeping the contribution self-contained, and ensuring rebuttal and revision packets stay off the page count.
---

# MobiCom Supplementary Material

MobiCom gives you a hard **12 double-column pages including figures and tables**, with
**references and optional appendices (placed after the references) outside the cap**. The
skill is placement: what must a reviewer read to judge the contribution, and what can wait
in an appendix without hollowing out the body.

## The placement contract

| Content | Where it goes | Why |
|---|---|---|
| Mechanism, headline result, main figures | 12-page body | reviewers judge the contribution here |
| Channel-model derivation, proofs | appendix (after references) | needed for correctness, not for the argument's flow |
| Full protocol / state machine | appendix | body states the idea; appendix has the detail |
| Extended sweeps, extra conditions | appendix | supports, does not carry, the claim |
| Instrument/measurement setup detail | appendix | provenance, not narrative |
| All citations | references (outside cap) | never trimmed for space or anonymity |

The controlling rule: **the body must be self-contained enough to judge novelty and
correctness without the appendix.** An appendix strengthens; it must not be load-bearing.
Reviewers are not obligated to read appendices, so the strongest result cannot live only
there (`mobicom-writing-style`).

## What must stay in the body

- The mechanism, stated with its operating regime.
- At least one headline over-the-air result with its condition and uncertainty.
- The baseline comparison that supports the main claim.
- Enough method that a reviewer can see *why* the mechanism works.

If moving something to the appendix would make the body's argument incomplete, it stays —
find the page elsewhere by triaging a figure or tightening prose, not by shrinking geometry.

## HotCRP fields are part of the submission

The form is not an afterthought; reviewers meet it first:

```text
HotCRP submission fields to treat as content:
  title/abstract  -> verbatim-match the PDF (drift reads as sloppiness)
  topics          -> chosen for the reviewer sub-community you want (routing)
  authors/conflicts -> full list at abstract time for conflict computation
  optional fields -> artifact/ethics declarations per the current CFP (待核实 wording)
```

## Anonymity crosses the body/appendix line

An appendix is still part of the double-blind submission. A channel-model derivation that
names your testbed, a protocol listing with your repository URL, or a measurement appendix
with a site identifier de-anonymizes exactly as a body leak would. Run the blindness sweep
over the appendices too (`mobicom-submission`).

## Rebuttal and revision packets are separate

Do not confuse post-review material with submission supplementary material:

- The **rebuttal** is a bounded response entered after stage-2 reviews; it is not extra
  paper pages and has its own length limit (`mobicom-author-response`).
- A **one-shot revision** returns with a change-highlighted PDF and a change summary as
  auxiliary material — again outside the 12-page count and governed by the revision
  instructions, not the original CFP page rules (`mobicom-review-process`).

Neither is a place to smuggle content that should have been in the body; both are governed
by their own limits.

## Audit checklist

- [ ] Body self-contained: novelty and correctness judgeable without the appendix.
- [ ] Strongest result in the body, not only supplementary.
- [ ] Derivations/protocols/extended results in appendices after references.
- [ ] References complete and outside the cap; none trimmed for anonymity.
- [ ] Appendices passed through the blindness sweep.
- [ ] HotCRP title/abstract/topics/conflicts audited as content.
- [ ] Rebuttal/revision material kept off the page count and to its own limit.

## Output format

```text
[Body completeness] can the contribution be judged from the 12 pages alone? y/n
[Placement] content mis-shelved (body<->appendix) with the move
[References] complete + outside cap? y/n
[Anonymity] appendix leaks found
[HotCRP] fields needing attention
```
