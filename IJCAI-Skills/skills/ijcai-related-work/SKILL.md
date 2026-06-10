---
name: ijcai-related-work
description: Use when positioning an IJCAI or IJCAI-ECAI submission against archival AI literature, arXiv preprints, workshop papers, prior rejected versions, dual-submission rules, shortened prior versions, and resubmission-information requirements.
---

# IJCAI Related Work

Use this to audit novelty, prior work, and submission eligibility. Reopen the current CFP and
submissions FAQ because resubmission and dual-submission rules are policy-sensitive.

## Positioning checks

- Distinguish non-archival workshop or poster versions from formally published proceedings
  with DOI, ISBN, or ISSN.
- If the paper was rejected by another peer-reviewed conference in the last 12 months,
  prepare the required anonymized rejected version and reviews; the response cover letter may
  be optional depending on current rules.
- Cite author preprints and prior work in third person. A non-anonymous arXiv version may be
  allowed, but the IJCAI submission itself must remain anonymous.
- Do not submit a paper that is under review, accepted, or published at another formal
  archival venue during the IJCAI review period.
- If a substantially shorter extended abstract, poster, or position paper exists, declare it
  when current rules require and explain the new technical content.
- Make the related-work section decision-useful: closest competing claims, why they are
  insufficient, and exactly what is new here.

## Positioning across IJCAI's breadth

Because IJCAI spans symbolic AI, search, planning, KR, constraint reasoning, multi-agent, game
theory, ML, NLP, and vision, the closest prior work may live in a different subcommunity than
the authors'. A reviewer from that adjacent area will know the literature you skipped.

| Prior-work source | Eligibility/anonymity handling | Positioning duty |
| --- | --- | --- |
| Archival proceedings (DOI/ISBN/ISSN) | Cite normally; counts as published | Distinguish your claim from it |
| Non-archival workshop/poster | Usually citable, not a dual-submission bar | Declare if a shorter prior version |
| Author arXiv preprint | Non-anonymous arXiv may be allowed; submission stays anonymous | Cite in third person |
| Recent rejected version (≤12 months) | Prepare anonymized rejected version and reviews | Disclose per current rules |
| Concurrent archival submission | Not permitted during the review period | Resolve before upload |

## Worked vignette: a search paper missing an adjacent baseline

A bidirectional-search paper cites only recent search venues and omits a closely related
planning-community result. An IJCAI planning reviewer flags the gap as a novelty threat. Fix:
add the planning result to the closest-works set, state precisely why it does not subsume the
new bound, and write a one-sentence novelty contrast a non-search reviewer can verify. If the
paper is a shortened version of a prior workshop poster, declare that and describe the added
technical content.

## Reviewer pushback and the venue-specific fix

- "Missed obvious prior art." Search the adjacent subfield, not just your home venue, since
  IJCAI reviewers cross subcommunities.
- "Looks like double submission." Confirm no concurrent archival submission and prepare the
  resubmission package if a recent rejection exists.
- "Related work is a list, not an argument." Convert it to closest claims, why insufficient, and
  what is new.

## Output format

```text
[Eligibility] clear / needs declaration / risky
[Closest works] <3-5 items and distinction>
[Resubmission package] <needed/not needed/unknown>
[Dual-submission risk] <none/issues>
[Novelty sentence] <IJCAI-ready contribution contrast>
```
