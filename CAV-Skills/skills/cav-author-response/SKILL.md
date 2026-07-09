---
name: cav-author-response
description: Use when drafting a CAV (Computer Aided Verification) author response (rebuttal) for a paper that has passed the two-stage review's first filter, covering how to answer soundness/proof objections, benchmark-fairness challenges, and novelty-delta doubts with verifiable evidence while preserving double-anonymity for Regular and Application papers.
---

# CAV Author Response

Use this after CAV stage-2 reviews are released. At CAV the rebuttal exists **only for papers that
passed the stage-1 filter** — the two-stage process means a rejected paper never reaches this turn.
So the rebuttal is a focused instrument: answer what the two additional reviewers, and the two from
stage 1, need in order to advocate for the paper in the PC discussion. For Regular and Application
papers, the response must respect double-anonymity — do not reveal authors, the tool's real name, or
identity-revealing repositories.

## Triage

- Answer what affects the decision: **soundness of the theorem/proof**, **fairness and
  reproducibility of the benchmarks**, **novelty/delta** against prior verification work, scope, and
  clarity.
- Use evidence that already exists in the submission or that you can state precisely — a proof step,
  a number already in a table, a benchmark-configuration clarification. Do **not** promise unrun
  experiments as if they were results.
- Correct factual misreadings first; a reviewer who misread a theorem's assumption or a benchmark
  subset is often persuadable.
- Keep every word anonymous for anonymized categories. (Tool and Industrial papers are not
  double-blind, so this constraint relaxes — but still avoid gratuitous self-promotion.)

## The verification rebuttal, point by point

Treat the response as a **claim ledger**: for each reviewer concern, either resolve it with concrete
evidence or explain precisely why the concern does not apply.

```text
[R1.1] "The soundness proof assumes X, which fails for unbounded inputs."
       -> Response: X is not assumed; Lemma 2 holds for unbounded inputs (the bound is only on
          the encoding width, §3.2). Pointer: §3.2, Lemma 2.
[R2.1] "The baseline solver was not the latest version / not tuned."
       -> Response: baseline is vA.B (latest release at submission); we used its default portfolio
          as recommended in its README; per-instance data in the artifact confirms parity of limits.
[R2.2] "Novelty over <prior technique> is unclear."
       -> Response: prior technique shares lemmas only propositionally; ours admits theory lemmas
          under a re-derivation check (the soundness contribution), see §3.3 and Table 2.
```

The rule that turns a stage-2 paper into an acceptance: **answer the axis the reviewer raised, with
something they can verify** — a section pointer, a proof step, or a benchmark fact — not a promise.

## Reviewer pushback patterns

| Pushback | What it signals | CAV-ready response |
|---|---|---|
| "The soundness argument is incomplete" | Correctness doubt | Point to the exact lemma/assumption, or concede and scope the claim |
| "The baseline is outdated or untuned" | Evaluation-fairness doubt | Name the version and configuration; show equal resource limits from the artifact |
| "Only easy/self-selected benchmarks" | External-validity limit | Point to the standard set/revision used; state the class not covered as a limit |
| "Delta over prior work X is thin" | Novelty doubt | Name the precise technical difference (what X cannot do that you do) |
| "The tool did not build / is missing" | Reproducibility gap | Clarify the build path; note the artifact plan (AEC is post-acceptance) |
| "Claim generality is over-stated" | Scope objection | Narrow the claim in the response and promise the camera-ready scoping edit |

## Anonymity in the response (anonymized categories)

- Refer to your own prior work in the third person, as in the paper.
- Describe tool/benchmark changes without naming the real tool or linking an identity-revealing
  repository; use the anonymized location.
- Do not thank a named collaborator or funder inside the response.

## Calibration

- Respond to the criterion the reviewer actually raised, not the one you would rather defend.
- Length and format norms for the response vary by cycle; confirm the current instructions and the
  word/character limit before sending.
- The PC discussion decides; write the response as evidence for an advocate, and let the paper — not
  the rebuttal — carry the argument.

## Output format

```text
[Turn] stage-2 rebuttal (only for papers past the stage-1 filter)
[Priority issue] <reviewer concern>
[Decision dimension] soundness/proof / benchmark-fairness / novelty / scope / clarity / tool
[Claim ledger] <concern -> resolved with (proof step / number / pointer) or scoped>
[Anonymity check] <no identity leak for Regular/Application: passed/issues>
```
