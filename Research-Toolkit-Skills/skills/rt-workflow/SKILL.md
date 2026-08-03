---
name: rt-workflow
description: Use to sequence a manuscript across venues — which cross-journal toolkit skill to invoke next, from picking a target journal through execution, submission-readiness, simulated review, rebuttal, and the replication package. Routes; it does not replace the per-journal depth packs or the specialized toolkit skills.
---

# Cross-Journal Workflow Router (rt-workflow)

The author-side loop that runs *across* journals, complementing the per-journal depth
packs (which answer "how do I clear THIS venue's bar?"). Each step is backed by a
canonical capability doc in `shared-resources/`.

## When to trigger

- You have a result/draft and don't yet know the venue, or just got a reject and need the next target.
- You are mid-project and want the next cross-journal step.
- You want the end-to-end sequence: pick → execute → ready → rehearse → submit → rebut → replicate.

## The loop (and the skill that owns each step)

1. **`rt-journal-match`** — profile the paper → ranked reach/match/safe shortlist + resubmission ladder.
2. **`rt-venue-reframe`** — when the target changes (a reject, or a switch), diff the manuscript from the old venue's framing to the new one.
3. **`rt-execution-bridge`** — run the analysis through the StatsPAI / Stata MCP tools (estimate + audit), not just advise it.
4. **`rt-submission-readiness`** — go/no-go scorecard on the manuscript against the target venue's bar.
5. **`rt-desk-reject-risk`** — score the draft against the target's own documented desk-reject triggers before uploading.
6. **`rt-simulated-referee`** — rehearse a calibrated AE + referee panel; surface the decisive objections before a real referee does.
7. **(fix)** — route each objection back to the target pack's skill + the execution bridge.
8. **`rt-response-to-referees`** — after an R&R, draft the point-by-point reply + revision plan (editor first).
9. **`rt-replication-package`** — assemble + validate the Data-Editor package against the venue's data-and-code policy.

## Routing table

| Symptom | Go to |
|---|---|
| "Where should I send this?" / "Rejected — what next?" | `rt-journal-match` |
| "What has to change to send it to X instead?" | `rt-venue-reframe` |
| "I need to actually run the DiD/IV/RDD/SCM/DML, not just plan it" | `rt-execution-bridge` |
| "Is it ready to submit?" | `rt-submission-readiness` |
| "Will the editor desk-reject this?" | `rt-desk-reject-risk` |
| "What will referees attack?" | `rt-simulated-referee` |
| "I have an R&R to answer" | `rt-response-to-referees` |
| "The Data Editor needs a replication package" | `rt-replication-package` |

## How it relates to the per-journal packs

This router sequences the *cross-journal* steps; the **venue bar and all live facts**
(fees, limits, acceptance, data policy, house style) come from the chosen pack's own
skills and `resources/official-source-map.md`. Always defer venue-specific judgment to
that pack — this toolkit picks the venue, runs the analysis, and rehearses the gauntlet.

## Anti-patterns

- Submitting before `rt-submission-readiness` clears the mechanical bar.
- Picking a venue without reading its live source-map facts (`rt-journal-match` hard rule).
- Treating the simulated referee as a verdict rather than a rehearsal.

## Output format

```
【Current step】pick / execute / ready / rehearse / respond / replicate
【Next skill】rt-...
【Why】one line
【Venue bar source】<target pack>/resources/official-source-map.md + skills
```
