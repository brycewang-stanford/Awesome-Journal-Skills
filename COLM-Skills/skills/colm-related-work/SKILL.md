---
name: colm-related-work
description: Use when positioning a COLM paper inside the fastest-moving literature in ML — triaging arXiv-heavy citations, handling concurrent work fairly, citing model and dataset artifacts correctly, distinguishing COLM's three-edition archive from adjacent venues' archives, and keeping self-citation double-blind safe.
---

# COLM Related Work

The LM literature moves faster than any archival process: the work you must position
against is substantially on arXiv, some of it appeared after your experiments
finished, and some "well-known results" are blog posts. A COLM related-work section
is therefore an exercise in *versioned honesty* — saying precisely what existed,
where, and when, without pretending the field is tidier than it is.

## Triage the literature into lanes

Cover each lane that touches your claim; reviewers at this venue are typically
active in two or three of them and will notice a missing lane immediately:

| Lane | What to position against | Typical miss |
|---|---|---|
| Method lineage | The 2-4 papers your technique descends from | Citing a survey instead of the source |
| Phenomenon reports | Prior observations of the effect you study, incl. analysis papers | Ignoring negative or contradictory reports |
| Evaluation infrastructure | The benchmarks/harnesses you use or compete with | Treating a benchmark as neutral ground rather than citable, criticizable work |
| Model artifacts | The model families your claims are scoped to | Citing a company blog when a technical report exists (or vice versa — cite what actually exists) |
| Adjacent-venue archive | Related results at ICLR/NeurIPS/ACL/EMNLP and in COLM 2024-2025 | Assuming COLM reviewers only read COLM |

Checking the COLM 2024 and 2025 accepted lists for near neighbors is cheap and
high-yield: citing the venue's own archive signals you know where you are
submitting, and the archive is only two editions deep (checked 2026-07-08).

## arXiv status honesty

State venue status accurately at citation time: published (venue, year), arXiv-only
(cite the arXiv ID; do not launder it into a "publication"), or since-published
(prefer the archival version, keep the arXiv date if chronology matters to your
priority story). For results that exist only as blog posts or model cards, cite them
as what they are, with access dates — at a venue that studies industry models, gray
literature is unavoidable; disguising it is the sin.

## Concurrent work: the protocol

With a March 31 deadline and a field publishing daily, concurrency is guaranteed.
The credible pattern:

1. Sweep arXiv for the last ~3 months against your core claims in the final week
   before submission (and again before the May rebuttal — reviewers will cite what
   appeared in April).
2. Give genuinely concurrent work its own labeled paragraph: state the overlap and
   the delta in one factual sentence each, without defensive framing.
3. Never bury a concurrent paper you know about. A reviewer who finds it first
   converts a neutral fact into a credibility wound.

```text
Concurrent-work paragraph skeleton:
  "Concurrent work [X, arXiv YYMM] also studies <shared object>.
   They <their finding, one clause>; we <orthogonal axis: different
   models / different measurement / different conclusion and why>.
   Results were developed independently."
```

## Positioning moves that work here

- **Against benchmark papers:** engage their validity arguments, not just their
  difficulty numbers — evaluation critique is a first-class COLM genre.
- **Against method papers:** identify the assumption or budget under which they
  win, and place your contribution on that axis rather than claiming dominance.
- **Against analysis papers:** state whether you *replicate, extend, or contradict*
  each prior observation, model-by-model where findings disagree — disagreement
  across model families is a finding, not an embarrassment.

## A positioning micro-example

The difference between listing and positioning, on one fictional paragraph:

- *Listing (weak):* "Prior work has studied contamination [1,2,3], benchmarks
  [4,5], and knowledge cutoffs [6]. We also study contamination."
- *Positioning (strong):* "[1] detects verbatim overlap via n-gram matching, which
  [2] shows misses paraphrase leakage; [6] estimates effective cutoffs from model
  behavior but cannot separate exposure from difficulty drift. Our dated-item
  design closes exactly that gap: exposure becomes an experimental variable rather
  than an inference."

Every cited paper in the strong version does work — it carries a specific
capability or limitation that motivates a design choice. A COLM reviewer reads
related work as the paper's *reasoning about its field*, not as a bibliography
compliance exercise; a paragraph where citations are interchangeable is a paragraph
that is not yet written.

## Double-blind self-citation

Cite your own prior work in the third person, exactly as you would a stranger's. The
LM-specific trap is artifact continuity: "we evaluate on the dataset of [7]" is
safe; "we extend our dataset [7]" is a leak; a Hugging Face link under your org
inside the related-work section is a hard violation of COLM's no-identifying-links
rule (`colm-submission`).

## Pre-submission citation audit

- Every lane in the table above covered or consciously excluded.
- Every citation's venue status accurate as of the submission date.
- Concurrent-work paragraph present if the sweep found anything; sweep re-run in
  deadline week.
- No first-person self-reference; no author-resolving artifact links.
- Bibliography sanity pass: LLM-assisted writing has made fabricated references a
  named disclosure category in COLM's 2026 policy — verify that every entry
  resolves to a real document. A hallucinated citation found in review reads as an
  integrity problem, not a typo.
- Citation pages are unlimited under the 2026 format — never cut references to save
  space; cut prose.

## Output format

```text
[Lane coverage] method ▢ phenomenon ▢ eval-infra ▢ artifacts ▢ adjacent-archive ▢
[COLM-archive neighbors] <papers from 2024/2025 accepted lists, or "none — checked">
[arXiv honesty] clean / laundered citations at: <items>
[Concurrent work] handled: <papers> / sweep stale — rerun
[Self-citation risk] none / leaks at: <locations>
[Reference integrity] all resolve / unverified: <count>
```
