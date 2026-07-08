---
name: icra-writing-style
description: Use when drafting or tightening an ICRA manuscript — leading with the robot task and physical constraint, compressing a systems story into 6 IEEE two-column pages, writing figure-first for skimming reviewers, quantifying instead of demo-speak, and keeping notation consistent across kinematics, control, and learning sections.
---

# ICRA Writing Style

An ICRA paper is read by a tired Associate Editor and two or three reviewers who
between them skim hundreds of robotics PDFs each autumn. The style that survives
this is figure-first, task-first, and ruthlessly quantitative. This skill rewrites
drafts toward that shape inside the 6-content-page envelope.

## Lead with the task, not the technique

The strongest ICRA openings establish, within the first column: what the robot
must do, why physics or uncertainty makes that hard, what the paper contributes,
and what the headline number is.

- Weak: "Deep reinforcement learning has shown impressive results in recent
  years..." (parent-field throat-clearing; tells a robotics reviewer nothing).
- Strong: "Regrasping a tool that slips mid-task takes a torque-controlled arm
  out of its planned contact state; we present a reflex layer that detects slip
  onset from joint-torque residuals within 12 ms and recovers 87% of failed
  grasps that the nominal planner abandons."

The second version names the task, the physical difficulty, the mechanism, and
two measured numbers — before the reader decides whether to keep reading.

## The six-page budget

| Section | Target share | Notes |
|---|---|---|
| Title/abstract/intro | ~1.0 page | contribution bullets end the intro |
| Related work | ~0.5 page | positioning, not survey; see `icra-related-work` |
| Method / system | ~1.75 pages | one architecture figure carries the load |
| Experimental setup | ~0.75 page | platform, task, protocol, metrics |
| Results + analysis | ~1.5 pages | tables and failure analysis |
| Conclusion + limitations | ~0.5 page | honest limits read as strength |

Two structural rules follow from the budget. First, there is no appendix escape
valve: unlike ML venues, the 2026 rules give no unlimited supplementary PDF, so
anything reviewers need must fit the body (the video can *show* but not *state*
essential content — see `icra-supplementary`). Second, derivations longer than
half a column belong in a cited technical report or the eventual journal
version, with only the result and assumptions in the paper.

## Figure-first discipline

Robotics reviewers reconstruct papers from figures before reading prose. Audit
the figure chain alone: does Fig. 1 (task + platform), Fig. 2 (system/method),
Fig. 3+ (results, failure cases) tell the whole story with captions only?

- Fig. 1 should show the actual robot in the actual task, not a block diagram.
- Every plot needs units, and success-rate plots need trial counts in the
  caption ("n = 25 trials per condition").
- Prefer one dense, well-designed results figure over four thin ones; column
  width in the IEEE template punishes small multiples with unreadable fonts.
- Frame-strip figures (time-lapse of one execution) buy more reviewer goodwill
  per square centimeter than any other robotics figure type.

## Quantify or delete

Demo-speak is the house style of press releases, not ICRA papers. Rewrite every
qualitative claim into a measurement or remove it:

```text
"robust"            -> success rate + condition range it held over
"real-time"         -> control/inference latency in ms + rate in Hz
"generalizes"       -> performance on N held-out objects/terrains, listed
"significantly
 outperforms"       -> absolute + relative delta, trials, dispersion
"lightweight"       -> parameters / FLOPs / on-board compute used
"safe"              -> constraint-violation count over all trials, or cut it
```

## Notation across the stack

ICRA papers routinely span kinematics, dynamics, estimation, and learning in six
pages; notation collisions between these subcultures confuse reviewers fast.

- Reserve q for configuration; do not reuse it as a Q-function five lines later
  — rename one of them and say so.
- State frames explicitly on first use ({W}, {B}, {E}) and superscript
  transforms consistently; frame ambiguity in equations is a classic review
  complaint.
- Define every symbol at first use even if "standard in your subfield"; the
  assigned reviewers may come from an adjacent RAS keyword.
- SI units, comma-free equations, and bolded vectors per IEEE convention.

## Anonymity-safe prose (2026-cycle rule)

Style intersects the double-anonymous policy in three recurring spots:

- Platform descriptions: specs yes ("a 7-DOF torque-controlled arm"),
  possessives no ("our custom arm developed over five years").
- Prior-work continuity: "extending [7]" in third person, even when [7] is
  transparently the same group's paper.
- Site references: "an industrial partner's facility" instead of the named
  factory; generalize any detail that uniquely identifies the lab.

## Limitations paragraph that helps you

Since the classic pipeline offers no rebuttal (see `icra-review-process`), the
limitations paragraph is the one place to pre-answer the objection every reviewer
will otherwise raise unassisted. Name the strongest weakness precisely ("all
objects were rigid; deformables defeat the contact model"), say why the
contribution stands anyway, and point to the future-work line that addresses it.
A reviewer who sees their objection already acknowledged writes "authors are
aware" instead of "authors overclaim."

## Revision pass order

1. Task-first opening rewritten; headline numbers in the abstract.
2. Figure chain self-sufficient; captions carry trial counts and units.
3. Demo-speak sweep (table above) across every section.
4. Notation table built privately; collisions resolved.
5. Page budget enforced; derivations exported; body at 6.0 pages with
   references isolated on pages 7-8.
6. Limitations paragraph pre-answering the top predicted objection.

## Output format

```text
[Opening] task-first? headline numbers present? <rewrite if not>
[Figure chain] self-sufficient y/n — weakest figure: <which>
[Demo-speak] <count> unquantified claims, worst three listed
[Notation] collisions found: <list or none>
[Budget] content pages <n>/6 — overflow plan: <what moves/dies>
[Pre-answered objection] <the one the limitations ¶ now covers>
```
