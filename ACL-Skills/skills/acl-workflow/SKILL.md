---
name: acl-workflow
description: Use when planning an ACL project calendar across ACL Rolling Review cycles, covering cycle selection against conference commitment windows, backward planning from an ARR deadline, the review-response-meta-review timeline, commitment decisions, resubmission loops to later cycles, and camera-ready through ACL Anthology publication.
---

# ACL Workflow

Use this as the project-management layer for an ACL paper. Unlike one-deadline
conferences, ACL runs on a **cycle-and-commit** rhythm: pick an ARR cycle, ride
its ~10-week review train, then decide at the commitment window whether to send
the package to the conference or loop back for another cycle.

ACL is a conference with rotating per-edition program committees, not a
journal: there is no standing editor and no APC. Costs are registration-based,
and Anthology publication is free and open access.

## The live edition: ACL 2027

ACL 2027 (65th edition, Kyoto, August 17-22, 2027) published its main-conference
call on September 29, 2026 (re-verified 2026-11-23):

| Milestone | Date (ACL 2027 call) |
|---|---|
| ARR January 2027 cycle submission | January 4, 2027 (AoE) |
| Eligible packages | January 2027 cycle or any earlier cycle |
| Commitment to ACL 2027 | TBA |
| Acceptance notification / camera-ready | TBA |
| Tutorials · workshops · main conference | Aug 17 · Aug 18-19 · Aug 20-22, 2027 |

ARR has not yet published the January 2027 cycle's review, response and
meta-review dates, so the offsets below come from the previous edition.

## The 2026 rhythm as a worked anchor

ACL 2026 (64th edition, San Diego, July 2-7, 2026) drew from the ARR October
2025 and January 2026 cycles:

| Milestone | Date (verified for ACL 2026) |
|---|---|
| ARR January cycle submission | January 5, 2026 |
| Reviews + meta-reviews to authors | by March 9-10, 2026 |
| Commitment to ACL 2026 | March 14, 2026 |
| Acceptance notification | April 4, 2026 |
| Camera-ready | April 19, 2026 |
| Conference | July 2-7, 2026 |

## Which cycle reaches which conference

The commitment table is the part authors get wrong, because it is set by ARR and not by
the conference: a cycle can only commit to the venues ARR lists against it, so "I will
aim for ACL" is a decision about *which month to submit to ARR*, often two or three
cycles ahead. As published on `aclrollingreview.org/dates` (re-verified 2026-11-23):

| Venue | Final ARR submission | Commitment |
|---|---|---|
| EMNLP 2026 · AACL 2026 | May 25, 2026 | August 2, 2026 |
| EACL 2027 | August 3, 2026 | October 11, 2026 |
| NAACL 2027 · COLING 2027 | October 12, 2026 | December 23, 2026 |
| **ACL 2027** (Kyoto, Aug 17-22, 2027) | **January 2027** (Jan 4 per the ACL 2027 call) | not yet posted |

Two things follow that a reader working from the 2026 anchor above would get wrong.
**No 2026 cycle is a first-submission route to ACL 2027** — the October 12 slot, the
last one on the 2026 calendar, commits to NAACL and COLING (its author response runs
November 24-30, meta-reviews December 17, cycle end December 20). A package already
reviewed in an earlier cycle can still be committed to ACL 2027, since the call accepts
"the January 2027 cycle or an earlier cycle". And ARR lists no 2027 cycle rows yet, so
a plan that needs the January cycle's author-response window cannot pin it yet.

Every date here is cycle-volatile, including the ones that are printed: re-read
`aclrollingreview.org/dates` before committing a team to any of them.

## Choosing a cycle

- Work backward from the conference you want: each \*ACL conference announces
  which cycles it accepts commitments from. The *earlier* eligible cycle
  buys a free resubmission shot at the *same* conference if reviews go badly.
- A cycle deadline you hit with a rushed paper is worse than the next cycle
  hit with a finished one — reviews persist and follow resubmissions.
- Mind the response window inside the cycle (a few days, roughly five weeks
  after submission): the team must be available then, not just at submission.

## Backward plan from a cycle deadline

| Weeks out | Milestone for an experiments-heavy NLP paper |
|---|---|
| 8 | Claim fixed; datasets, baselines, and evaluation protocol frozen |
| 6 | Main results in; error-analysis sampling started |
| 4 | Human evaluation fielded; ablations running |
| 3 | Full draft in ACL style; internal red-team read |
| 2 | Responsible NLP checklist drafted against the real paper |
| 1 | Limitations written; anonymity sweep; supplement archive built |
| 0 | Submit early on deadline day (AoE) |

## The resubmission loop

```text
cycle N reviews weak?
  -> revise (new experiments, rescoped claims)
  -> cycle N+1 submission WITH: link to prior submission,
     change summary, point-by-point response to old weaknesses
  -> commit the stronger package to the next eligible conference
```

Budget one loop into any plan that matters: the modal strong ACL paper today
has seen two cycles. Skipping the revision note is a desk reject; a floor
meta-review score forbids quick resubmission without wholesale revision.

## Post-decision branches

- **Main conference**: camera-ready sprint (see `acl-camera-ready`),
  registration, presentation prep, artifact release.
- **Findings**: same camera-ready track; decide early on the presentation
  option the edition offers and whether to present at an affiliated workshop.
- **Reject**: hold a post-mortem against the meta-review within a week while
  context is fresh; choose next cycle + venue deliberately, not reflexively.

## Coordination rules that save cycles

- One owner for the checklist, one for anonymity, one for the supplement —
  the three most common last-day failures are all ownerless tasks.
- Freeze a "submitted" tag in the repo: the author response may only cite
  what that tag contains.
- Calendar the response window and the commitment deadline the day you submit;
  both are short and both are missable.

## Running multiple papers through the machine

- Stagger sibling papers across cycles rather than stacking one deadline:
  the response windows will otherwise collide, and response quality is the
  highest-leverage hour-for-hour work in the pipeline.
- Track each paper as (cycle, state, target venue, fallback venue) — the
  fallback is a real decision because commitment windows do not wait.
- Reuse infrastructure deliberately: one anonymization script, one
  checklist template pre-filled with lab defaults, one supplement layout.
- Reviewer duty is now per submission: from the October 2026 cycle, ARR's
  sustainable reviewing policy guarantees review only to submissions naming a
  qualified service contributor (max 2 submissions each, registered within 48
  hours after the deadline); the rest go to a lottery and are desk rejected if
  not drawn. Caps: 20 submissions per author, 5 as first or joint-first author.
  Allocate contributors across the lab's papers before deadline week (verify
  the current cycle's policy — this has changed repeatedly).

## Signals to re-plan immediately

- The dates page announces a cycle-structure change (it has happened
  multiple times; 10-week cycles arrived only in May 2025).
- Your target conference posts its eligible-cycle list and your intended
  cycle is not on it.
- Reviews arrive with a fixable core objection and the next cycle's
  deadline is within two weeks — a rushed loop beats a stale package only
  if the fix is genuinely small.
- A competing preprint lands mid-cycle: plan the response-window framing
  and the camera-ready citation now, not at notification.

## Output format

```text
[Stage] planning / cycle-N under review / response window / commit window / accepted / revising
[Target] <conference + eligible ARR cycles, with dates and source>
[Critical path] <three tasks gating the next deadline>
[Loop budget] <cycles remaining before target conference>
[Owner map] <checklist/anonymity/supplement/response owners>
```
