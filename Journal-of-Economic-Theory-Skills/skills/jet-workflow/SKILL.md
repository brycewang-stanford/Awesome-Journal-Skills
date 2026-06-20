---
name: jet-workflow
description: Use when routing a Journal of Economic Theory (JET) manuscript — decides which jet- sub-skill to invoke next across the theorem-proof lifecycle, from theory-first scope check through Editorial Manager submission and single-anonymized R&R. Use first when unsure where to start.
---

# JET Workflow Router (jet-workflow)

## When to trigger

- "I want to send a theory paper to JET — where do I start?"
- You have a result but are unsure whether it clears JET's theory-first scope gate
- You need the next step after identification of assumptions, drafting, or a referee report

## What JET is (so the router routes correctly)

The *Journal of Economic Theory* is Elsevier's flagship general economic-theory venue (ISSN
0022-0531). The deciding criterion is a **rigorous, original theoretical contribution** —
mechanism design, information economics, decision theory, game theory, matching, market design,
political economy, finance and macro/monetary theory. Empirical, experimental, quantitative, or
computational work is welcome **only when firmly grounded in theory**. House style is
theorem-proof, typeset in LaTeX (Elsevier `elsarticle`). Review is **single anonymized
(single-blind)** with a floor of **at least two referees** after an editor desk screen.

## Default order

```text
jet-topic-selection          (is this a JET-scope theoretical contribution?)
        ▼
jet-literature-positioning   (stake the result against the theory frontier)
        ▼
jet-identification-strategy  (assumptions, results, proof architecture, generality)
        ▼
jet-contribution-framing     (state the theorem and why it matters)
        ▼
jet-data-analysis            (numerical examples / computation — only if any)
        ▼
jet-tables-figures           (schematic exhibits, notation discipline)
        ▼
jet-writing-style            (elsarticle theorem-proof prose; polish)
        ▼
jet-replication-and-data-policy (Option C data statement; reproducible computation)
        ▼
jet-review-process           (what single-anonymized refereeing expects)
        ▼
jet-submission               (Editorial Manager preflight, .tex source, AI disclosure)
        ▼
jet-rebuttal                 (response letter on an R&R)
```

## Router diagnostics

- No theorem sentence yet -> `jet-topic-selection`.
- Closest theorem unclear -> `jet-literature-positioning`.
- Assumptions or proof dependencies unclear -> `jet-identification-strategy`.
- Theorem is right but buried -> `jet-contribution-framing`.
- Computation is doing too much work -> `jet-data-analysis`.
- Figures introduce notation drift -> `jet-tables-figures`.
- Source/package facts are volatile -> `jet-submission` and `resources/official-source-map.md`.

The next skill should always reduce one JET desk/referee risk: off-scope empirics, overclaimed theorem,
hidden assumption, unreadable proof, notation drift, or unsupported submission fact.

## Manuscript-state routing table

| Manuscript state | Dominant JET risk | Route |
|---|---|---|
| Idea + model, no theorem sentence yet | off-scope at the desk | jet-topic-selection |
| Theorem proved, novelty delta fuzzy | a "follows from known results" report | jet-literature-positioning |
| Theorem + proof drafted, assumptions scattered through proofs | hidden-assumption catch by a referee | jet-identification-strategy |
| Full draft, introduction shaped like a data story | theorem buried at the desk screen | jet-contribution-framing, then jet-writing-style |
| A numerical section dominating the paper | computation overshadowing the theory | jet-data-analysis |
| Exhibits renaming model objects | notation drift across figure and proof | jet-tables-figures |
| Camera-ready PDF, source files not checked | format bounce (PDF-as-source) | jet-submission |
| R&R letter alleging a proof gap | broken-lemma risk | jet-rebuttal plus jet-identification-strategy |

## Routing vignette: a dynamic-contracts paper

The paper proves a recursive characterization of optimal long-term contracts under two-sided
limited commitment, plus one computed example. The pass order actually used:

1. Topic gate — the characterization theorem is the deliverable: pass.
2. Positioning — closest recursive-contract theorem named; delta = commitment limited on **both**
   sides.
3. Identification — Assumption 2's role in the contraction-mapping step made explicit; a tightness
   Example added for one-sided commitment.
4. Framing — the abstract now carries the characterization sentence, not the application.
5. Data-analysis — the computed contract path demoted to Example 2 with a pinned script.
6. Tables-figures → writing-style → submission, in order.

One skill was consciously skipped until submission: no external research data existed, but the computed
example script was still made reproducible and the eventual Option C statement said so plainly. Record
deliberate skips so a later pass does not mistake them for gaps.

## Loops, not a one-way pipe

- A rebuttal that **narrows a claim** re-opens framing and positioning — the abstract and the
  delta sentence must shrink with the theorem.
- A new counterexample found late re-enters at identification, then propagates forward through
  framing, exhibits, and prose.
- A referee's "follows from known results" verdict sends the paper back to positioning before any
  rebuttal sentence is drafted — the reduction must be checked first.

## Output format

```
【Where you are】<stage>
【Use next】jet-<skill>
【Why】<one line tied to JET's theory-first bar>
【Volatile facts checked】editor roster / APC / abstract cap / data statement? [Y/N]
```
