---
name: iclr-author-response
description: Use when drafting ICLR OpenReview author discussion replies, revision notes, public comments, restricted comments, and responses to reviewer or AC concerns during the discussion period.
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

## Output format

```text
[Audience] public / reviewer-only / AC-only / PC escalation
[Decision issue] correctness / novelty / experiments / clarity / ethics / reproducibility
[Reply] <anonymous OpenReview-ready text>
[Revision pointer] <section/table/appendix/file/link>
[Risk note] <whether this should stay public or restricted>
```

