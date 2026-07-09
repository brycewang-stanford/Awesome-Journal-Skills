---
name: acmmm-workflow
description: Use when planning the end-to-end ACM MM (ACM Multimedia) campaign calendar — from thematic-area scoping and track choice, through the April OpenReview abstract/paper/supplement chain, the June anonymous rebuttal, the July decision, the August camera-ready, and the November presentation in Rio, with the right skill invoked at each stage.
---

# ACM MM Workflow

Use this to run an ACM Multimedia submission as a scheduled campaign rather than a
deadline scramble. The SIGMM calendar has a long gap between the April submission chain and
the July decision, so the work clusters at the front and the back.

## The ACM MM calendar (2026 anchors, AoE)

| Phase | 2026 date | What must be true | Skill |
|---|---|---|---|
| Scope + track choice | pre-March | Contribution is cross-modal; thematic area and track chosen | `acmmm-topic-selection` |
| Draft + evidence | March | First page leads with the multimedia claim; ablations planned | `acmmm-writing-style`, `acmmm-experiments` |
| Abstract | Mar 25 | Abstract registered in OpenReview | `acmmm-submission` |
| Paper | Apr 1 | 6–8 sigconf pages, anonymous, final PDF | `acmmm-submission` |
| Supplement | Apr 8 | Media/appendix package, anonymous, plays | `acmmm-supplementary` |
| Rebuttal | ~Jun 4 | Anonymous response, small confirmatory results | `acmmm-author-response` |
| Notification | ~early Jul | Decision + tier | `acmmm-review-process` |
| Camera-ready | ~Aug 6 | De-anonymized ACM version, artifact released | `acmmm-camera-ready` |
| Conference | Nov 10–14 | Registered; media-ready talk/poster | `acmmm-camera-ready` |

Treat these dates as the 2026 snapshot; reopen the current site each cycle. Note the 2026
notification date was listed inconsistently (July 7 on the CFP vs. July 9 elsewhere).

## Front-loaded work (before April)

The April chain is unforgiving because three deadlines land in eight days. Do the slow work
early:

- Lock the **thematic area and track** — they set format and blinding, and switching late is
  expensive.
- Build the **cross-modal evidence**: matched baselines and the leave-one-modality-out
  ablation that proves the fusion matters.
- Plan any **user study** now; recruiting raters cannot be done in the final week.
- Draft so the first page already leads with the multimedia contribution.

## The three-deadline sprint

```text
T-14d: freeze claims; media assets rendering from scripts
T-7d:  body fits 6-8 sigconf pages; references on overflow pages only
Mar 25: abstract registered (do not miss the earliest deadline)
Apr 1:  paper PDF final, anonymous, metadata-clean
Apr 8:  supplement packaged, anonymous, media plays for a stranger
```

## The long gap and the rebuttal

Between April and June, prepare the confirmatory experiments a reviewer is likely to ask for
(the missing baseline, the extra ablation) so the June rebuttal is a matter of *reporting*
results, not scrambling to run them.

## Back end (July–November)

- On acceptance, de-anonymize, complete ACM rights/CCS, and release the public artifact.
- Register early and plan travel to **Rio**; visas and international logistics are the usual
  failure.
- Build a presentation that **plays the media** — the seam between modalities should be
  seen/heard, not just described.
- On rejection, use the reviews to re-target: MM Asia, ICMR, a workshop, or next year's MM.

## Risk register

| Risk | Where it bites | Mitigation |
|---|---|---|
| Missing the abstract deadline | Mar 25 forecloses the paper | Register the abstract days early |
| Wrong track blinding | Desk reject | Confirm the track call before formatting |
| Fusion not shown to matter | Reviews / rebuttal | Run the leave-one-modality-out ablation pre-submission |
| User study not recruited in time | Perceptual claim unbacked | Start recruiting before April |
| Broken anonymous media link | Lost evidence in review | Test the mirror from a clean machine |
| Rio travel/visa delay | Cannot present | Start visa paperwork at acceptance |

## Re-targeting after a rejection

An ACM MM rejection is not the end of the work. Match the reviews to the next move: a
retrieval-leaning paper can go to **ICMR**; a systems-leaning one to **MMSys**; a regionally
scoped or earlier-stage result to **ACM Multimedia Asia** or a **workshop**; a matured version
to the **ACM TOMM** journal or next year's ACM MM. Fix the decisive critique — usually the
cross-modal-significance one — before resubmitting anywhere.

## Output format

```text
[Current phase] <scope/draft/abstract/paper/supplement/rebuttal/decision/camera-ready/conference>
[On track?] yes / at-risk: <what slips>
[Next deadline] <date + deliverable>
[Active skill] <which skill to run now>
[Risks] <ordered>
```
