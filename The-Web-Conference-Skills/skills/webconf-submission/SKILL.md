---
name: webconf-submission
description: Use when auditing a Web Conference (WWW) research-tracks submission before the abstract or full-paper deadline, covering track choice among the ten research tracks, the single-PDF 8+references+appendix page arithmetic within 12 pages, EasyChair profile completeness, the author-list freeze, the 7-submission cap, and double-blind checks.
---

# Web Conference Submission

The Web Conference splits its abstract and full-paper deadlines by exactly one week
(2026: September 30 and October 7, 2025, AoE, explicitly strict). Several of the
checks below can only be fixed inside that week, and one — the author list — locks
shut at the *abstract* deadline. Treat every number here as a 2026-edition anchor
and reopen the current research-tracks CFP first.

## The three gates, in order of irreversibility

1. **Author-list freeze.** At the abstract deadline the author list and its ordering
   become final: no additions, removals, or reordering afterward, only spelling and
   affiliation corrections. Settle authorship disputes *before* registering the
   abstract, not during the review cycle. This is stricter than most ML venues and
   catches teams every year.
2. **Track declaration.** A submission goes to exactly one of the ten research
   tracks; the track determines which chairs and reviewer pool see the paper. A graph
   learning paper sent to "Web mining and content analysis" instead of "Graph
   algorithms and modeling for the Web" gets reviewers who ask different questions.
   If the track is contested inside the team, run `webconf-topic-selection` first.
3. **The 7-submission cap.** No author may appear on more than seven research-tracks
   submissions cumulatively. Count every draft your name is on across all
   collaborations *now* — a cap violation discovered at the deadline forces someone
   to withdraw something.

## Page arithmetic (2026 rule)

One PDF, three zones, hard total:

| Zone | Limit | Reviewer obligation |
|---|---|---|
| Main paper | 8 pages | Read fully |
| References | no separate cap | Consulted as needed |
| Optional appendix (proofs, pseudo-code, reproducibility) | fills remainder | **Not required to read** |
| Whole PDF | 12 pages total | — |

The binding constraint most teams miss: references and appendix *share* the
remaining 4 pages. A 2.5-page bibliography — common in survey-adjacent web papers —
leaves only 1.5 pages of appendix. And because reviewers may stop at page 8, any
result, ablation, or ethics statement that carries a claim must live in the main
paper. The appendix is for *verification*, not *persuasion*.

## Format and anonymity

```latex
% WWW 2026 research-tracks setting (reconfirm against the current CFP)
\documentclass[sigconf, anonymous, review]{acmart}
% sigconf   -> ACM two-column proceedings layout
% anonymous -> suppresses the author block for double-blind review
% review    -> line numbers for reviewer reference
% Word authors: the ACM "Interim Template" was accepted in 2026.
```

- Strip acknowledgements, grant numbers, and identifying self-citations ("our prior
  system [12]" where [12] names your platform); refer to your own published work in
  the third person.
- Preprint tolerance is specific: an *anonymized* copy on arXiv or SSRN may exist,
  but the submission must not cite it. Do not tweet the preprint under the paper
  title during review.
- Web papers leak identity through data: an internal dataset name, a crawler
  user-agent string in the appendix, or a screenshot showing a logged-in session can
  each de-anonymize. Sweep figures and dataset descriptions, not just the header.

## EasyChair profile gate

The 2026 research tracks ran on EasyChair (a switch from the OpenReview groups of
2024-2025), and required an up-to-date profile — current and past institutional
affiliations plus conflict information — for **every listed author**. Because the
author list freezes at the abstract deadline, incomplete co-author profiles and
authorship questions must both be resolved in the same pre-abstract sweep. Confirm
which platform the current edition uses before sending co-authors instructions.

## Failure-severity ledger

| Failure | When it becomes unfixable | Typical outcome |
|---|---|---|
| Wrong author list | Abstract deadline | Live with it or withdraw |
| Over 12 total pages / over 8 main pages | Paper deadline | Desk-level rejection risk |
| Identity leak (text, figures, data names) | Paper deadline | Desk-level rejection risk |
| Track mismatch | Paper deadline | Hostile or confused reviews |
| Key evidence only in appendix | Paper deadline | Reviewers may never see it |
| 8th submission under one name | Abstract deadline | Forced withdrawal |
| Missing co-author EasyChair profile | Abstract deadline | Submission blocked |

## Deadline-week runbook

1. Day 7 (abstract day): register title, abstract, track, and the final author list;
   verify all profiles; recount the per-author submission tally.
2. Day 5: rebuild the PDF from a clean `acmart` checkout; check page zones; confirm
   nothing claim-bearing sits past page 8.
3. Day 3: anonymity sweep — text, references, figures, dataset names, PDF metadata,
   any linked repository.
4. Day 1: upload with hours of margin. The 2026 CFP said no extensions, and the
   venue's history backs that up.

## Vignette: the abstract-week authorship dispute

A four-person team plans to add a fifth author "if their experiments make it in."
At most venues this is safe procrastination; here it is a trap. The experiments
land on October 3 — three days after the abstract deadline froze the list. The
options are now all bad: publish without credit, withdraw and lose the cycle, or
ask chairs for an exception the CFP explicitly rules out. The audit lesson: at
T-2 weeks, force the question "who could conceivably deserve authorship by
camera-ready?" and register the inclusive list — trimming never becomes necessary
(contribution statements can scope credit), but adding becomes impossible.

## Cross-lane edge cases

- **Downgrading to a short paper after the research deadline** is a rewrite into a
  different call (4 pages *including* references in 2026, November deadlines), not
  a resubmission — the abstract registered in September does not carry over.
- **A paper rejected from the research tracks cannot slide into Web4Good** in the
  same cycle; the 2026 Web4Good deadline (November 30) passed before research
  notifications (January 13).
- **Industry-track double-dipping** is a different-platform trap: the 2026 research
  tracks ran on EasyChair while Industry ran on OpenReview, and the originality
  rule bars the same work from both regardless.
- **The 7-submission cap counts submissions, not acceptances** — a withdrawal
  after the paper deadline still consumed a slot during the window that mattered.

## Output format

```text
[WebConf readiness] Ready / Needs fixes / Not ready
[Track] <one of the current research tracks> (source: current CFP)
[Page zones] main=<n>/8, total=<n>/12, claim-bearing content past p.8: yes/no
[Author gates] list frozen OK / at risk; per-author cap: OK / violated
[Anonymity] text / figures / data names / metadata: pass or fail each
[Fix order] <ordered actions before the AoE deadline>
```
