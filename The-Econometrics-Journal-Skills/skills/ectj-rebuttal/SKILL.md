---
name: ectj-rebuttal
description: Use when drafting a The Econometrics Journal response letter and revision plan after a referee report, especially for assumptions, proofs, Monte Carlo evidence, empirical application, 20-page compression, resubmission timing, and replication-package conditions.
---

# EctJ Rebuttal

Use this after an EctJ decision letter. Reopen the decision letter, RES review-process page,
and current author instructions before setting deadlines.

## Response strategy

- Separate econometric-validity issues from exposition, simulation, application, and
  replication issues.
- Answer assumption and proof objections with exact theorem, lemma, or appendix changes.
- If a referee asks for broader treatment, decide whether it belongs in the printed paper,
  online supplement, or a clearly scoped limitation.
- Add Monte Carlo or empirical checks only when they resolve a decision-critical concern.
- Preserve compactness; an R&R that bloats beyond the EctJ page discipline can create a new
  conformance problem.
- Track the RES resubmission clock; the source map records normal windows of one month and
  sometimes three months.

## Revision triage

Classify each requested change before writing:

- **Validity-critical**: assumptions, theorem statements, proof gaps, estimator definition, simulation design.
  These must be fixed in the manuscript and cross-referenced in the response.
- **Applied-value-critical**: application too decorative, weak comparison, missing practical diagnostic. Add
  only the smallest table or paragraph that proves use value.
- **Compression-risk**: requests for extra cases, literature, or robustness that would break the printed-paper
  discipline. Move noncritical material to supplement or explain why it is outside scope.
- **Replication-risk**: code, seeds, data access, or package layout. Fix in the archive and cite the file path.

The response letter should show that the leading case is now stronger, not just longer.

## Response evidence rule

For every major comment, attach exactly one evidence object: theorem change, proof fix, simulation result,
application table, compression decision, or replication-file update. If a response has no evidence object,
it is probably only reassurance and should be strengthened before resubmission.

## EctJ pushback patterns and venue-specific fixes

| Referee pushback | What it signals at EctJ | Fix that closes it |
|---|---|---|
| "Asymptotic results carry no finite-sample evidence" | Theory-simulation contract broken | Add the one coverage or size panel that pairs with the contested theorem, summarized within the main-text page norm |
| "Simulation DGPs are detached from the empirical illustration" | Applied-value claim looks decorative | Re-anchor one DGP to parameters estimated from the application data and say so in the design preamble |
| "The leading case is too special to matter" | Scope guardrail read as a defect | Show the leading case covers the application class; add a remark stating what an extension would require |
| "Why is this proof only in the online appendix?" | Proof-placement conformance risk | Move the derivation into the printed appendix and re-verify the 20-page budget |
| "Code did not reproduce Table 3" | Replication credibility, decisive after conditional acceptance | Rerun the package, fix seeds or versions, cite the exact script in the response |

## Worked response fragment

Illustrative numbers: a referee writes that the proposed test's size is untrustworthy with few
clusters. A strong EctJ response does four things in four sentences: concede the gap ("the
original design only simulated 30 or more clusters"), report new evidence ("at 8 clusters the test
rejects 5.6% at nominal 5%, versus 12.9% for the incumbent; new Table 2, rows 1-2"), tie it to the
theorem ("consistent with Proposition 2's symmetric leading case"), and protect the page budget
("the full grid moved to Supplement S3"). Evidence, theorem, location — nothing else.

## Resubmission clock triage

- Map each validity-critical fix to the clock first: a new proof usually fits the normal
  one-month window, while a new simulation arm or application re-estimation often needs the
  longer window — ask the editorial office early rather than overrunning silently.
- Re-verify conformance after revising: added material at this venue can push the printed paper
  past the page norm and convert a scientific R&R into a format failure.
- If the decision letter touches the replication package, treat the rerun as part of the
  response, not as post-acceptance housekeeping.

## Output format

```text
[Decision] R&R / conditional acceptance / reject-resubmit / other
[Revision thesis] <one sentence>
[Major issues] <assumptions/proofs/simulations/application/replication>
[Response draft] <point-by-point structure>
[Compression guardrail] <what must not grow>
```
