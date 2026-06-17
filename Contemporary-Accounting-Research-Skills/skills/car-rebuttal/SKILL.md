---
name: car-rebuttal
description: Use when a Contemporary Accounting Research (CAR) revise-and-resubmit arrives — planning the revision and drafting a point-by-point response to two reviewers and the subject Editor, including any new analyses, robustness, and updated Data Integrity/code-sharing materials. Drafts the response; it does not run the new estimation (car-data-analysis) or the final preflight (car-submission).
---

# R&R Rebuttal (car-rebuttal)

## When to trigger

- You received a CAR revise-and-resubmit and must plan revisions and the response
- Reviewers asked for new identification tests, experiments, or model robustness
- The subject Editor's letter sets priorities you must address first
- You need to reconcile the response with CAR's code-sharing and data-availability requirements

## Plan the revision before writing the letter

- Build a **concordance**: every point from Reviewer 1, Reviewer 2, and the subject Editor, each mapped to a concrete action (new test, added robustness, reframing, clarification, or a reasoned push-back).
- Let the **subject Editor's letter set priority** — it signals which concerns are decisive at CAR, where the subject Editor disposes and the **EIC approves all acceptances**.
- Do the analytical/empirical work *first*; only then draft the response. **Invited revisions pay no further submission fee**, so the constraint is substance and the editor's deadline, not cost.

## Respond by tradition

- **Archival.** Reviewers typically press on **identification and robustness** — new natural-experiment evidence, parallel-trends/placebo tests, alternative measures, additional fixed effects, or sample-screen sensitivity. Show, don't assert, that the inference survives.
- **Experimental.** Expect requests on **confounds, the mediator, manipulation strength, and the participant pool** — possibly a new condition or a follow-up study isolating the mechanism.
- **Analytical.** Expect requests to relax assumptions, add comparative statics, or sharpen the empirical/institutional implication.

## Write the point-by-point response

- Quote each comment, then give the response and the **exact manuscript location** of the change (page/section/table).
- Be specific and courteous; where you disagree, argue from theory or evidence, not assertion.
- Keep a verifiable change-trail; ensure new results are reproducible from the **code repository**.

## Update CAR-specific materials

- Refresh the **data availability statement** and the **public code repository** if analyses changed, keeping variable definitions, omission rules, and modifications (winsorizing/truncating) documented; honor the **six-year retention** assurance.
- Disclose any new **generative-AI** use in Methods; if a related paper of yours has since appeared, update the **overlap disclosure**.
- Re-check the length budget (30/50 pages); route new robustness to the **online-only appendix**.

## Reproducibility change ledger

Every new or changed result needs a reproducibility row:

| Revision item | Table / figure | Code or data change | Disclosure update |
| --- | --- | --- | --- |
| New robustness or alternative measure | Main or online appendix table | Script name, variable definition, sample restriction | Data availability / repository note |
| New experiment or archival sample | Study/table number | Instrument, randomization, or sample construction file | Ethics, data, and retention note |
| Revised construct or proxy | Hypothesis/table location | Renamed variable and transformation log | Construct/proxy explanation |
| AI-assisted text/code cleanup | Methods or disclosure note | Tool use and human verification | AI disclosure if required |

Do not resubmit until a fresh clone of the repository or analysis folder regenerates all changed exhibits. CAR's data-integrity expectations make stale replication files a substantive defect, not an administrative detail.

## Checklist

- [ ] Concordance covers every reviewer and editor point with a concrete action
- [ ] Subject Editor's priorities addressed first
- [ ] New analyses/experiments/robustness completed and reproducible from the repo
- [ ] Point-by-point response cites exact change locations; disagreements argued, not asserted
- [ ] Data availability statement and code repository updated; retention assurance intact
- [ ] AI disclosure and own-work overlap disclosure refreshed
- [ ] Length budget respected; overflow in the online appendix
- [ ] Reproducibility change ledger completed and regenerated from a clean run

## Anti-patterns

- **Drafting the letter before doing the work** — CAR reviewers verify the manuscript actually changed.
- **Selective response** that quietly skips a reviewer's hard point.
- **Defensive push-back** without theory or evidence.
- **Stale reproducibility** — updated tables the archived code no longer regenerates.
- **Disclosure lag** — new analyses added but data availability, AI, or overlap statements left in the old state.

## Output format

```
【Concordance】R1 / R2 / subject Editor points → actions ...
【Priority】editor's first-order items addressed first?
【New work】tests/experiments/robustness done & reproducible?
【Response letter】each comment quoted, answered, located?
【CAR materials】data availability statement, code repo, AI & overlap disclosures updated?
【Reproducibility ledger】changed exhibits regenerate from clean run?
【Next step】car-submission (final preflight) → resubmit in Editorial Manager
```
