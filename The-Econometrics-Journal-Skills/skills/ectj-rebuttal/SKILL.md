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

## Output format

```text
[Decision] R&R / conditional acceptance / reject-resubmit / other
[Revision thesis] <one sentence>
[Major issues] <assumptions/proofs/simulations/application/replication>
[Response draft] <point-by-point structure>
[Compression guardrail] <what must not grow>
```
