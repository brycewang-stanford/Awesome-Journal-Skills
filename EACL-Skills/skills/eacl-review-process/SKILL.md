---
name: eacl-review-process
description: Use when reasoning about the EACL review pipeline through ACL Rolling Review, covering reviewers and the action editor's meta-review, the commitment step where EACL decides main versus Findings versus reject, ethics escalation, confidentiality, and when to route a reviewed package to a sibling *ACL venue.
---

# EACL Review Process

Use this to model how an EACL decision actually gets made, so advice matches the machinery.
EACL outsources reviewing to **ACL Rolling Review** and keeps only the final decision: a paper
is reviewed in an ARR cycle, receives an **action-editor meta-review**, and is then **committed**
to EACL, where senior area chairs and program chairs sort commitments into **main**, **Findings
of ACL: EACL**, or **reject**. Reopen the current ARR and EACL pages before relying on specifics.

## The pipeline, stage by stage

| Stage | Who acts | Output |
|---|---|---|
| ARR review | Reviewers (usually 3) | Scores + written reviews |
| Rebuttal | Authors | Responses (see `eacl-author-response`) |
| Meta-review | Action editor | Synthesized assessment |
| Commitment | Authors | Package committed to EACL |
| Venue decision | EACL SACs / PCs | Main / Findings / reject |

The **meta-review is the pivot**: EACL's committee reads it, not the raw reviews in isolation, so
the rebuttal should aim to shape it.

## Findings is a real outcome

- **Findings of ACL: EACL** is archival, Anthology-published, and decided at commitment;
  notification is simultaneous with the main track. A Findings offer is an acceptance, not a
  rejection — weigh it as such (see `eacl-topic-selection` for the accept-Findings calculus).

## The single-cycle consequence for routing

- Because an edition like EACL 2027 draws from **one ARR cycle with no fallback**, a package that
  misses commitment or is rejected cannot simply wait for "the next EACL cycle" — the next
  opportunity is a **different conference**. Plan re-routing to a sibling *ACL venue (ACL, EMNLP,
  NAACL, AACL) as a first-class option, carrying the ARR reviews forward.

## Confidentiality and conduct

- ARR review is confidential; do not solicit, share, or discuss reviews outside the process.
- Reviewers and authors are bound by the ACL code of conduct; harassment or coercion (including
  citation coercion) is reportable.

## Ethics escalation

```text
If a submission raises an ethics concern:
  reviewer/AE flags it -> ethics review track -> may condition or block acceptance
Authors: address ethics/data-governance issues in the paper and checklist up front;
         an unresolved flag can override otherwise-positive reviews.
```

## Reading an outcome

- A **reject with substantive reviews** is a resource: the ARR reviews travel with a resubmission
  to another venue, so a clean rebuttal and revision plan are not wasted.
- A **borderline meta-review** often turns on the honesty of Limitations and the strength of the
  rebuttal — both are within author control.

## Output format

```text
[Pipeline position] <review / rebuttal / meta-review / commitment / decision>
[Meta-review read] <what the action editor likely concludes>
[Findings scenario] <accept-Findings vs push-for-main vs re-route>
[Ethics/conduct flags] <any, with handling>
[Next step] <commit here / re-route to sibling venue with ARR reviews>
```
