---
name: cc-scope-fit
description: Use when deciding whether a molecular / translational oncology study belongs in Cancer Cell (Cell Press) before investing in full submission. Diagnoses mechanism + translational-relevance fit; it does not design experiments or edit prose.
---

# Scope Fit (cc-scope-fit)

## When to trigger

- Starting a project and unsure if Cancer Cell is the right venue
- A reviewer or PI says "this feels incremental" or "too descriptive"
- Considering a Cell Press presubmission inquiry
- Deciding between Cancer Cell and a broader-scope or specialty journal

## What Cancer Cell wants

Cancer Cell publishes mechanistic, hypothesis-driven cancer biology and translational oncology. The recurring acceptance pattern combines **two pillars**:

1. **Mechanistic depth** — a defined molecular mechanism (a pathway, regulatory axis, genetic/epigenetic event, or cell-cell interaction), not just a phenotype or a correlation.
2. **Translational relevance** — the mechanism matters for human cancer: it is anchored in patient data, predicts a vulnerability, or motivates a therapeutic / biomarker strategy.

In-scope topics include tumor biology and signaling, cancer genetics / genomics, the tumor microenvironment, immuno-oncology, metastasis, therapy resistance, and clinical-translational studies that carry mechanistic insight.

## Fit decision table

| Signal in the manuscript                                              | Fit verdict                          |
|-----------------------------------------------------------------------|--------------------------------------|
| Clear mechanism + validated in cells, in vivo, AND human/patient data | Strong fit                            |
| Mechanism + in vivo, human data is associative but supportive         | Likely fit — strengthen human anchor |
| Mechanism only in cell lines, no in vivo, no human relevance          | Off-fit — go back to `cc-study-design` |
| Descriptive omics / atlas with no mechanism or vulnerability          | Off-fit unless reframed around a mechanism |
| Strong clinical correlation but no mechanism                          | Off-fit — likely a specialty / clinical journal |
| Methods / tool paper without a cancer-biology discovery               | Off-fit — a methods journal           |
| Therapeutic claim with only in vitro support                          | Premature — needs in vivo / human validation |

## How to position the contribution

- State the **gap** in mechanistic understanding, not just "X is understudied."
- Name the **orthogonal systems** that will close it (cells + in vivo + human).
- Make the **translational hook** explicit and proportionate to the evidence (mechanism → vulnerability → candidate intervention/biomarker).
- Compare to the closest 2–3 prior papers and say precisely what is new (new mechanism, new node, new context, new in vivo proof).

## Presubmission inquiry decision gate

For a borderline paper, reduce the decision to three evidence questions before investing in a full
Cancer Cell package:

| Question | Strong answer | Weak answer |
|----------|---------------|-------------|
| Mechanism | The causal molecular axis is perturbed, rescued, and connected to phenotype. | The axis is inferred from correlation or omics enrichment only. |
| Human anchor | Patient samples, clinical dataset, organoid, or translational model supports relevance. | Only immortalized cell-line evidence or an anecdotal clinical correlation. |
| Therapeutic/biomarker logic | The intervention, vulnerability, or stratification claim follows from the mechanism. | Translational language is aspirational and not tested. |

If one column is weak, the best next move is usually `cc-study-design`, not cover-letter polish. If all
three are strong, a presubmission inquiry can emphasize the mechanism, the human anchor, and the exact
delta over the nearest Cancer Cell or Cell Press papers.

## Checklist

- [ ] One sentence states the mechanism (molecule/axis → effect on cancer phenotype)
- [ ] Mechanism is validated in ≥2 orthogonal systems, ideally including human/patient data
- [ ] Translational relevance is explicit and matched to the evidence level
- [ ] Closest prior work is identified; the advance over it is specific
- [ ] The study is hypothesis-driven, not purely descriptive
- [ ] Therapeutic / biomarker claims are backed by in vivo and/or human data
- [ ] If a clinical-trial-style study, mechanism still carries the novelty

## Anti-patterns

- A single-system (cell-line-only) story pitched as a major mechanism
- Descriptive single-cell / genomic atlas with no functional mechanism or vulnerability
- "Therapeutic target" framing with no in vivo efficacy or human evidence
- Overclaiming clinical impact from a correlation
- Repackaging an incremental extension of the lab's prior paper without a new mechanistic node

## Output format

```
【Scope verdict】Strong fit / Likely fit / Off-fit
【Mechanism (1 sentence)】...
【Orthogonal validation present】cells / in vivo / human — list which
【Translational hook】... (and whether evidence supports it)
【Gap vs. closest prior work】...
【Next step】Strengthen via cc-study-design / proceed to cc-study-design / reconsider venue
```
