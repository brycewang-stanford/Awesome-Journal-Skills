---
name: uist-writing-style
description: Use when drafting or revising a UIST paper — structuring the systems-paper arc (walkthrough before mechanism), writing an implementation section with real technical depth, pairing every capability claim with a figure or measurement, and fitting the argument inside the 10-page or 5-page two-column limit.
---

# UIST Writing Style

A UIST paper is a guided tour of a working thing. The reader should experience the
system before dissecting it, believe the engineering because it is specified, and
finish knowing exactly which piece they could reuse. This is a different rhetoric
from an empirical HCI paper (argument from study design) and from an ML paper
(argument from benchmark deltas). Format facts below are the 2026 cycle's
(two-column `acmart`, 10-page standard / 5-page short, references and appendices
excluded); verify against the current Author Guide.

## The UIST arc

| Section | Job | Failure smell |
|---|---|---|
| Abstract + teaser figure | Name the artifact, the enabling idea, one number | No artifact named; "we explore..." |
| Introduction | What becomes possible that wasn't; contribution list | Motivation essay with the system in ¶5 |
| Walkthrough / scenario | Reader operates the system vicariously, figure-driven | Mechanism dumped before experience |
| Design rationale | The 2-4 decisions that define the system, with rejected alternatives | A feature inventory |
| Implementation | Enough specificity to re-implement: architecture, algorithms, parts, timings | "Built in Unity" as the whole section |
| Evaluation | Evidence matched to claims (see `uist-experiments`) | A ritual usability study proving nothing claimed |
| Applications | Breadth: 3-5 demonstrations the technique enables | Repeats of the walkthrough |
| Limitations | Engineering honesty: where it breaks, at what scale | Generic "future work will explore" |

The teaser figure under the title is load-bearing at UIST: many reviewers form their
contribution hypothesis from it before reading a sentence. Design it to show the
interaction, not the hardware on a bench.

## Implementation prose that earns trust

Vague implementation writing is the most common style failure in UIST rejections.
Specificity is cheap and convincing:

```text
WEAK:  "The system tracks the user's hand and updates the display with low latency."
STRONG: "A wrist-mounted IMU streams at 200 Hz over BLE; orientation is fused with
        a complementary filter (α = 0.98) and mapped to cursor space in 1.8 ms
        median (95th percentile 3.1 ms) on the target tablet, measured over
        10,000 events with the harness in the supplement."
```

Rules of thumb:

- Every latency, accuracy, weight, or cost figure carries its measurement condition.
- Name the algorithm, then say what is non-obvious about applying it here — the
  novelty is usually in the adaptation, and reviewers who know the algorithm will
  check.
- Fabrication and hardware papers: include the parts, materials, and process details
  a motivated lab needs; put the full bill of materials in the appendix (see
  `uist-reproducibility`).

## Claim discipline

- Claim capabilities, not superlatives: "supports freehand annotation on curved
  surfaces up to 40 cm" survives review; "the first system to enable natural
  annotation" invites a counterexample hunt.
- Every "the system can X" needs a figure, measurement, or application section
  pointing at X. Reviewers at a demo-culture venue mentally run your video against
  your claims (see `uist-supplementary` for keeping the two synchronized).
- Write your own prior work in the third person with full citations — UIST's
  anonymization rule, and also a useful humility device.

## Fitting the page budget

The 10-page limit (5 for short papers) excludes references and appendices, so the
compression targets are figures and mechanism prose:

- Merge walkthrough and rationale figures: one annotated sequence beats three
  screenshots.
- Move parameter tables, extended benchmark grids, and study instruments to the
  appendix — but keep the body self-contained; the 2026 guide is explicit that the
  body must be readable without the appendix.
- Cut applications last: breadth of demonstration is UIST evidence, not decoration.
- Never buy space with `\vspace` or margin tricks; over-limit and modified templates
  are desk-reject territory (see `uist-submission`).

## Figures do half the arguing

UIST papers are read figure-first, and the figure budget deserves design effort
equal to the prose:

- **The teaser** (figure 1, under the title): the interaction at its most
  legible moment, ideally input and output in one frame, with a caption that
  states the capability rather than naming the parts.
- **Sequence figures** for the walkthrough: numbered frames with annotation
  arrows; readers should follow the interaction without the body text.
- **Mechanism diagrams** for the implementation: signal paths, layer stacks,
  state machines — one honest diagram replaces four paragraphs of prose and is
  what re-implementers screenshot.
- **Results figures** follow `uist-experiments` rules: distributions visible,
  conditions labeled, no truncated axes performing significance.
- Captions are self-contained at this venue: many reviewers' first pass is
  figures-plus-captions only. Every caption should survive being read alone.

## Language habits of accepted systems papers

- Present tense for the system ("the controller re-fits the model"), past tense
  for what you did ("we measured latency over 10,000 events").
- Active voice for design decisions — "we chose capacitive sensing because..." —
  since rationale is a claimed contribution, not a confession.
- Name the system early and use the name consistently; "our system/our approach"
  prose reads as unnamed and unfinished.
- Kill the throat-clearing openers ("In recent years...", "With the advent
  of..."); UIST introductions start inside the problem.
- Define each term of art once, then trust the reader — the audience builds
  interfaces for a living.

## Revision passes

1. **Artifact-first pass** — can a reader say what you built after page 1?
2. **Specificity pass** — highlight every number without a measurement condition.
3. **Claim-evidence pass** — table every "can/enables/supports" against its proof.
4. **Video-consistency pass** — nothing in the paper that the video contradicts.
5. **Cold read** — a labmate outside the project reads the walkthrough and narrates
   the system back; misnarrations mark the unclear paragraphs.

## Output format

```text
[Arc audit] weakest section of the eight + why
[Implementation depth] re-implementable / partially / opaque
[Unbacked claims] <list of capability claims lacking figure/measurement/app>
[Page budget] body pages vs limit, with the two cheapest cuts
[Rewrite order] <top three passes to run first>
```
