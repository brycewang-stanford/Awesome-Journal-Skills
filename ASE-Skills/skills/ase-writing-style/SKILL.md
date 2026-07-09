---
name: ase-writing-style
description: Use when shaping the prose and structure of an ASE (IEEE/ACM Automated Software Engineering) research paper, covering the automation-first first-page arc, stating the automated task precisely, keeping the tool runnable and the model-swap test in mind, threats-as-argument, and the 10+2 page discipline on the ACM acmart template.
---

# ASE Writing Style

Write the paper so an automated-SE reviewer sees, on the first page, **what task you automate, how
you automate it, and that it runs on real subjects**. ASE rewards a clearly stated automation with
evidence proportional to the claim — not a systems win, not a leaderboard, and not a broad finding
that would read better at FSE. The worked example in `resources/worked-examples/01-introduction.md`
shows the arc before → after.

## The ASE first-page arc

Lead with the automation, in this order:

1. **The automatable task** — a software-engineering task the reader recognizes (detect X, generate
   Y, repair Z, comprehend W), named precisely enough that a reviewer knows what "success" is.
2. **Why current automation (or manual practice) is inadequate** — what existing tools do *not* do,
   stated as a gap, not a literature tour.
3. **The contribution as an automation design** — the technique (analysis, generator, synthesizer,
   repair, learned model) and, ideally, the **tool** that embodies it.
4. **Evidence on real subjects** — real systems, credible *tool* baselines, and the metric that
   matches the task (not a proxy).
5. **What it automates for practice + threats posture** — the payoff, with the central threat named
   where it lives, not deferred to a closing paragraph.

Put the automation and the first evidence within the first three pages; the early-rejection gate
means a weak opening can end the process before rebuttal.

## State the automated task precisely

- Name the **input**, the **output**, and the **success criterion** of the automation. "We improve
  code quality" is not a task; "given a flaky test, synthesize a patch that makes it deterministic
  without weakening its assertions" is.
- Say what the tool **takes as input** in practice (source? bytecode? traces? a repository?) and
  what it **produces** — reviewers map this straight to feasibility.

## Keep the model-swap test in view

If a learned component is involved, write so the **automation design is the contribution**, not the
model. Report an **ablation** that isolates the learned part from the analysis/oracle, and phrase
claims so the software-engineering lesson survives a model swap. A paper whose lesson evaporates
when the model changes reads as an ML re-route (see `ase-topic-selection`).

## Evidence proportional to the claim

- A **detection** claim needs precision/recall on real defects with a defined ground truth.
- A **generation/synthesis** claim needs validity of the generated artifact (does it compile, pass,
  hold the property?), not just similarity to a reference.
- A **repair** claim needs verified behavior change (re-run, oracle), not a classification score.
- A **speed/scalability** claim needs real-system sizes and a fair baseline configuration.

Pair every claim in the abstract with a table or figure it points to. Match evidence to claim shape;
see `ase-experiments`.

## Threats as argument, not boilerplate

Argue construct, internal, and external validity where they arise. For automated-SE tools the usual
suspects: the **oracle** (how do you know a "repair" is correct?), **subject selection** (are the
systems representative or self-selected?), **baseline fairness** (equal budgets/tuning?), and
**overfitting** to the evaluation set. Name the residual threat plainly and bound it (an audited
subsample, a held-out subject set) rather than reciting a checklist.

## Page-budget discipline (10 + 2)

- **10 pages** for everything readable — text, figures, tables, appendices — **plus 2** for
  references only. The mandatory **Data Availability Statement** after Conclusions counts inside the
  10 pages.
- Recover space **editorially**, not by shrinking the template. Move reproducible detail (full
  configs, extra tables, proofs) to the artifact, but nothing that *decides acceptance* may live
  outside the body (see `ase-supplementary`).
- Figures earn their space by carrying an argument (the automation's pipeline, a
  per-root-cause breakdown), not by decorating it.

## Prose conventions

- Present tense for what the tool does; past tense for what you did in the study.
- Name the tool once, early, and use it consistently (anonymized at submission).
- Prefer concrete verbs of automation — *detects, synthesizes, localizes, repairs, infers* — over
  vague ones like *leverages* or *explores*.
- Third-person self-citation throughout, for double-anonymity.

## Common ASE writing failures

| Failure | Why it hurts at ASE | Fix |
|---|---|---|
| Model/leaderboard framing | Reads as ML, not automated SE | Foreground the automation design; add the ablation |
| Vague task statement | Reviewer cannot judge success | Give input/output/success criterion in ¶1 |
| Proxy-metric evaluation | Evidence does not match a repair/synthesis claim | Verify the produced artifact directly (re-run/oracle) |
| Threats as a closing recital | Construct/oracle validity never engaged | Argue each threat where it arises; bound it |
| Body over 10 pages | Desk-reject-grade | Move reproducible detail to the artifact |

## Output format

```text
[Task] input -> output -> success criterion (one sentence, on page 1?)
[Automation-first arc] task / inadequacy / technique+tool / real-subject evidence / payoff+threats — all present?
[Model-swap] ablation isolating the learned component present? lesson survives a model swap?
[Evidence-claim pairing] each abstract claim -> a table/figure with a matching metric
[Budget] content pages / reference pages / Data Availability inside 10pp?
```
