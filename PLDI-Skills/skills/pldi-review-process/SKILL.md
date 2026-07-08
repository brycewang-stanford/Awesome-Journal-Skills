---
name: pldi-review-process
description: Use when interpreting PLDI's review pipeline — double-blind HotCRP reviewing by a PL-implementor PC, the February author-response window, March notification, up-to-10% Distinguished Paper selection, and how post-acceptance artifact evaluation and PACMPL publication follow the decision.
---

# PLDI Review Process

Model the pipeline from the 2026 cycle (pldi26.sigplan.org, read 2026-07-08),
then re-anchor every date to the current edition: papers due November 13, 2025;
reviews written over the winter; author response February 17-21, 2026; decisions
March 5, 2026; artifact evaluation after acceptance; publication as PACMPL Issue
PLDI; talks in Boulder June 17-19, 2026. Chairs rotate per edition — 2026 ran
under Program Chair Manu Sridharan — so process details are one-cycle facts.

## Who is reading you

The PC is dominated by people who have shipped compilers, runtimes, analyzers,
and verifiers. Practical consequences:

- **Claims are audited mechanically.** A reviewer may re-derive your complexity
  bound, check your semantics against a corner case, or mentally rerun your
  benchmark protocol. Vague spots read as hidden flaws.
- **"Would this survive contact with real programs?"** is the ambient question.
  Toy-language-only evaluations need an explicit argument for why the toy
  captures the hard part.
- **Double-blind is real but statistical**: some reviewers will guess your lab;
  the process still requires the paper not to confirm it.

## Stage-by-stage

| Stage (2026 anchors) | What happens | Your lever |
|---|---|---|
| Nov deadline | Triage: format, page cap, anonymity, scope | Zero summary-rejection triggers (`pldi-submission`) |
| Winter reviewing | 3+ reviews scored on novelty, soundness, evaluation, clarity | Already spent; the paper argues alone |
| Feb 17-21 response | Authors answer factual errors and direct questions | The one paragraph that saves a soundness doubt (`pldi-author-response`) |
| PC discussion | Reviews + response reconciled; champions matter | A response that arms your champion with quotable pointers |
| Mar 5 notification | Accept / reject (any shepherding terms come with the letter) | Deliver conditions precisely and fast |
| Post-acceptance | Artifact evaluation, badges, PACMPL production | `pldi-artifact-evaluation`, `pldi-camera-ready` |

Whether a given cycle uses conditional acceptance or formal shepherding was not
confirmed for 2026 (待核实) — read your notification letter as the authority.

## Distinguished papers

Up to 10% of accepted papers may be designated Distinguished Papers; PLDI 2025
named 6 of 89 (about 6.7%). You cannot apply for it, but the profile is
consistent: a crisp problem, a mechanism others can reuse, an evaluation beyond
reproach, and usually a strong artifact. Aim the paper at that profile and let
the committee do what it does.

## Reading a decision

- **Reject with soundness objections**: fix before anything else; the same PC
  community reviews for POPL and OOPSLA, and a known-broken theorem follows you.
- **Reject on evaluation**: usually the cheapest repair — the SIGPLAN Empirical
  Evaluation checklist (`pldi-reproducibility`) is the reviewers' own rubric.
- **Reject on fit** ("this is a POPL paper", "this is engineering"): a routing
  signal, not a quality verdict; rerun `pldi-topic-selection` honestly.
- **Accept**: your response commitments are now contractual; see
  `pldi-camera-ready`.

## Output format

```text
[Stage] pre-submission / in review / response window / decided
[Review posture] champion? soundness doubts? evaluation objections?
[Response leverage] <which objections are answerable from the submitted PDF>
[Decision reading] accept path / repair-and-resubmit / re-route venue
[Next dates] <from the live cycle pages, with 待核实 flags>
```
