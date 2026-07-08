---
name: isca-workflow
description: Use when planning a full ISCA campaign on a calendar — working back from the expected mid-November abstract and paper deadlines to freeze simulation evidence in time, staffing the winter two-round review wait, preparing for the February-March rebuttal and revision window, and branching to camera-ready, artifacts, and the June conference.
---

# ISCA Workflow

An ISCA year has one gate. Miss mid-November and the next identical opportunity is
twelve months away, which is why experienced groups treat the ISCA calendar as an
engineering schedule with the deadline as tape-out. This skill lays out that
schedule using the verified ISCA 2026 dates as the template; as of 2026-07-08 the
ISCA 2027 CFP was not yet posted, so every 2027 date below is an expectation to
confirm against `iscaconf.org/isca2027/` the moment it exists (待核实).

## The verified 2026-cycle skeleton

| Milestone | ISCA 2026 date (verified) | What it means operationally |
|---|---|---|
| Abstract registration | November 10, 2025 | Title, abstract, authors, conflicts locked in HotCRP; paper content still fluid |
| Full paper | November 17, 2025 | The reviewed PDF — one week after abstracts, so the abstract week is a writing week, not a buffer |
| Round 1 reviews due | December 19, 2025 | First reviewer wave completes before the holidays |
| Round 2 reviews due | February 13, 2026 | Additional reviews on papers that advanced |
| Rebuttal + revision | February 16 - March 6, 2026 | Authors see reviews, respond, and may revise — a three-week working window |
| Conference | June 27 - July 1, 2026 (Raleigh, NC) | Presentation; artifact badges resolved before publication |

Industry-track submissions ran about a month behind (abstracts December 5, papers
December 12, 2025). Final notification date for 2026 was not captured in this
pack's verification — 待核实.

## Working backward from November

Count in weeks from the expected paper deadline (call it P, likely mid-November
2026 for ISCA 2027):

- **P minus 16 weeks (late July):** venue decision final (`isca-topic-selection`);
  simulation or prototype infrastructure chosen and validated
  (`isca-experiments`); the one-sentence claim written on the whiteboard.
- **P minus 10 weeks:** baseline configurations frozen and reproduced from scratch
  by a second person. Baseline drift discovered later invalidates every downstream
  number.
- **P minus 6 weeks:** main-result experiments complete. From here, compute goes to
  sensitivity studies and reviewer-anticipation runs, not to the headline.
- **P minus 4 weeks:** full draft exists — bad prose, complete structure. Internal
  "mock PC" read by two colleagues who did not build the system.
- **P minus 1 week (abstract deadline):** title/abstract/topics/conflicts final in
  HotCRP. The abstract steers reviewer assignment; write it for bidding, not as a
  placeholder.
- **P:** upload per `isca-submission`, then freeze the artifact snapshot that
  matches the submitted numbers (`isca-reproducibility`).

## The winter: silence, then three loud weeks

Between November and mid-February the authors' only jobs are (a) keep the
evaluation environment resurrectable and (b) pre-build rebuttal ammunition: the
five most likely objections, each with a ready experiment or a pointer into the
submitted PDF. The 2026 cycle then opened a combined **rebuttal/revision period**
(February 16 - March 6) — unusually long by conference standards precisely because
ISCA lets authors *change the paper*, not just argue about it. Staff those three
weeks like a sprint: compute reserved, coauthors on call, no conference travel
booked. Details of what to do inside the window live in `isca-author-response`.

## Branch plans after notification

- **Accept:** camera-ready under the edition's publisher workflow
  (`isca-camera-ready`), voluntary artifact submission (`isca-artifact-evaluation`),
  talk and travel for late June.
- **Reject with salvageable reviews:** map every misunderstanding to the sentence
  that permitted it; decide MICRO (spring gate) vs HPCA (summer gate) within two
  weeks while the reviews are fresh.
- **Reject with a fit objection:** rerun `isca-topic-selection` honestly — the
  committee may have told you the paper's true venue.

## Team ledger

Keep a single tracking file in the paper repo; every risk has one owner.

```yaml
# isca-campaign.yaml
target: ISCA 2027            # 54th by arithmetic - ordinal 待核实
gate:
  abstract: TBD-2026-11      # confirm on iscaconf.org/isca2027 when live
  paper:    TBD-2026-11
  source:   "not yet posted as of 2026-07-08"
owners:
  claim_and_story:   <name>   # one sentence, defended weekly
  simulation_infra:  <name>   # versions pinned, configs archived
  baselines:         <name>   # frozen P-10w, independently reproduced
  writing:           <name>   # draft complete P-4w
  submission_admin:  <name>   # HotCRP, conflicts, template, metadata
  rebuttal_reserve:  <name>   # compute + calendar hold, mid-Feb to early Mar
checks:
  - abstract written for reviewer bidding, not filler
  - artifact snapshot tagged at submission commit
  - mock-PC read completed and objections filed
  - fallback venue named with trigger condition
```

## Failure modes this calendar prevents

- **The November collision:** abstract and paper a week apart means groups that
  planned "we'll write after the abstract" write the whole paper in seven days.
  The P-4w draft rule exists for this.
- **The dead environment:** rebuttal-window experiments that fail because the
  simulator tree no longer builds in February. Tag and containerize at submission.
- **The unstaffed revision:** ISCA's revision option is leverage only for teams
  that can produce new results in days; treat the window as scheduled work.
- **The stale retarget:** rejected papers resubmitted unchanged to MICRO carry
  their ISCA reviews' fingerprints; committees overlap. Budget a real revision.

## Milestone-to-skill routing

| When you are at... | Open... |
|---|---|
| Venue decision (P-16w) | `isca-topic-selection`, exemplars library |
| Infrastructure setup | `isca-experiments`, `isca-reproducibility` |
| Drafting (P-6w to P-1w) | `isca-writing-style`, `isca-related-work`, `isca-supplementary` |
| Upload week | `isca-submission` (twice: abstract step, paper step) |
| Winter wait | `isca-review-process` |
| February window | `isca-author-response` |
| Post-decision | `isca-camera-ready`, `isca-artifact-evaluation`, or the retarget branch |

All dates above are the 2026-cycle record
(`../../resources/official-source-map.md`, checked 2026-07-08). Confirm the 2027
calendar, page rules, and review mechanics on the official site before acting on
any of them.
