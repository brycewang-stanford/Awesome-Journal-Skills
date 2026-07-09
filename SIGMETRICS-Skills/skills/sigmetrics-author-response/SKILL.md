---
name: sigmetrics-author-response
description: Use when responding to ACM SIGMETRICS reviews, covering any initial rebuttal and — distinctively — the one-shot revision response letter that must map every item on the reviewers' required-changes list to a concrete change in the revised POMACS paper, resubmitted to a subsequent rolling deadline and re-reviewed once by the original reviewers under double-anonymity.
---

# SIGMETRICS Author Response

Use this after SIGMETRICS reviews are released. The defining SIGMETRICS response is the **one-shot
revision letter**: if you receive a **One-Shot Revision** decision, you get **exactly one** chance
to resubmit a revised paper (to one of the next two rolling deadlines) accompanied by a letter that
closes the reviewers' **explicit list of required changes**. Any initial-round rebuttal is
secondary; the revision letter is where the paper is won.

## Triage

- Answer what affects the decision: model rigor, proof correctness, assumption validity, the
  soundness and fairness of empirical/simulation evidence, novelty, and reproducibility.
- Use evidence that already exists or that the revision will concretely add — a completed proof
  case, a new simulation, a validated assumption — never a vague promise.
- Correct factual misreadings first; a reviewer who misread a lemma or a plot is often persuadable.
- Preserve **double-anonymity** in any letter that circulates before decision (the Operational
  Systems Track excepted).

## The one-shot revision response letter (the distinctive SIGMETRICS move)

A One-Shot Revision is single-shot: there is no second revision, so the letter must demonstrate that
**every** item on the required-changes list is resolved. It is a **change ledger**:

```text
[R1.1] Required change (quoted briefly): "prove the bound holds for the heavy-tailed case"
       -> Action: DONE  | added Thm. 1 case (b) and its proof in §3.2 (App. B for the full derivation)
       -> Where: §3.2, Appendix B; simulator run in artifact/sim/heavy_tail.ipynb validates it
[R2.1] Required change: "validate the M/G/1 assumption against a real workload"
       -> Action: DONE  | added §5.1 fitting the service-time distribution to the trace; QQ-plot Fig. 6
[R2.2] Required change: "compare against the size-aware optimal, not only the default"
       -> Action: DONE  | added the SRPT-style baseline, tuned with an equal budget (Table 2)
[R3.1] Required change: "discuss estimation error in fetch size"
       -> Action: DONE  | §6 quantifies degradation under estimation error and bounds it
```

The rule that turns a One-Shot Revision into an acceptance: **close the whole list.** Because the
revision is re-reviewed once against that list, an item neither done nor explicitly and
convincingly justified as infeasible is what the single shot punishes.

## Choosing the resubmission deadline

- You may target **one of the two subsequent deadlines** — pick the later one if closing the list
  needs a real proof or a new measurement campaign; do not rush a single-shot revision into the
  nearer deadline and leave an item half-done.
- Keep the paper under the SIGMETRICS process while revising: submitting the same work elsewhere
  before withdrawing is a simultaneous-submission violation.

## Reviewer pushback patterns

| Pushback | What it signals | SIGMETRICS-ready response |
|---|---|---|
| "The proof omits a case / an assumption is unstated" | Rigor/correctness doubt | Add the case or state the assumption explicitly; give the full derivation in an appendix |
| "The model assumption is unrealistic" | Construct validity of the model | Fit the assumption to a real workload/trace; quantify the gap and bound its effect |
| "The baseline is not the right/optimal one" | Fairness of the comparison | Add the strongest baseline (e.g. size-aware optimal), tuned with an equal, documented budget |
| "Simulation and analysis are not shown to agree" | Validation gap | Overlay the analytic curve on simulated measurements with confidence intervals |
| "Not reproducible" | Open-science gap | Ship the seeded simulator, trace-processing scripts, and analysis notebooks |

## Anonymity in the letter (easy to slip)

- Refer to your own prior work in the third person, as in the paper.
- Describe artifact changes without linking to an identity-revealing repository; use the anonymized
  location.
- Do not thank a named collaborator or funder inside a letter that circulates before decision.

## Calibration

- Respond to the criterion the reviewer actually raised, not the one you would rather defend.
- The revision, not the letter, carries the argument — the letter maps the list; the paper proves
  the point.
- Length/format norms for the letter vary by cycle; confirm the current instructions before sending.

## Output format

```text
[Turn] initial rebuttal / one-shot revision response letter
[Resubmission deadline] which subsequent rolling deadline, and why
[Priority issue] <reviewer required change>
[Decision dimension] rigor / proof / assumption validity / evidence / novelty / reproducibility
[Change ledger] <required change -> DONE/JUSTIFIED-INFEASIBLE + where in paper/appendix/artifact>
[List-closure check] every required change resolved? yes/no
[Anonymity check] <no identity leak in the letter: passed/issues>
```
