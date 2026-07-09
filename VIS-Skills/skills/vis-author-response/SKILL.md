---
name: vis-author-response
description: Use when drafting IEEE VIS author responses across the two-phase review, covering the first-round reviewer discussion, and — distinctively — the conditional-accept second-round revision with its summary-of-changes that maps every required change to a concrete edit and is re-read by the same primary, secondary, and external reviewers under the IEEE TVCG process.
---

# VIS Author Response

Use this after IEEE VIS reviews are released. VIS has **two distinct speaking turns**, and
conflating them is a common mistake: a first-round engagement with the reviewer discussion, and — if
you receive a **conditional accept** — a full **second-round revision** with a **summary of
changes** accompanying a revised paper that the original reviewers re-read against the required
changes. This is a journal-style revise-and-review, not a one-shot CVPR rebuttal.

## Triage (both turns)

- Answer what affects the decision: novelty, impact, whether the evidence supports the claims,
  methodology, encoding/interaction rationale, and reproducibility.
- Use evidence that already exists or that the revision will concretely add — never a vague promise
  to "consider" a study.
- Correct factual misreadings first; a reviewer who misread a figure or a task is often persuadable.
- If you submitted double-blind, keep every word anonymous through the first round — do not name your
  system, lab, grant, or a public repository even to strengthen a point.

## Turn 1 — the first-round engagement

VIS's first phase includes a **reviewer discussion**. Your first-round comments (where the cycle
allows author input before the decision) should be short and decision-focused: concede what is true,
correct what is misread, and point to exactly where the answer already lives in the paper or the
supplemental video/code. Do not smuggle in new results the reviewers cannot verify. The goal is to
move the paper from "reject" toward "conditional accept" by removing correctable misunderstandings.

## Turn 2 — the conditional-accept revision (the distinctive VIS move)

A conditional accept comes with a list of **required changes**. The revision is judged on whether
you met them. The **summary of changes** is a change ledger: for every required change, either make
it and show where, or justify declining it with a reason.

```text
[R1.1] Required change (quoted briefly)
       -> Action: DONE  | added the within-subjects study (§6.2), Fig. 7, effect sizes + CIs
       -> Where: §6.2, Fig. 7; supplemental/analysis/study2.ipynb
[R2.1] Required change
       -> Action: DONE  | rewrote the encoding-rationale (§4.1) to tie each channel to a task
       -> Where: §4.1, Table 2
[R1.2] Required change
       -> Action: JUSTIFIED DECLINE | the requested 3D condition contradicts the task's
          occlusion constraint; added a scoping sentence + threat instead (§8)
[R3.1] Required change
       -> Action: PARTIAL | added the perceptual pilot; the full longitudinal deployment is
          out of scope for the revision window and is noted as future work (§9)
```

The rule that turns a conditional accept into an acceptance: **no silent omissions.** A required
change that is neither made nor explicitly justified as declined is what the second read punishes.

## Reviewer pushback patterns (visualization-specific)

| Pushback | What it signals | VIS-ready response |
|---|---|---|
| "Why this encoding rather than a standard chart?" | Design-rationale gap | Add a task-to-channel justification; compare against the conventional baseline |
| "The evaluation does not match the contribution" | Method mismatch | Add the evidence the contribution type needs (study for a claim about people; benchmark for a technique) |
| "Is this better than [existing tool/technique]?" | Novelty/delta doubt | Add the comparison or a scoped delta sentence naming what is new |
| "The user study is underpowered / confounded" | Conclusion-validity objection | Report power/effect sizes; add participants or bound the claim |
| "The system/results are not reproducible" | Open-practices gap | Release anonymized code/data; describe the reproduction path and target the Replicability Stamp |
| "Color/perception choices are not accessible" | Perceptual-validity concern | Justify the palette (CVD-safe, luminance); cite the perceptual basis |

## Anonymity in the response (when submitted double-blind)

- Refer to your own prior work in the third person, as in the paper.
- Describe system/artifact changes without linking to an identity-revealing repository or demo; use
  the anonymized location until the paper is accepted.
- Do not thank a named collaborator or funder inside a first-round response.

## Calibration

- Respond to the criterion the reviewer actually raised, not the one you would rather defend.
- The revised paper — not the summary of changes — carries the argument; the summary is a map from
  required change to edit.
- Length and format norms for both turns vary by cycle; confirm the current instructions and the
  second-round timeline before writing.

## Output format

```text
[Turn] first-round engagement / conditional-accept revision
[Priority issue] <reviewer concern>
[Decision dimension] novelty / impact / evidence / methodology / encoding rationale / reproducibility
[Change ledger] <required change -> DONE/PARTIAL/JUSTIFIED-DECLINE + where in paper/supplemental>
[Anonymity check] <if double-blind: no identity leak in the response: passed/issues>
```
