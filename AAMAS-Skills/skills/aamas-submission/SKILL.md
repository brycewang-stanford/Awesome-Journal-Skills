---
name: aamas-submission
description: Use when auditing an AAMAS main-track submission for OpenReview readiness, the 8-page-plus-references limit, the full-paper versus 2-page extended-abstract choice, double-blind anonymity, the supplementary zip cap, track fit across the AAAI/JAAMAS/Blue Sky tracks, dual-submission rules, and desk-reject triggers before upload.
---

# AAMAS Submission

Use this for an AAMAS submission audit. Reopen the current-edition Call for Papers, submission
instructions, important-dates page, and OpenReview group before giving deadline-ready advice;
AAMAS rotates hosts yearly and the host page may block automated fetches.

## Pick the track first

AAMAS is a multi-track conference, and choosing the wrong one is a silent rejection.

- Main Technical Track: original agents/multiagent research, submitted as a full paper or a
  2-page extended abstract.
- AAAI Track: a strong AAAI submission redirected to AAMAS, in main-track format plus a short
  response to the AAAI reviews with changes highlighted; the extended-abstract option does not
  apply.
- JAAMAS Track: a 2-page extended abstract of a JAAMAS journal article accepted or published in
  the window before the notification date.
- Blue Sky Ideas, Demo, Competitions: visionary positions, live systems, and contests, each
  with its own page rule and deadline.

## Submission audit

- Confirm the target is the intended AAMAS track, not a workshop, tutorial, or a neighbor
  conference sharing the deadline season.
- Verify OpenReview profiles, coauthor list, conflicts, subject-area keywords, title, and the
  short plain-text abstract that is due before the paper deadline.
- Apply the current style file with no margin, spacing, or font hacks. AAMAS 2026 main-track
  papers were at most 8 pages **plus any number of reference pages**, and typesetting tricks to
  cram content into 8 pages were disallowed.
- Decide full paper versus extended abstract deliberately: an extended abstract is archival
  presence, not a compressed full paper, and cannot carry a full evaluation.
- Package supplementary material as one zip within the current cap (25 MB in 2026).
- Enforce double-blind anonymity: replace author names and affiliations on page one with the
  paper tracking number, remove acknowledgements, and strip identifying metadata, paths, and
  repository owners from the PDF, code, and supplement.
- Check the dual-submission and prior-publication rules for the chosen track before upload.

## Blocking risks

- Late abstract or paper upload against an AoE deadline.
- Overlength main text, or an extended abstract mistaken for a full-paper slot.
- Identity leak in the PDF, supplement, code paths, or metadata.
- Supplement zip over the size cap or in a rejected format.
- Wrong track, or a concurrent archival submission the track forbids.
- An interaction claim with no multiagent evidence, or weak opponent/baseline coverage.

## Desk-reject and triage table

| Trigger | Severity at AAMAS | Repair window |
|---|---|---|
| Overlength 8-page body | Desk reject | None after the deadline |
| Style-file tampering | Desk reject or chair flag | None |
| Author identity leak in PDF or code | Desk reject | None |
| Wrong track (e.g. AAAI-Track rules unmet) | Return without review | Only before that track's deadline |
| Interaction claim without multiagent experiment | Review-stage damage | Fixable only before the deadline |

## Final-week sequence for a MARL-plus-theory paper

1. Freeze the game definition, agent objectives, and any equilibrium claims; reviewers
   cross-reference them.
2. Regenerate every learning curve and payoff table from seeded scripts so PDF and supplement
   cannot diverge.
3. Confirm the opponent/population set and evaluation protocol are stated in the body, not
   buried in the appendix.
4. Strip PDF metadata, notebook authorship, and repository owner strings from the supplement.
5. Confirm the OpenReview abstract matches the PDF abstract exactly, and the track is correct.

## Format anchors

- AAMAS uses a two-column proceedings layout; wide algorithm blocks, extensive-form game
  figures, and multi-panel learning curves that fit a one-column draft routinely overflow, so
  compress early rather than on deadline night.
- The page and supplement numbers above describe the 2026 cycle; treat every value as
  provisional and recheck the current CFP before relying on it.

## Output format

```text
[AAMAS readiness] Ready / Needs fixes / Not ready
[Track] main-full / main-extended-abstract / AAAI / JAAMAS / Blue Sky / Demo / Competitions
[Blocking checks] <OpenReview/page/anonymity/supplement/track/dual-submission>
[Interaction-evidence risk] <one issue about the multiagent claim>
[Desk-reject risk] <one issue>
[Fix order] <ordered fixes before submission>
```
