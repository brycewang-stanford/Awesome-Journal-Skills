---
name: ieee-journal-on-selected-areas-in-communications
description: Use when targeting IEEE Journal on Selected Areas in Communications (JSAC) or deciding whether a communications-and-networking manuscript fits this venue. Encodes the journal's call-driven fit, the high-impact-and-topical bar, the route-by-active-call logic, house style, official-submission re-check, and desk-reject heuristics.
---

# IEEE Journal on Selected Areas in Communications (ieee-journal-on-selected-areas-in-communications)

## Journal positioning

IEEE Journal on Selected Areas in Communications (JSAC) publishes high-impact work at
the systems and networks frontier of communications, organized largely around
**topical special issues defined by current calls for papers** — next-generation
wireless, networking, security, optical and quantum communication, and
machine-learning-for-communications, among others. Unlike a broad-scope transaction,
JSAC's fit is set by the active call: a paper must match a specific issue's theme and
clear a bar of impact and timeliness, not merely be technically correct. Routine,
incremental results — even sound ones — that do not advance a call's frontier are a
poor fit. This skill is a **fit / venue-selection / re-framing** tool. It does not
replace the journal's current official author guidelines or any call's specific
instructions. Before submitting, re-check the live JSAC author information and the
target call for papers.

## When to trigger

- The author names JSAC for a communications/networking manuscript and wants to check
  fit against an active or upcoming special-issue call.
- A result must be re-framed to foreground its impact and timeliness for a particular
  call's frontier theme.
- The author is choosing between JSAC (call-driven, topical) and a broad-scope
  transaction (`ieee-transactions-on-communications` / `ieee-transactions-on-wireless-communications`).
- The author needs the call-matching logic and desk-reject heuristics specific to a
  special-issue venue.

## Scope & topic fit

- Next-generation wireless and cellular systems, integrated sensing and communication,
  non-terrestrial and massive-connectivity architectures — when matching a live call.
- Network architecture, protocols, virtualization, edge/cloud, and network management
  at the systems frontier.
- Security, privacy, and trust in communication systems and networks, including
  physical-layer and cross-layer security.
- Machine-learning-for-communications and communications-for-AI, where the advance is
  a communications-systems contribution, not generic ML.
- Optical, quantum, molecular, and emerging communication paradigms when aligned with
  a dedicated issue; route strictly by the call's stated scope and timeline.

## Method & evidence bar

- The contribution must be **high-impact and timely for the targeted call** — a frontier
  advance, not a routine increment; the call's aims-and-scope text is the rubric.
- Technical rigor still applies: analysis, simulation, and where appropriate testbed
  or prototype evidence, with correct, current baselines under realistic models.
- Claims of advancing the frontier must be substantiated against the most recent
  relevant work, including very recent preprints and standards activity where the
  topic is fast-moving.
- System-level and cross-layer evaluation is often expected; isolated PHY tweaks
  rarely match a systems-and-networks call.
- Reproducibility and clear assumptions matter as in any IEEE communications venue;
  impact claims must be evidence-backed, not aspirational.

## Structure & house style

- IEEE format; submissions go to a specific special issue (or, where offered, an
  ongoing series) — match the manuscript to the call and re-check current article
  types, limits, and deadlines on the live call page.
- The introduction must connect the work to the call's theme and articulate why it
  advances that frontier now.
- Figures and evaluation should be system-level and comparative; include architecture
  diagrams and end-to-end performance, not only link-level curves.
- Hard submission deadlines and guest-editor handling are typical for special issues;
  confirm the timeline before preparing the manuscript.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and
  `../../resources/official-source-map.md`; start from the IEEE Author Center anchors,
  then cite the current JSAC page and the specific call for papers you checked.
- Search the live site for "IEEE JSAC call for papers" and confirm the active issue,
  its scope, and its submission deadline.
- Re-check article types, length/overlength policy, the IEEE template, and any
  issue-specific requirements.
- Confirm reproducibility/simulation-code expectations and overlap/dual-submission
  policy with sibling journals.
- Re-check ORCID, competing-interests, funding, author-contribution, and AI-use
  disclosure requirements, and IEEE open-access options.
- If the live official instructions conflict with this skill, the official
  instructions win.

## Pre-submission self-check

- [ ] The manuscript matches a specific active call's theme, scope, and timeline.
- [ ] The contribution is framed as a high-impact, timely frontier advance, not a routine increment.
- [ ] Frontier claims are substantiated against the most recent relevant work, including recent preprints/standards.
- [ ] Evaluation is system-level/cross-layer where the call expects it, with matched, current baselines.
- [ ] The JSAC (call-driven) vs. broad-transaction choice is deliberate and justified.
- [ ] Article type, length, and the call's deadline are confirmed on the live page.

## Common desk-reject triggers

- Out-of-scope for every active call, or submitted after the issue deadline.
- Technically sound but routine/incremental work that does not advance the call's frontier.
- A narrow PHY-layer tweak submitted to a systems-and-networks call with no system-level contribution.
- Generic machine-learning applied to a communications dataset with no communications-systems advance.
- Impact claimed but not benchmarked against the latest relevant work in a fast-moving topic.

## Re-routing decision

- Broad-scope general communications result, no matching call → `ieee-transactions-on-communications`.
- Wireless-specific PHY/MAC, MIMO, channel work → `ieee-transactions-on-wireless-communications`.
- Fundamental-limit/capacity theorem → `ieee-transactions-on-information-theory`.
- Signal-processing method with analysis as the core → `ieee-transactions-on-signal-processing`.
- Broad tutorial/survey of a communications frontier → `proceedings-of-the-ieee`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] IEEE Journal on Selected Areas in Communications
[Active call] <matched special-issue theme, or "none — re-route">
[Topic tags] <2–3 closest communications/networking subtopics>
[Impact + timeliness] <why this advances the call's frontier now>
[Top risk] <the single most likely reason for rejection>
[Deadline check] <call submission window confirmed?>
[Official items to re-check] <call scope+deadline / article type / length / disclosures>
[Re-route suggestion] <if no call matches, a better-matched venue>
```
