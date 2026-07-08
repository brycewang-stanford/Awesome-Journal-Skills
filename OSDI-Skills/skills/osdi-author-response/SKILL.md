---
name: osdi-author-response
description: Use when handling author-side dialogue in an OSDI cycle — which in 2026 means no rebuttal at all: pre-empting objections inside the submission, then treating the conditional-accept shepherd exchange as the real author response, with a protocol for mandated revisions and for cycles that reinstate a response phase.
---

# OSDI Author Response

At most venues this skill would draft a rebuttal. At OSDI '26 there was **no
author-response period** (verified 2026-07-08) — a deliberate removal, since earlier
OSDI cycles had one. The author's voice therefore appears at exactly two points:
**before submission**, inside the paper, and **after a conditional accept**, in the
shepherding exchange. This skill covers both, plus the fallback if a future cycle
reinstates a response phase (待核实 each year — check the current CFP's process
section first, always).

## Phase 1: the rebuttal you write in advance

Since no clarification channel will exist between December and March, run a
**pre-mortem rebuttal** on the draft two to three weeks before the deadline:

1. Convene readers who did not build the system; have them write the three most
   damaging reviewer objections, in review language.
2. For each objection, classify: *misreading* (the text permits a wrong
   interpretation), *gap* (the evidence genuinely lacks it), or *disagreement*
   (a judgment call about scope or trade-offs).
3. Fix each in the only medium available — the paper: misreadings get rewritten
   prose; gaps get the experiment or an explicit, reasoned limitation statement;
   disagreements get their justification moved from your head into Section 2's
   why-alternatives-fail paragraph (`osdi-writing-style`).

The test of the fix: a sympathetic PC member should be able to answer the objection
in discussion **by quoting your paper**. You will not be in the room; your text is.

## Phase 2: shepherding is the author response

A conditional accept arrives with a PC-mandated change list and a shepherd who must
approve the final paper by June 9 — otherwise the paper is rejected from the program.
This is a response process with enforcement, and it rewards the same discipline a
rebuttal would:

| Rebuttal instinct | Shepherding translation |
|---|---|
| Answer every point | Build a change matrix: mandate → action → paper location → status |
| Be concise and factual | Short status notes to the shepherd; diffs and section pointers over essays |
| Don't relitigate scores | Don't relitigate the reviews — the decision is made; only the changes matter |
| New results need care | Mandated experiments get full `osdi-experiments` rigor on the frozen testbed |
| Deadline discipline | Front-load: first full revision to the shepherd weeks before June 9, not on it |

```text
change-matrix.md (shared with coauthors; mirrored in notes to the shepherd)
M1 "compare against X under skewed load"  -> new fig 9      -> §5.3 -> DONE
M2 "state the consistency model precisely"-> new §3.1 defs  -> §3.1 -> DRAFT
M3 "temper claims about portability"      -> rewrote claims -> §1,§7 -> DONE
open question -> shepherd (2026-04-14): does M1 require both skew levels?
```

Two rules of tone: the shepherd is the paper's ally and its gate simultaneously —
give them evidence to approve, never pressure to concede; and where a mandate seems
infeasible (hardware gone, trace unlicensable), raise it immediately with an
alternative, not in June with an apology.

## The shepherding calendar (2026 spacing)

The '26 cycle allowed roughly ten weeks from notification (March 26) to the final
paper (June 9), and the artifact deadline (May 8) lands in the middle of it. A
workable split for a conditional accept:

- **Week 1** — decode the mandate list with all coauthors; send the shepherd a scoped
  restatement of each mandate and get written confirmation of the interpretation.
- **Weeks 2–5** — mandated experiments on the frozen testbed; writing fixes in
  parallel; artifact packaging proceeds concurrently against the May deadline
  (`osdi-artifact-evaluation`) — the same person cannot do both in the same week, so
  split ownership explicitly.
- **Week 6** — full revised draft to the shepherd, change matrix attached; ask what
  is still short of approval rather than assuming silence means yes.
- **Weeks 7–9** — iterate; fold in the artifact appendix if the badge landed.
- **Week 10** — buffer. If the plan needs week 10 for content, it has already
  failed; week 10 absorbs compile problems and sign-off latency only.

## Phase 3: if a future cycle reinstates a response

OSDI has had responses before and could again. If the current CFP announces one,
apply the compressed classic form — and OSDI-specific emphases:

- Lead with the one clarification that changes a score, stated as fact-plus-pointer
  ("§4.2 already reports this; the number is 11%").
- Systems reviewers respect measurements over promises: if the window allows a small
  clarifying run on the frozen testbed, one number beats three paragraphs.
- Never claim results the PDF does not contain unless the cycle's rules explicitly
  permit new data — and say so if they do.
- Stay anonymous; response text is part of the double-blind record.

## When a mandate demands new experiments

Mandated runs are the highest-risk shepherding item because they can fail:

- Reproduce one submission-era result on the testbed *first*, to prove the frozen
  environment still matches the paper before adding anything new.
- Scope the run with the shepherd in numbers (which baseline, which scale points,
  which metric) before burning cluster weeks on an interpretation.
- If the new result *weakens* a claim, the move is to temper the claim in the final
  paper and tell the shepherd directly — shepherds exist precisely to certify that
  the published version is honest, and discovering the weakening later is worse for
  everyone.

## Failure modes

- Spending the silent window composing imaginary rebuttals instead of preparing the
  artifact and testbed for the two channels that do exist.
- Treating the shepherd's mandate list as an opening bid to negotiate down.
- Making mandated changes *only* in a letter, not in the paper — approval attaches
  to the June PDF.
- Assuming next cycle's process from this cycle's: the response's existence, format,
  and rules are annual variables at OSDI.

## Output format

```text
[Cycle process] response period this year? none / exists (source: current CFP; else 待核实)
[Phase] pre-submission pre-mortem / shepherding / reinstated-response
[If pre-mortem] top objections + class (misreading/gap/disagreement) + in-text fix
[If shepherding] change matrix status <done/total>; open questions to shepherd; June risk
[Tone check] anything that relitigates instead of resolves? <flag it>
```
