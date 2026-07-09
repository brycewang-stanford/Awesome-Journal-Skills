---
name: ecai-supplementary
description: Use when deciding what goes in the ECAI 7-page body versus the anonymized supplement — splitting content by decision-criticality so nothing a reviewer needs to judge the paper lives outside the tight body, given there is no unlimited in-paper appendix and no separate artifact track.
---

# ECAI Supplementary Material

ECAI's defining constraint is the **7-page body** (references are the only overflow: 1 page in a
standalone ECAI, 2 pages in IJCAI-ECAI 2026). There is **no unlimited in-paper appendix**: the
paper is exactly its 7 pages plus references. A separate **supplement** can carry proofs, extra
tables, and code — but it is optional reading for reviewers, so the split must be made by
**decision-criticality**, not convenience.

## The one rule

> **Anything a reviewer needs in order to judge the paper must be in the 7-page body.**
> The supplement holds *support and detail*, never the claim, the core argument, or the key
> evidence.

Reviewers may or may not open the supplement, and they read it under time pressure. If your central
result only becomes convincing after page 7, the paper is under-argued.

## Belongs in the body (7 pages)

- The **problem statement, contribution, and the claim** in precise form.
- The **core of the argument**: the main theorem statement and proof idea, or the main experimental
  result with the comparison that supports the claim.
- The **key table/figure** a reviewer uses to decide, with enough of the protocol to trust it.
- Threats/limitations that bear on whether the claim holds.

## Belongs in the supplement (anonymized)

- **Full proofs** the body sketches (typical for KR/theory/argumentation/planning work).
- **Additional experiments, ablations, and per-domain/per-dataset breakdowns** beyond the headline.
- **Code, domain files, seeds, configs, and cached outputs** (`ecai-reproducibility`).
- **Extended related-work discussion** that does not fit the reference budget.
- **Hyperparameter grids, dataset statistics, and preprocessing details.**

## The decision-criticality test

For each block ask: *"If a reviewer skipped this, could they still fairly judge the contribution?"*

- **No** → it is decision-critical → keep it in the body, compress elsewhere to fit.
- **Yes** → it supports/details the claim → supplement.

A frequent ECAI mistake is exiling the **proof idea** or the **baseline comparison** to the
supplement to save space. Those are decision-critical; cut prose, merge figures, or tighten
notation instead.

## Compression tactics before you exile content

The tension is real at 7 pages. Recover space *editorially* before demoting anything critical:

- Merge related figures; use one multi-panel figure instead of three.
- State lemmas compactly; move only routine proof steps to the supplement, keep the idea in-body.
- Cut roadmap/signposting sentences; the body is too short to preview itself section by section.
- Tighten related work to *delta-first* positioning (`ecai-related-work`).
- Move verbose hyperparameter tables out; keep the one setting that matters in the text.

## Double-blind and anonymity

The supplement is read under **double-blind** review — anonymize it exactly as the PDF (strip
repository owners, institution and funding lines, system names). A de-anonymizing supplement risks
a summary reject (`ecai-submission`, `ecai-reproducibility`).

## Format and mechanics (verify per cycle)

- Confirm on the current call **whether and how** a supplement is submitted (a separate file/archive
  vs. an appendix mechanism), the **size limit**, and whether reviewers are told it is optional.
  These differ between a standalone ECAI and the joint IJCAI-ECAI 2026 — treat as **待核实** until
  the call confirms.
- Do **not** use the reference pages as a spillover for body text; they are for references (plus, in
  2026, an optional ethics statement).

## Output format

```text
[Body budget] 7 pages; decision-critical content all inside? yes/no
[In body] problem, contribution, main theorem/idea or main result + supporting table
[In supplement] full proofs / extra experiments / code+data / extended related work
[Criticality check] anything decision-critical currently outside the body? <list -> move in>
[Anonymity] supplement clean / leaks: <where>
[Mechanics] supplement format/size per current call confirmed (待核实 if not)
```
