---
name: issta-author-response
description: Use when drafting an ISSTA author response for the rebuttal window or planning a Major-Revision resubmission, covering evidence-anchored replies, the Accept/Major-Revision/Reject outcome model, converting reviewer asks into a revision ledger, anonymity in the response, and the difference between a rebuttal claim and a promised change.
---

# ISSTA Author Response

Use this after ISSTA reviews are released. ISSTA's response step feeds a decision that is not just
accept/reject: a first-round paper can be told to submit a **Major Revision**, so the response and
the revision plan are two connected artifacts. Reopen the current author-response and
major-revision instructions before drafting, because the dates and mechanics are cycle-specific.

## Triage

- Answer concerns that move the decision: soundness of the technique, fairness of the evaluation,
  scope of the claims, comparison to related work, and verifiability. Cosmetic complaints come last.
- Use submitted evidence — paper sections, tables, the artifact, threats-to-validity discussion.
  Do not promise experiments you have not run unless you can run them within a Major-Revision window.
- Keep the response anonymous. Do not reveal institution, tool name if it de-anonymizes, repository
  ownership, or grant numbers in the rebuttal text.
- Separate a **rebuttal correction** (the reviewer misread something already in the paper) from a
  **promised change** (something you will add). Label which is which so the meta-reviewer can weigh
  the paper as-is against the paper-if-revised.
- If the review budget is tight, spend it on the one objection that, unaddressed, sinks the paper —
  usually an evaluation-validity or missing-baseline concern.

## Drafting pattern

1. State the decision-critical correction or concession in the first line of each reply.
2. Point to the exact table, figure, section, or artifact path that already answers it.
3. Explain the consequence for the claim: what still holds, what you will scope down.
4. Promise only changes that fit the outcome — a camera-ready wording fix for an Accept-leaning
   paper, a concrete new experiment only if a Major-Revision window exists.

## Reviewer pushback patterns

| Pushback | What it signals | ISSTA-ready reply |
|---|---|---|
| "Evaluated only on your own subjects" | External-validity doubt | Point to the labelled benchmark and its provenance, or commit to adding an established one (Defects4J, real CVEs) in revision |
| "Baseline is not configured fairly" | Comparison-validity doubt | Cite the equal-budget setup, or concede and re-run the baseline under the reviewer's configuration |
| "Improvement is within noise" | Statistical-significance doubt | Reference the non-parametric test and effect size, or add repeated runs in revision |
| "Cannot tell if the artifact reproduces this" | Verifiability doubt | Point to the entry script and logged outputs, or fix the README before the artifact deadline |

## From reviews to a Major-Revision ledger

When the outcome is Major Revision, convert every review comment into a tracked row: the comment,
the change, where it lands in the paper, and its status. The resubmission's cover letter walks this
ledger; reviewers who see each of their points addressed in order revise upward.

```text
[R2.3] "No comparison to reversed-order rerunning."
  -> Added reversed-order baseline at equal budget; Table 2, rows 4-6. STATUS: done
[R1.1] "Shared-state model undefined for native calls."
  -> Scoped native state out explicitly; Section 3.1, threats. STATUS: done
[R3.2] "Overhead not reported."
  -> Added per-project overhead; Table 3. STATUS: in progress
```

## Discussion-phase calibration

- Reply precisely and early; ISSTA response windows are short and a focused rebuttal beats an
  exhaustive one.
- Never paste a whole new results section into the response box; summarize the finding and anchor it
  to submitted or clearly-promised material.
- Do not argue tone. Convert a hostile review into the technical objection underneath it and answer
  that.

## Output format

```text
[Priority issue] <reviewer concern>
[Decision dimension] soundness / evaluation / scope / related-work / verifiability
[Reply type] rebuttal correction / promised change
[Draft reply] <anonymous, evidence-anchored text>
[Evidence anchor] <table/figure/section/artifact path>
[Revision-ledger row] <comment -> change -> location -> status>
```
