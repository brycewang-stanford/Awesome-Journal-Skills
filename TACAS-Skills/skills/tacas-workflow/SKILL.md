---
name: tacas-workflow
description: Use when planning a TACAS (ETAPS) project timeline from category choice and venue fit through the EasyChair paper deadline, the mandatory tool-paper artifact deadline, the rebuttal window, notification, the voluntary post-acceptance artifact round, LNCS camera-ready, and presentation, with backward-planning offsets that account for TACAS's single annual round and its parallel paper+artifact review.
---

# TACAS Workflow

Use this as the project-management skill for a TACAS submission. Replace every date with the current
ETAPS joint schedule and work backwards from the **EasyChair paper deadline** — remembering that for
a **tool or tool-demonstration** paper a second, firm **artifact deadline** lands about two weeks
later and its evaluation runs **in parallel with the PC**. TACAS runs a **single annual review
round** on the shared ETAPS calendar (it does not use ESOP's two rounds), so missing the deadline
costs roughly a year.

TACAS is a conference whose proceedings are an open-access LNCS volume: it has **no standing
editor-in-chief** and **no author-facing APC**. Rotating leadership is the per-edition **PC chairs**
and the **ETAPS steering committee**; the cost model is registration, and ETAPS funds the gold open
access centrally. Chairs rotate yearly — re-check the current TACAS page rather than carrying a name
forward.

## The reported TACAS 2026 timeline (verify on the live page)

- **Paper submission:** 16 Oct 2025 (AoE).
- **Mandatory artifact** (regular tool + tool-demonstration): 30 Oct 2025.
- **Rebuttal / author response:** 8-10 Dec 2025.
- **Notification:** 22 Dec 2025.
- **Voluntary artifact** (accepted research + case-study): 8 Jan 2026.
- **Conference:** ETAPS 2026, Turin, 11-16 Apr 2026 (main conferences 13-16 Apr).

As of 2026-07-09 the TACAS 2026 edition has already taken place, so the **live next target is TACAS
2027** (ETAPS 2027, Copenhagen, 10-15 Apr 2027).

## Milestones

- **Venue + category fit:** confirm TACAS over CAV/VMCAI/FMCAD and pick the category
  (`tacas-topic-selection`) — this fixes the page limit, blind mode, and artifact obligation.
- **Evidence + tool lock:** freeze the algorithm/tool, the benchmark set, the baselines, and the
  artifact contents.
- **Submission:** upload the LNCS PDF via EasyChair; anonymize if it is a **research** paper.
- **Mandatory artifact (tool/tool-demo):** submit the clean-VM artifact on its firm deadline; it
  gates acceptance.
- **Rebuttal:** answer the reviews in the ETAPS response window.
- **Notification:** archive reviews and every submitted version.
- **Voluntary artifact (research/case-study):** if pursuing badges, submit after acceptance.
- **Camera-ready + presentation:** prepare the LNCS camera-ready, complete Springer rights, register,
  and present.

## Backward plan from the paper deadline

| Weeks out (heuristic) | Verification-tool milestone |
|---|---|
| 10+ | Category chosen; algorithm/tool feature-frozen; benchmark set and baselines chosen |
| 8 | Experiments run; wall-clock/scalability logged on stated hardware; soundness argument drafted |
| 6 | Comparison against the strongest baseline complete with equal budgets; results tables built |
| 4 | Full draft in `llncs.cls` within the page limit; **artifact assembled in the clean VM** |
| 3 | Internal mock review by a verification-literate reader; artifact dry-run on a fresh VM |
| 2 | Tool/tool-demo: freeze the artifact for its post-paper deadline; research: anonymity sweep |
| 1 | Final PDF check; EasyChair fields, category, conflicts complete |
| 0 | Submit paper; then (tool/tool-demo) submit the mandatory artifact on its firm date |

These offsets are planning heuristics only — anchor every one to the current ETAPS joint CfP, never
to a previous cycle.

## Failure modes by stage

- **Leaving the artifact to after the paper** for a tool/tool-demo paper — the mandatory artifact
  deadline is only ~two weeks out and a package that does not build on the ETAPS VM costs the paper.
- **Experiments still moving at week 4** forces last-minute benchmark runs nobody has audited — the
  classic unfair-comparison or unreproducible-result reject.
- **Anonymizing the wrong category** — stripping the tool name from a single-blind tool paper, or
  forgetting to anonymize a double-blind research paper.
- **Treating the rebuttal as decisive** — it corrects misreadings and supplies a missing number; it
  does not rewrite the paper.

## Coordination notes

- Assign one owner for the **artifact / clean-VM build** and another for the **paper**; for a tool
  paper these are two deadlines a fortnight apart and shared ownership is how the artifact slips.
- Archive the exact submitted PDF and artifact — the rebuttal and camera-ready must quote them.

## Output format

```text
[Current stage] idea / evidence / writing / submitted / rebuttal / notified / camera-ready / accepted
[Category] research / case-study / regular tool / tool-demonstration
[Next official deadline] <paper or mandatory-artifact date and source, or unknown>
[Critical path] <three tasks that determine readiness, incl. artifact for tool papers>
[Risk register] <category fit / page limit / anonymity / benchmark fairness / artifact-on-VM / presentation>
[Owner map] <task -> person or role>
```
