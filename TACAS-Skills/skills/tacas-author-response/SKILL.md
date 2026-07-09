---
name: tacas-author-response
description: Use when drafting a TACAS (ETAPS) author response for the rebuttal window, covering the short single-round rebuttal, answering soundness and benchmark-fairness objections with checkable evidence, addressing artifact concerns for tool papers, respecting the per-category blind model when it applies, and reading which objections a rebuttal can and cannot move.
---

# TACAS Author Response

Use this after TACAS reviews are released in the **rebuttal window**. TACAS has **one speaking
turn**: a short, targeted author response before the PC finalizes decisions — not a journal-style
revise-and-resubmit. The job is to correct misreadings and supply the one or two checkable facts
that move a borderline paper, not to rewrite the paper.

## Triage

- Answer what affects the decision: **soundness** of the algorithm, **fairness and reproducibility**
  of the evaluation, **artifact** function (for tool papers), correctness of a proof step, and
  genuine misreadings.
- Use evidence that already exists in the submitted paper or artifact, or a number you can state
  now — never a vague promise of future work.
- Correct factual misreadings first; a reviewer who misread a theorem or a benchmark table is often
  persuadable.
- Respect anonymity **where it applies**: for a **double-blind research** paper the rebuttal must not
  reveal authors, institutions, tool identity, or a repository owner; for a **single-blind tool /
  case-study** paper this constraint does not apply.

## The rebuttal shape

Short and decision-focused. One or two decision-critical points per reviewer beats an exhaustive
reply. Concede what is true, correct what is misread, and point to exactly where the answer lives in
the submitted paper or artifact. Do not paste large new results the reviewers cannot verify in the
window.

```text
[R1.1] Reviewer concern (quoted briefly)
       -> Response: the soundness objection assumes X; Theorem 1 handles it via Y (see §3.2)
       -> Evidence: already in the submitted proof / artifact script reproduce/rq1.sh
[R2.1] Reviewer concern
       -> Response: the baseline was configured with an equal 900s timeout on the same machine
          (§4.1); the per-category table shows the comparison is fair, not cherry-picked
[R3.1] Reviewer concern (artifact)
       -> Response: the artifact builds offline on the VM; the smoke run is `smoke.sh`; we will
          clarify the one missing dependency note in the README
```

## Reviewer pushback patterns

| Pushback | What it signals | TACAS-ready response |
|---|---|---|
| "Is this actually sound?" | Correctness doubt | Point to the theorem/argument; note any validation (witness/cross-tool) already done |
| "The baseline is not fair / not the latest" | Comparison doubt | State the version, timeout, and hardware; if truly unfair, concede and scope the claim |
| "Results are not reproducible" | Verifiability gap | Point to the artifact scripts and the clean-VM smoke run; fix a doc gap you can name |
| "The artifact did not build" (tool paper) | Mandatory-artifact failure | Identify the concrete cause; if fixable in the window per the rules, say exactly how |
| "Overlaps prior tool/algorithm X" | Novelty doubt | Sharpen the one-sentence delta; name the capability/guarantee X lacks |
| "Only one benchmark family" | External-validity limit | Point to other categories evaluated, or scope the claim and name the limit |

## What a rebuttal can and cannot move

- **Can move:** a misread proof, a baseline the reviewer thought was untuned but was not, a "not
  reproducible" that a pointer to the right script resolves, a novelty doubt a crisp delta answers.
- **Cannot move:** a genuinely broken artifact for a tool paper, an unsound core, an evaluation that
  really is cherry-picked. Do not argue taste; the PC discussion decides, and your response is
  evidence for an advocate, not a closing argument.

## Anonymity check (research papers only)

- Refer to your own prior work in the third person, as in the paper.
- Do not name your tool's identifying name, institution, grant, or a private repository in the
  response.
- For a single-blind tool/case-study paper, none of this applies — answer plainly.

## Calibration

- The rebuttal is short and single-round; do not treat it as a revision.
- Length and format norms vary by cycle; confirm the current ETAPS instructions before sending.
- Answer the criterion the reviewer actually raised (soundness vs fairness vs artifact), not the one
  you would rather defend.

## Output format

```text
[Rebuttal focus] soundness / benchmark-fairness / reproducibility / artifact / novelty
[Category + blind mode] research (anonymous rebuttal) / tool|case-study (named)
[Point ledger] <reviewer concern -> response -> where the evidence already lives>
[Concessions] <what you concede + how you scope the claim>
[Anonymity check] (research only) <no identity leak in the response: passed/issues>
```
