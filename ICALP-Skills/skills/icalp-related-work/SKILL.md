---
name: icalp-related-work
description: Use when writing the related-work and positioning of an ICALP (EATCS) theory paper — comparing against the best known bounds in the TCS literature, crediting the right prior venues (STOC/FOCS/SODA/LICS/CCC and TCS journals), stating the delta precisely, and keeping self-citations third-person under lightweight double-blind.
---

# ICALP Related Work

At ICALP, related work is where you prove your result is **new and better**, not where you list
adjacent papers. A theory referee arrives already knowing the best bound for your problem; your job is
to state **exactly how your result compares** and to credit the lineage correctly. Vague or missing
positioning is a top rejection cause even for correct proofs.

## The comparison is the point

- Name the **best known prior bound** for your exact problem and setting, and state your improvement in
  the same sentence. "Prior work achieved X under assumption A; we achieve Y, removing A" is the
  contract.
- If your result is **incomparable** to prior work (different regime, different parameter), say so
  explicitly and give the reader the axis of comparison — do not let them assume you missed a stronger
  result.
- Distinguish **unconditional** from **conditional** results (and which assumption: SETH, 3SUM, APSP,
  etc.). A conditional lower bound compared against an unconditional one is a category error referees
  catch instantly.

## Cover the right literature lanes

For a Track A paper, the lanes are typically: the **algorithmic** line (best upper bounds), the
**hardness** line (matching or conditional lower bounds), and the **model/parameter** line (dynamic,
parallel, streaming, parameterized). For a Track B paper: the **expressiveness** line, the
**decidability/complexity** line, and the **prior characterizations** of the class. Miss a lane and a
referee who works in it reads you as unaware.

## Credit the right venues

TCS results scatter across venues and journals; attribute them correctly:

- Conference origins: **STOC, FOCS, SODA, ICALP, LICS, CCC, SoCG, CONCUR, ...** — cite the venue and
  year that established the result you compare against.
- **Journal versions matter.** Many TCS results have a definitive journal version (JACM, SICOMP,
  TALG, TCS, LMCS) with the full proof and the tightest bound; cite it when it is the version of
  record for the bound you claim to beat.
- Do not misattribute a famous result to ICALP because it "feels" like a Track A/B result — check
  dblp for the actual venue (see `resources/exemplars/library.md` for sibling-venue traps like the
  PCP theorem at FOCS, or AKS in the *Annals*).

## Lightweight double-blind self-citation

Under ICALP's lightweight double-blind, your own prior work must be cited in the **third person**:

- Not "in our previous paper [12] we showed" but "**it was shown in [12] that**".
- Keep the citation in the bibliography; do not remove your own relevant work (that itself signals
  authorship and weakens positioning) — just phrase it neutrally.
- Do not cite "our full version on arXiv" in a way that de-anonymizes; refer to "the full version"
  without the identifying handle during review.

## Positioning patterns that work

```text
[Delta-first]     "The best known bound for P is B [ref]. We improve this to B', and show B' is
                  optimal under <assumption> (Thm 2)."
[Barrier-named]   "Prior approaches were limited by <obstruction>; we bypass it via <technique>."
[Regime-split]    "For dense inputs [ref] is best; our result is the first improvement in the sparse
                  regime."
[Characterization] "Earlier work classified <subclass>; we complete the picture with a full
                  dichotomy over the whole family."
```

## Anti-patterns

- **A related-work paragraph that only lists titles** with no comparison of bounds.
- **Omitting the matching lower bound literature** so the reader cannot judge tightness.
- **Claiming novelty against a weaker prior bound** while a stronger one exists (the referee knows it).
- **First-person self-citation** that breaks the blind.
- **Attributing a result to the wrong venue** because a coauthor or technique is familiar.

## Output format

```text
[Best prior bound] <named result, venue/journal, the exact quantity>
[Our delta] <improvement, conditional/unconditional, regime>
[Lanes covered] algorithmic / hardness / model — or expressiveness / complexity / characterization
[Attribution check] venues verified on dblp? journal versions cited where they are the record?
[Anonymity] self-citations third-person? full version referenced without de-anonymizing?
[Fix queue] <ordered positioning edits>
```
