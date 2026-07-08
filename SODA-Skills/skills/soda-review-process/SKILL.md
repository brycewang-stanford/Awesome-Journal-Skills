---
name: soda-review-process
description: Use when reasoning about how a SODA (ACM-SIAM Symposium on Discrete Algorithms) submission is evaluated — the per-edition program committee under joint ACM-SIAM sponsorship, HotCRP triage of a record-size submission pool, lightweight double-blind refereeing of full versions, the September rebuttal, and October decisions.
---

# SODA Review Process

SODA is run jointly by the SIAM Activity Group on Discrete Mathematics and ACM
SIGACT, with a fresh program committee appointed for each edition — there is no
standing editorial board, and every policy below is re-decided annually. Anchor
facts for the 2027 cycle (checked 2026-07-08 via SIAM SODA27 pages read through
search renderings, plus organizer announcements): submission July 9, 2026 AoE on
HotCRP; reviews to authors by September 1; responses due September 4; decisions
and instructions in October 2026. The 2027 PC chairs were not yet indexed at check
time: 待核实. For scale context, SODA 2026's chair reported the largest submission
pool in SODA history, roughly a 25% jump year-over-year (reported via the PC
chair's public announcement; treat as reported, not official).

## Pipeline anatomy

| Phase (2027 anchors) | What happens | Author-side reality |
|---|---|---|
| July 9 | HotCRP closes | The record is frozen; nothing is added later |
| July | Bidding and assignment | Your title-page abstract and topic tags determine who reads you |
| July-August | Refereeing, often with external subreviewers | The full version is the reviewed object; depth checks are real |
| By September 1 | Initial reviews released | Read for factual errors first, opinions second |
| September 4 | Responses due | Three days; preparation happened in August (`soda-author-response`) |
| September-October | PC discussion and ranking | Reviews are debated; the response is evidence in that debate |
| October | Decisions + final instructions | Accept/reject; no shepherding tier by default (待核实 per cycle) |

## Who reads you: the subreviewer economy

A large-pool theory conference distributes much of its reading to external
subreviewers — domain experts recruited per paper by PC members. Consequences:

- Expect one deep technical review (the subreviewer who works in your niche) and
  broader reviews weighing significance. Write for both: airtight proofs *and* a
  first-ten-pages case for why the bound matters (`soda-writing-style`).
- Subreviewers check lineage. A comparison table that omits the actual
  state-of-the-art bound will be caught by the one person who proved it.
- Expertise variance is the norm, not a scandal. The rebuttal exists partly to
  arbitrate when the deep review and a skim review disagree.

## Lightweight double-blind, referee's view

Referees see no author names, but SODA's rules keep the literature intact:
authors post to arXiv freely and cite themselves in third person. In practice
many referees can guess authorship; the process is designed to remove the
*default* weight of names from triage, not to guarantee ignorance. Author-side
consequences: never rely on reputation carrying a thin section, and never burn
words hiding a self-citation the rules told you to keep visible.

## What moves a borderline paper

PC discussions compress each paper into a few sentences. The compressible
virtues:

- A **named open problem or barrier** the result resolves or bypasses — with the
  citation where it was posed.
- A **clean headline bound**: "first deterministic near-linear time" survives
  compression; "improves several parameters in some regimes" does not.
- A **transferable technique** a PC member can imagine using elsewhere.
- A **decisive rebuttal correction** of the most negative review's factual core.

And the compressible sins: a bound worse than known work (fatal), a proof the
deep review could not verify (near-fatal), scope mismatch better served by a
satellite or sibling venue (`soda-topic-selection`).

## Interpreting the calendar's silences

Author anxiety maps poorly onto PC reality; this table converts one to the
other for the 2027 anchors:

| What you observe | What it usually means | What it does not mean |
|---|---|---|
| No confirmation beyond HotCRP receipt in July | Normal; assignment is in progress | Nothing about your paper's fate |
| Reviews arrive well before September 1 | A punctual referee pool | Neither enthusiasm nor doom |
| One review far shorter than the others | A triage-level read alongside deep ones | Not automatically negative — check its F/L content |
| A referee question phrased as a request for computation | Your rebuttal's highest-value target | Not an acceptance signal |
| Silence from September 5 to October | Deliberation; scores are being argued | No news is literally no news |
| Decision earlier or later within October | PC logistics | Nothing paper-specific |

The single decision authors control in this period is rebuttal quality; the
single mistake available is contacting PC members outside HotCRP, which
converts a borderline paper into a conflict-of-interest incident.

## Reading a SODA review packet

```text
For each review, classify every substantive sentence:
  F  factual claim about your paper      -> verifiable; rebut if wrong
  L  literature claim (prior bound, who did what) -> check the citation yourself
  S  significance judgment               -> rebuttal leverage is low
  C  correctness doubt                   -> highest priority; answer with page numbers
Then decide: does the packet's most negative review rest on F/L errors
(rebuttable) or on S consensus (usually terminal for this cycle)?
```

## After the decision

- **Accept:** October instructions start the camera-ready track
  (`soda-camera-ready`).
- **Reject with correctness doubts:** repair the proof before any resubmission;
  theory reviewer pools overlap heavily across SODA, STOC, FOCS, ESA, and ICALP,
  and a resubmitted known bug follows the paper.
- **Reject on significance:** re-route rather than re-argue — ITCS for
  conceptual framing, ESA/ICALP for strong-but-specialized algorithmics, SOSA if
  the real contribution is a simplification (`soda-workflow` has the calendar).

## Output format

```text
[Process stage] <where the paper sits in the 2027 pipeline>
[Review triage] <F/L/S/C classification summary per review>
[Rebuttal leverage] <high/medium/low, with the deciding factor>
[Post-decision route] <camera-ready / repair / re-route target>
```
