---
name: cvpr-writing-style
description: Use when writing or revising a CVPR paper's prose and figures, covering the 8-page budget where figures and tables count against the limit, the page-1 teaser figure convention, benchmark-table craft, claim calibration for a skeptical vision audience, and taking responsibility for tool-assisted text under CVPR's rules.
---

# CVPR Writing Style

CVPR is a visual venue with a brutal budget: eight pages **including figures and
tables** (references overflow free — verified 2026 rule). The papers that survive
triage by an overloaded reviewer pool are the ones a reader can evaluate in two passes:
a 90-second flip through figures and tables, then a real read. Write both passes on
purpose.

## The two-pass reader

**Pass one is visual.** Reviewers at a 16k-submission venue flip: Figure 1, the tables,
the qualitative grid, the ablation. If that flip communicates problem → idea → win, the
close read starts friendly. Concretely:

- **Figure 1 (the teaser)** sits on page 1 and must state the paper alone: task, what
  prior work gets wrong, what yours does instead — ideally on the same input. A teaser
  that needs the caption's third sentence has failed.
- **Every caption is self-contained**: dataset, metric, and the takeaway sentence. Flip
  readers never see body text.
- **The main table is typeset as an argument**: best numbers bold, second-best
  underlined, methods grouped by supervision/backbone class, your row where the eye
  lands last.

## Budgeting eight inclusive pages

| Section | Typical share | Compression lever |
|---|---|---|
| Title/abstract/teaser | ~1 page | Teaser earns its half page or shrinks |
| Intro | ~1 page | Contributions as 3 bullets, no history lesson |
| Related work | ~0.75 page | Position, don't survey (see `cvpr-related-work`) |
| Method + pipeline figure | ~2 pages | One figure replacing a page of prose |
| Experiments | ~2.5–3 pages | Grids to supplement; keep the decisive ablation |
| Limitations/conclusion | ~0.25–0.5 page | Honest and short |

Because figures count, figure design *is* text editing: a two-column pipeline figure
costing 0.6 page must delete at least 0.6 page of method prose, or it is negative
space. Cut from the flip-reader's perspective — never cut the ablation table to save a
paragraph of adjectives.

## Sentence-level norms of the genre

- Present tense, active voice, mechanism first: "We replace the cost volume with …"
  beats "In recent years, cost volumes have been widely used…".
- Name the delta in numbers early: "+2.1 AP on COCO with 40% fewer FLOPs" in the
  abstract, not "significant improvements".
- One notation table, introduced once; vision papers drown in re-defined symbols.
- Kill hype adjectives ("novel", "remarkable", "extensive") — at this venue they mark
  inexperience; the table is the adjective.

## Claim calibration

Vision reviewers are professionally allergic to overclaiming, because the field's
benchmark culture makes checking easy:

```text
Weak claim, strong paper:
  "Ours improves X on datasets A and B under protocol P with backbone Q."
Strong claim, dead paper:
  "Ours solves X"  /  "generalizes to real-world scenes"   (shown on 2 curated clips)
  "state-of-the-art"                      (on one dataset, vs. year-old baselines)
  "real-time"                             (no hardware named — CRF row contradicts you)
```

Every superlative must name its scope: dataset, protocol, compute class. If a
limitation is visible in your own qualitative grid, write it in the limitations
paragraph first — reviewers reward the paper that scoops its own weaknesses.

## Tool-assisted text is your text

The verified 2026 author-side rule: use whatever tools you like, but fabricated
citations and factual inaccuracies are rejection grounds — possibly without review —
and "an LLM did it" is explicitly no defense. Operational habit: any machine-drafted
paragraph gets a human pass for (a) citations that exist and say what's claimed,
(b) numbers matching your own tables, (c) generic filler that flip-readers instantly
recognize as padding.

## An abstract skeleton that fits the venue

Six sentences carry a CVPR abstract; more usually means the contribution is unclear:

1. **Task + failure**: the specific visual problem and where current methods break
   ("Trackers lose identity during occlusions longer than their temporal horizon").
2. **Cause**: the mechanism behind the failure, in one clause — this sentence is what
   separates insight papers from tweak papers.
3. **Method**: what you built, named, with its one central idea.
4. **Headline evidence**: the scoped number ("+2.1 AP on COCO, matched backbone").
5. **Breadth or cost**: second dataset, transfer result, or the efficiency figure.
6. **Availability**: what will be released (code/models/data — and remember datasets
   claimed as contributions carry a camera-ready release obligation).

Write the abstract twice: once before the experiments as a plan, once after as a
report; the diff between the two is your overclaiming audit.

## Revision protocol for a drafted paper

1. Print the figures and tables alone; run the 90-second flip test on a colleague
   outside the project.
2. Reconcile abstract numbers against tables (rebuttal-week embarrassment prevention).
3. Hunt "see supplement" pointers that hide decision-critical logic; pull those back.
4. Delete the roadmap paragraph ("Section 2 reviews…") — page-limited venues stopped
   reading them years ago.
5. Read the intro's last bullet against the conclusion: the promised contribution and
   the delivered one must be the same sentence.

## Reverify each cycle

- Page cap and the references-only overflow rule.
- Template/author-kit version (build from the current `cvpr-org/author-kit`).
- Any new writing-adjacent form fields (limitations sections, AI-use disclosures —
  none verified for 2026, 待核实 for later cycles).

## Output format

```text
[Flip test] passes / fails at: <figure or table>
[Budget] pages by section vs 8.0 incl. figures
[Claim audit] superlatives without scope: <list>
[Caption audit] non-self-contained: <figure numbers>
[Tool-text risk] unverified citations or numbers: <locations>
[Edit order] <highest-leverage cuts first>
```
