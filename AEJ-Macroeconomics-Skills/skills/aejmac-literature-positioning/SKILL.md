---
name: aejmac-literature-positioning
description: Use when the contribution of an American Economic Journal: Macroeconomics (AEJ: Macro) manuscript relative to the macro frontier is fuzzy, contested, or undersold. Frames the marginal contribution against quantitative-theory and identified-empirical literatures; it does not fix the identification or the model itself.
---

# Literature Positioning (aejmac-literature-positioning)

## When to trigger

- The introduction cites many papers but never says what is *new*
- A referee could ask "how is this different from [the obvious prior paper]?" and you lack a one-line answer
- The paper sits between a theory literature and an empirical literature and the bridge is unclear
- The contribution is real but framed as incremental ("we extend X by adding Y")

## The AEJ: Macro positioning bar

AEJ: Macro is a **broad-interest** macro journal, so positioning must locate the paper for a *general* macro reader, not only for the three people working on the exact model or shock series. Two literatures usually bound a macro paper, and you must place the contribution against **both**:

- the **quantitative-theory** frontier (DSGE / HANK / heterogeneous-agent / structural) — what does your model deliver that the canonical model cannot?
- the **identified-empirical** frontier (SVAR / local projections / narrative / proxy-VAR / micro-data macro) — what does your evidence pin down that prior designs left open?

A hybrid paper (model matched to identified evidence) must say why the *combination* answers a question neither side resolved alone — this is often the strongest AEJ: Macro contribution.

## Positioning moves

### Move 1 — Name the closest 2–3 papers, then the wedge
Do not list 30 citations. Name the 2–3 papers a referee would call "basically the same," and state in one sentence what your paper does that each cannot. The wedge should be a **quantity, mechanism, or identification gain**, not "a different dataset."

### Move 2 — Place against both frontiers
- vs. theory frontier: "The canonical [RBC/NK/HANK] model predicts/assumes Z; we relax/measure Z and the macro implication changes by ___."
- vs. empirical frontier: "Prior [SVAR/LP] designs cannot separate channel A from channel B; our [narrative/high-frequency/sign-restriction] identification does."

### Move 3 — State the contribution as a sentence with a quantity
"We show that [mechanism] accounts for [X%] of [aggregate], overturning/refining the prior view that ___." A magnitude makes the contribution legible to a general reader and to the AEA process.

### Move 4 — Calibrate the claim
Say what the paper does **not** establish: the regime, sample, or country where the result holds, and what remains open. Over-claiming is the fastest path to a referee's "the contribution is oversold."

## Checklist

- [ ] The 2–3 nearest papers named, each with a one-line wedge
- [ ] Positioned against the quantitative-theory frontier (what the model adds)
- [ ] Positioned against the identified-empirical frontier (what the design pins down)
- [ ] Hybrid papers: why model + evidence beats either alone
- [ ] Contribution stated as one sentence with a quantity/mechanism
- [ ] Scope limits stated; no over-claiming beyond regime/sample
- [ ] Broad-interest framing: a general macroeconomist sees why it matters

## Anti-patterns

- A "literature wall" — long paragraphs of citations with no stated wedge
- Positioning only against the subfield, invisible to general macro readers (reads as a field paper, wrong for AEJ: Macro)
- "We are the first to…" claims that a single prior paper falsifies
- Framing the contribution as a method tweak rather than a macro answer
- Burying the contribution sentence on page 4 instead of paragraph 1–2 of the intro

## Output format

```
【Nearest papers + wedge】1) ... 2) ... 3) ...
【Vs. theory frontier】what the model/structure adds
【Vs. empirical frontier】what the identification pins down
【Contribution sentence (with quantity)】...
【Scope / what it does NOT claim】...
【Next step】aejmac-identification (empirical) and/or aejmac-theory-model (quantitative)
```
