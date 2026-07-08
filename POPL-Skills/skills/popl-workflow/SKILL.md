---
name: popl-workflow
description: Use when planning a POPL campaign calendar — backward-scheduling theory and mechanization from the July deadline, riding the October notification into the conditional-acceptance revision and artifact evaluation, landing the January conference, and retargeting across the SIGPLAN/PACMPL deadline wheel if July slips.
---

# POPL Workflow

POPL's seat in the SIGPLAN year is fixed and unforgiving: **submit in July, hear in
early October, revise and package artifacts in the fall, present in January**. For
POPL 2027 (verified 2026-07-08): deadline July 9, 2026 AoE; notification October 5,
2026; symposium January 10-16, 2027, Mexico City. There is no abstract deadline and
no second call. POPL is a conference — no editor-in-chief, no submission fee; the
chairs rotate per edition (2027 names 待核实) and publication costs run through
PACMPL's open-access model, not author-facing page charges in the normal case.

## Backward plan from a July deadline

| Weeks before deadline | Theory-paper milestone |
|---|---|
| 16+ | Core calculus stable; main theorem conjectured precisely |
| 12 | Hard lemmas proved on paper; mechanization of the kernel started |
| 8 | Main theorem proved; decide mechanize-vs-hand-prove split per theorem |
| 6 | Case studies or prototype evidence frozen (`popl-experiments`) |
| 4 | Full draft in acmsmall; informal-to-formal ramp reviewed by an outsider |
| 2 | Mock review by someone who tries to break the theorem, not the prose |
| 1 | Anonymity sweep of paper + proof archive; correspondence table regenerated |
| 0 | HotCRP upload with hours of AoE margin, not minutes |

The distinctive scheduling truth: **theorems do not compress**. An experiment can be
rerun overnight; a broken lemma two weeks out cannot be fixed by working weekends.
Freeze the formal core earlier than feels necessary.

## The fall gauntlet (acceptance path)

October notification opens three parallel tracks that all land before January:

1. **Committee revision** — mandatory, deadline set at notification
   (`popl-camera-ready`).
2. **Artifact evaluation** — by invitation for conditionally accepted papers; the
   no-admit/no-sorry pass and Zenodo archiving take real days
   (`popl-artifact-evaluation`).
3. **January logistics** — visa appointment, registration, talk. Mexico City in
   January is an international trip for most authors; start visas the week the
   decision lands.

## If July slips: the PACMPL deadline wheel

All four SIGPLAN flagships publish in the same journal, so retargeting costs
reviewer culture, not archival quality. From POPL's July seat, the recent pattern
(verify each venue's current call — dates rotate):

```text
POPL (July deadline, January conference)   <- you are here
  -> OOPSLA: next PACMPL deadline after July in recent cycles
  -> PLDI: November-ish deadline, June conference
  -> ICFP: late-winter/spring deadline, fall conference
Retarget rule: move to the venue whose reviewers match your EVIDENCE,
not the nearest date — see popl-topic-selection.
```

Never park the same paper at two of them at once; dual submission burns the pair.

## Output format

```text
[Current stage] framing / proving / mechanizing / drafting / submitted / response / revision / production
[Next hard date] <event + date + source URL, or 待核实>
[Critical path] <the three tasks that gate the next date>
[Frozen vs fluid] <what may still change without cascading into proofs>
[Fallback] <retarget venue + its verified deadline, if July is unrealistic>
```
