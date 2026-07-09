---
name: iros-review-process
description: Use when reasoning about IROS peer review — the PaperPlaza Associate-Editor/Editor pipeline, the traditional no-rebuttal single-notification model, how the video and embodied evidence steer reviewers, the 2026 double-anonymous posture, decision criteria for systems papers, and IEEE Xplore proceedings outcomes.
---

# IROS Review Process

Use this to reason about review-stage strategy. Reopen the current CFP, PaperPlaza instructions, and any
reviewer guidelines before making process claims — IROS review mechanics are set per edition by the
co-sponsoring IEEE/RSJ committee.

## Process model

- Submission and review run on **PaperPlaza**. Papers are handled by an **Associate Editor** under an
  **Editor**, who assign and synthesize reviews; there is no standing editor-in-chief for the conference.
- Reviewers are **embodied-systems researchers**. They weigh hardware, task distributions, trial counts,
  failure analysis, and sim-to-real honesty at least as much as a clean plot.
- The **video is read as evidence**: many reviewers watch it before the text, so a weak or misleading
  video colors the whole review.
- The **2026 cycle is double-anonymous**; author identity should not be inferable from text, figures, or
  video.
- Accepted papers go to **IEEE Xplore**, so camera-ready compliance and the copyright form matter as much
  as the initial decision.

## The no-rebuttal consequence

IROS has traditionally delivered **reviews together with the decision and no author-response phase**.
This changes strategy fundamentally: you cannot answer an objection after the fact, so **every
foreseeable objection must be pre-answered in the paper and the video**. The video functions as the only
asynchronous "rebuttal" a reviewer gets — a shown-and-labeled failure disarms the "did it really work?"
reviewer before they can write it down. Confirm the current cycle's policy before assuming a rebuttal
exists or does not.

## Scoring leverage table

| Review dimension | What raises it | What sinks it |
|---|---|---|
| Technical merit | A system that integrates cleanly and runs under a real constraint | A component swap dressed up as a system |
| Evidence | Trials, resets, failures, and a stated sim-to-real gap | A hero demo with no counts and no failures |
| Clarity | A system diagram and figures that carry the argument | An argument that needs an appendix IROS does not provide |
| Reproducibility | Hardware ledger, logs, honest availability | "Code coming soon" with no specs |

## Stage-by-stage realism

- Submission to notification is a **long silence** (spring to mid-June in 2026); there is no interaction
  to manage, only evidence to preserve for camera-ready.
- Notification arrives with the reviews; with no rebuttal, the lever is the **camera-ready revision** and
  the meta-review's requested changes.
- A single unresolved "I don't believe the robot did this" concern outweighs several resolved clarity
  nits, because embodied credibility is the currency here.

## Reject-to-next-venue realism

Because IROS is on the fall calendar, a reject can route to the next ICRA, to CoRL, or to an RA-L
submission with revision — decide by the reviews' substance, not by prestige.

```text
Reading a review packet:
  [ ] separate "the robot didn't convince me" from "writing unclear"
  [ ] list objections that a camera-ready edit can address vs cannot
  [ ] note every evidence gap the reviewers named for the next run
  [ ] pick the re-route (ICRA / CoRL / RA-L) if rejected, by substance
```

## Output format

```text
[Current stage] submitted / in-review / notified / camera-ready
[Decision actors] <Associate Editor / Editor / reviewers>
[Likely leverage] <integration / evidence / clarity / reproducibility>
[No-rebuttal implication] <what must be pre-answered in paper + video>
[Next move] <camera-ready edit or re-route>
```
