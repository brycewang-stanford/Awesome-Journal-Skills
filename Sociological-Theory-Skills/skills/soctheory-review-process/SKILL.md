---
name: soctheory-review-process
description: Use when you need to understand Sociological Theory (ST)'s double-anonymous peer review and interpret a decision letter focused on conceptual novelty and logical soundness. Explains the process and decision types; it does NOT draft the response document (that is soctheory-rebuttal).
---

# Understanding ST's Peer Review (soctheory-review-process)

## When to trigger

- You just received an ST decision letter and need to interpret it
- You do not know what ST review weights or expects of you
- You are deciding whether an R&R is worth pursuing and how to read the editor's signals
- You need to triage reviewer comments by what ST actually values

## What ST review is (durable norms)

ST uses **double-anonymous peer review** through SAGE's web-based system (Manuscript Central,
`mc.manuscriptcentral.com/soct`; 检索于 2026-06；以官网为准). The durable shape:

- A handling editor assigns the paper to reviewers expert in your **theoretical tradition**.
  (The editorial team rotates; recent ST guidance lists a multi-person editor group rather than
  a single EIC — confirm the current slate on the official ASA/ST page; do not name individuals
  from memory. See `resources/official-source-map.md`.)
- Reviews focus on what ST exists to protect: a genuine **conceptual contribution** (a new way
  of seeing — see `soctheory-contribution-framing`), **conceptual clarity**, **internal
  consistency**, the **logical soundness** of the argument, and **engagement with the relevant
  tradition**. Reviewers do **not** ask about identification, sample size, robustness, or
  measurement validity — those are ASR/AJS criteria.
- Decisions are commonly: **Reject**; **Major Revision (R&R)**; **Minor Revision**; rarely an
  immediate **Accept**. Multiple rounds are normal for theory papers.
- An R&R is an invitation, not a promise; the bar can rise across rounds.

## Desk-reject triggers specific to ST

The editor screens for fit and contribution before sending a paper out. Most common ST desk
rejects: (1) "this is an empirical paper" (a hypothesis test in disguise); (2) a literature
review with no original theoretical move; (3) an "application" of a theory that does not change
the theory; (4) conceptual relabeling presented as new theory; (5) an argument with no engaged
tradition; (6) length/format/masking failures or out-of-scope submissions (route to ASR/AJS,
Sociological Methodology, ARS, or Theory and Society).

## Reading the decision letter

| Signal in the letter | What it usually means | Your move |
|----------------------|-----------------------|-----------|
| "Promising but the contribution is unclear" | Theory may be sound but under-differentiated | Re-run `soctheory-contribution-framing` |
| "Propositions are not well argued" | Reasoning gaps between premises and claims | Re-run `soctheory-argument-development` |
| "Reads as a review of the literature" | No real theoretical move | Re-run `soctheory-literature-positioning` + `soctheory-writing-style` |
| "Concepts are unclear / overlap existing ones" | Conceptual clarity challenged | Re-run `soctheory-theory-construction` (definition/extension) |
| "Theory over-reaches" | Scope unstated | Re-run `soctheory-boundary-conditions` |
| "Doesn't engage tradition T" | Positioning gap | Re-run `soctheory-literature-positioning` |
| Editor flags specific reviewer points as essential | The editor's priorities | Address these first and most fully |

## Triaging reviewer comments

- **Read the editor's letter as the master key.** When reviewers disagree, the editor's framing
  tells you which issues are decision-critical.
- **Separate substance comments from presentation comments.** A missing mechanism or an
  undefended proposition outranks wording.
- **Distinguish "the theory is wrong" from "the prose hid a sound argument."** The first needs
  re-theorizing; the second needs `soctheory-writing-style`.
- **Note conflicts between reviewers** and plan to adjudicate them transparently (in `soctheory-rebuttal`).

## Checklist

- [ ] Decision type identified (Reject / Major R&R / Minor)
- [ ] The editor's stated priorities extracted and ranked
- [ ] Each reviewer comment tagged: substance vs. presentation
- [ ] Comments mapped to the skill that addresses them (theory / argument / positioning / scope / contribution)
- [ ] Reviewer conflicts identified for transparent adjudication
- [ ] Realistic judgment made on whether the revision can meet the raised bar

## Anti-patterns

- Treating an R&R as acceptance and making only cosmetic changes
- Ignoring the editor's letter and responding only to reviewers
- Reading reviews as "the reviewers will fix the theory for me"
- Promising to add an empirical test — ST neither wants nor accepts one
- Underestimating the number of rounds and over-claiming the revision is final

## Output format

```
【Decision type】Reject / Major (R&R) / Minor
【Editor's priorities】ranked list
【Comment triage】substance: [...] | presentation: [...]
【Skill mapping】comment → soctheory-* skill
【Reviewer conflicts】[...]
【Go / no-go】pursue revision? rationale
【Next step】soctheory-rebuttal
```
