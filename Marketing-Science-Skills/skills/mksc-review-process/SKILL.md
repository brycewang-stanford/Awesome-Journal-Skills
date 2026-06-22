---
name: mksc-review-process
description: Use when understanding how Marketing Science evaluates a manuscript — the double-anonymous Senior-Editor / Associate-Editor routing, what the first-pass and review look for, and how to read a decision letter. Explains the process; it does not draft the revision response (mksc-rebuttal).
---

# Review Process (mksc-review-process)

## When to trigger

- You want to know what happens after you submit, and on what criteria
- You received a decision letter and need to interpret it before responding
- You are unsure how MKSC review differs from single-blind economics/marketing outlets

## How the process works

- **Editorial structure.** The Editor-in-Chief (Puneet Manchanda, Michigan Ross; term Jan 1 2025–Dec 31 2027, renewable through 2030 — verified 2026-06-22) oversees a set of **Senior Editors** who handle assigned papers, working with **Associate Editors** — a Senior-Editor/Associate-Editor routing model, *not* Management Science's standing departmental Area Editors. Verify the current board on the editorial-board page before relying on specific names.
- **Double-anonymous review.** Regular submissions are reviewed double-anonymous per the INFORMS-wide mandate; reviewers do not see author identities, and the manuscript must stay blinded. The cover letter is seen by the Editor/AE but not reviewers. (Practice/Science-to-Practice tracks are single-blind.)
- **First pass.** The handling team screens for readability and whether the paper makes a **significant, original contribution on an important topic** using a credible model. Papers that are model-free, off-topic, or unreadable can be returned early.

## What reviewers weigh

- **Importance and fit** — is the marketing question important, and is it answered through a model (the MKSC core)?
- **Model and identification** — are the assumptions defensible, the parameters credibly identified, the estimator appropriate?
- **Fit and counterfactuals** — does the model fit, and is the counterfactual/policy result valid and well-quantified?
- **Originality / self-overlap** — is the contribution genuinely new relative to prior work, including the authors' own?
- **Transparency** — can the work be reproduced (the Replication and Disclosure Policy looms on acceptance)?

## Reading the decision letter

- **Reject** — usually a fit, importance, or identification problem the team sees as unfixable; weigh whether a different venue (JCR/JMR/Management Science) fits better.
- **Revise & resubmit** — the developmental signal; the AE's letter prioritizes the issues. The process is typically **multi-round**; the AE letter is the contract for what must change.
- **Conditional/minor** — usually identification, robustness, exposition, or replication-package items.

## Checklist

- [ ] You know your handling SE/AE structure and that review is double-anonymous
- [ ] You understand the first-pass bar (importance + model + readability + originality)
- [ ] You can map each reviewer point to model / identification / fit / counterfactual / transparency
- [ ] You have identified the AE's prioritized concerns (the real contract)
- [ ] You have decided whether to revise or redirect venues

## Anti-patterns

- Treating MKSC review like a single-blind economics submission.
- Reading reviews as a checklist while ignoring the AE's stated priorities.
- Promising new structural estimation you cannot deliver in the next round.


## Review-risk pass for Marketing Science

Use this as a second-pass capability check. First lock the demand/supply mechanism, fit evidence, and counterfactual decision margin; then test whether the manuscript addresses quantitative marketing reviewers who read the model through the managerial counterfactual it makes possible.

- **Primary move:** Turn likely reviewer objections into a ledger with response evidence, manuscript location, and the decision-maker who must be convinced first.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against Journal of Marketing Research for empirical marketing breadth, Management Science for wider OR/MS reach, Quantitative Marketing and Economics for specialist modeling; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Decision】reject / R&R / conditional
【Handling】SE/AE; double-anonymous (or Practice single-blind)
【AE priorities】1... 2... 3... (the contract)
【Reviewer themes】model / identification / fit / counterfactual / transparency
【Go/redirect】revise for MKSC or target another venue
【Next step】mksc-rebuttal (if revising)
```
