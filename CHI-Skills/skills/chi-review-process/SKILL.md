---
name: chi-review-process
description: Use when interpreting the ACM CHI Papers review pipeline — 1AC and 2AC roles, the A/ARR/RR/RRX/X recommendation scale, desk-reject and rubric-based assisted desk-reject screening, the revise-and-resubmit threshold, round-2 PC decisions — and what each stage means for authors.
---

# CHI Review Process

CHI's Papers track runs a two-round, committee-anchored process that resembles a
journal's revise-and-resubmit more than an ML conference's rebuttal. Mechanics below
follow the CHI 2027 and CHI 2026 Papers Review Process pages and the CHI 2026
outcome reports (read 2026-07-08 via search renderings; the conference sites block
direct automated fetching).

## Who touches your paper

- **1AC** — the Associate Chair who manages your submission: screens it, recruits two
  external reviewers, writes the meta-review, and represents the paper at the PC
  meeting. The 1AC is your most important reader at CHI.
- **2AC** — a second committee member who writes a full review like the externals.
- **Two external reviewers** — recruited by the 1AC for topical expertise.
- **Subcommittee chairs (SCs)** — run the subcommittee you designated, arbitrate desk
  rejects with the ACs, and chair the discussions.
- **Papers Chairs / PC** — own the overall process and the final accept list.

## Two kinds of early rejection

CHI screens before full review, and since the 2026 cycle this screening has teeth:

1. **Desk reject (DR):** format and compliance — wrong template, anonymization
   failure, unjustified length (the >12,000-word rule), policy violations.
2. **Assisted desk reject (ADR):** a rubric-based judgment call made jointly by SCs
   and ACs, introduced for CHI 2026 and codified by the CHI Steering Committee. The
   four posted rubric grounds:

| Rubric code | Meaning |
|---|---|
| ADR-Context | Grossly insufficient literature review to contextualize the contribution |
| ADR-Contribution | Disproportionately small HCI contribution for the paper's length |
| ADR-Data | Grossly insufficient data to support the claims |
| ADR-Method | Grossly insufficient methodological detail, conceptual clarity, or research transparency |

At CHI 2026, subcommittees desk-rejected between 1.4% and 17.9% of their submissions
and assisted-desk-rejected between 1.1% and 16.6%, with **ADR-Context the most common
rubric ground** — weak related work is now a pre-review rejection risk, not just a
score penalty (`chi-related-work`).

## Round 1: the recommendation scale

Reviewers and ACs recommend on a five-point scale:

- **A** — Accept
- **ARR** — Accept with Required Revisions
- **RR** — Revise and Resubmit
- **RRX** — Revise and Resubmit / Reject (leaning reject)
- **X** — Reject

**No paper is accepted in round 1.** The posted threshold: a paper earning at least
one recommendation of RR or better (A, ARR, or RR — not RRX or X) *from the 1AC or the
2AC* is invited to revise and resubmit. External reviewers' scores inform but do not
trigger the invitation; the AC pair holds the keys.

## Round 2: revision, then the PC meeting

Invited authors get about five weeks to submit a tracked-changes revision plus a
response to the reviews (mechanics in `chi-author-response`). The same review team
re-reads, and the PC meeting settles accepts and rejects. The process page warns that
as many as 50% of revised papers may still be rejected; the realized CHI 2026 numbers:

```text
CHI 2026 Papers funnel (posted outcome reports, chi2026.acm.org):
  6,730 completed submissions
→ 2,603 invited to revise and resubmit  (38.7% of submissions survived round 1)
→ 2,576 actually resubmitted            (27 withdrawn/lapsed)
→ 1,705 conditionally accepted          (65.5% of resubmissions; 25.3% overall)
```

Read your round-1 packet against this funnel: an RR invitation means you are in the
top ~39%, with roughly two-in-three odds that depend heavily on revision quality.

## Reading the reviews you receive

- Weigh the **1AC meta-review** above everything; it frames the PC-meeting discussion
  and tells you which criticisms the committee actually owns.
- An **RRX from an external** with **RR from the ACs** is survivable; the inverse
  pattern (ACs at RRX/X) means the invitation, if it comes at all, is fragile.
- Contradictory externals are common at CHI because subcommittees mix methodological
  cultures; resolve contradictions by aligning with the meta-review, and flag the
  contradiction politely in the response rather than picking a side silently.
- "The contribution is unclear" from multiple reviewers is a framing defect you can
  fix in five weeks; "the study cannot support these claims" usually is not — decide
  early whether to revise seriously or withdraw and redo the work for next cycle.

## Confidentiality and conduct

Submissions are confidential to the review team; contacting reviewers or ACs about a
paper outside PCS channels violates the process. Reviewer anonymity is permanent.
Public complaints during the cycle can only hurt — escalation happens through the
subcommittee chairs and Papers Chairs, in writing, via PCS or the posted contacts.

## Output format

```text
[Stage] screening / round-1 / RnR window / round-2 / decided
[Screening exposure] DR: <format risks> · ADR: <weakest rubric ground>
[Round-1 read] 1AC: <score> 2AC: <score> ext: <scores> → invitation likely? yes/no
[Meta-review center of gravity] <the criticism the PC will discuss>
[Realistic odds] <calibrated vs the ~65% resubmission acceptance base rate>
[Action] <revise seriously / fix framing / withdraw and re-route>
```
