---
name: chi-review-process
description: Use when interpreting the ACM CHI Papers review pipeline — the AC, Subcommunity Chair and external-reviewer roles, descriptor-based reviewer matching, the A/ARR/RR/RRX/X recommendation scale, desk-reject and rubric-based assisted desk-reject screening, the minor/major-revision split, round-2 accept/reject decisions — and what each stage means for authors.
---

# CHI Review Process

CHI's Papers track runs a two-round, committee-anchored process that resembles a
journal's revise-and-resubmit more than an ML conference's rebuttal. Mechanics below
follow the CHI 2027 Papers Review Process page (re-read directly on 2026-11-24) and
the CHI 2026 outcome reports. CHI 2027 restructured the pipeline: topical
subcommittees are gone, reviewer matching runs on author-selected descriptors, and
the old 1AC/2AC pair is replaced by one AC per paper.

## Who touches your paper

- **AC (Associate Chair)** — manages your submission, holds full authority over the
  choice of external reviewers, leads the PCS discussion, and writes the meta-review
  that forms the basis of the round-1 outcome. Each AC handles about 15 papers. The AC
  is your most important reader at CHI.
- **External reviewers** — a matching system proposes three candidate reviewers from
  the Review Responsibility pool by comparing your paper's descriptors with reviewers'
  registered expertise; the AC may accept them or recruit others. In total a paper
  that reaches full review is read by four or more experts including the AC.
- **Emergency Review Board (ERB)** — experienced reviewers who can supply reviews in
  the final two weeks of the review period when an assigned reviewer cannot finish.
- **Subcommunity Chairs (SCs)** — each oversees about 10–15 ACs, monitoring review
  quality, consistency and fairness, confirming ADR outcomes, and deciding how their
  subcommunity deliberates (synchronous meeting, fully asynchronous on PCS, or a mix).
- **Papers Chairs** — run administrative and completeness checks, own the overall
  process and the final accept list.

CHI 2027 also pilots AI-assisted tools for AC/reviewer matching, initial DR/ADR
screening, and completeness checks; the posted process is explicit that decisions,
from desk reject to final outcome, stay with the AC, SC and Papers Chairs.

## Before screening: the completeness report

After the deadline an automated tool checks each paper's review-responsibility slots,
that named reviewer-authors have valid ORCIDs, and that the paper carries enough
descriptors for matching. Authors receive the report and get a short window to fix
issues before screening begins.

## Two kinds of early rejection

CHI screens before full review, and since the 2026 cycle this screening has teeth:

1. **Desk reject (DR):** format and compliance — wrong template (including
   double-column and extended-abstract formats), anonymization failure, undeclared
   closely related concurrent submissions, undeclared/uncited closely related own
   prior work, unjustified length (the >12,000-word rule) or a mis-declared short
   paper, not written in English, clearly unfinished or sloppy papers, violations of
   the ACM Policy on Authorship. DR criteria apply throughout the process, including
   the revise-and-resubmit phase. Under the Review Responsibility Policy, if a declared
   reviewer-author fails to deliver their reviews, their submissions are desk-rejected.
2. **Assisted desk reject (ADR):** after basic DR checks, an automated tool scores
   each paper on a method-agnostic rubric built from the ACM criteria (Originality,
   Correctness, Novelty, Importance, Clarity of Exposition), focusing on whether
   claims are matched by evidence, argument or design work. The AC reads the paper with
   the report and decides; an SC and a Papers Chair confirm before authors are
   notified **around October 25**, with written AC feedback.

The CHI 2026 ADR rubric used four named grounds, still a useful self-check:

| Rubric code (CHI 2026) | Meaning |
|---|---|
| ADR-Context | Grossly insufficient literature review to contextualize the contribution |
| ADR-Contribution | Disproportionately small HCI contribution for the paper's length |
| ADR-Data | Grossly insufficient data to support the claims |
| ADR-Method | Grossly insufficient methodological detail, conceptual clarity, or research transparency |

At CHI 2026, subcommittees desk-rejected between 1.4% and 17.9% of their submissions
and assisted-desk-rejected between 1.1% and 16.6%, with **ADR-Context the most common
rubric ground** — weak related work is a pre-review rejection risk, not just a score
penalty (`chi-related-work`).

## Round 1: the recommendation scale

Reviewers recommend on a five-point scale:

- **A** — Accept with Minor Revisions
- **ARR** — either Accept with Minor Revisions or Revise and Resubmit
- **RR** — Revise and Resubmit
- **RRX** — either Reject or Revise and Resubmit (leaning reject)
- **X** — Reject

**No paper is accepted outright in round 1.** After the PCS discussion, the AC's
meta-review places each paper in one of three groups (CHI 2027 process page):

- **Minor revisions** — three reviews at ARR or higher (A or ARR; no RR, RRX or X):
  likely accepted subject to minor revisions.
- **Major revisions required** — not minor, but a majority of positive external
  reviews (A, ARR): invited to revise; can still be rejected in round 2.
- **Reject** — the AC recommends X; below the revise-and-resubmit threshold.

Both revision groups get **4 weeks** (reviews released November 5, resubmission due
December 3, 2026).

## Round 2: revision, then the final decision

Invited authors submit a revision with changes highlighted in colour plus a response
letter (mechanics in `chi-author-response`). The original AC and external reviewers
re-review (the AC may add reviewers); the round-2 result is Accept or Reject, with no
second major revision. The realized CHI 2026 numbers (old two-AC process) are still
the best base rate:

```text
CHI 2026 Papers funnel (posted outcome reports, chi2026.acm.org):
  6,730 completed submissions
→ 2,603 invited to revise and resubmit  (38.7% of submissions survived round 1)
→ 2,576 actually resubmitted            (27 withdrawn/lapsed)
→ 1,705 conditionally accepted          (65.5% of resubmissions; 25.3% overall)
```

Read your round-1 packet against this funnel: an invitation means you are in roughly
the top ~39%; a *minor-revisions* placement is far safer than a *major-revisions* one.

## Reading the reviews you receive

- Weigh the **AC meta-review** above everything; it summarizes the PCS discussion and
  tells you which criticisms the committee actually owns.
- A single RRX among otherwise positive externals is survivable; an AC meta-review that
  leans X means the invitation, if it comes at all, is fragile.
- Contradictory externals are common at CHI because reviewers are matched on topic,
  method and contribution descriptors that can pull in different directions; resolve
  contradictions by aligning with the meta-review, and flag the contradiction politely
  in the response rather than picking a side silently.
- "The contribution is unclear" from multiple reviewers is a framing defect you can
  fix in four weeks; "the study cannot support these claims" usually is not — decide
  early whether to revise seriously or withdraw and redo the work for next cycle.

## Confidentiality and conduct

Submissions are confidential to the review team; authors may message the AC
anonymously through PCS for clarification (and contact the SCs if the AC does not
respond), but contacting reviewers or ACs outside PCS violates the process. Reviewer
anonymity is permanent. Public complaints during the cycle can only hurt — escalation
happens through the Subcommunity Chairs and Papers Chairs, in writing, via PCS or the
posted contacts.

## Output format

```text
[Stage] completeness / screening / round-1 / RnR window / round-2 / decided
[Screening exposure] DR: <format/RRP risks> · ADR: <weakest rubric criterion>
[Round-1 read] AC meta: <lean> ext: <scores> → group: minor / major / reject
[Meta-review center of gravity] <the criticism the committee will hold you to>
[Realistic odds] <calibrated vs the ~65% resubmission acceptance base rate>
[Action] <revise seriously / fix framing / withdraw and re-route>
```
