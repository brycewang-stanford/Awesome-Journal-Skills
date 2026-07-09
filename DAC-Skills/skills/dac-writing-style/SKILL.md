---
name: dac-writing-style
description: Use when drafting or tightening the prose of an ACM/IEEE Design Automation Conference (DAC) Research Manuscript, covering the QoR-forward first-page arc, stating the design-automation contribution as a measured delta, fitting a complete argument into six double-column pages plus a references-only page, building column-width EDA figures, and third-person self-citation for double-blind review.
---

# DAC Writing Style

Use this while writing the body. DAC Research Manuscripts live inside a **6-page double-column
budget** (plus a references-only page), so the writing discipline is not "explain everything" but
"prove one design-automation contribution, in the field's own QoR currency, in six dense pages."
DAC reviewers are EDA experts under time pressure; they decide fast whether the paper has a real,
measured advance.

## The DAC first-page arc

Front-load the contribution. By the end of the first column-and-a-half a reviewer should know:

1. **The design problem** — a concrete EDA/chip-design task (placement, timing closure, functional
   verification, IR-drop prediction, IP protection) that the community recognizes.
2. **Why the current state is inadequate** — the specific limitation of the best existing tool or
   technique, ideally with a number (it does not scale past N cells, it leaves X% negative slack).
3. **The contribution as a measured delta** — the new mechanism *and* the headline QoR result:
   "we reduce total negative slack by X% at equal area with Y× lower runtime versus [state of the
   art] on [standard benchmark]."
4. **Why it generalizes** — that the mechanism is not a one-benchmark trick.

Do not open with "AI has transformed chip design." Open with the design problem and the number.

## State the contribution as a QoR claim

The EDA community speaks in **PPA (power, performance, area)**, plus wirelength, timing slack
(WNS/TNS), routability/DRC, coverage, and **runtime**. A DAC contribution is strongest when phrased
as a delta in those units against a named baseline:

- Weak: "Our method improves quality and is efficient."
- Strong: "On the ISPD placement benchmarks our router reduces total wirelength by X% and DRC
  violations by Y% while completing in Z× less runtime than [baseline]."

Every headline claim in the abstract and introduction should reappear as a per-benchmark row in a
results table, not just an average.

## Living in six double-column pages

The budget is the constraint that shapes the paper:

- **One contribution, deep.** Six pages cannot carry three loosely related ideas; pick the strongest
  and develop it fully. A sprawling paper reads as thin at DAC.
- **Method before menagerie.** Spend pages on the mechanism and the evaluation, not on a long
  taxonomy or a tutorial of standard EDA background the reviewers already know.
- **Tables over prose for results.** A compact per-benchmark table communicates more per square inch
  than paragraphs; DAC reviewers read tables first.
- **Cut the roadmap.** "Section 2 covers... Section 3 covers..." is dead weight at six pages; let
  section headings do that work.
- **References go on the seventh page only.** Body content there is a desk-reject; plan the argument
  to end at page six.

## EDA figures that survive double-column at 9-10 pt

- Design figures (floorplans, layouts, congestion/heatmaps, netlist graphs) must be **legible at
  column width** — roughly half of a US-letter page wide. Test every figure at final size.
- Label axes with the real QoR units; a curve with no units persuades no one.
- Prefer a clear **flow diagram** of the technique over a dense algorithm listing when space is
  scarce; move full pseudocode to the body only if it earns its space.
- Color heatmaps must still read in grayscale and for color-blind reviewers.

## Third-person self-citation (double-blind)

Because review is double-blind, refer to your own prior work in the **third person**: not "in our
earlier tool [7]" but "the prior technique [7]." Keep acknowledgements, funding, and grant numbers
out of the review version entirely; they return in the camera-ready.

## Common DAC prose failures

| Failure | Why it costs you | Fix |
|---|---|---|
| QoR claim only as an average | Reviewers suspect a few benchmarks carry it | Per-benchmark table; report all circuits |
| Baseline unnamed or "a standard method" | Reads as evasive about the real state of the art | Name the strongest prior tool and its tuning |
| Background eats two pages | Leaves no room for the contribution | Assume EDA literacy; cut to the delta |
| Figures illegible at column width | Reviewer cannot verify the claim | Rebuild at final size, real units |
| First-person self-citation | De-anonymizes under double-blind | Third-person throughout |

## Output format

```text
[First-page arc]  design problem -> inadequacy (with a number) -> QoR delta -> generality? present?
[QoR framing]     headline claim stated in PPA/wirelength/slack/runtime vs a named baseline? yes/no
[Budget]          body within 6 double-column pages? references-only 7th page clean?
[Figures]         legible at column width, real units, grayscale-safe? yes/no
[Anonymity]       self-citations third-person; acks/funding removed? yes/no
[Cut list]        <lowest-value paragraphs/figures to reclaim space>
```
