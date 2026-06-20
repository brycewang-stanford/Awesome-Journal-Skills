---
name: ijoc-review-process
description: Use when calibrating expectations for the INFORMS Journal on Computing (IJOC) review cycle — the Area-Editor desk-reject gate, the undisclosed associate editor, single-blind reviewing, decision types, and whether a sibling journal fits better. Sets expectations and strategy; it does not draft the rebuttal (see ijoc-rebuttal).
---

# Review Process (ijoc-review-process)

## When to trigger

- You are about to submit and want to understand the **gates** and likely timeline
- A submission has been silent and you are unsure where it sits in the IJOC pipeline
- A decision arrived (reject / major / minor) and you need to read it correctly before responding
- You are weighing whether IJOC or a **sibling** (Operations Research, Management Science, MPC, IJOO) is the better home after a tough first round

## How the IJOC pipeline actually works

The cycle has a structure worth planning around (检索于 2026-06；以官网为准):

1. **Area-Editor suitability gate.** Your chosen technical area routes the paper to an **Area Editor** who first judges fit. Roughly **40% are desk-rejected** here for being out of scope, computing-light, or mismatched to the area. This gate rewards the `ijoc-topic-selection` and `ijoc-contribution-framing` work: an Area Editor who cannot see the computational advance in the abstract and intro will not send it out.
2. **Associate-editor handling — blind to you.** Survivors are assigned an **associate editor who manages the review and whose identity is never revealed** to authors. You cannot tailor a response to "the AE"; write to the report content, not the person.
3. **Single-blind refereeing.** Reviewers see your names; you do not see theirs. Reviewers are typically active researchers in your area who will know the current methods and may try to **reproduce your results from the deposit** — another reason the GitHub artifact must actually run.
4. **Decision.** Outcomes are the usual reject / major revision / minor revision / accept. A major revision on a computational paper often means re-running experiments (more instances, fairer baselines, more seeds), not just rewriting.

## Reading an IJOC decision letter

Triage every point by what it really demands:

| Referee theme | What it usually means | Where to fix |
|---------------|----------------------|--------------|
| "comparison is unfair / baseline weak" | re-run against the SOTA / current solver, symmetric tuning | `ijoc-data-analysis` |
| "instances cherry-picked / too small" | full standard set + scaling | `ijoc-data-analysis` |
| "contribution unclear / incremental" | sharpen the claim and positioning | `ijoc-contribution-framing` / `ijoc-literature-positioning` |
| "no guarantee / correctness unproven" | add validity/complexity argument | `ijoc-theory-development` |
| "cannot reproduce" | fix the deposit; align results to scripts | `ijoc-data-analysis` |
| "out of scope for this area" | re-argue fit, or consider sibling/area change | `ijoc-topic-selection` |

## Sibling fit after a hard round

If the recurring objection is "the contribution is the OR model, not the computing," the paper may belong at *Operations Research*; if it is "this is optimization theory," at *INFORMS Journal on Optimization*; if it is "pure MP-computation," at *Mathematical Programming Computation*. Conversely, a strong computational result rejected elsewhere as "too applied/computational" may fit IJOC well. Decide before burning a revision cycle on the wrong venue.

## Checklist

- [ ] Abstract/intro make the computational advance visible to clear the Area-Editor gate
- [ ] You expect to write to report content, not to a named AE
- [ ] The deposit runs, in case a referee tries to reproduce it
- [ ] Each decision-letter point is triaged to the owning skill and classed as re-experiment vs. rewrite
- [ ] A major revision plan budgets compute time for re-running experiments
- [ ] The sibling-fit question is answered if scope objections recur

## Anti-patterns

- Treating the Area-Editor gate as a formality and submitting a computing-light paper
- Trying to guess and flatter the (undisclosed) associate editor
- Submitting a deposit that does not run, then being surprised by a "cannot reproduce" report
- Reading a "major revision" on experiments as a rewrite job and not budgeting compute
- Re-submitting to IJOC when the persistent objection says the paper belongs at a sibling

## Output format

```text
【Journal】INFORMS Journal on Computing
【Skill】ijoc-review-process
【Stage】pre-submit / in-review / decision-received
【Gate read】Area-Editor fit risk; AE undisclosed; single-blind noted
【Decision triage】point → owning skill → re-experiment vs. rewrite
【Compute budget】re-run plan if major revision
【Sibling check】stay IJOC / consider OR / MS / MPC / IJOO
【Next skill】ijoc-rebuttal
```
