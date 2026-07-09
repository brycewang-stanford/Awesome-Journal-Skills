---
name: tacas-review-process
description: Use when reasoning about how a TACAS (ETAPS) submission is evaluated, covering the per-category blind model (double-blind research vs single-blind tool/case-study), the single annual PC round with a rebuttal, the parallel mandatory artifact evaluation that feeds tool-paper acceptance, accept/reject decisions, and how TACAS's process differs from CAV's and from a journal's.
---

# TACAS Review Process

Model the pipeline before interpreting any single review. TACAS's process has three features that
surprise authors arriving from other venues: reviewing is **blind by category**, the decision for a
**tool paper** depends on a **parallel artifact evaluation**, and the whole thing runs in a **single
annual round** on the ETAPS schedule with a short rebuttal — not a rolling or multi-round journal
cycle.

## Process model

- Submission and review run on **EasyChair** under the ETAPS joint schedule. Reviewing is
  **per-category**: **regular research papers are double-blind**; **case-study, regular tool, and
  tool-demonstration papers are single-blind**.
- Each paper is read by multiple PC members who weigh, for a research paper, the **soundness and
  significance of the algorithm**; for a tool paper, the **tool's contribution and its working
  artifact**; for a case study, the **realism of the system and the honesty of the lessons**.
- For **regular tool and tool-demonstration** papers, a **mandatory artifact** is evaluated by the
  Artifact Evaluation Committee **in parallel with the PC**, and the artifact outcome **feeds the
  acceptance decision** — a paper whose artifact does not work is in real jeopardy.
- There is a short **rebuttal / author-response** window before the PC finalizes decisions.
- Accepted papers publish in **Springer LNCS**, gold open access; badges earned by the AEC
  (Available / Functional / Reusable) are printed on the title page.

## Reading a decision against the category

| Category | What reviewers weigh most | Author move on a weak review |
|---|---|---|
| Research | Soundness of the algorithm/encoding; is the correctness argument right? | Correct a misread proof/step in the rebuttal; supply the missing lemma or example |
| Regular tool | Does the tool work and advance practice? Does the artifact reproduce the claims? | Fix/clarify the artifact story; show the benchmark comparison is fair |
| Case study | Is the system real and the evaluation honest? Are the lessons transferable? | Sharpen what generalizes; bound the threats to the lessons |
| Tool-demonstration | Is there a genuine, reproducible demonstration in six pages? | Clarify the demo path; ensure the artifact demonstrates what the text claims |

The strategic reading: for a **tool paper**, the artifact is part of the review — a great write-up
with a broken package still fails. Budget the artifact like a co-equal deliverable, not an
afterthought.

## How TACAS differs from its siblings

- **vs. CAV:** CAV is the broader formal-methods flagship with more theory room and a different
  calendar; TACAS's identity is the **tools-and-algorithms** emphasis, the **four categories**, and
  the **mandatory tool-paper artifact** integrated into acceptance. Never assume a shared deadline,
  page limit, or template — TACAS is LNCS via ETAPS.
- **vs. a journal (STTT/FMSD):** a journal offers revise-and-resubmit and no page ceiling; TACAS is
  a single-round conference with a rebuttal, not an R&R. Route a long, proof-heavy treatment to the
  journal.
- **vs. SV-COMP:** the competition ranks verifiers on a common task set and its results are reported
  separately; a **tool paper** is peer-reviewed prose about a tool, judged on contribution and
  artifact, not on a leaderboard position.

## Who reads you

Expect verification experts matched to your subarea. For a research paper they will check the
soundness argument line by line; for a tool paper they (or the AEC) will try to **run your
artifact** and reproduce a headline result; for a case study they will probe whether the system is
representative. Vague algorithm descriptions and unreproducible tool claims are caught, not skimmed.

## Where author leverage actually exists

```text
[Before submission]  category choice + topic keywords -> reviewer match      (largest lever)
[Artifact (tool)]    a clean-VM package that reproduces the claims           (co-decides tool papers)
[Rebuttal]           correct factual misreadings, supply a requested number, clarify a proof step
[After reject]       no appeal; reroute to CAV/VMCAI/FMCAD or a journal, or return next TACAS cycle
```

A rebuttal moves borderline papers when it fixes a misreading or answers a concrete question; it
does not move papers by arguing taste, and it cannot repair a fundamentally broken artifact after
the fact.

## Misreadings to avoid

- **Thinking the artifact is post-acceptance for a tool paper** — it is mandatory, parallel, and
  decision-feeding.
- **Anonymity confusion** — only research papers are double-blind; do not anonymize a single-blind
  tool paper, and do not deanonymize a research paper.
- **Treating the rebuttal as a second submission** — it is short and targeted; the paper as
  submitted carries the argument.
- **Projecting CAV's or last year's process** — categories, dates, and artifact rules are set per
  ETAPS edition.

## Output format

```text
[Process stage] pre-submission / under review / rebuttal / notified / accepted
[Category + blind mode] research (double-blind) / case-study|tool|tool-demo (single-blind)
[Decision drivers] soundness | tool+artifact | case realism | demo reproducibility
[Artifact status] (tool/tool-demo) reproduces claims on clean VM? yes/no
[Leverage plan] the next-stage action that can actually change the outcome
[Forbidden moves] wrong-category anonymity error / unrunnable artifact / unsupported new claims in rebuttal
```
