---
name: jape-review-process
description: Use when navigating the Journal of Applied Econometrics (JAE) editorial process — single-blind peer review by anonymous reviewers in addition to the Editor, with final accept/reject authority vested in the Editor-in-Chief, plus the three-papers-under-review cap and the rule that rejected papers are not resubmittable unless invited.
---

# Review Process at JAE (jape-review-process)

## When to trigger

- Setting expectations for how a JAE submission will be evaluated
- Understanding who decides and what referees focus on
- Planning a pipeline around JAE's submission and resubmission rules

## How JAE review works

- **Single-blind peer review.** Official text: manuscripts are "single-blind peer reviewed by **anonymous reviewers in addition to the Editor**." Reviewers are anonymous; **authors are not** — do not anonymize the manuscript the way a double-blind journal would.
- **Editor-in-Chief decides.** Final acceptance or rejection rests with the **Editor-in-Chief** (Barbara Rossi). Co-editors handle many papers, but the final call is the EiC's. (The full current co-editor roster is **待核实** against a live board page.)
- **Rejected papers are not resubmittable unless the Editor invites it.** Treat a rejection as final absent an explicit invitation.
- **Cap:** no more than **three papers** from the same author may be under review at once — stagger submissions.

## What applied-econometrics referees check

Because JAE is empirical and replicable, expect reviewers to probe whether the **estimand is identified** on your real data; whether the **method is useful** in that setting; whether **inference** is appropriate (HAC, clustered, weak-IV-robust); whether **robustness** is shown (in the unlimited online appendix); and whether the work is **reproducible**, consistent with the mandatory Data Archive deposit. Treat replication objections as central, not administrative; a clean package pre-empts many. Do not infer process details beyond what the source map verifies.

## Desk-screen failure patterns at JAE

Most early exits at this venue trace to scope and replicability, not polish. Audit against the recurring patterns:

| Pattern | Why JAE screens it out | Pre-submission fix |
| --- | --- | --- |
| Pure-theory paper (asymptotics, no real data) | Outside the applied mandate | Add a genuine application or reroute to a theory outlet |
| Simulation-only evidence | The venue wants the method on real data | Anchor the Monte Carlo to an empirical question and dataset |
| Data that can be neither deposited nor documented | Mandatory archive deposit is unworkable | Resolve access/description before submitting |
| Main text far over 35 pages | Limit is hard; appendix is the designed overflow | Move robustness grids out of the article |
| Summary >100 words or carrying citations | House front-matter rule | Rewrite per `jape-writing-style` |

## Decision vocabulary and what each letter implies

- **Reject** — final; the no-resubmission-unless-invited rule means a reworked version goes elsewhere, not back to JAE.
- **Reject with invitation to resubmit / major revision** — the Editor sees a path; the resubmission is judged on whether each referee objection got *evidence*, not prose.
- **Minor revision** — protect the archive: any number that changes must change in the deposited code too.
- Exact decision categories and turnaround times vary; confirm against the journal's current author guidelines rather than assuming figures.

## Planning the pipeline without invented statistics

Do not budget around rumored acceptance rates or review speeds — JAE does not owe you a number, and this skill will not fabricate one. Plan around the verifiable constraints instead: the three-papers-under-review cap forces staggering across coauthor teams; the single-blind model means your identity and prior work are visible context, so the paper must be consistent with your own archived past results; and the EiC's final authority means the response letter's executive summary should be written for the Editor, with referee-level detail beneath it. What is predictable is *content*: an applied-econometrics referee pool drawn from people who write HAC, bootstrap, and weak-IV papers themselves will test exactly those joints first.

## Output format

```
【Model】single-blind; reviewers anonymous, authors not — prepared? [Y/N]
【Authority】final decision = Editor-in-Chief
【Desk screen】scope + replicability + 35pp + summary all clear? [Y/N]
【Pipeline】≤ 3 papers under review for this author? [Y/N]
【Resubmit】reject is final unless invited — understood? [Y/N]
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — single-blind, EiC authority, three-paper cap (and 待核实 board notes)
