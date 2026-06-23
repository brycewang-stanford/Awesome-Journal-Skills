---
name: amr-review-process
description: Use when you need to understand the Academy of Management Review (AMR) developmental, multi-round review and interpret a decision letter focused on theoretical novelty and logical soundness. Explains the process and decision types; it does NOT draft the response document (that is amr-rebuttal).
---

# Understanding AMR's Developmental Review (amr-review-process)

## When to trigger

- You just received an AMR decision letter and need to interpret it
- You do not know what "developmental review" means or what is expected of you
- You are deciding whether an R&R is worth pursuing and how to read the editor's signals
- You need to triage reviewer comments by what AMR actually weights

## What AMR review is (durable norms)

AMR uses a **double-anonymous, multi-round, developmental** review. "Developmental" is the
operative word: the goal is to help promising theory papers become stronger, so reviews are
detailed and the bar rises across rounds. Verify current specifics on the official page, but
the durable shape is:

- A handling editor (the **Editor-in-Chief** — currently **Kris Byron** (Georgia State University), AMR EIC succeeding Sherry M. B. Thatcher; three-year term runs through the end of 2026 (1 July 2023 transition start), still sitting as of 2026-06-23 with no successor yet announced; verify the current slate on the AOM AMR editorial-leadership page — or an action editor) assigns the paper to reviewers expert in your conversation. AOM's public author page says designated reviewers advise the editor and that revisions may continue through multiple rounds; it does not publish an exact AMR reviewer count or acceptance rate, so do not quote one unless AOM publishes it.
- Reviews focus on the things AMR exists to protect: a genuine **theoretical contribution** (Whetten's What/How/Why/Who-Where-When, AMR 1989, DOI 10.5465/amr.1989.4308371), **construct clarity** (Suddaby, AMR 2010, DOI 10.5465/amr.2010.0419), and the **logical soundness** of the argument — not data (there is none). Reviewers do not ask about identification, sample size, robustness, or measurement validity; those are AMJ/ASQ/SMJ criteria.
- Decisions are commonly: **Reject**; **Reject & Resubmit** (encouraged to rebuild, treated
  as a fresh submission); **Major Revision (R&R)**; less often **Minor Revision**; rarely an
  immediate **Accept**.
- An R&R is an invitation, not a promise. Multiple rounds are normal at AMR.

## Desk-reject triggers specific to AMR

The editor screens for fit and contribution before sending a paper out. Most common AMR desk
rejects: (1) "this is an empirical paper"; (2) incremental theory; (3) a literature review
with no original move; (4) construct proliferation (relabeling); (5) untestable-in-principle
or tautological propositions; (6) poor fit/scope or anonymization failures.

## Reading the decision letter

| Signal in the letter | What it usually means | Your move |
|----------------------|-----------------------|-----------|
| "Promising but the contribution is not yet clear" | Theory may be sound but under-differentiated | Re-run `amr-contribution-framing` |
| "Propositions are not well supported by the argument" | Logic gaps between premises and propositions | Re-run `amr-data-analysis`, then `amr-theory-development` |
| "Reads as a review of the literature" | No real theoretical move | Re-run `amr-literature-positioning` + `amr-writing-style` |
| "Constructs overlap existing ones" | Construct distinctiveness challenged | Re-run `amr-theory-development` (domain/distinction) |
| "Scope/level inconsistency" | Level-of-theory confusion | Re-run `amr-methods` (cross-level) |
| Editor highlights specific reviewer points as essential | The editor's priorities | Address these first and most fully |

## Triaging reviewer comments

- **Read the editor's letter as the master key.** When reviewers disagree, the editor's
  framing tells you which issues are decision-critical.
- **Separate theory-substance comments from presentation comments.** Substance (a missing
  mechanism, an undefended proposition) outranks wording.
- **Distinguish "must change the theory" from "must explain better."** Some comments mean
  the theory is wrong; others mean the prose hid a sound argument.
- **Note conflicts between reviewers** and plan to adjudicate them transparently in the
  response (handled in `amr-rebuttal`).

## Checklist

- [ ] Decision type identified (Reject / R&R / Reject & Resubmit / Minor)
- [ ] The editor's stated priorities are extracted and ranked
- [ ] Each reviewer comment tagged: theory-substance vs. presentation
- [ ] Comments mapped to the skill that addresses them (theory / logic / positioning / contribution)
- [ ] Reviewer conflicts identified for transparent adjudication
- [ ] Realistic judgment made on whether the revision can meet the raised bar

## Anti-patterns

- Treating an R&R as acceptance and making only cosmetic changes
- Ignoring the editor's letter and responding only to reviewers
- Reading "developmental" as "the reviewers will fix it for me"
- Promising in a rebuttal to add data — AMR neither wants nor accepts data
- Underestimating the number of rounds and over-claiming the revision is final

## Output format

```
【Decision type】Reject / Reject & Resubmit / Major (R&R) / Minor
【Editor's priorities】ranked list
【Comment triage】substance: [...] | presentation: [...]
【Skill mapping】comment → amr-* skill
【Reviewer conflicts】[...]
【Go / no-go】pursue revision? rationale
【Next step】amr-rebuttal
```
