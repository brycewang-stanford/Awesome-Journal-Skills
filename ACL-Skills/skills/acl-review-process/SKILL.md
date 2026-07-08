---
name: acl-review-process
description: Use when reasoning about how an ACL paper travels through ACL Rolling Review and conference commitment, covering reviewer and area-chair roles, meta-reviews, the commitment decision by senior area chairs and program chairs, Findings versus main-conference outcomes, ethics review escalation, and resubmission strategy across cycles.
---

# ACL Review Process

Use this to model where an ACL paper actually is and who decides what next.
ACL decoupled reviewing from the conference: ARR produces the review package;
the conference consumes it. Confirm current mechanics at
aclrollingreview.org/reviewing, since cycle structure has changed repeatedly
(most recently to 10-week cycles in 2025).

## The pipeline, stage by stage

1. **ARR cycle intake**: submission on OpenReview to a dated cycle (e.g.,
   ARR January 2026); checks for format, Limitations, checklist, anonymity.
2. **Review**: at least three reviewers score and write reviews.
3. **Author response + discussion**: authors reply; reviewers discuss and may
   update reviews (see `acl-author-response`).
4. **Meta-review**: the action editor / area chair synthesizes reviews into a
   meta-review with a recommendation. Notably, ARR senior area chairs do *not*
   make accept/reject recommendations — that authority sits with the venue.
5. **Commitment**: authors choose whether and where to send the finished
   package — ACL, or another \*ACL venue accepting that cycle.
6. **Venue decision**: the conference's senior area chairs and program chairs
   read reviews + meta-review and decide: main conference, Findings, or reject.
7. **Ethics branch**: papers flagged during review go to an ethics committee,
   which can require revisions or recommend rejection on ACL Code of Ethics
   grounds independent of technical merit.

## Who decides what

| Actor | Controls | Cannot do |
|---|---|---|
| Reviewer | Review text, scores, discussion updates | Accept or reject anything |
| AC / action editor | Meta-review, review-issue handling | Bind the conference's decision |
| Author | Response, revision, where/whether to commit | Change reviews after the cycle closes |
| Venue SACs + PCs | Main/Findings/reject from the ARR package | Re-run the reviewing itself |
| Ethics committee | Ethics-based conditions or rejection | Judge technical contribution |

## Outcomes and what they mean

- **Main conference**: full acceptance with a presentation slot.
- **Findings of ACL**: peer-reviewed, Anthology-published acceptance for solid
  work that missed the main-program bar; typically without a main-stage oral.
  Citation-wise Findings papers perform respectably — treat it as a real
  publication decision, not a consolation to appeal.
- **Reject at commitment**: the ARR reviews remain attached to the paper's
  history; a stronger resubmission through a later cycle is the designed path.

## Reading your review package strategically

- Weigh the meta-review over individual scores: it is the document venue
  chairs actually read.
- A package with one detailed negative review and a meta-review that endorses
  the objection rarely survives commitment — fix the objection in a new cycle
  instead of shopping the package to another venue unchanged.
- Conversely, mediocre scores with a meta-review noting resolved concerns can
  be worth committing: the venue decision is made on the whole record.
- A meta-review score at the floor triggers the resubmission constraint:
  within six months, only a wholesale revision avoids desk rejection.

## Venue-shopping within the ARR ecosystem

The same review package can be committed to exactly one venue at a time, but a
rejected or withheld package can target a later conference (EMNLP, EACL,
NAACL, AACL) whose commitment window accepts that cycle. Sequence deliberately:
each conference publishes which ARR cycles it accepts, and reviews age — a
package built on a two-cycle-old baseline set gets punished at commitment.

## Anatomy of one 10-week cycle

```text
week 0      submission deadline (AoE)
weeks 1-2   desk checks; reviewer + AC assignment
weeks 3-5   reviewing
week 5      reviews released -> author response (a few days)
week 6      reviewer discussion; reviews may be updated
weeks 7-8   meta-review written
~week 10    package complete -> commitment window for eligible venues
```

Offsets drift by cycle; the January 2026 cycle ran Jan 5 → reviews by early
March → ACL 2026 commitment March 14. Always re-derive from the current
dates page.

## Reading reviewer language for what it predicts

- "The contribution is unclear" from two reviewers predicts a meta-review
  hedge — fix framing in the response, not just individual complaints.
- "Missing citation X, Y, Z" alone rarely sinks a paper; the same list
  attached to "novelty over X is marginal" usually does.
- A confident low-score review with factual errors is the best target for
  a review-issue flag plus a surgical rebuttal.
- Uniform middling scores with short reviews often mean poor reviewer fit;
  at commitment, venue chairs weigh the meta-review's own reading more —
  make sure the response arms the AC with the paper's best case.

## Confidentiality and conduct boundaries

- Review content is confidential to the cycle; quoting reviews publicly
  (even anonymized) before decisions violates ARR expectations.
- Contacting reviewers or guessing identities is out of bounds; all
  communication flows through the OpenReview thread and the AC.
- Authors are bound by the ACL code of ethics throughout — including in
  how the author response characterizes reviewers' competence.
- Deadlines inside the cycle (response, discussion) are short and rarely
  extended; plan around them rather than requesting exceptions.

## Output format

```text
[Stage] cycle-intake / under review / response / meta-review / commit-window / venue decision / ethics review
[Package strength] <meta-review thrust + score pattern>
[Commit recommendation] commit to ACL / hold for revision / target sibling venue
[Ethics exposure] <flag risk and mitigation>
[Next actor to influence] <reviewer via discussion / AC via response / venue via commitment note>
```
