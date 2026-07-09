---
name: ase-author-response
description: Use when drafting ASE (IEEE/ACM Automated Software Engineering) author responses, covering the double-anonymous rebuttal that must first survive the early-rejection gate and — distinctively — the criteria-bound revision-round summary-of-changes that maps every stated revision criterion to a concrete change and is re-checked against those criteria.
---

# ASE Author Response

Use this after ASE reviews are released. ASE has **two distinct speaking turns**, and conflating
them is a common mistake: a short **rebuttal** (for papers that survive the early-rejection gate),
and — if you receive a **Revision** — a **summary-of-changes** accompanying a revised paper that is
re-checked against the reviewers' explicitly stated criteria. Both must respect double-anonymity:
no author names, institutions, or revealed repository ownership, even to strengthen a point.

## Triage (both turns)

- Answer what affects the decision: significance and soundness of the automation, evaluation quality
  on real subjects, threats to validity, clarity, and the Data Availability / artifact posture.
- Use evidence that already exists or that the revision will concretely add — never a vague promise.
- Correct factual misreadings first; a reviewer who misread your tool's configuration or a table is
  often persuadable.
- Keep every word anonymous. Do not name your tool's real name, institution, grant, or a private
  repository.

## Turn 1 — the rebuttal (only if you survived early rejection)

If your paper reached the rebuttal stage, at least one reviewer saw value; a uniformly negative set
would have been early-rejected. So the rebuttal's job is narrow: **move the borderline reviewer**.

- Short and decision-focused. One decision-critical point per reviewer beats an exhaustive reply.
- Concede what is true, correct what is misread, and point to exactly where the answer lives in the
  submitted paper or artifact.
- Do not paste large new results the reviewers cannot verify; if a small, checkable number answers a
  direct question ("what is the runtime overhead?"), give it.
- Signal what you *would* do in a revision, because Revision is a live outcome — but do not promise a
  redesign you cannot deliver in the window.

## Turn 2 — the revision summary-of-changes (the distinctive ASE move)

A Revision is criteria-bound: the reviewers wrote **concrete, actionable criteria** and agreed to
accept in principle if they are met. The summary-of-changes is a **criterion ledger**: for every
stated criterion, either meet it and show where, or explain precisely why it is infeasible and what
you did instead.

```text
[C1] Criterion (quoted): "Add a comparison against tool X on the same subjects."
     -> Action: DONE  | added §5.3, Table 4: X run with an equal, documented budget on all 90 subjects
     -> Where: §5.3, Table 4; artifact/eval/compare_X.sh
[C2] Criterion: "Report an ablation isolating the learned component."
     -> Action: DONE  | §5.4, Table 5 replaces learned templates with static rewrites
[C3] Criterion: "Evaluate on an industrial code base."
     -> Action: INFEASIBLE (with reason) | no license to redistribute proprietary subjects; added
        an open large-scale subject instead (§5.5) and noted the residual external-validity threat
```

The rule that turns a Revision into an acceptance: **address every criterion.** A criterion that is
neither met nor explicitly and reasonably addressed is what the re-check punishes — the discussion
lead maps your summary-of-changes back onto the criteria one by one.

## Reviewer pushback patterns (automated-SE flavored)

| Pushback | What it signals | ASE-ready response |
|---|---|---|
| "The baseline tool is not tuned/fair" | Soundness doubt about the comparison | Re-run with an equal, documented budget; report new numbers, or justify the setup |
| "Evaluated only on toy or self-selected subjects" | External-validity limit | Add real subject systems, or scope the claim and name the threat |
| "The improvement is the model, not your design" | Model-as-contribution doubt | Add the ablation isolating the automation from the model; report marginal value |
| "The tool/artifact does not run" | Reproducibility / availability gap | Fix and re-anonymize; describe the run path and re-execution oracle in the response |
| "Overlaps prior automation X" | Novelty/delta doubt | Sharpen the delta sentence; add the missing head-to-head comparison |

## Anonymity in the response (easy to slip)

- Refer to your own prior work in the third person, as in the paper.
- Describe tool/artifact changes without linking to an identity-revealing repository; use the
  anonymized location.
- Do not thank a named collaborator or funder inside the response or the summary-of-changes.

## Calibration

- Respond to the criterion the reviewer actually raised, not the one you would rather defend.
- Length and format norms for both turns vary by cycle; confirm the current instructions before
  sending.
- The PC discussion (and, for a Revision, the re-check against the stated criteria) decides; write
  the response as evidence for an advocate, and make the revised paper — not the letter — carry the
  argument.

## Output format

```text
[Turn] rebuttal / revision summary-of-changes
[Priority issue] <reviewer concern or stated criterion>
[Decision dimension] significance / soundness / evaluation / threats / clarity / data-availability
[Criterion ledger] <criterion -> DONE/PARTIAL/INFEASIBLE + where in paper/artifact>
[Anonymity check] <no identity leak in the response: passed/issues>
```
