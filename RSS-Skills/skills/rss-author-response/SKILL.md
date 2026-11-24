---
name: rss-author-response
description: Use when drafting the RSS (Robotics: Science and Systems) invited rebuttal — in RSS 2027 the response to the Stage 1 Metareview that the Area Chair turns into the Extension Charter — including triage, length budgeting, anonymity, and what to do when no rebuttal invitation arrives.
---

# RSS Author Response

Draft the rebuttal RSS grants to papers invited past Stage 1. In RSS 2027 invited
papers receive a Metareview on February 5, 2027 listing required clarifications,
evaluations and methodological extensions; the rebuttal is due **February 12, 2027**
(AoE), and the AC revises the Metareview into the **Extension Charter** sent on
February 26 (verified 2026-11-24). RSS 2026 used a one-page rebuttal (April 3, 2026)
for papers above a first-round threshold. Either way this is a memo to the Area Chair,
not a reply thread — and in 2027 it negotiates the work you will be held to.

## First, establish which situation you are in

| Situation | Meaning | Move |
|---|---|---|
| Rebuttal invited (Stage 1 passed) | Metareview proposes Charter items | Full drafting protocol below |
| Stage 1 reject | Decided without author input | Skip to resubmission triage (bottom) |
| Reviews arrived, rules unclear | Cycle may have changed the design | Reread roboticsconference.org/information/cfp/ before writing a word |

## Drafting protocol

The 2027 rebuttal template had not been published on 2026-11-24 ("will be made
available in due course" — 待核实); obey its length rule when it appears. The 2026
format was one page.

### Negotiating the Extension Charter

Each Metareview item will become an obligation. For each one: accept it, propose a
feasible scoped variant (with the reason the variant still tests the hypothesis), or
argue it is out of scope. A Charter you cannot execute by April 16 is a rejection
deferred.

**Budget the page like the scarce resource it is.** A workable split: 60% on the one
or two objections that could flip the meeting, 25% on factual corrections, 15% on a
scope concession that shows calibration. Zero on thanking reviewers at length.

1. **Open with the verdict-relevant sentence.** State, in one line, why the central
   objection does not undermine the claim — then support it. ACs skim top-down under
   meeting time pressure.
2. **Cite the submission by coordinates.** "Table 3, row 4 reports exactly this
   ablation" beats paragraphs of re-explanation, and signals the evidence existed at
   review time.
3. **Concede cleanly where the reviewer is right.** A scoped concession ("the claim
   holds for quasi-static tasks; we will retitle Section 5 accordingly") converts an
   objection into a camera-ready edit.
4. **No new experiments as load-bearing evidence.** You may clarify protocol or cite
   numbers already in the supplement; a fresh results table invites the fair reply
   that it was never reviewed.
5. **Stay anonymous.** Double-blind still applies — no links, no lab tells, no
   "as our prior work" constructions.

## Writing for the AC, not the reviewers

The AC revises the Metareview into the Charter based on your response, so the
realistic reader model is one busy expert deciding what your final paper must contain:

- Give the AC quotable material: short, declarative, coordinate-anchored sentences.
- Resolve reviewer disagreements explicitly ("R2 and R3 read the trial protocol
  differently; the protocol in §4.2 matches R3's reading") — arbitration help is
  what an AC most lacks.
- Do not relitigate significance at length; one sentence connecting the claim to the
  broader program is the ceiling of what a rebuttal can move.

## Skeleton of a page that works

A compressed example shape (fictional content, real structure):

```text
R1's central concern — that the gain could come from the retuned controller
rather than the schedule — is tested directly: Table 3 row 4 holds the
controller fixed and varies only the schedule (41% -> 78%).

Corrections. R2: trials per condition are 100, not 25 (§4.2 line 3 states
the protocol; 25 is the object count). R3: the baseline uses the authors'
released configuration, not a reimplementation (§4.1).

Scope. R1 is right that the claim as titled overreaches quasi-static tasks;
we will scope the title and §5 header accordingly.

Reviewer disagreement. R2 and R3 read the reset protocol differently; §4.2
matches R3's reading, and the supplement ledger logs every reset.
```

Note what is absent: gratitude paragraphs, new results, promises of future
work, and any sentence the AC could not lift directly into the meeting.

## Failure patterns that waste the page

| Pattern | Why it fails |
|---|---|
| Point-by-point replies to every comment | Dilutes the one meeting-flippable argument |
| "We have now run additional experiments..." | Unreviewed evidence; invites procedural dismissal |
| Tone-matching an irritated review | ACs read composure as confidence in the evidence |
| Restating the paper's contribution | The AC has the paper; they need the *resolution* |
| Deferring everything to "the final version" | Signals the objection is real and unanswered |

## If no rebuttal came

The decision is effectively made; spend the energy forward. Map each objection to the
next calendar slot: protocol gaps → fix before IROS (~March deadline has passed;
next: CoRL ~June or ICRA ~September patterns, verify live); framing objections →
rerun `rss-topic-selection` honestly before re-targeting RSS 2028.

## Window logistics

- The 2027 window is one week (February 5 → 12); pre-draft answers to the three most
  likely objections and a feasibility estimate for plausible extra experiments during
  the December-January silence, so the invitation triggers assembly, not composition.
- One author owns the page; committee-written rebuttals converge to mush. Others
  supply evidence coordinates and red-team the draft.
- Verify the submission channel and length rule on the form or template itself when
  the invitation arrives.
- Freeze the text several hours before the AoE cutoff; a rebuttal that arrives late
  is a rebuttal that does not exist, and there is no grace channel.
- Archive what you sent; the final paper must deliver every Charter item, and the
  camera-ready every edit the rebuttal promised (`rss-camera-ready`).

## Output format

```text
[Invitation status] invited / stage 1 reject / unclear (reread the CFP)
[Charter stance] <per Metareview item: accept / scoped variant / out of scope>
[Meeting-flippable objections] <1-2, each with evidence coordinates>
[Corrections] <error -> paper location>
[Concession] <scoped sentence + camera-ready edit>
[Page budget check] flip 60 / correct 25 / concede 15
[Anonymity check] pass / issues
```
