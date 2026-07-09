---
name: icdt-author-response
description: Use when responding to ICDT (International Conference on Database Theory) referees — principally the first-cycle Revise-and-resubmit round, where you return a corrected paper that closes each identified proof gap, plus any short author-comment phase, keeping the response anonymous and mapping every referee point to a concrete change in the revised PDF.
---

# ICDT Author Response

Write the response for a venue where the referees **checked your proofs**. ICDT's central
author-interaction mechanism is the **Cycle-1 Revise-and-resubmit**: not a short rebuttal that
argues taste, but a returned paper in which each gap the referees named has been *closed* and the
change documented. The second read is done by the same referees; a point raised and not addressed is
what turns a revision into a reject.

> Confirm the exact interaction model for the live cycle: ICDT's primary lever is the revision;
> whether a separate short rebuttal/author-comment phase runs in a given edition is **待核实** —
> read the current call. The advice below applies to the revision and, where one exists, to a brief
> comment phase.

## Triage the referee points first

Sort every point by kind, because the fix differs:

| Point kind | Example | Response |
|---|---|---|
| Correctness gap | "The proof of Lemma 4 omits the cyclic case" | Fix it in the paper; show the added case; this is top priority |
| Missing bound | "Only the upper bound is proved" | Prove the matching lower bound or scope the claim honestly |
| Model ambiguity | "Is this data or combined complexity?" | Pin the model in the body; correct any statement that was ambiguous |
| Positioning | "How does this differ from [PODS year]?" | Add the precise delta to related work (icdt-related-work) |
| Clarity | "Definition 2 is hard to parse" | Rewrite; a confused referee re-reads the revision |
| Genuine misreading | The referee misunderstood a quantifier | Correct it *and* fix the prose that allowed the misreading |

Correctness first, then bounds, then model, then clarity and positioning.

## Write the revision, not a debate

- **Close the gap in the paper**, then point to where: "Lemma 4 now covers the cyclic case
  (Appendix A, para 3)." The change lives in the PDF; the response is a map to it.
- **Prefer a fix over an argument.** "We prove the missing lower bound in the new Section 5" beats
  "we believe the lower bound is not essential."
- **Where you decline a request, say why, technically.** "A matching lower bound would require
  resolving [open problem]; we instead scope the claim to [restricted class] (Theorem 3)." An
  explicit, reasoned decline is respected; a silent omission is not.
- **Never argue taste.** "We think the model is natural" moves nothing; a referee who found a gap
  wants it closed, not defended.

## Anonymity in the response (since 2024)

The regular track is anonymous through review, so the revised paper and any response text must not
de-anonymize you:

- No author names, no "our prior work," no acknowledgments reintroduced in the revision.
- Do not add an arXiv/full-version link that names you into the revised PDF.
- Keep self-citations third-person in the revised text (see `icdt-related-work`).

## A point-by-point skeleton for the revision letter

```text
Summary: what changed at the top level (e.g., "added the matching lower bound; fixed the cyclic
         case in Lemma 4; clarified the complexity measure throughout").

R1.1 [correctness] "Lemma 4 omits the cyclic case."
     -> Fixed. The cyclic case is now handled in Lemma 4, with the argument in Appendix A.
R1.2 [bound] "Only an upper bound is shown."
     -> Added. Theorem 5 now proves a matching lower bound by reduction from <problem>.
R2.1 [model] "Data or combined complexity?"
     -> Clarified. The bound is combined complexity; stated explicitly in Section 3 and the abstract.
R2.2 [positioning] "Relation to [X, PODS year]?"
     -> Added to Related Work: their result is the special case of bounded arity; ours removes it.
```

## The cross-cycle rule (do not misuse the response)

If your paper was **rejected** in Cycle 1 (not invited to revise), a response cannot resurrect it,
and you **may not resubmit to Cycle 2 unless the referees explicitly invited it**. Reroute instead
(`icdt-topic-selection`). The response letter belongs to the *revision* path, not the reject path.

## Output format

```text
[Interaction type] Cycle-1 revision / short comment phase / na (rejected)
[Point triage] correctness / bound / model / positioning / clarity, each -> concrete change
[Changes made] <list of paper edits with locations>
[Declines] <each declined request + technical reason>
[Anonymity] revised PDF and letter non-identifying? yes/no
```
