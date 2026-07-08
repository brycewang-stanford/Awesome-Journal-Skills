---
name: asplos-writing-style
description: Use when drafting or revising ASPLOS prose — engineering the first two pages that rapid review actually reads, stating the cross-layer insight as one quotable sentence, structuring per-layer mechanism sections, writing bounded claims, and fitting everything into 11 self-contained pages that include figures and footnotes.
---

# ASPLOS Writing Style

Two 2027 mechanics dictate ASPLOS prose (CFP, checked 2026-07-08): the rapid review
reads **only the first two pages**, and the 11-page limit counts **all text,
figures, tables, and footnotes** — references excluded. The first makes pages 1-2 a
survival organ; the second makes every figure a budget decision. Style here is
mostly resource allocation.

## Engineering pages 1-2 as a standalone document

By the bottom of page 2, a screener must hold four things. Audit for them
mechanically, in order:

| Element | Test | Common failure |
|---|---|---|
| Cross-layer problem | Can a reader from any of the three communities restate it? | A single-community problem with "co-design" sprinkled on |
| One-sentence insight | Is there a sentence a screener could quote in their note? | Insight diffused across three paragraphs, or a category ("we co-design X and Y") instead of an idea |
| Mechanism sketch | Does the reader know what each layer *does*? | Architecture described, software hand-waved (or vice versa) |
| Headline evidence | Result + platform class (silicon/FPGA/simulator) + baseline named? | "Significant improvements on a variety of workloads" |

Corollary: background sections, notation, and roadmaps do not belong on pages 1-2.
The worked example (`../../resources/worked-examples/01-introduction.md`) shows a
full before → after against exactly this table.

## The insight sentence

The load-bearing sentence in an ASPLOS paper names **information or capability that
crosses a layer boundary**: what the hardware knows that the OS needs, what the
compiler can prove that the microarchitecture can exploit. Drafting discipline:

```text
Weak:   "We propose a hardware/software co-designed approach to memory tiering."
        (names a category and a topic; contains no idea)
Strong: "The contention data the OS needs already passes through the memory
        controller on every access; the fix is a narrow architectural channel,
        not a smarter kernel heuristic."
        (names the information, its current location, and the boundary moved)
```

If this sentence cannot be written, the problem is usually fit, not prose — return
to `asplos-topic-selection`.

## Structuring the mechanism across layers

Give each layer its own subsection with its own contribution statement, then a
section for the **interface** between them — the interface is the paper's actual
thesis and deserves first-class treatment (encoding, semantics, virtualization
behavior, failure modes). Reviewers from different communities will each read "their"
subsection closely; the interface section is where they meet.

## Claim calibration, systems dialect

- Bound claims by construction: "never regresses more than 2% on our non-tiered
  suite" is a stronger sentence than "negligible overhead."
- Attach the instrument to the number in the same sentence: "1.18× gmean on real
  hardware (14 workloads)" vs "up to 3.4× in simulation" are different epistemic
  objects and must not blend.
- Write the losing case in the same register as the winning ones. One honestly
  analyzed regression buys more reviewer trust than a page of wins.

## The 11-page budget with figures inside it

Because figures count against the limit, they compete with prose on equal terms:

- Every figure must either carry a claim or explain the mechanism; delete gallery
  plots and merge panels that make one point.
- Prefer one annotated diagram of the boundary/interface over three block diagrams
  of components — reviewers cite the diagram that explains the *idea*.
- Compression order when over budget: cut duplicate-message plots → collapse
  per-workload bars into summary + appendix grid → tighten mechanism prose → never
  touch template geometry (mandatory template; violations risk rejection unread).

## House-rule details that mark a native submission

- References carry every author's full first and last name — no "et al." — with
  hyperlinked in-text numbers and DOIs per entry; a hygiene-signaling detail
  reviewers notice early.
- Third-person self-citation throughout; no "removed for blind review" text.
- GenAI assistance, if any, disclosed per ACM policy (Acknowledgments, immediately
  before References).

## A load-order for the abstract

Six sentences, in this order, cover what both the rapid screener and the
eventual citer need: (1) the friction two layers create today; (2) the insight
sentence; (3) the mechanism, one clause per layer; (4) the headline number with
instrument and baseline; (5) the bound on the downside; (6) what the interface
enables beyond this paper. Most first drafts invert 1 and a background sentence
— delete the background sentence; ASPLOS readers do not need to be told memory
matters.

## Section skeleton that serves three readerships

A cross-layer paper defaults well to: motivation-with-evidence (measured, not
asserted — a characterization figure beats three citations); design overview
around one boundary diagram; per-layer mechanism sections; the interface
section; evaluation ordered by the claim matrix; related work by lanes
(`asplos-related-work`); then discussion of what the boundary change costs.
Each community's reviewer should be able to find "their" section from the table
of contents alone — a paper organized by implementation chronology instead
forces reviewers to reconstruct the design, and annoyed reconstruction reads as
"unclear writing" in reviews.

## Revision-aware prose

Because Major Revision is a standing outcome, write sentences that can absorb
revision without rewiring: quantitative claims phrased with their scope ("across
the 14-workload suite") extend gracefully when workloads are added; hard-coded
superlatives ("the first", "the fastest") require re-litigation at every
resubmission and are the first phrases a shepherd strikes.

## Output format

```text
[Two-page audit] problem / insight-sentence / mechanism / evidence — each Y/N + fix
[Insight sentence] <quoted verbatim>
[Layer structure] per-layer subsections + interface section present: Y/N
[Claim calibration] unbounded adjectives found: N · instrument attached per number: Y/N
[Figure budget] figures: N · pages consumed: N · deletions/merges proposed
[House rules] citations format / self-cite person / GenAI disclosure — pass/fail
```
