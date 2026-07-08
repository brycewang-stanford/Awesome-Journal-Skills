---
name: kdd-submission
description: Use when auditing a KDD submission for readiness in either cycle, covering Research vs ADS track declaration, OpenReview profile completeness for all authors, the ACM sigconf 8-content-page budget, double-blind checks, in-paper artifact references, resubmission declarations, and desk-reject triggers specific to ACM SIGKDD.
---

# KDD Submission

Run this audit twice: once when the abstract is registered, once before the full-paper
deadline. KDD's abstract and paper deadlines are about a week apart in each cycle
(2026 Cycle 1: July 24 / July 31, 2025; Cycle 2: February 1 / February 8, 2026, all
AoE), and several failure modes below are only fixable in that gap. Reopen the current
track CFP first — every number here is a 2026-cycle anchor, not a permanent rule.

## Track and cycle declaration

- One paper, one track: the same work may not go to the Research Track and the Applied
  Data Science Track simultaneously. If the team is still arguing about track choice at
  submission week, run `kdd-topic-selection` before anything else.
- Confirm which cycle the deadline belongs to. A team planning around "the KDD
  deadline" without naming the cycle is planning around the wrong date half the time.
- Resubmissions from a prior cycle's Resubmit decision must be flagged in the form,
  must carry the previous OpenReview forum id, and must prepend a one-page summary of
  changes as the first page of the PDF. Omitting the summary page wastes the
  resubmission advantage.

## OpenReview profile gate

KDD 2026 required a **complete OpenReview profile for every listed author**, not just
the submitter: institutional affiliations covering at least the past five years,
homepage, DBLP link where prior publications exist, ORCID, advisors, and recent
publications. Incomplete co-author profiles are a pre-deadline blocker that no one
person can fix alone — chase them at abstract time, not on deadline night.

## Format audit

The Research Track submission is **8 content pages**, followed by references and an
optional appendix, in the double-column ACM format:

```latex
% KDD 2026 Research Track recommended setting (verify against the current CFP)
\documentclass[sigconf,anonymous,review]{acmart}
% - sigconf: ACM conference two-column layout
% - anonymous: strips author block for double-blind review
% - review: adds line numbers reviewers cite in their reports
% Do NOT tweak \baselineskip, margins, or font sizes; ACM/TAPS tooling and
% chairs both detect a modified acmart.
```

- Content beyond page 8 that is not references or appendix is a desk-level risk; move
  it or cut it, never squeeze it.
- Anonymity must survive the appendix and the referenced repository: author names,
  affiliations, acknowledgements, grant numbers, institutional dataset names, and
  git history are all leak surfaces.
- Reference the code/data repository **inside the PDF**: KDD's rebuttal and discussion
  phases forbid hyperlinks, so a repository not cited at submission time is invisible
  to reviewers forever.
- Complete the generative-AI disclosure in the submission form if any such tool touched
  the text or the work; ACM's authorship policy also governs who may appear as an
  author.

## Desk-reject and severity table

| Trigger | Track affected | Severity | Fixable after deadline? |
|---|---|---|---|
| Missing post-launch performance quantification | ADS | Desk reject per the 2026 CFP | No |
| Content pages over the budget | Both | Desk-level | No |
| Identity leak in PDF, appendix, or repo | Both | Desk-level or chair flag | No |
| Incomplete co-author OpenReview profile | Both | Submission blocked or flagged | Only before deadline |
| Undeclared resubmission of a Resubmit paper | Both | Loses resubmission standing | No |
| Same paper in Research and ADS | Both | Rejection of both | No |
| Repository link absent from PDF | Both | Not fatal, but unrepairable in rebuttal | No |

## Final-week sequence

1. Freeze the track and cycle declaration; verify the OpenReview group id matches
   (e.g., a `Research_Track_Cycle_2` group is not the ADS group).
2. Sweep all co-author profiles against the completeness list above.
3. Rebuild the PDF from a clean acmart checkout; confirm 8 content pages and that the
   appendix starts after the references.
4. Anonymize the artifact: fresh repo without history, no institutional paths, README
   free of names; cite it in the paper body.
5. For ADS: point at the exact section and table quantifying post-launch performance —
   if a reviewer cannot find it in 30 seconds, neither will the desk check.
6. Register the abstract early in the week; upload the paper with hours, not minutes,
   of margin against AoE.

## Vignette: an ADS submission that nearly desk-rejected itself

A payments team submits their deployed risk model to the ADS track. The draft's
evaluation section leads with offline AUC across four benchmark datasets — strong
work, but the post-launch numbers sit in a single sentence inside the conclusion
("since launch, chargebacks decreased"). Under the 2026 ADS rule this reads as
unquantified deployment evidence: no metric definition, no window, no baseline
period. The audit fix costs one evening, not one experiment:

- Promote the production measurement to its own section with a table: metric
  definition, measurement window, traffic share, before/after or A/B values.
- Demote two of the four offline benchmarks to the appendix; ADS reviewers weight
  the online table far above the third and fourth offline dataset.
- Add one paragraph on what the offline metrics failed to predict about online
  behavior — the lessons-learned register the track exists for.

The general lesson: at submission time, audit *findability* of the track's gate
evidence, not just its existence.

## Cross-cycle edge cases

- A paper rejected (not Resubmitted) in Cycle 1 and substantially rewritten may
  return in Cycle 2 as a fresh submission — but if the overlap with the old forum is
  obvious, silence is riskier than a voluntary note; check the current CFP's wording
  on prior-cycle papers before deciding.
- A Resubmit paper whose authors switch tracks (Research → ADS) is effectively a new
  submission: the Resubmit standing attaches to the reviewed paper, not to the
  project. Re-read the current rules before assuming the change summary carries over.
- Adding authors between abstract and paper deadlines can trip the profile gate again
  at the worst moment: every new name needs a complete OpenReview profile too.
- The abstract registered at the abstract deadline should match the final framing;
  bait-and-switch abstracts (registered as graph mining, submitted as LLM prompting)
  risk mis-bidding and hostile expert assignment.

## Output format

```text
[KDD readiness] Ready / Needs fixes / Not ready
[Track x cycle] Research|ADS x Cycle 1|Cycle 2 (source: current CFP)
[Blocking checks] <profiles/pages/anonymity/track duplication/resubmission flag>
[ADS deployment gate] quantified post-launch evidence: present / absent / N-A (Research)
[Artifact visibility] repo cited in PDF: yes / no
[Fix order] <ordered fixes before the AoE deadline>
```
