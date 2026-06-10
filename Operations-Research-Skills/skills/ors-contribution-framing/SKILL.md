---
name: ors-contribution-framing
description: Use when articulating the contribution of an Operations Research (OR) manuscript — especially the mandatory cover-letter contribution statement (since 1 June 2023, fewer than 500 words) and the discussion's significance claims. Frames why the work matters to OR; it does not position against specific prior papers (ors-literature-positioning) or run experiments (ors-data-analysis).
---

# Contribution Framing (ors-contribution-framing)

## When to trigger

- You must write the **mandatory contribution statement** for the cover letter.
- The introduction and discussion need to state significance to the OR community.
- A reviewer says "the contribution is incremental" or "significance to OR is unclear."

## The mandatory contribution statement (OR-specific)

Since **1 June 2023**, *Operations Research* requires the cover letter to include a
statement, in **fewer than 500 words**, articulating the manuscript's **novel,
innovative, and rigorous original contribution to operations research**. Treat this as
a first-class deliverable, not boilerplate. A strong statement:

- Names the **methodological contribution** in one or two sentences a non-specialist OR
  reader can grasp (new model class, first provable guarantee, tighter bound/rate,
  algorithm with better complexity, new analysis technique).
- Says **what was not possible before** and is now — the precise delta over prior art.
- Establishes **rigor**: which results are theorems/propositions and what they
  guarantee; that computation/simulation is reproducible.
- States **significance**: which OR problems, methods, or applications this changes.
- Stays under the **500-word** cap and avoids drowning in notation.

## Frame the three pillars: novel · innovative · rigorous

| Pillar | Make concrete |
|--------|---------------|
| Novel | The specific model/result/technique that did not exist before |
| Innovative | Why the approach is non-obvious; the idea that unlocks the result |
| Rigorous | The proved guarantees; tightness; reproducible computation |

## Carry significance into the paper

- **Equation-free introduction:** state the problem, the results, and their
  significance to the OR community *in words* — the introduction must contain **no
  equations or mathematical notation**. Draft these significance sentences here so the
  intro and the contribution statement are consistent.
- **Discussion:** spell out implications for OR theory and practice, the limits of the
  results (where assumptions bind), and concrete open problems the work opens.

## What OR area editors weigh in the contribution statement

The handling Area Editor reads the <500-word statement as a gate before assigning the
manuscript. They are scanning for the three pillars *and* for the decision payoff that
separates *Operations Research* from a pure-math venue. A practical weighting:

| Signal the AE looks for | Strong statement shows | Weak statement shows |
|--------------------------|------------------------|-----------------------|
| Methodological core | named new model/result/technique | "we study an important problem" |
| Provable delta | "first guarantee / tighter rate than X" | restated abstract |
| Computational credibility | corroborated by a benchmark study | theory-only, no validation plan |
| Decision relevance | which OR decision this changes | elegance with no managerial hook |
| Rigor signposting | which claims are theorems vs. heuristics | rate "shown" by numerical curves |

The INFORMS-flagship bar is **both**: theorem-grade rigor *and* a credible
computational or decision study. A statement that nails novelty but never connects the
structure to an operational decision draws the classic OR pushback below.

## Contribution pushback patterns and the fix

| Referee remark | The OR-specific repair |
|----------------|------------------------|
| "Model elegance without managerial/decision relevance" | add one sentence naming the decision the structure improves and the regime |
| "Contribution is incremental" | sharpen the delta to a quantified gain (tighter factor/rate, weaker assumption) |
| "Significance to OR unclear" | state which OR methods/applications change, not generic importance |
| "Theory not connected to the computational study" | promise (and later deliver) experiments that corroborate the proved bound |

## Worked statement skeleton (illustrative)

For a paper proving a threshold policy is optimal for a stochastic-scheduling model and
giving a 1.2-approximation heuristic with a computational study (numbers illustrative):

> *Novel:* first proof that a single-threshold policy is optimal under correlated job
> sizes. *Innovative:* a coupling argument that sidesteps the usual exchange-argument
> failure. *Rigorous:* Theorem 1 (optimality), Theorem 2 (1.2-factor for the heuristic),
> validated on 240 benchmark instances against a commercial solver. *Significance:*
> replaces a costly re-optimization with a closed-form rule for scheduling decisions.

Each clause maps to a pillar and ends on the **decision payoff** — the line that keeps
the statement out of "elegant but irrelevant" territory.

## Anti-patterns

- A contribution statement that just summarizes the paper instead of naming the delta.
- Listing "we study X" without "what is provably new."
- Overflowing the 500-word cap or filling it with equations.
- An introduction that leans on notation the equation-free rule forbids.
- Significance claims in the cover letter that the results do not support.

## Output format

```
【Contribution statement】<500 words; novel/innovative/rigorous covered? word count: ...
【Delta】what is provably new vs. prior art
【Equation-free intro lines】problem / results / significance (no notation)
【Discussion】implications + limits (where assumptions bind) + open problems
【Next step】ors-tables-figures or ors-writing-style
```
