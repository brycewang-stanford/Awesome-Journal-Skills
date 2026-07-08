---
name: iccv-submission
description: Use when auditing an ICCV submission in the weeks before the early-March deadline, covering OpenReview registration and profile completeness, the single same-day paper-plus-supplement upload, the 8-page inclusive format, the 25-submissions-per-author cap, every-author reviewer enrollment, anonymity and media-embargo rules, and desk-reject triage.
---

# ICCV Submission

This is the pre-flight audit for an ICCV upload. Anchors are the ICCV 2025 cycle
(registration March 3; paper **and** supplementary material March 7, 2025, 11:59pm
HST; verified via official-page renderings on 2026-07-08). The 2027 cycle had
published no instructions at check time — re-read the live Author Guidelines,
Dates, and Submission Checklist pages before acting on any number below.

## One upload event, not two

ICCV 2025 deliberately merged what its CVF siblings stagger: the main paper and
the supplementary archive were due together. The consequences for your audit:

- The supplement must pass the same review-readiness bar as the paper *on the same
  night* — schedule its freeze for the same internal deadline.
- There is no post-deadline week to render videos, scrub code, or fix a corrupt
  zip. A supplement that fails to upload is simply absent from review.
- Registration (title, abstract, author list, complete OpenReview profiles for
  everyone) closes days earlier. After it, you cannot add authors casually — the
  list you register is the list you defend.

## The three caps to check mechanically

| Cap | 2025 value | Consequence of violation |
|---|---|---|
| Page budget | 8 pages including figures and tables; extra pages for cited references only | Rejected without review |
| Per-author submissions | 25 registered papers per author | Excess submissions desk-rejected by the PCs |
| Rebuttal (later) | One page, official template | Longer responses not read — plan evidence density now |

The 25-paper cap sounds unreachable until a big-lab PI's name is on thirty
submissions; confirm every senior coauthor's count *before* registration day.

## Reviewer enrollment is part of this form

Submitting to ICCV 2025 enrolled **every author** as a reviewer unless they held
another conference role or were exempted as new to / outside the vision community.
Enforcement was real: the 2025 PCs desk-rejected 29 papers because 25 of their
authors reviewed irresponsibly (one-sentence reviews, LLM-generated reviews,
reviews ignoring most of the paper), including 12 papers that would otherwise have
been accepted. Your submission audit therefore includes a people audit: which
coauthors will carry review load in March–May, and who checks their drafts.

## Anonymity, ICCV wording

- Double-blind throughout paper and supplement: no author names, affiliations,
  acknowledgements, grant numbers, or identifying dataset paths.
- **arXiv is explicitly tolerated**: posting a preprint is not an anonymity
  violation on the authors' part, and reviewers are instructed accordingly.
- **Your public codebase is different**: the 2025 guidance says do not cite it —
  write "code will be made publicly available" instead of linking a repo whose
  owner field is your lab.
- **Media embargo**: papers under review may not be pitched to or discussed with
  media until acceptance; a violation removes the paper from the conference and
  proceedings.
- GitHub documents are not publications under the dual-submission policy — a
  public repo does not make your work "previously published," and equally does not
  license a substantially similar manuscript under review elsewhere.

## Mechanical sweep, deadline week

```bash
# Run against the final PDF and the supplement archive together
pdftotext iccv_final.pdf - | grep -niE 'acknowledg|grant no|our (code|repo) at|github\.com/[a-z]' | head
pdfinfo iccv_final.pdf | grep -iE 'author|creator|title'         # metadata identity
unzip -l supplement.zip | grep -iE '\.git|DS_Store|home/|users/' # path leaks in the archive
grep -rn 'setlength\|newgeometry\|baselinestretch' *.tex          # style tampering tells
pdftotext iccv_final.pdf - | grep -c ''                           # >0 lines: text layer intact
```

Every hit is a blocker, not a judgment call: formatting violations and identity
leaks are rejected without review at CVF venues, and no discussion phase exists to
appeal a desk reject.

## Form fields that bite at midnight

OpenReview fields deserve a dry run a full day early. The abstract you registered
on registration day drives reviewer bidding — if the paper's framing shifted since,
update the field to match the PDF exactly. Subject areas route the paper to its
reviewer pool: pick the areas whose reviewers you *want*, not every area the paper
touches. Conflicts must be complete for all authors; a missing conflict discovered
in May cannot be fixed. And the HST timezone (2025) is a gift only to teams who
noticed it — put the *converted local time* in the calendar, with a two-hour pad.

## Triage table for the final 48 hours

| Finding | Action | Deadline sensitivity |
|---|---|---|
| A coauthor's OpenReview profile incomplete | That author completes it now; profiles were required at registration | Hard stop at registration day |
| Page 9 has a caption tail or appendix line | Recut; only references may overflow | Hard stop at paper deadline |
| Supplement references "Sec. F" that does not exist | Fix pointer or add section | Same night — no supplement week |
| Repo link in a footnote | Replace with availability statement | Same night |
| Senior coauthor at 26 registered papers | Withdraw one before the PCs choose for you | Registration day |
| Abstract field ≠ PDF abstract | Paste PDF version into form | Same night |

## Withdrawal is also a form action

If the paper must come out of the pool — a fatal bug found in April, a
dual-submission conflict discovered late — withdraw through OpenReview rather
than silently abandoning it: an unwithdrawn broken paper still consumes three
reviewers' labor at a venue that measures reviewer load in the tens of
thousands, and it stays attached to your OpenReview identity. Withdrawn ICCV
2025 papers with at least one completed review round also fed the Findings
pipeline (`iccv-review-process`), so withdrawal timing can affect that option.

## Cycle-volatility ledger

Reopen the current pages for: both deadline dates and their timezone; whether the
unified paper+supplement deadline persists; the exemption wording for reviewer
enrollment; the per-author cap; supplement size/format limits (unverified even for
2025 — 待核实); and the Submission Checklist page the 2025 cycle published, which
is the closest thing to an official version of this skill.

## Output format

```text
[Submission verdict] go / go-with-fixes / no-go
[Registration] profiles+authors+abstract locked by: <date>
[Caps] pages OK / author-counts OK / template untouched
[Anonymity] sweep hits: <none or list>
[Supplement] frozen same-night: yes/no; pointers resolve: n/m
[Duty exposure] reviewing coauthors identified: yes/no
[Fix order] <blockers first, then risks>
```
