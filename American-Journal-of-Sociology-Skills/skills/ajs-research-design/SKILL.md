---
name: ajs-research-design
description: Use when defending the research design of an American Journal of Sociology (AJS) manuscript on its own methodological terms — quantitative, comparative-historical, ethnographic, network, or formal. AJS judges each kind of work by the standards of its tradition; the design must support the theoretical claim. Defends the design; it does not run the analysis.
---

# Research Design (ajs-research-design)

AJS is method-pluralist: it publishes leading quantitative, **comparative-historical**, ethnographic,
network, and formal work, and it judges each by the standards of *its own tradition*. The job here is
to make the design defensible to a generalist, possibly cross-method, double-blind reviewer — and to
show the design actually supports the theoretical claim from `ajs-theory-building`.

## When to trigger

- Choosing or justifying the design before data collection or analysis
- A reader questioned identification, case selection, sampling, or evidentiary warrant
- Aligning the design with the mechanism and observable implications
- Mixed-methods work that must defend each component on its own terms

## Defend the design (by tradition)

### Quantitative / observational
- State the **estimand** and the **identifying assumptions** plainly; AJS rewards honesty over false
  precision. Where the design is descriptive or associational, say so and theorize accordingly.
- Justify sample, measurement, and model; pre-empt confounding and selection.

### Comparative-historical
- Make **case selection** and the **comparative logic** explicit (most-similar / most-different,
  typical / deviant, scope of the comparison).
- Keep a clear **evidentiary trail** from primary sources to claims; treat sequence and conjuncture as
  evidence, not decoration.

### Ethnographic / interview
- Describe **access, site/case selection, duration, and positionality**; justify why this case bears
  the theoretical weight.
- Make the **link from fieldnotes/transcripts to claims** legible (without exposing informants).

### Network / computational
- Justify **boundary specification, tie definition, and missingness**; match the model (e.g., ERGM,
  SAOM) to the relational question.

### Formal
- Tie assumptions to the substantive setting; specify what empirical patterns would corroborate or
  challenge the model.

## Match design to claim

The single most common AJS reviewer objection: **the design cannot bear the theoretical claim.** Walk
the chain: claim → mechanism → observable implication → the design's leverage on it. If a step is
weak, tighten the claim or strengthen the design — do not overclaim.

## Anti-patterns

- Borrowing a quantitative identification template for work that is interpretive or comparative
- Case selection that quietly guarantees the result (selecting on the outcome without acknowledging it)
- Ethnography that asserts representativeness it cannot support
- Overclaiming causality from an associational design
- A design that tests something adjacent to, but not, the stated theoretical claim

## Output format

```
【Tradition】quantitative / comparative-historical / ethnographic / network / formal / mixed
【Claim it must support】from theory-building
【Design leverage】how this design bears on the claim
【Key assumptions / threats】identification, selection, access, boundary, etc.
【Evidentiary trail】sources → claims is legible? [Y/N]
【Verdict】supports the claim / needs tightening / overclaims (fix)
【Next】ajs-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — design and method tooling by tradition
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — AJS method-pluralism and reviewer-matching policy
