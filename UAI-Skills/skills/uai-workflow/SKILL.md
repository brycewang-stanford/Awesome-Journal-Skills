---
name: uai-workflow
description: Use when planning a UAI cycle end to end, from venue-fit confirmation through the winter submission deadline, the spring review and author-response phases, the June decision, the July PMLR camera-ready, and the August conference, as one backward-planned calendar with named owners for anonymity, evidence, and packaging tasks.
---

# UAI Workflow

Use this as the project-management layer over the other UAI skills. UAI is a conference
run by the AUAI: there is no editor-in-chief and no rolling submission — one deadline
per year, per-edition chairs, and PMLR publication funded by registration rather than
author fees. The 2026 calendar below is the verified anchor (checked 2026-07-08);
substitute the current year's official dates before planning anything.

## The 2026 shape of a UAI year

| Phase | 2026 anchor | Owner-side work |
|---|---|---|
| Fit decision | months before | Confirm uncertainty is the contribution (uai-topic-selection) |
| Submission opens | Jan 25 | OpenReview profiles, conflicts, subject areas ready |
| Paper deadline | Feb 25, 23:59 AoE | Single PDF (8pp main + appendix), ≤15 MB, ZIP ≤50 MB |
| Bidding | Mar 2–9 | Nothing — routing was set by your abstract |
| Reviews written | Mar 21 – Apr 11 | Prepare response infrastructure; draft anticipated objections |
| Author response | Apr 23 – May 2 | Evidence-anchored replies (uai-author-response) |
| Reviewer–AC discussion | May 2–8 | Silence; the response argues for you |
| Notification | Jun 1 | Triage outcome; celebrate or re-route |
| Camera-ready | Jul 27 | PMLR files, public artifacts (uai-camera-ready) |
| Conference | Aug 17–21, Amsterdam | Tutorials Mon, main Tue–Thu, workshops Fri |

## Backward plan from the paper deadline

Offsets assume a probabilistic-methods paper with theory and experiments; shift for
your mix, and re-anchor to current official dates:

- **T−10 weeks**: contribution sentence frozen; identifiability/guarantee target named;
  ladder of experiments designed (exact-truth, stress, real).
- **T−8**: core theorem believed and sketched; assumption set labeled A1…An and no
  longer moving.
- **T−6**: exact-truth experiments done; the theorem's prediction visibly matches or
  the paper's story changes now, not at T−1.
- **T−4**: full draft in the UAI template; appendix skeleton mirrors main-text
  numbering; baselines tuned and logged.
- **T−3**: internal mock review against the four criteria (correctness, novelty,
  backing, clarity) by someone outside the project.
- **T−2**: stress and real-data experiments locked; determinism ledger and manifests in
  the artifact; supplementary ZIP assembled from a clean export.
- **T−1**: anonymity sweep of PDF and ZIP; page/size caps verified mechanically;
  OpenReview form fields drafted.
- **T−0**: upload early in the day AoE-wise; re-download and cold-read.

## Role assignments that prevent the classic failures

```yaml
# uai-cycle-owners.yaml — one name per row, no shared ownership
anonymity_sweep:      # PDF + ZIP + metadata; leaks are unfixable after the deadline
evidence_map:         # every claim -> exhibit; updated when any result changes
appendix_integrity:   # body statements == appendix statements after every edit
artifact_build:       # clean-export ZIP, manifest files, size cap
openreview_form:      # profiles, conflicts, subject areas, abstract == PDF abstract
response_marshal:     # archives submitted PDF; drafts objection bank before reviews
camera_ready:         # PMLR forms, de-anonymization, public repo tag
presentation:         # poster, spotlight, registration, travel/visa timeline
```

The two most damaging single points of failure at UAI specifically: an unowned
anonymity sweep (appendices inside the reviewed PDF widen the leak surface), and an
unowned appendix-integrity check (deadline-week edits to body theorems silently orphan
their proofs).

## Between decision and conference

- Accepted: the June-to-July window carries camera-ready, artifact publication, and
  registration simultaneously — assign them to different people on day one.
- Rejected: run the axis triage from `uai-review-process` within a week while context
  is fresh; the natural re-route targets (AISTATS, NeurIPS/ICML, CLeaR, or a journal)
  have their own calendars, and reviews in hand are an asset that depreciates.
- Either way: at least one author may be called to review for UAI — the volunteer
  agreement signed at submission — so protect reviewing bandwidth in March–April.

## The cycle archive

One deadline per year means institutional memory is the compounding asset. At each
transition, file into a shared, dated directory:

- The exact uploaded PDF and ZIP (deadline day) — responses must quote these.
- The OpenReview form contents as submitted (screenshot or export).
- All reviews, your responses, and the meta-review (decision day).
- The camera-ready as published, plus the PMLR entry once the volume is live.
- A one-page retrospective: which criterion drew fire, which anticipated objection
  materialized, what the next cycle should do differently.

Groups that skip the retrospective re-learn the same reviewer objection annually.

## Contingency table

| If this happens | Then | Because |
|---|---|---|
| Theorem breaks at T−3 | Demote it to a conjecture + empirical study, or pull the paper | A wrong proof fails correctness; a scoped claim can still pass backing |
| Key experiment unfinished at T−1 | Cut the claim, not the caveats | Claims without exhibits fail the backing criterion |
| Coauthor conflict list incomplete at deadline | Fix profiles before the form, even if tight | Conflict errors poison assignment invisibly |
| Reviews arrive harsher than expected | Run axis triage before drafting anything | Emotion-first responses waste the short window |
| Accepted but presenter cannot travel | Check the current remote-presentation rules immediately | 2026 said "physically or remotely", but details were 待核实 |
| Rejected with fixable-axis reviews | Target the next honest-fit deadline within the month | Review memory and momentum decay fast |

## First-cycle notes

For a group's first UAI attempt: budget one extra week for OpenReview profile setup
and conflict entry across all authors; expect the two-column template to shrink an
apparently-fitting draft by half a page; and have the mock reviewer score the four
posted criteria explicitly — first-time submissions most often lose on backing, not
on correctness.

## Standing warnings

- Never inherit dates from this file or from memory; the official important-dates page
  is the only calendar.
- Registration fees, in-person requirements, and remote-presentation options were not
  fully verifiable for 2026 at pack-check time (待核实) — confirm before booking travel
  or promising remote attendance.
- One-deadline venues punish schedule slips brutally: a week late here is a year late.

## Output format

```text
[Cycle position] fit / build / submitted / response / decided / camera-ready / conference
[Next hard date] <official date + source URL>
[Critical path] <three tasks gating the next transition>
[Owner gaps] <rows in the owner map without a name>
[Re-route plan] <standing answer to "if rejected, then where">
```
