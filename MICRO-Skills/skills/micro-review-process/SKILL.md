---
name: micro-review-process
description: Use when reasoning about how a MICRO submission is judged — the double-blind HotCRP pipeline from the April deadline through the June rebuttal/revision window to the early-July notification, what reviewers score in a microarchitecture paper, the professional-conduct rules, and how the new Industry Track review differs.
---

# MICRO Review Process

Model of the pipeline a MICRO submission enters, anchored to the 2026 (59th) cycle
as verified 2026-07-08. Committee composition and internal mechanics vary by year
and are only partly public — items marked 待核实 must be reconfirmed on
`microarch.org/micro59/` before being repeated as fact.

## 2026 cycle timeline (verified)

| Gate | Date | Notes |
|---|---|---|
| Abstract registration | March 31, 2026, 11:59 PM EDT | Hard gate for paper upload |
| Full paper | April 7, 2026, 11:59 PM EDT | HotCRP: `micro2026.hotcrp.com` |
| Rebuttal / revision window | **June 3–17, 2026** | Two weeks — unusually long |
| Notification | July 7, 2026 | |
| Camera-ready | September 11, 2026 | |
| Symposium | Oct 31 – Nov 4, 2026, Athens | |

The eight-week gap between upload and rebuttal is when reviews are written; the
three weeks after the window close is discussion and the decision meeting.

## What the process is known to enforce

- **Double-blind, end to end.** Anonymity obligations persist through the
  rebuttal/revision window; artifact links stay anonymized the whole time.
- **Format policing with teeth.** Submissions are inspected visually and
  automatically; violations can reject a paper even after the HotCRP checker
  passed it (see `micro-submission`).
- **A professional-conduct clause covering both directions.** The 2026 guidelines
  state that abusive or inappropriate language in reviews, comments, *or rebuttals*
  can be grounds for dismissing reviewers, rejecting papers, and reporting to ACM
  and IEEE. Anger in a rebuttal is not just ineffective at MICRO — it is enumerated
  as a rejection ground.
- **A separate Industry Track review.** The inaugural 2026 track advertises a
  review process tailored to production work — evidence standards that accommodate
  proprietary constraints. Main-track novelty framing and industry-track deployment
  framing are different games; know which one your paper entered.

## What reviewers weigh in a microarchitecture paper

Composite of the community's public reviewing norms (not a quoted rubric — 待核实
against any published review form for the current cycle):

1. **Mechanism novelty and clarity** — is there a new hardware idea, stated at
   implementable precision?
2. **Methodology credibility** — simulator, baseline strength, workloads, sampling;
   the fastest score-killer in this community.
3. **Evidence-claim match** — simulation claims sized to simulation fidelity
   (`micro-experiments` instrument ladder).
4. **Cost honesty** — storage/area/power/latency accounting present and plausible.
5. **Significance** — does the headroom captured justify silicon change; would
   anyone build it?

A practical corollary: reviewer expertise at MICRO skews toward *methodology
forensics*. Expect at least one review that reconstructs your simulator config from
the paper and interrogates the discrepancies.

## Reading the outcome space

MICRO 2026's public timeline names one rebuttal/revision window and one
notification date; whether the cycle offered conditional accepts or shepherding is
待核实. Plan against the simple model:

```text
accept    -> camera-ready sprint (Sept 11) + artifact evaluation decision
reject    -> triage: fixable-methodology vs wrong-venue vs insufficient-headroom
             next slots: ASPLOS Sept 9 '26 · ISCA Nov 17 '26 · HPCA July '27 · MICRO Apr '27
resubmit rule: fix what reviews falsified, re-verify every date on live pages
```

Keep the reviews regardless of outcome — architecture PCs overlap heavily across
MICRO/ISCA/HPCA/ASPLOS, and a resubmission that ignores prior reviews may meet its
own reviewer again.

## Anatomy of a typical architecture review

Expect each review to contain, in some order: a summary paragraph (check it — a
wrong summary means the paper failed to communicate, and the rebuttal's first job
is a polite correction), a strengths list, a weaknesses list where methodology
items dominate, and detailed questions. Useful triage signals:

- A review whose weaknesses are all *questions* is winnable in rebuttal; a review
  whose weaknesses are all *assertions* needs numbers to move.
- The most senior-sounding review is not automatically the decision driver; the
  review with the most specific methodology engagement usually is.
- Uniform mid-scores with shallow text often mean the paper landed outside every
  reviewer's exact expertise — a topic-checkbox lesson for the resubmission.

Score scales, reviewer counts, and whether an online discussion precedes the PC
meeting are internal mechanics that vary by year: 待核实, do not assume.

## Leverage points for authors

- **Before submission:** topic checkboxes in HotCRP (steer toward mechanism
  expertise), abstract quality (bidding happens on it), format cleanliness.
- **During review:** nothing. Do not update linked repos in identifying ways; the
  submission is frozen.
- **Rebuttal window:** the only mid-process input — see `micro-author-response`
  for how to spend two weeks well.
- **After notification:** AE participation (badges strengthen the published
  record), Top Picks nomination season (IEEE Micro selects from the year's
  architecture papers).

## Calibrating expectations

Flagship-architecture acceptance rates historically sit in the high-teens to
low-twenties percent (exact per-year figures 待核实 from PC-chair reports or the
proceedings front matter — do not quote a number without a source). The planning
consequence is not pessimism but *lattice thinking*: a strong paper's expected
path to publication is one to two cycles across the four venues, which is why
`micro-workflow` treats every submission as having a plan B with a date on it,
and why reviews — even from a rejection — are the highest-value artifact the
process returns.

## Output format

```text
[Stage] pre-submission / under review / rebuttal window / post-notification
[Days to next gate] <N days to date, per verified timeline>
[Reviewer-lens self-score] mechanism / methodology / evidence-match / cost / significance: 1-5 each
[Conduct check] rebuttal tone professional: yes / revise
[Outcome plan] accept path + reject path both written: yes / no
[待核实 before quoting] <items to reconfirm on microarch.org>
```
