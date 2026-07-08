---
name: icra-topic-selection
description: Use when deciding whether a robotics project belongs at ICRA, choosing between a direct ICRA submission and the RA-L journal route with conference presentation, or re-routing to IROS, RSS, CoRL, T-RO, HRI, or CASE based on contribution type, evidence shape, and the embodiment test.
---

# ICRA Topic Selection

Route a robotics project before any formatting work begins. ICRA — the IEEE
International Conference on Robotics and Automation, the flagship conference of the
IEEE Robotics and Automation Society (RAS) — is the broadest and largest robotics
deadline of the year, but "broad" does not mean "anything with a robot picture."
This skill runs two decisions in order: (1) is the contribution ICRA-shaped at all,
and (2) if yes, should it travel as a direct conference paper or as an RA-L journal
paper carrying a conference-presentation option.

## The embodiment test

Ask what breaks if the physical robot is deleted from the paper.

- If the answer is "nothing — the method is really about images, language, or generic
  optimization," ICRA reviewers will say so. Route to a vision, ML, or optimization
  venue and cite robotics as an application.
- If the answer is "the whole contribution — the method exists because of contact,
  dynamics, sensing noise, actuation limits, real-time constraints, or task resets,"
  the project is in ICRA territory.
- Middle cases (learning method evaluated only in simulation) can survive at ICRA,
  but the burden shifts to the experiments plan; see `icra-experiments` before
  committing.

## Fit by contribution type

| Contribution type | ICRA fit | Stronger alternative to weigh |
|---|---|---|
| New manipulation / locomotion / navigation algorithm with hardware trials | Core | RSS if the algorithmic idea is the star |
| Integrated robot system solving a hard task end to end | Core | IROS, field-robotics journals |
| Robot-learning method, sim-heavy, some real transfer | Good | CoRL if learning is the entire story |
| Control / estimation theory with robot validation | Good | T-RO or RA-L for longer proofs |
| Dataset or benchmark for robot tasks | Good | RA-L, IJRR for archival datasets |
| Human-robot interaction with a user study | Possible | HRI conference for study-centric work |
| Factory / logistics automation, scheduling | Possible | CASE, T-ASE |
| Perception with no downstream robot task | Weak | CVPR/ICCV, then a robotics follow-up |
| Pure RL / optimization theory, no embodiment | Weak | NeurIPS, ICML, L4DC |

## Direct ICRA vs RA-L with conference presentation

The RAS ecosystem offers two distinct roads to an ICRA podium, and choosing between
them is a real strategic decision, not a formality:

- **Direct ICRA submission.** One deadline per year (mid-September for a
  late-May/June conference), conference peer review, proceedings in IEEE Xplore,
  6 pages plus up to 2 pages of references at submission in the 2026 cycle.
- **RA-L (IEEE Robotics and Automation Letters).** Year-round submission, first
  decision targeted within about three months, revise-and-resubmit possible,
  6 pages including references with up to 2 extra pages at USD 175 each. Accepted
  RA-L papers can be transferred, within the posted window and within 270 days of
  acceptance, for presentation at an upcoming RAS conference such as ICRA — a journal
  publication plus the same stage.

Decide with these levers:

1. **Clock.** Missed September or the result matures in November? RA-L is the only
   road that still reaches the next ICRA stage.
2. **Revision tolerance.** RA-L allows a revision cycle; direct ICRA is
   accept-or-reject on one shot. Work with one fixable weakness favors RA-L.
3. **CV target.** Some fields and hiring committees weight the journal line (RA-L)
   differently from the conference line (ICRA proceedings). Check what the career
   context rewards; the presentation looks identical at the venue.
4. **Length.** Both cap near 6-8 pages, so length rarely decides; T-RO or IJRR is
   the route for genuinely long papers.
5. **Dual-submission trap.** The same manuscript must never sit in the ICRA
   conference pipeline and at RA-L simultaneously; that is a rejection offense in
   both systems.

## Quick routing script

```text
Q1 Embodiment: does deleting the robot delete the contribution?
   no  -> route to the parent field's venue; stop.
Q2 Maturity: results solid by early September?
   no  -> RA-L (rolling) or next IROS deadline (typically March).
Q3 One clean contribution statable in 6 pages?
   no  -> T-RO / IJRR long-form, or split the project.
Q4 Is the star the algorithmic idea (RSS), the learning method (CoRL),
   the user study (HRI), or the factory floor (CASE)?
   yes -> weigh that sibling before defaulting to ICRA.
Q5 Otherwise -> direct ICRA; record why in one sentence for the intro.
```

## Lighter tracks at the same conference

Not every result deserves — or needs — the full-paper gauntlet. The ICRA weeks
also host workshops with their own paper calls, late-breaking/abstract-style
contributions, competitions, and demo slots, each with separate winter/spring
deadlines and lighter (often non-archival) review. Correct uses:

- A promising-but-thin result: workshop now, full paper next September with the
  workshop feedback baked in.
- A dataset or tool needing community exposure before the archival paper.
- A negative or replication result that the main track rarely rewards but a
  topical workshop will discuss seriously.

Check archival status per call: some workshop papers preclude later "new"
submission of the same content, most do not — read the specific call's wording.

## Anti-patterns that waste a cycle

- Submitting a workshop-depth demo as a full paper: ICRA has late-breaking,
  poster, and workshop tracks better suited to preliminary results — check the
  current year's calls.
- Choosing ICRA purely for prestige when the reviewer pool for the subfield
  (e.g., soft robotics, surgical robotics) is deeper at a specialized venue.
- Planning "we will add real-robot results during rebuttal" — the classic ICRA
  pipeline has no author-response phase to add them in (see
  `icra-review-process`), so the evidence must be complete at submission.
- Ignoring that ICRA 2026 moved to double-anonymous review: a framing that leans
  on "our lab's famous platform" no longer helps and may leak identity.

## Output format

```text
[Embodiment test] pass / borderline / fail — <one line>
[Route] direct ICRA / RA-L + presentation option / sibling venue <name>
[Deadline reality] <next reachable deadline and date to verify>
[Contribution type] algorithm / system / learning / theory / dataset / HRI / automation
[Single biggest routing risk] <one line>
[Verify before commitment] current CFP at the ICRA year-site + RA-L information-for-authors page
```
