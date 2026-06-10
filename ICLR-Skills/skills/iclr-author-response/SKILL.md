---
name: iclr-author-response
description: Use when drafting ICLR OpenReview author discussion replies, revision notes, public comments, restricted comments, and responses to reviewer or AC concerns during the discussion period. Use when reviews land and you must decide what to answer publicly versus privately, how to log a discussion-period revision, or how to move a borderline score before the AC writes the meta-review for the permanent record.
---

# ICLR Author Response

Use this after ICLR reviews arrive. ICLR discussion is not just a static rebuttal: authors can
answer reviewers, clarify misunderstandings, make visible revisions when allowed, and help the AC
evaluate whether concerns are resolved.

## Response strategy

- Separate public comments from restricted comments to reviewers, ACs, or PCs according to the
  current OpenReview permissions.
- Lead with decision-relevant points: correctness, novelty, empirical adequacy, clarity,
  reproducibility, ethics, and community value.
- When uploading a revision during discussion, summarize the exact changes and give a compact diff
  map. Do not assume reviewers or ACs will re-read the full PDF.
- Keep identity hidden. Do not reveal lab, institution, funding, private repository ownership, or
  author-controlled analytics.
- Use private links only when the Author Guide permits them and only for the intended reviewers/ACs.
- Escalate low-quality, abusive, or suspected LLM-generated reviews through the official confidential
  channel rather than arguing publicly.

## Reply pattern

1. State the reviewer concern in one sentence.
2. Provide the correction, evidence, or concession.
3. Point to the original paper, appendix, supplementary material, or newly uploaded revision.
4. Say what has changed and why it is within discussion-period rules.
5. Close with a specific invitation for the reviewer or AC to verify the fix.

## Public-forever calibration

Every word you post on OpenReview is visible permanently and to people far beyond this reviewer:
future readers, citers, and program committees. Tone and precision are part of the record.

| Situation | ICLR-tuned move | Avoid |
| --- | --- | --- |
| Reviewer misread a claim | Quote the sentence, point to a revision | Calling the review careless |
| Reviewer wants an ablation | Run it, post the table, upload a revision | "In the final version", no evidence |
| Score seems unmovable | Address the AC-relevant objection, not the digit | Re-arguing minor points |
| Abusive or LLM-written review | Flag confidentially to the AC/PC | Public accusation |

## Worked vignette

A paper introduces an LLM fine-tuning recipe and reports reasoning gains. A public review says the
gains "probably come from extra training tokens, not the method." Instead of debating, the authors
post an inline compute-matched control showing the lift persists, upload a revision adding it as
Table 4, and reply with a two-line diff map. The AC, reading the public thread, sees a concrete
resolution, and the reviewer raises the score in an updated review that also stays public.

## Pushback patterns and fixes

- "Concurrent arXiv work already does this." Acknowledge it, state the dated distinction, add a
  related-work sentence rather than disputing priority.
- "Numbers changed between versions." Explain the corrected bug or seed in the changelog.
- "Rebuttal is too long." Lead each reply with the decision-relevant point; ACs skim threads.

## Output format

```text
[Audience] public / reviewer-only / AC-only / PC escalation
[Decision issue] correctness / novelty / experiments / clarity / ethics / reproducibility
[Reply] <anonymous OpenReview-ready text>
[Revision pointer] <section/table/appendix/file/link>
[Risk note] <whether this should stay public or restricted>
```

