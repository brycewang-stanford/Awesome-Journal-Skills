---
name: sigir-workflow
description: Use when planning a SIGIR project calendar — backward-planning from the January-pattern abstract/paper deadlines to the July conference, sequencing evidence freeze, significance testing, and anonymization, coordinating multi-track decisions, and wiring the SIGIR/ECIR/CIKM/WSDM/SIGIR-AP fallback calendar into one pipeline.
---

# SIGIR Workflow

SIGIR is an annual single-cycle venue with a distinctive rhythm: recent editions
put the full-paper deadline in mid-January (2025: abstract Jan 16, paper Jan 23;
2026 trackers reported Jan 15/22 — exact dates 待核实 on the current Key Dates page),
notification in early spring, camera-ready in late April (Apr 29, 2026 verified for
Resources/LRE), and the conference in July (2026: July 20-24, Melbourne). Secondary
tracks stagger a few weeks behind the full-paper dates. Plan backward from the dates
you verify, and treat every date in this file as a pattern anchor, not a promise.

SIGIR is a conference run by ACM SIGIR (the special interest group): there is no
standing editor-in-chief — program leadership rotates per edition — and no
journal-style APC; costs arrive as registration and travel, with ACM Open status
determining any publication-fee exposure per institution (待核实).

## The annual shape

| Phase (pattern) | Months (recent cycles) | Owner's job |
|---|---|---|
| Track decision + scoping | Aug-Oct | Pick full/short/resource/repro target; freeze claim |
| Evidence build | Oct-Dec | Collections, baselines, runs, ablations |
| Writing + audits | Dec-Jan | Style, related-work, submission audits |
| Abstract → paper deadlines | mid-Jan | Metadata frozen a week early; PDF last |
| Review window | Feb-Mar | Response prep if a channel opens; next-venue scouting |
| Notification → camera-ready | Mar-Apr | TAPS pipeline, artifacts public |
| Conference | Jul | Presentation, community work |

## Backward plan from the paper deadline

| Weeks out | Milestone for a ranking/retrieval paper |
|---|---|
| 10+ | Claim frozen; collection lineup chosen against the claim's scope |
| 8 | Baselines reproduced at current strength, tuning protocol logged |
| 6 | Main results stable across seeds; ablation matrix running |
| 4 | Full draft in `sigconf`; significance script wired to run files |
| 3 | Internal mock review by an evaluation-minded reader |
| 2 | Repository mirror anonymized; PAPER_MAP written |
| 1 | Submission audit (`sigir-submission`); PC nominee confirmed; buffer |
| 0 | Abstract by its deadline, PDF by its deadline, both AoE |

The two-stage deadline is a real gate: the abstract registers title, authors, and
track, and late abstracts close the door regardless of PDF readiness. Freeze the
author list before the abstract — ACM authorship policy makes later changes painful.

## Multi-track coordination

Groups often have several irons: a full paper, a short paper from a side finding, a
resource from the data work. SIGIR's cross-track double-submission ban makes this a
planning problem, not just an ethics one:

- Assign each *contribution* to exactly one track before the abstract deadline.
- Stagger risk: if the full paper is rejected, which parts return as a short paper
  or resource paper next cycle? Write the modular repo accordingly.
- The Resources track's own calendar (2026: abstract Feb 5, notify Apr 2, camera
  Apr 29) runs weeks behind full papers — a rejected-dataset-chapter salvage plan
  is sometimes executable *in the same year*. Verify each cycle.

## The fallback calendar

IR has a dense venue ring, so a SIGIR reject waits weeks, not a year:

```text
Typical resubmission ring (verify each venue's current dates):
SIGIR (Jan deadline, Jul conf)
  -> CIKM     (~May/Jun deadline, Nov conf)   broader IR+KM+DB scope
  -> SIGIR-AP (~Jul deadline, Dec conf)       regional; has advertised an R&R route
  -> WSDM     (~Aug deadline, Feb/Mar conf)   web search + data mining angle
  -> ECIR     (~Sep/Oct deadline, Mar/Apr conf) European IR, full+repro tracks
  -> back to SIGIR (Jan)
Journal exits: TOIS / TOIS-adjacent for work that outgrew 9 pages.
```

Each hop costs a re-framing pass, not just a re-upload: CIKM wants the knowledge/
data-management angle sharpened, WSDM the web/user-data angle, ECIR welcomes
reproducibility framing. Budget one week per hop for venue-fit revision.

## Ownership map

Deadline collapses at SIGIR are usually ownership failures, not effort failures.
Assign by name, once, in the scoping phase:

| Deliverable | Single owner's duty |
|---|---|
| Run files + significance script | One person regenerates every table end-to-end |
| Baseline tuning log | Proves symmetry claims during review |
| Anonymization sweep | Names, logs, leaderboards, metadata, repo history |
| OpenReview metadata + PC nominee | Abstract-deadline gate; nominee agreed in advance |
| Camera-ready/TAPS | Starts the week of notification, not the week of the deadline |

Shared ownership of the anonymization sweep is the classic failure: everyone
assumes someone else checked the PDF metadata.

## Failure modes by phase

- **Claim still moving at week 6** → the collection lineup no longer matches the
  claim; scope-narrow now rather than during reviews.
- **Baselines start in week 4** → tuning symmetry becomes unprovable; this is the
  most-cited fatal review at this venue.
- **Anonymization at week 0** → leaderboard rows, repo history, and system names
  leak under deadline pressure (see `sigir-submission`).
- **Response window opens and nobody owns run files** → coordinate-based replies
  become impossible; archive the exact submitted PDF + runs at upload time.
- **Camera-ready collides with teaching/travel in April** → TAPS proofs get
  rubber-stamped; schedule the proof check like a review, not a formality.

## Output format

```text
[Current phase] scoping / evidence / writing / submitted / responding / camera-ready
[Verified dates] <each from the live Key Dates page, with URL + check date>
[Backward plan] next three milestones with owners
[Track map] contribution -> track, cross-track conflicts: none / <list>
[Fallback route] <next two venues with verified deadlines>
[Risk register] <top risk from the failure-mode list>
```
