---
name: kdd-author-response
description: Use when drafting KDD rebuttals on OpenReview, where authors answer each review under a no-hyperlink rule, cannot upload revisions, and write for the area chair who recommends Accept, Reject, or Resubmit. Covers evidence-anchoring without links, per-reviewer triage, and turning a likely Resubmit into next-cycle material at ACM SIGKDD.
---

# KDD Author Response

Use this when KDD reviews land. The structural facts that shape every rebuttal here:
authors get a chance to respond to **each review**; the area chair reads the responses
plus the reviewer discussion and recommends; the PC chairs decide; and the decision
space includes **Resubmit**, not just accept/reject. Confirm the current cycle's exact
rebuttal window and length limits on OpenReview before drafting — mechanics move
between cycles.

## The no-links constraint

KDD 2026 forbade hyperlinks in rebuttals and discussion. Practical consequences:

- You cannot introduce a new repository, demo, or anonymous site now. The only
  artifact reviewers can check is whatever the submitted PDF already references.
- Point with coordinates instead: "Table 3, column 4", "Section 5.2, lines 412-419"
  (the `review` option's line numbers exist precisely for this), "Appendix B,
  Algorithm 2", "README section 'Repro' of the repository cited in Section 6".
- New numbers may be typed into the response as plain text tables if the cycle's rules
  allow new experimental results at all — check before running anything.

## Per-reviewer triage

Sort every reviewer point into one of four bins before writing a word:

| Bin | Example at KDD | Response move |
|---|---|---|
| Factual misread | "No ablation for the drift module" when Table 5 is that ablation | Correct politely with exact coordinates; this is the cheapest score repair available |
| Missing-baseline demand | "Compare against the latest graph transformer" | Run it if rules and time permit and report as text; otherwise explain the regime mismatch concretely |
| Scale skepticism | "Would this hold beyond the 10M-edge graphs tested?" | Cite the complexity analysis plus the largest reported run; concede the untested regime explicitly |
| Scope objection | "This is engineering, not research" (or, on ADS: "no deployment evidence") | Restate the contribution as mechanism + regime; for ADS point to the post-launch metrics section |

Answer the area chair, not the loudest reviewer: one resolved decision-critical
objection moves a recommendation more than five resolved nitpicks.

## Drafting pattern per review

```text
R<k>, thank you for the careful read. We respond to your main concerns:

[W1 - <reviewer's phrase>] <one-sentence answer>.
Evidence: Section X.Y / Table N / Appendix Z (submitted version).
<If conceded:> This is correct; we will scope the claim in the final version to <...>.

[W2 - ...] ...

Summary: the decision-relevant points are W1 (misread, resolved by Table N) and
W3 (new run reported above as plain text). We believe W2 is a presentation fix
we commit to for the final version.
```

Keep each response self-contained; area chairs skim per-review threads independently.

## Playing for Resubmit when Accept is out of reach

Unique to KDD's dual-cycle system: a rebuttal that will not rescue acceptance can
still set up a strong next-cycle resubmission, because the Resubmit path expects the
noted concerns to be addressed and rewards papers that address them.

- Concede precisely. A concession recorded in this cycle's thread becomes the first
  line of the next cycle's mandatory one-page change summary.
- Ask for actionability: if a reviewer's objection is vague, a polite request to name
  the missing experiment gives the resubmission a concrete target.
- Never burn the thread. The resubmission declares the previous forum id, so hostile
  rebuttal text travels with the paper into the next cycle.

## Tone calibration for this venue

- KDD reviewer pools mix academic miners with industry practitioners; answer
  efficiency and deployment questions with numbers, not with "left to future work".
- Do not promise camera-ready experiments you have not run — ACs discount unbacked
  promises, and the Resubmit option means "come back when it exists" is a real outcome.
- Confidentiality and anonymity still bind: no identity hints, no "as our production
  system at <company>" phrasing in Research Track responses.

## Worked micro-exchange

Reviewer 2 (practitioner lens) writes: "The 12% lift over the baseline likely comes
from the extra embedding table, not the proposed propagation rule. Also, results on
the industrial dataset cannot be verified." A response that moves the AC:

1. **Attribute with the ablation**: "The variant `-propagation` in Table 5 keeps the
   embedding table and removes only the propagation rule; the lift drops from 12% to
   3%, isolating the rule's contribution (Section 5.3, lines 512-528)."
2. **Convert the verification complaint into a specification answer**: "The
   industrial dataset cannot be released, but Section 4.1 specifies schema, size
   (1.9B interactions), and collection window, and all pipeline code runs on the
   public datasets in the repository cited in Section 6."
3. **Concede the residue**: "We agree the 3% residual on public data is smaller than
   the industrial figure and will state this asymmetry explicitly in the final
   version."

Three moves, three sentences each, zero links — and each maps a review objection to
submitted evidence or a bounded commitment.

## Rebuttal-window logistics

- Draft against the clock: per-review responses for a 3-4 reviewer packet under a
  length limit take a full author-day; two for papers with new runs. Reserve the
  capacity when reviews are announced, not when they arrive (`kdd-workflow`).
- One author owns tone-consistency across all responses; reviewers compare notes in
  discussion, and contradictory answers to R1 and R3 are visible to the AC.
- Character/word limits per response box vary by cycle (待核实) — measure before
  writing, since cutting a finished response degrades it more than planning short.
- After submitting responses, monitor the forum if the cycle allows follow-up
  discussion; an unanswered reviewer follow-up in the closing days reads as
  abandonment.

## Output format

```text
[Rebuttal stance] repair-for-accept / stabilize-borderline / build-for-resubmit
[Per-reviewer bins] R1: <bin>, R2: <bin>, R3: <bin>
[Decision-critical point] <the one objection the AC will weigh>
[Evidence anchors] <section/table/line coordinates only - no links>
[Concessions recorded] <items that feed a Cycle-2 change summary>
[Forbidden content check] links: none / identity: clean / unbacked promises: none
```
