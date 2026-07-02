---
name: jacs-scope-fit
description: Use when deciding whether a chemistry result belongs in the Journal of the American Chemical Society (JACS) versus a specialized ACS journal, and which JACS format fits. Judges fit and venue — it does not improve the chemistry itself.
---

# Scope and Venue Fit (jacs-scope-fit)

## When to trigger

- You are unsure JACS is the right home versus a subfield ACS journal
- A co-author says "this is JACS-level" and you want a sober test
- An editor desk-rejected a prior version for "insufficient general interest"
- You must choose Article vs Communication early

## The JACS bar (broad interest + rigor)

JACS publishes a **significant chemical advance of broad interest across
chemistry**, fully supported by data. Two tests must both pass:

1. **Advance test** — Is the result genuinely new and important, not incremental?
   A new reaction/bond construction, a new mechanism or principle, a new
   material/property, a new method that others will adopt, or a problem long
   considered hard that you solved.
2. **Breadth test** — Will chemists *outside* your immediate subfield care?
   Generality (scope), conceptual insight, or enabling utility are the usual
   sources of breadth.

If only the advance test passes but breadth is narrow, a specialized journal is
the honest fit.

## Venue decision table

| Situation | Likely better venue |
|-----------|---------------------|
| Broad, general-interest advance, fully supported | **JACS** (Article or Communication) |
| Solid methodology, mainly of interest within organic synthesis | *Org. Lett.* / *J. Org. Chem.* |
| Coordination/main-group/bioinorganic, subfield interest | *Inorg. Chem.* |
| Catalysis-focused, mechanism within catalysis community | *ACS Catal.* |
| Materials synthesis/properties, materials audience | *Chem. Mater.* / *ACS Nano* |
| Physical-chemistry measurement, PC audience | *J. Phys. Chem.* family |
| Incremental scope extension of a known reaction | Specialized journal, not JACS |

> Verify current sister-journal scopes on the ACS site; portfolios evolve.

## Format fit (set expectations early)

- **Communication** — a complete, urgent, high-impact advance that can stand on
  concise evidence (full proof lives in the SI). Choose when timeliness and a
  clean central result dominate.
- **Article** — a full account with complete scope, controls, and mechanism.
  Choose when the story needs tables of scope, multiple mechanistic probes, or
  several characterized systems.
- Confirm current article types and limits on the JACS author page; hand sizing
  to `jacs-length-management`.

## Naming the breadth driver (be specific)

Editors triage on whether the manuscript itself argues breadth. Pick one primary
driver and make the abstract carry it:

| Breadth driver | What must be in the data | Example framing |
|----------------|--------------------------|-----------------|
| **Generality** | Scope spanning substrate classes others use daily; failures disclosed | "…across ethers, amines, and three drug scaffolds" |
| **Concept / mechanism** | A principle transferable beyond the system (new elementary step, selectivity model) | "…establishes ligand-controlled distal selectivity as a design rule" |
| **Enabling utility** | Something practitioners can now do (a disconnection, a probe, a material function) | "…renders the C(sp³)–F disconnection strategic in route design" |
| **Long-standing problem** | Documented prior failures by others; your data closing the gap | "…solves the site-selectivity problem posed since [prior art]" |

If you cannot fill the middle column from your own data, the driver is aspirational
— either gather the missing evidence or pivot venue now, before writing.

## Worked micro-example (same chemistry, two pitches)

- **Subfield pitch (belongs at *Org. Lett.*):** "We extend Ni-catalyzed
  hydroamination to six new pyrazole nucleophiles in 61–88% yield."
- **JACS pitch (only if the data back it):** "A single Ni catalyst couples any
  N–H heterocycle class we tested (5 azole families, 31 examples) with
  unactivated olefins, and kinetics reveal why: turnover-limiting olefin
  insertion is insensitive to azole pKa — a generality mechanism, not a scope
  accident."

The second pitch is honest only when the kinetics and the five-family scope
exist. The scope-fit call is therefore a **data audit**, not a wording exercise.

## Desk-rejection signals worth heeding

- Your own abstract needs a subfield term (e.g., a niche ligand class) to state
  why the result matters — the breadth case has not been made.
- The closest peer papers you can cite are all in specialized journals, none in
  JACS from the past few volumes.
- The advance sentence begins "We extend / We also / We further" — extension
  language reads as incremental at a flagship venue.

## Checklist

- [ ] One sentence states the advance in terms a non-specialist chemist grasps
- [ ] The breadth source is named (generality / concept / enabling utility)
- [ ] At least two recent JACS papers in adjacent areas are identified as peers
- [ ] An honest answer to "why not a specialized journal?" is written down
- [ ] The intended format (Article vs Communication) is chosen with a reason
- [ ] No claim of breadth that the data cannot support

## Anti-patterns

- Equating "lots of work" with "broad interest" — effort is not significance
- "First example of X in our hands" framed as a field-wide first
- Pitching an incremental substrate-scope paper as a conceptual advance
- Choosing Communication when the central claim actually needs full Article-level support

## Output format

```
【Advance】one-sentence statement of the new chemistry
【Breadth source】generality / concept / enabling utility
【Verdict】JACS-fit / better at <named ACS journal>
【Format】Article / Communication (+ reason)
【Next】jacs-results-framing (if JACS-fit) or pivot venue
```

## Related resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — characterization platforms and deposition services
